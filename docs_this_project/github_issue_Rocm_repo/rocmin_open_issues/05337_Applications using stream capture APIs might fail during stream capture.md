# Applications using stream capture APIs might fail during stream capture

- **Issue #:** 5337
- **State:** open
- **Created:** 2025-09-16T15:26:53Z
- **Updated:** 2026-03-06T15:44:58Z
- **Labels:** Verified Issue, ROCm 7.0.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5337

Applications using ``hipLaunchHostFunc`` with stream capture APIs might fail to capture graphs during stream capture, and return `hipErrorStreamCaptureUnsupported`. This issue resulted from an update in ``hipStreamAddCallback``. This issue will be fixed in a future ROCm release.