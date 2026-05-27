# Differences ROCm packages

> **Issue #224**
> **状态**: closed
> **创建时间**: 2017-10-13T13:19:07Z
> **更新时间**: 2017-10-13T13:23:15Z
> **关闭时间**: 2017-10-13T13:23:15Z
> **作者**: javierox
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/224

## 描述

What are the differences between the ROCm package in the AMDGPU-PRO Driver Version 17.30 for Ubuntu 16.04.3 and this repository?.Because I successfully compiled manually and run many samples for rocm without installing any custom kernel, only module. There are some information not updated for ROCm and AMD-GPU PRO?
I do not want to offend anyone, sorry
Is really necessary all this package so complex and immersive? Is not a simple kernel module enough?
 Sorry again for my English.

---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-10-13T13:23:15Z)

AMDGPU-Pro has subset of functionality for ROCm in this repo, what you do not understand DKMS package has all the bit on github   There is KFD, Thunk and ROCr runtime API which all the language runtime run on,  and also there are number of firmware enhancement over stock AMDGPU driver 

---
