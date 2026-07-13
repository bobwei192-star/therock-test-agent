# Reduced precision in gemm_ex operations for rocBLAS and hipBLAS

- **Issue #:** 5640
- **State:** closed
- **Created:** 2025-11-07T23:50:06Z
- **Updated:** 2025-11-27T15:04:15Z
- **Labels:** Verified Issue, ROCm 7.1.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5640

Some `gemm_ex` operations with `half` or `f32_r` data types might yield 16-bit precision results instead of the expected 32-bit precision when matrix dimensions are m=1 or n=1. The issue results from the optimization that enables `_ex` APIs to use lower precision multiples. It limits the high-precision matrix operations performed in PyTorch with rocBLAS and hipBLAS. The issue will be fixed in a future ROCm release.