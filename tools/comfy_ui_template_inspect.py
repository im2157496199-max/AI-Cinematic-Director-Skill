#!/usr/bin/env python3
"""Inspect ComfyUI UI/template workflow JSON, including nested subgraphs.

This intentionally does NOT convert UI workflow JSON to API format.
It extracts provenance, dependency declarations, assets, subgraphs and candidate
control surfaces so a later verified API export can be bound safely.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any, Dict, List, Tuple

CORE_CNR = "comfy-core"
ASSET_NODE_HINTS = {
    "LoadImage": "image", "LoadVideo": "video", "LoadAudio": "audio",
    "VHS_LoadVideo": "video", "VHS_LoadImages": "image"
}

def load_json(path: Path) -> Dict[str, Any]:
    data=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("workflow root must be an object")
    return data

def is_api_graph(data: Dict[str, Any]) -> bool:
    if "nodes" in data:
        return False
    graph=data.get("prompt") if isinstance(data.get("prompt"),dict) else data
    nodes=[v for v in graph.values() if isinstance(v,dict)] if isinstance(graph,dict) else []
    return bool(nodes) and all("class_type" in n for n in nodes[:min(5,len(nodes))])

def subgraph_definitions(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    defs=data.get("definitions") or {}
    out={}
    for sg in defs.get("subgraphs") or []:
        if isinstance(sg,dict) and sg.get("id") is not None:
            out[str(sg["id"])]=sg
    return out

def node_models(node: Dict[str, Any]) -> List[Dict[str, Any]]:
    props=node.get("properties") or {}
    models=props.get("models") or []
    return [m for m in models if isinstance(m,dict)]

def node_provenance(node: Dict[str, Any], sg_ids:set[str]) -> str:
    ntype=str(node.get("type"))
    if ntype in sg_ids:
        return "subgraph_instance"
    cnr=(node.get("properties") or {}).get("cnr_id")
    if cnr == CORE_CNR:
        return "core"
    if cnr:
        return "non_core"
    return "unknown"

def asset_from_node(node: Dict[str, Any]) -> Dict[str, Any] | None:
    ntype=str(node.get("type"))
    kind=ASSET_NODE_HINTS.get(ntype)
    if not kind:
        if "LoadImage" in ntype: kind="image"
        elif "LoadVideo" in ntype: kind="video"
        elif "LoadAudio" in ntype: kind="audio"
    if not kind:
        return None
    vals=node.get("widgets_values") or []
    filename=vals[0] if vals and isinstance(vals[0],str) and vals[0] else None
    return {"kind":kind,"filename":filename,"node_id":node.get("id"),"node_type":ntype}

def inspect(data: Dict[str, Any]) -> Dict[str, Any]:
    if is_api_graph(data):
        raise ValueError("input appears to be API-format JSON; expected UI/template workflow JSON")
    if not isinstance(data.get("nodes"),list):
        raise ValueError("UI workflow requires root nodes[]")
    sgs=subgraph_definitions(data)
    sg_ids=set(sgs)
    records=[]; models=[]; assets=[]; promoted=[]; proxy=[]

    def walk(nodes: List[Dict[str, Any]], namespace: str):
        for node in nodes:
            if not isinstance(node,dict): continue
            ntype=str(node.get("type"))
            nid=str(node.get("id"))
            props=node.get("properties") or {}
            prov=node_provenance(node,sg_ids)
            rec={
                "namespace": namespace,
                "node_id": nid,
                "node_type": ntype,
                "title": node.get("title"),
                "mode": node.get("mode"),
                "provenance": prov,
                "cnr_id": props.get("cnr_id"),
                "node_version": props.get("ver"),
                "input_names": [i.get("name") for i in (node.get("inputs") or []) if isinstance(i,dict)],
            }
            records.append(rec)
            for m in node_models(node):
                mm={k:m.get(k) for k in ("name","url","directory","hash","hash_type") if m.get(k) is not None}
                mm["declared_by"]={"namespace":namespace,"node_id":nid,"node_type":ntype}
                models.append(mm)
            a=asset_from_node(node)
            if a:
                a["namespace"]=namespace; assets.append(a)
            if prov=="subgraph_instance":
                for inp in node.get("inputs") or []:
                    if not isinstance(inp,dict): continue
                    if inp.get("widget") is not None or inp.get("label"):
                        promoted.append({
                            "instance_node_id":nid,
                            "subgraph_id":ntype,
                            "name":inp.get("name"),
                            "label":inp.get("label"),
                            "type":inp.get("type"),
                            "linked":inp.get("link") is not None,
                        })
                for p in props.get("proxyWidgets") or []:
                    if isinstance(p,(list,tuple)) and len(p)>=2:
                        proxy.append({"instance_node_id":nid,"subgraph_id":ntype,"internal_node_id":str(p[0]),"widget":p[1]})

    walk(data["nodes"],"root")
    for sgid,sg in sgs.items():
        walk(sg.get("nodes") or [],f"subgraph:{sgid}")

    prov_counts={}
    for r in records: prov_counts[r["provenance"]]=prov_counts.get(r["provenance"],0)+1
    return {
        "format":"comfyui_ui_workflow",
        "workflow_id":data.get("id"),
        "workflow_version":data.get("version"),
        "revision":data.get("revision"),
        "frontend_version":((data.get("extra") or {}).get("frontendVersion")),
        "root_node_count":len(data["nodes"]),
        "subgraph_count":len(sgs),
        "total_nodes_including_subgraphs":len(records),
        "provenance_counts":prov_counts,
        "nodes":records,
        "model_dependencies":models,
        "asset_references":assets,
        "promoted_inputs":promoted,
        "proxy_widgets":proxy,
        "subgraphs":[{"id":sgid,"name":sg.get("name"),"node_count":len(sg.get("nodes") or [])} for sgid,sg in sgs.items()],
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("workflow_ui_json",type=Path)
    ap.add_argument("--out",type=Path)
    args=ap.parse_args()
    report=inspect(load_json(args.workflow_ui_json))
    text=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.out: args.out.write_text(text,encoding="utf-8")
    else: print(text,end="")

if __name__=="__main__": main()
