# MIVisionX memory access fault in Canny edge detection

- **Issue #:** 4086
- **State:** closed
- **Created:** 2024-12-03T22:19:44Z
- **Updated:** 2025-01-28T20:32:48Z
- **Labels:** Verified Issue, AMD Instinct MI300X, AMD Instinct MI300A, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4086

Canny edge detection kernels might access out-of-bounds memory locations while computing gradient intensities on edge pixels. This issue is isolated to Canny-specific use cases on Instinct MI300 series accelerators. This issue is resolved in the [MIVisionX develop branch](https://github.com/ROCm/mivisionx) and will be part of a future ROCm release.