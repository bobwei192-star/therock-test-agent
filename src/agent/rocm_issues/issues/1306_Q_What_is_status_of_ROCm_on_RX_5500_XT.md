#  Q: What is status of ROCm on RX 5500 XT?

> **Issue #1306**
> **状态**: closed
> **创建时间**: 2020-11-26T20:19:03Z
> **更新时间**: 2024-03-07T15:48:55Z
> **关闭时间**: 2020-12-15T12:53:04Z
> **作者**: Doev
> **标签**: Question, Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1306

## 标签

- **Question** (颜色: #cc317c)
- **Feature Request** (颜色: #fbca04)

## 描述

Hello,

I like to evaluate if ROCm is suitable for deeplearning. What about the RX 5500 XT? Is it possible to use that cheap GPU for doing so?

---

## 评论 (89 条)

### 评论 #1 — baryluk (2020-11-27T01:07:05Z)

Duplicate of https://github.com/RadeonOpenCompute/ROCm/issues/887

---

### 评论 #2 — ROCmSupport (2020-11-27T05:20:41Z)

Hi @Doev 
Thanks for reaching out.
We are not officially supporting Navi series of cards with ROCm.
But you can still give a try, things might work.

---

### 评论 #3 — xuhuisheng (2020-11-27T05:33:49Z)

@ROCmSupport 
Since rocm-libs didnt configure gfx1010/gfx1012 in AMDGPU_TARGETS, there will always meet ` guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!") `

If you want to try navi10,
1. openCL maybe work
2. recompile rocm-libs related libraries like rocBLAS, rocSPARSE with AMDGPU_TARGETS=gfx1010;gfx1011;gfx1012, you may met some compilation issues.

---

### 评论 #4 — ROCmSupport (2020-11-27T05:46:15Z)

Agree @xuhuisheng 
Some things might work and some definitely can not.

---

### 评论 #5 — unexploredtest (2020-11-27T06:19:52Z)

I don't know about RX 5500 XT, but for my RX 5500M(Navi 14), I face this issue in version 3.9 when I want to use TF:
#1269 
I should note that OpenCL works fine.
Previous versions don't work for me at all(OpenCL doesn't get installed properly for  some reasons).
EDIT: On Ubuntu 20.04.1
EDIT 2: I could also install OpenCL in Manjaro, but faced compilation errors during rocm-libs installation(Probably because of my 5.9 kernel)

---

### 评论 #6 — da-phil (2020-11-27T10:53:21Z)

> Agree @xuhuisheng
> Some things might work and some definitely can not.

And which things definitely won't work? 
It would be really great to know which bits and pieces of integrating navi chipsets into ROCm are missing. Then the open source community would at least know what is missing and what can be done by them.

---

### 评论 #7 — xuhuisheng (2020-11-27T11:00:21Z)

@da-phil 
The frameworks like tensorflow/pytorch based on rocm-libs definitely wont work. Or you can recompile rocm-libs with AMDGPU_TARGETS=gfx1010 and fixed the issues though compiling.

OpenCL that didnt depends on rocm-libs may work.

---

### 评论 #8 — da-phil (2020-11-27T11:04:24Z)

> @da-phil
> The frameworks like tensorflow/pytorch based on rocm-libs definitely wont work. Or you can recompile rocm-libs with AMDGPU_TARGETS=gfx1010 and fixed the issues though compiling.
> 
> OpenCL that didnt depends on rocm-libs may work.

Yup, OpenCL works well, it's not the issue. The issue are the deeplearning frameworks which currently don't work.
Did you get tensorflow or pytorch running with a navi based GPU by "just" recompiling some rocm-libs?
I read in another issue that you contemplated on getting a navi GPU once the prices drop, but don't own one yet, right?

---

### 评论 #9 — xuhuisheng (2020-11-27T11:15:57Z)

@da-phil 
Yes. I didnt have a navi10 gpu now. I read from AMD website, and get the navi10 didnot better than vega10 on computation. And it maybe wont get offcial supporting in high possibility.

Following Rigtorp's steps. I am sure that ROCm-3.10.x could compile successly on gfx1010, only rocSPARSE has some dpp-bcast issues, but I think we could follow rocPRIM's resovling way.
And Pytorch could be confirmed that it can compile successly on gfx1010 on Sept. But nobody go further. In my opinion, there maybe other issues.

I think I can share some building scripts for gfx1010, after ROCm-3.10 released. Anyone who interesting in it could have a try.

---

### 评论 #10 — da-phil (2020-11-27T13:30:51Z)

> Following Rigtorp's steps. I am sure that ROCm-3.10.x could compile successly on gfx1010, only rocSPARSE has some dpp-bcast issues, but I think we could follow rocPRIM's resovling way.
> And Pytorch could be confirmed that it can compile successly on gfx1010 on Sept. But nobody go further. In my opinion, there maybe other issues.

Yeah, only compiling ROCm for gfx1010 is not enough, it would be also great if it would also work :sweat_smile: 

> I think I can share some building scripts for gfx1010, after ROCm-3.10 released. Anyone who interesting in it could have a try.

This would be awesome, then I'd give it a try too :smile: 

---

### 评论 #11 — Doev (2020-11-27T16:45:34Z)

Thanks for the many replies. I give it a try and I have ordered a RX 5500 XT, cause 200€ is not so much and if everything fails I can sell the card.

I don't understand why the NAVI architecture is so important, cause I think the RX 5500 XT is from the Vega series. Well I never owned an amd gpu before.

---

### 评论 #12 — livegenic-akyrychek (2020-11-27T16:52:22Z)

@Doev try to use PlaidML, it might not give you huge boost but may be some improvement (if works on rx 5500 xt)
 Have not tested yet... As I recently found out about it myself.

---

### 评论 #13 — unexploredtest (2020-11-27T20:15:22Z)

Plaidml will work just with Keras, you should use nGraph(with PlaidML backend) besides it, but these are out-dated, though they said they're working on a new release.

---

### 评论 #14 — da-phil (2020-11-29T22:09:35Z)

> @da-phil
> The frameworks like tensorflow/pytorch based on rocm-libs definitely wont work. Or you can recompile rocm-libs with AMDGPU_TARGETS=gfx1010 and fixed the issues though compiling.
> 
> OpenCL that didnt depends on rocm-libs may work.

Yup, OpenCL works well, it's not the issue. The issue are the deeplearning frameworks which currently don't work.
Did you get tensorflow or pytorch running with a navi based GPU by "just" recompiling some rocm-libs?
I read in another issue that you contemplated on getting a navi GPU once the prices drop, but don't own one yet, right?

---

### 评论 #15 — unexploredtest (2020-12-01T15:11:18Z)

> I think I can share some building scripts for gfx1010, after ROCm-3.10 released. Anyone who interesting in it could have a try.

When can we expect it?


---

### 评论 #16 — xuhuisheng (2020-12-02T11:59:50Z)

@da-phil @aliPMPAINT 
I wrote a doc for navi10.
<https://github.com/xuhuisheng/rocm-build/tree/navi10/navi10/README.md>

---

### 评论 #17 — livegenic-akyrychek (2020-12-02T12:27:35Z)

@xuhuisheng may be duplicate it in https://github.com/RadeonOpenCompute/ROCm/issues/887

---

### 评论 #18 — unexploredtest (2020-12-02T12:33:30Z)

@xuhuisheng Thanks. Will test it on Friday. Just one question, with RX 5500M(gfx 1012) I should replace `AMDGPU_TARGETS="gfx1010"` with `AMDGPU_TARGETS="gfx1012"` or leave it unchanged?
Also, with only 16 GB of RAM, how much swap memory is recommended?

---

### 评论 #19 — xuhuisheng (2020-12-02T12:40:18Z)

> @xuhuisheng Thanks. Will test it on Friday. Just one question, with RX 5500M(gfx 1012) I should replace `AMDGPU_TARGETS="gfx1010"` with `AMDGPU_TARGETS="gfx1012"` or leave it unchanged?
> Also, with only 16 GB of RAM, how much swap memory is recommended?

must use gfx1012, or there will throw a hipErrorNoBinaryForGpu. you can get the gpu arch name by rocminfo



---

### 评论 #20 — xuhuisheng (2020-12-02T12:47:06Z)

> @xuhuisheng may be duplicate it in #887

Too complicated to do recompiling rocm. cannot be sure if it works. So dont want to show it to who not very interesting.

---

### 评论 #21 — unexploredtest (2020-12-02T18:51:17Z)

@xuhuisheng Thanks for the response, will report back within next Saturday. Much appreciated.
One last question, I have already installed ROCm 3.9.1, is `sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils` enough for the complete uninstallation?

---

### 评论 #22 — ROCmSupport (2020-12-03T05:35:05Z)

Hi @aliPMPAINT 
You can uninstall rocm using above command.
After that also, if something is there under /opt/rocm-xxx, recommend to check all packages as sudo dpkg -l | grep hsa and followed with replacing hsa to hip, llvm, rocm, rock.
Remove all visible packages one by one as sudo apt purge <pkg name>
Hope it helps.
Thank you.

---

### 评论 #23 — unexploredtest (2020-12-04T12:44:59Z)

@xuhuisheng Ok, so I tried your guide. Unfortuantely it didn't work out, I either encountered `guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")` or `Segmentation fault (core dumped)` when importing/using pytorch.
I also didn't encounter any compilation errors. Here is more info about my device and environment:
I have a Bravo 17 laptop, with GPU Radeon RX 5500M(Navi 14, gfx 1012) and Ryzen 7 4800H.
On Ubuntu 20.04.1 with the `5.6.0-1033-oem` kernel (Coudn't test 5.4.x out because <5.5 is incompatible with my hardware)
I've tried both python 3.7 and 3.8, have used `AMDGPU_TARGETS="gfx1012"`, and tried both `export PYTORCH_ROCM_ARCH=gfx1010` and `export PYTORCH_ROCM_ARCH=gfx1012`
Will share more info later on.
EDIT: WAIT

---

### 评论 #24 — unexploredtest (2020-12-04T13:59:19Z)

So, I tested 5.4.0-56 out. Because 5.4.0-56 isn't compatible with my hardware, I had to "crtl+alt+f2" in order to log in(I can't pass through booting).
When I did `rocminfo` I got:
```
[37mROCk module is loaded[0m
[31mUnable to open /dev/kfd read-write: Cannot allocate memory[0m
[37malipmpaint is member of render group[0m
[31mhsa api call failure at: /src/rocminfo/rocminfo.cc:1142
[31mCall returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
[0m
```
And `clinfo`:
```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (3212.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform
```

But they do get recognized on 5.6, I'll attach files.
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5643167/clinfo.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5643170/rocminfo.txt)

---

### 评论 #25 — xuhuisheng (2020-12-05T01:09:22Z)

@aliPMPAINT 
There are some differences between gfx1010 to gfx1012, I upload a nav14 directory for gfx1012.
https://github.com/xuhuisheng/rocm-build/tree/develop/navi14
But it didnot like to throw a hipErrorNoBinaryForGpu, except there are other components missing gfx1012 target.
I will go to find some test to check each components.

And if rocminfo cannot recoganize gfx1012, it means the kernel-driver or thunk-interface or hsa-runtime canot support target device. Now I dont know how to debug that level, so I suggest using version which could run rocminfo normally.


---

### 评论 #26 — unexploredtest (2020-12-05T04:38:35Z)

@xuhuisheng 
Thanks! I'll check this one out too. 
rocminfo does recognize gfx 1012 but not on 5.4, just 5.6, so it's no big deal

---

### 评论 #27 — xuhuisheng (2020-12-05T09:47:49Z)

Upload some codes for check rocm-libs.
https://github.com/xuhuisheng/rocm-build/tree/develop/check

---

### 评论 #28 — unexploredtest (2020-12-07T18:45:55Z)

@xuhuisheng 
Will test it out within a week, thank you

---

### 评论 #29 — unexploredtest (2020-12-11T12:28:34Z)

@xuhuisheng So, I followed the [Navi14](https://github.com/xuhuisheng/rocm-build/tree/develop/navi14) guide and then checked them via [check](https://github.com/xuhuisheng/rocm-build/tree/develop/check) scripts.
Apparently, `rocSPARSE` doesn't work:
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ bash check.sh
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocBLAS]   2.32.0.2844-cc18d25f
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocFFT]    1.0.8.966-2d35fd6
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocPRIM]   201005
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocRAND]   201006
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
/src/external/hip-on-vdi/rocclr/hip_code_object.cpp:120: guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")
check.sh: line 25:  2687 Aborted                 (core dumped) ./build/hello_rocsparse
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rccl]      2708
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[MIOpen]    2 9 0
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocSOVLER] 3.10.0.183-6b820a8
```
Also, when I tried to run `run-rocblas.sh`, it got stuck here(waited for a few hours):
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ bash run-rocblas.sh
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
 ########## start sgemm
info: mapper init - hip_Cijk_Ailk_BjlkC_CB was used in 3 devices
info: mapper init - hip_Cijk_Alik_BjlkC_CB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_4xi8BH was used in 3 devices
info: mapper init - hip_Cijk_Ailk_BjlkC_ZB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_SB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_HB was used in 3 devices
info: mapper init - hip_Cijk_AlikC_Bjlk_CB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_DB was used in 3 devices
info: mapper init - hip_Cijk_Alik_BjlkC_ZB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_CB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_BBH was used in 3 devices
info: mapper init - hip_Cijk_AlikC_BjlkC_ZB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_BBH was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_4xi8BH was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_DB was used in 3 devices
info: mapper init - hip_Cijk_AlikC_BjlkC_CB was used in 3 devices
info: mapper init - hip_Cijk_AlikC_Bljk_CB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_CB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_CB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_BBH was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_ZB was used in 3 devices
info: mapper init - hip_Cijk_AlikC_Bljk_ZB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_BBH was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_HBH was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_ZB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_4xi8BH was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_HBH was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_CB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_ZB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_DB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_SB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_HBH was used in 3 devices
info: mapper init - hip_Cijk_AlikC_Bjlk_ZB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_SB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bjlk_HB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_HB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_HBH was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_SB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bljk_4xi8BH was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_DB was used in 3 devices
info: mapper init - hip_Cijk_Alik_Bljk_HB was used in 3 devices
info: mapper init - hip_Cijk_Ailk_Bjlk_ZB was used in 3 devices
rocblas_create_handle,atomics_allowed
```
EDIT: The `The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.` warning is happening because I also have an integrated GPU(gfx902), alongside with Radeon RX 5500M(gfx 1012, Navi14) , so I don't think it's important

---

### 评论 #30 — xuhuisheng (2020-12-11T12:51:11Z)

@aliPMPAINT I suggest you re-compile rocSPARSE and watch the logs if there is compiling warning like cannot support gfx1012. 

---

### 评论 #31 — unexploredtest (2020-12-11T14:02:37Z)

@xuhuisheng These are the warnings I'm facing:
```
clang-12: warning: argument unused during compilation: '-Xarch_gfx906 -mno-sram-ecc' [-Wunused-command-line-argument]
clang-12: warning: argument unused during compilation: '-Xarch_gfx908 -msram-ecc' [-Wunused-command-line-argument]
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
```

---

### 评论 #32 — xuhuisheng (2020-12-11T15:04:06Z)

@aliPMPAINT could you show me the whole compiling logs? please delete whole build dir, rebuild clearly. iam very interesting, looks like the andgpu_targets wasnot used.

---

### 评论 #33 — unexploredtest (2020-12-11T15:41:54Z)

@xuhuisheng 
Thanks for responding and trying to help, much appreciated.
So, after deleting the `rocm-build/build` directory and executing `source env.sh`, which contains:
```
#!/bin/bash

export ROCM_INSTALL_DIR=/opt/rocm
export ROCM_GIT_DIR=/home/alipmpaint/Documents/ROCm/ROCm
export ROCM_BUILD_DIR=/home/alipmpaint/Documents/ROCm/rocm-build/build
export ROCM_PATCH_DIR=/home/alipmpaint/Documents/ROCm/rocm-build/patch
export AMDGPU_TARGETS="gfx1012"
export PATH=$ROCM_INSTALL_DIR/bin:$ROCM_INSTALL_DIR/llvm/bin:$ROCM_INSTALL_DIR/hip/bin:$PATH
```
I ran `bash navi14/25.rocsparse.sh`.
The whole compiling log:
[log1.txt](https://github.com/RadeonOpenCompute/ROCm/files/5680086/log1.txt)
The `.ninja_log` (idk whether it's useful):
[ninjalog.txt](https://github.com/RadeonOpenCompute/ROCm/files/5680103/ninjalog.txt)
Are there any other logs/files I should've included?





---

### 评论 #34 — xuhuisheng (2020-12-11T15:58:49Z)

@aliPMPAINT I suspect rocSPARSE didnot used AMDGPU_TARGETS=gfx1012, seems like it used gfx902 which comes from local rocminfo.
I suggest open rocm-build/build/rocsparse/CMakeCache.txt and search AMDGPU_TARGETS to confirm if it is gfx1012 or not.
And please show me the CMakeCache.txt

---

### 评论 #35 — unexploredtest (2020-12-11T16:03:02Z)

@xuhuisheng 
Apparently it is gfx1012:
[CMakeCache.txt](https://github.com/RadeonOpenCompute/ROCm/files/5680208/CMakeCache.txt)


---

### 评论 #36 — xuhuisheng (2020-12-11T16:38:05Z)

@aliPMPAINT 
CMakeCache.txt is correct. Another posibility is you have two GPU which is gfx902 and gfx1012, and gfx902 is used by default.
`/opt/rocm/bin/rocm_agent_enumerator` will show the local GPU list.

So maybe change AMDGPU_TARGETS="gfx902;gfx1012" could solve your problems, I guess.
Its late, I have to go bed. Good luck.
 

---

### 评论 #37 — Djip007 (2020-12-11T20:14:57Z)

> @xuhuisheng Ok, so I tried your guide. Unfortuantely it didn't work out, I either encountered `guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")` or `Segmentation fault (core dumped)` when importing/using pytorch.
> I also didn't encounter any compilation errors. Here is more info about my device and environment:
> I have a Bravo 17 laptop, with GPU Radeon RX 5500M(Navi 14, gfx 1012) and Ryzen 7 4800H.
> On Ubuntu 20.04.1 with the `5.6.0-1033-oem` kernel (Coudn't test 5.4.x out because <5.5 is incompatible with my hardware)
> I've tried both python 3.7 and 3.8, have used `AMDGPU_TARGETS="gfx1012"`, and tried both `export PYTORCH_ROCM_ARCH=gfx1010` and `export PYTORCH_ROCM_ARCH=gfx1012`
> Will share more info later on.
> EDIT: WAIT

ho... you will have some other things to du because of mix iGPU and dGPU (RX_5500 as dGPU + Vega GPU in 4800H APU...)
have a look at this issus: https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-615980464 ... it may be long to read => ask if any question...
(I can (will...) update the path if needed for my actual kernel: 5.10.nn... )

(ps: if you can give retrun of ' dmesg | grep kfd ' ... it can help me to give you more help with this config...)

---

### 评论 #38 — unexploredtest (2020-12-11T20:22:20Z)

@xuhuisheng Thank you so much! After looking on #841 , I set the variables to: `HIP_VISIBLE_DEVICES=1` and `ROCR_VISIBLE_DEVICES=1` and now, the `check.sh` and `run-rocblas.sh` scripts run successfully!:
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ export HIP_VISIBLE_DEVICES=1
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ bash check.sh
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocBLAS]   2.32.0.2844-cc18d25f
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocFFT]    1.0.8.966-2d35fd6
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocPRIM]   201005
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocRAND]   201006
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocSPARSE] 101800
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rccl]      2708
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[MIOpen]    2 9 0
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocSOVLER] 3.10.0.183-6b820a8
```
and `run-rocblas.sh`:
```
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
TENSILE_FIND_ALGO= -4 (SolutionMapperRuntime::EuclideanDistanceAlgo)
 ########## start sgemm
 ########## end   sgemm
 ########## start sgemm-batched
 ########## end   sgemm-batched
 ########## start sgemm-strided-batched
 ########## end   sgemm-strided-batched
```
However, Pytorch seems to have problems(after setting `ROCR_VISIBLE_DEVICES=1`, so it would use gfx1012):
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ python
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> x = torch.tensor([[1., -1.], [1., 1.]], requires_grad=True)
>>> out = x.pow(2).sum()
>>> out.backward()
terminate called after throwing an instance of 'c10::Error'
  what():  HIP error: hipErrorNoDevice
Exception raised from deviceCount at /home/alipmpaint/Documents/ROCm/pytorch/aten/src/ATen/hip/impl/HIPGuardImplMasqueradingAsCUDA.h:98 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x6c (0x7f42e1acdf3c in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xdbca68 (0x7f42e28d5a68 in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_hip.so)
frame #2: torch::autograd::Engine::start_device_threads() + 0xa1 (0x7f42f20fafd1 in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so)
frame #3: <unknown function> + 0x1247f (0x7f42f864847f in /lib/x86_64-linux-gnu/libpthread.so.0)
frame #4: torch::autograd::Engine::initialize_device_threads_pool() + 0x105 (0x7f42f20fb6a5 in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so)
frame #5: torch::autograd::Engine::execute_with_graph_task(std::shared_ptr<torch::autograd::GraphTask> const&, std::shared_ptr<torch::autograd::Node>) + 0x3f (0x7f42f20fdc5f in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so)
frame #6: torch::autograd::python::PythonEngine::execute_with_graph_task(std::shared_ptr<torch::autograd::GraphTask> const&, std::shared_ptr<torch::autograd::Node>) + 0x4d (0x7f42f6ef81ed in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_python.so)
frame #7: torch::autograd::Engine::execute(std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&, std::vector<at::Tensor, std::allocator<at::Tensor> > const&, bool, bool, std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&) + 0x5a0 (0x7f42f2100790 in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so)
frame #8: torch::autograd::python::PythonEngine::execute(std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&, std::vector<at::Tensor, std::allocator<at::Tensor> > const&, bool, bool, std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&) + 0x78 (0x7f42f6ef8168 in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_python.so)
frame #9: THPEngine_run_backward(THPEngine*, _object*, _object*) + 0xa73 (0x7f42f6ef8d13 in /home/alipmpaint/.local/lib/python3.8/site-packages/torch/lib/libtorch_python.so)
<omitting python frames>
frame #21: python() [0x67bc91]
frame #22: python() [0x67bd0f]
frame #23: python() [0x4a3291]
frame #26: python() [0x4ee716]
frame #28: __libc_start_main + 0xf3 (0x7f42f86800b3 in /lib/x86_64-linux-gnu/libc.so.6)

Aborted (core dumped)
```


---

### 评论 #39 — Djip007 (2020-12-11T20:25:45Z)

> @aliPMPAINT
> CMakeCache.txt is correct. Another posibility is you have two GPU which is gfx902 and gfx1012, and gfx902 is used by default.
> `/opt/rocm/bin/rocm_agent_enumerator` will show the local GPU list.
> 
> So maybe change AMDGPU_TARGETS="gfx902;gfx1012" could solve your problems, I guess.
> Its late, I have to go bed. Good luck.

yes it is (may not be the only) the problem here... but the master is that the gfx902 is a iGPU... memory management is different on iGPU and dGPU and can't be mixed... we nead to path the kfd kernel module to force kfd to only use one of the 2 GPU... (what I did in my path for in kernel... nead the same patch out of tree kfd driver use by Ubuntu...)

---

### 评论 #40 — unexploredtest (2020-12-11T20:28:51Z)

@Djip007 output of `dmesg | grep kfd`:
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~$ dmesg | grep kfd
[    3.127641] kfd kfd: Allocated 3969056 bytes on gart
[    3.128554] kfd kfd: added device 1002:7340
[    4.018225] kfd kfd: Allocated 3969056 bytes on gart
[    4.018420] kfd kfd: added device 1002:1636
```
And thanks, will be going through it

---

### 评论 #41 — unexploredtest (2020-12-11T20:33:22Z)

@Djip007 Sorry if it's a silly question, but how to add a patch?

---

### 评论 #42 — Djip007 (2020-12-11T20:34:45Z)

```
[    6.259637] kfd kfd: amdgpu: Ignoring ACPI CRAT on disabled iGPU (rocm_mode!=ROCM_MODE_IGPU)
[    6.494350] kfd kfd: Allocated 3969056 bytes on gart
[    6.495017] kfd kfd: added device 1002:67ef
[    6.505456] kfd kfd: skipped RAVEN, don't support dGPU memory management models
```
is what I have with my patch (I have a Ryzen 3550H + RX560M ...) 
(I reboot to check what is without my patch ....)

---

### 评论 #43 — Djip007 (2020-12-11T20:39:41Z)

> @Djip007 Sorry if it's a silly question, but how to add a patch?

For me I use fedora so have more resent kernel that use kdf from kernel... so I need to path and rebuild the kernel...
In your case I think we need to path the "rocm-dkms" => https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver 
(need some time to look at it if you want...)

---

### 评论 #44 — Djip007 (2020-12-11T20:51:41Z)

```
[    2.881572] kfd kfd: Allocated 3969056 bytes on gart
[    2.882086] kfd kfd: added device 1002:67ef
[    3.115632] kfd kfd: Allocated 3969056 bytes on gart
[    3.115874] kfd kfd: added device 1002:15d8
```
that is what I have without my patch... same as you...

@ROCmSupport  is it now possible to mix iGPU and dGPU? 
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-475983602
is this comment changed?

---

### 评论 #45 — xuhuisheng (2020-12-12T02:51:17Z)

@aliPMPAINT Could you test pytorch using this script:
https://github.com/xuhuisheng/rocm-build/blob/develop/check/test_pytoch.py
And please show me the result.

---

### 评论 #46 — unexploredtest (2020-12-12T04:58:25Z)

@xuhuisheng Here are the results:
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ export HIP_VISIBLE_DEVICES=1
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ export ROCR_VISIBLE_DEVICES=1
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ python test_torch.py
False
Devices:0
[]
Traceback (most recent call last):
  File "test_torch.py", line 11, in <module>
    with torch.cuda.device(0):
  File "/home/alipmpaint/.local/lib/python3.8/site-packages/torch/cuda/__init__.py", line 225, in __enter__
    self.prev_idx = torch._C._cuda_getDevice()
  File "/home/alipmpaint/.local/lib/python3.8/site-packages/torch/cuda/__init__.py", line 172, in _lazy_init
    torch._C._cuda_init()
RuntimeError: No HIP GPUs are available
```
for some reasons it's not detected?

---

### 评论 #47 — unexploredtest (2020-12-12T05:59:14Z)

@Djip007 I applied the patches to https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver, compiled and installed it. The problem is, the kernel is incompatible with my hardware. GPUs ain't detected and WiFi doesn't even work. `dmesg | grep kfd` doesn't output anything, and `rocminfo` and `clinfo` don't detect anything either. Will it be ok if I try the patch with the 5.6.0-1036-oem, which I'm sure is compatible with my hardware?

---

### 评论 #48 — xuhuisheng (2020-12-12T06:51:32Z)

@aliPMPAINT Could you run test_pytorch.py again, without export HIP_VISIBLE_DEVICES and ROCR_VISIBLE_DEVIDES?
Wish the result may change.

Now pytorch think there is no avaliable GPU.
rocminfo show gfx1012 so HIP ok.
check.sh show right versions so rocm-libs looks like ok.

Next question is why pytorch cannot find the GPU. 

---

### 评论 #49 — unexploredtest (2020-12-12T07:03:51Z)

@xuhuisheng 
Without exporting them, wel'l get to the problem we used to have:
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ python test_torch.py
/src/external/hip-on-vdi/rocclr/hip_code_object.cpp:120: guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")
Aborted (core dumped)
```
Maybe while compiling pytorch, we should have specified not to compile for `gfx902` but for `gfx1012`? Like exporting other values other than `PYTORCH_ROCM_ARCH`.

---

### 评论 #50 — xuhuisheng (2020-12-12T07:15:39Z)

OK. seems you should compiling for both gfx902 and gfx1012. But it not easy, please refer my build scripts that rocBLAS and Tensile need more updates for gfx902.
I dont think support gfx902 is good idea, if we could hide the gfx902. or modify source of HIP, just skip the hipErrorNoBinaryForGpu error.

Going to find codes for the HIP_VISIBLE_DEVICES=1 and pytorch cannot get the GPU situation. Will go back if get anything helpfully.

---

### 评论 #51 — xuhuisheng (2020-12-12T07:23:17Z)

Re-check the rocminfo, there are three agent, 0: cpu, 1: gfx1012, 2: gfx902. 

* HIP_VISIBLE_DEVICES=0 using agent:1 gfx1012, crashed with hipErrorNoBinaryForGpu.
* HIP_VISIBLE_DEVICES=1 using agent:2 gfx902, seems ROCm cannot support APU now, so pytorch cannot find GPU.

---

### 评论 #52 — unexploredtest (2020-12-12T07:42:00Z)

@xuhuisheng , so, using the `check.sh` script,
if amd_gpu targets is `gfx902;gfx1012`, with `HIP_VISIBLE_DEVICES=0` or not exporting any variables:
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ bash check.sh
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocBLAS]   2.32.0.2844-cc18d25f
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocFFT]    1.0.8.966-2d35fd6
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocPRIM]   201005
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocRAND]   201006
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
```
It get stuck here, with no errors, so `rocSPARSE` doesn't work.
Should I try amdgpu targets as `gfx1012` only?
Here is my rocminfo:
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5682672/rocminfo.txt)
Yeah. it's the way you said.

---

### 评论 #53 — xuhuisheng (2020-12-12T11:01:21Z)

@aliPMPAINT
We started to the beginning, rocSPARSE throw hipErrorNoBinaryForGpu.
I re-try navi14/25.rocsparse.sh with gfx1012.
After success compiling and installing, I execute `vi /opt/rocm/lib/librocsparse.so`, then find `gfx`, can see `hip-amdgcn-amd-amdhsa-gfx1012`, so we can confirm that rocsparse supported gfx1012.
Then execute `check/check.sh` from rocm-build, can show the hipErrorNoBinaryForGpu. That's correct, because I hadn't a gfx1012. MyGPU is gfx803.

I also upload a test_hip.cpp to verify the HIP supporting gfx1012.
https://github.com/xuhuisheng/rocm-build/blob/develop/check/run-hip.sh

Additionally, I want to clarify there are three level of ROCm.

1. kernel-driver: If the GPU could be used by OS, kernel-driver had been successfully supported. (AMD always provide driver when GPU published)
2. compiler: If rocminfo or HIP(test_hip.cpp) can run successfully. (OpenCL can use compiler to invoke specific GPU, so we often see OpenCL can and ROCm cannot)
3. ROCm math library: Aka, rocm-libs. they only support limited GPU as we know : "gfx803;gfx900;gfx906;gfx908". And if one GPU like gfx1012 wasn't contained in AMDGPU_TARGETS, HIP will throw a hipErrorNoBinaryForGpu while register kernel function. Yes, kernel function like BLAS, SPARSE, FFT, RAND, need register first then execute on GPU. each kernel function have to compiled to GPU target `hip-amdgcn-amd-amdhsa-gfx1012`. compiler help to compile source / assembly codes to binary for related GPU target.

Frameworks like tensorflow and pytorch, use HIP to replace cuda on GPU, and use rocm-libs to speed up DNN.

So what we did is re-compiling rocm-libs with AMDGPU_TARGETS="gfx1012". So HIP can find related kernel function.
But here we see a hipErrorNoBinaryForGpu on rocSPARSE, looks like rocSPARSE didnot contains related kernel function. Or rocSPARSE with gfx1012 wasn't installed correctly.

That's the point.

---

### 评论 #54 — Djip007 (2020-12-12T11:08:58Z)

> @Djip007 I applied the patches to https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver, compiled and installed it. The problem is, the kernel is incompatible with my hardware. GPUs ain't detected and WiFi doesn't even work. `dmesg | grep kfd` doesn't output anything, and `rocminfo` and `clinfo` don't detect anything either. Will it be ok if I try the patch with the 5.6.0-1036-oem, which I'm sure is compatible with my hardware?

I think yes... it may be the best... 

I have Fedora (33 now...) and rebuild the manstream (https://www.kernel.org/) kernel with my patch and a .config for my hardware... But it need some time to have a working config...

Never use Ubuntu... I find that: https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel .... and i will try to apply my patch after 'LANG=C fakeroot debian/rules clean' ... before build...
Next be sure to install rocm without rocm_dkms (cf: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#using-debian-based-rocm-with-upstream-kernel-drivers)

and add  "amdgpu.rocm_mode=2" on kerenel boot param ...


---

### 评论 #55 — Djip007 (2020-12-12T11:19:52Z)

>     1. kernel-driver. if the GPU could be used by OS, kernel-driver had been successfully supported. (AMD always provide driver when GPU published)
> 

Well in most case ... but there was (and still is ?) not supporting mix of dGPU (discret card) and iGPU (the on from APU) because of different Memory access (usage...) ... in that case my patch may help cf https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-478330720 for more detail of what it did...

---

### 评论 #56 — xuhuisheng (2020-12-12T11:35:59Z)

@Djip007 
You are right. Kernel may have bugs. Or it didn't test on gfx1012 completely.
So even we could compiled ROCm without error on gfx1012, itis not guarantee that tf/pytorch could run successfully.

While hipErrorNoBinaryForGpu is an already known issue, and could be sovled by set AMDGPU_TARGETS and re-compiling.

---

### 评论 #57 — Djip007 (2020-12-12T13:07:54Z)

@xuhuisheng 
> You are right. Kernel may have bugs. Or it didn't test on gfx1012 completely.
> So even we could compiled ROCm without error on gfx1012, itis not guarantee that tf/pytorch could run successfully.
> 
> While hipErrorNoBinaryForGpu is an already known issue, and could be sovled by set AMDGPU_TARGETS and re-compiling.

I agree with that ! 
It's two different problems. But in his case I think we will have to deal with both :crossed_fingers: 

---

### 评论 #58 — unexploredtest (2020-12-13T06:46:59Z)

@xuhuisheng  @Djip007 Thank you all for your efforts and patience, much appreciated.
So, I re-set AMDGPU_TARGETS to 'gfx1012' and recompiled rocSPARCE. If I execute `check.sh` without setting `HIP_VISIBLE_DEVICES`, I get the same `hipErrorNoBinaryForGpu` result, but if I set `HIP_VISIBLE_DEVICES=0` and make it to use agent 1, I get some interesting results.
As for `check.sh`, while it doesn't throw `hipErrorNoBinaryForGpu`, it get stuck here:
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ bash check.sh
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocBLAS]   2.32.0.2844-cc18d25f
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocFFT]    1.0.8.966-2d35fd6
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocPRIM]   201005
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
[rocRAND]   201006
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
```
I waited for hours but nothing.
And with `run-hip.sh`, we get another interesting results(after setting `HIP_VISIBLE_DEVICES=0`):
```
alipmpaint@aliPMPAINT-Bravo-17-A4DDR:~/Documents/ROCm/rocm-build/check$ bash run-hip.sh
Warning: The specified HIP target: gfx902 is unknown. Correct compilation is not guaranteed.
info: running on device Navi 14 [Radeon RX 5500/5500M / Pro 5500M]
info: allocate host mem (  7.63 MB)
info: allocate device mem (  7.63 MB)
info: copy Host2Device
```
And it get stuck here
My hope is that after patching Djip007's patches, it'll get fixed. For now I have exams but we'll come back to it within a week.
Again, thanks.

---

### 评论 #59 — xuhuisheng (2020-12-14T03:59:46Z)

@aliPMPAINT 
Looks like there are errors on copy memory from host to device. Can use `dmesg` to see if there are kernel errors.
And I think Pjip007 is right. ROCm cannot support mixing APU and dGPU.

---

### 评论 #60 — unexploredtest (2020-12-14T07:21:17Z)

@xuhuisheng 
These appeared on `dmesg` output:
```
[  105.149088] Evicting PASID 0x8003 queues
[  105.149091] Evicting PASID 0x8003 queues
[  106.949368] Evicting PASID 0x8003 queues
[  106.949372] Evicting PASID 0x8003 queues
[  113.284631] Evicting PASID 0x8003 queues
[  113.284634] Evicting PASID 0x8003 queues
[  115.848233] Evicting PASID 0x8003 queues
[  115.848235] Evicting PASID 0x8003 queues
[  117.468455] Evicting PASID 0x8003 queues
[  117.468459] Evicting PASID 0x8003 queues
[  119.086436] Evicting PASID 0x8003 queues
[  119.086439] Evicting PASID 0x8003 queues
[  121.128277] Evicting PASID 0x8003 queues
[  121.128280] Evicting PASID 0x8003 queues
[  137.284013] Evicting PASID 0x8003 queues
[  137.284017] Evicting PASID 0x8003 queues
[  139.036657] Evicting PASID 0x8003 queues
[  139.036661] Evicting PASID 0x8003 queues
[  145.330447] Evicting PASID 0x8003 queues
[  145.330449] Evicting PASID 0x8003 queues
[  268.056297] Evicting PASID 0x8003 queues
[  268.056301] Evicting PASID 0x8003 queues
```

---

### 评论 #61 — ROCmSupport (2020-12-15T12:53:04Z)

I am closing this as the required information is shared that "We are not officially supporting Navi series of cards with ROCm at present".
But you can still give a try, things might work.
We have plans to support as POR in next year, we will share some updates soon via our documentation.

---

### 评论 #62 — vdrhtc (2020-12-21T11:24:16Z)

@aliPMPAINT Hi! Did you manage to achieve any progress on this? 

Actually, I had the same problem of hanging during the Host to Device memcopy phase when I was using the amdgpu-pro SDK on my 5500XT card with OpenCL code. However, when I have migrated to ROC, the problem has gone away: pyopencl matrix multiplication [(here)](https://github.com/stefanv/PyOpenCL/blob/master/examples/matrix-multiply.py) and hip matrix multiplication from [here](https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/master/HIP-Examples-Applications/MatrixMultiplication) work OK. So memcpy should work in principle.

LLVM also lists gfx1012 as supported [here](https://llvm.org/docs/AMDGPUUsage.html)

Why there are problems?

---

### 评论 #63 — xuhuisheng (2020-12-21T11:57:51Z)

@vdrhtc Hi, Which version of ROCm do you use? ROCm-3.10 or ROCm-4.0.

---

### 评论 #64 — unexploredtest (2020-12-21T18:49:27Z)

@vdrhtc No unfortunately I couldn't succeed. My last attempt was trying out Djip007's patches (cause we thought it might be a problem with iGPU and dGPU, on a laptop) but the patches couldn't resolve the issue(the issues was with `rocSPARCE`). ( I have tested ROCm 3.10 on Ubuntu 20.04.1 5.6-oem kernel btw) So I eventually gave up, especially after hearing that they might support Navi officially next year, though they once said(https://github.com/RadeonOpenCompute/ROCm/issues/1172#issuecomment-747215616) they may have no plans for RX 5000s series.

---

### 评论 #65 — vdrhtc (2020-12-23T07:48:38Z)

@xuhuisheng, I use ROCm 3.10 from the ubuntu repo


@aliPMPAINT, I will attempt recompiling since I have only one GPU and hope that maybe it will work on my system

---

### 评论 #66 — vdrhtc (2020-12-23T13:24:20Z)

@xuhuisheng, @aliPMPAINT,

I was able to compile and run ROCm 4.0 on my gfx1012. Everything worked fine except for the hipSPARSE module: when using the sources that `repo` downloads, there is a CMake error about missing directory /opt/rocm-3.10 which means that something is not updated in hipSPARSE to 4.0. Trying to get around the problem, I have cloned the most recent  version of hipSPARSE, which wouldn't compile either. However, when I have finally tried the code from the latest release downloaded as an archive, everything worked.
![изображение](https://user-images.githubusercontent.com/3819012/102995899-12715d00-4533-11eb-83c6-fa71798cdf30.png)

The tests pass and I even managed to build CuPy:
![изображение](https://user-images.githubusercontent.com/3819012/102999385-f4f3c180-4539-11eb-8315-26970c4913bb.png)

I did not do anything special, just went on by the instructions [here](
https://github.com/xuhuisheng/rocm-build/blob/develop/README.md) and then [here
](
https://github.com/xuhuisheng/rocm-build/tree/develop/navi14)

---

### 评论 #67 — xuhuisheng (2020-12-23T15:31:59Z)

@vdrhtc 
Good job! Could you try these tests? Wish both of them could pass successfully.
* https://github.com/xuhuisheng/rocm-build/blob/master/check/run-hip.sh
* https://github.com/xuhuisheng/rocm-build/blob/master/check/run-rocblas.sh

If you had time, please try compiling pytorch for gfx1012.  :smile: 

BTW, hipSPARSE is an abstract layer for ROCm and cuda, it may be not have to compiling for gfx1012. I will try to find out where is /opt/rocm-3.10. comes from. And Don't suggest to using the latest develop branch. As there maybe unstable functions.

---

### 评论 #68 — unexploredtest (2020-12-23T15:40:03Z)

@vdrhtc Yeah, I had the same issue. `hipSPARSE` won't work.

---

### 评论 #69 — vdrhtc (2020-12-25T10:45:37Z)

@xuhuisheng 
The tests ran OK
[run_hip.log](https://github.com/RadeonOpenCompute/ROCm/files/5741760/run_hip.log)
[run_rocblas.log](https://github.com/RadeonOpenCompute/ROCm/files/5741761/run_rocblas.log)

I am also able to train a small feed-forward network with Pytorch on cuda:0 device,  so I guess everything is all right...

---

### 评论 #70 — xuhuisheng (2020-12-25T10:57:57Z)

@vdrhtc 
Sounds like ROCm-4.0 could support navi14.
Thank you very much for verifying this.

---

### 评论 #71 — unexploredtest (2020-12-25T13:58:05Z)

@vdrhtc Yeah?
> Trying to get around the problem, I have cloned the most recent version of hipSPARSE, which wouldn't compile either. However, when I have finally tried the code from the latest release downloaded as an archive, everything worked.

Could you provide the link? I also wanna test it
EDIT: this?:
https://github.com/ROCmSoftwarePlatform/hipSPARSE/releases/tag/rocm-4.0.0

---

### 评论 #72 — vdrhtc (2020-12-26T06:55:39Z)

@aliPMPAINT Yes, your edit is correct!

---

### 评论 #73 — Spacefish (2020-12-27T01:28:34Z)

Tried it on my 5700 XT Navi 10. IT WORKS!!! 👍🏻 :)
Thank you AMD Devs! Nice Christmas present!
It´s significantly faster than CPU as well:
i made a video: https://www.youtube.com/watch?v=-iYwbnvV2w0

Edit: Among further inspection, it does not really work.. If you look at the loss, it does not improve.. So whatever it computes, it does not seem to be right / no weights are changed :(

---

### 评论 #74 — unexploredtest (2020-12-27T06:36:08Z)

Oh no... Well, it seems like we should wait till ROCm adds official support for Navi series, hopefully.

---

### 评论 #75 — xuhuisheng (2020-12-27T08:53:50Z)

@Spacefish 
Thanks for feedback. Right now, I have no idea for which may cause loss not changed.
I will go back if got any more information.

---

### 评论 #76 — qyb (2020-12-28T07:09:41Z)

> Tried it on my 5700 XT Navi 10. IT WORKS!!! 👍🏻 :)
> Thank you AMD Devs! Nice Christmas present!
> It´s significantly faster than CPU as well:
> i made a video: https://www.youtube.com/watch?v=-iYwbnvV2w0
> 
> Edit: Among further inspection, it does not really work.. If you look at the loss, it does not improve.. So whatever it computes, it does not seem to be right / no weights are changed :(

How do you install torchvision? 
I have built pytorch as https://github.com/xuhuisheng/rocm-build/tree/develop/navi14
then run check/test_pytoch.py
   "True ... Navi 14 [Radeon RX 5500/5500M / Pro 5500M]"
pip3 install --no-dependencies torchvision
At last I get the same result as you

---

### 评论 #77 — xuhuisheng (2020-12-28T08:26:07Z)

@qyb 
Could you rebuild torchvision and test again?
The build of torchvision is fast. 

```
git clone https://github.com/pytorch/vision
cd vision
git checkout v0.8.2
python3 setup.py bdist_wheel
pip3 install dist/torchvision-0.8.0a0+2f40a48-cp38-cp38-linux_x86_64.whl

```

I remembered that vision used HIP to compile some cpp sources, but it didnot report hipErrorNoBinaryForGpu, so I am afraid it isn't the point.

**UPDATE** try pytorch-1.7.1(with gfx803) and torchvision-0.8.2(from pypi), the loss of mnist can compute properly. So the torchvision should be not the point.



---

### 评论 #78 — qyb (2020-12-28T08:47:56Z)

If i build from torchvision src, the example main.py throw hipErrorNoBinaryForGpu and crash, even with --no-cuda argument.

Now I change back torchvision-pypi
I noticed that mnist example script report:
MIOpen(HIP): Warning [ParseAndLoadDb] File is unreadable: /opt/rocm/miopen/share/miopen/db/gfx1012_11.HIP.fdb.txt

---

### 评论 #79 — xuhuisheng (2020-12-28T09:43:51Z)

@qyb 
Could you help me to run a test script on gfx1012?
https://github.com/xuhuisheng/rocm-build/blob/develop/check/test-pytorch-fc.py

It's an one full connection layer net, comes from https://d2l.ai/.
I try to find out whether there is the problem of pytorch, or it is the problem of MIOpen.
On my gfx803, it shows as bellow:

```
work@2f7125ec29dd:~/test$ python3 test-pytorch.py 
Sequential(
  (0): Linear(in_features=2, out_features=1, bias=True)
)
SGD (
Parameter Group 0
    dampening: 0
    lr: 0.03
    momentum: 0
    nesterov: False
    weight_decay: 0
)
epoch 1, loss: 1.165843
epoch 2, loss: 0.022983
epoch 3, loss: 0.000715
epoch 4, loss: 0.000028
epoch 5, loss: 0.000073
epoch 6, loss: 0.000128
epoch 7, loss: 0.000118
epoch 8, loss: 0.000051
epoch 9, loss: 0.000141
epoch 10, loss: 0.000065
[2, -3.4] Parameter containing:
tensor([[ 2.0002, -3.4005]], device='cuda:0', requires_grad=True)
4.2 Parameter containing:
tensor([4.2001], device='cuda:0', requires_grad=True)

```

---

### 评论 #80 — qyb (2020-12-28T09:51:03Z)

> @qyb
> Could you help me to run a test script on gfx1012?
> https://github.com/xuhuisheng/rocm-build/blob/develop/check/test-pytorch-fc.py
> 
> It's an one full connection layer net, comes from https://d2l.ai/.
> I try to find out whether there is the problem of pytorch, or it is the problem of MIOpen.
> On my gfx803, it shows as bellow:
> 
> ```
> work@2f7125ec29dd:~/test$ python3 test-pytorch.py 
> Sequential(
>   (0): Linear(in_features=2, out_features=1, bias=True)
> )
> SGD (
> Parameter Group 0
>     dampening: 0
>     lr: 0.03
>     momentum: 0
>     nesterov: False
>     weight_decay: 0
> )
> epoch 1, loss: 1.165843
> epoch 2, loss: 0.022983
> epoch 3, loss: 0.000715
> epoch 4, loss: 0.000028
> epoch 5, loss: 0.000073
> epoch 6, loss: 0.000128
> epoch 7, loss: 0.000118
> epoch 8, loss: 0.000051
> epoch 9, loss: 0.000141
> epoch 10, loss: 0.000065
> [2, -3.4] Parameter containing:
> tensor([[ 2.0002, -3.4005]], device='cuda:0', requires_grad=True)
> 4.2 Parameter containing:
> tensor([4.2001], device='cuda:0', requires_grad=True)
> ```

```
$ python3 test-pytorch-fc.py 
Sequential(
  (0): Linear(in_features=2, out_features=1, bias=True)
)
SGD (
Parameter Group 0
    dampening: 0
    lr: 0.03
    momentum: 0
    nesterov: False
    weight_decay: 0
)
epoch 1, loss: 0.985102
epoch 2, loss: 0.007260
epoch 3, loss: 0.000400
epoch 4, loss: 0.000043
epoch 5, loss: 0.000081
epoch 6, loss: 0.000161
epoch 7, loss: 0.000140
epoch 8, loss: 0.000208
epoch 9, loss: 0.000073
epoch 10, loss: 0.000093
[2, -3.4] Parameter containing:
tensor([[ 2.0006, -3.3998]], device='cuda:0', requires_grad=True)
4.2 Parameter containing:
tensor([4.2000], device='cuda:0', requires_grad=True)
```

---

### 评论 #81 — xuhuisheng (2020-12-28T09:55:39Z)

@qyb 
OK. So full connection layer training seems properly.
But convolution or pool layers used on mnist maybe fail.

Guess it should be the MIOpen issue. :cry: 

---

### 评论 #82 — vdrhtc (2020-12-28T10:31:09Z)

@xuhuisheng 

I have ran the tests in the MIOpen repo, some of them fail, please see the log attached.
[cmake_build_check.log](https://github.com/RadeonOpenCompute/ROCm/files/5746936/cmake_build_check.log)
But I am not 100% sure I have built them correctly -- I have only executed env.sh from the rocm-build directory before compilation.

---

### 评论 #83 — co-manifold (2021-01-14T09:07:03Z)

Any updates on 5500 XT?

---

### 评论 #84 — xuhuisheng (2021-01-14T09:14:53Z)

@interpharaohmetric 
Most likely, MIOpen cannot support gfx10 for convolution layer. So mnist failed.
Good news is AMD said gfx10 will get offcial supporting in 2021.

---

### 评论 #85 — nvmnghia (2021-06-01T01:06:31Z)

I'm too lazy to read all of this, but are you telling me that some old GPUs are (partially) supported, while the new ones are not? Except for the new & pricey ones?

---

### 评论 #86 — timgws (2021-06-21T01:03:58Z)

@nvmnghia 

> I can not comment on exact timelines as of today, but, roughly, will be available in next 2 to 4 months.

https://github.com/RadeonOpenCompute/ROCm/issues/887#issuecomment-822222885

---

### 评论 #87 — kvnptl (2022-06-06T23:31:16Z)

Still waiting for RX 5600 (Navi 10, RDNA 1) support ;(

---

### 评论 #88 — AnriEvs (2023-09-29T13:49:55Z)

any news for this gpu compatibility?

---

### 评论 #89 — serhii-nakon (2024-03-07T15:48:54Z)

Here Docker for RX/W5500(M) https://hub.docker.com/r/serhiin/rocm_gfx1012_pytorch

---
