# TransferBench package not functional

- **Issue #:** 4081
- **State:** closed
- **Created:** 2024-12-03T22:19:30Z
- **Updated:** 2025-01-28T20:35:03Z
- **Labels:** Verified Issue, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4081

TransferBench packages included in the ROCm 6.3.0 release are not compiled properly and are not functional for most GPU targets, with the exception of gfx906. Full functionality will be available in a future ROCm release.

TransferBench is a utility for benchmarking simultaneous transfers between user-specified devices (CPUs or GPUs). See the documentation at [TransferBench documentation](https://rocm.docs.amd.com/projects/TransferBench/en/docs-6.3.0/index.html). Those looking to use TransferBench can access the properly compiled packages at [ROCm/TransferBench](https://github.com/ROCm/TransferBench/releases).