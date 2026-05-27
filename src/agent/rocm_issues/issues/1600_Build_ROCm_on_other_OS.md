# Build ROCm on other OS

> **Issue #1600**
> **状态**: closed
> **创建时间**: 2021-10-27T15:27:15Z
> **更新时间**: 2025-05-09T08:05:48Z
> **关闭时间**: 2021-11-03T10:12:26Z
> **作者**: mariolpantunes
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1600

## 描述

Is there any way to compile and install the ROCm library on another OS?
I use Slackware, and there is no support for this OS.

---

## 评论 (3 条)

### 评论 #1 — xuhuisheng (2021-11-02T11:25:54Z)

How about install docker on other OS. Then run an ubuntu:20.04 image on docker, we could install rocm-dev and rocm-libs in docker.
And rock-dkms should be included in upstream linux kernel, I guess.

---

### 评论 #2 — ROCmSupport (2021-11-03T10:12:26Z)

Hi @mariolpantunes 
Thanks for reaching out.
ROCm supports the mentioned OSes @ [https://github.com/RadeonOpenCompute/ROCm#supported-operating-environments](url)
All other OSes are not officially supported.
Thank you.

---

### 评论 #3 — dchmelik (2025-05-09T07:55:42Z)

Oh, come on!  If one can package.deb & .rpm, then oldest GNU/Linux package type. txz--for Slackware (and about as large OS family)--is even easier than those.  Recent years you can can compile ROCm using Slackware's largest/quasi-official build script repository: [Linux Questions: (official) Slackware forum: AMD ROCm support ](http://www.linuxquestions.org/questions/slackware-14/amd-rocm-support-4175733461/).

---
