#!/usr/bin/env python3
"""Derive semantic binding candidates from an LTX-2 UI workflow.

The Appvikalabs workflows use SetNode/GetNode as semantic buses. This tool traces
backward from Set_* anchors to the nearest user-editable source node. It does not
modify the graph. Use its output only as a candidate map; production bindings
must still be checked against an API-format export and /object_info.
"""
from __future__ import annotations
import argparse, json, sys
from collections import deque
from pathlib import Path
from typing import Any

EDITABLE_TYPES = {
    "CLIPTextEncode", "LoadImage", "LoadAudio", "VHS_LoadVideo",
    "INTConstant", "PrimitiveFloat", "PrimitiveBoolean", "PrimitiveStringMultiline",
    "RandomNoise", "LoraLoaderModelOnly", "UNETLoader", "UnetLoaderGGUF",
    "DualCLIPLoader", "DualCLIPLoaderGGUF", "VAELoader", "VAELoaderKJ",
}

ROLE_MAP = {
    "width": "width", "height": "height", "frames": "frame_length", "fps": "fps",
    "ref_image": "source_image", "start_image": "source_image", "image": "source_image",
    "firstframe": "first_image", "middleframe": "middle_image", "lastframe": "end_image",
    "positive": "positive_prompt", "negative": "negative_prompt",
    "t2v_mode": "text_only_mode", "ext_seconds": "extension_seconds",
    "ref_pose": "pose_control", "ref_depth": "depth_control", "ref_canny": "canny_control",
    "ref_control": "control_video", "org_audio": "custom_audio", "ref_audio": "reference_audio",
    "latent_custom_audio": "custom_audio_latent", "source_video": "source_video",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def link_maps(data: dict[str, Any]):
    by_id = {}
    incoming: dict[int, dict[int, list]] = {}
    for link in data.get("links", []):
        if not isinstance(link, list) or len(link) < 6:
            continue
        lid, origin, origin_slot, target, target_slot, typ = link[:6]
        by_id[lid] = link
        incoming.setdefault(int(target), {})[int(target_slot)] = link
    return by_id, incoming


def node_key(n: dict[str, Any]) -> str | None:
    w = n.get("widgets_values")
    if isinstance(w, list) and w and isinstance(w[0], str):
        return w[0]
    title = n.get("title") or ""
    if title.startswith("Set_"):
        return title[4:].lower()
    return None


def selected_inputs_for_output(node: dict[str, Any], origin_slot: int) -> list[int]:
    """Prefer same-name input for pass-through-like nodes, else all linked inputs."""
    outputs = node.get("outputs") or []
    inputs = node.get("inputs") or []
    if 0 <= origin_slot < len(outputs):
        out_name = outputs[origin_slot].get("name")
        if out_name:
            exact = [i for i, inp in enumerate(inputs) if inp.get("name") == out_name and inp.get("link") is not None]
            if exact:
                return exact
    return [i for i, inp in enumerate(inputs) if inp.get("link") is not None]


def trace_sources(data: dict[str, Any], set_node: dict[str, Any], max_depth: int = 10) -> list[dict[str, Any]]:
    nodes = {int(n["id"]): n for n in data.get("nodes", []) if isinstance(n.get("id"), int)}
    by_id, incoming = link_maps(data)
    start_inputs = [i for i, inp in enumerate(set_node.get("inputs") or []) if inp.get("link") is not None]
    q = deque()
    for slot in start_inputs:
        link = incoming.get(int(set_node["id"]), {}).get(slot)
        if link:
            q.append((int(link[1]), int(link[2]), 1, [int(set_node["id"])]))
    seen = set(); found = []
    while q:
        nid, out_slot, depth, path = q.popleft()
        token = (nid, out_slot)
        if token in seen or depth > max_depth:
            continue
        seen.add(token)
        n = nodes.get(nid)
        if not n:
            continue
        if n.get("type") in EDITABLE_TYPES:
            found.append({
                "node_id": nid,
                "type": n.get("type"),
                "title": n.get("title"),
                "widgets_values": n.get("widgets_values"),
                "depth": depth,
                "path": [nid] + path,
            })
            continue
        for input_slot in selected_inputs_for_output(n, out_slot):
            link = incoming.get(nid, {}).get(input_slot)
            if link:
                q.append((int(link[1]), int(link[2]), depth + 1, [nid] + path))
    found.sort(key=lambda x: (x["depth"], x["node_id"]))
    return found


def classify_source(anchor_key: str, source: dict[str, Any]) -> str:
    title = (source.get("title") or "").lower()
    typ = source.get("type")
    if anchor_key == "frames":
        if "seconds" in title:
            return "duration_seconds"
        if "frame" in title:
            return "frame_length"
    if anchor_key == "fps" or title == "fps":
        return "fps"
    return ROLE_MAP.get(anchor_key, anchor_key)


def build(data: dict[str, Any]) -> dict[str, Any]:
    anchors = []
    for n in data.get("nodes", []):
        if n.get("type") != "SetNode":
            continue
        key = node_key(n)
        if not key:
            continue
        srcs = trace_sources(data, n)
        for s in srcs:
            s["role"] = classify_source(key, s)
        anchors.append({
            "set_node_id": n.get("id"),
            "set_title": n.get("title"),
            "semantic_key": key,
            "semantic_role": ROLE_MAP.get(key, key),
            "source_candidates": srcs,
            "status": "CANDIDATE_ONLY",
        })
    return {
        "schema": "ltx2_binding_candidates/v1",
        "workflow_id": data.get("id"),
        "workflow_format_version": data.get("version"),
        "anchors": anchors,
        "production_rule": "Convert candidates to API bindings only after matching the same node IDs/types in an Export Workflow (API) graph and checking /object_info.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("workflow_ui", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    out = build(load(args.workflow_ui))
    text = json.dumps(out, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
