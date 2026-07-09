# distributed/test_distributed_spawn Fails

- **Issue #:** 2107
- **State:** closed
- **Created:** 2023-05-04T08:00:10Z
- **Updated:** 2024-02-16T20:10:51Z
- **Labels:** Verified Issue, 5.5.0
- **URL:** https://github.com/ROCm/ROCm/issues/2107

This issue is ported from the release notes.

When user applications call `ncclCommAbort` to destruct communicators and then create new
communicators repeatedly, subsequent communicators may fail to initialize.