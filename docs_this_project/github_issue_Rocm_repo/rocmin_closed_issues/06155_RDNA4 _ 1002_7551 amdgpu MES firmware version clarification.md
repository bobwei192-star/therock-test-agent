# RDNA4 / 1002:7551 amdgpu MES firmware version clarification

- **Issue #:** 6155
- **State:** closed
- **Created:** 2026-04-16T00:40:55Z
- **Updated:** 2026-05-12T07:17:28Z
- **Labels:** status: assessed
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6155

I am seeing a persistent firmware/interface mismatch on two RDNA4 GPUs with PCI ID 1002:7551.

The issue reproduces on:
- 6.8.0-110-generic
- 6.17.0-20-generic

It also reproduces with both:
- AMD DKMS amdgpu 6.16.13
- the stock in-kernel amdgpu driver

With the stock driver loaded from:
/lib/modules/6.17.0-20-generic/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko.zst

dmesg reports for both GPUs:
- SMU driver if version not matched
- smu driver if version = 0x0000002e
- smu fw if version = 0x00000032
- smu fw version = 0x00684a00 (104.74.0)

GPU 03:00.0 also reports:
- MES FW version must be >= 0x82 to enable LR compute workaround

The cards still initialize successfully, but the mismatch persists across kernels and driver paths, which suggests this is not just a DKMS packaging issue and is more likely related to firmware / upstream support for these GPUs.