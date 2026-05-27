# where the roc-2.3 tag of this repo

> **Issue #763**
> **状态**: closed
> **创建时间**: 2019-04-13T09:40:25Z
> **更新时间**: 2024-01-09T08:56:50Z
> **关闭时间**: 2024-01-09T08:56:50Z
> **作者**: wormwang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/763

## 描述

*(无描述)*

---

## 评论 (3 条)

### 评论 #1 — johnbridgman (2019-04-15T01:40:27Z)

Not sure about tags, but a roc-2.3.0 branch was just added to the repo (it was missing before, sorry). 

Doing a repo sync will still run into problems with lld and llvm because those repos were each split into two parts between 2.2 and 2.3... work is being done on that now.

---

### 评论 #2 — wormwang (2019-04-15T03:47:57Z)

some repo still lost roc-2.3.0 tag

warning: redirecting to https://github.com/RadeonOpenCompute/lld/
fatal: Couldn't find remote ref refs/tags/roc-2.3.0
warning: redirecting to https://github.com/RadeonOpenCompute/llvm/
fatal: Couldn't find remote ref refs/tags/roc-2.3.0
warning: redirecting to https://github.com/RadeonOpenCompute/lld/
fatal: Couldn't find remote ref refs/tags/roc-2.3.0
warning: redirecting to https://github.com/RadeonOpenCompute/llvm/
fatal: Couldn't find remote ref refs/tags/roc-2.3.0
error: Cannot fetch lld from http://github.com/RadeonOpenCompute/lld
error: Cannot fetch llvm from http://github.com/RadeonOpenCompute/llvm

error: Exited sync due to fetch errors


---

### 评论 #3 — nartmada (2024-01-04T05:55:15Z)

Hi @wormwang, please check latest ROCm 6.0 to see if your issue still exists ?  If issue is fixed, please close the ticket.  Thanks.

---
