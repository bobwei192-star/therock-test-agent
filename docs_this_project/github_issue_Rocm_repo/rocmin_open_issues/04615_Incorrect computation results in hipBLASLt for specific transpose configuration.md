# Incorrect computation results in hipBLASLt for specific transpose configuration

- **Issue #:** 4615
- **State:** open
- **Created:** 2025-04-11T23:20:43Z
- **Updated:** 2025-04-11T23:20:43Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4615

When running the hipBLASLt library using the transpose configuration (TT) with FP32 and XF32 data types, you might receive incorrect computation results. As a workaround, select alternative solutions from the list returned by `hipblasLtMatmulAlgoGetHeuristic()`. Verify the result to identify the correct alternative solution. The issue will be fixed in a future ROCm release.