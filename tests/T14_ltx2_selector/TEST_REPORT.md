# T14 TEST REPORT — PASS

11 routing cases were checked against the derived 19-workflow catalog. Every result remained `production_ready=false`.

```json
{
  "status": "PASS",
  "cases": [
    {
      "case": "simple_i2v_no_upscale",
      "selected": "LTX-2 - I2V Simple (no upscale).json"
    },
    {
      "case": "start_end",
      "selected": "LTX-2 - First Last Frame (guide node).json"
    },
    {
      "case": "start_middle_end",
      "selected": "LTX-2 - First Middle Last Frame (guide node).json"
    },
    {
      "case": "pose",
      "selected": "LTX-2 - I2V IC-Control (pose).json"
    },
    {
      "case": "pose_canny_depth",
      "selected": "LTX-2 - I2V and T2V IC-Control (All-In-One Pose Canny Depth).json"
    },
    {
      "case": "custom_audio_i2v",
      "selected": "LTX-2 - I2V Basic (custom audio).json"
    },
    {
      "case": "voice_clone_i2v",
      "selected": "LTX-2 - I2V Talking Avatar (voice clone Qwen-TTS).json"
    },
    {
      "case": "v2v",
      "selected": "LTX-2 - V2V (extend any video).json"
    },
    {
      "case": "foley",
      "selected": "LTX-2 - V2A Foley (add sound to any video).json"
    },
    {
      "case": "low_vram_t2v",
      "selected": "LTX-2 - T2V Basic (low vram).json"
    },
    {
      "case": "gguf_i2v",
      "selected": "LTX-2 - I2V Basic (GGUF).json"
    }
  ]
}
```
