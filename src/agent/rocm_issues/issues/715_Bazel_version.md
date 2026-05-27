# Bazel version

> **Issue #715**
> **状态**: closed
> **创建时间**: 2019-02-20T01:36:52Z
> **更新时间**: 2019-03-12T11:45:09Z
> **关闭时间**: 2019-03-12T11:45:09Z
> **作者**: baerbock
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/715

## 标签

- **Question** (颜色: #cc317c)

## 描述

Is bazel 0.22.0 currently supported? Until shortly it wasn't.

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2019-02-20T03:06:47Z)

Hi @baerbock 

I'm not sure your question has enough details for me to answer it. Is bazel 0.22.0 supported for what?

---

### 评论 #2 — kentrussell (2019-03-12T11:45:09Z)

We don't build using Bazel. If you want components to build via Bazel, feel free to make the changes yourself and submit them for review. We don't use Bazel internally, and there is no pressure to move to using it, so any support for building the ROCm stack in Bazel will either be coincidental, or by users submitting patches to make it happen.

---
