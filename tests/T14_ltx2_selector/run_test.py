#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]; D=Path(__file__).resolve().parent

def mod(path,name):
 s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
sel=mod(ROOT/'tools/ltx2_select_profile.py','ltx2_sel')
cat=json.loads((ROOT/'video_engine/ltx2/catalog/appvikalabs_workflow_catalog.json').read_text(encoding='utf-8'))
expected={
'simple_i2v_no_upscale':'LTX-2 - I2V Simple (no upscale).json',
'start_end':'LTX-2 - First Last Frame (guide node).json',
'start_middle_end':'LTX-2 - First Middle Last Frame (guide node).json',
'pose':'LTX-2 - I2V IC-Control (pose).json',
'pose_canny_depth':'LTX-2 - I2V and T2V IC-Control (All-In-One Pose Canny Depth).json',
'custom_audio_i2v':'LTX-2 - I2V Basic (custom audio).json',
'voice_clone_i2v':'LTX-2 - I2V Talking Avatar (voice clone Qwen-TTS).json',
'v2v':'LTX-2 - V2V (extend any video).json',
'foley':'LTX-2 - V2A Foley (add sound to any video).json',
'low_vram_t2v':'LTX-2 - T2V Basic (low vram).json',
'gguf_i2v':'LTX-2 - I2V Basic (GGUF).json'}
out=[]
for key,exp in expected.items():
 req=json.loads((D/'fixtures'/f'{key}.json').read_text(encoding='utf-8')); r=sel.select(cat,req)
 assert r['status']=='REFERENCE_CASE_SELECTED', (key,r); assert r['production_ready'] is False
 got=Path(r['selected']['source_file']).name; assert got==exp,(key,got,exp,r)
 out.append({'case':key,'selected':got})
print(json.dumps({'status':'PASS','cases':out},ensure_ascii=False,indent=2))
