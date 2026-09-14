#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]; D=Path(__file__).resolve().parent

def mod(path,name):
 s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
if len(sys.argv)!=2: raise SystemExit('usage: run_test.py <real-I2V-Basic.json>')
ui=Path(sys.argv[1]); assert ui.exists()
trace=mod(ROOT/'tools/ltx2_binding_candidates.py','ltx_trace'); mapper=mod(ROOT/'tools/ltx2_ui_to_api_binding.py','ltx_map')
data=json.loads(ui.read_text(encoding='utf-8')); c=trace.build(data)
roles={}
for a in c['anchors']:
 for s in a['source_candidates']:
  roles.setdefault(s['role'],[]).append(s)
def one(role,nid,typ):
 hits=[x for x in roles.get(role,[]) if x['node_id']==nid and x['type']==typ]; assert hits,(role,nid,roles.get(role)); return hits[0]
expected={
 'frame_length':one('frame_length',187,'INTConstant'), 'height':one('height',195,'INTConstant'),
 'width':one('width',194,'INTConstant'), 'positive_prompt':one('positive_prompt',121,'CLIPTextEncode'),
 'negative_prompt':one('negative_prompt',110,'CLIPTextEncode'), 'source_image':one('source_image',167,'LoadImage')}
api=json.loads((D/'fixtures/synthetic_api_pair.json').read_text(encoding='utf-8'))
api['121']['inputs']['text']=expected['positive_prompt']['widgets_values'][0]
r=mapper.build(c,api)
for role,nid in {'frame_length':'187','height':'195','width':'194','positive_prompt':'121','negative_prompt':'110','source_image':'167'}.items():
 assert role in r['bindings'],(role,r['rejected']); assert r['bindings'][role]['node_id']==nid
 assert r['bindings'][role]['verification']=='CANDIDATE'
assert r['production_ready'] is False
print(json.dumps({'status':'PASS','real_ui_source':ui.name,'semantic_sources':{k:v['node_id'] for k,v in expected.items()},'api_pair':'SYNTHETIC_ONLY','production_ready':False},indent=2))
