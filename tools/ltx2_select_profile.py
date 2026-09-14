#!/usr/bin/env python3
"""Select an LTX-2 community workflow *reference case* from a derived catalog.

This selector is planning-only. It never marks a community UI workflow as production
ready. Production requires a user-run verified workflow, API export, binding, and
/object_info preflight.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Any


def load(p: Path) -> Any:
    return json.loads(p.read_text(encoding="utf-8"))


def required_caps(req: dict[str, Any]) -> set[str]:
    caps = set()
    mode = req.get("mode")
    if mode: caps.add(mode)
    k = req.get("keyframes", "start_only")
    if k == "start_end": caps.add("first_last_frame")
    if k == "start_middle_end": caps.add("first_middle_last_frame")
    for c in req.get("controls", []) or []:
        caps.add(f"{c}_control")
    audio = req.get("audio_mode")
    if audio == "custom": caps.add("custom_audio")
    elif audio == "voice_clone": caps.add("voice_clone")
    elif audio == "foley": caps.update({"video_to_audio", "foley"})
    if req.get("low_vram_required"): caps.add("low_vram_variant")
    if req.get("gguf_required"): caps.add("gguf")
    if req.get("sampler_preview_required"): caps.add("sampler_preview")
    if req.get("upscale") == "required": caps.add("two_stage_upscale")
    if req.get("upscale") == "forbidden": caps.add("single_stage_no_upscale")
    return caps


def score(w: dict[str, Any], req: dict[str, Any]) -> tuple[float, list[str]]:
    caps = set(w.get("capabilities", [])); reasons=[]; s=0.0
    required = required_caps(req)
    missing = sorted(required - caps)
    if missing:
        return -1e9, ["missing:" + ",".join(missing)]
    s += 100 * len(required)
    mode = req.get("mode")
    name = w.get("source_file", "").lower()
    if mode == "image_to_video" and "i2v" in name: s += 20
    if mode == "text_to_video" and "t2v" in name: s += 20
    if mode == "video_to_video" and "v2v" in name: s += 30
    if mode == "video_to_audio" and ("v2a" in name or "foley" in name): s += 30
    upscale = req.get("upscale", "prefer")
    if upscale == "prefer" and "two_stage_upscale" in caps: s += 12
    if upscale == "avoid" and "single_stage_no_upscale" in caps: s += 12
    if req.get("gguf_preferred") and "gguf" in caps: s += 8
    if req.get("low_vram_preferred") and "low_vram_variant" in caps: s += 15
    # Prefer narrower/simpler cases when equally capable.
    s -= 0.05 * float(w.get("node_count", 0))
    extras = caps - required
    if "voice_clone" in extras and req.get("audio_mode") != "voice_clone": s -= 20
    if "ic_control" in extras and not req.get("controls"): s -= 10
    if "sampler_preview" in extras and not req.get("sampler_preview_required"): s -= 3
    reasons.append(f"required_caps={sorted(required)}")
    reasons.append(f"node_count={w.get('node_count')}")
    return s, reasons


def select(catalog: dict[str, Any], req: dict[str, Any]) -> dict[str, Any]:
    ranked=[]
    for w in catalog.get("workflows", []):
        s, rs = score(w, req)
        if s > -1e8:
            ranked.append((s, w, rs))
    ranked.sort(key=lambda x: (-x[0], x[1].get("node_count", 10**9), x[1].get("source_file", "")))
    if not ranked:
        return {"status":"NO_COMPATIBLE_REFERENCE_CASE", "requirements":req, "required_capabilities":sorted(required_caps(req))}
    top=ranked[0]
    return {
        "status":"REFERENCE_CASE_SELECTED",
        "production_ready":False,
        "requirements":req,
        "required_capabilities":sorted(required_caps(req)),
        "selected": {
            "source_file":top[1]["source_file"], "sha256":top[1]["sha256"],
            "capabilities":top[1]["capabilities"], "node_count":top[1]["node_count"], "score":round(top[0],3),
        },
        "alternatives":[{"source_file":w[1]["source_file"],"score":round(w[0],3),"node_count":w[1]["node_count"]} for w in ranked[1:5]],
        "next_gate":"User/local workflow must run successfully -> Export Workflow (API) -> binding -> /object_info -> regression run.",
    }


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("catalog",type=Path); ap.add_argument("requirements",type=Path); ap.add_argument("--out",type=Path)
    a=ap.parse_args(); result=select(load(a.catalog),load(a.requirements)); text=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if a.out:a.out.write_text(text,encoding="utf-8")
    else:sys.stdout.write(text)
    return 0 if result["status"]=="REFERENCE_CASE_SELECTED" else 3

if __name__=="__main__": raise SystemExit(main())
