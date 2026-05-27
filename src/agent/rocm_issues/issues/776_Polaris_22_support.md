# Polaris 22 support?

> **Issue #776**
> **状态**: closed
> **创建时间**: 2019-04-18T19:02:30Z
> **更新时间**: 2020-10-28T23:15:45Z
> **关闭时间**: 2019-04-19T16:32:49Z
> **作者**: jeffhammond
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/776

## 描述

https://www.techpowerup.com/gpu-specs/amd-polaris-22.g821 says ROCm isn't supported on Polaris 22.  Is that accurate and not going to change?

I am running Ubuntu 18.10 with Linux 4.18 and the ROCm stack appears to be completely broken, include HCC and OpenCL.

```
$ rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.3/rocminfo/rocminfo.cc. Call returned 4104
```

```
$ lsmod | grep amd
amdgpu               3518464  11
amdttm                102400  1 amdgpu
amd_sched              28672  1 amdgpu
amdkcl                 24576  3 amd_sched,amdttm,amdgpu
amd_iommu_v2           20480  1 amdgpu
drm_kms_helper        172032  2 amdgpu,i915
drm                   458752  10 drm_kms_helper,amd_sched,amdttm,amdgpu,i915,amdkcl
i2c_algo_bit           16384  3 igb,amdgpu,i915
```

---

## 评论 (9 条)

### 评论 #1 — jlgreathouse (2019-04-19T16:32:46Z)

No, Polaris 22 ("Vega M") is not supported at this time.

---

### 评论 #2 — jeffhammond (2019-04-29T18:53:13Z)

https://www.phoronix.com/scan.php?page=news_item&px=AMDKFD-Vega-M-Plus-More seems to suggest that support for Vega M is happening. Can you confirm?

---

### 评论 #3 — jlgreathouse (2019-05-02T21:27:02Z)

Vega M may make it into our list of enabled GPUs as of the upcoming ROCm 2.4. However, I don't believe it will be part of our "official support" list. I make this distinction because VegaM won't go through the level of internal validation and verification that our "supported" GPUs go through on each release. It appears support has been added in [the kernel driver as of 2.4](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.4.0/drivers/gpu/drm/amd/amdkfd/kfd_device.c#L406) and [Thunk as of 2.3](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/roc-2.3.0/src/topology.c#L181).

With that in mind, when ROCm 2.4 drops, I will be interested to hear your feedback on if things work. :)

It appears that the kernel driver and Thunk will return that Vega M is ISA 803. [ROCr handles gfx803 cleanly](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-2.3.0/src/loader/loaders.cpp#L78), as does HIP/HCC.

In the OpenCL runtime, [Vega M is not directly in the device list](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-2.3.0/runtime/device/rocm/rocdefs.hpp#L59), but [it treats all gfx803 GPUs as Fiji](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-2.3.0/runtime/device/rocm/rocdevice.cpp#L79).

So I think things may work, but because I don't have a Vega M to test this on right now (and because it's not going through our official support validation pipeline), I can't guarantee things. So I'll be interested in your feedback. :)

---

### 评论 #4 — jeffhammond (2019-05-02T21:28:38Z)

Thanks for the details.  That is very helpful.  I'll try this as soon as I can.

---

### 评论 #5 — jasontitus (2020-04-04T11:46:20Z)

Did this ever work?  Curious if Hades Canyon NUCs will ever have ROCm support. 

---

### 评论 #6 — jeffhammond (2020-04-06T20:48:15Z)

I have nothing to report here.  I got busy and prioritized other things, so I can't say one way or the other if it works, although the information I was able to find made me pessimistic.

---

### 评论 #7 — jeffhammond (2020-04-06T20:50:45Z)

I have no idea what impact it could have on this topic, but https://www.tomshardware.com/news/intel-graphics-driver-update-hades-canyon-amd-12-month-delay may be relevant.

---

### 评论 #8 — jasontitus (2020-06-21T10:27:44Z)

Now that 2.5 has dropped, has anyone been able to test if it works with Polaris 22?

---

### 评论 #9 — jeffhammond (2020-10-28T23:15:45Z)

It took me a long time to get to Linux 5.3 but I finally tried it today with Ubuntu 20 and it's working.

---
