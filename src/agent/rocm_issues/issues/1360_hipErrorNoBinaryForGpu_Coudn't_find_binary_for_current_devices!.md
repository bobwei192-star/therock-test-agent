# "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!"

> **Issue #1360**
> **状态**: closed
> **创建时间**: 2021-01-15T18:49:30Z
> **更新时间**: 2021-01-20T05:11:35Z
> **关闭时间**: 2021-01-20T05:09:29Z
> **作者**: dllu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1360

## 描述

I am trying to run the unit tests on AMDMiGraphX and am getting a lot of test failures with `"hipErrorNoBinaryForGpu: Coudn't find binary for current devices!"` from various parts of the ROCm stack. 

Distro: Arch Linux
Linux kernel: 5.10.6
GPU: AMD Radeon RX 6800
ROCm version: 4.0.0

`rocminfo` output:

```
rocminfo
ROCk module is loaded
Able to open /dev/kfd read-write
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
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65834580(0x3ec8e54) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65834580(0x3ec8e54) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx1030
  Uuid:                    GPU-XX
  Marketing Name:          Device 73bf
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 29631(0x73bf)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2475
  BDFID:                   2560
  Internal Node ID:        1
  Compute Unit:            60
  SIMDs per CU:            4
  Shader Engines:          8
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        64(0x40)
  Max Work-item Per CU:    2048(0x800)
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

---

## 评论 (5 条)

### 评论 #1 — xuhuisheng (2021-01-16T00:32:41Z)

rdna2 didnot get official support for now. Good news is AMD said it will be support in 2021.

Confirmed that we can compile ROCm for navi21 successfully. https://github.com/xuhuisheng/rocm-build/tree/develop/navi21
But I am afraid that navi21 had same problem about un-changed loss value on convolution layer.

---

### 评论 #2 — ROCmSupport (2021-01-18T06:47:57Z)

@dllu , 
   Thank you for notifying this problem. Let me check for this problem.

---

### 评论 #3 — ROCmSupport (2021-01-19T04:09:02Z)

@dllu,
     Could you kindly let me know how are you compiling & executing your test case?
     A detail log would be helpful.


---

### 评论 #4 — dllu (2021-01-19T04:29:02Z)

For example the error happens when I run `make check` in the [AMDMIGraphX](https://github.com/ROCmSoftwarePlatform/AMDMIGraphX) repo. The full stderr log of `make check` is attached. The code has compiled fine, however.

[test.log](https://github.com/RadeonOpenCompute/ROCm/files/5833642/test.log)


---

### 评论 #5 — ROCmSupport (2021-01-20T05:09:28Z)

@dllu ,
    We are currently not supporting your rdna2 architecture for compute as mentioned by @xuhuisheng   :

> rdna2 didnot get official support for now. Good news is AMD said it will be support in 2021.
> 

Although we shall be supporting this soon.  Kindly look for any announcement from AMD for compute support.


---
