#  ImportError: librocblas.so.0: cannot open shared object file: No such file or directory

- **Issue #:** 1637
- **State:** closed
- **Created:** 2021-12-12T19:58:35Z
- **Updated:** 2021-12-20T11:55:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/1637

Hello, I get this error when I want to use tenserflow rocm
`    from tensorflow.python._pywrap_tensorflow_internal import *
ImportError: librccl.so.1: cannot open shared object file: No such file or directory
`

but I don't have this file in `opt/rocm/lib`

```
cmake                          libhipblas.so           libhip_hcc.so        libhiprtc.so        libmcwamp_hsa.so  librocblas.so.0         librocfft-device.so.0        librocfft.so.0        librocr_debug_agent64.so
libclang_rt.builtins-x86_64.a  libhipblas.so.0         libhip_hcc_static.a  libmcwamp_atomic.a  libmcwamp.so      librocblas.so.2.2.11.0  librocfft-device.so.0.9.4.0  librocfft.so.0.9.4.0
libhc_am.so                    libhipblas.so.0.12.6.0  libhiprand.so        libmcwamp_cpu.so    librocblas.so     librocfft-device.so     librocfft.so                 librocrand.so
```

And when I try to install rocm-libs I get this error

```
sudo apt install rocm-libs
[sudo] password for server: 
Sorry, try again.
[sudo] password for server: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-libs is already the newest version (2.6.22).
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.
2 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] Y
Setting up rock-dkms (2.6-22) ...
Removing old amdgpu-2.6-22 DKMS files...

------------------------------
Deleting module version: 2.6-22
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-2.6-22 DKMS files...
Building for 5.4.0-91-generic
Building for architecture x86_64
Building initial module for 5.4.0-91-generic
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: aclocal --force 
autoreconf: configure.ac: tracing
autoreconf: configure.ac: not using Libtool
autoreconf: running: /usr/bin/autoconf --force
autoreconf: running: /usr/bin/autoheader --force
autoreconf: configure.ac: not using Automake
autoreconf: Leaving directory `.'
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms.0.crash'
Error! Bad return status for module build on kernel: 5.4.0-91-generic (x86_64)
Consult /var/lib/dkms/amdgpu/2.6-22/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
No apport report written because the error message indicates its a followup error from a previous failure.
                                                                                                          dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

here are the contents of `/var/crash/rock-dkms.0.crash`

```
ProblemType: Package
DKMSBuildLog:
 DKMS make.log for amdgpu-2.6-22 for kernel 5.4.0-91-generic (x86_64)
 Sun 12 Dec 2021 07:45:54 PM UTC
 make: Entering directory '/usr/src/linux-headers-5.4.0-91-generic'
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_drm.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/main.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/symbols.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/sched_main.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_memory.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_drv.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_device.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_tt.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/ttm/backport/backport.h:7,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_memory.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/sched_fence.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/../include/../backport/backport.h:11,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_drv.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/sched_entity.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/../include/../backport/backport.h:11,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu/amdgpu_device.o] Error 1
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdgpu] Error 2
 make[1]: *** Waiting for unfinished jobs....
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_fence.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/ttm/backport/backport.h:7,
                  from <command-line>:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/ttm/ttm_tt.o] Error 1
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.6-22/build/ttm] Error 2
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_fence_array.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_kthread.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_io.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_reservation.o
   CC [M]  /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.o
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_reservation.c:33:
 /var/lib/dkms/amdgpu/2.6-22/build/include/kcl/kcl_reservation.h:4:10: fatal error: linux/reservation.h: No such file or directory
     4 | #include <linux/reservation.h>
       |          ^~~~~~~~~~~~~~~~~~~~~
 compilation terminated.
 make[2]: *** [scripts/Makefile.build:270: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_reservation.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
   LD [M]  /var/lib/dkms/amdgpu/2.6-22/build/scheduler/amd-sched.o
 /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
 /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.c:199:83: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
   199 |  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed",_kcl_pcie_link_speed_stub);
       |                                                                                   ^~~~~~~~~~~~~~~~~~~~~~~~~
 In file included from /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_pci.c:3:
 /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl/kcl_common.h:22:63: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
    22 | static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
       |                                                         ~~~~~~^~~~~~~
 make[1]: *** [scripts/Makefile.build:519: /var/lib/dkms/amdgpu/2.6-22/build/amd/amdkcl] Error 2
 make: *** [Makefile:1762: /var/lib/dkms/amdgpu/2.6-22/build] Error 2
 make: Leaving directory '/usr/src/linux-headers-5.4.0-91-generic'
DKMSKernelVersion: 5.4.0-91-generic
Date: Sun Dec 12 19:45:57 2021
Package: rock-dkms 2.6-22
PackageVersion: 2.6-22
SourcePackage: rock-dkms
Title: rock-dkms 2.6-22: amdgpu kernel module failed to build
```

Here is my configuration:
- kernel: 5.4.0-91-generic
- cpu: Intel(R) Core(TM) i5-9600K CPU @ 3.70GHz
- gpu: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
- os: Ubuntu 20.04.3 LTS
