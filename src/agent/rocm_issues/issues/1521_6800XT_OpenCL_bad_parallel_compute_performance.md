# 6800XT OpenCL bad parallel compute performance

> **Issue #1521**
> **状态**: closed
> **创建时间**: 2021-07-13T19:52:41Z
> **更新时间**: 2021-07-14T04:07:40Z
> **关闭时间**: 2021-07-14T04:07:40Z
> **作者**: aoolmay
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1521

## 描述

I'm transitioning my workloads from old and failing 803gfx WX cards to new 1030gfx cards. I have a test setup with a 6800XT where i encounter an issue where first two workloads i dispatch are treated with somewhat equal priority and are executed quite fast, but every consecutive program that uses OpenCL seems to be disproportionately disadvantaged and executes at what seems like 1:3 rate, until the first workloads finish and next ones can be "promoted".

The 803gfx WX cards behaved differently, no matter how overburdened they divided compute time equally. Typically i was running 10-15 workloads in parallel. Even though the new card has more compute ability the limitation reduces it to nearly sequential ( 2x, but still not parallel 15x ) execution.

Does anything immediately comes to mind? Maybe there's some configuration specific to gaming performance that could be responsible for such behaviour? I noticed in the kernel module available options as shed_jobs, shed_policy, shed_hw_submissions, compute_multipipe but i'd love to avoid diving into a rabbit hole if you can direct me to best possible solution.

Btw, ROCm + 1030gfx, very much welcome, any time, please. ;]

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-07-14T04:07:40Z)

Hi @aoolmay 
Thanks for reaching out.
Navi is not supported with ROCm. Until then, I can not comment on this issue.
Please stay tuned for some time so that the support will be enabled.
Thank you.

---
