# rocminfo problem?

> **Issue #249**
> **状态**: closed
> **创建时间**: 2017-11-11T11:33:09Z
> **更新时间**: 2017-11-12T08:53:16Z
> **关闭时间**: 2017-11-12T08:53:16Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/249

## 描述

Ubuntu 16.04.3, ROCm 1.6-180.
When I try the "rocminfo" from the /opt/rocm/bin/, I always get an error message:

$ /opt/rocm/bin/rocminfo 
Ill-formed call, no flag or invalid flags passed.

(but everything else seems to work fine).

---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-11-11T15:27:05Z)

This is being replaced with new version in 1.7,  with expanded fictionality.  This was tool originally to just get the id for the GPU for compiler,  it moving to proper tool to tell you info about your system and how ROCm is configured.

You can see it here.   This tool fictionality is moving into compiler tool.

https://github.com/RadeonOpenCompute/rocminfo

G

On Nov 11, 2017, at 5:33 AM, Mihai Preda <notifications@github.com> wrote:


Ubuntu 16.04.3, ROCm 1.6-180.
When I try the "rocminfo" from the /opt/rocm/bin/, I always get an error message:

$ /opt/rocm/bin/rocminfo
Ill-formed call, no flag or invalid flags passed.

(but everything else seems to work fine).

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/249>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DucpzZDwnG_By5dtJt-P3vwU7xb19ks5s1YX2gaJpZM4QadgB>.



---

### 评论 #2 — preda (2017-11-12T08:53:16Z)

OK, thanks, may I close it then?

---
