#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]

def loadmod(path,name):
    spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    if len(sys.argv)!=2: raise SystemExit('usage: run_test.py <source-zip-or-directory>')
    source=Path(sys.argv[1]); assert source.exists(), source
    mod=loadmod(ROOT/'tools/ltx2_repo_inspect.py','ltx2_repo_inspect')
    c=mod.inspect_path(source)
    assert c['workflow_count']==19, c['workflow_count']
    assert sum(w['node_count'] for w in c['workflows'])==1797
    assert sum(w['link_count'] for w in c['workflows'])==1618
    names={Path(w['source_file']).name:w for w in c['workflows']}
    must={
      'LTX-2 - I2V Basic.json': {'image_to_video','two_stage_upscale'},
      'LTX-2 - First Middle Last Frame (guide node).json': {'first_middle_last_frame','image_to_video'},
      'LTX-2 - I2V and T2V IC-Control (All-In-One Pose Canny Depth).json': {'pose_control','canny_control','depth_control'},
      'LTX-2 - V2V (extend any video).json': {'video_to_video'},
      'LTX-2 - V2A Foley (add sound to any video).json': {'video_to_audio','foley'},
    }
    for n,caps in must.items():
        assert n in names,n; assert caps <= set(names[n]['capabilities']), (n,names[n]['capabilities'])
    sha=hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else None
    if source.is_file(): assert sha=='fd99ce019f55525c671b791cad089db86c7d05a60db3d1948e9444c635210638',sha
    print(json.dumps({'status':'PASS','workflow_count':19,'nodes':1797,'links':1618,'source_sha256':sha},indent=2))
if __name__=='__main__': main()
