# rocm-hip-runtime-dev : Depends: rocm-device-libs problem

- **Issue #:** 2378
- **State:** closed
- **Created:** 2023-08-14T09:18:50Z
- **Updated:** 2024-01-25T09:11:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/2378

i try to install sudo amdgpu-install --usecase=rocm in ubuntu 22.04 (version 5.6.0)
but i get this


The following packages have unmet dependencies:
 rocm-hip-runtime-dev : Depends: rocm-device-libs (= 1.0.0.50600-67~22.04) but 5.0.0-1 is to be installed
 rocm-openmp-sdk : Depends: rocm-device-libs (= 1.0.0.50600-67~22.04) but 5.0.0-1 is to be installed
E: Unable to correct problems, you have held broken packages.
habernir@nirUbuntu:~/Documents$ 




thanks 
nir
