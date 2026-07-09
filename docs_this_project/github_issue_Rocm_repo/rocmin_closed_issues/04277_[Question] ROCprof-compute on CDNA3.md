# [Question] ROCprof-compute on CDNA3

- **Issue #:** 4277
- **State:** closed
- **Created:** 2025-01-20T21:22:46Z
- **Updated:** 2025-01-21T19:43:04Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4277

When looking at `rocprof-compute` for hardware events profiling on MI300A (CDNA3) platforms, I'm not finding details for the infinity cache. The more I think about it, the more I'm realizing that there is likely things that are missing.

For memory operations profiling, `rocprof-compute` only provides analysis of L1, L2, LDS, and HBM memory; however, CDNA3 introduced another layer of cache (infinity cache) between L2 and HBM. What I'm wondering is what the L2 profiling metrics are actually showing in `rocprof-compute` ? Are they actually showing metrics related to Infinity Cache (L3) ??

Can you provide some clarification about using rocprof-compute on CDNA3 architectures ?