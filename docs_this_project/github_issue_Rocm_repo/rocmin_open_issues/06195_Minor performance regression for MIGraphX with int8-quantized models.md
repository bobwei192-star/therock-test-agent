# Minor performance regression for MIGraphX with int8-quantized models

- **Issue #:** 6195
- **State:** open
- **Created:** 2026-05-04T14:45:39Z
- **Updated:** 2026-05-04T14:46:37Z
- **Labels:** Verified Issue, ROCm 7.2.3
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6195

You might observe a slight performance regression when running int8-quantized models with MIGraphX. This impact is generally minimal and does not affect correctness. However, workloads sensitive to peak throughput might have reduced performance when compared to non-quantized or alternative execution paths. This issue is currently under investigation and will be fixed in a future ROCm release.