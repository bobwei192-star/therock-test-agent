# OpenCL-OpenGL interop on Raven Ridge

- **Issue #:** 610
- **State:** closed
- **Created:** 2018-11-13T20:07:54Z
- **Updated:** 2023-12-12T21:51:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/610

Hi,

I have been trying to get the OpenCL-OpenGL interop working on [Raven Ridge APUs](https://en.wikichip.org/wiki/amd/cores/raven_ridge) (e.g. the Ryzen 5 2400G), unfortunately without any luck.

I have tried two different approaches:

1. Ubuntu 18.04.1 with kernel 4.15 and the DKMS module, following the standard install procedure
2. Ubuntu 18.04.1 or 18.10 with kernel 4.19, without the DKMS module, as also discussed in Issue #588.

While the first approach results in a system with a working and usable OpenCL-OpenGL interop when using a discrete Vega 64 card ([using this repo to test](https://github.com/9prady9/CLGLInterop)), the interop does not work on Raven Ridge APUs (while pure OpenCL works, just the interop is broken).

Am I correct in my assumption that CL-GL interop is not supported in the DKMS for Raven Ridge? This also seems to be related to the kernel version, as the 4.15 kernel seems to be the latest one still supported by DKMS (as @jlgreathouse [suggested here](https://github.com/RadeonOpenCompute/ROCm/issues/576#issuecomment-432433555): `rock-dkms is currently broken on kernels newer than 4.15`)?  

This lead me to trying another approach using a newer kernel (4.19, tried both Ubuntu 18.04 and 18.10) that out of the box supports Raven Ridge via `amdgpu`. I installed it like described in Issue #588. But here again, we get a working OpenCL platform with broken CL-GL interop.

Any hints on how I could get this to work??