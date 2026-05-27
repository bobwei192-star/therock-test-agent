# Please support Ubuntu 20.04.5 LTS with 5.14 Kernel

> **Issue #1809**
> **状态**: closed
> **创建时间**: 2022-09-20T06:51:19Z
> **更新时间**: 2023-11-27T16:36:42Z
> **关闭时间**: 2023-11-27T16:36:42Z
> **作者**: m-reuter
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1809

## 描述

Hi, I get errors when installing on Ubuntu 20.04.5 LTS with Kernel 5.14.0-1051-oem (I know it is not officially supported yet). 

`amdgpu-install --usecase=dkms`

gives

```
Package linux-modules-extra-5.14.0-1051-oem is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'linux-modules-extra-5.14.0-1051-oem' has no installation candidate
```

Older versions of amdgpu-install run further but fail during compiling with a different error.
Thanks, would be great to try our networks for medical image analysis on AMD hardware and support that for our users. If support for Ubuntu 20.04.5 is planned for the next release, do you have a time line for that? Or should I try downgrading the kernel?

---

## 评论 (2 条)

### 评论 #1 — saadrahim (2022-10-14T03:28:17Z)

I do recommend downgrading the kernel in the interim. The next minor release (ROCm 5.4) is due late this year. Fixes may be available in a point release earlier but I have no timelines to share.

---

### 评论 #2 — m-reuter (2022-10-14T06:56:05Z)

Yes, I had downgraded and that worked. 

---
