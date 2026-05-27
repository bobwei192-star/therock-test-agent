# Official support to Kernel 5.10

> **Issue #1474**
> **状态**: closed
> **创建时间**: 2021-05-18T08:37:04Z
> **更新时间**: 2021-06-02T09:57:28Z
> **关闭时间**: 2021-06-02T09:50:14Z
> **作者**: staticdev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1474

## 描述

ROCm is always updated with latest graphics cards (also phased out not so old ones like RX 580). It would be very nice to keep the pace with the kernel. Latest versions of Ubuntu/Debian and all other Linux are coming with kernel 5.10. 

Kernel 5.4 is now very outdated. Shouldn't ROCm 4.2 officially support the new ones instead?

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-06-01T08:57:29Z)

Hi @staticdev 
Thanks for reaching out.
Agree with your point.
Let me get some information from the team and share you soon.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-06-02T09:50:14Z)

Hi @staticdev 
We started validating the latest kernels like 5.8+ with the latest ROCm sources and we will update the docs with the same in the future releases.
I can not comment on specific version of kernel but I am sure that its better than the current 5.4.
We have internal policies and standards for verification/validation of ROCm with set of kernels/OS versions and thus we will make them official.
It does not mean that things do not work on any other kernels, mostly things might work(telling you as per my past experience).
Thank you.


---
