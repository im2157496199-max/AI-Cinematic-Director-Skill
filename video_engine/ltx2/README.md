# LTX-2 Workflow Intelligence

This module converts a third-party LTX-2 workflow repository into **planning knowledge**, not blind execution authority.

## Source studied

- Community repository: `appvikalabs/LTX-2-Workflows`
- Uploaded source archive parsed in this build: 19 workflow files
- Repository branch checked: `upstream`
- Observed branch head: `739d7e9e5db868a57eedf87a1865d35c6d9f6816`
- Raw third-party workflow JSON is **not bundled** in this Skill package because no license file was detected in the uploaded archive and GitHub did not expose a repository license.

See `SOURCE_PROVENANCE.yaml`.

## What was learned

The repository is useful because it exposes a practical family of workflows rather than one monolithic graph:

- I2V basic / simple / GGUF / custom-audio
- T2V basic / GGUF / low-VRAM / custom-audio
- first+last frame control
- first+middle+last frame control
- IC-Control pose
- all-in-one pose + canny + depth control
- I2V/T2V mode switching
- sampler-preview variant
- voice-clone talking-avatar variants
- V2A Foley
- V2V extension

The strongest reusable pattern is not any single node ID. It is the combination of:

1. **semantic buses** built around `SetNode`/`GetNode` names such as `Set_width`, `Set_frames`, `Set_positive`, `Set_ref_image`;
2. a stable separation between **models → prompt → latent preparation → sampler pass 1 → latent upscale → sampler pass 2 → decode**;
3. optional branches added only when a requirement exists: keyframes, custom audio, IC control, T2V switch, voice clone, or V2V/V2A input;
4. external-node dependencies that must be treated as runtime contracts, not assumed from memory.

## Important currentness boundary

The Appvikalabs repository is a **community case library**. It is not used as the current official LTX-2 contract.

Current Lightricks documentation now separates newer **LTX-2.3** workflows from older **LTX-2.0** workflows. Therefore the current system uses Appvikalabs examples to learn selector patterns, semantic anchors, dependency recognition, and graph organization, while production execution still requires the user's currently working local workflow.

## Production gate

```text
creative requirement
  ↓
video_shot_plan
  ↓
LTX-2 reference-case selector
  ↓
user/local workflow that actually runs
  ↓
Export Workflow (API)
  ↓
UI semantic-anchor → API binding candidate
  ↓
/object_info contract check
  ↓
topology-preserving compile
  ↓
regression run
  ↓
PRODUCTION_READY
```

A community UI workflow can never jump directly from `DISCOVERED` to `PRODUCTION_READY`.

## Files

- `SOURCE_PROVENANCE.yaml` — exact study provenance and redistribution policy
- `catalog/appvikalabs_workflow_catalog.json` — derived catalog from all 19 workflows
- `WORKFLOW_FAMILY_MATRIX.md` — human-readable family map
- `SELECTOR_POLICY.md` — director requirement → workflow family logic
- `SEMANTIC_BINDING_STRATEGY.md` — Set/Get anchor tracing into API binding
- `PARAMETER_AND_CONSTRAINTS.md` — what is actually observed vs what is unsafe to universalize
- `CONTROL_AND_KEYFRAME_PATTERNS.md` — first/last/middle and pose/canny/depth patterns
- `AUDIO_PATTERNS.md` — native audio, custom audio, voice clone, Foley
- `DEPENDENCY_ECOSYSTEM.md` — node/model dependency evidence
- `CURRENTNESS_AND_MIGRATION.md` — legacy/community patterns vs current official LTX workflows

## Tools

- `tools/ltx2_repo_inspect.py`
- `tools/ltx2_select_profile.py`
- `tools/ltx2_binding_candidates.py`
- `tools/ltx2_ui_to_api_binding.py`

These tools are deliberately conservative. They output `CANDIDATE` or `REFERENCE_CASE_SELECTED`, not fake execution proof.
