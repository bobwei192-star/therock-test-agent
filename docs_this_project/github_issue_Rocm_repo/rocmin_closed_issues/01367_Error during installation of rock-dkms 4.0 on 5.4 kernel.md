# Error during installation of rock-dkms 4.0 on 5.4 kernel

- **Issue #:** 1367
- **State:** closed
- **Created:** 2021-01-24T17:06:27Z
- **Updated:** 2021-05-31T17:53:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1367

I tried on several machines, guest VM or bare-metal, and installation is failing on Ubuntu 20.04.1 with 5.4 kernel which should be supported after going through all the previous steps. There appears to be a build error which informs to look at log file:
I will attach the log file if necessary: 

----------
apt install rocm-dkms -y
----------

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...

....

 - Installation
   - Installing to /lib/modules/5.4.0-42-generic/updates/dkms/

depmod....

DKMS: install completed.
Building initial module for 5.8.0-40-generic
Error! Bad return status for module build on kernel: 5.8.0-40-generic (x86_64)
Consult /var/lib/dkms/amdgpu/4.0-23/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
Setting up rocm-smi (1.0.0-206-rocm-rel-4.0-23-ge39c0e2) ...
Setting up xtrans-dev (1.4.0-1) ...

....


Setting up rocm-clang-ocl (0.5.0.64-rocm-rel-4.0-23-50fb51a) ...
Setting up rocm-utils (4.0.0.40000-23) ...
Setting up rocm-dev (4.0.0.40000-23) ...
Processing triggers for libc-bin (2.31-0ubuntu9.1) ...
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
