# Architecture: Form, Space, & Order — Focused / Deduplicated Skill Extraction

> Source: Francis D.K. Ching, Fourth Edition.
> Role: environment / spatial-design grammar for AI art direction, anime/game scenes, film environments, and interior visualization.
> Policy: do not turn the Skill into an architecture textbook. Extract spatial perception and organization; keep technical construction/proportion systems out of runtime.

## ACTIVE CORE

### A01 — Space is not background; it is an organized system
Treat environment as interacting forms, voids, boundaries, openings, paths, and scale cues rather than a flat backdrop.

### A02 — Form and void define each other
A room/field/void is shaped by surrounding masses and planes, while the void also changes how those forms are perceived.

### A03 — Degree of enclosure is controllable
Openings within a plane preserve more enclosure; openings near edges weaken corners and increase continuity; openings between planes can make a space more diffuse and merge it with adjacent space.

### A04 — Openings control different variables
Keep separate:
1. enclosure / boundary strength
2. view / visual focus
3. light access

Light appearance belongs to LIGHT_COLOR; this module only declares the spatial opening and view relationship.

### A05 — Four fundamental spatial relationships
- space within a space
- interlocking spaces
- adjacent spaces
- spaces linked by a common/intermediate space

### A06 — Organization archetypes are layout grammar, not style presets
- centralized: dominant center + secondary spaces
- linear: sequential spaces / directional movement
- radial: center + outward branches
- clustered: proximity/common trait, flexible growth
- grid: modular field / repeatable framework

### A07 — Circulation is a perceptual thread
Viewers/users experience environments over time as a sequence of spaces. Define approach, entry, path, nodes, turns, terminations, destination, and what is revealed or withheld.

### A08 — Design the approach before the room
The approach can be frontal/direct, oblique, compressed, extended, revealing, or withholding. It prepares the viewer for the destination.

### A09 — Path hierarchy prevents maze-like scenes
Differentiate main route, secondary routes, nodes, pauses, and destinations by scale/form/length/placement.

### A10 — Sequence can carry narrative
Useful transitions:
compression -> release
concealment -> reveal
low -> high
narrow -> broad
ordinary -> dominant
private -> public
safe -> exposed

### A11 — Visual scale is relational
Perceived scale comes from comparison with familiar elements, not only numerical dimensions.

Useful anchors:
- human figure
- door
- stair
- chair/table
- window
- railing
- vehicle
- floor/module repetition

### A12 — Human-scale anchors make huge environments readable
For megastructures, keep one or more familiar anchors small and legible. Contrast makes monumental scale readable instead of merely labeling something “gigantic.”

### A13 — Multiple scales can coexist
A scene may simultaneously carry city/megastructure, building/interior, and human/furniture scales. Preserve at least one bridge between them.

### A14 — Spatial hierarchy uses exception
A space/form becomes important by differing from the norm through size, shape, or strategic placement.

### A15 — Axis organizes movement and views
A spatial axis is an environment-level line of organization. It can guide movement and views and should have meaningful termination(s).
Do not confuse this with the cinematography 180-degree axis.

### A16 — Rhythm is recurrence through space
Repeated columns, openings, modules, frames, lights, furniture bays, or structural motifs can create measured visual/spatial rhythm. Repeated elements need not be identical; a shared trait is enough to form a family.

### A17 — Break rhythm intentionally for emphasis
An exception in size/shape/spacing/placement can make a destination, entrance, landmark, or key object read as important.

### A18 — Unity needs variety
Perfect regularity can become monotonous; unconstrained variety becomes chaotic. Maintain a shared organizing logic with controlled exceptions.

### A19 — Spatial design responds to context
Organization/path/enclosure should respond to project needs, surrounding space, desired view, light access, and user activity—not exist as abstract geometry alone.

### A20 — Explicit spatial decisions beat generic tags
Before generating a space, choose a few explicit spatial decisions instead of relying on generic tags like `futuristic interior`, `beautiful hall`, or `epic city`.

## MERGE / CROSS-REFERENCE
- light through openings -> LIGHT_COLOR / Cinematography
- color/texture of surfaces -> Art Direction + LIGHT_COLOR
- shot composition/focal hierarchy -> Visual Story / Cinematography
- actor blocking -> Director; SPACE_DESIGN only defines usable topology and paths
- 180-degree screen direction -> Cinematography
- furniture production dimensions -> Interior specialist / user data
- generic hierarchy -> existing salience logic; this source contributes spatial hierarchy by size/shape/placement
- repetition/rhythm -> Visual Story; this source contributes environmental/spatial recurrence

## REFERENCE_ONLY
- golden-section formulas
- Renaissance proportion formulas
- Classical Orders
- Modulor numeric systems
- exact anthropometric tables
- structural-engineering ratios
- material-manufacturing dimensions
- historical building catalog as style targets
- drafting conventions not needed by generation

## AI ADAPTATION
### Anime/game environment
Use the book to answer:
`where is the viewer/character, what encloses them, what path exists, what is dominant, how large does it feel?`

Do not use the book to answer:
`what current anime/game style is fashionable?`
That comes from the case/reference library.

### Furniture/interior visualization
Use adjacency, circulation, enclosure, view, human-scale anchors, and spatial hierarchy.
Do not enforce fabrication-grade accuracy unless another module supplies real dimensions.
