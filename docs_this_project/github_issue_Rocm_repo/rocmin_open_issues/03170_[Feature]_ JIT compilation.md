# [Feature]: JIT compilation

- **Issue #:** 3170
- **State:** open
- **Created:** 2024-05-28T19:01:08Z
- **Updated:** 2024-06-24T15:17:15Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/3170

### Suggestion Description

ROCm currently requires ahead-of-time compilation, which results in very large packages with limited hardware support.  CUDA, on the other hand, uses just-in-time compilation: software is shipped as an IR, and the runtime compiles only the code the user actually needs.  It would be nice if ROCm had the same ability.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_