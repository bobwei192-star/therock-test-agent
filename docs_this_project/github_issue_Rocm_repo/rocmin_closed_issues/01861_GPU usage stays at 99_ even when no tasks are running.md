# GPU usage stays at 99% even when no tasks are running

- **Issue #:** 1861
- **State:** closed
- **Created:** 2022-11-18T08:39:14Z
- **Updated:** 2022-11-18T12:29:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1861

For any GPU operation, the GPU usage will always remain at 99%, and it can only be restored to the normal state by using the `rocm-smi --gpureset -d 0` command.

Normally, `rocm-smi` outputs:

```
~# rocm-smi

======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK  MCLK   Fan  Perf  PwrCap  VRAM%  GPU%
0    41.0c  5.0W    0Mhz  96Mhz  0%   auto  203.0W    0%   0%
================================================================================
============================= End of ROCm SMI Log ==============================
```

After executing any GPU task, (pytorch training, even running `rocminfo` command)

```
~# rocm-smi

======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK     MCLK   Fan  Perf  PwrCap  VRAM%  GPU%
0    43.0c  24.0W   2265Mhz  96Mhz  0%   auto  203.0W    0%   99%
================================================================================
============================= End of ROCm SMI Log ==============================
```
This state will remain until the `rocm-smi --gpureset -d 0` command is run.

Some info:

```
root@hs2 ~# cat /etc/system-release
Rocky Linux release 9.0 (Blue Onyx)
root@hs2 ~# uname -a
Linux hs2 5.14.0-70.30.1.el9_0.x86_64 #1 SMP PREEMPT Thu Nov 3 20:29:04 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
root@hs2 ~# dnf list --installed | grep rocm
hsa-rocr5.3.0.x86_64                             1.7.0.50300-63.el9                @rocm
rocm-core.x86_64                                 5.3.0.50300-63.el9                @rocm
rocm-core5.3.0.x86_64                            5.3.0.50300-63.el9                @rocm
rocm-smi-lib.x86_64                              5.0.0.50300-63.el9                @rocm
rocminfo5.3.0.x86_64                             1.0.0.50300-63.el9                @rocm
root@hs2 ~# dnf list --installed | grep amdgpu
amdgpu-dkms.noarch                               1:5.18.2.22.40.50300-1483871.el9  @amdgpu
amdgpu-dkms-firmware.noarch                      1:5.18.2.22.40.50300-1483871.el9  @amdgpu
root@hs2 ~# lsmod | grep amdgpu
amdgpu               7393280  1
iommu_v2               24576  1 amdgpu
gpu_sched              49152  1 amdgpu
i2c_algo_bit           16384  2 amdgpu,i915
drm_ttm_helper         16384  1 amdgpu
ttm                    86016  3 amdgpu,drm_ttm_helper,i915
drm_kms_helper        311296  2 amdgpu,i915
drm                   634880  7 gpu_sched,drm_kms_helper,amdgpu,drm_ttm_helper,i915,ttm
```

rocminfo
```
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    12th Gen Intel(R) Core(TM) i9-12900
  Uuid:                    CPU-XX
  Marketing Name:          12th Gen Intel(R) Core(TM) i9-12900
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
    L1:                      49152(0xc000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   5100
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            24
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    65323860(0x3e4c354) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65323860(0x3e4c354) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65323860(0x3e4c354) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1030
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon RX 6800
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
  Chip ID:                 29631(0x73bf)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2475
  BDFID:                   768
  Internal Node ID:        1
  Compute Unit:            60
  SIMDs per CU:            2
  Shader Engines:          8
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
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
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16760832(0xffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1030
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