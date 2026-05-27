# Radeon VII is a top GPU for Mersenne prime search

> **Issue #757**
> **状态**: closed
> **创建时间**: 2019-04-08T11:36:05Z
> **更新时间**: 2019-11-26T13:34:01Z
> **关闭时间**: 2019-11-26T13:34:01Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/757

## 描述

Many times I submitted issues and requests here, but now I have some praise:

Since about 1week I acquired a Radeon VII GPU, using it for Mersenne primes search (
http://mersenne.org/ http://mersenneforum.org/ )

I must say that I'm very happy with this GPU, for these reasons:
- it is extremely fast. More than 2x faster than Vega64, on the same power use (i.e. more than double the efficiency).
- OpenCL works easily, without issues with Ubuntu 19.04, Kernel 5.0.x, and newest ROCm.
- power management including undervolting and memory overclocking through pp_od_clk_voltage works correctly and easily

Congrats to the ROCm team, keep up the good work!

---

## 评论 (1 条)

### 评论 #1 — Moading (2019-04-15T12:58:58Z)

Hi preda,

I'm happy to see ROCm OpenCL is working for you. I have been trying to get my code working on ROCm since 1.7 or so but one central piece ist still broken: OpenCL 2.0 device side enqueue

I have raised that issue multiple times here but received basically zero attention from the ROCm people. Would you be so kind to have a look at issue #540? Could you please try the test program to see if device side enqueue is working on your setup? I have tried two different mainboards and two different GPUs bt no combination works.

I would be happy if you could veryfiy the issue.

When you say you are using kernel 5.0.x, that means you are not using ROCm dkms, right? Are you using the driver included in the kernel? I have not tried kernel 5.0.x because that kernel is not on the list of supported kernels.

Greetings!

---
