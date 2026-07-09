# Cannot detect OpenCL platform for both amdgpu-pro and rocm-dkms

- **Issue #:** 692
- **State:** closed
- **Created:** 2019-01-29T09:59:51Z
- **Updated:** 2019-01-29T17:26:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/692

Hi,

I have a metal equipped with `Raven Ridge Ryzen 5 2400G` and seems like it is not supporting ROCM at the moment officially. Then I tried to install amdgpu-pro drivers to enable the OpenCL platform for this APU but also reported failure. However, this model should support OpenCL, right?

```sh
$ uname -a
Linux ubuntu 4.18.0-10-generic #11-Ubuntu SMP Thu Oct 11 15:13:55 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
$ /opt/amdgpu-pro/bin/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
$ ./a.out
OpenCL error: clGetPlatformIDs(-1001)

```

My OS is Ubuntu 18.10 with latest Linux image driver 4.18.

Any root cause to lead to the failure? Thanks!
