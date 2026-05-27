# Support for RX6600XT (gfx1032,navi23)?

> **Issue #1698**
> **状态**: closed
> **创建时间**: 2022-03-03T08:03:06Z
> **更新时间**: 2024-09-24T14:20:28Z
> **关闭时间**: 2022-10-12T06:34:15Z
> **作者**: kubawis128
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1698

## 描述

Hi
I own an RX 6600XT amd gpu (gfx1032,Navi23)
I'd like to try machine learning on gpu (tensorflow or PyTorch) but when i install ROCm using official tool (amdgpu-install (rocm version 5.0.1) on ubuntu 20.4.3 with HWE kernel) i get an error that no HIP binary could be found for my gpu (hipErrorNoBinaryForGpu).
rocminfo shows my cpu and gpu as agents.
Hashcat from ubuntu repository shows error (clCreateCommandQueue(): CL_OUT_OF_HOST_MEMORY)
I have a few questions:
- Can i recompile rocm to support my gpu?
- When will my card get support?
- Is it problem with rocm or hip?

hipconfig --full output:
```
Warning: HIP_PLATFORM=hcc is deprecated. Please use HIP_PLATFORM=amd. 
HIP version  : 5.0.13601-6b731c37

== hipconfig
HIP_PATH     : /opt/rocm/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm/hip/include -I/opt/rocm/llvm/bin/../lib/clang/14.0.0 -I/opt/rocm/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm/hsa
HIP_CLANG_PATH   : /opt/rocm/llvm/bin
AMD clang version 14.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.0.0 22051 235b6880e2e515507478181ec11a20c1ec87945b)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
AMD LLVM version 14.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : Warning: HIP_PLATFORM=hcc is deprecated. Please use HIP_PLATFORM=amd. 
 -std=c++11 -isystem "/opt/rocm-5.0.0/llvm/lib/clang/14.0.0/include/.." -isystem /opt/rocm/hsa/include -isystem "/opt/rocm/hip/include" -O3
hip-clang-ldflags  : Warning: HIP_PLATFORM=hcc is deprecated. Please use HIP_PLATFORM=amd. 
 -L"/opt/rocm/hip/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/usr/local/bin:/opt/rocm/hcc/bin:/opt/rocm/hip/bin:/opt/rocm/bin:/opt/rocm/opencl/bin/x86_64:/usr/local/bin:/opt/rocm/hcc/bin:/opt/rocm/hip/bin:/opt/rocm/bin:/opt/rocm/opencl/bin/x86_64:/home/wisnia/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
LD_LIBRARY_PATH=:/opt/rocm/opencl/lib/x86_64:/opt/rocm/opencl/lib/x86_64
HIP_PATH=/opt/rocm/hip
HIP_PLATFORM=hcc
HIP_VISIBLE_DEVICES=0

== Linux Kernel
Hostname     : Wisnia-ML
Linux Wisnia-ML 5.13.0-30-generic #33~20.04.1-Ubuntu SMP Mon Feb 7 14:25:10 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.3 LTS
Release:	20.04
Codename:	focal
```
rocminfo output:
```
ROCk module is loaded
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
  Name:                    AMD Ryzen 5 3600 6-Core Processor  
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 3600 6-Core Processor  
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
  Max Clock Freq. (MHz):   3600                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    16323864(0xf91518) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16323864(0xf91518) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16323864(0xf91518) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1032                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 6600 XT              
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
    L2:                      2048(0x800) KB                     
    L3:                      32768(0x8000) KB                   
  Chip ID:                 29695(0x73ff)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2900                               
  BDFID:                   3072                               
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx1032         
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

## 评论 (28 条)

### 评论 #1 — ROCmSupport (2022-03-03T11:30:32Z)

Hi @kubawis128 
Currently ROCm 5.0 does not support Navi23.
Anyhow I will try to get some information on the support part and update you asap.
Thank you.

---

### 评论 #2 — kubawis128 (2022-03-03T11:39:14Z)

Hi @ROCmSupport,
Thanks for your reply.
I can't wait for an update.

---

### 评论 #3 — qyb (2022-03-10T00:36:59Z)

AMD have released a [beta windows driver for AMD Radeon™ 6000 series](https://www.amd.com/zh-hans/support/kb/release-notes/rn-rad-win-21-40-beta-blender-3-0), to support HIP GPU Acceleration feature. And it looks that [RX 5500 XT](https://wiki.blender.org/wiki/Reference/Release_Notes/3.0/Cycles#AMD) run well.

More information: [AMD HIP Linux GPU Acceleration For Blender Delayed To v3.2 Release](https://www.phoronix.com/scan.php?page=news_item&px=AMD-HIP-Blender-3.2-Delay)

---

### 评论 #4 — limapedro (2022-03-10T19:07:41Z)

@qyb @ROCmSupport  So does this mean that we could run tensorflow or pytorch ROCm on Windows soon?


---

### 评论 #5 — RoARene317 (2022-03-14T03:39:33Z)

> @qyb @ROCmSupport So does this mean that we could run tensorflow or pytorch ROCm on Windows soon?

It's different. Same with NVIDIA , apps that can use CUDA Core doesn't mean it's can use by Pytorch / TF. In NVIDIA, you need CUDA Toolkit to run with GPU Computing (Tensorflow or Pytorch). But in this case (AMD Terms) it's required ROCm-Development which is different HIP Runtime. Maybe in term of video processing or rendering , AMD could use HIP but for other than that, it's really limited.

---

### 评论 #6 — falaca (2022-05-08T18:21:19Z)

Any updates on Navi23 support?

---

### 评论 #7 — arcaspo (2022-05-13T07:58:41Z)

I also have a 6600xt and I am trying to use pytorch rocm with it. I saw these build scripts, https://github.com/xuhuisheng/rocm-build, but it doesn't mention Navi 23. Is it possible to edit those scrips for Navi 23/gfx1032 or use a different method to support the 6600xt?

---

### 评论 #8 — Uklosk (2022-05-29T21:29:56Z)

Same here.

---

### 评论 #9 — qixiang109 (2022-06-08T01:58:47Z)

same here.

---

### 评论 #10 — NorColumba (2022-06-10T09:17:42Z)

same here。

---

### 评论 #11 — langyuxf (2022-06-22T06:46:48Z)

@falaca @qixiang109 you can refer to https://github.com/RadeonOpenCompute/ROCm/issues/1756.

---

### 评论 #12 — markbex (2022-09-01T05:46:09Z)

same here

---

### 评论 #13 — raiko86 (2022-09-09T12:37:55Z)

same here

---

### 评论 #14 — Default103 (2022-09-29T01:56:29Z)

you can use ROCm on rx6600/6600xt by rewriting env variable. Add 'HSA_OVERRIDE_GFX_VERSION=10.3.0 ' before call python

---

### 评论 #15 — kubawis128 (2022-10-12T06:34:09Z)

Hi
I can confirm that you can run rocm on rx6600xt using `HSA_OVERRIDE_GFX_VERSION` and am able to run pytorch-rocm and generate images on gpu using stable diffusion
I think that we can close the issue for now (and maybe add a little note to the documentation to use env variable)
Thanks for all support

---

### 评论 #16 — lhemerly (2022-12-30T20:33:54Z)

Tried the HSA_OVERRIDE_GFX_VERSION=10.3.0 without success.
The ROCMINFO and CLINFO shows the 6600XT, tensorflow won't:

> 2022-12-30 17:29:25.112376: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
> To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
> 2022-12-30 17:29:26.358871: E tensorflow/compiler/xla/stream_executor/rocm/rocm_driver.cc:302] failed call to hipInit: HIP_ERROR_InvalidDevice
> 2022-12-30 17:29:26.358891: I tensorflow/compiler/xla/stream_executor/rocm/rocm_diagnostics.cc:112] retrieving ROCM diagnostic information for host: hemerly-AI
> 2022-12-30 17:29:26.358897: I tensorflow/compiler/xla/stream_executor/rocm/rocm_diagnostics.cc:119] hostname: hemerly-AI
> 2022-12-30 17:29:26.358924: I tensorflow/compiler/xla/stream_executor/rocm/rocm_diagnostics.cc:142] librocm reported version is: NOT_FOUND: was unable to find librocm.so DSO loaded into this program
> 2022-12-30 17:29:26.358930: I tensorflow/compiler/xla/stream_executor/rocm/rocm_diagnostics.cc:146] kernel reported version is: UNIMPLEMENTED: kernel reported driver version not implemented
> [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]

---

### 评论 #17 — brewfalconenterprises (2023-02-26T20:11:59Z)

After much trial-and-error, here's the cocktail that I finally got to work on Ubuntu 22.04 bare metal with Navi23 (6600XT). (Both PyTorch and Tensorflow from the command line)

- ROCm 5.4.2
- Python 3.9 (may need to separately install distutils)
- tensorflow-rocm
- pytorch5.2

Environment variables:
- PYTHONPATH=/usr/bin/python3.9
- ROCM_PATH=/opt/rocm
- HSA_OVERRIDE_GFX_VERSION=10.3.0


---

### 评论 #18 — pterodactyl-soup (2023-03-16T18:37:50Z)

Same here.

> same here。



---

### 评论 #19 — AhmedGamal411 (2023-03-17T07:06:38Z)

`export HSA_OVERRIDE_GFX_VERSION=10.3.0`

Seems to made this error disappear:
`Ignoring visible gpu device with AMDGPU version : gfx1032 `

---

### 评论 #20 — yoshyteru (2023-04-02T04:07:22Z)

in short, crap, spend a lot of money on the gpu for nothing to work right, Windowns + AMD + Stable Diffusion = 0

---

### 评论 #21 — dagelf (2023-04-13T08:04:02Z)

Welcome to the club. This has been ongoing since the R9 days. Literally. What's that, 3 (or 4?) generations of cards - what's that, 10 years now? Where only random unicorn cards work because some unicorn at AMD managed to get it working for some random card because someone could apply the right unicorn magic at the right place... condolences to everyone working for AMD. AMD has acquired a lot of companies over the years and I guess there is a lot of internal politics and mismatched company culture, and this is the result, a company scoring own goals... a perfect case where open sourcing everything will actually help them. 

Here is the current open source unicorn to get Pytorch running at good speed on most AMD cards, just a tiny push is needed, come on lets jump in and help out: https://github.com/artyom-beilis/dlprimitives

---

### 评论 #22 — csbnw (2023-04-13T08:10:57Z)

I completely agree with @dagelf and this is also (unfortunately) what keeps me (mostly) away from using AMD GPUs. With NVIDIA, you can at least be pretty certain that any reasonably recent GPU (e.g. Maxwell and newer) just works with the latest NVIDIA driver and/or CUDA toolkit + libraries.

---

### 评论 #23 — Nyongwon (2023-08-11T18:01:36Z)

Same here : )

---

### 评论 #24 — brewfalconenterprises (2023-08-11T18:30:09Z)

I was having trouble making my cocktail work in the PyCharm venv, until I had a moment of clarity.

- Install the venv packages From Disk, using the .whl downloaded previously (several versions old).
- Export the Environment variables inside the Python venv script.

I have not experimented with Docker, so YMMV.

---

### 评论 #25 — mishurov (2023-09-26T16:10:01Z)

`export HSA_OVERRIDE_GFX_VERSION=10.3.0` means that it uses the code for gfx1030. In my personal tests RX 6600 is 3 times slower than RTX 3060 in TensorFlow, despite that in games they have similar performance

---

### 评论 #26 — langyuxf (2023-09-27T12:26:40Z)

> `export HSA_OVERRIDE_GFX_VERSION=10.3.0` means that it uses the code for gfx1030. In my personal tests RX 6600 is 3 times slower than RTX 3060 in TensorFlow, despite that in games they have similar performance

What's your ROCm version?

---

### 评论 #27 — mishurov (2023-09-27T12:34:30Z)

@xfyucg 5.6.0, it is already installed in the Docker image `rocm/tensorflow:latest`

---

### 评论 #28 — Germano0 (2024-09-24T14:20:26Z)

Similar issue
https://github.com/ROCm/ROCm/issues/3798

---
