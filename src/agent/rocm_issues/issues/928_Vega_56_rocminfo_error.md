# Vega 56 rocminfo error

> **Issue #928**
> **状态**: closed
> **创建时间**: 2019-11-03T11:14:29Z
> **更新时间**: 2022-01-28T06:30:42Z
> **关闭时间**: 2022-01-28T06:30:42Z
> **作者**: jjrugui
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/928

## 描述

Hi, 

I just installed ROCm following the repo readme on an ubuntu 18.04 install. One I run rocminfo I get the following error:

`ROCk module is loaded
jugu is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.`

And trying to run clinfo I get the following:

`Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)`

Even though the error is about the device ID I can see the GPU on rocm-smi.

Any info on how to debug the issue? I'm on Ubuntu 18.04, fresh install and updated, upstream kernel, Vega 65, ryzen 1400 and gigabyte aorus wifi

---

## 评论 (5 条)

### 评论 #1 — jjrugui (2019-11-05T12:40:33Z)

It has to do with permissions since when executing as root there is no problem. As far as I know I have followed exactly the installation process.

Any idea how to fix this issue?

`5.0.0-32-generic #34~18.04.2-Ubuntu SMP Thu Oct 10 10:36:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux`

If I strace the execution of rocminfo I find the following error:

`openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 EACCES (Permission denied)`

---

### 评论 #2 — phush0 (2019-11-12T12:28:29Z)

you have to add group video and make yourself part of this group

---

### 评论 #3 — jjrugui (2019-11-13T23:32:45Z)

I'm already in the video group

---

### 评论 #4 — billyswong (2019-11-14T13:36:48Z)

As like my post in #934 the issue may not be whether the user account is in `video` group. Look at the rocminfo error message below:
 ```
$ sudo /opt/rocm/bin/rocminfo
ROCk module is loaded
Failed to get user name to check for video group membership
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
⋮
```
It says "Failed to get user name", even when the command continue to run okay under sudo mode.

---

### 评论 #5 — ROCmSupport (2022-01-28T06:30:42Z)

This issue is not seen anymore with the latest ROCm 4.5/4.5.1.

---
