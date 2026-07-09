# [Issue]: Error while installing rocm-bandwidth-test package on ubuntu 22.04 with rocm 6.0.2

- **Issue #:** 3415
- **State:** closed
- **Created:** 2024-07-12T14:54:16Z
- **Updated:** 2024-08-15T14:36:42Z
- **Labels:** ROCm 6.0.0, AMD Instinct MI210
- **URL:** https://github.com/ROCm/ROCm/issues/3415

### Problem Description

rocm-bandwidth-test package is having issues while installing 

ERROR Details
=========================================================================
testsystem:/opt/rocm/bin$ sudo apt install rocm-bandwidth-test
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libevent-2.1-7 libevent-dev libevent-extra-2.1-7 libevent-openssl-2.1-7 libevent-pthreads-2.1-7 libpmix-dev libpmix2
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  hsa-rocr rocm-core
The following NEW packages will be installed:
  hsa-rocr rocm-bandwidth-test rocm-core
0 upgraded, 3 newly installed, 0 to remove and 120 not upgraded.
Need to get 893 kB of archives.
After this operation, 8,965 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 https://repo.radeon.com/rocm/apt/6.0.2 jammy/main amd64 rocm-core amd64 6.0.2.60002-115~22.04 [9,034 B]
Get:2 https://repo.radeon.com/rocm/apt/6.0.2 jammy/main amd64 hsa-rocr amd64 1.12.0.60002-115~22.04 [823 kB]
Get:3 https://repo.radeon.com/rocm/apt/6.0.2 jammy/main amd64 rocm-bandwidth-test amd64 1.4.0.60002-115~22.04 [60.2 kB]
Fetched 893 kB in 1s (795 kB/s)
Selecting previously unselected package rocm-core.
(Reading database ... 310309 files and directories currently installed.)
Preparing to unpack .../rocm-core_6.0.2.60002-115~22.04_amd64.deb ...
Unpacking rocm-core (6.0.2.60002-115~22.04) ...
dpkg: error processing archive /var/cache/apt/archives/rocm-core_6.0.2.60002-115~22.04_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-6.0.2/.info/version', which is also in package rocm-core6.0.2 6.0.2.60002-115~22.04
Selecting previously unselected package hsa-rocr.
Preparing to unpack .../hsa-rocr_1.12.0.60002-115~22.04_amd64.deb ...
Unpacking hsa-rocr (1.12.0.60002-115~22.04) ...
dpkg: error processing archive /var/cache/apt/archives/hsa-rocr_1.12.0.60002-115~22.04_amd64.deb (--unpack):
 trying to overwrite '/opt/rocm-6.0.2/lib/libhsa-runtime64.so.1.12.60002', which is also in package hsa-rocr6.0.2 1.12.0.60002-115~22.04
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Selecting previously unselected package rocm-bandwidth-test.
Preparing to unpack .../rocm-bandwidth-test_1.4.0.60002-115~22.04_amd64.deb ...
Unpacking rocm-bandwidth-test (1.4.0.60002-115~22.04) ...
Errors were encountered while processing:
 /var/cache/apt/archives/rocm-core_6.0.2.60002-115~22.04_amd64.deb
 /var/cache/apt/archives/hsa-rocr_1.12.0.60002-115~22.04_amd64.deb
needrestart is being skipped since dpkg has failed
E: Sub-process /usr/bin/dpkg returned an error code (1)



### Operating System

ubuntu 22.04

### CPU

AMD EYPC

### GPU

AMD Instinct MI210

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

sudo apt install rocm-bandwidth-test

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_