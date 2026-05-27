# Indigo Bench doesn't seem to work with ROCm 1.8.0beta on Vega FE

> **Issue #408**
> **状态**: closed
> **创建时间**: 2018-05-09T06:18:42Z
> **更新时间**: 2021-01-05T10:21:53Z
> **关闭时间**: 2021-01-05T10:21:53Z
> **作者**: boberfly
> **标签**: Compiler Performance Issue
> **URL**: https://github.com/ROCm/ROCm/issues/408

## 标签

- **Compiler Performance Issue** (颜色: #8ff442)

## 描述

Hi all,

I did a test of this with ROCm 1.8.0beta
```
https://www.indigorenderer.com/indigobench
```
Seems to stall and not progress after building OpenCL code. My specs are the same as my other posts:
```
Ubuntu 18.04
Kernel 4.13
ROCm 1.8.0beta
AMD Vega 10 XTX Frontier Edition
```
Printed in the terminal:
```
OpenCL code for 'blend(phong,diffuse)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.04700 s)
OpenCL code for 'diffuse' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.04998 s)
OpenCL code for 'phong' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.03738 s)
OpenCL code for 'blend(diffuse,diffuse_transmitter)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.03057 s)
OpenCL code for 'blend(oren_nayar,diffuse_transmitter)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.009486 s)
OpenCL code for 'blend(phong,diffuse_transmitter)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.01825 s)
OpenCL code for 'blend(diffuse,null)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.02253 s)
OpenCL code for 'specular' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.01029 s)
OpenCL code built: (elapsed: 0.05369 s)
Optimised OpenCL code for 'blend(phong,diffuse)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.005047 s)
Optimised OpenCL code for 'diffuse' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.02840 s)
Optimised OpenCL code for 'phong' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.02449 s)
Optimised OpenCL code for 'blend(diffuse,diffuse_transmitter)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.02021 s)
Optimised OpenCL code for 'blend(oren_nayar,diffuse_transmitter)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.01636 s)
Optimised OpenCL code for 'blend(phong,diffuse_transmitter)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.006637 s)
Optimised OpenCL code for 'blend(diffuse,null)' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.01176 s)
Optimised OpenCL code for 'specular' on Vega 10 XTX [Radeon Vega Frontier Edition] built. (from cache, elapsed: 0.007623 s)
```
Just to confirm, is this an ok place to put down bug reports/tests for these kind of things?

Cheers

---

## 评论 (3 条)

### 评论 #1 — gstoner (2018-05-12T04:24:31Z)

The team is looking at it. 

greg

---

### 评论 #2 — searlmc1 (2018-12-28T20:40:44Z)

This has been fixed internally; will update once the fix is available.

---

### 评论 #3 — ROCmSupport (2021-01-05T10:21:53Z)

Hi @boberfly 
The issue was fixed and closed in ROCm 3.x.
Recommend to try with the latest ROCm 4.0.
File a new issue if you find any issue so that we will track the issue with more speed.
Thank you.

---
