from pathlib import Path
import json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
out=HERE/'compiled.json'
subprocess.check_call([sys.executable,str(ROOT/'tools/comfy_api_inspect.py'),str(HERE/'basic_api.json'),'--out',str(HERE/'inspect.json')])
subprocess.check_call([sys.executable,str(ROOT/'tools/comfy_workflow_compile.py'),str(HERE/'basic_api.json'),str(HERE/'binding.json'),str(HERE/'request.json'),str(out)])
rep=json.loads((out.with_suffix('.json.report.json')).read_text(encoding='utf-8'))
assert rep['structure_sha256_before']==rep['structure_sha256_after']
assert len(rep['changes'])==3
bad=json.loads((HERE/'binding.json').read_text())
bad['bindings']['break_link']={'node_id':'3','expected_class_type':'KSampler','input':'model'}
bad['mutable_allowlist'].append('break_link')
(HERE/'bad_binding.json').write_text(json.dumps(bad),encoding='utf-8')
(HERE/'bad_request.json').write_text(json.dumps({'values':{'break_link':'oops'}}),encoding='utf-8')
p=subprocess.run([sys.executable,str(ROOT/'tools/comfy_workflow_compile.py'),str(HERE/'basic_api.json'),str(HERE/'bad_binding.json'),str(HERE/'bad_request.json'),str(HERE/'bad.json')],capture_output=True,text=True)
assert p.returncode!=0 and 'refusing to overwrite linked input' in (p.stderr+p.stdout)
print('T11 PASS: API format inspect + allowlist patch + topology invariant + linked-input guard')
