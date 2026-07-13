# Please support Ubuntu 20.04.5 LTS with 5.14 Kernel

- **Issue #:** 1809
- **State:** closed
- **Created:** 2022-09-20T06:51:19Z
- **Updated:** 2023-11-27T16:36:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1809

Hi, I get errors when installing on Ubuntu 20.04.5 LTS with Kernel 5.14.0-1051-oem (I know it is not officially supported yet). 

`amdgpu-install --usecase=dkms`

gives

```
Package linux-modules-extra-5.14.0-1051-oem is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'linux-modules-extra-5.14.0-1051-oem' has no installation candidate
```

Older versions of amdgpu-install run further but fail during compiling with a different error.
Thanks, would be great to try our networks for medical image analysis on AMD hardware and support that for our users. If support for Ubuntu 20.04.5 is planned for the next release, do you have a time line for that? Or should I try downgrading the kernel?