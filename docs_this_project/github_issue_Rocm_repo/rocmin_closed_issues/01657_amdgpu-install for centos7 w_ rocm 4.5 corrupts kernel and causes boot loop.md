# amdgpu-install for centos7 w/ rocm 4.5 corrupts kernel and causes boot loop

- **Issue #:** 1657
- **State:** closed
- **Created:** 2022-01-19T18:15:15Z
- **Updated:** 2022-07-21T12:39:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/1657

I tried to use the amdgpu-install script for a centos7.9 system running the 3.10.0-1160.49.1.el7.x86_64 kernel with `amdgpu-install --usecase=hiplibsdk,openclsdk,rocm`. The host has a Vega56 GPU installed. The generated amdgpu kernel module causes a boot failure, with an endless boot cycle. Adding the boot option `modprobe.blacklist=amdgpu` allows the kernel to boot, but uninstalling all packages with `amdgpu-uninstall` does not fix the boot issue. A full kernel deletion and re-installation is necessary.

If I install with `amdgpu-install --usecase=hiplibsdk,openclsdk,rocm --no-dkms`, it is able to boot, but the installation seems broken. Only the OpenCL device for the Vega56 GPU is seen, and rocm-smi shows errors:
```
> rocm-smi
Failed to get "domain" properity from properties files for kfd node 2.
rsmi_init() failed
ERROR:root:ROCm SMI returned 8 (the expected value is 0)
```

I previously had rocm4.2 installed and running without issue.