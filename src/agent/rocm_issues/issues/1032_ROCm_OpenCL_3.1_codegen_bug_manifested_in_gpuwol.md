# ROCm OpenCL 3.1 codegen bug manifested in gpuwol

> **Issue #1032**
> **状态**: closed
> **创建时间**: 2020-03-01T11:59:27Z
> **更新时间**: 2023-12-18T17:35:11Z
> **关闭时间**: 2023-12-18T17:35:11Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1032

## 描述

Hi, I've been investigating gpuowl's failure to run correctly on 3.1 that was introduced by this gpuowl commit:
https://github.com/preda/gpuowl/commit/6d275b7130dbcc05d9ca1771fd8ba2522f3b6a75

[That means, the previous commit runs correctly on ROCm 3.1 while the one pointed above does not. Please note that the "breaking" commit above (and all the following) do run correctly on ROCm 2.10. So the question becomes, is this a bug in gpuowl that was not manisfesting itself in 2.10, or is this a regression in ROCm 3.1 vs. 2.10]

(for context, the breakage was brought to my attention in https://github.com/preda/gpuowl/issues/109 and https://github.com/RadeonOpenCompute/ROCm/issues/1020 )

Analyzing the breaking commit above I'm puzzled because the commit is perfectly neutral semantically. That means, the "breaking" commit does not actually change anything, it just rewords it. The equivalence of the before/after code may not be very obvious at first sight, but it becomes clearer taking into consideration that the value of the "gr" variable in that block ranges from 1 to H inclusive; luckily the change is very small thus easier to analyze.

But there's more: I did fix it by making another non-material, changes-nothing change. Please have a look at this commit which fixes the execution on 3.1, and attempt to explain *why* it fixes it:
https://github.com/preda/gpuowl/commit/390986b43a30bc72b95ad5a7b31c9ae8f91a6de2

My point is: making insignificant changes to the code, that should not change anything at all, turns it into good-or-bad on 3.1. This I think is enough evidence for a codegen bug. Luckly it is not difficult to reproduce.

On the positive side, I do see a slight performance improvement for gpuowl on 3.1, which is nice!


---

## 评论 (4 条)

### 评论 #1 — seesturm (2020-03-08T16:23:12Z)

Had a look at the assembly output. Seems that making the "non-material" change prevents the code 
```CL
for (i32 i = 0; i < NW; ++i) {
   carry[i] = carryShuttlePtr[(gr - 1) * WIDTH + me * NW + i];
}
```
being re-ordered before the "acquire" work_group_barrier by the compiler. If reordered, "carryShuttlePtr" data is read before `ready[gr-1]==1`. Looks to me like a bug in the CL compiler.

Interesting that you use "ready" for spin lock in your code. Guess that such a pattern is not used very often.

---

### 评论 #2 — ROCmSupport (2021-04-19T12:48:16Z)

Thanks @preda for reaching out.
Can you please check on ROCm 4.1 and share an update asap.
Thank you.

---

### 评论 #3 — nartmada (2023-12-14T03:37:56Z)

Hi @preda, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.




---

### 评论 #4 — nartmada (2023-12-18T17:35:11Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
