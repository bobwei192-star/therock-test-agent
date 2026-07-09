# run_test failure with current rocm3.0_ubuntu16.04_py3.6_pytorch image on gfx906

- **Issue #:** 1014
- **State:** closed
- **Created:** 2020-02-17T18:21:14Z
- **Updated:** 2021-04-19T12:54:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/1014

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