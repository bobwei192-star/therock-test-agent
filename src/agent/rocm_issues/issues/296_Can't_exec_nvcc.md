# Can't exec "nvcc"

> **Issue #296**
> **状态**: closed
> **创建时间**: 2018-01-04T09:53:49Z
> **更新时间**: 2018-01-22T16:47:55Z
> **关闭时间**: 2018-01-15T15:34:14Z
> **作者**: greatken999
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/296

## 描述

I installed rocm1.7  and run hipconfig ,get this error info:
HIP version  : 1.4.17494

== hipconfig
HIP_PATH     : /opt/rocm/hip
HIP_PLATFORM : nvcc
CPP_CONFIG   :  -D__HIP_PLATFORM_NVCC__=  -I/opt/rocm/hip/include -I/usr/local/cuda/include

== nvcc
Can't exec "nvcc": 没有那个文件或目录 at /opt/rocm/hip/bin/hipconfig line 144.

=== Environment Variables
PATH=/opt/rocm/hcc/bin:/opt/rocm/hip/bin:/home/ken/bin:/home/ken/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/rocm/bin/
HIP_PATH=/opt/rocm/hip
HCC_HOME=/opt/rocm/hcc

== Linux Kernel
Hostname     : ken-B250M-D3H
Linux ken-B250M-D3H 4.13.0-21-generic #24~16.04.1-Ubuntu SMP Mon Dec 18 19:39:31 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.3 LTS
Release:	16.04
Codename:	xenial


this error  look is line  70 of hipconfig  programe:
if (not defined $HIP_PLATFORM) {
     70     $NAMDGPUNODES=`cat /sys/class/kfd/kfd/topology/nodes/*/properties 2>/dev/null | grep -c 'simd_count [1-9]'`;
     71 
     72     if ($NAMDGPUNODES > 0) {
     73         $HIP_PLATFORM = "hcc"
     74     } else {
     75         $HIP_PLATFORM = "nvcc";
     76     }
     77 }
cat /sys/class/kfd/kfd/topology/nodes/*/properties 2>/dev/null | grep -c 'simd_count [1-9]'
$NAMDGPUNODES =0


lspci info:
lspci |grep VGA
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)

my GPU is a xfx vega64 gpu.

---

## 评论 (4 条)

### 评论 #1 — tingxingdong (2018-01-05T22:28:07Z)

You have an AMD card, and of course has no an nvidia compiler. 

---

### 评论 #2 — greatken999 (2018-01-06T09:34:30Z)

right thing is:
 $HIP_PLATFORM = "hcc" if use amd card.


---

### 评论 #3 — gstoner (2018-01-15T15:34:14Z)

We do not use NVCC on AMD GPU card, this path on HIP is only used when you have NVIDIA GPU install and HIP run on top Cuda driver and use NVCC

---

### 评论 #4 — RaymonSHan (2018-01-22T16:47:55Z)

same thing to me 

**# for hipconfig**
raymon@raymonR7:/opt/rocm/hip/bin$ ./hipconfig
HIP version  : 1.3.0

== hipconfig
HIP_PATH     : /opt/rocm/hip/bin
HIP_PLATFORM : nvcc
CPP_CONFIG   :  -D__HIP_PLATFORM_NVCC__=  -I/opt/rocm/hip/bin/include -I/usr/local/cuda/include

== nvcc
Can't exec "nvcc": No such file or directory at ./hipconfig line 143.


**# for clinfo**
raymon@raymonR7:~/solution/qttest$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (2482.3)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     Ellesmere
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2482.3)
  Driver Version                                  2482.3
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         Radeon RX 580 Series
  Device Topology (AMD)                           PCI-E, 28:00.0
  Max compute units                               36
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1

something MUST change, the hipInfo is corrent days before, but now it report SIGSEGV now.


If set 
HIP_PLATFORM=hcc
not # HIP_PLATFORM=$(shell $(HIP_PATH)/bin/hipconfig --platform)

it report in link

/opt/rocm/hip/bin/hipcc -Wl,-rpath,/home/raymon/Qt5.6.3/5.6.3/gcc_64/lib -o qttest main.o mainwindow.o hiptest.o moc_mainwindow.o   -L/home/raymon/Qt5.6.3/5.6.3/gcc_64/lib -lQt5Widgets -L/usr/lib64 -lQt5Gui -lQt5Core -lGL -lpthread 
Died at /opt/rocm/hip/bin/hipcc line 415.
No valid AMD GPU target was either specified or found. Please specify a valid target using --amdgpu-target=Makefile:220: recipe for target 'qttest' failed

but it is ok days before.





---
