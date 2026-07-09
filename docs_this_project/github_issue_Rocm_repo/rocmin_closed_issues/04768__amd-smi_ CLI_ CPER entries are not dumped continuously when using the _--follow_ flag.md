# `amd-smi` CLI: CPER entries are not dumped continuously when using the `--follow` flag

- **Issue #:** 4768
- **State:** closed
- **Created:** 2025-05-21T18:44:11Z
- **Updated:** 2025-07-21T20:47:23Z
- **Labels:** Verified Issue, ROCm 6.4.1
- **URL:** https://github.com/ROCm/ROCm/issues/4768

When using the `--follow` flag with `amd-smi ras --cper`, CPER entries are not streamed continuously as intended. This will be fixed in an upcoming ROCm release.