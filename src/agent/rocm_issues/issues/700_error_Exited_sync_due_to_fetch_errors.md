# error: Exited sync due to fetch errors

> **Issue #700**
> **状态**: closed
> **创建时间**: 2019-02-06T14:09:06Z
> **更新时间**: 2019-02-07T12:57:05Z
> **关闭时间**: 2019-02-06T17:58:51Z
> **作者**: zockolade
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/700

## 描述

Still not able to checkout the sourcecode.
The process end up with: 
error: Exited sync due to fetch errors

and in a longer form:

remote: Total 6288675 (delta 25670), reused 28988 (delta 25035), pack-reused 6257163        MiB/s   
Receiving objects: 100% (6288675/6288675), 1.34 GiB | 2.45 MiB/s, done.
Resolving deltas: 100% (5308789/5308789), done.
From http://github.com/RadeonOpenCompute/ROCK-Kernel-Driver
 * [new tag]         roc-2.1.0  -> roc-2.1.0
 * [new tag]         roc-1.0.0  -> roc-1.0.0
 * [new tag]         roc-1.1.0  -> roc-1.1.0
 * [new tag]         roc-1.1.1  -> roc-1.1.1
 * [new tag]         roc-1.2.0  -> roc-1.2.0
 * [new tag]         roc-1.3.0  -> roc-1.3.0
 * [new tag]         roc-1.3.1  -> roc-1.3.1
 * [new tag]         roc-1.5.0  -> roc-1.5.0
 * [new tag]         roc-1.5.1  -> roc-1.5.1
 * [new tag]         roc-1.6.0  -> roc-1.6.0
 * [new tag]         roc-1.6.1  -> roc-1.6.1
 * [new tag]         roc-1.6.2  -> roc-1.6.2
 * [new tag]         roc-1.6.3  -> roc-1.6.3
 * [new tag]         roc-1.7.0  -> roc-1.7.0
 * [new tag]         roc-1.7.1  -> roc-1.7.1
 * [new tag]         roc-1.7.2  -> roc-1.7.2
 * [new tag]         roc-1.8.0  -> roc-1.8.0
 * [new tag]         roc-1.8.1  -> roc-1.8.1
 * [new tag]         roc-1.8.2  -> roc-1.8.2
 * [new tag]         roc-1.8.3  -> roc-1.8.3
 * [new tag]         roc-1.9.0  -> roc-1.9.0
 * [new tag]         roc-1.9.1  -> roc-1.9.1
 * [new tag]         roc-1.9.2  -> roc-1.9.2
 * [new tag]         roc-2.0.0  -> roc-2.0.0
Fetching projects:  97% (41/42)  
error: Exited sync due to fetch errors



---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2019-02-06T16:47:25Z)

Repo is attempting to download multiple projects in parallel, so it's not the ROCK project that is failing to download. The underlying problem (if you keep running `repo sync` until all other projects are downloaded) is that we missed the `roc-2.1.0` tag on `rocm_smi_lib`. We're in the process of getting this fixed.

---

### 评论 #2 — jlgreathouse (2019-02-06T17:58:51Z)

This should be fixed now. Thanks for the report.

---

### 评论 #3 — zockolade (2019-02-07T12:57:05Z)

Thanks for your fast intervention. It looks like getting all this components together will be quite harder.

---
