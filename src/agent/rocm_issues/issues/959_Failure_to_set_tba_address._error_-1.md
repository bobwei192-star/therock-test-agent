# Failure to set tba address. error -1

> **Issue #959**
> **状态**: closed
> **创建时间**: 2019-12-07T11:16:38Z
> **更新时间**: 2023-12-18T16:05:34Z
> **关闭时间**: 2023-12-18T16:05:34Z
> **作者**: PlutoniumHeart
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/959

## 描述

Linux kernel version: Git tag v5.4, with known required configures turned on
ROCm version: 2.10 (repo)
Device: Ryzen 7 2700U with Vegas 10

```
$ ./clinfo
Number of platforms:                             2
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (3019.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 1.1 Mesa 19.2.6
  Platform Name:                                 Clover
  Platform Vendor:                               Mesa
  Platform Extensions:                           cl_khr_icd


  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

```

```
$ ./rocminfo
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-2.10/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
After running rocminfo dmesg shows:

```
# dmesg
...
[   71.181067] Failure to set tba address. error -1.
...
```

---

## 评论 (4 条)

### 评论 #1 — JonChesterfield (2020-09-28T18:48:02Z)

Same behaviour on a 2700U here, with Debian's stock 5.8.0-2

---

### 评论 #2 — LinAGKar (2021-03-17T19:30:58Z)

Same on OpenSUSE Tumbleweed with the same APU.

---

### 评论 #3 — nartmada (2023-12-13T21:27:36Z)

Hi @PlutoniumHeart, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #4 — nartmada (2023-12-18T16:05:34Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
