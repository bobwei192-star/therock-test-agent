# A memory error in the kernel might lead to applications using the ROCr library becoming unresponsive

- **Issue #:** 5334
- **State:** open
- **Created:** 2025-09-16T15:17:29Z
- **Updated:** 2025-09-16T15:33:41Z
- **Labels:** Verified Issue, ROCm 7.0.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5334

Applications using the ROCr library might become unresponsive if a memory error occurs in the launched kernel when the queue from which it was launched is destroyed. The application is unable to receive further signal, resulting in the stall condition. The issue will be fixed in a future ROCm release.