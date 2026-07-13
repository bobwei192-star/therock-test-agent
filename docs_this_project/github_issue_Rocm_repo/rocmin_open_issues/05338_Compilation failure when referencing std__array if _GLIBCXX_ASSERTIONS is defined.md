# Compilation failure when referencing std::array if _GLIBCXX_ASSERTIONS is defined

- **Issue #:** 5338
- **State:** open
- **Created:** 2025-09-16T15:30:23Z
- **Updated:** 2025-09-16T15:34:11Z
- **Labels:** Verified Issue, ROCm 7.0.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5338

Compiling from a device kernel or function results in failure when attempting to reference `std::array` if `_GLIBCXX_ASSERTIONS` is defined. The issue occurs because there's no device definition for `std::__glibcxx_asert_fail()`. This issue will be resolved in a future ROCm release with the implementation of `std::__glibcxx_assert_fail()`.