# Which version of tensorflow is supported in ROCm 3.0 ?

> **Issue #996**
> **状态**: closed
> **创建时间**: 2020-01-08T05:23:19Z
> **更新时间**: 2020-01-08T22:31:09Z
> **关闭时间**: 2020-01-08T22:31:09Z
> **作者**: mk2016a
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/996

## 描述

When I upgrade the new ROCm, the old tensorflow 2.0 not work at all.

I think it only supports the newest tensorflow framework.

Thanks for snapshort of the disk.  I rolled back before upgrade.

---

## 评论 (2 条)

### 评论 #1 — dagamayank (2020-01-08T22:28:58Z)

@sunway513 

---

### 评论 #2 — sunway513 (2020-01-08T22:31:09Z)

Hi @mk2016a , please refer to the following doc on ROCm3.0 compatible tensorflow-rocm pypi packages:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md
In addition, you can use the following command to upgrade the tensorflow-rocm package to the latest available:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-install-basic.md#install-tensorflow-rocm-release-build

---
