# [Issue]: [gfx1151] ROCm does not support Radeon 8060S (RDNA 3.5 Strix Halo) — Missing HIP kernel

- **Issue #:** 6348
- **State:** closed
- **Created:** 2026-06-11T15:26:09Z
- **Updated:** 2026-06-22T13:57:11Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6348

### Problem Description

Body:

Hardware Information
- Architecture: RDNA 3.5 (Strix Halo)
- GPU ID: gfx1151
- VRAM: 128GB GDDR5


Problem Description

ROCm does not currently support the gfx1151 (RDNA 3.5 Strix Halo) architecture. ROCm 7.x HIP kernels only cover up to gfx110x (RDNA 3 consumer GPUs) and do not include gfx1151.

When attempting to force the use of gfx110x kernel indexing (e.g., by setting the environment variable HSA_OVERRIDE_GFX_VERSION=11.0.0), the following error occurs:

ROCm kernel launch failed: no matching kernel image found for GPU gfx1151


Impact

This prevents all ROCm-based AI/ML tools from functioning on this GPU, including:

- ComfyUI — Cannot start at all
- PyTorch with ROCm — Cannot detect the GPU
- llama.cpp with ROCm — Cannot perform inference
- Any CUDA alternative using HIP/ROCm — Similarly affected

Alternative Solutions Attempted

1. DirectML — Orders of magnitude slower than ROCm/CUDA; not practical
2. ZLUDA — AMD has abandoned this project; does not support gfx1151
3. Vulkan (VKD3D-Proton) — Still in early stages; lacks full PyTorch support
4. WSL2 + ROCm — Equally affected by the missing gfx1151 kernel

Request

I hope the ROCm team can add official support for gfx1151. Specific suggestions:

1. Add HIP kernel support for gfx1151 in ROCm 7.x or 8.x
2. Update ROCm's GPU compatibility list to explicitly include the Strix Halo series
3. Provide official testing and validation to ensure PyTorch, Triton, and other components work correctly

Additional Notes

This laptop (Ryzen AI 395 / Radeon 8060S) was purchased at a premium price (NTD$110,000 / ~US$3,400) specifically for its AI computing capabilities. However, the primary AI ecosystem (ROCm) does not support this hardware out of the box. This is a serious concern for consumers.

Thank you to the ROCm team for your hard work. I look forward to gfx1151 support becoming available.


### Operating System

Windows 11 / Ubuntu 24.04 (WSL2)

### CPU

AMD Ryzen AI 395

### GPU

AMD Radeon 8060S

### ROCm Version

ROCm 7.x

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_