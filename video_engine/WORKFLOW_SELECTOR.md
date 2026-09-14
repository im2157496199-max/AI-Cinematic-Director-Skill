# Workflow Selector

The selector chooses a **verified production workflow** when one exists, or a **reference case** when the system is still planning. It must never confuse the two states.

## General decision

1. Approved still + simple motion → basic I2V profile.
2. Designed start + designed end frame → first/last-frame-capable profile.
3. Designed start + critical middle beat + designed end → first/middle/last-capable profile.
4. Explicit controlled pan/zoom/roll → camera-capable profile if available.
5. Explicit pose / trajectory / control video → control-capable profile.
6. Identity-critical recurring protagonist → prefer workflows whose binding exposes reference conditioning in addition to the start image.
7. Existing clip extension → V2V profile, not I2V.
8. Existing clip needing generated Foley → V2A profile, not I2V/T2V.
9. Supplied audio or voice cloning → require the matching audio-capable workflow family.

If no verified profile satisfies the requested capability, output `NO_COMPATIBLE_WORKFLOW`; do not invent nodes.

## Selection state model

```text
DISCOVERED
→ STATIC_STUDY_ONLY
→ LOCAL_RUN_VERIFIED
→ API_EXPORTED
→ BINDING_VERIFIED
→ OBJECT_INFO_PREFLIGHT_PASS
→ REGRESSION_PASS
→ PRODUCTION_READY
```

Community repositories can help at `STATIC_STUDY_ONLY`; they cannot self-promote to production.

## LTX-2 branch

The Appvikalabs repository was deeply studied as a capability corpus. The LTX selector can now reason over:

- I2V / T2V / V2V / V2A
- first-last / first-middle-last keyframes
- pose / canny / depth IC-Control
- custom audio
- voice clone / talking avatar
- GGUF variants
- low-VRAM reference variants
- no-upscale vs two-stage-upscale architecture
- sampler-preview instrumentation

See `video_engine/ltx2/SELECTOR_POLICY.md` and `tools/ltx2_select_profile.py`.

## Minimum-complexity rule

When several workflows satisfy all hard requirements, prefer the smallest verified graph with the fewest unnecessary branches. Do not route a simple approved-still I2V shot through a 160+ node all-in-one control graph just because it is more capable.

## Authority order

1. user's regression-tested local workflow
2. current official ComfyUI / model-author workflow
3. maintained extension workflow
4. community reference case
5. guessed graph from model memory

Model family is selected after creative requirements, hardware/workflow availability, and quality needs are known. The Skill must not force Wan/LTX/Hunyuan merely because an adapter exists.
