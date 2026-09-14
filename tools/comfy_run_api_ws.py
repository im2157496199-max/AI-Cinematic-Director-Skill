#!/usr/bin/env python3
"""Run an API-format workflow using the official classic self-hosted pattern: WebSocket + history."""
import argparse,json,time,uuid,urllib.request,urllib.error
from pathlib import Path

def graph_from(path):
    x=json.loads(Path(path).read_text(encoding='utf-8')); return x['prompt'] if isinstance(x,dict) and isinstance(x.get('prompt'),dict) else x

def post_json(url,payload):
    req=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=30) as r: return json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        body=e.read().decode('utf-8','replace')
        raise SystemExit(f'HTTP {e.code}: {body}')

def history(base,pid):
    with urllib.request.urlopen(base.rstrip('/')+'/history/'+pid,timeout=30) as r: return json.loads(r.read())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('workflow'); ap.add_argument('--server',default='http://127.0.0.1:8188'); ap.add_argument('--timeout',type=int,default=900); ap.add_argument('--report'); a=ap.parse_args()
    try: import websocket
    except ImportError: raise SystemExit('websocket-client required: pip install websocket-client')
    base=a.server.rstrip('/'); graph=graph_from(a.workflow); client_id=str(uuid.uuid4()); prompt_id=str(uuid.uuid4())
    wsurl=('wss://' if base.startswith('https://') else 'ws://')+base.split('://',1)[1]+f'/ws?clientId={client_id}'
    ws=websocket.WebSocket(); ws.connect(wsurl,timeout=30)
    accepted=post_json(base+'/prompt',{'prompt':graph,'client_id':client_id,'prompt_id':prompt_id})
    deadline=time.time()+a.timeout; events=[]; status='RUNNING'; exec_error=None
    while time.time()<deadline:
        raw=ws.recv()
        if not isinstance(raw,str): continue
        msg=json.loads(raw); typ=msg.get('type'); data=msg.get('data',{})
        if data.get('prompt_id') not in (None,prompt_id): continue
        events.append({'type':typ,'data':data})
        if typ=='execution_error': status='ERROR'; exec_error=data; break
        if typ=='execution_interrupted': status='INTERRUPTED'; break
        if typ=='execution_success' or (typ=='executing' and data.get('node') is None): status='SUCCESS'; break
    else: status='TIMEOUT'
    ws.close(); hist=history(base,prompt_id) if status in ('SUCCESS','ERROR','INTERRUPTED') else {}
    report={'status':status,'prompt_id':prompt_id,'accepted':accepted,'execution_error':exec_error,'events':events,'history':hist}
    txt=json.dumps(report,ensure_ascii=False,indent=2)+'\n'; print(txt,end='')
    if a.report: Path(a.report).write_text(txt,encoding='utf-8')
    raise SystemExit(0 if status=='SUCCESS' else 2)
if __name__=='__main__': main()
