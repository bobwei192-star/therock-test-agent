# Vulkan driver in ROCm

> **Issue #706**
> **状态**: closed
> **创建时间**: 2019-02-14T13:10:51Z
> **更新时间**: 2023-12-12T22:48:24Z
> **关闭时间**: 2023-12-12T22:48:24Z
> **作者**: aryamazaheri
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/706

## 描述

Does ROCm include Vulkan driver? I cannot find anywhere that ROCm supports Vulkan. Should I install AMDGPU-Pro driver instead?

---

## 评论 (3 条)

### 评论 #1 — ms178 (2019-02-20T20:19:50Z)

ROCm is AMD's compute stack. If you want Vulkan support, you have two options. 1) the Mesa community RADV driver or 2) AMD's AMDVLK driver (which should be also part of their AMDGPU-PRO driver).

---

### 评论 #2 — preda (2023-09-25T10:07:01Z)

On ubuntu this may help:
```
sudo apt install mesa-vulkan-drivers
```

---

### 评论 #3 — tasso (2023-12-12T22:32:10Z)

Is this still an issue?  if not, can you please close it?

---
