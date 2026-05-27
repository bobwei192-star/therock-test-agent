# Build OpenCL kernels using multiple threads failed

> **Issue #1467**
> **状态**: closed
> **创建时间**: 2021-05-10T08:00:51Z
> **更新时间**: 2021-05-13T06:13:39Z
> **关闭时间**: 2021-05-13T06:13:39Z
> **作者**: WyldeCat
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1467

## 描述

I'm trying to read multiple *.cl files and write pre-built *.bin files with multiple threads.
So I made a simple compiler and it works like this `./my_opencl_compiler foo.cl -o foo.bin`
It just create `clContext` with 1 AMD GPU and call `clBuildProgram()`, `clGetProgramInfo(..., CL_PROGRAM_BINARIES, ...)` to get the byte sequences.

But when I put compile command in Makefile and do `make -j`, it fails like this
```
Error: AMD HSA Code Object loading failed: HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed 
to allocate the necessary resources. This error may also occur when the core runtime library needs to
spawn threads or create internal OS-specific events.
```

Any suggestions?

ROCm : 4.0.0
OS : ubuntu 20.04.1 LTS
GPU : rx5700

---

## 评论 (5 条)

### 评论 #1 — b-sumner (2021-05-10T14:32:54Z)

Are you Release'ing the Program after you are done with it (and any other unneeded objects)?

---

### 评论 #2 — WyldeCat (2021-05-11T01:35:04Z)

> Are you Release'ing the Program after you are done with it (and any other unneeded objects)?

I fixed my program to release all cl objects.
But when it fails to compile a single kernel (because of syntax error), all threads are hanged, and rocm-smi results like below.
```
================================================================================
Expected integer value from monitor, but got ""
ERROR: 15 GPU[0]:Data (usually from reading a file) was not of the type that was expected
Expected integer value from monitor, but got ""
ERROR: 15 GPU[0]:Data (usually from reading a file) was not of the type that was expected
GPU  Temp   AvgPwr  SCLK    MCLK    Fan   Perf     PwrCap       VRAM%  GPU%
0    N/A    N/A     None    None    0.0%  unknown  Unsupported    0%   0%
```

---

### 评论 #3 — WyldeCat (2021-05-11T04:41:32Z)

Is there any way to build a OCL kernel with command line interface like `rocc foo.cl -o foo.bin -march=gfx1010`?

---

### 评论 #4 — b-sumner (2021-05-12T14:45:46Z)

@WyldeCat since the original resource leak is fixed, can we close this issue.  Regarding the other problem, can you please double check your code for other problems?  FWIW, the OpenCL runtime compiler is LLVM based and LLVM's use of global variables limits the amount of concurrency possible within the process.  It would probably be faster to keep your program single threaded and launch multiple instances on the command line when compiling many sources.

---

### 评论 #5 — WyldeCat (2021-05-13T06:13:18Z)

@b-sumner Thanks for the info

---
