# if ROCm source code can be cross compiled?

> **Issue #174**
> **状态**: closed
> **创建时间**: 2017-08-01T06:14:14Z
> **更新时间**: 2017-08-02T17:30:40Z
> **关闭时间**: 2017-08-02T17:30:40Z
> **作者**: zhaojunfan
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/174

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I want to know if the rocm source code can be cross compiled?  On x86_64 platform, I want to compile arm target? 

---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-08-02T03:34:22Z)

We have he the ability for HCC to be standalone compiler which can build built as cross compiler if you put ARM code generator int the platform.

Greg
On Aug 1, 2017, at 1:14 AM, zhaojunfan <notifications@github.com<mailto:notifications@github.com>> wrote:


I want to know if the rocm source code can be cross compiled? On x86_64 platform, I want to compile arm target?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/174>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuX7yPzjyaGvdYnWAGOtjY9KAGzfIks5sTsI3gaJpZM4OpRUd>.



---
