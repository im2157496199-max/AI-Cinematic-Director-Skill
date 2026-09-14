# From Pixels to Personas — Focused Extraction for Character Embodiment

> Project role: large-scale empirical check on how personality archetypes, visual traits and audience preference relate in anime character design.
> Status: research bridge source.
> This file contains paraphrased project rules only.

## SOURCE ROLE

This paper is useful because it provides a data-oriented view of anime character design.
It supports three important runtime conclusions:
1. personality archetypes recur and can be clustered,
2. visual design is systematically associated with those archetypes,
3. visual signals often predict audience preference better than personality labels alone.

## ACTIVE RULES

### PP01 — Characters are multimodal products
Treat anime characters as a combination of:
- personality traits
- distinct visual features
- role / production context
- sometimes voice/performance cues
Do not design from text labels only.

### PP02 — Archetype clusters are useful but not exhaustive
The paper identifies recurring clusters such as:
- Energetic Extroverts
- Steadfast Leaders
- Cold-hearted Antagonists
- Passionate Strivers
- Kind Caregivers
- Justice Keepers
- Reserved Introverts
- Arrogant Tsunderes
Use these as a reminder that recurring bundles exist, not as a closed ontology.

### PP03 — Some archetypes are visually more predictable than others
The paper reports that Justice Keepers, Energetic Extroverts, and Cold-hearted Antagonists are relatively predictable from visual features.
Runtime implication:
- some roles have heavily conventionalized design language
- if you want fast readability, using conventions helps
- if you want uniqueness, break conventions in a controlled way.

### PP04 — Visual signals often dominate popularity prediction
The paper finds that visual signals can be more influential than personality labels in audience preference modeling.
Runtime implication:
- if the design is meant to attract immediate attention, face/silhouette/color/prop logic matters enormously
- good backstory alone will not rescue a visually weak design in image-first media.

### PP05 — Conventionality and novelty must be balanced
The paper suggests audiences like some familiar design tropes,
but also respond well to less conventionalized characters.
Use a mix:
- one fast-read anchor
- one or two differentiating twists
Avoid complete trope-randomness and complete cliché.

### PP06 — Moe-ification is a historical trend, not a mandatory default
The paper observes a broader historical increase in softer / moe-like signals in anime character design.
This is useful as trend context.
It is NOT a command to push every design toward moe softness.

### PP07 — Reserved / contrast-rich archetypes can be especially appealing
The paper notes higher audience-preference signals for clusters such as Reserved Introverts and Arrogant Tsunderes.
Runtime implication:
- contrast and layered interiority can increase attachment
- shy / reserved / contradictory behavior should be visualized carefully, not flattened.

### PP08 — Personality and visual traits should be checked for alignment
Because the paper studies systematic association,
it supports adding a validator question:
- does the visual package actually express the intended trait bundle?
If not, revise face / silhouette / color / staging.

### PP09 — Target audience affects trait packaging
The paper discusses the historical shift toward older teen/young-adult audiences.
Runtime implication:
- age target and medium affect how strongly traits should be simplified or made psychologically layered.

### PP10 — Distinctiveness should survive outside story context
The discussion of kyara-like persistence supports this rule:
A strong character should remain identifiable even when detached from the original story scene.
Check:
- silhouette
- color identity
- face family
- signature prop / motif
- behavior cue.

## MERGE WITH EXISTING SKILL

- Character Embodiment: supports trait -> visual validation.
- Character Differentiation: supports ensemble contrast beyond text labels.
- Prompt Compiler: encourages visible, image-executable signals over abstract descriptors.
- Case libraries: can use empirical trend data to decide when to follow or resist current anime conventions.

## REFERENCE_ONLY

- MyAnimeList popularity as a universal artistic value measure
- historical trend graphs as direct style mandates
- overfitting to any one audience demographic

## STYLE FIREWALL

DO NOT:
- confuse historical frequency with design necessity
- let popularity statistics replace creative intent
- reduce archetypes to data labels without behavioral translation
