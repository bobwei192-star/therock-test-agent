# [Issue]: ComfyUI randomly but consistently causing driver crash on gfx1030 (RX 6950 XT) and torch==2.8.0+rocm6.4

- **Issue #:** 5195
- **State:** closed
- **Created:** 2025-08-14T11:54:28Z
- **Updated:** 2025-10-23T21:17:20Z
- **Labels:** Under Investigation
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5195

### Problem Description

ComfyUI has been causing driver crash on my setup w/ RX 6950 XT randomly and consistently. The crash can happen if I tried to infer a number of images with smaller resolutions (512x512) consecutively. It can also just immediately crash the system upon my first attempt to infer an image with larger resolution (1024x1024). All crashes seem to be hard crashes where the whole system is automatically rendered a soft reset, and the GPU cannot be seen through the bus after the reboot unless a hard reset is performed. No kernel logs were collectable most of the time since the hang seems to happen too fast for kernel to write any logs.

I doubted this might be an instance of #4729 , since I do have some crashes happening when the flow was in VAE decoding. But further test with `--cpu-vae` still crashes and most of the crashes happen in the process of UNET inference anyway.

**This also seems to be strongly connected to comfyui and/or PyTorch. Since I have been running ggml-based applications without any problems.** Both [llama.cpp](https://github.com/ggml-org/llama.cpp) and [sd.cpp](https://github.com/leejet/stable-diffusion.cpp) run with ROCm without any problems on my setup. Especially on `sd.cpp`, where exact same image inference tasks causing crashes in `comfyui` completed without even a single issue there. However I have not tested any other torch application on this setup so if there is any suggested small test snippets/benchmarks I could use for replicating the issue please do let me know.

Currently my runtime setup for comfyui looks like this 
```
podman run --device /dev/kfd --device /dev/dri --security-opt seccomp=unconfined -d --name comfyui \
    <volume and port flags> --replace \
    -e HIP_VISIBLE_DEVICES=0 \
    -e TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1 \
    -e HSA_OVERRIDE_GFX_VERSION=10.3.0 \
    comfyui-rocm:latest --port 8818 --cpu-vae --listen
```

I am right now trying to go through the various different flags from ComfyUI and different ROCm configuration envs to see if any of them could help mitigate the issue. I have tried these and they don't seem to work:
```
--disable-cuda-malloc
--use-pytorch-cross-attention
--f16-vae
MIOPEN_FIND_MODE=2
 PYTORCH_HIP_ALLOC_CONF=garbage_collection_threshold:0.6,max_split_size_mb:6144
 PYTORCH_HIP_ALLOC_CONF=backend:native
 PYTORCH_HIP_ALLOC_CONF=backend:native,expandable_segments=True
```
Any suggestions for me to try would be appreciated.

### Operating System

Fedora CoreOS 42.20250623.3.1, Kernel 6.15.8-200.fc42.x86_64, Container Debian GNU/Linux 12 (bookworm)

### CPU

AMD Ryzen 9 7950X3D 16-Core Processor

### GPU

AMD Radeon RX 6950 XT

### ROCm Version

ROCm 6.4 from PyTorch Pip Package

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_