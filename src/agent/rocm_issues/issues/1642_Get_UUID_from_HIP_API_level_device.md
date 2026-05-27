# Get UUID from HIP API level device

> **Issue #1642**
> **状态**: closed
> **创建时间**: 2021-12-17T08:48:19Z
> **更新时间**: 2023-06-07T16:06:54Z
> **关闭时间**: 2023-06-07T16:06:54Z
> **作者**: bertwesarg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1642

## 描述

Is there a way, to get the UUID of a device from the HIP API? I can see the UUID of devices with `rocm-smi --showuniqueid` and also with `rocminfo`. But I would like to relate them, without considering `HIP_VISIBLE_DEVICES`.

---

## 评论 (10 条)

### 评论 #1 — bertwesarg (2021-12-17T09:00:06Z)

FYI, CUDA provides the UUID in the `struct cudaDeviceProp::uuid` member. 

---

### 评论 #2 — ROCmSupport (2021-12-20T11:11:06Z)

Hi @bertwesarg 
Thanks for reaching out.
I will get information from HIP team and will update you asap.
Thank you.

---

### 评论 #3 — JBlaschke (2022-03-07T21:54:33Z)

Are there any updates on this? I would also be interested.

---

### 评论 #4 — bertwesarg (2022-03-08T06:11:12Z)

They implemented it and promised us to get a beta release. But nothing in our hands yet.

---

### 评论 #5 — ROCmSupport (2022-03-08T07:17:18Z)

Hi @bertwesarg 
Our HIP team implemented it, changes are ready, will be merged into our internal builds soon and thus it will be part of Release branch.
As per the discussion with HIP team, this will be part of ROCm 5.2 release and request to wait for the same.
Thank you.

---

### 评论 #6 — bertwesarg (2022-03-08T09:04:03Z)

That is good news. Thanks for the update. A preview build, so that we can test the feature is still desirable. I will talk to my AMD contact again.

---

### 评论 #7 — bertwesarg (2022-05-12T11:34:47Z)

Dear all,

`hipDeviceGetUUID` returns a 16 byte UUID (`hipUUID`), but ROCM SMI only a 8 byte (`uint64_t`) unique ID. Are they the same? And if so, how to match these?

Thanks.

---

### 评论 #8 — TimourPaltashev (2022-05-13T17:53:24Z)

Hi Bert, 
Below the comment from developers:
HIP makes use of ROC Runtime to query the UUID. As per ROCr API spec (See https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/83b46ab91086e10edbc6100d5e55cac11c9b5d7a/src/inc/hsa_ext_amd.h#L291-L300), the UUID it returns is of the form "GPU-<16-digit-hex-string>". HIP returns the 16-digit hex string.

As far as how ROCr converts the 8 byte value returned by ROCm SMI to a 16 byte value see https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/1594b0778a4d9a7c7065190489aa8be901e66c34/src/core/runtime/amd_gpu_agent.cpp#L993-L1011 for the implementation.

Regards,
Maneesh

---

### 评论 #9 — bertwesarg (2022-05-13T19:28:52Z)

Thanks, this matches my assumption.

---

### 评论 #10 — bertwesarg (2023-06-07T16:06:54Z)

closed as solved

---
