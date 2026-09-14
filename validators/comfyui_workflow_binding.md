# ComfyUI Workflow Binding Validator

For every non-null binding:
1. target node exists in API JSON
2. node class_type matches expected_class_type when specified
3. input key already exists unless binding explicitly allows create
4. no two semantic bindings accidentally target an incompatible field
5. required capability has all required bindings
6. no ambiguous class-type-only selector is accepted silently

Compile result:
- PASS
- WARN
- FAIL
- UNBOUND
