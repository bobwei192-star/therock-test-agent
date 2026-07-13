# Is Linux 4.13/Ubuntu 16.04.3 + Ryzen/Vega APU supported? Any fix to this invalid pointer error?

- **Issue #:** 303
- **State:** closed
- **Created:** 2018-01-18T18:36:59Z
- **Updated:** 2018-01-28T05:22:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/303

I followed https://github.com/RadeonOpenCompute/ROCm to install rocm on my machine.  I got this invalid pointer error when running anything (HelloWorld sample, hsa sample, clinfo).  Any help is appreciated.  My ultimate goal is to use OpenVX (amdovx).

Here is the error (I got the same error with clinfo/HelloWorld/vector_copy):

```bash
yang@VeGa:/opt/rocm/bin$ ./rocminfo 
*** Error in `./rocminfo': free(): invalid pointer: 0x0000000001908380 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7f2e067517e5]
/lib/x86_64-linux-gnu/libc.so.6(+0x8037a)[0x7f2e0675a37a]
/lib/x86_64-linux-gnu/libc.so.6(cfree+0x4c)[0x7f2e0675e53c]
/lib/x86_64-linux-gnu/libc.so.6(fclose+0x103)[0x7f2e06747363]
/opt/rocm/libhsakmt/lib/libhsakmt.so.1(+0xe7f4)[0x7f2e062b27f4]
/opt/rocm/libhsakmt/lib/libhsakmt.so.1(+0xfb05)[0x7f2e062b3b05]
/opt/rocm/libhsakmt/lib/libhsakmt.so.1(hsaKmtAcquireSystemProperties+0x3d)[0x7f2e062b516d]
/opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x2ace8)[0x7f2e06e50ce8]
/opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x2ae04)[0x7f2e06e50e04]
/opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x453ae)[0x7f2e06e6b3ae]
/opt/rocm/hsa/lib/libhsa-runtime64.so.1(+0x2bd2a)[0x7f2e06e51d2a]
./rocminfo(main+0x1a)[0x40132a]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7f2e066fa830]
./rocminfo(_start+0x29)[0x401759]

```

I felt this is an error due to HSA runtime not supporting Raven Ridge (Zen + Vega).  When will it be supported?

Here are the info of my machine:

```bash
yang@VeGa:~/Downloads/test_opencl_rocm$ lspci | grep -i AMD
00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15d0
00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Device 15d1
00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge
00:01.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 15d3
00:01.6 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 15d3
00:01.7 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 15d3
00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 00h-0fh) PCIe Dummy Host Bridge
00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 15db
00:08.2 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 15dc
00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 61)
00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15e8
00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15e9
00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15ea
00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15eb
00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15ec
00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15ed
00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15ee
00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Device 15ef
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega [Radeon Vega 8 Mobile] (rev c4)
04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device 15de
04:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Device 15df
04:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Device 15e0
04:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Device 15e1
04:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Device 15e3
05:00.0 SATA controller: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] (rev 51)
```

```bash
yang@VeGa:/opt/rocm/bin$ uname -mr && cat /etc/*release
4.13.0-26-generic x86_64
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

```

``` bash
yang@VeGa:~/Downloads/test_opencl_rocm$ gcc --version 
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.5) 5.4.0 20160609
```

```bash
yang@VeGa:~/Downloads/test_opencl_rocm$ lsmod | grep amd
edac_mce_amd           28672  0
amdkfd                262144  1
amd_iommu_v2           20480  1 amdkfd
amdgpu               3063808  46
amdttm                102400  1 amdgpu
amdkcl                 24576  3 amdttm,amdgpu,amdkfd
i2c_algo_bit           16384  1 amdgpu
drm_kms_helper        167936  1 amdgpu
drm                   356352  7 amdttm,amdgpu,amdkcl,drm_kms_helpe
```

```bash
yang@VeGa:~/Downloads/test_opencl_rocm$ dpkg -l roc*
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                                          Version                     Architecture                Description
+++-=============================================-===========================-===========================-===============================================================================================
ii  rock-dkms                                     1.7.60-ubuntu               all                         rock driver in DKMS format.
ii  rocm-clang-ocl                                0.2.0-83527dd               amd64                       OpenCL compilation with clang compiler.
ii  rocm-dev                                      1.7.60                      amd64                       Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                              0.0.1                       amd64                       Radeon Open Compute - device libraries
ii  rocm-dkms                                     1.7.60                      amd64                       Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl                                   1.2.0-2017121952            amd64                       OpenCL/ROCm
ii  rocm-opencl-dev                               1.2.0-2017121952            amd64                       OpenCL/ROCm
ii  rocm-smi                                      1.0.0-34-g23012d0           amd64                       System Management Interface for ROCm
ii  rocm-utils                                    1.7.60                      amd64                       Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                                      1.0.7                       amd64                       Radeon Open Compute (ROCm) Runtime rocminfo tool
```