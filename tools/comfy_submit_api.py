#!/usr/bin/env python3
"""Submit a compiled ComfyUI API graph to a local ComfyUI server."""
import json, sys, urllib.request
from pathlib import Path

if len(sys.argv) not in (2,3):
    raise SystemExit("usage: comfy_submit_api.py compiled_api.json [http://127.0.0.1:8188]")
url=(sys.argv[2] if len(sys.argv)==3 else "http://127.0.0.1:8188").rstrip("/")
graph=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
if "prompt" not in graph:
    payload={"prompt":graph}
else:
    payload=graph
req=urllib.request.Request(url+"/prompt", data=json.dumps(payload).encode("utf-8"), headers={"Content-Type":"application/json"})
with urllib.request.urlopen(req) as r:
    print(r.read().decode("utf-8"))
