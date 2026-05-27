# GDS access

> **Issue #308**
> **状态**: closed
> **创建时间**: 2018-01-23T06:41:43Z
> **更新时间**: 2020-11-18T11:35:34Z
> **关闭时间**: 2020-11-18T11:35:34Z
> **作者**: preda
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/308

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

This is a feature request:

Please provide/document a way to use GDS, and a sample.


---

## 评论 (6 条)

### 评论 #1 — gstoner (2018-01-24T01:05:10Z)

This is something we have been looking in too.  It is still just preliminary research

---

### 评论 #2 — ob7 (2018-02-21T13:26:53Z)

What is GDS?

---

### 评论 #3 — preda (2018-02-21T19:54:39Z)

Global Data Share. It is similar to LDS (Local Data Share), but global i.e. shared between all the workgroups. Could be a very fast solution for some particular situations, but it is not exposed by the API (such as OpenCL).
See
https://developer.amd.com/wp-content/resources/Vega_Shader_ISA_28July2017.pdf

---

### 评论 #4 — preda (2019-01-04T00:08:59Z)

Any update on exposing GDS?


---

### 评论 #5 — jlgreathouse (2019-01-04T00:20:50Z)

We're still internally exploring the best way to expose this feature through our languages and runtimes. I have a helper library built that I use internally to access this hardware mechanism, and I'm going to try to see if I can release that through the Experimental ROC repo. However, I'll note that my experimental mechanisms are extremely not-product-ready. For instance, the GDS space is not currently virtualized, so every process using a GPU on the entire system would be able to see (and modify!) what's written. Very not-safe for general use.

Stuff like virtualizing the GDS, handling "what happens when multiple processes all want the GDS?", making GDS space part of task switch space, and sharing GDS between compute and graphics are just part of what we're working through as we think about this feature.

---

### 评论 #6 — ROCmSupport (2020-11-18T11:30:27Z)

Thanks @preda 
As its very old issue, and no updates for the last 2 years, this issue is going to be closed.
Request to open a new ticket, if you found any.
Thank you.

---
