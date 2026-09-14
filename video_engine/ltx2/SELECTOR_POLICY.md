# LTX-2 Selector Policy

The selector translates **director requirements** into a workflow family. It does not decide from model fashion or from whichever JSON happens to be available.

## Required input

The minimum planning contract is:

```yaml
mode: image_to_video | text_to_video | video_to_video | video_to_audio
keyframes: start_only | start_end | start_middle_end
controls: []               # pose | canny | depth
audio_mode: native         # native | custom | voice_clone | foley | none
upscale: prefer            # required | prefer | avoid | forbidden
gguf_required: false
low_vram_required: false
sampler_preview_required: false
```

## Decision order

1. **Choose generation mode**: I2V, T2V, V2V, or V2A.
2. **Escalate keyframe control only when needed**:
   - start only → basic I2V
   - start + end → first/last family
   - start + middle + end → first/middle/last family
3. **Escalate structure control only when needed**:
   - pose only → pose IC-Control
   - pose/canny/depth mix → all-in-one IC-Control reference family
4. **Choose audio behavior**:
   - native model audio → keep normal AV latent path
   - user-supplied soundtrack/dialogue → custom-audio family
   - cloned voice → talking-avatar family
   - sound generation from an existing clip → V2A Foley
5. **Choose execution envelope**:
   - low-VRAM requirement → only a workflow explicitly designed/tested for that envelope may satisfy it
   - GGUF requirement → select a GGUF family; do not replace the loader inside an already verified graph unless the workflow is revalidated
6. **Choose quality path**:
   - two-stage upscale is preferred when the selected family supports it and the runtime can afford it
   - no-upscale is a separate reference case, not a scalar toggle
7. Among equally capable cases, prefer the **smallest graph** and fewest optional branches.

## Examples

```text
Approved still + gentle head turn
→ I2V Simple / I2V Basic reference family

Approved first and end poses are both art-directed
→ First Last Frame family

Critical mid-action pose must also land exactly
→ First Middle Last Frame family

Approved still + exact body choreography from a control clip
→ I2V IC-Control pose

Need pose + silhouette/edge + depth constraints
→ I2V/T2V IC-Control All-In-One

Existing clip needs 8 more seconds
→ V2V extension

Existing silent clip needs generated Foley
→ V2A Foley
```

## Hard refusal rule

If the requirement set cannot be satisfied by a registered and verified profile, output:

`NO_COMPATIBLE_WORKFLOW`

Do **not** invent nodes, merge unrelated workflows, or silently drop a control requirement.

## Community-case boundary

`tools/ltx2_select_profile.py` returns `REFERENCE_CASE_SELECTED`, not `PRODUCTION_READY`. A community source can inform which local workflow to try, but the production profile must be promoted through the normal API gate.
