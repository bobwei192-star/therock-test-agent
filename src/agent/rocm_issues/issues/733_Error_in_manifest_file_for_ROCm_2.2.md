# Error in manifest file for ROCm 2.2

> **Issue #733**
> **状态**: closed
> **创建时间**: 2019-03-13T16:57:02Z
> **更新时间**: 2019-03-13T20:56:42Z
> **关闭时间**: 2019-03-13T20:56:34Z
> **作者**: FinnStokes
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/733

## 描述

The contents of default.xml seem to be almost duplicated, causing a parsing error when checking out with repo, when the parser encounters a second xml declaration in the middle of the manifest block:
```
fatal: manifest 'default.xml' not available
fatal: error parsing manifest /home/fstokes/build/ROCm-2.2/.repo/manifests/default.xml: XML or text declaration not at start of entity: line 57, column 0
```

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-03-13T20:56:34Z)

#734 should fix this. Thanks for the report!

---
