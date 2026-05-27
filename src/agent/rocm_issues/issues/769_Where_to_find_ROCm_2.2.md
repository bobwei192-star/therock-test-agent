# Where to find ROCm 2.2

> **Issue #769**
> **状态**: closed
> **创建时间**: 2019-04-15T11:45:05Z
> **更新时间**: 2019-04-15T20:39:39Z
> **关闭时间**: 2019-04-15T20:39:39Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/769

## 负责人

- amd-aakash

## 描述

Hi, I would like to install ROCm 2.2 from binary packages. Where may I find it?


---

## 评论 (2 条)

### 评论 #1 — beatboxa (2019-04-15T15:35:00Z)

See my reply here:
https://github.com/RadeonOpenCompute/ROCm/issues/768#issuecomment-483283444

You are able to follow that tree, and you will eventually come across this:

http://repo.radeon.com/rocm/

---

### 评论 #2 — preda (2019-04-15T20:39:39Z)

Thanks! adding 
deb [arch=amd64] http://repo.radeon.com/rocm/apt/2.2/ xenial main
to a file under /etc/apt/sources.list.d allows to install ROCm 2.2


---
