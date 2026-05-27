# Rocm kernel etherten not working on ASUS am1m-a mobo

> **Issue #193**
> **状态**: closed
> **创建时间**: 2017-09-02T04:47:06Z
> **更新时间**: 2017-09-07T01:58:37Z
> **关闭时间**: 2017-09-02T11:54:47Z
> **作者**: kusayuzayushko
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/193

## 描述

For some reason, with default Ubuntu kernel it's ok, but when i boot with 4.11.0-kfd-compute-rocm kernel, lan not working.
This is 2 kernels diff http://paste.ubuntu.com/25449195/
Any ideas how i can fix it?

---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-09-02T11:54:47Z)

THis APU processor is not supported by the base Linux Driver used by the ROCm software stack.   it not fixable since it is missing core HW capabilities needed.   

---

### 评论 #2 — kusayuzayushko (2017-09-07T01:58:37Z)

Could you please give an advice what can i do to make ROCm work with my mobo? I'm not familiar with Linux kernel stuff, but i really want to try... something. Maybe it is possible to find one of Ubuntu patches (because on Ubuntu lan is working ok) or build ROCm with default Ubuntu kernel?
Thank you.

---
