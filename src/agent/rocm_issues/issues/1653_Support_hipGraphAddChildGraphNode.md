# Support hipGraphAddChildGraphNode

> **Issue #1653**
> **状态**: closed
> **创建时间**: 2022-01-01T19:07:19Z
> **更新时间**: 2024-02-01T17:28:07Z
> **关闭时间**: 2024-02-01T17:28:06Z
> **作者**: FreddieWitherden
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1653

## 描述

Currently, with the experimental HIP graph API it is not possible to embed one graph inside of another (cf cuGraphAddChildGraphNode).  The node type is listed in the relevant node type enum as hipGraphNodeTypeGraph, but there is no corresponding function.

Child graph nodes are useful if one wishes to include third party library calls in a graph, for example to rocBLAS.  Here, one can use the stream capturing functionality to obtain a graph which corresponds to the relevant third party kernels and then embed this as a child graph node.

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2022-01-28T11:53:11Z)

Thanks @FreddieWitherden for reaching out.
Let me assign this to HIP team for some update. Thank you.

---

### 评论 #2 — shadidashmiz (2024-02-01T17:28:06Z)

we do have support for hipGraphAddChildGraphNode, 
https://github.com/ROCm/HIP/blob/develop/include/hip/hip_runtime_api.h here is the header and also inside hip code the functionality is supported.

---
