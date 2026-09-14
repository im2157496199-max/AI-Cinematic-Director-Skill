#!/usr/bin/env python3
import argparse,json,mimetypes,uuid,urllib.request
from pathlib import Path

def upload(path,base,subfolder='skill_inputs',upload_type='input',overwrite=False):
    p=Path(path); boundary='----ComfySkill'+uuid.uuid4().hex
    parts=[]
    def field(name,value):
        parts.extend([f'--{boundary}\r\n'.encode(),f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),str(value).encode(),b'\r\n'])
    field('type',upload_type); field('subfolder',subfolder); field('overwrite','true' if overwrite else 'false')
    mime=mimetypes.guess_type(p.name)[0] or 'application/octet-stream'
    parts.extend([f'--{boundary}\r\n'.encode(),f'Content-Disposition: form-data; name="image"; filename="{p.name}"\r\n'.encode(),f'Content-Type: {mime}\r\n\r\n'.encode(),p.read_bytes(),b'\r\n',f'--{boundary}--\r\n'.encode()])
    req=urllib.request.Request(base.rstrip('/')+'/upload/image',data=b''.join(parts),headers={'Content-Type':f'multipart/form-data; boundary={boundary}'})
    with urllib.request.urlopen(req,timeout=120) as r: out=json.loads(r.read())
    out['workflow_value']=(out.get('subfolder','').rstrip('/')+'/'+out['name']).lstrip('/') if out.get('subfolder') else out['name']
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('image'); ap.add_argument('--server',default='http://127.0.0.1:8188'); ap.add_argument('--subfolder',default='skill_inputs'); ap.add_argument('--type',default='input'); ap.add_argument('--overwrite',action='store_true'); a=ap.parse_args()
    print(json.dumps(upload(a.image,a.server,a.subfolder,a.type,a.overwrite),ensure_ascii=False,indent=2))
if __name__=='__main__': main()
