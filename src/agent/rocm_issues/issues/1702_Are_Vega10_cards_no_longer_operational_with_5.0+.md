# Are Vega10 cards no longer operational with 5.0+?

> **Issue #1702**
> **状态**: closed
> **创建时间**: 2022-03-15T16:38:59Z
> **更新时间**: 2025-07-12T23:44:09Z
> **关闭时间**: 2022-03-19T17:13:31Z
> **作者**: wreckdump
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1702

## 描述

I am confused about the EOL for Vega10 cards. Does this mean that Vega10 cards are no longer usable, as in no longer are detected by the ROCm driver stack and the runtime components, under ROCm 5.0+? Or is it just that there won't be any updates yet they are still usable (running HIP and OpenCL codes)? Could you please clarify this? Thanks.

---

## 评论 (12 条)

### 评论 #1 — ramin-raeisi (2022-03-16T23:56:54Z)

I am a fan of this question as I have a RX Vega 56(Vega 10) and wonder if it is supported or not, however I have segmentation faults with ROCm v4.5.2 and can not run any sample

---

### 评论 #2 — perestoronin (2022-03-17T08:54:09Z)

Please provide full cases to test, I have Vega Frontier cards, and can approve on decline issue with Vega's on rocm 5.0.2 in linux environment.

---

### 评论 #3 — ramin-raeisi (2022-03-17T09:12:07Z)

@perestoronin Could you please tell me which GPU are you exactly using successfully with ROCm 5.0.2? And also please tell me about the kernel version you have installed dkms driver into

---

### 评论 #4 — perestoronin (2022-03-18T11:16:50Z)

Native amdgpu driver from `Linux 5.16.15` with some known amdgpu patches without use dkms
```
rocm-smi -a
...
GPU[0]          : Card series:          Vega 10 XTX [Radeon Vega Frontier Edition]
GPU[0]          : Card vendor:          Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]          : Card SKU:             D05011
...
```
```
# hipcc --version
HIP version: 5.0.13601-
clang version 14.0.0
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-5.0.2/llvm/bin
```
```
hipconfig 
HIP version  : 5.0.13601-

== hipconfig
HIP_PATH     : /opt/rocm-5.0.2/hip
ROCM_PATH    : /opt/rocm-5.0.2
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm-5.0.2/hip/include -I/opt/rocm-5.0.2/llvm/bin/../lib/clang/14.0.0 -I/opt/rocm-5.0.2/include

== hip-clang
HSA_PATH         : /opt/rocm-5.0.2
HIP_CLANG_PATH   : /opt/rocm-5.0.2/llvm/bin
clang version 14.0.0
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-5.0.2/llvm/bin
AOMP-12.0-3 (http://github.com/ROCm-Developer-Tools/aomp):
 Source ID:12.0-3-bebd719ff2bb58a4220658c708f91d486729dbc1
  LLVM version 14.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags :  -std=c++17 -isystem "/opt/rocm-5.0.2/llvm/lib/clang/14.0.0/include/.." -isystem /opt/rocm-5.0.2/include -isystem "/opt/rocm-5.0.2/hip/include" -O2
hip-clang-ldflags  :  -L"/opt/rocm-5.0.2/hip/lib" -O2 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/bin:/usr/lib/llvm/13/bin:/usr/lib64/subversion/bin:/opt/cuda/bin:/opt/rocm-5.0.2/hip/bin:/opt/rocm-5.0.2/llvm/bin
HSA_PATH=/opt/rocm-5.0.2
HIP_PATH=/opt/rocm-5.0.2/hip
HIP_PLATFORM=amd

== Linux Kernel
...
Linux 5.16.15 AuthenticAMD GNU/Linux
...
```
[rocminfo](https://gist.github.com/raw/6c94d453f4aefc16d408055c07afc826)


---

### 评论 #5 — perestoronin (2022-03-18T11:36:38Z)

I use successful rocm from version old 2.0 (Vega 56) in past to 5.0.2 now with Vega Frontier cards, but now I have only Vega Frontier cards, and plan migrate to Vega 20 and Instinct cards and sell Vega Frontier cards after obtain new cards.

---

### 评论 #6 — wreckdump (2022-03-18T14:04:19Z)

@perestoronin So, with Vega Frontier you can run your HIP or OpenCL code under ROCm version 5.0.2?

---

### 评论 #7 — perestoronin (2022-03-19T17:04:03Z)

> @perestoronin So, with Vega Frontier you can run your HIP or OpenCL code under ROCm version 5.0.2?

yes, self-compiled ethminer and hashcat works with rocm 5.0.2 on Vega cards, but in near future version rocm, I affraid, will lost support Vega cards as in past rocm lost support more old cards 

---

### 评论 #8 — wreckdump (2022-03-19T17:04:58Z)

> > @perestoronin So, with Vega Frontier you can run your HIP or OpenCL code under ROCm version 5.0.2?
> 
> yes, self-compiled ethminer and hashcat works with rocm

Version 5.0.2, yes?

---

### 评论 #9 — perestoronin (2022-03-19T17:11:10Z)

> > > @perestoronin So, with Vega Frontier you can run your HIP or OpenCL code under ROCm version 5.0.2?
> > 
> > 
> > yes, self-compiled ethminer and hashcat works with rocm
> 
> Version 5.0.2, yes?

yes, except rocm-smi from rocm-smi-libs, for Vega card I use old rocm-smi 4.0.0 with libs from 5.0.2  rocm-smi-lib, other packages (all self compiled) from rocm 5.0.2 sources.

---

### 评论 #10 — wreckdump (2022-03-19T17:13:31Z)

> > > > @perestoronin So, with Vega Frontier you can run your HIP or OpenCL code under ROCm version 5.0.2?
> > > 
> > > 
> > > yes, self-compiled ethminer and hashcat works with rocm
> > 
> > 
> > Version 5.0.2, yes?
> 
> yes, except rocm-smi from rocm-smi-libs, for Vega card I use old rocm-smi 4.0.0 with libs from 5.0.2 rocm-smi-lib, other packages (all self compiled) from rocm 5.0.2 sources.

Thank you for the clarification!

---

### 评论 #11 — ramin-raeisi (2022-03-20T17:31:35Z)

I have a Radeon RX Vega 56(Vega 10) and can confirm it is working properly in the 5th version. I am using HIP.

---

### 评论 #12 — rajhlinux (2025-07-12T23:44:09Z)

What about V320 Cards, any support for these or which ROCm use to support it? 

---
