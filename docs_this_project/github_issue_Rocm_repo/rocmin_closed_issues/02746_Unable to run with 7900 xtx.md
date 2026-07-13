# Unable to run with 7900 xtx

- **Issue #:** 2746
- **State:** closed
- **Created:** 2023-12-18T08:58:53Z
- **Updated:** 2024-03-31T15:10:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/2746

Hi I've tried every combination possible of rocm and pytorch
(with docker, without, from sources, 5.6, 5.7, with env variables, ...)
but all that I get is 100% CPU forever of immediate segfault.

This is on fresh ubuntu 22.04.

amdgpu-install has all the 'usecases', rocminfo and rocm-smi do work,
steam is able to run 3d accelerated games
and on windows the card works (tried stable diffusion, shark ai, directml)

Did anyone here have more luck ?
