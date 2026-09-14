# Character Color Design Core

Purpose:
Make anime/moe character color choices deliberate, readable and compatible with personality + world design.

## Runtime route
`skin base -> hair mass -> eye accent -> costume support/accent -> group contrast check -> lighting compatibility`

## Active rules

1. Decide skin temperature first.
   - yellow-base, pink-base, pale/cool-base are useful starting families.

2. Hair usually carries the largest color mass.
   - use it as the main identity field unless a helmet/coat/cape dominates instead.

3. Eyes usually carry the highest local accent.
   - strongest small-area contrast often belongs near the face.

4. Outfit should support, not drown the face.
   - reserve strongest global contrast for deliberate focal hierarchy.

5. Complementary or near-complementary accents are powerful.
   - use sparingly; too much high-contrast accent causes noise.

6. Cohesion and separation are different goals.
   - related hues = team/faction coherence.
   - contrast hues/values = individual differentiation.

7. Saturation and brightness change impression.
   - brighter + more saturated often reads younger / more energetic.
   - darker / quieter palettes often read cooler, heavier, or more mature.

8. Repeat a color echo only when useful.
   - a small eye-color echo in tie/ribbon/device can improve cohesion.

9. Mini/chibi modes need fewer colors.
   - simplify blocks and keep the face readable at reduced scale.

10. Local palette must still obey scene light.
   - character design palette does not override lighting logic.

## AI generation handoff
Before prompting, specify:
- skin base
- dominant hair color family
- eye accent color
- outfit dominant / support / accent
- whether the character belongs to a group palette
- whether lighting will warm/cool/neutralize those relationships
