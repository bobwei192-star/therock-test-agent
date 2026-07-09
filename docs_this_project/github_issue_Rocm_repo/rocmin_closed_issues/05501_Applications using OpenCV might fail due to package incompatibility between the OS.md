# Applications using OpenCV might fail due to package incompatibility between the OS

- **Issue #:** 5501
- **State:** closed
- **Created:** 2025-10-10T22:49:13Z
- **Updated:** 2026-01-28T16:18:26Z
- **Labels:** Verified Issue, ROCm 7.0.2
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5501

OpenCV packages built on Ubuntu 24.04 are incompatible with Debian 13 due to a version conflict. As a result, applications, tests, and samples that use OpenCV might fail. As a workaround, rebuild OpenCV with the version corresponding to Debian 13 from source, followed by the application that uses OpenCV. This issue will be fixed in a future ROCm release.