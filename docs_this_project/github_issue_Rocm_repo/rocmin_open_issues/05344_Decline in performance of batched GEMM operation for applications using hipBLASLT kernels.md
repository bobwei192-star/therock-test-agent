# Decline in performance of batched GEMM operation for applications using hipBLASLT kernels

- **Issue #:** 5344
- **State:** open
- **Created:** 2025-09-16T15:39:22Z
- **Updated:** 2025-11-10T23:55:45Z
- **Labels:** Verified Issue, ROCm 7.0.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5344

Default batched General Matrix Multiplications (GEMM) operations for rocBLAS and hipBLAS on gfx1200 and gfx1201 may have a decline in performance in comparison with non-batched and strided_batched GEMM operations. By default, the batched GEMM uses hipBLASLT kernels, and switching to the Tensile kernel resolves the performance decline issue. The issue will be fixed in a future ROCm release. As a workaround, you can set the environment variable `ROCBLAS_USE_HIPBLASLT=0` before the batched GEMM operation is performed on gfx1200 and gfx1201. After completing the batched operation, reset the variable to `ROCBLAS_USE_HIPBLASLT=1` before calling non-batched or strided_batched operations.