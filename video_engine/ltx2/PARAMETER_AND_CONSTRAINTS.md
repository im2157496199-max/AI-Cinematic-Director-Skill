# Parameter and Constraint Study

This file distinguishes **source-observed facts** from **safe production rules**. The distinction matters because several repository notes are advisory and some examples do not perfectly match the note wording.

## 1. Frame-count pattern

Many studied workflows use frame counts such as `121` and `241`, and several calculator nodes explicitly compute a value equivalent to:

```text
1 + 8 * round(duration_seconds * fps / 8)
```

This is strong evidence that **8n+1 frame counts are a recurring Appvikalabs/LTX-2.0-era pattern**.

However, custom-audio examples contain different literal frame values and derive frame length from audio duration. Therefore the current system does **not** globally force every LTX workflow to 8n+1. Instead:

- if the verified workflow exposes a duration→frame calculator, preserve that workflow logic;
- if the verified workflow exposes a literal frame-count control, bind the literal control and validate against that workflow's tested behavior;
- never replace a workflow's own frame logic merely because another LTX graph uses 8n+1.

## 2. Width/height note is not promoted to a universal validator

The source repeatedly contains a note roughly saying width/height should be divisible by 32 and frames should follow an 8n+1-like rule. But the actual workflows use example dimensions including `1280×720`, `1280×704`, `960×544`, and `704×1280`.

Because these observed examples are not fully consistent with a naive “both dimensions divisible by 32” rule, the current system treats the note as **source guidance**, not a hard global constraint.

Production rule:

> dimension validity comes from the exact verified workflow and target runtime, not from a copied generic divisibility formula.

## 3. Resolution tiers observed

Examples in the repository include:

- `1280×720` / `720×1280` — common nominal 720p-like output target
- `1280×704` / `704×1280` — alternate model-friendly dimensions
- `960×544` — explicitly used in a low-VRAM T2V workflow
- notes also suggest `832×480` or `960×544` when memory is limited

These are **examples**, not guaranteed hardware-fit promises.

## 4. FPS

Observed controls commonly use `24` or `25` FPS. One source note suggests 24/25 normally, with 48/50 only when the system can handle it.

Production rule:

- default to the shot/sequence FPS;
- preserve exact workflow timing logic;
- do not increase FPS as a quality knob without accounting for proportional frame count and compute cost.

## 5. Two-stage sampling

Most non-simple workflows follow:

```text
pass 1 → latent upscale → pass 2 → decode
```

This is a graph-level quality architecture, not a single scalar parameter. The Skill must not “turn upscale on” inside a no-upscale graph unless it switches to a different verified profile.

## 6. Distilled vs dev model branches

The source includes both dev/GGUF and distilled model loaders and repeated distilled-LoRA notes. One IC-Control note says that if a dev main model is used without the distilled LoRA in one stage, the distilled LoRA may need enabling in another stage.

Because this behavior is workflow- and model-version-sensitive, the current system records it as a **dependency/branch condition** rather than a general model rule. The exact local graph remains authoritative.

## 7. Prompting guidance observed in source notes

The source repeatedly advises:

1. describe actions/events as they unfold over time;
2. include desired audio/dialogue;
3. avoid redundantly re-describing reference-image details;
4. avoid prompt instructions that conflict with the reference image.

The Skill maps this into director language as:

```text
static appearance lock
→ inherited from approved still/entity sheet

temporal action + camera + sound
→ written into video prompt
```

This prevents the video prompt from fighting the approved still.

## 8. Safe mutation policy

Safe mutable fields are selected from the actual exported API workflow. Typical candidates:

- prompt / negative prompt
- source/keyframe image filenames
- width / height
- duration or frame count
- fps
- seeds
- explicit mode booleans
- explicit control inputs

Model loaders, sampler topology, LoRA chains, VAE/audio-VAE chains, and upscale architecture remain frozen unless the selected **verified profile** explicitly allows them.
