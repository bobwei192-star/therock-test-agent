# RDNA 3 support?

> **Issue #1813**
> **状态**: closed
> **创建时间**: 2022-09-27T06:23:28Z
> **更新时间**: 2024-06-18T16:51:09Z
> **关闭时间**: 2024-06-18T16:51:09Z
> **作者**: zhiyuanzhai
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1813

## 描述

Will RDNA 3 GPUs get ROCm support at launch?

---

## 评论 (13 条)

### 评论 #1 — xuhuisheng (2022-09-27T11:57:36Z)

The gfx11 related codes is on going.

We are not worry about kernel driver, it always the highest priority.

The llvm had added gfx11 related codes. 
<https://github.com/RadeonOpenCompute/llvm-project/commit/b982ba2a6e0f11340b4e75d1d4eba9ff62a81df7>

Even Tensile had merged some gfx11 codes.
<https://github.com/ROCmSoftwarePlatform/Tensile/pull/1521>

But math library always need time to debug.

Because RDNA2 had got official support, RDNA3 may be more quickly.

---

### 评论 #2 — Mushoz (2022-12-12T08:53:27Z)

The new series are launching tomorrow. In what state is ROCM support for these new 7900 cards? Will it already work? If not, when can we expect them to work?

I am currently using a 6900XT, but depending on whether I can run my ROCM workloads on a 7900 I want to try to purchase a new card tomorrow. I am using tensorflow-rocm in my workloads in case that matters.

@xuhuisheng 

---

### 评论 #3 — xuhuisheng (2022-12-12T20:27:33Z)

@Mushoz 
There is no offcial roadmap for gfx11 which might be classified. But we can get some clue from CMakeLists.txt. Here is the search results:

```
work@d96e2f6e1fb2:~/ROCm$ find . -type f -name CMakeLists.txt -print|xargs grep gfx11
./rocThrust/CMakeLists.txt:       TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx1030;gfx1100;gfx1102"
./rocThrust/CMakeLists.txt:        set(DEFAULT_AMDGPU_TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx1030;gfx1100;gfx1102")
./rocFFT/CMakeLists.txt:  TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx1030;gfx1100;gfx1102")
./rocSOLVER/CMakeLists.txt:set(AMDGPU_TARGETS "gfx803;gfx900;gfx906:xnack-;gfx908:xnack-;gfx1010;gfx1030;gfx1102;gfx1100;${OPTIONAL_AMDGPU_TARGETS}"
./llvm-project/openmp/libomptarget/libm/CMakeLists.txt:set(amdgpu_mcpus gfx700 gfx701 gfx801 gfx803 gfx900 gfx902 gfx906 gfx908 gfx90a gfx90c gfx940 gfx1030 gfx1031 gfx1032 gfx1033 gfx1034 gfx1035 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103)
./llvm-project/openmp/libomptarget/hostrpc/CMakeLists.txt:set(amdgpu_mcpus gfx700 gfx701 gfx801 gfx803 gfx900 gfx902 gfx906 gfx908 gfx90a gfx90c gfx940 gfx1030 gfx1031 gfx1032 gfx1033 gfx1034 gfx1035 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103)
./llvm-project/openmp/libomptarget/DeviceRTL/CMakeLists.txt:    set(amdgpu_wfsz_is32 gfx1030 gfx1031 gfx1032 gfx1033 gfx1034 gfx1035 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103)
./llvm-project/openmp/libomptarget/deviceRTLs/amdgcn/CMakeLists.txt:set(amdgpu_mcpus gfx700 gfx701 gfx801 gfx803 gfx900 gfx902 gfx906 gfx908 gfx90a gfx90c gfx940 gfx1030 gfx1031 gfx1032 gfx1033 gfx1034 gfx1035 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103)
./llvm-project/openmp/libomptarget/deviceRTLs/amdgcn/CMakeLists.txt:set(amdgpu_32bitwf gfx1030 gfx1031 gfx1032 gfx1033 gfx1034 gfx1035 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103)
./rocSPARSE/CMakeLists.txt:        TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx1030;gfx1100;gfx1102"
./rocSPARSE/CMakeLists.txt:        set(DEFAULT_AMDGPU_TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx1030;gfx1100;gfx1102")
./hipCUB/CMakeLists.txt:      TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx1030;gfx1100;gfx1102"
./rccl/CMakeLists.txt:       TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx1030;gfx1100;gfx1101;gfx1102"
./rccl/CMakeLists.txt:        set(DEFAULT_AMDGPU_TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx1030;gfx1100;gfx1101;gfx1102")
./rocBLAS/CMakeLists.txt:set_property( CACHE AMDGPU_TARGETS PROPERTY STRINGS all gfx803 gfx900 gfx906:xnack- gfx908:xnack- gfx90a:xnack+ gfx90a:xnack- gfx1010 gfx1012 gfx1030 gfx1100 gfx1102 )
./rocBLAS/CMakeLists.txt:      TARGETS "gfx803;gfx900;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack+;gfx90a:xnack-;gfx1010;gfx1012;gfx1030;gfx1100;gfx1102"
./rocRAND/CMakeLists.txt:    TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx1030;gfx1100;gfx1102"
./Tensile/Tensile/Source/CMakeLists.txt:  set(TENSILE_GPU_ARCHS gfx803 gfx900 gfx906:xnack- gfx908:xnack- gfx90a:xnack- gfx1010 gfx1011 gfx1012 gfx1030 gfx1100 gfx1101 gfx1102 CACHE STRING "GPU architectures")
./Tensile/Tensile/Source/CMakeLists.txt:  set(TENSILE_GPU_ARCHS gfx803 gfx900 gfx906 gfx908 gfx90a gfx1010 gfx1011 gfx1012 gfx1030 gfx1100 gfx1101 gfx1102 CACHE STRING "GPU architectures")
./rocPRIM/CMakeLists.txt:      TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx90a:xnack-;gfx90a:xnack+;gfx1030;gfx1100;gfx1102"
./ROCR-Runtime/src/CMakeLists.txt:                   image/addrlib/src/gfx11/gfx11addrlib.cpp
./ROCR-Runtime/src/CMakeLists.txt:                   image/image_manager_gfx11.cpp
./ROCR-Runtime/src/CMakeLists.txt:                   image/image_lut_gfx11.cpp
./ROCR-Runtime/src/CMakeLists.txt:    ${CMAKE_CURRENT_SOURCE_DIR}/image/addrlib/src/gfx11
./ROCR-Runtime/src/CMakeLists.txt:    ${CMAKE_CURRENT_SOURCE_DIR}/image/addrlib/src/chip/gfx11 )
./ROCR-Runtime/src/core/runtime/trap_handler/CMakeLists.txt:set (TARGET_DEVS "gfx900;gfx1010;gfx1030;gfx1100")
./ROCR-Runtime/src/image/blit_src/CMakeLists.txt:  set (TARGET_DEVICES "gfx700;gfx701;gfx702;gfx801;gfx802;gfx803;gfx805;gfx810;gfx900;gfx902;gfx904;gfx906;gfx908;gfx909;gfx90a;gfx90c;gfx1010;gfx1011;gfx1012;gfx1013;gfx1030;gfx1031;gfx1032;gfx1033;gfx1034;gfx1035;gfx1036;gfx1100;gfx1102;gfx1103")
./rocALUTION/CMakeLists.txt:  set(DEFAULT_AMDGPU_TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx1030;gfx90a:xnack-;gfx90a:xnack+;gfx1100;gfx1102")
./rocALUTION/CMakeLists.txt:  set(DEFAULT_AMDGPU_TARGETS "gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-;gfx1030;gfx1100;gfx1102")

```

And it definitely cannot work, because of leaking support for MIOpen at once. But At least we can hope for waiting less time than navi21.


---

### 评论 #4 — Lolliedieb (2022-12-15T13:20:58Z)

Sometimes I wonder about what amd does during the 2-3 years they are planning a new arch ... I mean the llvm branch released with rocm 5.4 does understand the gfx1100 target and compiles all fine, yet the output of it is incompatible with the released amdgpu-pro drivers (this is not the case with gfx1030...). And well lack of rocm support at release day for new architectures is an other thing.
I can not understand with the planning time going into a new architecture, why there is so poor software support the moment they get released. 

---

### 评论 #5 — Mushoz (2022-12-15T13:23:31Z)

@Lolliedieb What about using Mesa instead of the amdgpu-pro? I have always used tensorflow-rocm on my 6900xt while running the opensource drivers. I just received my new 7900 XTX today and was hoping I could use it to run tensorflow-rocm again. 

---

### 评论 #6 — jellersby (2023-02-11T07:27:20Z)

Hello. Will gfx11 support be in ROCm 5.5 (including MIOpen)? Thank you.

---

### 评论 #7 — briansp2020 (2023-09-04T16:09:54Z)

Are there still people who are waiting for 7900XTX support? Though the performance is still a bit poor, TensorFlow-upstream now runs when built on the latest ROCm release. I was looking into the status of ROCm support for 7900XTX and found a few issues opened by different people and wanted to link all to the issue I opened in MIOpen repo. Though there has not been any confirmation from the developer, I think the performance issues are due to insufficient optimization of MIOpen. 
https://github.com/ROCmSoftwarePlatform/MIOpen/issues/2342

---

### 评论 #8 — johnnynunez (2023-09-05T11:07:29Z)

> Are there still people who are waiting for 7900XTX support? Though the performance is still a bit poor, TensorFlow-upstream now runs when built on the latest ROCm release. I was looking into the status of ROCm support for 7900XTX and found a few issues opened by different people and wanted to link all to the issue I opened in MIOpen repo. Though there has not been any confirmation from the developer, I think the performance issues are due to insufficient optimization of MIOpen. [ROCmSoftwarePlatform/MIOpen#2342](https://github.com/ROCmSoftwarePlatform/MIOpen/issues/2342)

Next month will be released rocm 5.7(7900XTX official support) and miopen for windows

---

### 评论 #9 — AnonymousRonin (2023-12-10T04:34:02Z)

> Are there still people who are waiting for 7900XTX support? Though the performance is still a bit poor, TensorFlow-upstream now runs when built on the latest ROCm release. I was looking into the status of ROCm support for 7900XTX and found a few issues opened by different people and wanted to link all to the issue I opened in MIOpen repo. Though there has not been any confirmation from the developer, I think the performance issues are due to insufficient optimization of MIOpen. [ROCm/MIOpen#2342](https://github.com/ROCm/MIOpen/issues/2342)

Yeah, I've been waiting since I bought it.  I tried returning it based on the fact it never fully worked despite countless emails following every direction given.  I am about ready to publish the entire email chain so people can see what horrible support they provide and what happens when it doesn't work.  Basically they're response to linux support was to load the latest edition of windows and see if it works.  Seriously??  I will never buy another AMD.  My nvidia in my laptop works without a hitch, never had a problem.  This whole gfx11 saga has got to be one of the worst cases of misrepresentation I've come across.  As far as I'm concerned, they don't support linux as long as there's no RDNA3 support.

---

### 评论 #10 — briansp2020 (2023-12-10T06:32:53Z)

@AnonymousRonin
Have you tried ROCm5.7? What issues are you having? Though it takes some fiddling, you should be able to get TensorFlow and PyTorch working using ROCm 5.7 & 7900XTX. Hopefully, with the release of 6.0, things will work more smoothly. 


---

### 评论 #11 — distantorigin (2024-01-10T07:29:28Z)

Is there any plan for GFX1103 (780M) support? Currently I see 1100 and 1102, and copying the 1102 libraries to 1103 produces issues.

---

### 评论 #12 — johnnynunez (2024-01-10T08:43:23Z)

> @AnonymousRonin Have you tried ROCm5.7? What issues are you having? Though it takes some fiddling, you should be able to get TensorFlow and PyTorch working using ROCm 5.7 & 7900XTX. Hopefully, with the release of 6.0, things will work more smoothly.

I'm using rocm6. With tensorflow still have freezes when put models and data in memory

---

### 评论 #13 — ppanchad-amd (2024-06-18T16:51:09Z)

@zhiyuanzhai Closing bug since RDNA3 is supported in latest ROCm 6.1.2
@johnnynunez Please create a separate ticket for your issue if you are still seeing your issue with the latest ROCm 6.1.2

---
