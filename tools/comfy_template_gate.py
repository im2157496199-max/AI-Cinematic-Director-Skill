#!/usr/bin/env python3
"""Static gate for ComfyUI UI/template JSON.
PASS means structurally inspectable, NOT run-verified.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from comfy_ui_template_inspect import load_json, inspect

def gate(path: Path):
    errors=[]; warnings=[]
    try: rep=inspect(load_json(path))
    except Exception as e:
        return {"status":"FAIL","errors":[str(e)],"warnings":[],"scope":"static_only"}
    ver=rep.get("workflow_version")
    if ver not in (0.4,1,1.0,None): warnings.append(f"unrecognized workflow version: {ver!r}")
    if ver is None: warnings.append("workflow version missing")
    if rep["root_node_count"]<1: errors.append("no root nodes")
    if rep["provenance_counts"].get("unknown",0):
        warnings.append(f"{rep['provenance_counts']['unknown']} node(s) have unknown provenance metadata")
    if rep["provenance_counts"].get("non_core",0):
        warnings.append(f"{rep['provenance_counts']['non_core']} non-core node(s) declared")
    if rep["subgraph_count"]:
        warnings.append("subgraphs present: API binding must use exported API graph; UI proxy data is discovery-only")
    if rep["asset_references"]:
        warnings.append("input assets referenced: existence is not verified by static gate")
    return {
        "status":"FAIL" if errors else "PASS_STATIC",
        "scope":"static_only",
        "errors":errors,
        "warnings":warnings,
        "summary":{k:rep[k] for k in ("workflow_version","root_node_count","subgraph_count","total_nodes_including_subgraphs","provenance_counts")},
        "model_dependency_count":len(rep["model_dependencies"]),
        "asset_reference_count":len(rep["asset_references"]),
        "explicit_non_claims":["models_exist_on_disk","workflow_runs_successfully","UI_to_API_conversion_complete","production_binding_verified"]
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("workflow_ui_json",type=Path); ap.add_argument("--out",type=Path)
    a=ap.parse_args(); report=gate(a.workflow_ui_json); text=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if a.out: a.out.write_text(text,encoding="utf-8")
    else: print(text,end="")
    if report["status"]=="FAIL": raise SystemExit(2)
if __name__=="__main__": main()
