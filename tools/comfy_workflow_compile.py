#!/usr/bin/env python3
"""Safely patch only declared constant inputs in a ComfyUI API-format workflow."""
import json, sys, copy, hashlib
from pathlib import Path
class CompileError(Exception): pass

def load(path): return json.loads(Path(path).read_text(encoding="utf-8"))
def unwrap(w): return w["prompt"] if isinstance(w,dict) and isinstance(w.get("prompt"),dict) else w

def signature(g):
    rows=[]
    for nid in sorted(g,key=str):
        n=g[nid]; ins=[]
        for k,v in sorted(n.get("inputs",{}).items()):
            ins.append((k,"LINK",str(v[0]),v[1]) if isinstance(v,list) and len(v)==2 and str(v[0]) in g and isinstance(v[1],int) else (k,"CONST"))
        rows.append((str(nid),n.get("class_type"),ins))
    return hashlib.sha256(json.dumps(rows,ensure_ascii=False,separators=(",",":")).encode()).hexdigest()

def check_value(key,value,spec):
    t=spec.get("value_type")
    if t=="string" and not isinstance(value,str): raise CompileError(f"{key}: expected string")
    if t=="int" and (not isinstance(value,int) or isinstance(value,bool)): raise CompileError(f"{key}: expected int")
    if t=="float" and not isinstance(value,(int,float)): raise CompileError(f"{key}: expected number")
    if t=="bool" and not isinstance(value,bool): raise CompileError(f"{key}: expected bool")
    if "allowed_values" in spec and spec["allowed_values"] is not None and value not in spec["allowed_values"]: raise CompileError(f"{key}: value not allowed")
    if isinstance(value,(int,float)) and not isinstance(value,bool):
        if spec.get("min") is not None and value < spec["min"]: raise CompileError(f"{key}: below min")
        if spec.get("max") is not None and value > spec["max"]: raise CompileError(f"{key}: above max")
        step=spec.get("step"); base=spec.get("base",0)
        if step and abs(((value-base)/step)-round((value-base)/step))>1e-9: raise CompileError(f"{key}: violates step/base")

def compile_graph(workflow,binding,request):
    wrapper=workflow if isinstance(workflow,dict) and isinstance(workflow.get("prompt"),dict) else None
    graph=copy.deepcopy(unwrap(workflow)); before=signature(graph); report=[]
    allow=binding.get("mutable_allowlist")
    for key,value in request.get("values",{}).items():
        if value is None: continue
        if allow is not None and key not in allow: raise CompileError(f"NOT ALLOWLISTED semantic key: {key}")
        spec=binding.get("bindings",{}).get(key)
        if not spec: raise CompileError(f"UNBOUND semantic key: {key}")
        node_id=str(spec.get("node_id"))
        if node_id not in graph: raise CompileError(f"missing node_id {node_id} for {key}")
        node=graph[node_id]; expected=spec.get("expected_class_type")
        if expected and node.get("class_type")!=expected: raise CompileError(f"class_type mismatch for {key}: expected {expected}, got {node.get('class_type')}")
        input_name=spec.get("input")
        if input_name not in node.get("inputs",{}): raise CompileError(f"input {input_name!r} missing on node {node_id} for {key}")
        old=node["inputs"][input_name]
        if isinstance(old,list) and len(old)==2 and str(old[0]) in graph and isinstance(old[1],int): raise CompileError(f"refusing to overwrite linked input {node_id}.{input_name} for {key}")
        check_value(key,value,spec); node["inputs"][input_name]=value
        report.append({"key":key,"node_id":node_id,"input":input_name,"old":old,"new":value})
    after=signature(graph)
    if before!=after: raise CompileError("graph topology/class_type signature changed during scalar patch")
    out=copy.deepcopy(workflow) if wrapper else graph
    if wrapper: out["prompt"]=graph
    return out,{"structure_sha256_before":before,"structure_sha256_after":after,"changes":report}

def main():
    if len(sys.argv)!=5: raise SystemExit("usage: comfy_workflow_compile.py workflow_api.json binding.json request.json output.json")
    wf,b,r,out=map(Path,sys.argv[1:]); compiled,report=compile_graph(load(wf),load(b),load(r))
    out.write_text(json.dumps(compiled,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    out.with_suffix(out.suffix+".report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
