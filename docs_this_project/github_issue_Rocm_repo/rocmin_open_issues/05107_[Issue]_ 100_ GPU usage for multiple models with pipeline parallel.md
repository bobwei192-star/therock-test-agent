# [Issue]: 100% GPU usage for multiple models with pipeline parallel

- **Issue #:** 5107
- **State:** open
- **Created:** 2025-07-27T20:36:05Z
- **Updated:** 2026-06-30T19:31:43Z
- **Labels:** Under Investigation
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5107

### Problem Description

`rocm-smi` reports 100% GPU Usage when **multiple** models load with device_map="auto" on a multi-gpu host, idle state.

The 100% GPU issue looks like not a third-party library implementation problem. It happens to:
1. llama.cpp with "-dev ROCm0,ROCm1,...".
2. transformers (sentence_transformers) with device_map="auto"

process CPU usage is around 0%.

I am using gfx906 so I can only test on ROCm 6.3.3.


### Operating System

Arch Linux

### CPU

2 x Intel(R) Xeon(R) E5-2680 v4 (56) @ 3.30 GHz

### GPU

4x MI50 32GB

### ROCm Version

ROCm 6.3.3

### ROCm Component

_No response_

### Steps to Reproduce

Code to Reproduce:
```py
import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "Qwen/Qwen3-Embedding-0.6B",
    model_kwargs={
        "device_map": "auto",
        "torch_dtype": torch.float16
    },
    tokenizer_kwargs={"padding_side": "left"},
)
```

Steps to Reproduce:
1. Install torch with ROCm acceleration.
2. pip install sentence_transformers
3. run code above, in two seperate python terminal.

After First model load
```sh
=========================================== ROCm System Management Interface ===========================================
===================================================== Concise Info =====================================================
Device  Node  IDs              Temp    Power     Partitions          SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%
[3m              (DID,     GUID)  (Edge)  (Socket)  (Mem, Compute, ID)                                                     [0m
========================================================================================================================
0       2     0x66a1,   29631  45.0°C  24.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  4%     0%
1       3     0x66a1,   33535  47.0°C  19.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  1%     0%
2       4     0x66a1,   17183  43.0°C  18.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  1%     0%
3       5     0x66a1,   55003  43.0°C  18.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  2%     0%
========================================================================================================================
================================================= End of ROCm SMI Log ==================================================
```

After Second model load
```sh
============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp    Power     Partitions          SCLK     MCLK    Fan     Perf  PwrCap  VRAM%  GPU%
[3m              (DID,     GUID)  (Edge)  (Socket)  (Mem, Compute, ID)                                                      [0m
==========================================================================================================================
0       2     0x66a1,   29631  44.0°C  53.0W     N/A, N/A, 0         1725Mhz  350Mhz  15.69%  auto  225.0W  8%     100%
1       3     0x66a1,   33535  48.0°C  45.0W     N/A, N/A, 0         1725Mhz  350Mhz  16.08%  auto  225.0W  3%     100%
2       4     0x66a1,   17183  44.0°C  48.0W     N/A, N/A, 0         1725Mhz  350Mhz  14.51%  auto  225.0W  3%     100%
3       5     0x66a1,   55003  44.0°C  44.0W     N/A, N/A, 0         1725Mhz  350Mhz  14.51%  auto  225.0W  4%     100%
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================
```

After Second model **unload**
```sh
=========================================== ROCm System Management Interface ===========================================
===================================================== Concise Info =====================================================
Device  Node  IDs              Temp    Power     Partitions          SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%
[3m              (DID,     GUID)  (Edge)  (Socket)  (Mem, Compute, ID)                                                     [0m
========================================================================================================================
0       2     0x66a1,   29631  44.0°C  24.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  4%     0%
1       3     0x66a1,   33535  48.0°C  18.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  1%     0%
2       4     0x66a1,   17183  44.0°C  18.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  1%     0%
3       5     0x66a1,   55003  44.0°C  18.0W     N/A, N/A, 0         925Mhz  350Mhz  14.51%  auto  225.0W  2%     0%
========================================================================================================================
================================================= End of ROCm SMI Log ==================================================
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```sh
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
Runtime Ext Version:     1.6
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

......

*******
Agent 3
*******
  Name:                    gfx906
  Uuid:                    GPU-12b008e17337ecd9
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
    L2:                      8192(0x2000) KB
  Chip ID:                 26273(0x66a1)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1725
  BDFID:                   1024
  Internal Node ID:        2
  Compute Unit:            60
  SIMDs per CU:            4
  Shader Engines:          4
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
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    2560(0xa00)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 472
  SDMA engine uCode::      145
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    33538048(0x1ffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    33538048(0x1ffc000) KB
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
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
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
```

### Additional Information

Detailed test with llama.cpp:
1. If multiple MultiGPU models shares any same GPU, `shared GPU` usage goes to 100% instantly on load. `exclusive GPU` usage stays at 0%.
2. SingleGPU model + MultiGPU model works fine.

Test Table:

| First Model -dev | Second Model -dev | 100% GPU Usage (Idle) | 0% GPU Usage (Idle) |
| - | - | - | - |
| 0, 1 | 0, 1 | 0, 1| |
| 0, 1 | 1, 2 | 1|0, 2 |
| 0, 1 | 2, 3 | |0, 1, 2, 3 |
| 0, 1 | 1 | | 0, 1|
| 0, 1 | 2 | | 0, 1, 2|
| 0 | 1 | | 0, 1|

* number in cells: ROCm device index
