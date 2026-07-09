# rocm-dkms fails to build on clean xenial 

- **Issue #:** 329
- **State:** closed
- **Created:** 2018-02-07T19:39:58Z
- **Updated:** 2018-03-17T13:40:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/329

Hello 

I tried to build rocm-dkms on diskless ubuntu. It is a clean debootstrapped rootfs.

Systeminformation:
```
root@1:~# cat /etc/*release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.3 LTS"
NAME="Ubuntu"
VERSION="16.04.3 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.3 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial

root@1:~# uname -a
Linux 1 4.11.0-14-generic #20~16.04.1-Ubuntu SMP Wed Aug 9 09:06:22 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

root@1:~# gcc --version
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.6) 5.4.0 20160609
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```

I followed this instructions:
https://rocm.github.io/ROCmInstall.html

The buildlog is here:

```
----------------------- SNIP -------------------------------------
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_amdkfd_gpuvm.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_cgs.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../scheduler/gpu_scheduler.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_job.o
  CC [M]  /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.o
/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.c: In function 'acp_hw_init':
/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.c:330:4: error: 'DW_I2S_QUIRK_16BIT_IDX_OVERRIDE' undeclared (first use in this function)
    DW_I2S_QUIRK_16BIT_IDX_OVERRIDE;
    ^
/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.c:330:4: note: each undeclared identifier is reported only once for each function it appears in
scripts/Makefile.build:294: recipe for target '/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.o' failed
make[2]: *** [/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/amdgpu_acp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
scripts/Makefile.build:567: recipe for target '/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu] Error 2
Makefile:1526: recipe for target '_module_/var/lib/dkms/rock/1.7.60-ubuntu/build' failed
make: *** [_module_/var/lib/dkms/rock/1.7.60-ubuntu/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.11.0-14-generic'
```

Whats wrong with this one?

Thanks
derdigge