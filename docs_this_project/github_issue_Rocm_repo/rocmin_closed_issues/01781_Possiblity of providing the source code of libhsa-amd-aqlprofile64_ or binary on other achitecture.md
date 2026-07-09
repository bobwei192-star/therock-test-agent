# Possiblity of providing the source code of libhsa-amd-aqlprofile64, or binary on other achitecture

- **Issue #:** 1781
- **State:** closed
- **Created:** 2022-08-07T04:48:21Z
- **Updated:** 2025-06-12T14:12:13Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/1781

Hello, I am a member of Gentoo ROCm packaging team. There are a long history of discussing the closed-source libhsa-amd-aqlprofile64.so:

- https://bugs.gentoo.org/716948
- https://github.com/ROCm-Developer-Tools/rocprofiler/issues/38

Although not loading libhsa-amd-aqlprofile64.so does not affect running rocm, it does block rocprofiler's tracing, and the only source of libhsa-amd-aqlprofile64.so we can find is amd64 binary package. If ROCm is installed on arm or other arch, or compiled against musl, full featured profiling would be impossible.

So where can we find  the source code of libhsa-amd-aqlprofile64.so? It seems that it was previously open sourced in https://github.com/RadeonOpenCompute/HSA-AqlProfile-AMD-extension, but this is removed.