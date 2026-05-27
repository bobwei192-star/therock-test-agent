# Convert ROCm SMI Guide to Sphinx based documentation

> **Issue #1942**
> **状态**: closed
> **创建时间**: 2023-03-14T15:54:38Z
> **更新时间**: 2023-06-28T13:20:05Z
> **关闭时间**: 2023-06-28T13:20:04Z
> **作者**: saadrahim
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1942

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- MathiasMagnus
- samjwu

## 描述

*(无描述)*

---

## 评论 (4 条)

### 评论 #1 — aaronmondal (2023-03-23T22:05:11Z)

@MathiasMagnus  Btw you might also consider mkdocs instead. Just saying because we were using sphinx for a long time simply because we didn't know that mkdocs even existed. [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/) is wayy prettier than sphinx :laughing: ([another example](https://ll.eomii.org/guides/cuda_and_hip/)). And configuration via yaml instead of python feels a lot better for a website generator.

---

### 评论 #2 — MathiasMagnus (2023-03-24T09:08:52Z)

@aaronmondal Thank you for the suggestion. Two notes:
- The choice of doc tech isn't up to me (alone).
- The mere size of the ship (the breadth of ROCm documentation) is far greater than to challange Sphinx merely on aesthetics.
- The [material for mkdocs](https://squidfunk.github.io/mkdocs-material/) scrolls sluggishly slow on Firefox. It clearly has only been tested on Chromium-based browsers. (Resembling the browser monopoly of the late 90's, just not IE now.)

---

### 评论 #3 — MathiasMagnus (2023-03-24T14:53:29Z)

@saadrahim Addressed via [this](https://github.com/RadeonOpenCompute/rocm_smi_lib/pull/119) PR. This is also a fair demo of doxysphinx usage and how old docs can be incorporated into the new ones.

~~As mentioned in the PR, hooking it up to this repo (by adding a link to the readthedocs, a rocm-docs-core-related question needs needs to be addressed. (How to be free of the CLI of sass provided by npm). @Maetveis has a nice overview of the possible solutions.~~ This is a demo also of how to get rid of npm dependence. (ReadTheDocs not included.)

---

### 评论 #4 — saadrahim (2023-06-28T13:20:04Z)

Complete and will be published soon.

---
