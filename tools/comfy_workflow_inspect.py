#!/usr/bin/env python3
"""Inspect a ComfyUI API-format workflow and print bindable node inputs."""
import json, sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: comfy_workflow_inspect.py workflow_api.json")

graph=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
if "prompt" in graph and isinstance(graph["prompt"], dict):
    graph=graph["prompt"]
for node_id,node in graph.items():
    if not isinstance(node,dict):
        continue
    print(f"[{node_id}] {node.get('class_type')}")
    for k,v in node.get("inputs",{}).items():
        if isinstance(v,list) and len(v)==2:
            print(f"  {k}: link -> {v[0]}[{v[1]}]")
        else:
            print(f"  {k}: {v!r}")
