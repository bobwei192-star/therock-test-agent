# Request for a higher level script to compile all ROCm components on a new platform

> **Issue #1195**
> **状态**: closed
> **创建时间**: 2020-08-21T03:51:56Z
> **更新时间**: 2020-12-16T11:00:54Z
> **关闭时间**: 2020-12-16T11:00:54Z
> **作者**: sameershende
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1195

## 描述

It would help to have a script that configures, builds, and installs all the components from source code in a  given target directory with an architecture. I am compiling ROCm on ppc64le (Ubuntu 20.04) and I see several places where architecture specific parameters are hard-coded. For e.g., a Linux kernel version 3.6.0 is assumed instead of querying uname to retrieve the current value. This is set in ROCK-Kernel-Driver/include/config/kernel.release and  in ROCK-Kernel-Driver/include/config/auto.conf.cmd. The platform is assumed as amd64 in rocm_bandwidth_test/hsatimer.hpp where #include <x86intrin.h> and __rtdscp are used, rocminfo hard-codes NBIT and NBITSTR based on checks for x86_64 only. In rocm-smi, DEBIAN/control also hardcodes Architecture: amd64 in DEBIAN/control. These issues and the complex dependency graph of some of the other packages such as rocprofiler, make it difficult to build the entire tree from the source code. If a higher-level script can be developed, it would help port us ROCm to other platforms (e.g., ppc64le with Ubuntu 20.04). 

---

## 评论 (4 条)

### 评论 #1 — xuhuisheng (2020-08-21T04:01:22Z)

I found some shells in this project. https://github.com/RadeonOpenCompute/Experimental_ROC , but not support rocm-2.0

---

### 评论 #2 — baryluk (2020-11-23T22:54:04Z)

This is mostly a duplicate of https://github.com/RadeonOpenCompute/ROCm/issues/1188

The script will not help you with porting. You need to go over all the related project you find bugs in, and submit patches / pull requests for it.

I can't even compile ROCm easily on x86_64 / amd64 at the moment.

---

### 评论 #3 — ROCmSupport (2020-11-24T07:19:04Z)

Hi @sameershende 
Thanks for reaching out.
We are working on this, but it will take some time to gather all the information for building and validating.
Once validated, we will update the docs accordingly.
Please stay tuned.
Thank you.

---

### 评论 #4 — ROCmSupport (2020-12-16T11:00:54Z)

Duplicate of #1188. All progress can be seen there.
Thank you.

---
