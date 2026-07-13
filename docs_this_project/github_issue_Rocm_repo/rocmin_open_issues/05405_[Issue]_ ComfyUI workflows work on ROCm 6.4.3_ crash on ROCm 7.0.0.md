# [Issue]: ComfyUI workflows work on ROCm 6.4.3, crash on ROCm 7.0.0

- **Issue #:** 5405
- **State:** open
- **Created:** 2025-09-21T02:49:23Z
- **Updated:** 2025-10-22T13:46:51Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5405

### Problem Description

I have noticed worse performance when compared to my previous experience with WSL2 with ROCm 6.4.2

ComfyUI becomes very slow on VAE Decode, almost always there is a warning about running out of memory: 
```Warning: Ran out of memory when regular VAE decoding, retrying with tiled VAE decoding.```

Before I managed to even use WAN 2.2 with Q4 quantized model, now I would get
```Memory access fault by GPU node-1 (Agent handle: 0x629f9f9dae60) on address 0x7cb3770e0000. Reason: Page not present or supervisor privilege.```

I haven't managed to generate a single 5s video.

Generating an image with SD3.5 Large FP8 takes like 300 seconds. The same for Flux dev fp8. Performance way worse than in following video: https://youtu.be/7qDlHpeTmC0?si=EFxnUA3qRprUL1hD

### Operating System

Linux Mint 22.2 (Zara)

### CPU

AMD Ryzen 7 5700X3D 8-Core Processor

### GPU

RX 9070 XT

### ROCm Version

ROCm 7.0.0

### ROCm Component

_No response_

### Steps to Reproduce

Linux Mint 22.2

Instructions as here: https://github.com/Lonceg/comfyui_for_amd_docker

Or Pull the original https://hub.docker.com/r/rocm/pytorch make a container, download ComfyUI and custom nodes.




### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_