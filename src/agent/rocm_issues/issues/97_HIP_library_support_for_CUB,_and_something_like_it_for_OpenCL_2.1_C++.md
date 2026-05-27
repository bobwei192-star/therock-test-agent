# HIP library support for CUB, and something like it for OpenCL 2.1 C++

> **Issue #97**
> **状态**: closed
> **创建时间**: 2017-03-21T02:17:39Z
> **更新时间**: 2017-07-02T01:47:42Z
> **关闭时间**: 2017-07-02T01:47:42Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/97

## 描述

Hey folks,  please let me know if there's a better place for this issue/feature request in the future.

It's great to see the cuda compatability coming out of HIP/HCC - I thought I'd let you know of one other high profile library that I hope you can compatabilize - it's a fantastic library: [CUB](https://nvlabs.github.io/cub/) - or CUDA unbound.  The library basically lets you combine a bunch of variants of a bunch of the most common algorithms you run at either warp, block, or device level sized problems - the last 2 being the most useful in my experience. It can save you a ton of time solving the problem of rewriting things like parallel prefix sums or sorts 10 times for every program.

We need it (by we, I mean ROCm HIP/OCL community) to increase our development power both for both platforms.    I hope you guys have the staff hours to help get it up and going because with libraries like this and the performance requirements, its usually left best as an effort by the vendor for tuning (see rocBLAS vs cuBLAS).  It will further increase adoption of both OCL, HIP and ROCm and greatly improve productivity.  Particularly for OpenCL C++ - I had a ton of macros to hobble by getting something like CUB in OpenCL - performant algorithm blocks for the device side and this always stood out as _the_ solution.  I am aware OCL has workgroup functions, so that does help with some of the cases you'd use a CUB like library - but you can still do more with CUB than what work-group functions provide.

While we're at it, I hope you guys can make a thrust compatible library for HIP as well as an updating of Bolt for OpenCL.  Thrust comes out of the box with any CUDA SDK since 6.5 or 7 IIRC and I know a number of people lean on it.  I do not personally use these libraries much and I prefer a CUB port first, but I do acknowledge it has a following and you'd be making even more people happy.
