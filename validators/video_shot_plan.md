# Video Shot Plan Validator

FAIL if any:
- approved_still is false but compile_status is ready
- source_image_ref missing
- shot id / source shot spec missing
- target duration missing
- adapter_length violates workflow profile step/base
- actual duration not recorded after length snapping
- requested camera/control feature is unbound but compile_status says ready
- identity locks not carried into video handoff

WARN if:
- camera mapping is approximation (e.g. dolly intent -> Zoom In)
- motion amplitude is high while identity stability is critical
- complex multi-phase action is packed into a very short clip
- end state is not clearly defined for a sequence shot
