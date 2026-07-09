# [Issue]: MIOpen missing headers for JIT compilation on Windows 11 + RX 7900 XTX + driver 26.1.1

- **Issue #:** 5941
- **State:** open
- **Created:** 2026-02-07T01:47:35Z
- **Updated:** 2026-03-04T19:23:10Z
- **Labels:** Windows, status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5941

### Problem Description

# AMD ROCm Windows Bug Report

**For submission to:** [github.com/ROCm/ROCm/issues](https://github.com/ROCm/ROCm/issues)

---

## Title
`torch.cuda.is_available()` causes access violation crash on Windows 11 with RX 7900 XTX and driver 26.1.1

## Environment

| Component | Version |
|-----------|---------|
| **GPU** | AMD Radeon RX 7900 XTX (24GB VRAM) |
| **OS** | Windows 11 |
| **Driver** | AMD Adrenalin Edition 26.1.1 |
| **Python** | 3.12.12 (Anaconda) |
| **PyTorch** | 2.9.1+rocmsdk20260116 |
| **HIP Version** | 7.2.26024-f6f897bd3d |
| **ROCm SDK** | 7.2.0.dev0 (pip wheels from repo.radeon.com) |

## Description

Calling `torch.cuda.is_available()` causes a hard crash with "Windows fatal exception: access violation" in the HIP runtime. This occurs despite:
- Driver 26.1.1 installed correctly (confirmed in Adrenalin GUI)
- HIP DLLs loading successfully
- PyTorch importing correctly
- `torch.version.hip` reporting correct version

## Steps to Reproduce

1. Install AMD Adrenalin Edition 26.1.1
2. Create Python 3.12 environment
3. Install ROCm SDK and PyTorch from repo.radeon.com:
```bash
pip install --no-cache-dir \
    https://repo.radeon.com/rocm/windows/rocm-rel-7.2/rocm_sdk_core-7.2.0.dev0-py3-none-win_amd64.whl \
    https://repo.radeon.com/rocm/windows/rocm-rel-7.2/rocm-7.2.0.dev0.tar.gz \
    https://repo.radeon.com/rocm/windows/rocm-rel-7.2/torch-2.9.1%2Brocmsdk20260116-cp312-cp312-win_amd64.whl
```
4. Run:
```python
import torch
print(torch.__version__)  # Works: 2.9.1+rocmsdk20260116
print(torch.version.hip)  # Works: 7.2.26024-f6f897bd3d
print(torch.cuda.is_available())  # CRASH
```

## Expected Behavior

`torch.cuda.is_available()` should return `True` and GPU should be accessible.

## Actual Behavior

Process crashes with:
```
Windows fatal exception: access violation

Current thread 0x00004d48 (most recent call first):
  File "...\torch\cuda\__init__.py", line 182 in is_available
```

## Additional Notes

- AMD's AI Bundle (installed via Adrenalin's "AI Bundle" option) includes Amuse with HIP 6.0.4 DLLs, while the pip wheels install HIP 7.2. This version mismatch may contribute to the issue.
- The crash occurs with both:
  - Conda environment with pip-installed ROCm
  - System Python 3.12 installed by AMD's AI Bundle
- HIP DLLs (`amdhip64_7.dll`) load successfully via ctypes before the crash
- Environment variables set: `HIP_PATH`, `ROCM_HOME`, `HSA_ENABLE_SDMA=0`

## System Specs

- CPU: AMD Ryzen 9 9900X (12-Core)
- RAM: 32 GB
- GPU: AMD Radeon RX 7900 XTX + AMD Radeon(TM) Graphics (integrated)


### Operating System

Windows 11

### CPU

AMD Ryzen 9 9900X 12-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 7.2.0.dev0 (HIP 7.2.26024-f6f897bd3d)

### ROCm Component

_No response_

### Steps to Reproduce

ROCm Component:   HIP Runtime (amdhip64_7.dll), PyTorch Windows wheels


1. Install AMD Adrenalin Edition 26.1.1
2. Create Python 3.12 environment
3. pip install PyTorch from repo.radeon.com/rocm/windows/rocm-rel-7.2/
4. Run: import torch; torch.cuda.is_available()
5. Observe crash: "Windows fatal exception: access violation"


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_