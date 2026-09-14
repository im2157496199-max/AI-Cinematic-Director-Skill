# The Game Music Handbook — Noah Kellman — Focused / Deduplicated Extraction

> Source: *The Game Music Handbook: A Practical Guide to Crafting an Unforgettable Musical Soundscape*,
> Noah Kellman, Oxford University Press, 2020.
> User-supplied complete PDF: 291 pages.
> Project role: transferable music-design logic for interactive media and AI video/game-style music systems.
> Do not import Unity/FM0D/Wwise tutorials into runtime unless a task explicitly targets game implementation.

## ACTIVE CORE

### G01 — Music design before note-writing
Define what music must do, when it appears, how it interacts with the experience, what other audio occupies the same space,
and what technical/output constraints exist before composing.

### G02 — Nonlinear music needs emotional continuity without fixed event order
For interactive experiences, design emotional states and transitions rather than assuming one fixed timeline.

### G03 — Location can own musical identity
A location cue may encode safety/danger, geography, culture, story importance, familiarity, or changed meaning on return.
Revisiting a place can reuse and transform its theme to express narrative change.

### G04 — Theme transformation can communicate state change
Reuse recognizable thematic material while changing tempo, harmony, timbre, register, density, rhythm, or orchestration
to communicate altered character/location/story meaning.

### G05 — Diegesis is a continuum, not merely binary
Track whether music belongs inside the world, outside the world, or deliberately blurs with sound design.

### G06 — Horizontal resequencing
Use different musical sections/cues for different states, with explicit transition logic.
Transferable AI-video form:
`calm -> tension -> reveal -> action -> release`, each with designed entrances/exits rather than hard cuts between unrelated tracks.

### G07 — Vertical layering
Keep a coherent musical base while adding/removing functional stems to change intensity, danger, scale, or state.
Layers should have roles, not just instrument families.

### G08 — Hybrid systems are stronger than one-technique systems
Combine horizontal state changes with vertical density/intensity control.

### G09 — Music and sound design relationship must be deliberate
Choose whether the project uses:
- separated roles,
- overlapping/mixed roles,
- or a unified sonic system where environmental/action sounds are partly musical.

### G10 — Musical sound effects can carry information
Short musical events can signal reward, danger, progress, confirmation, failure, discovery, or world identity.
Their semiotic meaning must match the intended action.

### G11 — Cultural/musical codes are audience-dependent
Do not assume one musical signifier has universal meaning.
Treat genre, harmony, rhythm, instrument, timbre, and style associations as learned/cultural unless evidence supports otherwise.

### G12 — Reactive music maps state variables to musical variables
Possible mappings:
- danger -> density / dissonance / low-frequency impact
- proximity -> layer volume / timbre change
- movement -> rhythmic activity
- discovery -> new motif or harmonic region
- action peak -> stinger / accent
The mapping must be musically coherent, not one-to-one gimmickry.

### G13 — Procedural/algorithmic thinking = rules over fixed renders
For systems needing variation, define rules that can alter form, pitch, rhythm, harmony, timbre, instrumentation, or density.
For linear AI video, this becomes a reusable design grammar rather than literal real-time code.

### G14 — Build only the reactivity the project needs
Do not overengineer. Start with clear states and transitions; add procedural complexity only when it materially helps.

### G15 — Interactive music still needs silence and space
A state transition may intentionally remove music or return to ambience rather than always escalating.

## MERGE / CROSS-REFERENCE

- emotional arc -> Story / Editing already defines emotional timing; Music interprets it sonically
- motifs/themes -> Character/Story identity; Music owns musical transformation
- location meaning -> Setting / Space Design; Music owns sonic identity
- timing and cuts -> Editing; Music consumes cut/reveal/action events
- soundscape realism/worldbuilding -> Art Direction + Setting; Music/Sound owns aural realization

## REFERENCE_ONLY

- Unity implementation tutorials
- programming primer
- FMOD / Wwise / Elias UI steps
- version control workflow
- optimization specifics
- game business/contracts
- 2020-era predictions about future hardware

## AI ADAPTATION

Instead of "game data", AI video can expose:
- scene_id
- emotion / valence-arousal
- story_state
- character_state
- location
- cut point
- reveal point
- action intensity
- dialogue density
- silence requirement

Then map these to:
- cue family
- motif
- tempo band
- rhythmic density
- harmonic tension
- timbre/instrumentation
- layer density
- entry/exit mode
- accent/stinger
