# [Issue]: LAMMPS + KOKKOS error when running on MI300X

- **Issue #:** 5655
- **State:** closed
- **Created:** 2025-11-12T08:16:27Z
- **Updated:** 2025-11-19T15:29:25Z
- **Labels:** AMD Instinct MI300X, status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5655

### Problem Description

I get the following error (`hipErrorInvalidKernelFile`) when I try to run a GPU accelerated build of  the LAMMPS molecular dynamics package on a MI300X.

```
  what():  hipMemcpyToSymbol( HIP_SYMBOL(::Kokkos::Impl::g_device_hip_lock_arrays), &::Kokkos::Impl::g_host_hip_lock_arrays, sizeof(::Kokkos::Impl::HIPLockArrays)) error( hipErrorInvalidKernelFile): invalid kernel file /tmp/root/spack-stage/spack-stage-kokkos-3.7.02-6hnbw7mnamym2c7knpyesuyiet2nrt6u/spack-src/core/src/HIP/Kokkos_HIP_Locks.cpp:96
```

I built the software within a container based on ROCm 7.0.2 (but I also tried 6.3.3) and the Spack package manager. [The recipe is available here.](https://github.com/PawseySC/pawsey-containers/blob/cdp-cxivars/benchmarking/bench.dockerfile)

I made sure the software was built for the gfx90a and gfx942 architectures. The container runs fine on Setonix (MI250X system), but fails on a MI300X cluster.

Any idea of what could be causing the error?

### Operating System

Ubuntu 22.04.5

### CPU

AMD Zen4 architecture

### GPU

MI300X

### ROCm Version

6.3.3 and 7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_