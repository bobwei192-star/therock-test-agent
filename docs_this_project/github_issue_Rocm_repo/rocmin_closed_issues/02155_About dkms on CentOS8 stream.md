# About dkms on CentOS8 stream

- **Issue #:** 2155
- **State:** closed
- **Created:** 2023-05-20T04:06:40Z
- **Updated:** 2023-11-10T16:29:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/2155

Hi all,

I tried this and $ sudo amdgpu-install --usecase=hiplibsdk,rocm.
After installing finished, I did $rocm-smi but I is not woriking well.
I found an error during $ sudo amdgpu-install --usecase=hiplibsdk,rocm.
The error shows
Loading new amdgpu-5.18.13-1538762.el8 DKMS files...

Building for 4.18.0-490.el8.x86_64

Building initial module for 4.18.0-490.el8.x86_64

Error! Bad return status for module build on kernel: 4.18.0-490.el8.x86_64 (x86_64)

Consult /var/lib/dkms/amdgpu/5.18.13-1538762.el8/build/make.log for more information.

And I check the make.log
$ cat /var/lib/dkms/amdgpu/5.18.13-1538762.el8/build/make.log

DKMS make.log for amdgpu-5.18.13-1538762.el8 for kernel 4.18.0-490.el8.x86_64 (x86_64) 2023年 5月 19日 金曜日 15:50:29 JST

make: ディレクトリ '/usr/src/kernels/4.18.0-490.el8.x86_64'　に入ります /var/lib/dkms/amdgpu/5.18.13-1538762.el8/build/Makefile:16: *** dma_resv->seq is missing., exit.... 中止.

make: *** [Makefile:1616: module/var/lib/dkms/amdgpu/5.18.13-1538762.el8/build] エラー 2 make: ディレクトリ '/usr/src/kernels/4.18.0-490.el8.x86_64' から出ます

Now I am using CentOS8stream and kernel is $ uname -r 4.18.0-490.el8.x86_64

Could you teach me how to fix it?


And when I try installing $sudo amdgpu-install --usecase=dkms, I get a WARNING: amdgpu dkms failed for running kernel