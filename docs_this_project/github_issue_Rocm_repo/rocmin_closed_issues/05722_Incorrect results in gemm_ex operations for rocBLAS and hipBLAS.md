# Incorrect results in gemm_ex operations for rocBLAS and hipBLAS

- **Issue #:** 5722
- **State:** closed
- **Created:** 2025-11-28T21:40:46Z
- **Updated:** 2026-01-28T16:18:40Z
- **Labels:** Verified Issue, ROCm 7.1.1
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5722

Some `gemm_ex` operations with 8-bit input data types (`int8`, `float8`, `bfloat8`) for specific matrix dimensions (K = 1 and number of workgroups > 1) might yield incorrect results. The issue results from incorrect tailloop code that fails to consider workgroup index when calculating valid element size. The issue will be fixed in a future ROCm release.