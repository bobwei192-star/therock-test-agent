# Formatting for some tables looks odd

> **Issue #1955**
> **状态**: closed
> **创建时间**: 2023-03-16T14:15:40Z
> **更新时间**: 2023-03-24T14:32:24Z
> **关闭时间**: 2023-03-24T14:32:24Z
> **作者**: skyreflectedinmirrors
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1955

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- Naraenda

## 描述

![image](https://user-images.githubusercontent.com/6463881/225644616-3d6ac409-5e5a-46c6-9a7a-11f45069ea59.png)

Was discussing with @AlexVlx

Mainly this seems to result from putting the table header in a single column (so you get fixed width + wrap).  Not clear what the best solution is here, perhaps splitting it to be e.g., "Table 1" in the top row (to keep it from wrapping / looking out of place), and put a 'caption' below in some other format?



---

## 评论 (3 条)

### 评论 #1 — Naraenda (2023-03-20T12:32:23Z)

I propose using [captions with directives](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#table-with-captions) with [list tables](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#list-tables). It will be more readable in source which will make authoring and reviewing easier. I will create a PR that implements this.

---

### 评论 #2 — AlexVlx (2023-03-20T13:19:14Z)

> I propose using [captions with directives](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#table-with-captions) with [list tables](https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#list-tables). It will be more readable in source which will make authoring and reviewing easier. I will create a PR that implements this.

It's debatable if it's more readable as now you have a list that only gains special meaning due to meta-information, whereas e.g. a pipe table is unambiguously, visually, a table. .md source should still be readable. Also, GH doesn't render that since it's not part of GFM, AFAIR.

---

### 评论 #3 — Naraenda (2023-03-20T13:43:59Z)

> It's debatable if it's more readable as now you have a list that only gains special meaning due to meta-information, whereas e.g. a pipe table is unambiguously, visually, a table. .md source should still be readable. Also, GH doesn't render that since it's not part of GFM, AFAIR.

[Diffs containing tables with long text will become really wide (600+ columns)](https://github.com/RadeonOpenCompute/ROCm/blob/903aae3321c2f7c8848b7b1386d175495120e93f/docs/reference/rocmcc/rocmcc.md?plain=1#L45-L53). Why should with stick to GFM when we use MyST that will be rendered out via Sphinx?

Replacing
```markdown
| **Table 1. rocm-llvm vs. rocm-llvm-alt**            |                                                                                                                               |
|:---------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|
| **rocm-llvm**                                       | **rocm-llvm-alt**                                                                                                             |
| Installed by default when ROCm™ itself is installed | An optional package                                                                                                           |
| Provides an open-source compiler                    | Provides an additional closed-source compiler for users interested in additional CPU optimizations not available in rocm-llvm |
```

with
```markdown
:::{list-table} rocm-llvm vs. rocm-llvm-alt
:header-rows: 1
:name: rocm-llvm-vs-alt

* - **rocm-llvm** 
  - **rocm-llvm-alt**
* - Installed by default when ROCm™ itself is installed
  - An optional package  
* - Provides an open-source compiler  
  - Provides an additional closed-source compiler for users interested
    in additional CPU optimizations not available in rocm-llvm
:::
```
The latter is slightly more readable in-source for me and renders the same via Sphinx. Regardless of how we define the table, we can still use the table directive for captioning and referencing.

---
