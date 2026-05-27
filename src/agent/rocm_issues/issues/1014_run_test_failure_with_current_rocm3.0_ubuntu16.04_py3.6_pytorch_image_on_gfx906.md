# run_test failure with current rocm3.0_ubuntu16.04_py3.6_pytorch image on gfx906

> **Issue #1014**
> **状态**: closed
> **创建时间**: 2020-02-17T18:21:14Z
> **更新时间**: 2021-04-19T12:54:52Z
> **关闭时间**: 2021-04-19T12:54:52Z
> **作者**: happycube
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1014

## 描述

I tried to follow the instructions in https://rocm.github.io/pytorch.html with rocm3.0_ubuntu16.04_py3.6_pytorch so I can use Python 3... the test invocation needs to be changed to this:

```
cd ~/pytorch
PYTORCH_TEST_WITH_ROCM=1 python3.6 test/run_test.py --verbose
```
and it mostly works, but I get these test errors:

```
======================================================================
ERROR: test_dsmm (__main__.TestCudaSparse)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sparse.py", line 984, in test_dsmm
    test_shape(1000, 0, 100, 0)
  File "test_sparse.py", line 977, in test_shape
    expected = torch.mm(self.safeToDense(x), y)
RuntimeError: CUDA error: rocblas_status_invalid_pointer when calling `rocblas_dgemm( handle, opa, opb, m, n, k, &alpha, a, lda, b, ldb, &beta, c, ldc)`
======================================================================
ERROR: test_dsmm (__main__.TestCudaUncoalescedSparse)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sparse.py", line 984, in test_dsmm
    test_shape(1000, 0, 100, 0)
  File "test_sparse.py", line 977, in test_shape
    expected = torch.mm(self.safeToDense(x), y)
RuntimeError: CUDA error: rocblas_status_invalid_pointer when calling `rocblas_dgemm( handle, opa, opb, m, n, k, &alpha, a, lda, b, ldb, &beta, c, ldc)`
----------------------------------------------------------------------
```

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-04-19T12:54:52Z)

Thanks @happycube 
This issue is fixed and not observed with the latest ROCm 4.1.
Hence recommend you to try with the same.
Feel free to open a new issue, for any, for quick resolution.
Thank you.

---
