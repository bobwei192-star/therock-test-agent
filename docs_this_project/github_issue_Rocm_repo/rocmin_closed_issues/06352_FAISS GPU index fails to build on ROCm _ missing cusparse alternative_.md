# FAISS GPU index fails to build on ROCm — missing cusparse alternative?

- **Issue #:** 6352
- **State:** closed
- **Created:** 2026-06-11T18:10:42Z
- **Updated:** 2026-06-24T15:03:43Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6352

Trying to build FAISS with GPU support on ROCm. CMake fails at the cusparse dependency check.

```
CMake Error: Could not find cusparse (required for GPU index)
```

I know cusparse is NVIDIA-only. Is there a ROCm equivalent (rocsparse?) that FAISS can use? Or is there a fork that supports AMD GPUs?

Currently using FAISS CPU fallback which is 8x slower for my embedding search workload.

Setup: RX 7800 XT, ROCm 5.7, FAISS 1.7.4