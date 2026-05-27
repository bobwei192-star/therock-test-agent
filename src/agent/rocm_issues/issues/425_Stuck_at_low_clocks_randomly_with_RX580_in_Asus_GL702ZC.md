# Stuck at low clocks randomly with RX580 in Asus GL702ZC

> **Issue #425**
> **状态**: closed
> **创建时间**: 2018-05-25T05:23:59Z
> **更新时间**: 2019-01-05T20:05:43Z
> **关闭时间**: 2019-01-05T20:05:43Z
> **作者**: nioroso-x3
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/425

## 描述

Hi,
With ROCm 1.8 my laptop randomly loses ability to change to higher p-states, requiring shutting down the machine completely and turning it back on. Hot reboots do not work.
The amdgpu drivers in kernel ubuntu kernel 4.13 work fine.

Here is the dmesg output when trying to run a OpenCL application:
``
[ 4826.610906] amdgpu: [powerplay] Failed to notify smc display settings!
[ 5212.480671] amdgpu: [powerplay] Failed to notify smc display settings!
[ 5822.865839] amdgpu: [powerplay] Failed to notify smc display settings!
[ 6194.342332] amdgpu: [powerplay] Failed to notify smc display settings!
[ 6804.910781] amdgpu: [powerplay] Failed to notify smc display settings!
[26414.119861] amdgpu: [powerplay] Failed to start pm status log!
[26414.985049] amdgpu: [powerplay] Failed to start pm status log!
[26420.344579] amdgpu: [powerplay] Failed to start pm status log!
[26421.024833] amdgpu: [powerplay] Failed to start pm status log!
``


---

## 评论 (3 条)

### 评论 #1 — gstoner (2018-06-03T13:25:23Z)

Sent a note to the Linux team to look at this. 

---

### 评论 #2 — jlgreathouse (2019-01-04T00:09:19Z)

Hi @nioroso-x3 

Do you still see the issue in ROCm 2.0?

---

### 评论 #3 — nioroso-x3 (2019-01-05T18:28:51Z)

Nope, not anymore. I'm using amdgpu 18.40 with 18.04 now though.

---
