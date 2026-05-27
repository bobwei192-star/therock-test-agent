# When is Radeon VII going to work with stock Linux kernel (i.e. withouth rock-dkms)

> **Issue #1478**
> **状态**: closed
> **创建时间**: 2021-05-20T19:12:52Z
> **更新时间**: 2021-05-31T05:31:50Z
> **关闭时间**: 2021-05-31T05:31:50Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1478

## 描述

On ROCm 3.x, Radeon VII is working fine with a variety of stock Linux kernels, such as: 5.10, 5.11, 5.12. That means that Radeon VII can be used without installing rock-dkms.

Starting with ROCm 4.1, Radeon VII does not work anymore with *any* stock Linux kernel, and requires the installation of rocm-dkms. This fact is noted in the release notes: https://rocmdocs.amd.com/en/latest/Current_Release_Notes/Current-Release-Notes.html#driver-compability-issue-in-rocm-v4-1

I would like to know when Radeon VII can be used again without rock-dkms (as was possible with ROCm 3.x). And which stock Linux kernel version will be required for that (maybe the upcoming 5.13?)


---

## 评论 (2 条)

### 评论 #1 — preda (2021-05-21T10:22:24Z)

Please see also, more-or-less the same problem:
#1423
#1431

While those issues have been closed, the underlying problem is not fixed in ROCm 4.2: the fact remains that Radeon VII can not be used with a standard Linux kernel anymore, something that was possible with earlier ROCm versions. And, the fact that the problem is now documented in the release notes, does not mean that it's fixed.


---

### 评论 #2 — preda (2021-05-31T05:31:50Z)

Good news: it seems this problem is fixed in the 5.13 Linux kernel. I tried with 5.13-rc4 and ROCm 4.2.0 works with the stock kernel (i.e. without installing rock-dkms).


---
