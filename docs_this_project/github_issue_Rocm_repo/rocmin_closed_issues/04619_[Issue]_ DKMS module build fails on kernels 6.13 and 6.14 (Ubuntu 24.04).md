# [Issue]: DKMS module build fails on kernels 6.13 and 6.14 (Ubuntu 24.04)

- **Issue #:** 4619
- **State:** closed
- **Created:** 2025-04-13T05:50:20Z
- **Updated:** 2025-07-25T20:20:25Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4619

### Problem Description

DKMS modules provided by AMD's amdgpu-dkms package consistently fail to build against mainline Linux kernels 6.13 and 6.14 on Ubuntu 24.04. This issue prevents users with new hardware, which explicitly requires newer kernel features, from benefiting from GPU acceleration, ROCm, Vulkan, and OpenCL capabilities provided by AMDGPU.

### Operating System

Ubuntu 24.04.2 with mainline kernels

### CPU

AMD Ryzen 9950x

### GPU

AMD Radeon 9070 XT

### ROCm Version

ROCm 6.4

### ROCm Component

_No response_

### Steps to Reproduce

**Expected Behavior**

The DKMS modules (e.g., amdgpu.ko) should compile and install successfully against newer kernels, enabling full GPU acceleration and ROCm support on recent AMD hardware.

**Actual Behavior**

DKMS fails to build against kernels 6.13/6.14, producing errors similar to:

```
ERROR (dkms apport): kernel package linux-headers-6.14.0-061400-generic is not supported
make[1]: Entering directory '/usr/src/linux-headers-6.14.0-061400-generic'
...
amd/amdgpu/amdgpu_drv.c:3098:10: error: ‘const struct drm_driver’ has no member named ‘date’
```

**Detailed Technical Explanation**

The root cause appears to be API changes introduced in kernels 6.13/6.14, specifically DRM subsystem changes, which the AMDGPU DKMS driver (amdgpu-dkms version 6.4.x) has not adapted to.

Errors indicate structural changes in drm_driver, causing compilation errors (no member named ‘date’, implicit declaration of functions).

Additional build errors due to missing or altered kernel headers, or incompatibilities in the driver code with these kernels.

**Impact**

Users with new hardware (e.g., AMD Radeon RX 7000 series GPUs) are effectively forced to choose between hardware support (newer kernels) and GPU acceleration (AMD's official drivers and ROCm).

**Workarounds**

Currently, no stable workaround exists other than using older kernels (≤ 6.12), which do not fully support newer hardware platforms (e.g., networking issues, lack of full GPU functionality).

**Proposed Solutions**

AMD should update the DKMS drivers explicitly to handle new DRM and kernel API changes in kernels 6.13/6.14.

**Environment**

Ubuntu 24.04 (Noble Numbat)

AMD Radeon 9070 XT

Linux kernels: 6.13.x, 6.14.x

AMDGPU DKMS package: version 6.4

**Additional Information**

This issue explicitly limits users from fully utilizing new AMD hardware, pushing them toward unsupported or unstable configurations.

**Requested Action**

Update the AMDGPU DKMS driver codebase to support Linux kernels 6.13 and 6.14.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_