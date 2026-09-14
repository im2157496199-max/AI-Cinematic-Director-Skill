# Moe Character Application Layer

Integrated sources:
- 萌えキャラクターの描き分け 性格・感情表現編
- 萌えキャラクターの描き方 しぐさ・感情表現編
- 萌えキャラクターの描き分け 基本テクニック編
- 萌えキャラクターの描き分け 基本テクニック編（配色/基础图像观察）
- Mini Character source
- Angela Wang archetype-visualization thesis
- From Pixels to Personas research

Purpose:
Convert character personality, archetype and differentiation logic into visual, pose, color and prompt decisions.

## Runtime pipeline
`identity -> role -> base trait -> secondary trait/contradiction -> archetype energy -> visible behavior -> face/hair/silhouette -> color hierarchy -> costume attitude -> gesture/pose -> camera/light -> prompt`

## Active synthesis rules

### 1. Personality must become behavior before it becomes style
Do not jump directly from adjectives to accessories.
First define how the character looks, moves, reacts, and occupies space.

### 2. Archetype is an upstream control layer
Archetype helps choose silhouette pressure, posture, visual semiotics and prop logic.
It never replaces concrete behavior.

### 3. Identity survives emotion
The same character should remain recognizable across joy, anger, embarrassment, surprise and neutral states.
Eyes, brows, hair silhouette and facial mass cannot completely reset every time.

### 4. Differentiation is multi-channel
Use multiple contrast axes:
- eye family
- hair silhouette
- expression amplitude
- gesture behavior
- clothing attitude
- color hierarchy
- body proportion
- relationship geometry.
Do not separate characters by hair color only.

### 5. Color must be structured
Define:
- skin base
- hair dominant mass
- eye accent
- outfit support/accent
- group harmony vs cast contrast.

### 6. Gesture must match personality
The same emotion or action should look different on different personalities.
A shy wave, noble wave, hostile wave and energetic wave are not interchangeable.

### 7. Mini/chibi mode simplifies but does not erase identity
Reduce proportions and palette complexity, but keep:
- face family
- hair silhouette
- one signature color cue
- one gesture/personality cue.

### 8. Visual signals matter heavily for audience attachment
If the visual package is weak, abstract personality writing alone will not carry image-first media.
Prioritize readability and memorability.

### 9. Familiar anchor + differentiating twist
Many strong anime characters combine one quick-read trope anchor with one personal deviation.
Avoid total cliché and avoid random anti-trope noise.

### 10. Default prompt strategy
For character generation, prefer:
- identity anchors
- visible behavior
- silhouette and color instructions
- expression/gesture details
- costume attitude
and only then optional archetype labels.

## Runtime outputs expected
- character face/pose sheet
- differentiation notes for ensemble use
- color hierarchy block
- prompt-ready visible descriptors
