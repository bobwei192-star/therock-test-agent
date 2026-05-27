# Synchronizing Deadlock by libhskmt.so  and libmcwamp.so.3

> **Issue #1120**
> **状态**: closed
> **创建时间**: 2020-05-29T08:29:01Z
> **更新时间**: 2020-12-01T17:26:10Z
> **关闭时间**: 2020-12-01T17:26:10Z
> **作者**: SocratesWong
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1120

## 描述

When executing the HIP example code from https://github.com/ROCm-Developer-Tools/HIP-Examples/blob/roc-3.3.x/HIP-Examples-Applications/MatrixMultiplication/MatrixMultiplication.cpp, it is found for large data size [ex. 1000x1000 matrix multiplication ( -x 1000 -y 1000 -z 1000 )] that the kernel enters in a deadlock state.   The bug is currently reproducible with Vega 10 [Radeon Instinct MI25 MxGPU] with ubuntu18.04.4 LTS and HIP 3.3.20126.4629.  The follow environmental variables are set:
```
export HSA_ENABLE_SDMA=0
export HCC_SERIALIZE_KERNEL=3
export HCC_SERIALIZE_COPY=3

```

Code trace output:
```
<... hsa_queue_create resumed> )                                                       = 0
libmcwamp.so.3->hsa_amd_profiling_set_profiler_enabled(0x7f60d3742000, 1, 0xffffffff, 0) = 0
libmcwamp.so.3->hsa_queue_load_write_index_relaxed(0x7f60d3742000, 0xbef7c0, 0x7f60d0fff1d8, 0x440000) = 0
libmcwamp.so.3->hsa_queue_load_read_index_scacquire(0x7f60d3742000, 0xbef7c0, 0x7f60d1855d80, 0x440000) = 0
libmcwamp.so.3->hsa_signal_create(1, 0, 0, 0x7ffca5de4378 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffca5de4220, 0, 0, 0x7ffca5de4218)         = 0
<... hsa_signal_create resumed> )                                                      = 0
libmcwamp.so.3->hsa_queue_store_write_index_relaxed(0x7f60d3742000, 1, 0x7f60d3778058, 0xa10f30) = 0x7f60d3742000
libmcwamp.so.3->hsa_signal_store_relaxed(0x7f60d379a800, 0, 0x7f60d1855d50, 0xa10f30)  = 0
libmcwamp.so.3->hsa_signal_wait_scacquire(0x7f60d379a700, 2, 1, -1 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtWaitOnEvent(0x67cbaf0, 0xfffffffe, 0xbb300000000, 0x7f60d379a700 <unfinished ...>
libhsakmt.so.1->hsaKmtWaitOnMultipleEvents(0x7ffca5de4608, 1, 1, 0xfffffffe)           = 0
<... hsaKmtWaitOnEvent resumed> )                                                      = 0
<... hsa_signal_wait_scacquire resumed> )                                              = 0
libmcwamp.so.3->hsa_signal_create(1, 0, 0, 0x7ffca5de3970 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffca5de3850, 0, 0, 0x7ffca5de3848)         = 0
<... hsa_signal_create resumed> )                                                      = 0
libmcwamp.so.3->hsa_queue_load_write_index_relaxed(0x7f60d3742000, 0, 0x7f60d3778060, 0x7f60d379a680) = 1
libmcwamp.so.3->hsa_queue_load_read_index_scacquire(0x7f60d3742000, 0, 0x7f60d1855d80, 0x7f60d379a680) = 1
libmcwamp.so.3->hsa_queue_store_write_index_relaxed(0x7f60d3742000, 2, 0x7f60d1855db0, 0x7f5fc0200040) = 0x7f60d3742000
libmcwamp.so.3->hsa_signal_store_relaxed(0x7f60d379a800, 1, 0x7f60d1855d50, 0x7f5fc0200040) = 0
libmcwamp.so.3->hsa_signal_wait_scacquire(0x7f60d379a680, 2, 1, -1 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtWaitOnEvent(0x64bdbf0, 0xfffffffe, 0xbb300000000, 0x7f60d379a680 <unfinished ...>
libhsakmt.so.1->hsaKmtWaitOnMultipleEvents(0x7ffca5de3c68, 1, 1, 0xfffffffe <no return ...>

```
GPU information:
```
  Name:                    gfx900
  Marketing Name:          Vega 10 [Radeon Instinct MI25 MxGPU]
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    8
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 26732(0x686c)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   852
  BDFID:                   0
  Internal Node ID:        8
  Compute Unit:            64
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
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
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16449536(0xfb0000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx900
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

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2020-12-01T17:26:10Z)

I am unable to reproduce this as of at least ROCm 3.7, so I'm going to close the issue assuming it has been fixed. If you find the same problem again, please submit another issue and we can work to try to chase it down. Thanks!

---
