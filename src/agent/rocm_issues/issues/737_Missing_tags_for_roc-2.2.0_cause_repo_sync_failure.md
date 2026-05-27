# Missing tags for roc-2.2.0 cause repo sync failure

> **Issue #737**
> **状态**: closed
> **创建时间**: 2019-03-14T13:14:21Z
> **更新时间**: 2019-03-16T00:15:26Z
> **关闭时间**: 2019-03-16T00:15:26Z
> **作者**: FinnStokes
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/737

## 描述

There is no `roc-2.2.0` tag in the `rocm_bandwidth_test`, `rocm_smi_lib`, and `roctracer`. In addition, revision `7ce124f86d0fa59387462fc09a49b25ccb81f96` doesn't seem to exist in the tree for `clang-ocl` on github. This causes `repo sync` to fail.

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-03-16T00:15:26Z)

Fixed. Just pushed the changes and verified that a full repo sync works. Thanks for the report about this, and sorry about the problems.

---
