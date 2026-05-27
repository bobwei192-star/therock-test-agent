# AMD Radeon RX 6800 - HIPRTC_ERROR_COMPILATION

> **Issue #1889**
> **状态**: closed
> **创建时间**: 2023-01-12T14:32:46Z
> **更新时间**: 2024-03-02T03:42:39Z
> **关闭时间**: 2024-03-02T03:42:39Z
> **作者**: mikaba-eu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1889

## 描述

Hello,

I try to run a pytorch project with my RX 6800 (clinfo: gfx_1030)
/sys/module/amdgpu/version: 5.18.2.22.40

I installed ROCm 5.3 and pytorch Preview (Nightly).

But then I start the project I get after some time that errors and warnings:

```
MIOpen(HIP): Warning [SQLiteBase] Missing system database file: gfx1030_30.kdb Performance may degrade. Please follow instructions to install: https://github.com/ROCmSoftwarePlatform/MIOpen#installing-miopen-kernels-package
MIOpen(HIP): Error [Compile] 'hiprtcCompileProgram(prog.get(), c_options.size(), c_options.data())' naive_conv.cpp: HIPRTC_ERROR_COMPILATION (6)
MIOpen(HIP): Error [BuildHip] HIPRTC status = HIPRTC_ERROR_COMPILATION (6), source file: naive_conv.cpp
MIOpen(HIP): Warning [BuildHip] /tmp/comgr-112729/input/CompileSource:39:10: fatal error: 'limits' file not found
#include <limits> // std::numeric_limits
         ^~~~~~~~
1 error generated when compiling for gfx1030.
terminate called after throwing an instance of 'miopen::Exception'
  what():  /MIOpen/src/hipoc/hipoc_program.cpp:299: Code object build failed. Source: naive_conv.cpp
Aborted (core dumped)
```

---

## 评论 (7 条)

### 评论 #1 — tlaguz (2023-01-13T22:40:55Z)

I had this exact issue on Ubuntu 22.04 with TensorFlow. It seems ROCm libraries are compiled using clang which on Ubuntu 22.04 is missing default libraries. Installing `libstdc++-12-dev` package solved the issue.

---

### 评论 #2 — theepicflyer (2023-03-17T02:49:55Z)

Can confirm this is an issue with PyTorch on 22.04 on my 6900XT too. Installed `libstdc++-12-dev` as per @tlaguz and it works great.

---

### 评论 #3 — ExposedCat (2023-09-22T22:16:32Z)

Not sure if all of these is required, but on Fedora 38 with RX 6800 XT I also installed `make automake gcc gcc-c++ kernel-devel rocminfo` (and `libstdc++-devel` as mentioned before) to make it work

---

### 评论 #4 — lancediarmuid (2023-12-12T06:39:28Z)

Oh thanks!~ I got the same problem on my RX6600XT. It works when I installed `libstdc++-12-dev`.

---

### 评论 #5 — nartmada (2024-02-24T05:36:53Z)

Thanks everyone for your input.  @dakiba, please close the ticket if the issue has been resolved.  Thanks.

---

### 评论 #6 — 14790897 (2024-02-26T08:19:23Z)

thanks

---

### 评论 #7 — nartmada (2024-03-02T03:42:39Z)

Closing the ticket as reported issue has been resolved.  Thanks.

---
