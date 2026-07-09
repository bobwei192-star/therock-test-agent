# rocThrust and rocPRIM libraries no longer supporting certain iterator types

- **Issue #:** 2110
- **State:** closed
- **Created:** 2023-05-04T09:26:59Z
- **Updated:** 2023-05-04T09:27:08Z
- **Labels:** Verified Issue, 5.3.0, 5.3.1, 5.3.2
- **URL:** https://github.com/ROCm/ROCm/issues/2110

This issue is ported from the release notes.

There is a known known issue with rocThrust and rocPRIM libraries supporting iterator and types in ROCm v5.3.x releases.

- `thrust::merge` no longer correctly supports different iterator types for `keys_input1` and `keys_input2`.
- `rocprim::device_merge` no longer correctly supports using different types for `keys_input1` and `keys_input2`.