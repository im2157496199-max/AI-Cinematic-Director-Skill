# MANGA_SEQUENTIAL_CORE.md

> Purpose: convert Story / Character / Director intent into readable sequential still images before optional video animation.
> This is a medium-adaptation layer, not a replacement for Story, Director, Cinematography, or Art Direction.

## 1. When to load

Load for:
- manga / comic pages
- sequential anime stills
- visual novel-like illustrated sequences
- storyboard-as-final-output
- image-first video workflow
- manga panels used as keyframes / shot candidates

Skip for:
- a single isolated image
- a conventional film shot list where no sequential still output is needed

## 2. Core diagnostic

For manga-oriented tasks, check four connected areas:

```text
CHARACTER
STORY
STORY WORLD
THEME
    ↓
VISUAL EXPRESSION
    +
DIALOGUE / LANGUAGE
```

Do **not** treat this as an equal-weight formula.
The project may intentionally emphasize one area.

## 3. Opening hook

The first page / first 1–3 panels should create forward pull.

Check:
- orientation: enough to follow?
- novelty: what is not generic?
- promise: what kind of experience is this?
- character: who is worth watching?
- question: what remains unresolved?
- visual impact: is there a memorable image?

5W1H is a baseline for clarity, not a mandatory establishing shot.

## 4. Information density

Prefer panels that do multiple compatible jobs:

```text
ACTION
+ CHARACTER
+ WORLD
+ RELATIONSHIP
+ TONE
```

Avoid panels that exist only to dump background information.

## 5. Character readability in sequence

A recurring character should have:
- one-line identity summary
- stable desire / behavioral logic
- weakness or friction point
- relationship-specific behavior
- signature verbal or physical behavior
- role-specific researched details when relevant
- visual identity locks in `entity_sheet`

Do not require a 60-field dossier at runtime.
Expand biography only when the missing information could change:
`what the character does / says / notices / avoids`.

## 6. Forward-motion test

A sequence should not spend many panels returning to the exact same dramatic state.

Track net change:
- knowledge
- danger
- trust
- status
- access
- freedom
- commitment
- capability
- emotional stance

A circular detour is acceptable only if the return has new meaning or cost.

## 7. Page / sequence budget

Before final panels:

```text
TOTAL PAGE / PANEL BUDGET
        ↓
IMPORTANT MOMENTS
        ↓
SPACE ALLOCATION
        ↓
ROUGH SCRIPT
        ↓
NAME / ROUGH PANEL PLAN
        ↓
FINAL PANEL SPECS
```

More important moments may receive:
- more panels
- larger panels
- slower time
- reaction panels
- stronger visual contrast

Do not allocate equal space by habit.

## 8. Panel rhythm

Panel size / density / framing influence pace.

Useful controls:
- large panel = emphasis / pause / reveal / environment
- small panel = quick action / reaction / detail / compressed time
- close-up = emotion / key information
- wider shot = orientation / relation / environment
- whitespace = pause / isolation / emphasis
- irregular geometry = use deliberately, not decoratively

Avoid many pages with identical layout rhythm unless monotony is intentionally dramatic.

## 9. NAME mode

NAME is a cheap planning pass.

For AI workflow, a NAME can be:
- ugly thumbnail
- stick figures
- text rectangles
- low-cost draft images
- contact sheet
- YAML/JSON panel layout

It must answer:
- what happens?
- where is everyone?
- what does the character feel/notice?
- what is the reader meant to notice first?
- where does the page turn / reveal land?
- what information can be removed?

Do not spend final-generation budget until NAME logic is stable.

## 10. Manga psychology layer

For manga / anime-like sequential stills, do not only show physical action.

Track:
- reaction
- gaze
- hesitation
- realization
- attraction / disgust / fear / pride
- relationship distance
- internal shift that is externally readable

A physical event may justify extra panels when the emotional interpretation is the point.

## 11. Spatial orientation

Within a continuous local action:
- keep action axis readable
- avoid arbitrary side switching
- preserve character positions
- use deliberate reorientation if camera side must change

Reuse the main continuity validator.

## 12. Dialogue

Dialogue should:
- sound speakable for that character
- fit current relation / status / culture
- avoid ornamental complexity for prestige alone
- carry subtext when useful
- avoid repeating visible information

Research vocabulary / manners when role accuracy matters.

## 13. Manga -> video bridge

Manga panel and film shot are related but not identical.

```text
MANGA PANEL
  = selected frozen information / emotion / action moment

VIDEO SHOT
  = temporal event with start / motion / end
```

Promotion rule:
- P0 panel -> almost always consider as video shot/keyframe
- P1 panel -> use if needed for action/continuity
- P2 panel -> combine / bridge / omit
- P3 panel -> usually omit from video

Video adaptation must invent temporal motion **without changing**:
- character identity
- costume
- key prop state
- spatial relation
- story result
- emotional meaning

## 14. Non-formula rule

These manga rules are a map.
Project style, genre, audience, references, and user intent control concrete visual style. JOJO is a valid selectable style/reference when explicitly requested, but is not a default inherited from the source book.
