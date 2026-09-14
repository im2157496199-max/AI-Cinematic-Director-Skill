# Deep Study Report — appvikalabs/LTX-2-Workflows

## Scope actually inspected

This build parsed every workflow-like file in the uploaded repository archive that contained a valid ComfyUI UI workflow graph:

- **19 workflows**
- **1,797 nodes** total
- **1,618 links** total
- **177 groups** total
- **84 unique node types**
- **12 non-core `cnr_id` package families** observed

The study was static graph analysis plus source-note extraction. It did **not** execute these third-party workflows on the user's machine.

## Structural findings

### A. The repository is a workflow-family corpus, not one recipe

The files cover four different production modes:

- I2V
- T2V
- V2V extension
- V2A Foley

Within I2V/T2V, the repository then branches by:

- normal vs simple
- GGUF vs non-GGUF
- two-stage upscale vs no-upscale
- native vs custom audio
- voice clone
- keyframe count
- IC-control type
- memory envelope
- sampler-preview instrumentation

This directly supports a capability-driven selector architecture.

### B. Semantic buses are pervasive

A dominant authoring convention is named Set/Get buses. Examples repeated across graphs:

```text
Set_width / Get_width
Set_height / Get_height
Set_frames / Get_frames
Set_fps / Get_fps
Set_positive / Get_positive
Set_negative / Get_negative
Set_ref_image / Get_ref_image
```

Specialized graphs extend the same convention rather than abandoning it:

```text
Set_firstframe / Set_middleframe / Set_lastframe
Set_ref_pose / Set_ref_canny / Set_ref_depth
Set_t2v_mode
Set_ext_seconds
Set_org_audio / Set_ref_audio
```

This is the most important automation insight in the repository: **meaning is encoded in graph organization**, so the Skill can discover candidate controls without memorizing brittle node IDs.

### C. Basic generation uses an AV latent architecture

Across the family, repeated node types include:

- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVEmptyLatentAudio`
- `LTXVAudioVAEDecode`
- `LTXVImgToVideoInplace`
- `LTXVConditioning`

The graph is therefore not “video first, audio pasted later” in many cases. Audio intent is part of the generation architecture.

### D. Two-pass generation is a major recurring pattern

The majority of non-simple workflows visually/group-wise separate:

1. sampler first pass
2. latent upscale
3. sampler second pass
4. tiled decode

This pattern is encoded as a workflow capability in the current system rather than reduced to a single toggle.

### E. Control complexity is incremental

Graph size demonstrates the cost of specialization:

- I2V Simple (no upscale): 46 nodes
- I2V Basic: 85 nodes
- First/Middle/Last: 113 nodes
- I2V IC pose: 125 nodes
- All-in-one pose/canny/depth: 164 nodes

This supports the policy: **choose the least complex graph that satisfies the shot's hard constraints**.

### F. Prompting guidance is temporal, not appearance-heavy

Repeated source notes advise describing events/actions over time, desired audio, and avoiding repetition or contradiction of reference-image details.

The Skill therefore separates:

```text
appearance identity → approved still / entity lock
motion + camera + event + sound → video prompt
```

This is directly compatible with the user's script → storyboard still → approval → I2V production loop.

## Parameter findings that were NOT overgeneralized

### Frame count

The repository strongly exhibits an 8n+1-like pattern in many graphs, including explicit calculators. But custom-audio branches and different graph logic prevent treating it as a universal law.

### Dimensions

A repeated note describes divisibility guidance, but actual examples include 1280×720, 1280×704, and 960×544. Because a naive interpretation conflicts with examples, the current system records the note but does not hard-code a universal dimension validator.

### Model/LoRA branches

Dev, distilled, GGUF, IC-LoRA, camera LoRA, audio, and upscaler branches are preserved as dependency evidence. The Skill does not automatically swap models or LoRAs based on a community example.

## Currentness finding

The studied source points users onward to official ComfyUI and LTX-Video workflows. Current Lightricks documentation has since separated LTX-2.3 workflows from older LTX-2.0 examples. Therefore the current system deliberately classifies Appvikalabs as:

`COMMUNITY_REFERENCE_CASE / LEGACY_ARCHITECTURE_CORPUS`

rather than `CURRENT_OFFICIAL_TEMPLATE`.

## Engineering outcome

The study is converted into four executable layers:

1. **Catalog** — complete derived metadata for all 19 workflows.
2. **Selector** — requirement → reference-case family.
3. **Semantic binding discovery** — Set/Get buses → upstream mutable source nodes.
4. **UI→API candidate mapping** — same-ID/class validation before API binding.

The final execution gate remains the established API execution gate:

`API export → /object_info → allowlist patch → topology signature → run → QA`.
