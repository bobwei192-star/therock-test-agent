# Why does AMD break everything with each new release ?

> **Issue #1330**
> **状态**: closed
> **创建时间**: 2020-12-11T18:50:56Z
> **更新时间**: 2021-06-06T16:35:12Z
> **关闭时间**: 2020-12-14T07:25:21Z
> **作者**: Dan-RAI
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1330

## 描述

Today, after a system update, rocm was totally broken again. 

hipcc --version
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang": No such file or directory at /opt/rocm/bin/hipcc line 203.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm/bin/hipcc line 204.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm/bin/hipcc line 208.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm/bin/hipcc line 846.
HIP version: 3.10.20465-f9876b8d
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang": No such file or directory at /opt/rocm/bin/hipcc line 895.


Looked at github:

"Upgrade to AMD ROCm v3.10 Not Supported
An upgrade from previous releases to AMD ROCm v3.10 is not supported. A fresh and clean installation of AMD ROCm v3.10 is recommended."

Sorry for the rant, but do you really think we have time to remove all AMD traces and reinstall on each update ? 

---

## 评论 (3 条)

### 评论 #1 — iHandle (2020-12-13T05:55:07Z)

Everytime I need a fresh and clean installation, I use timeshift to rollback to a snapshot without ROCm☹

---

### 评论 #2 — ROCmSupport (2020-12-14T05:48:16Z)

Hi @Dan-RAI 
Thanks for reaching out.
Currently ROCm packaging and installation is going through many changes and so upgrade might not work well.
Recently, ROCm is broken on specific kernels and so quick fix has been pushed into ROCm 3.10.
Based on these points, we are recommending to do an upgrade for now.

There is another way also to proceed with ROCm installation without upgrade, concept of "Multi ROCm install".
You can install more than 2 versions of ROCm in the same machine.
For ex: for installing ROCm 3.9 --> sudo apt install rock-dkms rock-dkms-firmware rocm-dev3.9.0
for installing ROCm 3.10 --> sudo apt install rock-dkms rock-dkms-firmware rocm-dev3.10.0
Like wise you can install many versions of ROCm.
Please note that you can not mix with single ROCm and Multi ROCm, which creates mess.
Hope it clarifies.

---

### 评论 #3 — ROCmSupport (2020-12-14T07:35:35Z)

Hi @Dan-RAI 
rocm-dkms = kernel packagaes(rock-dkms + rock-dkms-firmware) + user-mode components(rocm-dev)
rocm-dkms is the combination of kernel space and user space.

---
