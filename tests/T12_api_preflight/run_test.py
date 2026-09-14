from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
wf=ROOT/'tests/fixtures/comfy_api_basic_fixture.json'
p=subprocess.run([sys.executable,str(ROOT/'tools/comfy_api_preflight.py'),str(wf),'--object-info',str(HERE/'object_info.json'),'--out',str(HERE/'preflight.json')],capture_output=True,text=True)
assert p.returncode==0,(p.stdout,p.stderr)
r=json.loads((HERE/'preflight.json').read_text()); assert r['ok']
bad=json.loads(wf.read_text())
bad['6']['class_type']='MissingCustomNode'
(HERE/'bad.json').write_text(json.dumps(bad),encoding='utf-8')
p=subprocess.run([sys.executable,str(ROOT/'tools/comfy_api_preflight.py'),str(HERE/'bad.json'),'--object-info',str(HERE/'object_info.json')],capture_output=True,text=True)
assert p.returncode!=0 and 'missing_node_type' in p.stdout
print('T12 PASS: object_info preflight catches runtime node contract mismatch')
