# [Issue]: [ROCm][Windows] NotImplementedError for FP8 (e4m3fn) operators on RDNA4 (Navi 48) GPUs

- **Issue #:** 6019
- **State:** closed
- **Created:** 2026-03-05T05:35:01Z
- **Updated:** 2026-04-22T14:01:05Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6019

### Problem Description

While official documentation for RDNA4 (Navi 48) and PyTorch on Windows states that FP8 (E5M2, E4M3) is supported, basic Eager-mode operators such as torch.mm and torch.mul throw a NotImplementedError. This suggests that the dispatching logic or the necessary ROCm/hipBLAS kernels are missing or not correctly linked for the Windows ROCm build.


### Operating System

Microsoft Windows 11 Pro (10.0.26200 64-bit)

### CPU

12th Gen Intel(R) Core(TM) i5-12400

### GPU

AMD Radeon AI PRO R9700 (gfx1201)

### ROCm Version

ROCm7.11

### ROCm Component

_No response_

### Steps to Reproduce

import torch
a = torch.ones((512,512), dtype=torch.float8_e4m3fn).cuda()
b = torch.ones((512,512), dtype=torch.float8_e4m3fn).cuda()
a
tensor([[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.],
...,
[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.]], device='cuda:0',
dtype=torch.float8_e4m3fn)
b
tensor([[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.],
...,
[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.],
[1., 1., 1., ..., 1., 1., 1.]], device='cuda:0',
dtype=torch.float8_e4m3fn)
c = torch.mm(a,b)
Traceback (most recent call last):
File "", line 1, in
NotImplementedError: "addmm_cuda" not implemented for 'Float8_e4m3fn'
d = torch.mul(a,b)
Traceback (most recent call last):
File "", line 1, in
NotImplementedError: "mul_cuda" not implemented for 'Float8_e4m3fn'

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

PyTorch version: 2.9.1+rocmsdk20260116
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 7.2.26024-f6f897bd3d

OS: Microsoft Windows 11 Pro (10.0.26200 64-bit)
GCC version: Could not collect
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: N/A

Python version: 3.12.12 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 20:05:38) [MSC v.1929 64 bit (AMD64)] (64-bit runtime)
Python platform: Windows-11-10.0.26200-SP0
Is CUDA available: True
CUDA runtime version: Could not collect
CUDA_MODULE_LOADING set to:
GPU models and configuration: AMD Radeon AI PRO R9700 (gfx1201)
Nvidia driver version: Could not collect
cuDNN version: Could not collect
Is XPU available: False
HIP runtime version: 7.2.26024
MIOpen runtime version: 3.5.1
Is XNNPACK available: True

Versions of relevant libraries:
[pip3] numpy==2.4.1
[pip3] torch==2.9.1+rocmsdk20260116
[pip3] torchaudio==2.9.1+rocmsdk20260116
[pip3] torchvision==0.24.1+rocmsdk20260116
[conda] numpy 2.4.1 pypi_0 pypi
[conda] torch 2.9.1+rocmsdk20260116 pypi_0 pypi
[conda] torchaudio 2.9.1+rocmsdk20260116 pypi_0 pypi
[conda] torchvision 0.24.1+rocmsdk20260116 pypi_0 pypi

### Additional Information

_No response_