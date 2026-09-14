# Official Wan 2.2 Example Study

External source studied: official ComfyUI examples for Wan 2.2.

Public reference: https://comfyanonymous.github.io/ComfyUI_examples/wan22/

## 5B I2V example observations
The official UI workflow visibly contains:
- `LoadImage`
- positive and negative `CLIPTextEncode`
- `Wan22ImageToVideoLatent`
- model / VAE / text-encoder loaders
- `KSampler`
- VAE decode
- video/image-sequence save nodes

The published example shows 24fps output and the I2V latent node carries width/height/length inputs. A note in the example discusses 1280x704 and a longer frame count as a quality target, while the downloadable demo itself uses a shorter length for faster first execution.

## Engineering conclusion
These are example workflow settings, not universal Skill defaults.
The 14B example has a different, more complex topology. Therefore the current system does not hard-code the example node IDs or sampler graph. It uses a binding layer so the same director-level plan can target different verified workflows.
