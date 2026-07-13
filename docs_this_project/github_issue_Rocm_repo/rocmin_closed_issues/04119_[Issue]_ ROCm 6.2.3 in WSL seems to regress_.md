# [Issue]: ROCm 6.2.3 in WSL seems to regress?

- **Issue #:** 4119
- **State:** closed
- **Created:** 2024-12-06T04:50:53Z
- **Updated:** 2026-01-12T19:54:27Z
- **Labels:** Under Investigation, ROCm 6.2.3, RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/4119

### Problem Description

I was using ComfyUI in ROCm 6.1.3 for WSL with PyTorch `2.5.1+rocm6.1`, and it was working pretty well.

As ROCm 6.2.3 for WSL rolling out, I installed [Adrenalin Edition 24.12.1](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-24-12-1.html), `amdgpu-uninstall` previous ROCm 6.1.3 installation in WSL, and reinstalled ROCm 6.2.3 following the [instructions](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html).

For ComfyUI, I `pip3 --force-reinstall` PyTorch `2.5.1+rocm6.2`, and launched it using `TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1 python3 main.py --use-pytorch-cross-attention`.

In my simple SDXL workflow, which directly generates an image of 1024x1536, the host driver keeps timed out during VAE decoding. Until I mess around and remove `~/.triton`, it progresses but with a warning of "Ran out of memory when regular VAE decoding, retrying with tiled VAE decoding", which has never been seen when using ROCm 6.1.3 for WSL.

The overall experience is not satisfying, tiled upscaling has also stuck for some time.

### Operating System

Ubuntu 22.04.5 LTS in WSL 2 in Windows 10 22H2

### CPU

Ryzen 7 7800X3D

### GPU

RX 7900 XTX

### ROCm Version

ROCm 6.2.3

### ROCm Component

_No response_

### Steps to Reproduce

![ComfyUI_114514](https://github.com/user-attachments/assets/d83d0ef1-e438-4e07-ac1e-7525ea4172be)

Drag the image into ComfyUI to load the workflow, and then click "Queue Prompt".

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_