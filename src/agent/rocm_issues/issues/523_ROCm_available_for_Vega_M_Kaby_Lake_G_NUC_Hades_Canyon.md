# ROCm available for Vega M / Kaby Lake G / NUC Hades Canyon?

> **Issue #523**
> **状态**: closed
> **创建时间**: 2018-09-07T21:11:54Z
> **更新时间**: 2018-10-04T06:04:39Z
> **关闭时间**: 2018-09-07T21:20:12Z
> **作者**: jmill597
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/523

## 描述

Is there support for Vega M processors (Intel i7 with combined AMD GPU)? It's not clear where that model fits in under the [supported list of CPUs](https://github.com/RadeonOpenCompute/ROCm#supported-cpus).

AMDGPU support for Vega M is [said to be available with the 4.18 kernel](https://www.phoronix.com/scan.php?page=news_item&px=Linux-4.18-DRM-Features). I can get ROCm installed under the 4.18.5 kernel on Ubuntu 18.04.1 following the [Vega 56/64 guide](https://github.com/RadeonOpenCompute/ROCm/issues/463), but calling `rocminfo` gives the dreaded return of 

> hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

System information is available [here](https://pastebin.com/raw/AuHQ6Lds) if useful.

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2018-09-07T21:20:12Z)

Hi @jmill597 

Unfortunately, at this time (ROCm 1.8.3, also for ROCm 1.9.0), the Vega M GPU is not supported in the `amdkfd` driver (which is required alongside `amdgpu`). As such, we have also not pushed support for it further up the ROCm stack.

I'll pass along a note to the team that there is interest for support of the device -- we are balancing our resources between adding support for more GPUs, adding new features and applications, and increasing stability, so we are trying to keep track of requests like this.

Thanks for your inquiry.

---
