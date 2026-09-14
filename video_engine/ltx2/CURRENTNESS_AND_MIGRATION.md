# Currentness and Migration Policy

## What the Appvikalabs repository represents

The studied repository is a useful snapshot of LTX-2 ComfyUI practice built around extracted LTXV2 model files, GGUF support, KJNodes utilities, two-pass sampling, IC-LoRA controls, audio paths, and several production-task variants.

It is **not frozen as the universal LTX-2 implementation** inside this Skill.

## Why

Current Lightricks `ComfyUI-LTXVideo` documentation now lists a separate LTX-2.3 workflow family, including:

- text/image to video single-stage
- text/image to video distilled two-stage with upsampling
- IC-LoRA depth + human pose + edges
- motion tracking
- HDR
- lipdub
- pixel spatial upscaling
- text-to-audio

The same official source labels LTX-2.0 workflows as older examples. Therefore the source studied here is best treated as a **legacy/community architecture corpus**.

## What is still durable knowledge

These concepts remain valuable even when exact model versions/nodes change:

- choose workflow by capability, not by brand name;
- basic generation is the trunk, specialized controls are branches;
- semantic controls can be discovered from graph organization;
- I2V, keyframe control, IC control, custom audio, V2V, and V2A are different production tasks;
- two-stage upscale is a graph architecture, not merely a checkbox;
- external dependencies must be preflighted against the target runtime;
- API export and exact node contracts are required before automation.

## What must be re-resolved for newer LTX versions

- model checkpoint names
- text-encoder packaging
- VAE/audio-VAE packaging
- LoRA names and conditioning semantics
- upscaler models
- node class types and inputs
- low-VRAM implementation
- current official recommended workflow topology

## Migration behavior

When the user supplies a newer official or locally working LTX workflow:

```text
1. keep the current director/selector semantics
2. ingest new UI workflow
3. derive new semantic anchors/capabilities
4. export API graph
5. rebuild binding
6. preflight /object_info
7. regression-run
8. promote the new local profile
```

Do not rewrite creative planning just because the underlying node graph changed.

## Authority order

For production decisions:

1. user's currently working, regression-tested local workflow
2. current official ComfyUI/Lightricks workflow/documentation
3. maintained extension documentation
4. Appvikalabs/community workflow case study
5. model memory / guesswork
