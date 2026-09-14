# EDITING_CORE.md

> Editing layer for AI multi-shot video and manga/keyframe-to-video workflows.
> Owns when to cut, what to omit, what to show next, and how shots become a sequence.

## Responsibilities
Director: what the scene means / what should be shot.
Cinematography: how an individual shot is framed and photographed.
Editing: which shots survive, in what order, and for how long.

## Rule of Six
Emotion
→ Story
→ Rhythm
→ Eye-trace
→ Planarity
→ 3D spatial continuity

Aim to satisfy all six. When tradeoffs are unavoidable, sacrifice lower priorities before higher ones.

## Minimal-cut principle
Before adding a cut ask:
- did the current thought finish?
- does the next shot add new story/emotion/information?
- is the cut needed for rhythm or attention?
- would holding be stronger?

## Cut-point model
Each shot may contain multiple candidate cut points. Track:
- audience_current_thought
- thought_completion
- emotional_completion
- next_needed_information
- next_attention_target
- effect_if_cut_now
- effect_if_hold

## Dialogue rule
Do not use `speaker -> cut -> speaker -> cut` mechanically.
Use reactions/subtext/listening when they carry the real meaning.

## Audience-lead rule
Give the next necessary idea slightly before the viewer consciously asks for it.

## Sunk-cost firewall
Ignore generation effort/cost. Keep only what improves the sequence.

## Contact-sheet edit map
For multi-shot work, review one representative frame per shot to spot:
- duplicate compositions
- repeated information
- missing orientation/reaction
- monotonous progression
- costume/location/state drift

## Feedback diagnosis
Viewer complaint != root cause.
Check earlier setup, missing information, rhythm, expectation, or continuity.

## Version discipline
If uncertain, make A/B cuts with a stated hypothesis. Do not generate random versions.

## Editing-to-sound handoff
Expose:
- cut points
- reveal points
- silence windows
- action peaks
- emotional turns

Editing does not compose music.
