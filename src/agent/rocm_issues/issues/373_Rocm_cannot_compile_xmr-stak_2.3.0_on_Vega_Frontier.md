# Rocm cannot compile xmr-stak 2.3.0 on Vega Frontier

> **Issue #373**
> **状态**: closed
> **创建时间**: 2018-03-26T01:28:50Z
> **更新时间**: 2018-03-26T15:37:13Z
> **关闭时间**: 2018-03-26T15:37:12Z
> **作者**: dfad44
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/373

## 描述

In preparation for POW change, i tried the newly released xmr-stak 2.3.0 and get the following error. 

-------------------------------------------------------------------
xmr-stak 2.3.0 a036cd8

Brought to you by fireice_uk and psychocrypt under GPLv3.
Based on CPU mining code by wolf9466 (heavily optimized by fireice_uk).
Based on OpenCL mining code by wolf9466.

Configurable dev donation level is set to 2.0%

You can use following keys to display reports:
'h' - hashrate
'r' - results
'c' - connection
-------------------------------------------------------------------
[2018-03-25 20:13:36] : Mining coin: monero
[2018-03-25 20:13:36] : Compiling code and initializing GPUs. This will take a w                                               hile...
[2018-03-25 20:13:36] : Device 0 work size 8 / 32.
[2018-03-25 20:13:37] : OpenCL device 0 - Precompiled code /home/xxx/.openclcach                                               e/dbb76e4a654cad114d7de496f11795ef645d53a661526a91abd792b656235acf.openclbin not                                                found. Compiling ...
[2018-03-25 20:13:37] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgr                                               am.
Build log:
Error: Failed to compile opencl source (from CL to LLVM IR).

Previous version works.

Might be a compilier issue, any help will be appreciated.

Thank you!

---

## 评论 (4 条)

### 评论 #1 — todxx (2018-03-26T05:34:21Z)

I'm running on rocm 1.7.1 and xmr-stak's kernels compiled for Vega and Polaris just fine.
I built from the 2.3.0 tag from the xmr-stak git repo.

What GPU are you using and which branch are you building from?

---

### 评论 #2 — dfad44 (2018-03-26T11:09:31Z)

I use Vega Frontier Edition GPUs. 
Tried both the dev and master branch for xmr-stak 2.3.0 and could not get it to compile. 
Using rocm 1.7.1 also.
It does mine with CPU just fine.

---

### 评论 #3 — gstoner (2018-03-26T14:55:51Z)

I ask SQE to look at XMR again, but i had asked performance engineer that just joined the team to look for areas to drive more performance 

---

### 评论 #4 — dfad44 (2018-03-26T15:37:12Z)

After close review, I discovered a user error at the currency prompt. The right choice is **monero7** not monero. I've since been able to compile and mine. Although sumokoin does give the same error, it can be mined with the monero7 option.

@gstoner That will be wonderful. Any performance boosts will be welcomed. Keep up the good work!
@todxx Thanks for your response.

Closing this issue.

---
