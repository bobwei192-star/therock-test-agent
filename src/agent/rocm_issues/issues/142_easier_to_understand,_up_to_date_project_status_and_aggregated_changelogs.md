# easier to understand, up to date project status and aggregated changelogs

> **Issue #142**
> **状态**: closed
> **创建时间**: 2017-07-01T08:03:20Z
> **更新时间**: 2017-07-01T21:52:00Z
> **关闭时间**: 2017-07-01T17:27:39Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/142

## 描述

I don't know how you all keep track of it internally, and as much as I'd like to poke @johnbridgman on phoronix forums - the project is in dire need of an update of birds eye view of features and a changelog telling us users/developers what's going on.  It's still really difficult to track ROCm and I put in a reasonable effort, many would put in less...

I can't put it together via commits - not across that many modules/repositories.

This would also have the advantage of better news coverage, such as via phoronix - and whatever other news sites when killer enough features become available.

---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-07-01T12:41:31Z)

We work with the team to start putting out change log,  the area needs it most in the base driver,  Since tools do this today.  One thing we are working on right now big update to documentation and we make this part of the this role out.

Understand this is much bigger project then just base driver,   It really three major efforts

ROCm Software Platform - Application, Frameworks, and Libraries ( Math MIOpen and C++ Template, etc)
ROCm Software Tools ( OpenCL, HIP, HCC, LLVM  and lot more being done by other group internal and external)
ROCm Headless Server  base driver which at the core is. AMDGPU  Driver + KFD + Thunk+ ROCr Runtime API

1.6 Based driver is based on 1.5 driver,  with Formal support Radeon Vega  Frontier addition + Radeon Instinct MI25, MI8 and MI6

All our software internally is tracked in our develop systems    I talk with the core linux team to publish it change log as well

Thank you for your feedback



On Jul 1, 2017, at 3:03 AM, Jason Newton <notifications@github.com<mailto:notifications@github.com>> wrote:


I don't know how you all keep track of it internally, and as much as I'd like to poke @johnbridgman<https://github.com/johnbridgman> on phoronix forums but the project is in dire need of an update of birds eye view of features and a changelog telling us users/developers what's going on. It's still really difficult to track ROCm and I put in a reasonable effort, many would put in less...

I can't put it together via commits - not across that many modules/repositories.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/142>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duft0_CGN-8vrrIitRHxfx9NQ_VcKks5sJf1JgaJpZM4OLQEU>.



---

### 评论 #2 — gstoner (2017-07-01T21:52:00Z)

ROCm 1.6 What New?
Brings Radeon Instinct Family MI25, MI8, MI6 and Radeon Vega Frontier Edition hardware support.
OpenCL 2.0 compatible kernel language support with OpenCL 1.2 compatible runtime
OpenCL compiler also has assembler and disassembler support, inline assembly support.
Big improvements in the base Native LLVM code generator with new large number of optimization.
HCC Compiler Upgrade with New Gid Dispatch foundation
HIP new APIs: hipMemcpy2DAsync, hipMallocPitch, hipHostMallocCoherent, hipHostMallocNonCoherent
New Low Level Performance Library Interface
ARM AArch64 and IBM Power 8 support in the core driver
MIOpen 1.0 Deep Learning Solver
Debian and Yum Package for Math Libraries ( rocBLAS, rocFFT, hcFFT, hcRNG, hcBLAS, hibBLAS)
ROCm-SMI update to check current Power Utilization of GPU
Radeon Compute Profiler Formally called the ROCm Profiler
New Package Server repo.radeon.com to give you better download performance

---
