# Audio Patterns in the Studied LTX-2 Workflows

The repository is valuable because audio is not treated as a final afterthought. Many workflows carry a joint audio/video latent path and then separate video/audio again before output.

## 1. Native audio/video path

Repeated node families include:

- `LTXVEmptyLatentAudio`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode`
- video/audio VAE loaders

Director implication: sound intent belongs in the shot plan early enough to influence the model prompt, not only in the edit stage.

## 2. Custom audio

`I2V Basic (custom audio)` and `T2V Basic (custom audio)` add an imported audio path. The static graph contains audio loading, trimming/duration math, audio VAE encoding, and in some cases Mel-Band RoFormer nodes.

Use when:

- dialogue/music already exists and must drive timing;
- the shot duration should derive from a supplied audio segment;
- generated audio is not acceptable.

Production rule: when audio duration determines frame count, bind **audio + fps/duration controls** rather than overwriting a downstream linked `Set_frames` input.

## 3. Talking avatar / voice clone

The I2V and T2V talking-avatar workflows add `ComfyUI-QwenTTS` voice-clone nodes plus reference-audio/text controls and AV-latent logic.

This is a specialized workflow family. It should only be selected when the shot requires cloned/specified speech identity. It is not a general improvement for ordinary cinematic I2V.

The Skill must keep separate:

- character visual identity
- speaker/voice identity
- dialogue text
- reference audio
- generated lip/speech timing

## 4. V2A Foley

`V2A Foley (add sound to any video)` takes an existing video and generates audio from it. This is a different production task from I2V/T2V generation.

Use it after picture is sufficiently stable when the goal is:

- environmental Foley
- impact/interaction sounds
- synchronized non-dialogue audio

Do not route a normal I2V request through V2A just because the model family supports audio.

## 5. Sequence-level rule

For the user's preferred production loop:

```text
script
→ still approval
→ per-shot I2V
→ per-shot audio review
→ sequence edit
```

Audio continuity is scored separately from image continuity. A visually correct shot can still fail because ambience, dialogue timbre, loudness, or timing jumps across cuts.

## 6. Automation fields added in

The planning schema distinguishes:

```yaml
audio_mode: native | custom | voice_clone | foley | none
reference_audio_ref: null
custom_audio_ref: null
voice_reference_text: null
dialogue_text: null
audio_drives_duration: false
```

These fields are selector inputs. They are not assumed to map to the same node names in every LTX workflow.
