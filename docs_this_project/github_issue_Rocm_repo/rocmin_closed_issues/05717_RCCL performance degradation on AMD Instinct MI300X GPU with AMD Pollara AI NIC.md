# RCCL performance degradation on AMD Instinct MI300X GPU with AMD Pollara AI NIC

- **Issue #:** 5717
- **State:** closed
- **Created:** 2025-11-28T15:09:15Z
- **Updated:** 2026-01-28T16:18:10Z
- **Labels:** Verified Issue, ROCm 7.1.1
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5717

If you’re using RCCL on AMD Instinct MI300X GPUs with AMD Pollara AI NIC, you might observe performance degradation for specific collectives and message sizes. The affected collectives are `Scatter`, `AllToAll`, and `AlltoAllv`. It's recommended to avoid using RCCL packaged with ROCm 7.1.1. As a workaround, use the {fab}`github`[RCCL `develop` branch](https://github.com/ROCm/rccl/tree/develop), which contains the fix and will be included in a future ROCm release.