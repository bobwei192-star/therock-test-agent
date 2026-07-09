# [Issue]: `amdgpu-install` suddenly fails to install on Rocky Linux 8 with 404 error

- **Issue #:** 5160
- **State:** closed
- **Created:** 2025-08-07T08:47:31Z
- **Updated:** 2025-08-27T13:22:25Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5160

### Problem Description

I am part of @blender and we are currently in the process of adding new GPU workers to our CI/CD stack, including AMD-specific ones. 

About 2 weeks ago we were following the following instructions for installing them (which I retrieved from [your documentation](https://amdgpu-install.readthedocs.io/en/latest/install-prereq.html#downloading-the-installer-package)) and was successful in doing so, however, re-running this right now causes a 404 error instead:

```
[blender@rocky-x64-amd-01 ~]$ amdgpu-install --usecase=workstation -y --vulkan=pro --opencl=rocr --opengl=mesa --rocmrelease=6.4.0 --accept-eula
AMDGPU 6.4.2 Proprietary repository                                                                                                                                                    485  B/s | 548  B     00:01
Errors during downloading metadata for repository 'amdgpu-proprietary':
  - Status code: 404 for https://repo.radeon.com/amdgpu/6.4.2/rhel/8.10/proprietary/x86_64/repodata/repomd.xml (IP: 104.126.37.145)
Error: Failed to download metadata for repo 'amdgpu-proprietary': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
```

It looks like the proprietary drivers for Rocky Linux 8 (`rhel8`) have been removed in the meantime.

### Operating System

Rocky Linux 8.10 (Green Obsidian)

### CPU

AMD Ryzen 9 7950X 16-Core Processor

### GPU

AMD Radeon RX 5700 XT (`gfx1010`)

### ROCm Version

ROCm 6.4.2

### ROCm Component

ROCm

### Steps to Reproduce

1. Be on RHEL8-based OS, in my case Rocky Linux 8.
2. Run `wget https://repo.radeon.com/amdgpu-install/6.4.2/rhel/8.10/amdgpu-install-6.4.60402-1.el8.noarch.rpm`
   ```
   --2025-08-06 15:22:55--  https://repo.radeon.com/amdgpu-install/6.4.2/rhel/8.10/amdgpu-install-6.4.60402-1.el8.noarch.rpm
   Resolving repo.radeon.com (repo.radeon.com)... 88.221.24.25, 88.221.24.58, 2a02:26f0:b200::58dd:1989, ...
   Connecting to repo.radeon.com (repo.radeon.com)|88.221.24.25|:443... connected.
   HTTP request sent, awaiting response... 200 OK
   Length: 25856 (25K) [application/x-redhat-package-manager]
   Saving to: ‘amdgpu-install-6.4.60402-1.el8.noarch.rpm’
   
   amdgpu-install-6.4.60402-1.el8.noarch.rpm             100%[========================================================================================================================>]  25.25K  --.-KB/s    in 0.002s
   
   2025-08-06 15:22:55 (10.4 MB/s) - ‘amdgpu-install-6.4.60402-1.el8.noarch.rpm’ saved [25856/25856]
   ```
3. Install using `sudo dnf install amdgpu-install-6.4.60402-1.el8.noarch.rpm -y`:
   ```
   Last metadata expiration check: 0:19:11 ago on Wed 06 Aug 2025 03:03:55 PM UTC.
   Package amdgpu-install-6.4.60402-2187269.el8.noarch is already installed.
   Dependencies resolved.
   Nothing to do.
   Complete!
   ```
5. Try to install Pro drivers using `amdgpu-install --usecase=workstation -y --vulkan=pro --opencl=rocr --opengl=mesa --rocmrelease=6.4.0 --accept-eula` and observe 404 errors:
   ```
   AMDGPU 6.4.2 Proprietary repository                                                                                                                                                    485  B/s | 548  B     00:01
   Errors during downloading metadata for repository 'amdgpu-proprietary':
   - Status code: 404 for https://repo.radeon.com/amdgpu/6.4.2/rhel/8.10/proprietary/x86_64/repodata/repomd.xml (IP: 104.126.37.145)
   Error: Failed to download metadata for repo 'amdgpu-proprietary': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
   ```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.15
Runtime Ext Version:     1.7
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          NO
VMM Support:             NO

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 9 7950X 16-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 9 7950X 16-Core Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   5881
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            32
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    64728840(0x3dbaf08) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    64728840(0x3dbaf08) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    64728840(0x3dbaf08) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    64728840(0x3dbaf08) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1010
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon RX 5700 XT
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      4096(0x1000) KB
  Chip ID:                 29471(0x731f)
  ASIC Revision:           2(0x2)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   768
  Internal Node ID:        1
  Compute Unit:            40
  SIMDs per CU:            2
  Shader Engines:          2
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    1280(0x500)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 156
  SDMA engine uCode::      35
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    8372224(0x7fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    8372224(0x7fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1010:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
    ISA 2
      Name:                    amdgcn-amd-amdhsa--gfx10-1-generic:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    gfx1036
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon Graphics
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      256(0x100) KB
  Chip ID:                 5710(0x164e)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2200
  BDFID:                   4352
  Internal Node ID:        2
  Compute Unit:            2
  SIMDs per CU:            2
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:       APU
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 22
  SDMA engine uCode::      9
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    524288(0x80000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    524288(0x80000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1036
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
    ISA 2
      Name:                    amdgcn-amd-amdhsa--gfx10-3-generic
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```

### Additional Information

_No response_