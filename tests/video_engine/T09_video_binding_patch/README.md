# T09 Video Binding Patch Regression

This is a compiler regression fixture, not a claim that a model was rendered.
It uses real ComfyUI 0.33.0 core class/input names:
- CLIPTextEncode
- Wan22ImageToVideoLatent
- LoadImage
- SaveWEBM

PASS requires the compiler to change only bound scalar fields and leave links/topology untouched.
