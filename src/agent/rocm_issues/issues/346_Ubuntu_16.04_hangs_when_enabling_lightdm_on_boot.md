# Ubuntu 16.04 hangs when enabling lightdm on boot

> **Issue #346**
> **状态**: closed
> **创建时间**: 2018-02-24T22:01:03Z
> **更新时间**: 2018-06-03T14:39:57Z
> **关闭时间**: 2018-06-03T14:39:57Z
> **作者**: xiamaz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/346

## 描述

I have just installed rocm on 16.04 LTS using Linux 4.13.0-32.

Unfortunately the boot hangs when starting the system normally showing only a blue or green screen without disk activity or the possibility to login via ssh.

When lightdm is disabled on boot the system starts correctly. Starting lightdm later is possible and all opencl and opengl features are enabled correctly.

Is this a known bug?

---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-02-27T14:25:00Z)

I am checking into this, will get back to you 

---

### 评论 #2 — gstoner (2018-03-02T23:00:24Z)

@xiamaz Can you try this beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2

---
