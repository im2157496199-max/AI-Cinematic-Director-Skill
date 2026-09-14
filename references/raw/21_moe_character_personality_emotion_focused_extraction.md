# 萌えキャラクターの描き分け 性格・感情表現編 — Focused / Deduplicated Extraction

> Project role: bridge `personality -> visible character behavior`.
> Status: Character Embodiment source 1/4.
> Copyrighted source is NOT redistributed. This file contains paraphrased rules only.

## SOURCE ROLE

This book is not treated as a style target. Its value is converting personality and emotion into visible choices:
face parts, hairstyle, shoulder/hand behavior, pose, expression intensity, clothing attitude, and reaction patterns.

## ACTIVE RULES

### CE01 — Start from a small personality basis
Do not define a character with a giant adjective cloud. Choose a base personality and one secondary trait / contrast.
The secondary trait should add depth without making the character incoherent.

### CE02 — Personality must become observable
A personality label is incomplete until translated into visible behavior:
`personality -> face -> hair -> posture -> gesture -> expression -> clothing attitude`.

### CE03 — Avoid neutral standing as the default
A straight neutral stance carries little personality information.
Even a small change in shoulder tension, foot direction, hand position, head angle, or body lean can communicate character.

### CE04 — Shoulders are a personality control surface
Shoulder states strongly affect perceived character:
- open / lifted / active shoulders: energetic, assertive, expansive
- dropped / relaxed shoulders: low energy, ease, resignation
- shrugged / compressed shoulders: cute, timid, embarrassed, defensive
Do not use these as deterministic stereotypes; combine with context.

### CE05 — Hand placement changes character meaning
The same hand sign or gesture changes meaning depending on distance from face/body, shoulder position, elbow angle, and direction.
Gesture is not an isolated hand-shape tag.

### CE06 — Expression is a system, not one icon
Expression intensity is produced by coordinated changes in:
- eyebrows
- upper/lower eyelids
- eye openness / eye force
- gaze
- mouth shape / mouth opening
- head angle
Do not turn every angry character into the same "sharp eyes".

### CE07 — Preserve the character's base eye design through emotion
Emotion modifies the existing eye structure; it should not replace a droopy-eyed character with generic upturned eyes just because they are angry.
This is critical for identity continuity.

### CE08 — Use expression amplitude as personality
Two characters can feel the same emotion with different amplitudes.
Cool / reserved characters may change very little; energetic characters may exaggerate face, hair movement, limbs, and mouth size.

### CE09 — Hair movement can carry behavior
Hair is not only a static identity feature.
Motion, looseness, organization, and silhouette can reinforce energy, neatness, reserve, aggression, or softness.

### CE10 — Clothing attitude can express personality
Even shared uniforms can be worn differently.
Use neatness, looseness, skirt length, sleeves, accessories, layering, and movement-readiness to express character.
Do not confuse this with changing the uniform beyond faction continuity.

### CE11 — Character contrast / gap is useful when grounded
A secondary trait, hobby, weakness, or private preference can create a strong gap.
The gap must not erase the base personality; it should be triggered in a specific context.

### CE12 — Body language belongs to the whole upper-body chain
Hands cannot be designed independently from wrist, elbow, shoulder, clavicle, neck, and torso.
AI pose prompts should specify the larger chain when a hand pose matters.

### CE13 — Physical states can be built by combining emotional primitives
Cold, heat, pain, embarrassment, discomfort, etc. can be expressed as combinations of face + protective/avoidant body behavior + effects.
Avoid relying on face alone.

### CE14 — Camera angle modulates the same expression
High/low angle changes how embarrassment, dominance, sadness, or threat reads.
Emotion design and camera design must be coordinated.

### CE15 — Character-type examples are CASES, not universal laws
Examples like "strong personality -> ponytail / crossed arms / wide stance" or "timid -> inward feet / compressed shoulders"
are useful priors, not hard-coded identity rules.
Project references and character history outrank stereotypes.

## SOURCE-SPECIFIC ANTI-RULES

- Do NOT force "long hair = feminine", "short hair = energetic" as universal.
- Do NOT turn yandere / tsundere / cool archetypes into fixed templates.
- Do NOT copy 2010s moe proportions / fashion as the project default.
- Do NOT let expression mechanics overwrite Blue Archive character identity.
- Do NOT treat exaggerated manga symbols as mandatory for cinematic or semi-realistic outputs.

## MERGE WITH EXISTING SKILL

- Truby / Corbett: own internal motivation, contradiction, relationships.
- Weston: action/behavior over result-direction.
- Costume core: clothes communicate role, function, identity.
- Blue Archive P0: final commercial visual language and character identity.
- Director/camera: spatial behavior and angle.
- Gurney/Brown: light/color reveal or suppress expression.
- Murch: reaction timing and cut choice.

## ROUTING

Default character image:
`identity -> 2 personality axes -> visible behavior -> BA visual design -> pose -> camera -> light -> prompt`

Story-heavy character:
`story want / relationship / contradiction -> visible behavior -> BA visual design -> staging -> camera`
