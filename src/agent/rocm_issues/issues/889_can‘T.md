# can‘T

> **Issue #889**
> **状态**: closed
> **创建时间**: 2019-09-17T11:53:39Z
> **更新时间**: 2023-08-05T18:23:45Z
> **关闭时间**: 2023-08-05T18:23:45Z
> **作者**: Bitllion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/889

## 描述

*(无描述)*

---

## 评论 (8 条)

### 评论 #1 — Bitllion (2019-09-17T11:54:49Z)

/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/x86_64/clinfo

ROCk module is loaded
root is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.7/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (2949.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices


  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

---

### 评论 #2 — ITfirewall (2019-09-17T19:02:03Z)

 Hey Bitllion, 

 Whats your OS and Gpu???  

---

### 评论 #3 — jppyykm (2019-09-22T15:24:11Z)

I have a similar problem. I am running Ububtu and my gpu is RX 480. 
```
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.7/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
https://rocm.github.io/ROCmInstall.html  <-- Following installation 
 
Installing this thing has been really, really annoying. I broke my Mint installation a few times tinkering to make it run there. I got tired and installed Ubuntu so it is supported. Now this.

---

### 评论 #4 — ITfirewall (2019-09-23T06:31:13Z)

Hi jppyykm,

Can you try again with an older version of ROCm driver??? ( try ROCm 2.6, 2.5,....) from repository.
I have a different problem with ubuntu 16.04 + ROCm 2.7.1, this is causing a problem with OpenCL. 


---

### 评论 #5 — jppyykm (2019-10-04T13:27:21Z)

Hi! I am having all sorts of trouble. I am working on it in sprints.. getting this thing to work is urgh,,

---

### 评论 #6 — b4551k5 (2019-11-09T17:13:38Z)

I got the same issue. It says:

"hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events."

I installed rocm-dev since my kernel seems to be not supported by rocm-dkms anyway. 

---

### 评论 #7 — jeffk95 (2020-02-16T23:14:08Z)

#1005 fixed the issue for me (Ubuntu 19.10 / Vega 56)

---

### 评论 #8 — leoniescape (2020-04-15T06:29:32Z)

I had same problem too. And it works after I add myself into groups "video".

---
