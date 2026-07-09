# Failure to declare out-of-bound CPERs for bad memory page

- **Issue #:** 5345
- **State:** open
- **Created:** 2025-09-16T15:40:09Z
- **Updated:** 2025-09-16T15:40:09Z
- **Labels:** Verified Issue, ROCm 7.0.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5345

Exceeding bad memory page threshold fails to declare Out-Of-Band Common Platform Error Records (CPERs). This issue affects all AMD Instinct MI300 Series and MI350 Series GPUs, and will be fixed in a future AMD GPU Driver release.