# [Issue]: ROCm 7.1 /opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory

- **Issue #:** 5943
- **State:** open
- **Created:** 2026-02-08T17:17:09Z
- **Updated:** 2026-02-12T16:12:28Z
- **Labels:** status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5943

### Problem Description

https://github.com/ROCm/ROCm/issues/2961 is closed without an obvious solution.
Just installed rocm and pytorch on CachyOS from the https://download.pytorch.org/whl/nightly/rocm7.1 index

```
python -c "import torch; print(torch.cuda.is_available())"
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
True
```
Now, in #2961 it is suggested to symlink to /opt/amdgpu but I'm wondering which source I should use.
I have
```
locate amdgpu.ids
/usr/share/libdrm/amdgpu.ids
```
and `venv/lib/python3.14/site-packages/torch/share/libdrm/amdgpu.ids` from my python venv installation.

I'm a bit lost here and very new to this whole rocm and torch party.



### Operating System

CachyOS Linux

### CPU

AMD Ryzen 9 7950X3D 16-Core Processor

### GPU

AMD Radeon RX 9070 XT 

### ROCm Version

ROCm 7.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_