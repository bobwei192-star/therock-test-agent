# Is it plan to upload rocm into Debian ?

> **Issue #304**
> **状态**: closed
> **创建时间**: 2018-01-19T07:10:28Z
> **更新时间**: 2020-11-18T11:35:52Z
> **关闭时间**: 2020-11-18T11:35:52Z
> **作者**: picca
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/304

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Hello, it would be great if out of the box peoples could have rocm uploaded into Debian.

So is it plan ?

Thanks


Frederic

---

## 评论 (6 条)

### 评论 #1 — preda (2018-01-31T10:43:07Z)

In my case, ROCm 1.7 with OpenCL works fine on Ubuntu 17.10 (which, note, is not the *supported* 16.04). So maybe you could try and see.

---

### 评论 #2 — picca (2018-01-31T21:49:02Z)

Hello, great, but my question was more about an upload of rocm into Debian main.

---

### 评论 #3 — dblueman (2018-03-13T05:25:33Z)

rocm-dkms builds fine against Debian 9.4's 4.9 kernel; I get full OpenCL support.

It looks like the last parts needed for upstream kernel support will be upstreamed in 4.17, so the question will be on integrating the userspace.

+1 for ROCm userspace packages in the Debian repos.

---

### 评论 #4 — valeriob01 (2018-11-18T15:46:22Z)

Some issues for Debianization:
1. gpu detection for the installer, to know when to install ROCm
2. requires the package firmware-amd-graphics from the non-free repository


---

### 评论 #5 — mmuehlenhoff (2019-02-12T12:48:10Z)

The http://repo.radeon.com/rocm/apt/debian/ repository currently only ships the debs, could you also publish the Debian source packages to allow custom builds?

---

### 评论 #6 — ROCmSupport (2020-11-18T11:29:19Z)

Thanks @picca 
As its very old issue, and no updates for the last 2 years, this issue is going to be closed.
Request to open a new ticket, if you found any.
Thank you.

---
