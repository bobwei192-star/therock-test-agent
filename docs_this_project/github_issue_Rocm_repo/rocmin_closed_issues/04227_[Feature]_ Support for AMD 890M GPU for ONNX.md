# [Feature]: Support for AMD 890M GPU for ONNX

- **Issue #:** 4227
- **State:** closed
- **Created:** 2025-01-06T12:06:34Z
- **Updated:** 2025-02-10T11:51:52Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/4227

### Suggestion Description

Hi, I have a new PC with AMD Ryzen AI 9 HX 370 with 890M GPU.
I have installed HIP SDK 6.2.  And I can see the architecture:
C:\Program Files\AMD\ROCm\6.2\bin>.\amdgpu-arch.exe
gfx1150
Since I am using ONNX to run many language models, but since I can only use CPU, the inference performance is very bad.  And I can't find good document on how to use AMD GPU for Windows.  The latest document seems only support GPU in Linux, but I am using Windows 11.
Please show me some instructions on how to enable GPU in ONNX for Windows.
Thanks,

### Operating System

Windows 11

### GPU

M890

### ROCm Component

ONNX with AMD GPU support