#!/usr/bin/env python3
"""Create a conservative capability profile from a ComfyUI UI/template workflow.
All inferred controls are candidates until an API-format export is bound and tested.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from comfy_ui_template_inspect import load_json, inspect

def make_profile(path: Path, profile_id: str, source_url: str|None=None):
    r=inspect(load_json(path))
    types={n["node_type"] for n in r["nodes"]}
    names=" ".join(types).lower()
    promoted=[(p.get("label") or p.get("name") or "").lower() for p in r["promoted_inputs"]]
    inputs=" ".join(promoted)
    caps=[]
    if any(k in names for k in ["imagetovideo","imgtovideo","image_to_video"]): caps.append("image_to_video")
    if any(k in names+" "+inputs for k in ["firstlast","first_last","flf","end_image"]): caps.append("first_last_frame")
    if "camera" in names: caps.append("camera_control")
    if "control" in names and "video" in names: caps.append("pose_or_control_video")
    provider_api=any(t.endswith("Api") or "Api" in t for t in types)
    caps.append("provider_api" if provider_api else "local_open_weight")
    candidate=[]
    for p in r["promoted_inputs"]:
        label=(p.get("label") or p.get("name") or "").lower()
        semantic=None
        if "prompt" in label and "negative" not in label: semantic="positive_prompt"
        elif "negative" in label and "prompt" in label: semantic="negative_prompt"
        elif "duration" in label: semantic="duration"
        elif "camera" in label: semantic="camera_control"
        elif "seed" in label: semantic="seed"
        if semantic: candidate.append({"semantic":semantic,"ui_surface":p,"status":"CANDIDATE_ONLY"})
    return {
        "profile_id":profile_id,
        "source":{"kind":"official_or_user_ui_template","path":str(path),"url":source_url,"observed_workflow_json_version":r["workflow_version"]},
        "graph":{"root_node_count":r["root_node_count"],"subgraph_count":r["subgraph_count"],"provenance_counts":r["provenance_counts"]},
        "capabilities":caps,
        "model_dependencies":r["model_dependencies"],
        "asset_references":r["asset_references"],
        "candidate_ui_controls":candidate,
        "verification":{"status":"UI_JSON_INSPECTED","run_verified":False,"api_exported":False,"binding_verified":False,"regression_pass":False},
        "production_ready":False,
        "note":"UI control inference is not an API binding. Export the exact run-verified workflow in API format before automation."
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("workflow_ui_json",type=Path); ap.add_argument("--profile-id",required=True); ap.add_argument("--source-url"); ap.add_argument("--out",type=Path)
    a=ap.parse_args(); p=make_profile(a.workflow_ui_json,a.profile_id,a.source_url); text=json.dumps(p,ensure_ascii=False,indent=2)+"\n"
    if a.out: a.out.write_text(text,encoding="utf-8")
    else: print(text,end="")
if __name__=="__main__": main()
