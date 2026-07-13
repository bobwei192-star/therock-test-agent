# OpenCL codegen: disable FP IEEE_mode on -cl-fast-relaxed-math

- **Issue #:** 967
- **State:** closed
- **Created:** 2019-12-15T07:16:54Z
- **Updated:** 2024-10-17T16:01:23Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/967

See #964 for context.
When OpenCL compilation is done with -cl-fast-relaxed-math (or maybe even just -cl-finite-math-only) disable FP IEEE_mode.

Why: this allows more efficient code to be generated, and that's exactly the intention of -cl-fast-relaxed-math. The generated code is potentially more efficient with IEEE_mode disabled because e.g. output-modifiers (mul:2) can be used, which are otherwise disabled in IEEE_mode.

Additionally, there is no other mecanism currently to control IEEE_mode in OpenCL.