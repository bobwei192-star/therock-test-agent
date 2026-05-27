# Cannot repo sync roc-2.0.0 (MIVisionX)

> **Issue #690**
> **状态**: closed
> **创建时间**: 2019-01-26T10:25:01Z
> **更新时间**: 2019-01-29T18:10:30Z
> **关闭时间**: 2019-01-29T18:10:30Z
> **作者**: seesturm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/690

## 描述

When following the instructions for roc-2.0.0 "repo sync" fails at fetching the MIVisionX repository. In default.xml revision points to "1.0.0", but no such branch exists.

Changing revision to "refs/tags/1.0.0" makes "repo sync" succeed. I'm using repo tool version v1.12.37.

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-01-29T18:10:30Z)

Thanks for catching this! Patch submitted.

---
