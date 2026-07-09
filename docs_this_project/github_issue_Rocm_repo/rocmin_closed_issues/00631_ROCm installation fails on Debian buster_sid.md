# ROCm installation fails on Debian buster/sid

- **Issue #:** 631
- **State:** closed
- **Created:** 2018-12-08T23:11:47Z
- **Updated:** 2021-07-19T13:37:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/631

On Debian/testing, apt install rocm-dkms fails with
Error! Bad return status for module build on kernel: 4.18.0-3-amd64 (amd64)
Consult /var/lib/dkms/amdgpu/1.9-307/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10

I attach the file
[make.log](https://github.com/RadeonOpenCompute/ROCm/files/2660115/make.log)
