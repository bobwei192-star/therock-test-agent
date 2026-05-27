# Problem using ROCm

> **Issue #4**
> **状态**: closed
> **创建时间**: 2016-04-21T03:43:00Z
> **更新时间**: 2016-08-20T18:49:33Z
> **关闭时间**: 2016-08-20T18:49:33Z
> **作者**: briansp2020
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/4

## 描述

Hi,
I have been following the development of hcc and ROCm for a while. I have used most of previous versions and had them running on my Kaveri APU system. However, since I updated to ROCm-1.0 release, none of the executable I compile runs.
When I try to run executable compiled with hcc, I get 

`### Error: HSA_STATUS_ERROR_INCOMPATIBLE_ARGUMENTS (4109) at line:1757`

Funny thing is, my code is not very long. They are toy examples and are well less than a thousand lines of code.

I can run /opt/rocm/hsa/sample/vector_copy and it prints out success messages. But that's the only thing I can run right now.

Also, configuring hcc compilation environment does not find hsa installation any more. Before installing ROCm, cmake would find everything without any issues. Now, I get

`=============================================`
`HCC version: 0.10.16163-caab0f1-7e4cd9e`
`=============================================`
`CMake Error at CMakeLists.txt:261 (MESSAGE):`
`Neither OpenCL nor HSA is available on the system!`

What did I do wrong?


---

## 评论 (8 条)

### 评论 #1 — scchan (2016-04-21T14:52:21Z)

Fiji family dGPU is the platform we support with this release.  
We included two hcc compiler packages with different compiler backends.  The default hcc with the native GCN ISA backend (hcc_lc) is incompatible with APUs.  The other hcc package that uses the hsail backend (hcc_hsail) would work with HSA APUs.  You could modify the symlink /opt/rocm/hcc to point to /opt/rocm/hcc-hsail.  


---

### 评论 #2 — scchan (2016-04-21T15:01:25Z)

Regarding building the hcc from source, we've been going through a series of directory changes, the roc-1.0.x branch should be able to detect the ROCm runtime files correctly with the new setup.  I'll be merging those changes back to master soon.


---

### 评论 #3 — briansp2020 (2016-04-22T05:12:36Z)

Changing hcc to point to hcc-hail worked!

Thanks


---

### 评论 #4 — briansp2020 (2016-05-17T04:00:32Z)

Hi,
I'm trying to port Parboil to hip and ran into some issues (see https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/issues/3). It looks like hip tests are failing on my machine. I did not run that test when I had ROCm-1.0. So, I do not know whehter something was broken with ROCm-1.1 or whether the problem was there from ROCm-1.0. Also, I was OC my iGPU a bit at 900MHz. However, some the tests are still failing at iGPU running at 750MHz.

Can some one with Kaveri machine run HIP [tests](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/tree/master/tests) and let me know whether there are issues with ROCm running on APUs (I know APUs are not the priority right now) or whether I should suspect my hardware?

Thanks


---

### 评论 #5 — briansp2020 (2016-08-17T18:33:53Z)

ROCm 1.2 release fixed my sgemm issue on my i7-6700+Fiji. However, my Udacity cs344 still fails and dumps core (see https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/issues/3). Udacity cs344 problem set used to work correctly on Kaveri and the cote-dump happened only on Fiji. It seems like hcc Fiji native path is not as well tested as HSAIL path. It is possible to use HSAIL path on Fiji setup as well?


---

### 评论 #6 — ghost (2016-08-17T19:04:12Z)

Hey Brian,

Both the LC(native) and HSAIL backends should be installed if you used the pre-built packages.

In order to switch backends you can switch the /opt/rocm/hcc symlink to point to either /opt/rocm/hcc-lc or hcc-hsail

Note that our focus going forward is LC first. So we encourage everyone to work on LC based setups. But in situations like this where a LC bug is suspected, comparing against HSAIL is still useful.


---

### 评论 #7 — briansp2020 (2016-08-18T04:30:48Z)

Hi arodrigx7,
I tried HSAIL by changing the symlink and it still core-dumps on my i7+Fiji setup. I no longer have my Kaveri setup. So, I can not test it on that machine. :( 


---

### 评论 #8 — ghost (2016-08-18T17:45:13Z)

If you have a good problem reproduction case, I would recommended opening an issue on the HIP github project. If the issue is with HIP/HCC I'm sure Ben/SiuChi/Maneesh will find it and patch it.


---
