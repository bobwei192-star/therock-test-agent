# clinfo crashes computer ubuntu 20.04

> **Issue #1117**
> **状态**: closed
> **创建时间**: 2020-05-24T14:11:34Z
> **更新时间**: 2021-02-22T08:48:24Z
> **关闭时间**: 2021-02-17T08:04:34Z
> **作者**: Goddard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1117

## 描述

When running clinfo it crashes the computer, or at the very least visually crashes video.

This is on a 3 agent system.

Threadripper 1950x
RX 580
RX 580

---

## 评论 (10 条)

### 评论 #1 — notokcomputerbadcomputer (2020-05-24T16:07:13Z)

You could always try a fresh install WITH recommended distribution AND recommended kernel. You can find those in documentation.

---

### 评论 #2 — Rmalavally (2020-05-24T16:13:49Z)

Thank you for reaching out. 

For all supported environments, you can find the AMD ROCm documentation at:
http://rocmdocs.amd.com

If you are unable to find the instructions you need, please let us know.

AMD ROCm Documentation Team

---

### 评论 #3 — Goddard (2020-05-24T19:16:38Z)

This repository is for developers correct?
I am merely letting developers know of a bug on a platform I expect will be supported in the future.

Everything works fine when you have 1 GPU, but if you have 2 it crashes video.

---

### 评论 #4 — Rmalavally (2020-05-24T19:55:46Z)

Thank you for letting the community know. You are right, Ubuntu 20.04 is not supported as yet.



---

### 评论 #5 — ableeker (2020-05-25T20:08:26Z)

Not sure if this is the same case, but clinfo will crash after installing ROCm. By crash I mean it will cause a 'Segmentation fault (core dump)'. I have to install libtinfo5, or libncurses5 before it will work. Anyway, after some trial and error I have rocm-dev working on my computer with Ubuntu 20.04. Well, the OpenCL part anyway, I haven't tried other parts.

---

### 评论 #6 — Goddard (2020-05-26T01:38:39Z)

Thanks for letting me know.  Pretty sure I had both of these installed when attempting to get it going, but I can give it a go again.  When I attempted to run things other then clinfo it totally locked up video.  Tensorflow did not want to work at all.

---

### 评论 #7 — alfabuster (2020-06-05T07:22:33Z)

Version 3.5 for Ubuntu 20.04 change nothing. Same errors like for 3.3...

---

### 评论 #8 — notokcomputerbadcomputer (2020-06-05T07:36:44Z)

```
The AMD ROCm v3.5.x platform is designed to support the following operating systems:

Ubuntu 16.04.6(Kernel 4.15) and 18.04.4(Kernel 5.3)
CentOS 7.7 (Kernel 3.10-1062) and RHEL 7.8(Kernel 3.10.0-1127)(Using devtoolset-7 runtime support)
SLES 15 SP1
CentOS and RHEL 8.1(Kernel 4.18.0-147)
```

---

### 评论 #9 — alfabuster (2020-06-05T07:41:50Z)

Yes, I hope 4.0 release will fix Ubuntu 20.04...

---

### 评论 #10 — ROCmSupport (2021-02-17T08:04:34Z)

Hi @Goddard 
Thanks for reaching us.
I am closing this issue as the latest ROCm 4.0 supports Ubuntu 20.04.x and hope this problem is gone with ROCm 4.0+Ubuntu 20.04.x.
Request you to try the same.
Request you to open a new issue if any, so that we can chase down the problem.
Thank you.


---
