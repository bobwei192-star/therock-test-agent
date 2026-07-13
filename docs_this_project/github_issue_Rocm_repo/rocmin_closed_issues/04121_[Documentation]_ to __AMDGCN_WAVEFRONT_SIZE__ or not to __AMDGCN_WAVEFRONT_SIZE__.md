# [Documentation]: to __AMDGCN_WAVEFRONT_SIZE__ or not to __AMDGCN_WAVEFRONT_SIZE__

- **Issue #:** 4121
- **State:** closed
- **Created:** 2024-12-06T15:02:40Z
- **Updated:** 2026-01-29T15:33:01Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4121

### Description of errors

[ROCm release notes](https://rocm.docs.amd.com/en/latest/about/release-notes.html#amdgpu-wavefront-size-compiler-macro-deprecation) declare `__AMDGCN_WAVEFRONT_SIZE__` deprecated and refer to [clang documentation](https://rocm.docs.amd.com/projects/llvm-project/en/docs-6.3.0/LLVM/clang/html/AMDGPUSupport.html) for **more** information. The issue is that the said additional information contradicts the release notes, because it states that it's `__AMDGCN_WAVEFRONT_SIZE` that is supposed to be deprecated, leaving developers uncertain about how to future-proof their code. Please resolve the contradiction.


### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_