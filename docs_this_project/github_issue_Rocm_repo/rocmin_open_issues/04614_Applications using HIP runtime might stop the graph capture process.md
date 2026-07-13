# Applications using HIP runtime might stop the graph capture process

- **Issue #:** 4614
- **State:** open
- **Created:** 2025-04-11T23:19:59Z
- **Updated:** 2025-04-11T23:19:59Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4614

Applications using the HIP runtime might stop the graph capture process if the HIP runtime detects an invalid stale state from a previous capture on the same HIP stream. Resetting the stale set for every new capture in the HIP runtime can resolve the issue. The issue will be fixed in a future ROCm release.