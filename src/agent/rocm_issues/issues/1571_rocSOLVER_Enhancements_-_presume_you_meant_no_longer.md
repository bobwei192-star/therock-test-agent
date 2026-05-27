# rocSOLVER Enhancements - presume you meant no longer 

> **Issue #1571**
> **状态**: closed
> **创建时间**: 2021-09-11T18:59:46Z
> **更新时间**: 2021-09-20T07:31:25Z
> **关闭时间**: 2021-09-20T07:31:25Z
> **作者**: whosystem
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1571

## 描述

rocSOLVER
Enhancements

Linear solvers for general non-square systems:

GELS now supports underdetermined and transposed cases

Inverse of triangular matrices

TRTRI (with batched and strided_batched versions)

Out-of-place general matrix inversion

GETRI_OUTOFPLACE (with batched and strided_batched versions)

Argument names for the benchmark client now match argument names from the public API

Fixed Issues

Known issues with Thin-SVD. The problem was identified in the test specification, not in the thin-SVD implementation or the rocBLAS gemm_batched routines.

Benchmark client **no** longer crashes as a result of leading dimension or stride arguments not being provided on the command line.

---

## 评论 (3 条)

### 评论 #1 — doctorcolinsmith (2021-09-14T15:22:31Z)

@whosystem Thanks for catching the error!  We'll get that fixed.

---

### 评论 #2 — Rmalavally (2021-09-18T19:39:20Z)

Thank you for the feedback. The fixed defect for rocSOLVER is corrected in the Release notes document for ROCm v4.3.

AMD ROCm Documentation Team

---

### 评论 #3 — ROCmSupport (2021-09-20T07:31:25Z)

Hi @whosystem 
Thanks for reaching out.
Issue is fixed now. Please check the documentation for the updated information.
Feel free to open a new issue, if any, for quick resolutions.
Thank you.

---
