# MI100 initiallization issue on AM4 hardware

- **Issue #:** 2927
- **State:** closed
- **Created:** 2024-02-25T17:17:57Z
- **Updated:** 2024-10-01T17:05:38Z
- **Labels:** ROCm 6.0.0, AMD Instinct MI100
- **URL:** https://github.com/ROCm/ROCm/issues/2927

### Problem Description

MI100 fails to initialize and nothing works. I found the following error messages. The hardware works as expected in my AM5 setup. So, it's something about MB/CPU/BIOS set up that is incompatible. I found the [following post](https://forum.level1techs.com/t/amd-mi100-not-being-recognized/204303/2) and made sure to disable CSM and to enable Re-Bar & Above 4G address decoding. dmesg says probe failed with error -12. Is there anything else I can try? What does error -12 mean? 

>$ sudo dmesg | grep amd
[    0.000000] Linux version 5.15.0-97-generic (buildd@lcy02-amd64-033) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #107-Ubuntu SMP Wed Feb 7 13:26:48 UTC 2024 (Ubuntu 5.15.0-97.107-generic 5.15.136)
[    0.572509] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    6.476797] amdkcl: loading out-of-tree module taints kernel.
[    6.476835] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    6.556702] amdkcl: Warning: fail to get symbol __cancel_work, replace it with kcl stub
[    6.756137] [drm] amdgpu kernel modesetting enabled.
[    6.756144] [drm] amdgpu version: 6.3.6
[    6.761824] amdgpu: Virtual CRAT table created for CPU
[    6.761833] amdgpu: Topology: Add CPU node
[    6.770241] amdgpu: PeerDirect support was initialized successfully
[    6.770337] amdgpu 0000:09:00.0: enabling device (0000 -> 0003)
[    6.770371] amdgpu 0000:09:00.0: amdgpu: Fatal error during GPU init
[    6.770386] amdgpu: probe of 0000:09:00.0 failed with error -12
[    6.770390] amdgpu: legacy kernel without apple_gmux_detect()

Hardware:
Gigabyte B550I-AORUS-PRO-AX-rev-11, Latest BIOS (F18d), Ryzen 3900X, 32 GB RAM.


### Operating System

22.04.4 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 9 3900X 12-Core Processor

### GPU

AMD Instinct MI100

### ROCm Version

ROCm 6.0.0

### ROCm Component

rocminfo

### Steps to Reproduce

Just plug in the card and boot it up.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

$ /opt/rocm/bin/rocminfo --support
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
  Name:                    AMD Ryzen 9 3900X 12-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 9 3900X 12-Core Processor
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
  Max Clock Freq. (MHz):   3800
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
      Size:                    32754184(0x1f3ca08) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32754184(0x1f3ca08) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32754184(0x1f3ca08) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*** Done ***

### Additional Information

_No response_