#!/usr/bin/env python3
"""Map LTX-2 UI semantic-source candidates onto an API-format export.

Assumption checked, never blindly trusted: ComfyUI API export usually preserves UI
node IDs. A binding is emitted only when the same node ID exists and class_type
matches. Constant input resolution is conservative.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Any

SAFE_ROLES = {
    "positive_prompt", "negative_prompt", "source_image", "first_image", "middle_image", "end_image",
    "width", "height", "frame_length", "duration_seconds", "fps", "text_only_mode", "extension_seconds",
    "pose_control", "depth_control", "canny_control", "control_video", "custom_audio", "reference_audio", "source_video",
}

def load(p: Path) -> Any: return json.loads(p.read_text(encoding="utf-8"))
def unwrap_api(x: Any) -> Any: return x.get("prompt") if isinstance(x,dict) and isinstance(x.get("prompt"),dict) else x

def is_link(v: Any, graph: dict[str,Any]) -> bool:
    return isinstance(v,list) and len(v)==2 and str(v[0]) in graph and isinstance(v[1],int)

def candidate_inputs(api_node: dict[str,Any], graph: dict[str,Any], ui_widgets: Any) -> list[tuple[str,Any,str]]:
    consts=[(k,v) for k,v in (api_node.get("inputs") or {}).items() if not is_link(v,graph)]
    widgets=ui_widgets if isinstance(ui_widgets,list) else []
    exact=[]
    for k,v in consts:
        if any(v==w for w in widgets): exact.append((k,v,"exact_widget_match"))
    if exact: return exact
    # Common class-specific safe names, but only when present as constants.
    preferred={
      "CLIPTextEncode":["text"], "LoadImage":["image"], "LoadAudio":["audio"], "VHS_LoadVideo":["video"],
      "INTConstant":["value","int","number"], "PrimitiveFloat":["value","float"], "PrimitiveBoolean":["value","boolean"],
      "RandomNoise":["noise_seed","seed"],
    }.get(api_node.get("class_type"),[])
    by={k:(k,v,"class_preferred_name") for k,v in consts}
    hit=[by[k] for k in preferred if k in by]
    if hit:return hit
    if len(consts)==1:
        k,v=consts[0]; return [(k,v,"single_constant_fallback")]
    return []

def build(cands: dict[str,Any], api: dict[str,Any]) -> dict[str,Any]:
    graph=unwrap_api(api)
    if not isinstance(graph,dict): raise ValueError("API graph must be a node-id keyed object or {'prompt': ...}")
    bindings={}; rejected=[]
    for a in cands.get("anchors",[]):
        for s in a.get("source_candidates",[]):
            role=s.get("role") or a.get("semantic_role")
            if role not in SAFE_ROLES: continue
            nid=str(s.get("node_id")); api_node=graph.get(nid)
            if not isinstance(api_node,dict):
                rejected.append({"role":role,"node_id":nid,"reason":"node_id_missing_in_api"}); continue
            if api_node.get("class_type")!=s.get("type"):
                rejected.append({"role":role,"node_id":nid,"reason":"class_type_mismatch","ui_type":s.get("type"),"api_type":api_node.get("class_type")}); continue
            ins=candidate_inputs(api_node,graph,s.get("widgets_values"))
            if len(ins)!=1:
                rejected.append({"role":role,"node_id":nid,"reason":"constant_input_not_unique","candidates":[x[0] for x in ins]}); continue
            input_name,current,method=ins[0]
            entry={"node_id":nid,"expected_class_type":api_node.get("class_type"),"input":input_name,"observed_value":current,"resolution":method,"verification":"CANDIDATE"}
            if role in bindings:
                # Keep ambiguity explicit instead of silently overwriting.
                prev=bindings.pop(role)
                rejected.append({"role":role,"reason":"multiple_candidates","candidates":[prev,entry]})
            else:
                bindings[role]=entry
    return {
      "schema":"ltx2_ui_api_binding_candidate/v1", "binding_target_format":"api", "production_ready":False,
      "mutable_allowlist":sorted(bindings), "bindings":bindings, "rejected":rejected,
      "next_gate":"Check against target /object_info, assign value types/ranges, compile with topology-preserving compiler, then regression-run the exact workflow.",
    }

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("binding_candidates",type=Path); ap.add_argument("workflow_api",type=Path); ap.add_argument("--out",type=Path)
    a=ap.parse_args(); out=build(load(a.binding_candidates),load(a.workflow_api)); text=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
    if a.out:a.out.write_text(text,encoding="utf-8")
    else:sys.stdout.write(text)
    return 0
if __name__=="__main__": raise SystemExit(main())
