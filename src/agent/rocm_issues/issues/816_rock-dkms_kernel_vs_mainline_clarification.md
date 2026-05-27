# rock-dkms kernel vs mainline clarification

> **Issue #816**
> **状态**: closed
> **创建时间**: 2019-06-08T21:00:59Z
> **更新时间**: 2019-09-20T08:31:07Z
> **关闭时间**: 2019-09-20T08:31:07Z
> **作者**: nicolaerosia
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/816

## 描述

`README.md` lists the differences between upstream kernel driver and `rock-dkms` but I find it a bit vague. Any help would be appreciated.

"Includes the latest GPU firmware"/"Does not include most up-to-date firmware", what firmware are we talking about? Where is it located?

"Features and hardware support varies depending on kernel version" exactly what features? Could you give some examples?

"IPC and RDMA capabilities are not yet enabled" When is this needed? I guess RDMA is needed when doing distributed computing with multiple separate physical machines? What about IPC? I can't seem to understand how the kernel driver is involved here.

---

## 评论 (3 条)

### 评论 #1 — JMadgwick (2019-06-11T14:06:01Z)

> "Includes the latest GPU firmware"/"Does not include most up-to-date firmware", what firmware are we talking about? Where is it located?

I believe this refers the the firmware stored in `/lib/firmware/amdgpu`.
The version included in the kernel firmware packages is not always up to date with the firmware released with Rocm. When Rocm is installed you get newer firmware. This is only a big deal when a product is new. For example when the Radeon VII was launched the firmware was not available straight away in the normal distro packages and Rocm had to be installed to get access to it (although it could also be extracted directly from the .deb).

The devs might be along to answer the other queries.


---

### 评论 #2 — kentrussell (2019-06-17T15:46:09Z)

@JMadgwick is right. The DKMS package includes the updated firmware .bin files as part of the rock-dkms package, so newer firmware (supporting newer cards, FW fixes, etc) is included and good to have. Newer firmware is an issue maybe 5% of the time, so that 95% improvement is a plus

The entire DKMS package is based on kernel versions. We have these kinds of lines all through the kernel to support different kernel versions:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_device.c#L671

Note that this indicates that only 4.15-and-newer can support resizeable BARs.

For IPC and RDMA, the support is in ROCK but not upstream (see kfd_ipc.c and kfd_rdma.c files here, but are absent upstream). Upstream kernels don't have this functionality yet, so if you want to use KFD's RDMA and IPC functionality, you'd need to use ROCm. 

Hopefully that helps!

---

### 评论 #3 — nicolaerosia (2019-09-20T08:31:07Z)

Thank you!

---
