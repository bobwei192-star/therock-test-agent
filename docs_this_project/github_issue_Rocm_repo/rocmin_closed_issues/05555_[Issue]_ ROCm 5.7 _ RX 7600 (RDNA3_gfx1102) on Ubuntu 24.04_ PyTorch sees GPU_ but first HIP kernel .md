# [Issue]: ROCm 5.7 + RX 7600 (RDNA3/gfx1102) on Ubuntu 24.04: PyTorch sees GPU, but first HIP kernel fails (“shared object initialization failed”)

- **Issue #:** 5555
- **State:** closed
- **Created:** 2025-10-21T18:40:06Z
- **Updated:** 2025-11-18T10:53:53Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5555

### Problem Description

Pytorch fails with GPU after kernel upgrade.
After routine Ubuntu updates on a system running ROCm 5.7 with an AMD Radeon RX 7600 XT (RDNA3 / gfx1102), PyTorch still detects the GPU (torch.cuda.is_available() == True, get_device_name(0) -> "AMD Radeon RX 7600 XT"), but the first GPU kernel fails with:

RuntimeError: HIP error: shared object initialization failed

This happens on the first operation that actually launches a kernel (e.g., tensor.fill_(0) or torch.zeros(...)). Pure allocations like torch.empty(..., device="cuda") succeed (no kernel launch). Earlier, this setup required HSA_OVERRIDE_GFX_VERSION=11.0.0 and worked; after the updates it no longer does.

### Operating System

OS: NAME="Ubuntu" VERSION="24.04.3 LTS  6.14.0-29-generic  (Noble Numbat)"

### CPU

CPU:  model name	: Intel(R) Core(TM) i5-14400

### GPU

Radeon RX 7600 XT (gfx1102)

### ROCm Version

5.7

### ROCm Component

_No response_

### Steps to Reproduce

ROCm 5.7 + RX 7600 (RDNA3/gfx1102) on Ubuntu 24.04: PyTorch sees GPU, but first HIP kernel fails (“shared object initialization failed”)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

PyTorch build tag: 2.3.1+rocm5.7

HIP runtime (torch): 5.7.31921-d1770ee1b

hip-runtime-amd: 5.7.31921.50700-63~22.04

libhsa-runtime64-1: 5.7.1-2build1

hsa-rocr-dev: 1.11.0.50700-63~22.04 (this 1.11.0 corresponds to ROCm 5.7)

rocminfo: 1.0.0.50700-63~22.04