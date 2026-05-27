# hsa-ext-rocr-dev terms and conditions

> **Issue #878**
> **状态**: closed
> **创建时间**: 2019-08-27T10:33:18Z
> **更新时间**: 2024-02-09T04:46:44Z
> **关闭时间**: 2024-02-09T04:46:44Z
> **作者**: mkszuba
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/878

## 描述

Hello,

I am one of the maintainers of the ROCm OpenCL stack (with other parts of ROC hopefully to follow) on Gentoo Linux. This includes the Gentoo packaging of hsa-ext-rocr-dev, which uses the relevant .deb packages from repo.radeon.com - and which has presented us with several questions we hope you might be able to answer for us. These are:

1. Under what licence does AMD distribute the libraries contained in hsa-ext-rocr-dev? We have assumed it would be the AMDGPU-Pro EULA because AMDGPU-Pro used to include ROCm OpenCL libraries, then again it is just an educated guess;

2. What are the terms and conditions of using the repo.radeon.com package repository? The specific use cases we have got in mind here are:
 - whether it is okay for a Gentoo package manager to download hsa-ext-rocr-dev from there, rather than requiring the user to download the file manually (as it is the case for _e.g._ AMDGPU-Pro), and
 - whether it is allowed to mirror packages from that repository.

PS. On a slightly unrelated note, is there any official timeline for open-sourcing ROCm OpenCL image support yet?

---

## 评论 (2 条)

### 评论 #1 — nartmada (2024-02-02T22:30:02Z)

Hi @mkszuba, I am sorry for the lack of response from AMD.  Can you please refer to latest ROCm6.0.2 to check if your queries have been addressed?  If you still have questions, please let me know and I will forward them to the internal teams.  Thanks.

---

### 评论 #2 — nartmada (2024-02-09T04:46:44Z)

Closing the ticket as it is stale and no response from @mkszuba.  Please re-open if you still need guidance from AMD.  Thanks.

---
