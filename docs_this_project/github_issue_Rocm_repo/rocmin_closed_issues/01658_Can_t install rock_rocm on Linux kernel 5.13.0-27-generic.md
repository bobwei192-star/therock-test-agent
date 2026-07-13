# Can't install rock/rocm on Linux kernel 5.13.0-27-generic

- **Issue #:** 1658
- **State:** closed
- **Created:** 2022-01-19T22:05:20Z
- **Updated:** 2022-02-21T08:32:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/1658

I just tried to install rocm on a brand new computer with freshly installed OS (Ubuntu 20.04.3), and encountered repeated failures including the the following:

```bpickrel@home-tower:~$ sudo apt-get install amdgpu-dkms
Reading package lists... Done
Building dependency tree
Reading state information... Done
amdgpu-dkms is already the newest version (1:5.11.32.40502-1350682).
0 upgraded, 0 newly installed, 0 to remove and 4 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] Y
Setting up amdgpu-dkms (1:5.11.32.40502-1350682) ...
Removing old amdgpu-5.11.32-1350682 DKMS files...

------------------------------
Deleting module version: 5.11.32-1350682
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-5.11.32-1350682 DKMS files...
Building for 5.13.0-27-generic
Building for architecture x86_64
Building initial module for 5.13.0-27-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms.0.crash'
Error! Bad return status for module build on kernel: 5.13.0-27-generic (x86_64)
Consult /var/lib/dkms/amdgpu/5.11.32-1350682/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```


The installation process for ver 4.5 apparently does not support the default linux kernel 5.13.0-27-generic.  (Apparently the previous version rocm 4.3 does not have this issue.)


