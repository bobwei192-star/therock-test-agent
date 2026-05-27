# HCC RUNTIME ERROR in hipCaffe

> **Issue #354**
> **状态**: closed
> **创建时间**: 2018-03-07T09:11:46Z
> **更新时间**: 2018-03-08T01:50:08Z
> **关闭时间**: 2018-03-08T01:50:08Z
> **作者**: haozhangcn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/354

## 描述

Issue summary

./build/test/test_all.testbin

Backtrace:
0x00007f04870cd32e:	Kalmar::CLAMP::DetermineAndGetProgram(Kalmar::KalmarQueue*, unsigned long*, void**) + 0x59e
0x00007f04870cd690:	Kalmar::KalmarBootstrap::KalmarBootstrap() + 0x120
0x00007f04870cd549:	__hcc_shared_library_init + 0x29
0x00007f048a2766ba:	_dl_rtld_di_serinfo + 0x706a
0x00007f048a2767cb:	_dl_rtld_di_serinfo + 0x717b
0x00007f048a266c6a:	+ 0x717b

HCC RUNTIME ERROR: Fail to find compatible kernel at file:mcwamp.cpp line:346


Operating system: Ubuntu 16.04


---

## 评论 (3 条)

### 评论 #1 — gstoner (2018-03-07T13:02:13Z)

@MAXHAOZHANG  This information is not enough for us to understand what is going wrong,  
When you report an issue we need the version of the driver your running which version of HCC.  

---

### 评论 #2 — parallelo (2018-03-07T16:46:27Z)

Duplicate issue:  https://github.com/ROCmSoftwarePlatform/hipCaffe/issues/39

---

### 评论 #3 — haozhangcn (2018-03-08T01:50:08Z)

The GPU in my server does not support ROCm -v1.7 -- From AMD
AMD Firepro W9100

Thank you!

---
