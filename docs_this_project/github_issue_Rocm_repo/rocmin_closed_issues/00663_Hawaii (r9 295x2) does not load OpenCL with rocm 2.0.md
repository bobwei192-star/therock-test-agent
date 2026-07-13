# Hawaii (r9 295x2) does not load OpenCL with rocm 2.0

- **Issue #:** 663
- **State:** closed
- **Created:** 2019-01-05T18:35:10Z
- **Updated:** 2019-01-07T23:05:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/663


I have a Intel Haswell PC with two R9 295X2, rocm opencl is not working, clinfo just shows no platforms available.
But rocminfo works, and loading the amdgpu 18.10 opencl implementation through LD_LIBRARY_PATH also works.

I'm using the latest rocm and rocm-dkms in the apt repo with ubuntu 16.04 and kernel 4.15, and also copied the hawaii firmware files to the amdgpu folder.
