# Where to find cxlactivitylogger?

> **Issue #849**
> **状态**: closed
> **创建时间**: 2019-07-27T16:09:04Z
> **更新时间**: 2019-08-08T19:36:49Z
> **关闭时间**: 2019-08-08T19:36:49Z
> **作者**: justdanyul
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/849

## 描述

I'm messing around with trying to get Tensorflow-rocm running on Arch Linux, I ran into quite a few wrinkles so far, all resolvable, but now, I ran into one I can't seem to resolve.

Long story short, on your official documentation refers to a package called cxlactivitylogger, which I can't use, so, I'll need to build it from source.

However, I can't find it anywhere. How can I go about building this from source?

---

## 评论 (3 条)

### 评论 #1 — acowley (2019-07-27T16:30:17Z)

I’ve been using [this recipe](https://github.com/nixos-rocm/nixos-rocm/blob/master/pkgs/development/libraries/cxlactivitylogger/default.nix) for that purpose on NixOS.

---

### 评论 #2 — justdanyul (2019-07-27T16:41:38Z)

Thanks a lot! I was looking in all the wrong places heh. I was searching for it in RadeonOpenCompute, not GPUOpen-Tools. 

---

### 评论 #3 — pramenku (2019-07-28T07:30:11Z)

If you need compiled Debian, you can get at http://repo.radeon.com/rocm/apt/debian/pool/main/c/cxlactivitylogger/

ROCm Profiler/CXLactivitylogger is an archived and old project as per https://github.com/rocmarchive/ROCm-Profiler

Same has been replaced with https://github.com/GPUOpen-Tools/RCP

https://github.com/RadeonOpenCompute/ROCm page has details of all active tools for ROCm

If your issue resolved, you can close this issue.

---
