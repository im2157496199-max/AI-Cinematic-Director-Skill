#!/usr/bin/env python3
"""Inspect an Appvikalabs-style LTX-2 ComfyUI workflow repository.

Accepts an extracted directory or a ZIP. It does not execute workflows and does
not claim compatibility with the local ComfyUI runtime. The output is a derived
catalog intended for planning, provenance, dependency review, and later API
binding. Note bodies are not redistributed; only note metadata/hashes are retained.
"""
from __future__ import annotations
import argparse, collections, hashlib, io, json, re, sys, zipfile
from pathlib import Path
from typing import Any, Iterable

MODEL_RE = re.compile(r"\.(?:safetensors|sft|gguf|pt|pth|ckpt|bin)$", re.I)
SKIP_NAMES = {"README.md", ".gitattributes", "LICENSE", "LICENSE.md"}


def _strings(x: Any) -> Iterable[str]:
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for v in x:
            yield from _strings(v)
    elif isinstance(x, dict):
        for v in x.values():
            yield from _strings(v)


def infer_capabilities(name: str, node_types: set[str]) -> list[str]:
    n = name.lower()
    caps: set[str] = set()
    if "i2v" in n or "first last" in n or "first middle last" in n:
        caps.add("image_to_video")
    if "t2v" in n:
        caps.add("text_to_video")
    if "v2v" in n:
        caps.add("video_to_video")
        caps.add("video_extension")
    if "v2a" in n or "foley" in n:
        caps.add("video_to_audio")
        caps.add("foley")
    if "first last" in n:
        caps.add("first_last_frame")
    if "first middle last" in n:
        caps.update({"first_last_frame", "first_middle_last_frame"})
    if "ic-control" in n or "ic control" in n:
        caps.add("ic_control")
    if "pose" in n:
        caps.add("pose_control")
    if "canny" in n:
        caps.add("canny_control")
    if "depth" in n:
        caps.add("depth_control")
    if "custom audio" in n:
        caps.add("custom_audio")
    if "talking avatar" in n:
        caps.update({"talking_avatar", "voice_clone"})
    if "gguf" in n:
        caps.add("gguf")
    if "low vram" in n:
        caps.add("low_vram_variant")
    if "no upscale" in n:
        caps.add("single_stage_no_upscale")
    elif "with upscale" in n or "LatentUpscaleModelLoader" in node_types:
        caps.add("two_stage_upscale")
    if "beta test sampler previews" in n or "LTX2SamplingPreviewOverride" in node_types:
        caps.add("sampler_preview")
    if "LTXVAudioVAEDecode" in node_types or "LTXVAudioVAEEncode" in node_types:
        caps.add("audio_latent_pipeline")
    if "LTXVLoopingSampler" in node_types:
        caps.add("looping_sampler")
    return sorted(caps)


def semantic_anchors(nodes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for n in nodes:
        if n.get("type") != "SetNode":
            continue
        title = n.get("title") or ""
        widgets = n.get("widgets_values")
        key = None
        if isinstance(widgets, list) and widgets and isinstance(widgets[0], str):
            key = widgets[0]
        out.append({"node_id": n.get("id"), "title": title, "semantic_key": key})
    return out


def summarize_workflow(name: str, raw: bytes) -> dict[str, Any] | None:
    try:
        data = json.loads(raw.decode("utf-8"))
    except Exception:
        return None
    if not isinstance(data, dict) or not isinstance(data.get("nodes"), list):
        return None
    nodes = data["nodes"]
    types = collections.Counter(str(n.get("type")) for n in nodes)
    packages: dict[str, set[str]] = collections.defaultdict(set)
    notes = []
    models = set()
    for n in nodes:
        props = n.get("properties") if isinstance(n.get("properties"), dict) else {}
        cnr = props.get("cnr_id")
        if cnr:
            packages[str(cnr)].add(str(props.get("ver")))
        for s in _strings(n.get("widgets_values")):
            if MODEL_RE.search(s):
                models.add(s.replace("\\", "/"))
        if n.get("type") in {"MarkdownNote", "Note"}:
            w = n.get("widgets_values")
            text = w[0] if isinstance(w, list) and w and isinstance(w[0], str) else None
            notes.append({"node_id": n.get("id"), "title": n.get("title"), "char_count": len(text) if text else 0, "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest() if text else None})
    groups = [g.get("title") for g in data.get("groups", []) if isinstance(g, dict)]
    node_types = set(types)
    return {
        "source_file": name,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "workflow_format_version": data.get("version"),
        "node_count": len(nodes),
        "link_count": len(data.get("links", [])),
        "group_count": len(groups),
        "groups": groups,
        "node_types": dict(sorted(types.items())),
        "custom_node_packages": {k: sorted(v) for k, v in sorted(packages.items()) if k != "comfy-core"},
        "models_observed": sorted(models),
        "semantic_anchors": semantic_anchors(nodes),
        "notes": notes,
        "capabilities": infer_capabilities(name, node_types),
    }


def inspect_path(path: Path) -> dict[str, Any]:
    workflows = []
    if path.is_dir():
        base = path
        candidates = [p for p in base.rglob("*") if p.is_file() and p.name not in SKIP_NAMES and not p.name.startswith(".")]
        for p in sorted(candidates):
            item = summarize_workflow(str(p.relative_to(base)), p.read_bytes())
            if item:
                workflows.append(item)
        source_sha = None
    else:
        source_sha = hashlib.sha256(path.read_bytes()).hexdigest()
        with zipfile.ZipFile(path) as z:
            for zi in sorted(z.infolist(), key=lambda x: x.filename):
                if zi.is_dir():
                    continue
                name = zi.filename.rsplit("/", 1)[-1]
                if name in SKIP_NAMES or name.startswith("."):
                    continue
                raw = z.read(zi)
                item = summarize_workflow(zi.filename, raw)
                if item:
                    workflows.append(item)
    all_types = collections.Counter()
    all_packages: dict[str, set[str]] = collections.defaultdict(set)
    for w in workflows:
        all_types.update(w["node_types"])
        for pkg, vers in w["custom_node_packages"].items():
            all_packages[pkg].update(vers)
    return {
        "schema": "ltx2_repo_catalog/v1",
        "source": {"path": str(path), "archive_sha256": source_sha},
        "workflow_count": len(workflows),
        "workflows": workflows,
        "aggregate": {
            "node_types": dict(sorted(all_types.items())),
            "custom_node_packages": {k: sorted(v) for k, v in sorted(all_packages.items())},
        },
        "limits": [
            "This is static UI-workflow inspection, not runtime execution proof.",
            "Repository examples are evidence of author workflow patterns, not universal LTX-2 requirements.",
            "Production execution still requires an API-format export plus target /object_info preflight.",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    cat = inspect_path(args.source)
    text = json.dumps(cat, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    if cat["workflow_count"] == 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
