# Transformer Engine `test_distributed_fused_attn` aborts with fatal Python error

- **Issue #:** 4087
- **State:** closed
- **Created:** 2024-12-03T22:19:50Z
- **Updated:** 2025-04-11T19:54:22Z
- **Labels:** 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4087

The `test_distributed_fused_attn` Pytest case for JAX in [Transformer Engine for ROCm](https://github.com/ROCm/TransformerEngine) fails with a fatal Python error under certain conditions. The root cause is unrelated Transformer Engine but due to some issue within XLA. This XLA issue is under investigation and will be addressed in a future release.