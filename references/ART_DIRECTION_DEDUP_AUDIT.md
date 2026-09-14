# ART_DIRECTION_DEDUP_AUDIT.md

Purpose: prevent theory-source accumulation from turning into duplicate runtime rules.

## Source comparison

| Barnwell topic | Existing coverage | Action |
|---|---|---|
| Story-first design | `ART_DIRECTION_CORE §1–3` | MERGE, no new rule |
| Design concept | `§2 Design concept first` | MERGE |
| Research | `§4 Research -> transform` | MERGE |
| Character through environment/possessions | `§3/5/9` | MERGE |
| Color | `§7` | MERGE |
| Texture/material/aging | `§8` | MERGE |
| Architecture/space | `§6` | MERGE |
| Props/décor | `§9` | MERGE |
| Digital tools | `§11` | MERGE |
| Stylization/nonrealism | `§10` | MERGE |
| **Place changes scene meaning** | only implicit | **ADD** |
| **Environment as active antagonist/agent** | psychological effect only | **ADD** |
| **Learned spatial geography + meaningful break** | continuity exists elsewhere, not design syntax | **ADD** |
| **Real-world conflicting signals + anti-stereotype curation** | reference transform, but not this test | **ADD** |
| **Design visibility: invisible / expressive / spectacle** | old validator leaned too strongly toward restraint | **ADD + CORRECT** |
| **Visual polarisation** | not explicit | **ADD** |
| **Story-order visual progression board** | palette progression only | **ADD** |
| **Motif recurrence map** | motif list only | **ADD** |
| **Negative space / omission as design material** | not explicit in PD layer | **ADD** |
| **Temporal identity / present-day trend noise** | period research only | **ADD** |
| **Observed vs transformed vs constructed vs virtual source strategy** | digital transform only | **ADD** |

## Dedup policy going forward

When a new theory book arrives:
1. map its candidate rules to current runtime rules;
2. mark `MERGE`, `ADD`, `CORRECT`, or `REFERENCE_ONLY`;
3. only `ADD`/`CORRECT` modify runtime core;
4. supporting overlap may be recorded in provenance but does not create another instruction;
5. if two sources disagree, preserve the difference as a conditional choice instead of silently averaging them.
