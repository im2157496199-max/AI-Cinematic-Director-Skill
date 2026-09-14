# ART_DIRECTION_CORE.md

> Purpose: transform story / character / theme / directorial POV into a coherent visible world.
> This layer is shared by film, anime, manga, AI stills, game-like visual scenes, and interior/furniture visualization.

## 1. Core principle

Art direction is not “add a style keyword.”

```text
STORY / CHARACTER / THEME
        ↓
DIRECTORIAL POV / PROJECT INTENT
        ↓
DESIGN CONCEPT
        ↓
REFERENCE / RESEARCH
        ↓
SPACE + ARCHITECTURE
        ↓
COLOR + MATERIAL + TEXTURE
        ↓
DÉCOR + PROPS + COSTUME RELATION
        ↓
ATMOSPHERE / PSYCHOLOGY
        ↓
CAMERA-COMPATIBLE ENVIRONMENT
```

The design should tell the same story as the script and performance.

## 2. Design concept first

Before generating details, define:

- one-line design concept
- psychological image
- atmosphere
- optional visual metaphor
- what the design should make the viewer feel
- what must NOT become generic

A design metaphor is optional.
Do not force symbolism into every object.

## 3. No generic environments

Do not output:

> “modern apartment, stylish furniture, cinematic lighting”

without character/story logic.

Ask instead:
- Who lives here?
- What do they value?
- What can they afford?
- What have they kept for years?
- What is repaired, neglected, displayed, hidden?
- What social/psychological state does the space project?
- What story action must this space support?

## 4. Research -> transform

Reference is evidence, not a cage.

Use:
- factual references for period / culture / object truth
- paintings / visual art for interpretation
- architecture for spatial logic
- photographs for physical detail
- material samples for texture
- project references for desired style

Then transform them through the design concept.

## 5. Psychological environment

Each important location should have:

```yaml
psychology:
  relationship_to_character:
  desired_audience_feeling:
  environment_pressure:
  emotional_temperature:
  story_function:
```

Possible environment relationships include:
`hostile / protective / aspirational / oppressive / seductive / sterile / chaotic / sacred / playful / alienating`.

These are descriptors, not fixed genre presets.

## 6. Architecture / space

Track:
- scale
- compression vs openness
- verticality
- hierarchy
- axes / symmetry / asymmetry
- circulation
- thresholds / entrances / exits
- foreground / midground / background
- staging zones
- sightlines
- camera positions
- repeated architectural language

A believable large world should imply systems beyond the frame.

For furniture/interior tasks, this section becomes especially important:
actual layout can be approximate when only visualization is required, but room identity, circulation, cabinetry/furniture relation, visual hierarchy, and camera usability should remain coherent.

## 7. Color

Color is dramatic structure.

Define:
- dominant palette
- supporting palette
- accent
- restricted/absent colors
- character color relationships
- location color relationships
- progression across story
- interaction with planned lighting

Avoid universal symbolic tables.
Meaning comes from project context.

## 8. Material / texture / age

Do not make every surface pristine.

For each important material:
- base material
- finish
- roughness / reflectivity
- age
- wear pattern
- maintenance
- environmental exposure
- stains / fading / damage when appropriate
- narrative or class meaning if relevant

Wear must have a cause.

## 9. Props and décor

Prioritize:

```text
P0 story-critical prop
P1 character-signature / repeated prop
P1 world-authenticating object
P2 atmosphere / décor
P3 random clutter
```

Prefer a few meaningful specific objects over an uncontrolled pile of detail.

## 10. Style flexibility

This Skill does not own one art style.

Valid outputs include:
- realistic live action
- Japanese anime
- manga
- JOJO-like stylization when explicitly selected
- graphic / expressionist
- painterly
- retro
- brutalist / Bauhaus / Art Deco / etc.
- sci-fi / fantasy
- furniture / interior marketing visualization

Style comes from user intent + project references + art-direction concept.

## 11. Digital / AI rule

Generative capability does not replace design reasoning.

AI may:
- invent impossible architecture
- transform locations
- replace materials
- age surfaces
- create virtual worlds
- blend realistic and stylized elements

But must still preserve:
- story relevance
- internal logic
- depth / perspective
- material behavior
- scale
- palette
- character-space relationship
- continuity across shots/panels

## 12. Approval gate

Before expensive image generation, confirm:

- [ ] design concept is clear
- [ ] reference set is sufficient
- [ ] key environments are distinct
- [ ] character-space relationships are defined
- [ ] palette has dramatic purpose
- [ ] materials/textures are not generic
- [ ] signature props/décor are identified
- [ ] architecture supports staging/camera
- [ ] style is explicitly selected or reference-driven
- [ ] no accidental “default cinematic look” has replaced the project identity


## 13. Place as narrative agent

Do not ask only “what does this location look like?” Ask:

- why must this scene happen **here**?
- what does this place allow / prevent?
- does it expose, hide, isolate, tempt, pressure, protect, or oppose the character?
- would the same scene mean something different elsewhere?

A location may be:
`background / supportive / active_character / antagonist`.

## 14. Spatial familiarity and meaningful breaks

Recurring spaces can teach the audience their geography.
Track established:
- routes
- room ownership
- public/private zones
- vertical status
- entrances/exits
- safe/unsafe areas

Breaking a learned spatial rule can carry narrative meaning. Do not treat every return to the same location as a fresh unrelated image.

## 15. Curate reality / anti-stereotype filter

Real-world reference contains too many signals.
Select the signals that serve this story and suppress accidental contradictions.

Do not choose a place/culture/period only through:
- tourist icons
- picturesque/exotic detail
- inherited genre clichés
- stereotyped “instant readability”

Prefer the **dominant characteristic relevant to the project**.

## 16. Design visibility mode

Choose deliberately:
- `supportive_invisible`
- `expressive_visible`
- `spectacle_forward`

A highly visible design is allowed when the project wants spectacle, stylization, fantasy, musicality, graphic excess, game/anime intensity, or architectural dominance.
The failure condition is not “too visible”; it is **visibility that contradicts the intended narrative experience**.

## 17. Visual polarisation

When a genuine story contrast exists, art direction may externalize it through controlled opposition in:
- shape
- material
- texture
- density
- order/disorder
- scale
- volume
- spatial openness
- palette

Use one clear polarity only when it helps. Do not reduce complex characters/worlds into arbitrary binaries.

## 18. Story-order visual progression

Review environments in narrative sequence, not only as isolated location sheets.
Track changes in:
- compression / expansion
- density / emptiness
- material state
- color structure
- access / ownership
- cleanliness / decay
- repeated motifs
- meaning of familiar spaces

A recurring motif should have an appearance map and an evolving function, not merely repeat as branding.

## 19. Negative space / omission

Bare walls, gaps, empty volume, darkness, missing furniture, absent decoration, and suppressed detail are valid Production Design decisions.
Do not fill every region simply because the image model can generate detail.

## 20. Temporal identity

For past / present / future, define the strategy:

```text
surface_accuracy
period_or_social_spirit
selective_shorthand
stylized_reinterpretation
production-era_bias
```

Past: do not confuse museum-like surface accuracy with dramatic truth.
Present: do not let fashionable trend objects enter by accident and date the project unnecessarily.
Future: do not make something “futuristic” without ensuring the future design supports the society, story, and character logic.

## 21. Environment source strategy

Choose per key location:
- `observed_real`
- `transformed_real`
- `constructed`
- `hybrid`
- `virtual`

Source type does not determine authenticity. Narrative and internal logic do.
