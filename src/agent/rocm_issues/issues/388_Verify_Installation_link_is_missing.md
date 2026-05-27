# "Verify Installation" link is missing

> **Issue #388**
> **状态**: closed
> **创建时间**: 2018-04-18T14:56:34Z
> **更新时间**: 2018-05-12T13:05:47Z
> **关闭时间**: 2018-05-12T13:05:22Z
> **作者**: grische
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/388

## 描述

The link to https://github.com/RadeonOpenCompute/ROCm#verify-installation is invalid, but it is mentioned on both documentations:

* [README.md](https://github.com/RadeonOpenCompute/ROCm/tree/7f15331a67361162346596ee43c5293d97536467/README.md#L175)
* https://rocm.github.io/install.html

Where is this supposed to point to? 

---

## 评论 (3 条)

### 评论 #1 — Bengt (2018-04-22T13:33:01Z)

I took a dig through the commit history and found that there once was a description on how to run example code from the HSA examples:

  https://github.com/RadeonOpenCompute/ROCm/commit/b06d1370975695c823e6ca2fd4c85ea22abbf958#diff-04c6e90faac2675aa89e2176d2eec7d8R155

That was however recently removed:

  https://github.com/RadeonOpenCompute/ROCm/commit/6e5b253e67b4f9b06f311227b8ea26e8c1d2e121#diff-04c6e90faac2675aa89e2176d2eec7d8L291

There now is a package HIP examples, but still nothing ROCM-specific, as far as I can tell:

  https://github.com/ROCm-Developer-Tools/HIP-Examples/tree/roc-1.7.x 

Perhaps one could use ROCM-SMI or ROCM-Info for a simple test of the platform:

    /opt/rocm/bin/rocm-smi --showid

    /opt/rocm/bin/rocminfo

@jedwards-AMD might have an opinion on this, as he added and removed these instructions to the README.

---

### 评论 #2 — gstoner (2018-05-12T13:05:22Z)

We addressed this issue 

---

### 评论 #3 — gstoner (2018-05-12T13:05:47Z)

Also we are working on new Customer Validation Test Suite it be out in the fall 

---
