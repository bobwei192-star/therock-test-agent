# Can't install ROCm 1.8.1 with Ubuntu 16.04 LTS (Desktop version)

- **Issue #:** 439
- **State:** closed
- **Created:** 2018-06-20T20:43:37Z
- **Updated:** 2019-01-08T18:53:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/439

Hi there,

I have followed every step in https://github.com/RadeonOpenCompute/ROCm and yet when I come to the step where I have to type "rocminfo" it returns "rocminfo: command not found". uname -r also doesn't look like it's a ROCm kernel.."4.13.0-45-generic".
Setup:
Intel Celeron G3930
RX 550 hooked up via a riser into the 16x slot.

amdgpu-pro 18.20 works perfectly. But I need the ROCm kernel. Any suggestions?

edit: also, it was a fresh install of Ubuntu 16.04 LTS, so no old ROCm kernels were present at any moment...
sudo dkms status returns
amdgpu, 1.8-151, 4.13.0-45-generic, x86_64: installed
and yes, I added user to video group
also, cl info outputs Number Of platforms 0