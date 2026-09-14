#!/usr/bin/env python3
import argparse,json,urllib.request
from pathlib import Path

def load_graph(p):
    x=json.loads(Path(p).read_text(encoding='utf-8')); return x['prompt'] if isinstance(x,dict) and isinstance(x.get('prompt'),dict) else x

def get_info(base):
    with urllib.request.urlopen(base.rstrip('/')+'/object_info',timeout=20) as r: return json.loads(r.read())

def schema_inputs(info):
    i=info.get('input',{}); return {**i.get('required',{}),**i.get('optional',{})}, set(i.get('required',{}))

def validate(graph, infos):
    errors=[]; warnings=[]
    for nid,n in graph.items():
        ct=n.get('class_type'); ins=n.get('inputs',{})
        if ct not in infos:
            errors.append({'node_id':str(nid),'class_type':ct,'type':'missing_node_type'}); continue
        defs,req=schema_inputs(infos[ct])
        for x in req:
            if x not in ins: errors.append({'node_id':str(nid),'class_type':ct,'type':'required_input_missing','input':x})
        for x,v in ins.items():
            if x not in defs:
                warnings.append({'node_id':str(nid),'class_type':ct,'type':'unknown_explicit_input','input':x}); continue
            if isinstance(v,list) and len(v)==2 and str(v[0]) in graph and isinstance(v[1],int):
                up=str(v[0]); slot=v[1]; uct=graph[up].get('class_type')
                outs=infos.get(uct,{}).get('output',[])
                if slot<0 or slot>=len(outs): errors.append({'node_id':str(nid),'input':x,'type':'bad_output_slot','upstream':up,'slot':slot})
            else:
                spec=defs[x]
                if isinstance(spec,list) and spec and isinstance(spec[0],list) and v not in spec[0]:
                    errors.append({'node_id':str(nid),'input':x,'type':'value_not_in_enum','value':v})
    return {'ok':not errors,'errors':errors,'warnings':warnings}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('workflow'); g=ap.add_mutually_exclusive_group(required=True); g.add_argument('--server'); g.add_argument('--object-info'); ap.add_argument('--dump-object-info'); ap.add_argument('--out')
    a=ap.parse_args(); graph=load_graph(a.workflow)
    infos=get_info(a.server) if a.server else json.loads(Path(a.object_info).read_text(encoding='utf-8'))
    if a.dump_object_info: Path(a.dump_object_info).write_text(json.dumps(infos,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    r=validate(graph,infos); txt=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.out: Path(a.out).write_text(txt,encoding='utf-8')
    print(txt,end=''); raise SystemExit(0 if r['ok'] else 2)
if __name__=='__main__': main()
