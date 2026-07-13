# [Issue]: Excessive VRAM Allocation with ComfyUI

- **Issue #:** 5778
- **State:** closed
- **Created:** 2025-12-15T19:34:47Z
- **Updated:** 2026-01-04T11:15:13Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5778

### Problem Description

wan2.2 I2V A14B High noise Q2_K with high noise lora
wan2.2 I2V A14B Low noise Q2_K with low noise lora
umt5 xxl encoder Q3_K_S

latent size 848x480

5 second first image to last image video generation. It tried to allocate 85 GB of memory. I’m not sure if it’s normal for it to request this much memory, but it seems a bit excessive to me.

### Operating System

Bazzite OS (distrobox ubuntu) ComfyUI git clone non portable

### CPU

r7 7700 32 gb ram

### GPU

rx 9060 xt 16 gb

### ROCm Version

7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

Download the workflow I’m using. Install the dependencies. Add two images, don’t enter a prompt, and just run it.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

[wan22_ftl_14B_gguf_upscale 2.0.json](https://github.com/user-attachments/files/24174043/wan22_ftl_14B_gguf_upscale.2.0.json)

![Image](https://github.com/user-attachments/assets/89120825-77f3-4b25-8cfc-269d4a5c3092)