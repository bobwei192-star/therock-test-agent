# Bad symlink to lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a

> **Issue #476**
> **状态**: closed
> **创建时间**: 2018-07-27T22:51:29Z
> **更新时间**: 2018-08-02T20:01:33Z
> **关闭时间**: 2018-08-02T20:01:33Z
> **作者**: BryantLam
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/476

## 描述

ROCm 1.8.2

There's a bad symlink on lib/libclang_rt.builtins-* that incorrectly expands `CMAKE_SYSTEM_PROCESSOR` using `@x@` instead of `${x}`.

---

## 评论 (3 条)

### 评论 #1 — b-sumner (2018-08-01T14:59:43Z)

Hi @BryantLam , could you clarify where you are seeing this and on which release?  Do you have a patch or pull request?

---

### 评论 #2 — BryantLam (2018-08-01T15:41:06Z)

Sorry. I should have been a bit more clear. This issue affects the ROCm 1.8.2 [RPM packages for CentOS](http://repo.radeon.com/rocm/yum/rpm/).

Specifically, if you go to this path:  `/opt/rocm/lib`, there's a broken symlink
from literal `/opt/rocm/hcc/lib/libclang_rt.bulitins-@CMAKE_SYSTEM_PROCESSOR@.a`
to `libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a` (the actual characters).

I assume (but have not confirmed) `@CMAKE_SYSTEM_PROCESSOR@` was supposed to be expanded with `${CMAKE_SYSTEM_PROCESSOR}`, but I haven't dived into looking where in the ROCm code (no patch/PR from me yet).

---

### 评论 #3 — scchan (2018-08-02T20:01:33Z)

It will be addressed by this: https://github.com/RadeonOpenCompute/hcc/pull/825

---
