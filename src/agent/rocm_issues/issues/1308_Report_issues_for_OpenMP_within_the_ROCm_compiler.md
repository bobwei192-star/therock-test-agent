# Report issues for OpenMP within the ROCm compiler

> **Issue #1308**
> **状态**: closed
> **创建时间**: 2020-11-27T11:58:08Z
> **更新时间**: 2022-02-22T12:49:23Z
> **关闭时间**: 2022-02-22T12:49:23Z
> **作者**: zjin-lcf
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1308

## 描述

Could you reproduce the following issues for offloading to an AMD GPU using OpenMP within the ROCm compiler ? When you can run any of the applications in my report successfully using your OpenMP within the ROCm compiler, please list them here. Then there may be some issues with my installation and/or build commands for these applications.

In each program with the suffix "-omp", there is a "Makefile.aomp". Please take a look at the file, and modify it for your environment. To build and run a program, go to a directory (e.g. all-pairs-distance-omp) and type

```
make -f Makefile.aomp run
```

Thanks.

The GPU results don't match the CPU results for the following OpenMP programs. 

https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/all-pairs-distance-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/compute-score-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/fft-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/amgmk-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/scan-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/axhelm-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/fpc-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/knn-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/lud-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/myoctye-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/nw-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/particlefilter-omp
https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/ccsd-trpdrv-omp

https://github.com/zjin-lcf/oneAPI-DirectProgramming/tree/master/crc64-omp
```
./main 10 5 33554432
Running 10 tests with seed 5
Loading global '_ZL11crc64_table' (Failed)
Libomptarget fatal error 1: failure of target construct while offloading is mandatory
make: *** [Makefile.aomp:65: run] Aborted (core dumped)
```


---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2020-11-27T12:22:13Z)

Thanks @zjin-lcf for reaching out.
Can you please respond with below answers.

**/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
/opt/rocm/bin/rocm-smi**

---

### 评论 #2 — ROCmSupport (2020-11-27T13:05:09Z)

Hi @zjin-lcf 
When I tried the first sample on my Radeon7 card, I got the below output.

/opt/rocm/llvm/bin/clang++ -std=c++14 -Wall  -O3 -target x86_64-pc-linux-gnu -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx906 -c main.cpp -o main.o
/opt/rocm/llvm/bin/clang++ -std=c++14 -Wall  -O3 -target x86_64-pc-linux-gnu -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx906 main.o -o main
./main
PASS
FAIL
Makefile.aomp:65: recipe for target 'run' failed
make: *** [run] Error 238


---

### 评论 #3 — zjin-lcf (2020-11-27T13:41:57Z)

I omitted the outputs of these programs, which directly/indirectly indicate CPU/GPU results mismatch, when reporting the issues for clarity.  Thanks for bringing my report to AOMP developers.

Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3204.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Vega 20 [Radeon VII]

*******
Agent 2
*******
  Name:                    gfx906
  Uuid:                    GPU-246660c172fd62df
  Marketing Name:          Vega 20 [Radeon VII]
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
  Chip ID:                 26287(0x66af)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1801
  BDFID:                   8960
  Internal Node ID:        1
  Compute Unit:            60
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
      Name:                    amdgcn-amd-amdhsa--gfx906
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

---

### 评论 #4 — estewart08 (2021-01-22T18:34:14Z)

In regards to all-pairs-distance-omp, the failure is a result of the compiler choosing to execute the second offload region as a SPMD kernel, which in turn makes the dist array become thread private instead of team private.  When the reduction occurs, thread 0 will only see an entry in dist[0] and everywhere else will be zeroed as it cannot see changes from other threads. This causes the check to fail due to having partial results. 

This should be a generic kernel as there is user code in between the target teams pragma and parallel region. Clang is explicitly looking over the int dist[THREADS] declaration because it is of a trivial type. For demonstration purposes, if you add 
```dist[0] = 0;``` after line 151, the kernel will be generic and the test passes.

Looking into filing a clang bug.

---

### 评论 #5 — zjin-lcf (2021-01-22T21:45:50Z)

I don't know what a generic kernel means, and if "user code exists or not between the two parallel regions" matters.  Thank you for explaining the issues in any case. 

---

### 评论 #6 — ROCmSupport (2022-02-22T12:49:23Z)

Hi @zjin-lcf 
The reported issues are fixed long back. Request to check with the latest ROCm 5.0.
Closing this, as the failures are not seen anymore.
Thank you.

---
