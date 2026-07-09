# [Issue]: hipEventSynchronize sporadically failing on ROCm 6.4 on Radeon Pro VII

- **Issue #:** 4670
- **State:** closed
- **Created:** 2025-04-23T11:59:59Z
- **Updated:** 2025-04-28T19:15:08Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4670

### Problem Description

We see `hipEventSynchronize` sporadically fail on ROCm 6.4 on **Radeon Pro VII**.

The failures arise in the CICD pipelines of our HPC code that we build on top of `Kokkos` with the `HIP` backend.

The failures are sporadic, but frequent enough to impact our work significantly. The error message looks like:
```bash
terminate called after throwing an instance of 'std::runtime_error'
  what():  hip_instance->hip_event_synchronize_wrapper( HIPInternal::constantMemReusable[hip_device]) error( hipErrorCapturedEvent): operation not permitted on an event last recorded in a capturing stream /opt/kokkos/include/HIP/Kokkos_HIP_KernelLaunch.hpp:525
Aborted (core dumped)
```

The error message is a bit surprising, because neither in our HPC code, neither in `Kokkos`, there is a graph capture. We raised the issue on the `Kokkos` repository:

- https://github.com/kokkos/kokkos/issues/8006

We posted a self-contained reproducer in a Dockerfile in that issue.

One particularity of the context in which the issue arises is that the "event record" and the "event synchronize" might be far apart. It can even happen that our code calls `eventSynchronize` on an event that was recorded into a stream when that stream may actually have been destroyed in the mean time.

We see the issue on Radeon PRO VII. We did limited testing on MI300A, where we didn't see the issue. We didn't test other architectures.

We are aware that Radeon PRO VII has been deprecated for a while in ROCm. But we did see Radeon PRO VII in AMD's recent "Developers, Developers, Developers" video for the community. So also tagging @powderluv in the hope that this apparent bug with the HIP event management API on (at least) Radeon PRO VII can be looked into and solved. Radeon PRO VII is (currently) the last prosumer GPU with great FP64 support. Thanks in any case.

@Rombur @romintomasetti




### Operating System

Ubuntu 24.04

### CPU

AMD Ryzen 5950X

### GPU

AMD Radeon PRO VII

### ROCm Version

Rocm 6.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_