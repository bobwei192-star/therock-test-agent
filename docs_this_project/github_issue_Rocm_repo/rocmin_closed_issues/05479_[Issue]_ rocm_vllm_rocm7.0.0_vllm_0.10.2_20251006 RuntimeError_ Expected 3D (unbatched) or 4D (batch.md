# [Issue]: rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006 RuntimeError: Expected 3D (unbatched) or 4D (batched) input to conv2d

- **Issue #:** 5479
- **State:** closed
- **Created:** 2025-10-08T03:42:41Z
- **Updated:** 2025-10-22T18:51:47Z
- **Labels:** status: triage
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5479

### Problem Description

I ran rocm/vllm docker image with **AIDC-AI/Ovis2-8B-GPTQ-Int4** model

With **rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006** version, I got error **RuntimeError: Expected 3D (unbatched) or 4D (batched) input to conv2d**

With previous version **rocm/vllm:rocm6.4.1_vllm_0.10.1_20250909** I have no issue.

The logs attached

[vllm-rocm6.4.1_vllm_0.10.1_20250909.txt](https://github.com/user-attachments/files/22758273/vllm-rocm6.4.1_vllm_0.10.1_20250909.txt)
[vllm-rocm7.0.0_vllm_0.10.2_20251006.txt](https://github.com/user-attachments/files/22758274/vllm-rocm7.0.0_vllm_0.10.2_20251006.txt)

### Operating System

CachyOS Linux

### CPU

AMD Ryzen 7 5700X3D 8-Core Processor

### GPU

AMD Radeon RX 7800 XT

### ROCm Version

ROCm 7

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_