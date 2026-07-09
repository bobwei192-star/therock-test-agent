# Rocm unable to detect GPU (Warn: GPU not getting identified)

- **Issue #:** 2995
- **State:** closed
- **Created:** 2024-04-04T11:07:06Z
- **Updated:** 2025-03-21T17:56:03Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/2995

We have installed the Rocm packages but it is unable to recognize the GPU. We have followed https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html to install the Rocm software.

"rocm-smi" returns WARNING: No AMD GPUs specified

GPU type: [Radeon Pro V620 MxGPU]
OS: Rhel 8.9

```
[root@amd-gpu ]# cat /etc/*release* | grep -i version
VERSION="8.9 (Ootpa)"
VERSION_ID="8.9"
REDHAT_BUGZILLA_PRODUCT_VERSION=8.9
REDHAT_SUPPORT_PRODUCT_VERSION="8.9"

[root@amd-gpu]# lspci -nn | grep -i amd
0002:00:00.0 Display controller [0380]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 21 [Radeon Pro V620 MxGPU] [1002:73ae]

```

after the installation, we rebooted the VM and when we ran "rocminfo" it failed with an error "Rock module not loaded"
```
[root@amd-gpu]# rocminfo
ROCk module is NOT loaded, possibly no GPU devices
[root@amd-gpu]#
```
then we added the module manually by running "**modprobe amdgpu**" The earlier issue was solved but it is unable to detect the GPU.
```
[root@amd-gpu]# modprobe amdgpu
[root@amd-gpu]# rocminfo
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD EPYC 7763 64-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD EPYC 7763 64-Core Processor
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
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            8
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    16074216(0xf545e8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16074216(0xf545e8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16074216(0xf545e8) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*** Done ***

[root@amd-gpu]# rocminfo | grep -i gfx
[root@amd-gpu]# rocminfo | grep -i gpu
[root@amd-gpu]#
```
rocm-smi output
```
[root@amd-gpu]# rocm-smi


WARNING: No AMD GPUs specified
=================================== ROCm System Management Interface ===================================
============================================= Concise Info =============================================
Device  [Model : Revision]  Temp    Power  Partitions      SCLK  MCLK  Fan  Perf  PwrCap  VRAM%  GPU%
        Name (20 chars)     (Edge)  (Avg)  (Mem, Compute)
========================================================================================================
========================================================================================================
========================================= End of ROCm SMI Log ==========================================
[root@amd-gpu]#
```
amdgpu module was loaded but still GPU is unidentified.
```
[root@amd-gpu]# lsmod | grep amdgpu
amdgpu              11243520  0
amddrm_ttm_helper      16384  1 amdgpu
amdttm                 77824  2 amdgpu,amddrm_ttm_helper
amdxcp                 16384  1 amdgpu
amddrm_buddy           20480  1 amdgpu
amd_sched              45056  1 amdgpu
amdkcl                 36864  3 amd_sched,amdttm,amdgpu
video                  53248  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
drm_display_helper    155648  1 amdgpu
drm_kms_helper        184320  2 drm_display_helper,amdgpu
drm                   602112  9 drm_kms_helper,amd_sched,amdttm,drm_display_helper,amdgpu,amddrm_buddy,amdkcl,amddrm_ttm_helper,amdxcp
[root@amd-gpu]#
```

We are planning to consume GPU by running pytorch application but since the driver is unable to recognise the GPU we are stuck and now looking for quick support, let us know if any further logs are needed.
