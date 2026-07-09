# rocprofv3 fails on RPM-based OS with Python 3.10 (and later)

- **Issue #:** 5606
- **State:** closed
- **Created:** 2025-10-31T17:50:01Z
- **Updated:** 2026-01-28T16:18:21Z
- **Labels:** Verified Issue, ROCm 7.1.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5606

On RPM-based operating systems (such as RHEL 8), the `rocprofv3` tool fails with Python 3.10 and later due to missing ROCPD bindings. As a workaround, use Python 3.6 if you need to use the `rocprofv3` tool with ROCm 7.1.0. This issue will be fixed in a future ROCm release.