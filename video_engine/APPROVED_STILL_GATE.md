# Approved Still Gate

I2V is downstream of still approval.

Required fields before video compilation:
- `approved_still: true`
- `source_image_ref`
- `entity_lock_snapshot_ref`
- final framing / aspect ratio
- shot start_state and intended end_state

If the user rejects the image, regenerate / repair the still first.
Do not ask the video model to “fix” a wrong face, wrong costume, wrong prop or wrong composition from an unapproved source image.
