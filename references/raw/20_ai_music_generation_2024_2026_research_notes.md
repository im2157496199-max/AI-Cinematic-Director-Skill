# AI Music / Video-to-Music Research 2024–2026 — Focused Notes

> Role: frontier reference for AI-assisted soundtrack workflow.
> These papers inform pipeline design; they do NOT replace stable music theory.

## M2M-Gen (2024)
A multimodal background-music pipeline for Japanese manga.
Useful transferable architecture:
dialogue/scene boundaries + facial emotion -> high-level music directive -> page-level music captions -> text-to-music generation.

Runtime adaptation:
- analyze narrative boundaries first
- infer emotion from multiple channels, not text alone
- compile low-level scene facts into high-level music directives before generation
- maintain cross-page/shot musical consistency

## EMSYNC (2025)
Video soundtrack generation aligned to emotion and temporal boundaries.
Useful transferable ideas:
- emotion conditioning
- explicit scene-boundary conditioning
- musical events can anticipate/align to visual cuts rather than merely react afterward

Runtime adaptation:
- Editing exports cut/reveal boundaries
- Music may prepare a transition before the visual cut
- track emotional continuity plus temporal alignment separately

## Video Echoed in Music / VeM (2025)
Targets semantic, temporal, and rhythmic alignment.
Useful transferable idea:
- separate semantic relevance, scene-transition timing, and beat/rhythm synchronization instead of treating "match the video" as one vague goal.

## VIBE (2026)
Text-and-video conditioned background-music generation with fine-grained instruction alignment.
Useful transferable idea:
- music prompt/spec should support explicit hard controls (tempo/key when desired)
  plus softer controls (musicality, semantic alignment, mood).
- generation directives should be structured enough to verify instruction adherence.

## Policy
These are fast-moving research references.
Mark them FRONTIER_REFERENCE and periodically re-check before treating model-specific claims as durable rules.
