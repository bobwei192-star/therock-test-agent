# Frameworks supported on AMD Tonga FirePro S7100X?

> **Issue #720**
> **状态**: closed
> **创建时间**: 2019-02-27T15:15:19Z
> **更新时间**: 2019-02-27T18:10:07Z
> **关闭时间**: 2019-02-27T16:03:17Z
> **作者**: smokhov
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/720

## 标签

- **Question** (颜色: #cc317c)

## 描述

I guess this is partially related to #509.

We have received HPC hardware with 5x GPUs of this model. ROCm does not seem to support it :-( The users are asking for deep learning and related frameworks that could take advantage of such GPUs in our servers... so my question here really is what is supported -- any list of libraries, frameworks, tools, that work right off the bat on these GPUs, or we have to write our own wrappers/shaders/OpenCL code first?

Thanks!

---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2019-02-27T16:03:17Z)

ROCm is neither supported nor enabled on Tonga at this time, nor are any of our ROCm libraries or ROCm-based GPU ML frameworks. Keep an eye on #509 if you would like to wait for potential experimental enablement. At this time, we have no plans for adding official support.

---

### 评论 #2 — smokhov (2019-02-27T16:07:51Z)

I guess my question is how about non-ROCm, any other set of software supports it out of the box?

---

### 评论 #3 — jlgreathouse (2019-02-27T18:02:25Z)

You are probably better off asking in other forums e.g. the [AMD community forums](https://community.amd.com/). This issue tracker is for ROCm software specifically, and I do not have enough contacts outside of this group to accurately answer that question.

---

### 评论 #4 — smokhov (2019-02-27T18:10:07Z)

Clear, thanks!

---
