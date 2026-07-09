# [Issue]: Intermittent GPU Hang HW Exception by GPU on MI300X when training with axolotl

- **Issue #:** 4021
- **State:** closed
- **Created:** 2024-11-09T16:36:14Z
- **Updated:** 2026-02-05T15:03:12Z
- **Labels:** Under Investigation, AMD Instinct MI300X, ROCm 6.2.3
- **URL:** https://github.com/ROCm/ROCm/issues/4021

### Problem Description

When running [axolotl](https://github.com/axolotl-ai-cloud/axolotl/) runs, I get intermittent GPU hangs:

```
{'loss': 0.4589, 'grad_norm': 1.0493940198290594, 'learning_rate': 5.284132841328413e-06, 'epoch': 1.22}
 41%|██████████████████████████████████████████▌                                                              | 366/903 [5:15:39<6:53:09, 46.16s/it]HW Exception by GPU node-9 (Agent handle: 0x631351bb5a20) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x64ff272d8ab0) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x565d634d8610) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x5ea50312c910) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x619acaf10aa0) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x5ab551f9f310) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x5e2772f37790) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x5a6c6e4a4680) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x582b7268cac0) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x5b5e27441f40) reason :GPU Hang
HW Exception by GPU node-9 (Agent handle: 0x5c6c69e57ff0) reason :GPU Hang
Aborted (core dumped)
(axolotl) 134 hotaisle@ENC1-CLS01-SVR14:~/shisa-v2/train/ablations$ [rank2]:[E1109 16:13:20.222288244 ProcessGroupNCCL.cpp:616] [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=500045, OpType=_REDUCE_SCATTER_BASE, NumelIn=67108864, NumelOut=8388608, Timeout(ms)=600000) ran for 600038 milliseconds before timing out.
[rank2]:[E1109 16:13:20.222705810 ProcessGroupNCCL.cpp:1785] [PG ID 1 PG GUID 1 Rank 2] Exception (either an error or timeout) detected by watchdog at work: 500045, last enqueued NCCL work: 500047, last completed NCCL work: 500044.
[rank7]:[E1109 16:13:20.230357202 ProcessGroupNCCL.cpp:616] [Rank 7] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=500045, OpType=_REDUCE_SCATTER_BASE, NumelIn=67108864, NumelOut=8388608, Timeout(ms)=600000) ran for 600046 milliseconds before timing out.
[rank7]:[E1109 16:13:20.230674458 ProcessGroupNCCL.cpp:1785] [PG ID 1 PG GUID 1 Rank 7] Exception (either an error or timeout) detected by watchdog at work: 500045, last enqueued NCCL work: 500047, last completed NCCL work: 500044.
[rank3]:[E1109 16:13:20.249114105 ProcessGroupNCCL.cpp:616] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=500045, OpType=_REDUCE_SCATTER_BASE, NumelIn=67108864, NumelOut=8388608, Timeout(ms)=600000) ran for 600065 milliseconds before timing out.
[rank3]:[E1109 16:13:20.249396998 ProcessGroupNCCL.cpp:1785] [PG ID 1 PG GUID 1 Rank 3] Exception (either an error or timeout) detected by watchdog at work: 500045, last enqueued NCCL work: 500045, last completed NCCL work: 500044.
[rank4]:[E1109 16:13:20.252514562 ProcessGroupNCCL.cpp:616] [Rank 4] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=500045, OpType=_REDUCE_SCATTER_BASE, NumelIn=67108864, NumelOut=8388608, Timeout(ms)=600000) ran for 600068 milliseconds before timing out.
[rank4]:[E1109 16:13:20.252770852 ProcessGroupNCCL.cpp:1785] [PG ID 1 PG GUID 1 Rank 4] Exception (either an error or timeout) detected by watchdog at work: 500045, last enqueued NCCL work: 500045, last completed NCCL work: 500044.
[rank6]:[E1109 16:13:20.262103416 ProcessGroupNCCL.cpp:616] [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=500045, OpType=_REDUCE_SCATTER_BASE, NumelIn=67108864, NumelOut=8388608, Timeout(ms)=600000) ran for 600078 milliseconds before timing out.
[rank6]:[E1109 16:13:20.262386071 ProcessGroupNCCL.cpp:1785] [PG ID 1 PG GUID 1 Rank 6] Exception (either an error or timeout) detected by watchdog at work: 500045, last enqueued NCCL work: 500045, last completed NCCL work: 500044.
[rank1]:[E1109 16:13:20.273208899 ProcessGroupNCCL.cpp:616] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=500045, OpType=_REDUCE_SCATTER_BASE, NumelIn=67108864, NumelOut=8388608, Timeout(ms)=600000) ran for 600089 milliseconds before timing out.
[rank1]:[E1109 16:13:20.273362088 ProcessGroupNCCL.cpp:1785] [PG ID 1 PG GUID 1 Rank 1] Exception (either an error or timeout) detected by watchdog at work: 500045, last enqueued NCCL work: 500047, last completed NCCL work: 500044.
```

Note, the GPUs are left in a bad state (despite a reset being reported in dmesg, logs included below):
```
============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK    MCLK    Fan  Perf  PwrCap  VRAM%  GPU%
^[3m              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                  ^[0m
==========================================================================================================================
0       2     0x74a1,   55354  48.0°C      145.0W    NPS1, SPX, 0        132Mhz  900Mhz  0%   auto  750.0W  1%     0%
1       3     0x74a1,   41632  40.0°C      138.0W    NPS1, SPX, 0        131Mhz  900Mhz  0%   auto  750.0W  75%    0%
2       4     0x74a1,   47045  42.0°C      135.0W    NPS1, SPX, 0        132Mhz  900Mhz  0%   auto  750.0W  74%    0%
3       5     0x74a1,   60169  49.0°C      150.0W    NPS1, SPX, 0        132Mhz  900Mhz  0%   auto  750.0W  74%    0%
4       6     0x74a1,   56024  47.0°C      146.0W    NPS1, SPX, 0        132Mhz  900Mhz  0%   auto  750.0W  75%    0%
5       7     0x74a1,   705    42.0°C      139.0W    NPS1, SPX, 0        132Mhz  900Mhz  0%   auto  750.0W  1%     0%
6       8     0x74a1,   59108  48.0°C      147.0W    NPS1, SPX, 0        132Mhz  900Mhz  0%   auto  750.0W  75%    0%
7       9     0x74a1,   10985  40.0°C      138.0W    NPS1, SPX, 0        132Mhz  900Mhz  0%   auto  750.0W  74%    0%
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================
```

VRAM remains in use. Running an additional GPU reset does not work: `sudo amd-smi reset -g 0 -G`, a full system reboot is required to clear this up.

This seems to happen on about half of my runs (that are greater than a few hours).

### Operating System

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### CPU

Intel(R) Xeon(R) Platinum 8470

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.2.3

### ROCm Component

_No response_

### Steps to Reproduce

Install and run axolotl, eg:
```
accelerate launch -m axolotl.cli.train mi300x-llama3.1-70b-fft.dsz3.yaml
```
You can see https://github.com/AUGMXNT/MI300-testing/ or https://github.com/shisa-ai/shisa-v2/tree/main/train/ablations for some sample yaml files (I am running llama3-70b ffts that take about 12-20h to do)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support
```
ROCk module version 6.8.5 is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.14
Runtime Ext Version:     1.6
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
  Name:                    Intel(R) Xeon(R) Platinum 8470
  Uuid:                    CPU-XX
  Marketing Name:          Intel(R) Xeon(R) Platinum 8470
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
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3800
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            104
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    1056364836(0x3ef6d924) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    1056364836(0x3ef6d924) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    1056364836(0x3ef6d924) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    Intel(R) Xeon(R) Platinum 8470
  Uuid:                    CPU-XX
  Marketing Name:          Intel(R) Xeon(R) Platinum 8470
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             CPU
  Cache Info:
    L1:                      49152(0xc000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3800
  BDFID:                   0
  Internal Node ID:        1
  Compute Unit:            104
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    1056871544(0x3efe9478) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    1056871544(0x3efe9478) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    1056871544(0x3efe9478) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 3
*******
  Name:                    gfx942
  Uuid:                    GPU-07386a321fa45d1e
  Marketing Name:          AMD Instinct MI300X
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
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   6912
  Internal Node ID:        2
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
Agent 4
*******
  Name:                    gfx942
  Uuid:                    GPU-c14abb436c69353f
  Marketing Name:          AMD Instinct MI300X
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    3
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   15616
  Internal Node ID:        3
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
Agent 5
*******
  Name:                    gfx942
  Uuid:                    GPU-4be0e20b12ab7fa1
  Marketing Name:          AMD Instinct MI300X
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    4
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   19968
  Internal Node ID:        4
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
Agent 6
*******
  Name:                    gfx942
  Uuid:                    GPU-18c80aec63536c85
  Marketing Name:          AMD Instinct MI300X
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    5
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   24320
  Internal Node ID:        5
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
Agent 7
*******
  Name:                    gfx942
  Uuid:                    GPU-98c78750297b3198
  Marketing Name:          AMD Instinct MI300X
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    6
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   40192
  Internal Node ID:        6
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
Agent 8
*******
  Name:                    gfx942
  Uuid:                    GPU-c8d0ce1363e0130e
  Marketing Name:          AMD Instinct MI300X
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    7
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   48384
  Internal Node ID:        7
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
Agent 9
*******
  Name:                    gfx942
  Uuid:                    GPU-fdee8fae2de9f2b6
  Marketing Name:          AMD Instinct MI300X
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    8
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   52480
  Internal Node ID:        8
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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
Agent 10
*******
  Name:                    gfx942
  Uuid:                    GPU-6f890acb8eb0492b
  Marketing Name:          AMD Instinct MI300X
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    9
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29857(0x74a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   56576
  Internal Node ID:        9
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    201310208(0xbffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
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

Here's what the `dmesg` looks like:
```
[76914.152141] amdgpu 0000:dd:00.0: {1}uncorrectable hardware error(ERREVENT_ATHUB_INTERRUPT) detected!
[76914.152174] amdgpu 0000:3d:00.0: amdgpu: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
[76914.152926] amdgpu 0000:1b:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.152940] amdgpu 0000:1b:00.0: {1}[Hardware Error]: aca entry[00].STATUS=0xbaa000000000080b
[76914.152948] amdgpu 0000:1b:00.0: {1}[Hardware Error]: aca entry[00].ADDR=0x0000000000000000
[76914.152953] amdgpu 0000:1b:00.0: {1}[Hardware Error]: aca entry[00].MISC0=0xd008000100000000
[76914.152957] amdgpu 0000:1b:00.0: {1}[Hardware Error]: aca entry[00].IPID=0x0001d02e1f007900
[76914.152961] amdgpu 0000:1b:00.0: {1}[Hardware Error]: aca entry[00].SYND=0x000000005d003e1b
[76914.156884] amdgpu: Failed to restore process queues
[76914.156901] amdgpu: Failed to restore process queues
[76914.156914] amdgpu: Failed to restore process queues
[76914.156925] amdgpu: Failed to restore process queues
[76914.156935] amdgpu: Failed to restore process queues
[76914.156945] amdgpu: Failed to restore process queues
[76914.156956] amdgpu: Failed to restore process queues
[76914.156965] amdgpu: Failed to restore process queues
[76914.184889] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.184894] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[00].STATUS=0xd820000000060150
[76914.184898] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[00].ADDR=0x0000000000000000
[76914.184902] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[00].MISC0=0xd008005100000000
[76914.184906] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[00].IPID=0x0000605011a09201
[76914.184910] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[00].SYND=0x009c732d4a000000
[76914.185363] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.185366] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[01].STATUS=0xd820000000060150
[76914.185370] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[01].ADDR=0x0000000000000000
[76914.185373] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[01].MISC0=0xd008003100000000
[76914.185377] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[01].IPID=0x0000605011a09201
[76914.185381] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[01].SYND=0x009c752d4a000000
[76914.185838] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.185842] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[02].STATUS=0xd820000000060400
[76914.185846] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[02].ADDR=0x0000000000000000
[76914.185850] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[02].MISC0=0xd008008100000000
[76914.185853] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[02].IPID=0x0000605011a09201
[76914.185857] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[02].SYND=0x00000000809c812d
[76914.186309] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.186313] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[03].STATUS=0xd820000000060150
[76914.186316] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[03].ADDR=0x0000000000000000
[76914.186320] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[03].MISC0=0xd008000400000000
[76914.186324] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[03].IPID=0x0000605011a09201
[76914.186327] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[03].SYND=0x009c812d4a000000
[76914.186783] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.186786] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[04].STATUS=0xd820000000060150
[76914.186790] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[04].ADDR=0x0000000000000000
[76914.186794] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[04].MISC0=0xd00800f800000000
[76914.186797] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[04].IPID=0x0000605011a09201
[76914.186801] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[04].SYND=0x009c812d4a000000
[76914.187259] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.187262] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[05].STATUS=0xd820000000060150
[76914.187266] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[05].ADDR=0x0000000000000000
[76914.187269] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[05].MISC0=0xd008005100000000
[76914.187273] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[05].IPID=0x0000605011a09201
[76914.187277] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[05].SYND=0x009c752d4a000000
[76914.187740] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.187744] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[06].STATUS=0xd820000000060150
[76914.187748] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[06].ADDR=0x0000000000000000
[76914.187751] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[06].MISC0=0xd008004000000000
[76914.187755] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[06].IPID=0x0000605011a09201
[76914.187759] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[06].SYND=0x009c752d4a000000
[76914.188214] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.188217] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[07].STATUS=0xd820000000060150
[76914.188221] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[07].ADDR=0x0000000000000000
[76914.188225] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[07].MISC0=0xd008002000000000
[76914.188228] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[07].IPID=0x0000605011a09201
[76914.188232] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[07].SYND=0x009c752d4a000000
[76914.188696] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.188700] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[08].STATUS=0xd820000000060150
[76914.188704] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[08].ADDR=0x0000000000000000
[76914.188708] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[08].MISC0=0xd00800a400000000
[76914.188711] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[08].IPID=0x0000605011a09201
[76914.188715] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[08].SYND=0x009c752d4a000000
[76914.189163] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.189166] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[09].STATUS=0xd820000000060150
[76914.189169] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[09].ADDR=0x0000000000000000
[76914.189172] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[09].MISC0=0xd008005000000000
[76914.189175] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[09].IPID=0x0000605011a09201
[76914.189178] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[09].SYND=0x009c752d4a000000
[76914.189644] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.189647] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[10].STATUS=0xd820000000060150
[76914.189651] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[10].ADDR=0x0000000000000000
[76914.189655] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[10].MISC0=0xd008012400000000
[76914.189658] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[10].IPID=0x0000605011a09201
[76914.189662] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[10].SYND=0x009c812d4a000000
[76914.190110] amdgpu 0000:9d:00.0: {1}[Hardware Error]: Accelerator Check Architecture events logged
[76914.190112] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[11].STATUS=0xd820000000060150
[76914.190116] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[11].ADDR=0x0000000000000000
[76914.190119] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[11].MISC0=0xd008013500000000
[76914.190122] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[11].IPID=0x0000605011a09201
[76914.190126] amdgpu 0000:9d:00.0: {1}[Hardware Error]: aca entry[11].SYND=0x009c812d4a000000
[76914.190522] amdgpu 0000:9d:00.0: {1}socket: 6, die: 1, 1533 new correctable hardware errors detected in xgmi_wafl block
[76914.190529] amdgpu 0000:9d:00.0: {1}socket: 6, die: 1, 1533 correctable hardware errors detected in total in xgmi_wafl block
[76914.214195] amdgpu 0000:dd:00.0: amdgpu: GPU reset begin!
[76914.216568] Pid 1230312(python3.12) over core_pipe_limit
[76914.216571] Skipping core dump
[76914.237823] amdgpu 0000:dd:00.0: amdgpu: Dumping IP State
[76914.237826] amdgpu 0000:dd:00.0: amdgpu: Dumping IP State Completed
[76914.238315] amdgpu 0000:1b:00.0: amdgpu: MODE1 reset
[76914.238316] amdgpu 0000:dd:00.0: amdgpu: MODE1 reset
[76914.238321] amdgpu 0000:dd:00.0: amdgpu: GPU mode1 reset
[76914.238320] amdgpu 0000:3d:00.0: amdgpu: MODE1 reset
[76914.238322] amdgpu 0000:1b:00.0: amdgpu: GPU mode1 reset
[76914.238321] amdgpu 0000:4e:00.0: amdgpu: MODE1 reset
[76914.238322] amdgpu 0000:bd:00.0: amdgpu: MODE1 reset
[76914.238323] amdgpu 0000:9d:00.0: amdgpu: MODE1 reset
[76914.238323] amdgpu 0000:5f:00.0: amdgpu: MODE1 reset
[76914.238324] amdgpu 0000:cd:00.0: amdgpu: MODE1 reset
[76914.238329] amdgpu 0000:9d:00.0: amdgpu: GPU mode1 reset
[76914.238330] amdgpu 0000:5f:00.0: amdgpu: GPU mode1 reset
[76914.238332] amdgpu 0000:bd:00.0: amdgpu: GPU mode1 reset
[76914.238334] amdgpu 0000:4e:00.0: amdgpu: GPU mode1 reset
[76914.238336] amdgpu 0000:cd:00.0: amdgpu: GPU mode1 reset
[76914.238337] amdgpu 0000:3d:00.0: amdgpu: GPU mode1 reset
[76914.240668] amdgpu 0000:dd:00.0: amdgpu: GPU smu mode1 reset
[76914.241079] amdgpu 0000:cd:00.0: amdgpu: GPU smu mode1 reset
[76914.241104] amdgpu 0000:1b:00.0: amdgpu: GPU smu mode1 reset
[76914.241152] amdgpu 0000:5f:00.0: amdgpu: GPU smu mode1 reset
[76914.241257] amdgpu 0000:3d:00.0: amdgpu: GPU smu mode1 reset
[76914.241282] amdgpu 0000:4e:00.0: amdgpu: GPU smu mode1 reset
[76914.243199] amdgpu 0000:9d:00.0: amdgpu: GPU smu mode1 reset
[76914.243283] amdgpu 0000:bd:00.0: amdgpu: GPU smu mode1 reset
[76919.010450] amdgpu 0000:dd:00.0: amdgpu: GPU reset succeeded, trying to resume
[76919.011774] [drm] PCIE GART of 512M enabled.
[76919.011779] [drm] PTB located at 0x000002EFED700000
[76919.011910] [drm] VRAM is lost due to GPU reset!
```