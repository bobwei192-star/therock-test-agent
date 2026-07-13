# Performance regression in kernel 7.0.12 (fc44): SDXL inference 42x slower than on kernel 7.0.11

- **Issue #:** 6358
- **State:** open
- **Created:** 2026-06-14T05:40:43Z
- **Updated:** 2026-06-29T18:46:23Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6358

## Problem Description

After updating from kernel 7.0.11-200.fc44 to 7.0.12-200.fc44, 
SDXL model inference in ComfyUI became extremely slow, taking around 
388 seconds instead of around 9 seconds. The regression is 
reproducible on both 7.0.12-200 and 7.0.12-201. Booting back to 
7.0.11-200 restores normal performance immediately.

## Environment

- OS: Fedora 44
- Kernel (working): 7.0.11-200.fc44.x86_64
- Kernel (broken): 7.0.12-200.fc44.x86_64 and 7.0.12-201.fc44.x86_64
- GPU: AMD Radeon RX 6950 XT (gfx1030)
- ROCm: 7.1.1-4.fc44 (rocm-core)
- PyTorch: 2.12.0+rocm7.2
- ComfyUI: 0.24.0

## Steps to Reproduce

1. Boot into kernel 7.0.12-200.fc44
2. Start ComfyUI
3. Run a workflow with an SD1.5 model
4. Switch to an SDXL model and run the same workflow

## Results

| Kernel            | SD1.5  | SDXL     |
|-------------------|--------|----------|
| 7.0.11-200.fc44   | 4.47s  | 9.14s    |
| 7.0.12-200.fc44   | 4.73s  | 388.25s  |

## Analysis

The iteration speed during generation is identical on both kernels 
(around 5 it/s for SDXL). This suggests the slowdown is not in GPU 
compute itself, but in something happening before generation starts, 
likely ROCm JIT kernel compilation taking significantly longer on 
7.0.12. The dmesg logs show no errors on either kernel.

Logs for both kernels are attached.

[comfyui_7.0.11.txt](https://github.com/user-attachments/files/28923093/comfyui_7.0.11.txt)
[comfyui_7.0.12.txt](https://github.com/user-attachments/files/28923088/comfyui_7.0.12.txt)
[dmesg_7.0.11.txt](https://github.com/user-attachments/files/28923090/dmesg_7.0.11.txt)
[dmesg_7.0.12.txt](https://github.com/user-attachments/files/28923089/dmesg_7.0.12.txt)
[sysinfo_7.0.11.txt](https://github.com/user-attachments/files/28923091/sysinfo_7.0.11.txt)
[sysinfo_7.0.12.txt](https://github.com/user-attachments/files/28923092/sysinfo_7.0.12.txt)