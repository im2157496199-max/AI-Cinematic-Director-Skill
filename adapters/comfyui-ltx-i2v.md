# ComfyUI LTX I2V Adapter

Core source node: `LTXVImgToVideo`.

Confirmed inputs:
- image
- width / height (step 32)
- length (minimum 9, step 8)
- batch_size
- strength 0..1

`strength` belongs to LTX image conditioning. Do not automatically equate it with general character motion amplitude.
Length should be snapped to `8n + 1` when using this node.
