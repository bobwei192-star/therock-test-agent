# Building on amd-staging

> **Issue #424**
> **状态**: closed
> **创建时间**: 2018-05-24T16:16:22Z
> **更新时间**: 2018-12-21T11:14:23Z
> **关闭时间**: 2018-12-21T02:08:47Z
> **作者**: Cyclic3
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/424

## 描述

Has anyone managed to get rocm to build on amd staging?

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-12-21T02:08:47Z)

Hi @Cyclic3 

Sorry for the long delay in getting to this. Yes, ROCm should now work with the most up-to-date upstream `amddgpu` and `amdkfd` drivers. If you're interesting in seeing how to build ROCm in this case, you may be interested in the newly released Experimental ROC project. This includes scripts and tools for rebuilding ROCm from source. This includes on distros like Ubuntu 18.10, Fedora 28, and Fedora 29, where they use the upstream kernel driver rather than the ROCK DKMS package.

https://github.com/RadeonOpenCompute/Experimental_ROC

Hopefully these scripts are relatively easy to understand. One of the ideas behind this project was to make them readable so that folks could understand the ROCm build process and extend it or modify it for their own needs.

---

### 评论 #2 — Cyclic3 (2018-12-21T11:14:23Z)

@jlgreathouse Thank you very much! At the time of posting, dkms was the only way to get it to work, and I was wondering if it could use the existing kfd kernel module. However, over the last couple of months, rocm now does this by default.

This is yet another example of why I need to go over my old issues. Sorry for any inconvenience caused!

---
