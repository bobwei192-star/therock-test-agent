# Add linkcheck to check for broken links in .readthedocs.yaml config file

> **Issue #1997**
> **状态**: closed
> **创建时间**: 2023-03-28T22:24:31Z
> **更新时间**: 2023-07-05T21:29:48Z
> **关闭时间**: 2023-07-05T21:29:48Z
> **作者**: samjwu
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1997

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- MathiasMagnus
- samjwu

## 描述

Ref: https://docs.readthedocs.io/en/stable/build-customization.html#perform-a-check-for-broken-links

To make sure external links are working

Goal: Have this across all ROCm repos for documentation 

---

## 评论 (2 条)

### 评论 #1 — samjwu (2023-05-24T18:15:07Z)

https://docs.readthedocs.io/en/stable/build-customization.html#perform-a-check-for-broken-links

sphinx linkcheck has many false negatives (working links marked broken) 
eg: https://github.com/RadeonOpenCompute/ROCm/pull/2173

explore alternative
eg: https://github.com/gaurav-nelson/github-action-markdown-link-check

---

### 评论 #2 — samjwu (2023-07-05T21:29:47Z)

Resolution: regular reports from https://www.deadlinkchecker.com/ instead of adding this as a CI Action

Reason: links may die, causing CI for unrelated PRs to fail

---
