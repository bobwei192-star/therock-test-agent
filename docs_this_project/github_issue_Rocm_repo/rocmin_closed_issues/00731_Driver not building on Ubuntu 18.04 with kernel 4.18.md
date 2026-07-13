# Driver not building on Ubuntu 18.04 with kernel 4.18

- **Issue #:** 731
- **State:** closed
- **Created:** 2019-03-13T09:37:20Z
- **Updated:** 2019-05-03T16:03:23Z
- **Assignees:** kentrussell
- **URL:** https://github.com/ROCm/ROCm/issues/731


My system is running Ubuntu 18.04 with default kernel (4.18), previously it ran fine on ROCm 2.1. Today I upgraded to ROCm 2.2 through apt and ROCK-dkms fails to build:

```
sudo apt install rocm-dkms
.
.
.
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms.0.crash'
Error! Bad return status for module build on kernel: 4.18.0-16-generic (x86_64)
Consult /var/lib/dkms/amdgpu/2.2-31/build/make.log for more information.
```

My GPU is a Radeon VII.
I tried reinstalling by following the instructions provided in the README.md, but to no avail. Downgrading doesn't appear to be an option as 2.1 doesn't seem to be in the apt repo anymore?

_edit:_ Attached the log file of the failing build.
[make.log](https://github.com/RadeonOpenCompute/ROCm/files/2960792/make.log)
