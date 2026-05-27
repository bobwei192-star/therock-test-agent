# Darktable opencl stops working with rocm 4.3.0 on supported GPUs

> **Issue #1557**
> **状态**: closed
> **创建时间**: 2021-08-18T09:30:34Z
> **更新时间**: 2021-09-06T10:19:01Z
> **关闭时间**: 2021-08-30T17:54:18Z
> **作者**: minfaer
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1557

## 描述

Hi,
I am opening this issue because #1553 got closed. I am experiencing the exact same thing on Vega/gfx900 which is on the official support list. This happens in CentOS 7 (and Fedora 34) just like #1553 reported for Ubuntu 20.04 LTS. ROCm 4.2 worked fine.

[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/7006122/clinfo.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/7006123/rocminfo.txt)
[dt-cltest.txt](https://github.com/RadeonOpenCompute/ROCm/files/7006124/dt-cltest.txt)


---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-08-18T10:35:53Z)

Thanks @minfaer for reaching out.
Can you please share the exact steps to reproduce the problem?
Thank you.

---

### 评论 #2 — minfaer (2021-08-18T12:51:48Z)

Sure

0. Uninstall all ROCm 4.2 packages if installed before
1. install rocm-dev (to have a complete install) from the ROCm 4.3 repository
2. run `darktable-cltest`

---

### 评论 #3 — minfaer (2021-08-30T17:54:18Z)

This was fixed in ROCm 4.3.1 for me. I will thus close this issue. Thank You for looking into this!

---

### 评论 #4 — ROCmSupport (2021-09-06T10:19:01Z)

Thanks @minfaer for confirming that issue is fixed with 4.3.1 and closed it.
Thank you.

---
