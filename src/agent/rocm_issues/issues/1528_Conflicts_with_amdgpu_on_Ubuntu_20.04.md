# Conflicts with amdgpu on Ubuntu 20.04

> **Issue #1528**
> **状态**: closed
> **创建时间**: 2021-07-18T10:40:02Z
> **更新时间**: 2021-07-20T07:14:21Z
> **关闭时间**: 2021-07-20T07:14:21Z
> **作者**: jwarnier
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1528

## 描述

This output should be self-explanatory:
`jwarnier@amdrx6900xtu:~$ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-hwe-5.8-headers-5.8.0-59 xserver-xorg-video-fbdev xserver-xorg-video-nouveau xserver-xorg-video-qxl xserver-xorg-video-radeon xserver-xorg-video-vesa
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  comgr hip-base hip-doc hip-rocclr hip-samples hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libasan4 libcilkrts5 libdrm-dev libelf-dev libgcc-7-dev libgl-dev libglx-dev
  libllvm12.0-amdgpu libmpx2 libncurses5 libpthread-stubs0-dev libstdc++-7-dev libtinfo5 libubsan0 libx11-dev libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu llvm-amdgpu-12.0 llvm-amdgpu-12.0-dev
  llvm-amdgpu-12.0-runtime llvm-amdgpu-runtime mesa-common-dev openmp-extras rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake rocm-dbgapi rocm-debug-agent rocm-dev rocm-device-libs rocm-gdb
  rocm-opencl rocm-opencl-dev rocm-smi-lib rocm-utils rocminfo rocprofiler-dev roctracer-dev x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev zlib1g-dev
Suggested packages:
  libstdc++-7-doc libx11-doc libxcb-doc
The following NEW packages will be installed:
  comgr hip-base hip-doc hip-rocclr hip-samples hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libasan4 libcilkrts5 libdrm-dev libelf-dev libgcc-7-dev libgl-dev libglx-dev
  libllvm12.0-amdgpu libmpx2 libncurses5 libpthread-stubs0-dev libstdc++-7-dev libtinfo5 libubsan0 libx11-dev libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu llvm-amdgpu-12.0 llvm-amdgpu-12.0-dev
  llvm-amdgpu-12.0-runtime llvm-amdgpu-runtime mesa-common-dev openmp-extras rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake rocm-dbgapi rocm-debug-agent rocm-dev rocm-device-libs rocm-dkms
  rocm-gdb rocm-opencl rocm-opencl-dev rocm-smi-lib rocm-utils rocminfo rocprofiler-dev roctracer-dev x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev zlib1g-dev
0 upgraded, 56 newly installed, 0 to remove and 3 not upgraded.
Need to get 58,5 MB/173 MB of archives.
After this operation, 1.074 MB of additional disk space will be used.
Do you want to continue? [Y/n] 
Get:1 file:/var/opt/amdgpu-pro-local ./ libllvm12.0-amdgpu 1:12.0-1271047 [17,5 MB]
Get:2 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libasan4 amd64 7.5.0-6ubuntu2 [358 kB]
Get:3 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-12.0-runtime 1:12.0-1271047 [82,7 kB]
Get:4 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-runtime 1:12.0-1271047 [4.216 B]
Get:5 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-12.0 1:12.0-1271047 [11,6 MB]
Get:6 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu 1:12.0-1271047 [5.052 B]     
Get:7 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libcilkrts5 amd64 7.5.0-6ubuntu2 [42,7 kB]
Get:8 http://be.archive.ubuntu.com/ubuntu focal-updates/main amd64 libdrm-dev amd64 2.4.102-1ubuntu1~20.04.1 [126 kB]
Get:9 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-12.0-dev 1:12.0-1271047 [26,6 MB]
Get:10 http://be.archive.ubuntu.com/ubuntu focal-updates/main amd64 zlib1g-dev amd64 1:1.2.11.dfsg-2ubuntu1.2 [155 kB]
Get:11 http://be.archive.ubuntu.com/ubuntu focal/main amd64 libelf-dev amd64 0.176-1.1build1 [57,0 kB]
Get:12 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libubsan0 amd64 7.5.0-6ubuntu2 [126 kB]
Get:13 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libmpx2 amd64 8.4.0-3ubuntu2 [11,8 kB]
Get:14 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libgcc-7-dev amd64 7.5.0-6ubuntu2 [2.311 kB]
Get:15 http://be.archive.ubuntu.com/ubuntu focal/main amd64 xorg-sgml-doctools all 1:1.11-1 [12,9 kB]
Get:16 http://be.archive.ubuntu.com/ubuntu focal/main amd64 x11proto-dev all 2019.2-1ubuntu1 [594 kB]
Get:17 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 comgr amd64 2.0.0.40200-21 [41,2 MB]
Get:18 http://be.archive.ubuntu.com/ubuntu focal/main amd64 x11proto-core-dev all 2019.2-1ubuntu1 [2.620 B]
Get:19 http://be.archive.ubuntu.com/ubuntu focal/main amd64 libxau-dev amd64 1:1.0.9-0ubuntu1 [9.552 B]
Get:20 http://be.archive.ubuntu.com/ubuntu focal/main amd64 libxdmcp-dev amd64 1:1.1.3-0ubuntu1 [25,3 kB]
Get:21 http://be.archive.ubuntu.com/ubuntu focal/main amd64 xtrans-dev all 1.4.0-1 [68,9 kB]
Get:22 http://be.archive.ubuntu.com/ubuntu focal/main amd64 libpthread-stubs0-dev amd64 0.4-1 [5.384 B]
Get:23 http://be.archive.ubuntu.com/ubuntu focal/main amd64 libxcb1-dev amd64 1.14-2 [80,5 kB]
Get:24 http://be.archive.ubuntu.com/ubuntu focal-updates/main amd64 libglx-dev amd64 1.3.2-1~ubuntu0.20.04.1 [14,0 kB]
Get:25 http://be.archive.ubuntu.com/ubuntu focal-updates/main amd64 libgl-dev amd64 1.3.2-1~ubuntu0.20.04.1 [97,8 kB]
Get:26 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libtinfo5 amd64 6.2-0ubuntu2 [83,0 kB]
Get:27 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libncurses5 amd64 6.2-0ubuntu2 [96,9 kB]
Get:28 http://be.archive.ubuntu.com/ubuntu focal/universe amd64 libstdc++-7-dev amd64 7.5.0-6ubuntu2 [1.471 kB]
Get:29 http://be.archive.ubuntu.com/ubuntu focal-updates/main amd64 mesa-common-dev amd64 20.2.6-0ubuntu0.20.04.1 [1.148 kB]
Get:30 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hip-base amd64 4.2.21155.5900.40200-21 [215 kB]                                                                                          
Get:31 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hip-doc amd64 4.2.21155.5900.40200-21 [2.233 kB]                                                                                         
Get:32 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hsakmt-roct amd64 20210315.0.7.40200-21 [75,0 kB]                                                                                        
Get:33 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hsa-rocr-dev amd64 1.3.0.40200-21 [904 kB]                                                                                               
Get:34 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hip-rocclr amd64 4.2.21155.5900.40200-21 [6.741 kB]                                                                                      
Get:35 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hip-samples amd64 4.2.21155.5900.40200-21 [70,5 kB]                                                                                      
Get:36 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hsa-amd-aqlprofile amd64 1.0.0.40200-21 [91,5 kB]                                                                                        
Get:37 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 hsakmt-roct-dev amd64 20210315.0.7.40200-21 [28,3 kB]                                                                                    
Fetched 58,5 MB in 25s (2.341 kB/s)                                                                                                                                                                       
Extracting templates from packages: 100%
Selecting previously unselected package rock-dkms-firmware.
(Reading database ... 180183 files and directories currently installed.)
Preparing to unpack .../rock-dkms-firmware_1%3a4.2-21_all.deb ...
Unpacking rock-dkms-firmware (1:4.2-21) ...
dpkg: error processing archive /var/cache/apt/archives/rock-dkms-firmware_1%3a4.2-21_all.deb (--unpack):
 trying to overwrite '/usr/share/doc/amdgpu-dkms-firmware/LICENSE', which is also in package amdgpu-dkms-firmware 1:5.11.5.26-1271047
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/rock-dkms-firmware_1%3a4.2-21_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)`

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-07-20T07:14:21Z)

Hi @jwarnier 
Thanks for reaching out.
I certainly understood your problem.

We do not recommend keeping both amdgpu-pro and ROCm on the same machine. ROCm installs amdgpu as the base driver. A separate and additional installation of amdgpu-pro will break ROCm as it cannot handle both packages.
Hope this helps.
Thank you.

---
