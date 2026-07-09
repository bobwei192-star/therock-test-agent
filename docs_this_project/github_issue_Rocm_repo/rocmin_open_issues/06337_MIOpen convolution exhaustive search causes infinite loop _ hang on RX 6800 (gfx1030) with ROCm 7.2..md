# MIOpen convolution exhaustive search causes infinite loop / hang on RX 6800 (gfx1030) with ROCm 7.2.1

- **Issue #:** 6337
- **State:** open
- **Created:** 2026-06-06T21:16:28Z
- **Updated:** 2026-06-08T13:57:56Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6337

### Problem Description

### Environment Description
* **GPU**: AMD Radeon RX 6800 (gfx1030)
* **OS**: Ubuntu 22.04 LTS  <!-- 如果是24.04请修改 -->
* **ROCm Version**: 7.2.1
* **PyTorch Version**: 2.9.1+rocm7.2  
* **Software Framework**: ComfyUI (with BiRefNet / Rembg nodes)
 
* ### Steps to Reproduce
1. Install ROCm 7.2.1 on Ubuntu.
2. Run ComfyUI with a workflow containing `BiRefNet` or `VAE Decode` nodes.
3. Start the queue. The process hits the convolution layer and hangs indefinitely.

### Expected Behavior
MIOpen should respect environment variables like `MIOPEN_FIND_MODE=2` to skip exhaustive tuning and use the fallback solver instantly.

### Actual Behavior
MIOpen completely ignores environment variables and forces an exhaustive search over 400+ runs, eventually leading to a complete freeze, GPU lockup, or ComfyUI process termination.

### Error Logs / Screenshots
<!-- 在这里直接把您上一张发给我的“带有 Runs left: 431, Please, be patient...”的终端截图拖拽或者粘贴进来 -->


### Operating System

Ubuntu 24.04.4 LTS Linux 6.14.0-1007-oem

### CPU

AMD Ryzen 5600

### GPU

Radeon 6800

### ROCm Version

rocm 7.2.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_