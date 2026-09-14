# ComfyUI Template Ingestion Validator

Fail if any hard rule is violated.

## Source/provenance
- [ ] source kind recorded
- [ ] source ref/URL recorded
- [ ] UI workflow version recorded
- [ ] ComfyUI/template-package version recorded when known

## UI graph
- [ ] valid JSON
- [ ] root `nodes` exists
- [ ] legacy 0.4 and current 1.0 handled without forced conversion
- [ ] subgraph instances are distinguished from unknown custom nodes
- [ ] `definitions.subgraphs` recursively inspected when present

## Dependencies
- [ ] `properties.models` extracted without inventing URLs
- [ ] input assets recorded when detectable
- [ ] non-core/custom nodes reported
- [ ] missing-model popup is not treated as definitive when nested model folders may be used

## Execution evidence
- [ ] unchanged workflow loaded
- [ ] unchanged workflow run successfully
- [ ] API-format export from the same run-verified workflow exists

## Binding
- [ ] binding targets API graph, not UI widget indexes
- [ ] node ID exists
- [ ] `class_type` matches expected
- [ ] input exists and is literal/mutable
- [ ] linked inputs are not overwritten
- [ ] unsupported director controls remain explicit `UNBOUND`

## Regression
- [ ] baseline API graph preserved
- [ ] patched graph validated
- [ ] test run result recorded
