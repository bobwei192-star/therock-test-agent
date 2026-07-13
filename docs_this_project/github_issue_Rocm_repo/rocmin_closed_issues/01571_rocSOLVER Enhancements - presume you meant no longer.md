# rocSOLVER Enhancements - presume you meant no longer 

- **Issue #:** 1571
- **State:** closed
- **Created:** 2021-09-11T18:59:46Z
- **Updated:** 2021-09-20T07:31:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/1571

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