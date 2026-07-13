# It is weired that RDNA2 support windows while Vega not

- **Issue #:** 2053
- **State:** closed
- **Created:** 2023-04-15T13:01:54Z
- **Updated:** 2024-01-24T20:17:48Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/2053

Please refer here: <https://github.com/RadeonOpenCompute/ROCm/blob/19c0ba11505cf504d42b2096713d761236202361/docs/release/gpu_os_support.md?plain=1#L59-L60>

It is said that using Radeon Pro Driver, RDNA2 likes RX6900xt and Rx6600  can support HIP sdk and runtime on windows, while Radeon VII is not.

As we know, the `amdhip64.dll` is installed by amdgpu driver, so the HIP sdk and runtime should avaiable for both vega10, vega20, cdna, rdna2.

The documents seems point out there is special support on RDNA2, not for other ISA.