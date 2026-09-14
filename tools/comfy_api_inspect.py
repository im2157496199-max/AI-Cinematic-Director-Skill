#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path

def unwrap(obj):
    return obj['prompt'] if isinstance(obj,dict) and isinstance(obj.get('prompt'),dict) else obj

def structural_signature(graph):
    rows=[]
    for nid in sorted(graph, key=str):
        n=graph[nid]
        ins=[]
        for k,v in sorted(n.get('inputs',{}).items()):
            if isinstance(v,list) and len(v)==2 and str(v[0]) in graph and isinstance(v[1],int):
                ins.append((k,'LINK',str(v[0]),v[1]))
            else:
                ins.append((k,'CONST'))
        rows.append((str(nid),n.get('class_type'),ins))
    raw=json.dumps(rows,ensure_ascii=False,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()

def inspect(obj):
    g=unwrap(obj)
    errors=[]; warnings=[]; links=[]
    if not isinstance(g,dict): return {'ok':False,'errors':['graph is not an object']}
    if 'nodes' in g and isinstance(g.get('nodes'),list):
        return {'ok':False,'errors':['looks like UI/save-format workflow, not API graph']}
    for nid,node in g.items():
        if not isinstance(node,dict): errors.append(f'{nid}: node is not object'); continue
        if not node.get('class_type'): errors.append(f'{nid}: missing class_type')
        if not isinstance(node.get('inputs'),dict): errors.append(f'{nid}: inputs is not object'); continue
        if not str(nid).isdigit(): warnings.append(f'{nid}: non-numeric node id; allowed by some programmatic examples but verify source')
        for name,v in node['inputs'].items():
            if isinstance(v,list) and len(v)==2 and isinstance(v[1],int):
                up=str(v[0])
                if up in g: links.append({'node_id':str(nid),'input':name,'upstream':up,'slot':v[1]})
                elif isinstance(v[0],str): errors.append(f'{nid}.{name}: link references missing node {up}')
    return {'ok':not errors,'node_count':len(g),'link_count':len(links),'class_types':sorted({n.get('class_type') for n in g.values() if isinstance(n,dict) and n.get('class_type')}),'structure_sha256':structural_signature(g) if not errors else None,'links':links,'warnings':warnings,'errors':errors}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('workflow'); ap.add_argument('--out')
    a=ap.parse_args(); obj=json.loads(Path(a.workflow).read_text(encoding='utf-8'))
    r=inspect(obj); txt=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.out: Path(a.out).write_text(txt,encoding='utf-8')
    print(txt,end=''); raise SystemExit(0 if r.get('ok') else 2)
if __name__=='__main__': main()
