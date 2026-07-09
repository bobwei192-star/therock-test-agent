# Longer runtime for hipBLASLt GEMM operations on Instinct MI300X GPUs in partitioned mode

- **Issue #:** 6066
- **State:** open
- **Created:** 2026-03-25T23:30:33Z
- **Updated:** 2026-03-25T23:31:01Z
- **Labels:** Verified Issue, ROCm 7.2.1
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6066

GEMM operations using hipBLASLt might result in longer runtime on AMD Instinct MI300X GPUs configured in CPX or NPS4 partition mode (38 control units or CUs). This issue occurs when hipBLASLt fails to find applicable pre-tuned kernels. As a result, it performs an extensive kernel search, which increases both search time and the overall operation runtime. This issue is resolved in the {fab}`github`[hipBLASLt develop branch](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblaslt) and will be part of a future ROCm release.