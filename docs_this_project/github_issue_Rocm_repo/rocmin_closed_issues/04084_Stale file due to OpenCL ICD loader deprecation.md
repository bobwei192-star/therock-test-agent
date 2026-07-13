# Stale file due to OpenCL ICD loader deprecation

- **Issue #:** 4084
- **State:** closed
- **Created:** 2024-12-03T22:19:39Z
- **Updated:** 2025-01-28T18:43:26Z
- **Labels:** Verified Issue, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4084

When upgrading from ROCm 6.2.x to ROCm 6.3.0, the [removal of the rocm-icd-loader package](https://rocm.docs.amd.com/en/docs-6.3.0/about/release-notes.html#opencl-icd-loader-separated-from-rocm) leaves a stale file in the old `rocm-6.2.x` directory. This has no functional impact. As a workaround, manually uninstall the `rocm-icd-loader` package to remove the stale file. This issue will be addressed in a future ROCm release.