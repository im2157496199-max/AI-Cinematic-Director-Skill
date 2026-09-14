# Video QA & Repair

## Review order
1. **Identity** — face/hair/body/species marks
2. **Costume / prop** — structure, ownership, material, damage state
3. **Action readability** — action happened in the intended order
4. **Anatomy / temporal deformation** — hands, limbs, face, object morphing
5. **Camera** — movement matches intent and does not destroy composition
6. **Environment** — background geometry and fixed objects remain coherent
7. **Timing** — action is neither compressed into chaos nor padded with dead time
8. **End state** — usable for next shot / edit

## Repair priority
- identity failure -> strengthen reference / simplify motion / split shot
- anatomy failure -> reduce action complexity / add pose-control workflow / split action phases
- camera failure -> lower/simplify camera motion or use explicit camera-capable workflow
- continuity failure -> regenerate from approved still or approved end-state reference
- timing failure -> recompile duration/length before touching style

Never repair a structural failure by merely adding more adjectives to the prompt.
