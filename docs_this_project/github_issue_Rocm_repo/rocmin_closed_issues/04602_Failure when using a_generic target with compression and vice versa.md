# Failure when using a generic target with compression and vice versa

- **Issue #:** 4602
- **State:** closed
- **Created:** 2025-04-11T23:05:09Z
- **Updated:** 2025-09-16T17:37:59Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4602

In ROCm 6.4.0, compilation for generic target with compression will fail. As a result, you won't be able to compile for a generic target and use compression simultaneously. As a workaround, it's recommended not to use compression when using generic targets and vice versa. This issue will be addressed in a future ROCm release.