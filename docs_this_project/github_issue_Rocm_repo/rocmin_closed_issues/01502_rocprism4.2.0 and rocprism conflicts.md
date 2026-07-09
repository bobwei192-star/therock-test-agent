# rocprism4.2.0 and rocprism conflicts

- **Issue #:** 1502
- **State:** closed
- **Created:** 2021-06-23T17:00:02Z
- **Updated:** 2021-07-27T11:53:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/1502

Hi,

   got a conflict that I can't seem to resolve.  Maybe I misinterpret the versioning. I can install rocprim fine, but installing rocprim4.2.0 gives me the below conflicts. After that, there is no way of working around it. 

    Why this conflict between the latest and the specific version? 

    I'd really would like to just install the kernel modules rocm-dkms on the nodes and let the rest be available in a modules environment, e.g.  /cm/shared/apps/amd/rocm/<version>.    Are the packages relocatable? Any suggestions on how to accomplish this with AMD ROCm appreciated.  

`root@n004:~# apt install rocprim4.2.0
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  comgr4.2.0 hip-base4.2.0 hip-rocclr4.2.0 hsa-rocr-dev4.2.0 hsakmt-roct4.2.0 llvm-amdgpu4.2.0 rocminfo4.2.0
The following NEW packages will be installed:
  comgr4.2.0 hip-base4.2.0 hip-rocclr4.2.0 hsa-rocr-dev4.2.0 hsakmt-roct4.2.0 llvm-amdgpu4.2.0 rocminfo4.2.0
  rocprim4.2.0
0 upgraded, 8 newly installed, 0 to remove and 2 not upgraded.
Need to get 0 B/581 MB of archives.
After this operation, 397 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
(Reading database ... 381851 files and directories currently installed.)
Preparing to unpack .../0-comgr4.2.0_2.0.0.40200-21_amd64.deb ...
Unpacking comgr4.2.0 (2.0.0.40200-21) ...
dpkg: error processing archive /tmp/apt-dpkg-install-MOKPJd/0-comgr4.2.0_2.0.0.40200-21_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-4.2.0/include/amd_comgr.h', which is also in package comgr 2.0.0.40200-21
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Preparing to unpack .../1-hip-base4.2.0_4.2.21155.5900.40200-21_amd64.deb ...
Unpacking hip-base4.2.0 (4.2.21155.5900.40200-21) ...
dpkg: error processing archive /tmp/apt-dpkg-install-MOKPJd/1-hip-base4.2.0_4.2.21155.5900.40200-21_amd64.deb (--unpa
ck):
 trying to overwrite '/opt/rocm-4.2.0/hip/bin/.hipVersion', which is also in package hip-base 4.2.21155.5900.40200-21
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Preparing to unpack .../2-hsakmt-roct4.2.0_20210315.0.7.40200-21_amd64.deb ...
Unpacking hsakmt-roct4.2.0 (20210315.0.7.40200-21) ...
dpkg: error processing archive /tmp/apt-dpkg-install-MOKPJd/2-hsakmt-roct4.2.0_20210315.0.7.40200-21_amd64.deb (--unp
ack):
 trying to overwrite '/opt/rocm-4.2.0/lib/libhsakmt.so.1.0.40200', which is also in package hsakmt-roct 20210315.0.7.
40200-21
Preparing to unpack .../3-hsa-rocr-dev4.2.0_1.3.0.40200-21_amd64.deb ...
Unpacking hsa-rocr-dev4.2.0 (1.3.0.40200-21) ...
dpkg: error processing archive /tmp/apt-dpkg-install-MOKPJd/3-hsa-rocr-dev4.2.0_1.3.0.40200-21_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-4.2.0/include/hsa/Brig.h', which is also in package hsa-rocr-dev 1.3.0.40200-21
No apport report written because MaxReports is reached already
                                                              dpkg-deb: error: paste subprocess was killed by signal 
(Broken pipe)
Preparing to unpack .../4-rocminfo4.2.0_1.0.0.40200-21_amd64.deb ...
Unpacking rocminfo4.2.0 (1.0.0.40200-21) ...
dpkg: error processing archive /tmp/apt-dpkg-install-MOKPJd/4-rocminfo4.2.0_1.0.0.40200-21_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-4.2.0/bin/rocm_agent_enumerator', which is also in package rocminfo 1.0.0.40200-21
No apport report written because MaxReports is reached already
                                                              Preparing to unpack .../5-llvm-amdgpu4.2.0_12.0.0.21161
.40200_amd64.deb ...
Unpacking llvm-amdgpu4.2.0 (12.0.0.21161.40200) ...
dpkg: error processing archive /tmp/apt-dpkg-install-MOKPJd/5-llvm-amdgpu4.2.0_12.0.0.21161.40200_amd64.deb (--unpack
):
 trying to overwrite '/opt/rocm-4.2.0/llvm/bin/bugpoint', which is also in package llvm-amdgpu 12.0.0.21161.40200
No apport report written because MaxReports is reached already
                                                              dpkg-deb: error: paste subprocess was killed by signal 
(Broken pipe)
Preparing to unpack .../6-hip-rocclr4.2.0_4.2.21155.5900.40200-21_amd64.deb ...
Unpacking hip-rocclr4.2.0 (4.2.21155.5900.40200-21) ...
dpkg: error processing archive /tmp/apt-dpkg-install-MOKPJd/6-hip-rocclr4.2.0_4.2.21155.5900.40200-21_amd64.deb (--un
pack):
 trying to overwrite '/opt/rocm-4.2.0/hip/lib/.hipInfo', which is also in package hip-rocclr 4.2.21155.5900.40200-21
No apport report written because MaxReports is reached already
                                                              dpkg-deb: error: paste subprocess was killed by signal 
(Broken pipe)
Selecting previously unselected package rocprim4.2.0.
Preparing to unpack .../7-rocprim4.2.0_2.10.9.40200-21_amd64.deb ...
Unpacking rocprim4.2.0 (2.10.9.40200-21) ...
Errors were encountered while processing:
 /tmp/apt-dpkg-install-MOKPJd/0-comgr4.2.0_2.0.0.40200-21_amd64.deb
 /tmp/apt-dpkg-install-MOKPJd/1-hip-base4.2.0_4.2.21155.5900.40200-21_amd64.deb
 /tmp/apt-dpkg-install-MOKPJd/2-hsakmt-roct4.2.0_20210315.0.7.40200-21_amd64.deb
 /tmp/apt-dpkg-install-MOKPJd/3-hsa-rocr-dev4.2.0_1.3.0.40200-21_amd64.deb
 /tmp/apt-dpkg-install-MOKPJd/4-rocminfo4.2.0_1.0.0.40200-21_amd64.deb
 /tmp/apt-dpkg-install-MOKPJd/5-llvm-amdgpu4.2.0_12.0.0.21161.40200_amd64.deb
 /tmp/apt-dpkg-install-MOKPJd/6-hip-rocclr4.2.0_4.2.21155.5900.40200-21_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
root@n004:~#`