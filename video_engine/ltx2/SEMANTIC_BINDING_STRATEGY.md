# Semantic Binding Strategy for Appvikalabs-style LTX-2 Graphs

## Key discovery

Across the studied workflows, the author repeatedly uses `SetNode` / `GetNode` as named semantic buses. Examples include:

- `Set_width`, `Set_height`, `Set_frames`, `Set_fps`
- `Set_positive`, `Set_negative`
- `Set_ref_image`, `Set_start_image`
- `Set_firstframe`, `Set_middleframe`, `Set_lastframe`
- `Set_ref_pose`, `Set_ref_canny`, `Set_ref_depth`
- `Set_org_audio`, `Set_ref_audio`
- `Set_t2v_mode`
- `Set_ext_seconds`

These names are more useful for automation than raw node IDs because they tell the Skill **what the branch means**.

## Important limitation

A `SetNode` is normally fed by a link. the safe API compiler correctly refuses to overwrite linked inputs. Therefore the Skill must not bind `Set_width.INT` directly if that input is linked.

Instead:

```text
Set_width
  ↑ linked from
INTConstant "WIDTH"
```

The actual mutable source is the upstream constant node.

Likewise:

```text
Set_positive
  ↑
LTXVConditioning.positive
  ↑
CLIPTextEncode
```

The actual mutable source is the positive `CLIPTextEncode.text`, not the SetNode.

## Binding discovery algorithm

1. Find every `SetNode` and derive a semantic key from `widgets_values[0]` or `Set_*` title.
2. Follow its input link backward.
3. For pass-through-like nodes, preserve output/input semantic names when possible:
   - output `positive` → input `positive`
   - output `negative` → input `negative`
   - output `images` → input `images`
4. Stop at the nearest user-editable source node:
   - `CLIPTextEncode`
   - `LoadImage`
   - `LoadAudio`
   - `VHS_LoadVideo`
   - `INTConstant`
   - `PrimitiveFloat`
   - `PrimitiveBoolean`
5. Record that source as a **UI binding candidate**.
6. Open the actual locally working graph and `Export Workflow (API)`.
7. Confirm that the same node ID exists in the API graph and the `class_type` matches.
8. Match the candidate's UI widget value against a constant API input to infer the API input name.
9. Check the target node/input against `/object_info`.
10. Only then emit a mutable binding used by `comfy_workflow_compile.py`.

## Why this is stronger than guessing node IDs

The studied workflows contain many repeated node types. For example, two `CLIPTextEncode` nodes are common, as are two sampler passes. Binding by class type alone is ambiguous. The semantic-bus trace supplies context and turns a complex UI graph into a small set of named production controls.

## Role map used in

| Set semantic key | Production role |
|---|---|
| `width` | width |
| `height` | height |
| `frames` | frame_length or duration-driven frame plan |
| `fps` | fps |
| `positive` | positive_prompt |
| `negative` | negative_prompt |
| `ref_image` / `start_image` | source_image |
| `firstframe` | first_image |
| `middleframe` | middle_image |
| `lastframe` | end_image |
| `ref_pose` | pose_control |
| `ref_canny` | canny_control |
| `ref_depth` | depth_control |
| `ref_control` | control_video |
| `org_audio` | custom_audio |
| `ref_audio` | reference_audio |
| `t2v_mode` | text_only_mode |
| `ext_seconds` | extension_seconds |
| `source_video` | source_video |

## Tools

- `tools/ltx2_binding_candidates.py` traces UI anchors backward.
- `tools/ltx2_ui_to_api_binding.py` conservatively matches those candidates onto an API-format export.

Neither tool marks a binding as verified. Verification remains a runtime gate.
