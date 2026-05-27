# ROCM source code for AARCH64

> **Issue #231**
> **状态**: closed
> **创建时间**: 2017-10-23T00:47:40Z
> **更新时间**: 2017-10-23T14:14:24Z
> **关闭时间**: 2017-10-23T14:14:24Z
> **作者**: zhaojunfan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/231

## 描述

Hi, I want to know which branch of rocm source code can be used on aarch64 now? I mean for all components. 
1.ROCK-Kernel-Driver
2.ROCT-Thunk-Interface
3.ROCR-Runtime
4.ROCm-Device-Libs
5.compiler-runtime
6.HCC
7.HIP
8.ROC-smi
9.ATMI

if they are all ready for aarch64 now? @gstoner 

Thanks!

---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-10-23T14:14:06Z)

1.ROCK-Kernel-Driver. <- this base support was in ROCm 1.6
2.ROCT-Thunk-Interface <- this base support was in ROCm 1.6
3.ROCR-Runtime. <- this needed new clean up see bellow -going upstream
4.ROCm-Device-Libs <-  this has zero dependencies on ARM
5.compiler-runtime <-  this has zero dependencies on ARM
6.HCC <- this is going out now
7.HIP <- this is going out now  
8.ROC-smi <- this python script  <-  this has zero dependencies on ARM

The issue on the thunder X system is you need to force PCIe  Platform Atomics/Atomic Completors to get the stack working 

ROCr change we upstreaming 
// Try to detect CPU endianness
#if !defined(LITTLEENDIAN_CPU) && !defined(BIGENDIAN_CPU)
#if defined(__i386__) || defined(__x86_64__) || defined(_M_IX86) || \
-    defined(_M_X64)
+    defined(_M_X64) || defined(__aarch64__)
#define LITTLEENDIAN_CPU
#endif
#endif

To fix the atomic completor issue 

$ sudo setpci -v -s 0005:8f:00.0 98.b=60
0005:8f:00.0 @98 60
 
$ ./simple_dispatch
Failed to get Processor Vendor. Setting to GenuineIntel
Initializing the hsa runtime succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The GPU agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
Creating a HSA signal succeeded.
Finding a host fine grained memory region succeeded.
Allocating host fine grained memory for kernel code object succeeded.
Dispatching the kernel succeeded.
Dispatch successfully completed.
Freeing kernel code object memory succeeded.
Destroying the signal succeeded.
Destroying the queue succeeded.
Shutting down the runtime succeeded.

---
