# Problems installing ROCm on Ubuntu Server

> **Issue #1152**
> **状态**: closed
> **创建时间**: 2020-06-17T09:31:45Z
> **更新时间**: 2020-06-19T09:11:47Z
> **关闭时间**: 2020-06-19T09:00:05Z
> **作者**: kazulittlefox
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1152

## 描述

## issue
I have tried installing ROCm on Ubuntu server(16.04 LTS/18.04 LTS) but it cannot recognize GPU devices properly,
since ROCm and tools do not work properly.

## To reproduce
 * Making platform with Ubuntu server(16.04 or 18.04).
 * Installing ROCm as it is shown on ROCm documents.
 * Running rocminfo and clinfo

If you have installed ROCm properly, you may see hardware infos, but I have encountered these errors.

(rocminfo)
```
$ /opt/rocm-3.5.0/bin/rocminfo 
ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
johndoe is member of video group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

(clinfo)
```
$ /opt/rocm-3.5.0/opencl/bin/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3137.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0

```

(rocm-smi)
```
$ /opt/rocm-3.5.0/bin/rocm-smi 
Unable to get devices, /sys/class/drm is empty or missing
ERROR: No DRM devices available. Exiting
```

And I could not find /dev/dri/* and /dev/kfd/* ,too.


 



---

## 评论 (8 条)

### 评论 #1 — c0d3st0rm (2020-06-17T12:37:37Z)

What GPUs do you have in the system? And do they have displays connected to them?

---

### 评论 #2 — kazulittlefox (2020-06-17T13:38:52Z)

@c0d3st0rm 
I user 2xRADEONVII in our system.
And i have not been connected to any monitors since the system has been used as server.

---

### 评论 #3 — c0d3st0rm (2020-06-17T17:17:47Z)

Could you try with monitors attached to both, to debug? I recall a system not booting with a Vega 56 without a monitor attached (although I assume you still have a basic VGA adapter provided by the BMC in your server). I don't know if this would render the cards unusable as targets for compute though.

---

### 评论 #4 — kazulittlefox (2020-06-18T06:31:21Z)

I have tried to attach monitor to both cards and checked them work fine then I have uninstalled and installed ROCm components, since ROCm and their tools still returns error and does not work properly.

---

### 评论 #5 — kazulittlefox (2020-06-18T08:13:07Z)

The error I caught was almost the same as this issue:

#1150 

---

### 评论 #6 — kazulittlefox (2020-06-19T09:00:05Z)

I am verry sorry for not checking the kernel version well(which is lower than 4.15).
So I would like to close this issue.

---

### 评论 #7 — c0d3st0rm (2020-06-19T09:01:30Z)

Are you able to try the HWE kernel?

---

### 评论 #8 — kazulittlefox (2020-06-19T09:11:47Z)

> Are you able to try the HWE kernel?

Yes. I have tried HWE kernel on Ubuntu 16.04 LTS and it worked in my environment.

---
