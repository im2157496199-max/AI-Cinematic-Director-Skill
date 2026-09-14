#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parents[2]
TOOLS=ROOT/'tools'
FIX=ROOT/'tests'/'fixtures'

def run(*args):
    cp=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)
    if cp.returncode:
        print(cp.stdout); print(cp.stderr,file=sys.stderr); raise SystemExit(cp.returncode)
    return cp.stdout

# flat template
out=json.loads(run(TOOLS/'comfy_ui_template_inspect.py', FIX/'ui_template_basic_i2v.json'))
assert out['workflow_version']==0.4
assert out['subgraph_count']==0
assert len(out['model_dependencies'])==1
assert out['asset_references'][0]['filename']=='fixture_start.png'
assert out['provenance_counts']['core']>=4

gate=json.loads(run(TOOLS/'comfy_template_gate.py', FIX/'ui_template_basic_i2v.json'))
assert gate['status']=='PASS_STATIC'

profile=json.loads(run(TOOLS/'comfy_template_profile.py', FIX/'ui_template_basic_i2v.json', '--profile-id','fixture_basic'))
assert 'image_to_video' in profile['capabilities']
assert profile['production_ready'] is False

# subgraph template
sg=json.loads(run(TOOLS/'comfy_ui_template_inspect.py', FIX/'ui_template_subgraph_i2v.json'))
assert sg['subgraph_count']==1
assert any(p['label']=='prompt' for p in sg['promoted_inputs'])
assert any(p['widget']=='length' for p in sg['proxy_widgets'])
assert any(m['declared_by']['namespace'].startswith('subgraph:') for m in sg['model_dependencies'])
assert sg['provenance_counts']['subgraph_instance']==1

gate2=json.loads(run(TOOLS/'comfy_template_gate.py', FIX/'ui_template_subgraph_i2v.json'))
assert gate2['status']=='PASS_STATIC'
assert any('subgraphs present' in w for w in gate2['warnings'])

profile2=json.loads(run(TOOLS/'comfy_template_profile.py', FIX/'ui_template_subgraph_i2v.json', '--profile-id','fixture_subgraph'))
assert 'image_to_video' in profile2['capabilities']
assert any(c['semantic']=='positive_prompt' for c in profile2['candidate_ui_controls'])
assert any(c['semantic']=='duration' for c in profile2['candidate_ui_controls'])
print('T10 PASS: flat + subgraph template inspection/gate/profile')
