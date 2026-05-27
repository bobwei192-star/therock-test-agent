# Please clarify OpenCL future support in ROCm

> **Issue #951**
> **状态**: closed
> **创建时间**: 2019-11-26T13:31:02Z
> **更新时间**: 2019-11-27T15:58:24Z
> **关闭时间**: 2019-11-27T08:36:26Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/951

## 描述

I see in the release notes for ROCm 2.10 that ROCm OpenCL Driver is listed as "Deprecated Feature". As an OpenCL developer, I would like some clarification about what it means:

- is there commitment to support OpenCL in ROCm in the future?
- or, am I given the choice ("forced to") choose between the language and the platform?


---

## 评论 (3 条)

### 评论 #1 — b-sumner (2019-11-26T15:50:44Z)

@preda that project is merely an old *compiler* driver which we have replaced with the new "Code Object Manager" (COMgr) which includes compilation services.  ROCm itself continues to provide an OpenCL runtime which supports the OpenCL 2.0 runtime API and either OpenCL 1.2 or 2.0 C source (depending on the device).  

---

### 评论 #2 — preda (2019-11-27T08:36:26Z)

Thank you for the clarification. I'm glad to hear OpenCL will continue to be supported in ROCm.

---

### 评论 #3 — b-sumner (2019-11-27T15:58:24Z)

You're welcome.  You're not the only one who raised concerns.  I expect the release notes will be improved.

---
