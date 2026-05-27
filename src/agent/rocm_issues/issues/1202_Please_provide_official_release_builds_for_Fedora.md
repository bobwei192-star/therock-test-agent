# Please provide official release builds for Fedora

> **Issue #1202**
> **状态**: closed
> **创建时间**: 2020-08-24T20:33:20Z
> **更新时间**: 2021-04-07T02:03:32Z
> **关闭时间**: 2020-12-15T11:33:30Z
> **作者**: rigtorp
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1202

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

It would be great to have official release packages for Fedora in addition to the RHEL packages.

---

## 评论 (8 条)

### 评论 #1 — rkothako (2020-08-27T05:48:53Z)

We will keep updating the documentation when we have plans to support any new OS. But at present, we have no plans to support Fedora.

---

### 评论 #2 — francisrichards (2020-08-30T18:32:38Z)

Thanks for the response rkothako, for what it is worth, I too would greatly benefit from official release packages for Fedora.  Take care.

---

### 评论 #3 — rigtorp (2020-08-31T22:10:09Z)

@rkothako It should be quite easy to add Fedora builds given that you already provide RHEL builds. Switching the container image from RHEL to Fedora should be enough to produce Fedora builds.

---

### 评论 #4 — cmdrogogov (2020-11-11T16:27:06Z)

+1 for this.

I've been fighting to try and get this running on FC33 all morning.   It's further complicated by the fact that the ROCm repo packages in 3.9.7 spit out patform_python dependency errors when installing (specifically rocm-smi) , but on the other Fedora DO have some rocm packages in their updates repo, but they are all out of date.

---

### 评论 #5 — francisrichards (2020-11-11T16:44:22Z)

> +1 for this.
> 
> I've been fighting to try and get this running on FC33 all morning. It's further complicated by the fact that the ROCm repo packages in 3.9.7 spit out patform_python dependency errors when installing (specifically rocm-smi) , but on the other Fedora DO have some rocm packages in their updates repo, but they are all out of date.

For what it's worth this is how I got OpenCL support working on Fedora 32 and 33 with an RX 580 using AMDGPU-Pro  (My use case is Dark Table).  I still use the native amdgpu non-pro for graphics as per the documentation.
https://ask.fedoraproject.org/t/guide-install-amdgpu-pro-opencl-in-fedora-32/7929 

---

### 评论 #6 — rigtorp (2020-11-11T19:45:33Z)

@cmdrogogov I have a hacky way to install the CentOS packages on Fedora 33: https://rigtorp.se/notes/rocm/

---

### 评论 #7 — ROCmSupport (2020-12-15T11:33:30Z)

Thanks all for the feedback.
Currently we are not providing official support of ROCm for fedora.
And also we do not have enough resources to validate and confirm every OS. We have definite plans to support a specific list of OSes only and we are mentioning all supported OSes in rocm docs.
RPM packages might work on other oses but we can not give guarantee.
Thank you.

---

### 评论 #8 — cmdrogogov (2021-04-07T02:03:32Z)

@ROCMSupport - 

You should reconsider this, now that CentOS is effectively dead.

---
