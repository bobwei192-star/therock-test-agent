# [Issue]: comfyui with SDXL to generate image, certain resolutions utilize 100% GPU without progress

- **Issue #:** 5474
- **State:** open
- **Created:** 2025-10-06T17:42:51Z
- **Updated:** 2026-02-10T16:32:30Z
- **Labels:** status: triage, project: miopen
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5474

### Problem Description

Workflow [amd.json](https://github.com/user-attachments/files/22727458/amd.json)

When use above basic workflow, *some* resolutions work normally and finished in ~8 seconds, *some* resolutions stuck at sampler 0th step while utilizing 100% GPU,  *some* resolutions stuck at VAE decoder while utilizing 100% GPU.

When stuck, it will take several minutes then trigger a driver timeout and then may or may not progress.

The system is configured with 64GB dedicated graphics memory.

For my system, following resolutions (w*h) work normally:
* 1024x1024
* 1344x768
* 1024x1536

Following resolutions (w*h) stuck:
* 1216x832
* 768x1344
* 1152x896
* 1536x1024

(Yes, weirdly the working/non-working resolutions are not symmetrical on w/h)

The ComfyUI is setup with following steps:
1. install python 3.12.10
2. install uv
3. git clone https://github.com/comfyanonymous/ComfyUI.git
4. remove torch, torchaudio, torchvision from requirement.txt
5. setup uv venv
6. uv pip install --index-url https://rocm.nightlies.amd.com/v2/gfx1151/ "rocm[libraries,devel]"
7. uv pip install --index-url https://rocm.nightlies.amd.com/v2/gfx1151/ --pre torch torchaudio torchvision
8. uv pip install -r requirements.txt

### Operating System

Windows 11 10.0.26100

### CPU

CPU: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S AMD Radeon(TM) 8060S Graphics

### GPU

AMD Radeon(TM) 8060S Graphics

### ROCm Version

7.9.0rc20250928

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_