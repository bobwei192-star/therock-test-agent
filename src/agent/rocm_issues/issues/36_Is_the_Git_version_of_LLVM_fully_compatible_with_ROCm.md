# Is the Git version of LLVM fully compatible with ROCm?

> **Issue #36**
> **状态**: closed
> **创建时间**: 2016-10-04T12:51:48Z
> **更新时间**: 2016-10-04T15:26:57Z
> **关闭时间**: 2016-10-04T13:06:56Z
> **作者**: almson
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/36

## 描述

Are all ROC-related changes merged into LLVM master? Is LLVM master compatible with ROCm 1.2? I have to use LLVM master due to a fixed bug. It seems to work, but I thought to ask.


---

## 评论 (2 条)

### 评论 #1 — gstoner (2016-10-04T12:54:21Z)

ROCm master is current source tree, there will be update with ROCm 1.3

greg
On Oct 4, 2016, at 7:51 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:

Are all ROC-related changes merged into LLVM master? Is LLVM master compatible with ROCm 1.2? I have to use LLVM master due to a fixed bug. It seems to work, but I thought to ask.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/36, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DudG1xBw291SqVBz9MN7tXIViwTOPks5qwkvlgaJpZM4KNo1_.


---

### 评论 #2 — ghost (2016-10-04T15:26:57Z)

Hey almson,

Our team works close together with the LLVM master repos. Everything you need to run ROCm should be available in master as we upstream our changes fairly often and run some simple validation tests against the latest public ROCm stack.

Do take into account that LLVM master is not a stable branch though, so you may encounter some unexpected issues. Our devs that work on the llvm components frequent the LLVM mailing lists. So if you do encounter an issue when running this branch that would be a good first place to send feedback.


---
