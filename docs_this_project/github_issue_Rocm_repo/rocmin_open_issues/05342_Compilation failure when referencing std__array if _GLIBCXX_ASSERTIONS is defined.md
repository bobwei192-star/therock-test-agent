# Compilation failure when referencing std::array if _GLIBCXX_ASSERTIONS is defined

- **Issue #:** 5342
- **State:** open
- **Created:** 2025-09-16T15:37:26Z
- **Updated:** 2025-09-16T17:35:56Z
- **Labels:** Verified Issue, ROCm 7.0.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5342

Compiling from a device kernel or function results in failure when attempting to reference `std::array` if `_GLIBCXX_ASSERTIONS` is defined. The issue occurs because there's no device definition for `std::__glibcxx_asert_fail()`. This issue will be resolved in a future ROCm release with the implementation of `std::__glibcxx_assert_fail()`.