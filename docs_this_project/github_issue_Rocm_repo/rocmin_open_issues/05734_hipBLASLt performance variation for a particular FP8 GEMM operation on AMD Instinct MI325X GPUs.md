# hipBLASLt performance variation for a particular FP8 GEMM operation on AMD Instinct MI325X GPUs

- **Issue #:** 5734
- **State:** open
- **Created:** 2025-12-03T13:03:31Z
- **Updated:** 2025-12-03T13:03:50Z
- **Labels:** Verified Issue, ROCm 7.1.1
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5734

If you’re using hipBLASLt on AMD Instinct MI325X GPUs for large FP8 GEMM operations (such as 9728x8192x65536), you might observe a noticeable performance variation. The issue is currently under investigation and will be fixed in a future ROCm release.