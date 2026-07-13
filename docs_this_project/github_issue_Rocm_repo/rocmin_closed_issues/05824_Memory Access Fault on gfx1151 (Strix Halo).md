# Memory Access Fault on gfx1151 (Strix Halo)

- **Issue #:** 5824
- **State:** closed
- **Created:** 2025-12-29T18:48:26Z
- **Updated:** 2026-01-26T03:21:06Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5824

# AMD ROCm Bug Report: Memory Access Fault on gfx1151 (Strix Halo)

## Summary

Basic PyTorch GPU memory operations crash with "Memory access fault by GPU node-1" on AMD Radeon 8060S (gfx1151 / Strix Halo). Even the simplest possible GPU tensor creation fails.

## Minimal Reproducer

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")  # True
print(f"Device: {torch.cuda.get_device_name(0)}")      # AMD Radeon 8060S
x = torch.tensor([1.0, 2.0, 3.0]).cuda()               # CRASHES HERE
```

**Environment variables used:**
```bash
TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1 HSA_OVERRIDE_GFX_VERSION=11.0.0 python test.py
```

## Error Output

```
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
CUDA available: True
Device: AMD Radeon 8060S
Memory access fault by GPU node-1 (Agent handle: 0x1b376c50) on address 0x7f762a667000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```

## System Information

### Hardware
- **CPU**: AMD Ryzen AI Max+ 395 (Strix Halo)
- **GPU**: AMD Radeon 8060S (gfx1151)
- **RAM**: 128GB (32GB CPU / 96GB GPU unified memory)

### Software Versions
- **OS**: Nobara Linux 43 (Fedora-based)
- **Kernel**: 6.17.8-200.nobara.fc43.x86_64
- **linux-firmware**: 20250808-1.fc42
- **ROCm Runtime**: 6.3.1-4.fc42
- **ROCm Core**: 6.3.1-2.fc42
- **PyTorch**: 2.9.1+rocm6.3

### Kernel Boot Parameters
```
amd_iommu=off ttm.pages_limit=25165824 ttm.page_pool_size=25165824
```

### ROCm Packages Installed
```
rocm-runtime-6.3.1-4.fc42.x86_64
rocm-core-6.3.1-2.fc42.x86_64
rocm-hip-6.3.1-4.fc42.x86_64
rocm-opencl-6.3.1-4.fc42.x86_64
rocm-smi-6.3.1-3.fc42.x86_64
rocm-device-libs-18-37.rocm6.3.1.fc42.x86_64
rocm-llvm-libs-18-37.rocm6.3.1.fc42.x86_64
rocm-comgr-18-37.rocm6.3.1.fc42.x86_64
```

## What I've Tried

| Configuration | Result |
|--------------|--------|
| linux-firmware 20251125 | Crash |
| linux-firmware 20250808 | Crash |
| Kernel 6.18.2 | Crash |
| Kernel 6.17.8 | Crash |
| ROCm 7.1.1 (via Docker) | Crash |
| ROCm 6.3.1 | Crash |
| amdgpu.cwsr_enable=0 | Crash |
| amd_iommu=off | Crash |
| ttm.pages_limit=25165824 | Crash |
| HSA_OVERRIDE_GFX_VERSION=11.0.0 | Crash |
| HSA_OVERRIDE_GFX_VERSION=11.0.3 | Crash |

## Additional Information

### GPU Detection Works
```bash
$ amd-smi
GPU-Name: Radeon 8060S Graphics
Mem-Usage: 874/98304 MB
```

### GTT Memory is Correct
```bash
$ sudo dmesg | grep -i "gtt memory"
amdgpu: 98304M of GTT memory ready.
```

### Previously Working
This configuration was working on **December 18, 2025**. The issue started after a system update on **December 29, 2025** which upgraded 1510+ packages including ROCm 6.3.1 → 7.1.1 and linux-firmware. Downgrading did not restore functionality.

## Expected Behavior

Simple tensor operations should work on gfx1151 GPU without memory access faults.

## Actual Behavior

Any GPU memory operation triggers "Memory access fault by GPU node-1" with "Page not present or supervisor privilege" error.

## Related Issues

- https://github.com/ROCm/ROCm/issues/5616 (Strix Point memory issues)
- AMD Strix Halo gfx1151 is a newer variant that may have similar issues

## Contact

Please let me know if you need any additional diagnostic information.
