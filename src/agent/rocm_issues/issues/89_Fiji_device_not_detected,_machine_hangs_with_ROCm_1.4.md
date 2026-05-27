# Fiji device not detected, machine hangs with ROCm 1.4

> **Issue #89**
> **状态**: closed
> **创建时间**: 2017-02-23T23:51:53Z
> **更新时间**: 2017-02-24T02:02:28Z
> **关闭时间**: 2017-02-24T02:02:28Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/89

## 描述

System Ubuntu 16.04
Hardware: CPU AMD FX-8350, GPU: Fiji (Fury Nano)

Installed:  rocm opencl-rocm opencl-rocm-dev
Rebooted with the new kernel, after which I can't get any devices detected nor run any HIP, hsa, or OpenCL code.

* bit_extract HIP sample gives:
```
### HCC STATUS_CHECK Error: HSA_STATUS_ERROR_OUT_OF_RESOURCES (0x1008) at file:/home/scchan/code/github/hcc-roc-1.4.x/hcc/lib/hsa/mcwamp_hsa.cpp line:2728
Aborted (core dumped)
```

* stadard clinfo hangs, the one provided by rocm outputs this:
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (2300.5)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 

  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

* kern.log contains the following (after running clinfo)
```
kfd: qcm fence wait loop timeout expired
kfd: unmapping queues failed.
kfd: the cp might be in an unrecoverable state due to an unsuccessful queues preemption<4>[ 3721.447737] amdkfd: Resetting wave fronts on dev ffff8800bf91bc00
```
This is often preceded by some NetworkManager stats printout. (Occasionally the machine hangs or does not respond over the network -- maybe related, maybe not.) 

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-02-24T00:25:42Z)

We do not support the AMD FX 8350 with GFX8 or newer GPU FIJI.  FIJI  use PCIe Atomics which are only in PCIe Gen3 CPU,  Intel Haswell, or newer and AMD new Rysen Processor.

We never tested it but W9100 or  Radeon 290 should work since they do not support PCIe atomics.

Greg

On Feb 23, 2017, at 5:51 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


System Ubuntu 16.04
Hardware: CPU AMD FX-8350, GPU: Fiji (Fury Nano)

Installed: rocm opencl-rocm opencl-rocm-dev
Rebooted with the new kernel, after which I can't get any devices detected nor run any HIP, hsa, or OpenCL code.

  *   bit_extract HIP sample gives:

### HCC STATUS_CHECK Error: HSA_STATUS_ERROR_OUT_OF_RESOURCES (0x1008) at file:/home/scchan/code/github/hcc-roc-1.4.x/hcc/lib/hsa/mcwamp_hsa.cpp line:2728
Aborted (core dumped)


  *   stadard clinfo hangs, the one provided by rocm outputs this:

Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (2300.5)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices

  Platform Name:                                 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)


  *   kern.log contains the following (after running clinfo)

kfd: qcm fence wait loop timeout expired
kfd: unmapping queues failed.
kfd: the cp might be in an unrecoverable state due to an unsuccessful queues preemption<4>[ 3721.447737] amdkfd: Resetting wave fronts on dev ffff8800bf91bc00


This is preceded by the NetworkManager stats. (Occasionally the machine hangs or does not respond over the network -- maybe related, maybe not.)

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/89>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuR3AJbPWpEaN4plPjETa0V0az7Wbks5rfhuagaJpZM4MKp4W>.



---

### 评论 #2 — pszi1ard (2017-02-24T00:32:08Z)

Thanks for the quick reply! It would be nice if the runtime somehow warned me about this rather than behaving all weird.

I've now plugged the card into a HSW-E machine and will try again later.

---

### 评论 #3 — gstoner (2017-02-24T00:34:43Z)

We are working on tool to look and see if you support  PCIe atomics and warn you,  We also see you have to put in on the right slot on Intel systems.

Greg
On Feb 23, 2017, at 6:32 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


Thanks for the quick reply! It would be nice if the runtime somehow warned me about this rather than behaving all weird.

I've now plugged the card into a HSW-E machine and will try again later.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/89#issuecomment-282167124>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYucRM3P2SM3aU2wTjiuNZszg0t-ks5rfiUJgaJpZM4MKp4W>.



---

### 评论 #4 — pszi1ard (2017-02-24T00:38:34Z)

What does "right slot" mean? I'm using an Intel X99 motherboard now.

Do you have some documentation on what exactly is required and why? I can't imagine such limitations are beneficial without a reasonable fallback, but I might be wrong and I'm all for it if it e.g. allows leaner and faster driver implementation.

---

### 评论 #5 — pszi1ard (2017-02-24T02:02:28Z)

Seems to "work" -- sortof, so I'll close this and open new ones.

---
