# AddressSanitizer fails in applications using texture references

- **Issue #:** 2552
- **State:** closed
- **Created:** 2023-10-13T21:40:21Z
- **Updated:** 2024-05-15T18:42:07Z
- **Labels:** Resolved, 5.7.1
- **URL:** https://github.com/ROCm/ROCm/issues/2552

The AddressSanitizer (ASan) feature may be unusable for HIP applications using texture references due to a runtime check failing on ASan instrumented texture references.

This known issue is under investigation and is expected to be fixed in a future release.

This issue is now resolved.
