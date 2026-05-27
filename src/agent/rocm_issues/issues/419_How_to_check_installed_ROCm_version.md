# How to check installed ROCm version?

> **Issue #419**
> **状态**: closed
> **创建时间**: 2018-05-17T02:35:14Z
> **更新时间**: 2025-11-10T16:43:34Z
> **关闭时间**: 2018-05-17T16:03:47Z
> **作者**: fpask
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/419

## 描述

Are there any way (preferably a one liner command) to print/confirm the installed version of ROCm? (1.8.0 or other versions)
I don't think I could find this detail in rocm-info.

---

## 评论 (7 条)

### 评论 #1 — djygithub (2018-05-17T11:51:19Z)

apt show rocm-libs -a
Package: rocm-libs
Version: 1.8.118
Priority: optional
Section: devel
Maintainer: Advanced Micro Devices Inc.
Installed-Size: 1,024 B
Depends: rocfft, rocrand, hipblas, rocblas
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 772 B
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack




---

### 评论 #2 — gstoner (2018-05-17T16:03:47Z)

rocminfo as well

---

### 评论 #3 — holyprince (2019-03-18T07:59:50Z)

I also want to check the installed ROCm version.
However, the apt command not found and the rocminfo like this :

\=====================
HSA System Attributes
\=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE
System Endianness:       LITTLE

\==========
HSA Agents
\==========
cpu info in Agent 1-8 ...
\*******
Agent 9
\*******
  Name:                    gfx906
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128
  Queue Min Size:          4096
  Queue Max Size:          131072
  Queue Type:              MULTI
  Node:                    8
  Device Type:             GPU
  Cache Info:
    L1:                      16KB
  Chip ID:                 26273
  Cacheline Size:          64
  Max Clock Frequency (MHz):1670
  BDFID:                   25344
  Compute Unit:            64
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64
  Workgroup Max Size:      1024
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888
    Dim[1]:                  1660945408
    Dim[2]:                  16711680
  Grid Max Size:           4294967295
  Waves Per CU:            40
  Max Work-item Per CU:    2560
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295
    Dim[1]:                  4294967295
    Dim[2]:                  4294967295
  Max number Of fbarriers Per Workgroup:32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    33538048KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx906
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Dimension:
        Dim[0]:                  67109888
        Dim[1]:                  1024
        Dim[2]:                  16777217
      Workgroup Max Size:      1024
      Grid Max Dimension:
        x                        4294967295
        y                        4294967295
        z                        4294967295
      Grid Max Size:           4294967295
      FBarrier Max Size:       32
\*** Done ***

How I can find the version number? Is it the runtime version: 1.1?
Thank you very much. @gstoner 

---

### 评论 #4 — djygithub (2019-03-18T20:41:40Z)

For centos75:
```
[rocm@tripper ~]$ yum info rocm-libs
Loaded plugins: fastestmirror, langpacks
Repodata is over 2 weeks old. Install yum-cron? Or run: yum makecache fast
Loading mirror speeds from cached hostfile
 * base: mirrors.xtom.com
 * epel: sjc.edge.kernel.org
 * extras: mirrors.xtom.com
 * updates: centos.sonn.com
Available Packages
Name        : rocm-libs
Arch        : x86_64
Version     : 2.1.96
Release     : 1
Size        : 2.7 k
Repo        : ROCm
Summary     : Radeon Open Compute (ROCm) Runtime software stack
License     : unknown
Description : DESCRIPTION
            : ===========
            :
            : This is an installer created using CPack (https://cmake.org). No additional installation instructions provided.

[rocm@tripper ~]$ rpm -qa | grep rocm
rocm-dev-2.1.96-1.x86_64
rocm-utils-2.1.96-1.x86_64
rocm-smi-1.0.0_100_g3cacdb9-1.x86_64
rocm-opencl-1.2.0-2019020220.x86_64
rocm-clang-ocl-0.4.0_7ce124f-1.x86_64
rocm-device-libs-0.0.1-1.x86_64
rocm-opencl-devel-1.2.0-2019020220.x86_64
procmail-3.22-36.el7_4.1.x86_64
rocminfo-1.0.0-1.x86_64
rocm-dkms-2.1.96-1.x86_64
[rocm@tripper ~]$ rpm -qa | grep hip
hip_doc-1.5.19025-1.x86_64
hip_hcc-1.5.19025-1.x86_64
hip_samples-1.5.19025-1.x86_64
hip_base-1.5.19025-1.x86_64
[rocm@tripper ~]$ rpm -qa | grep rock
rock-dkms-2.1-96.el7.noarch
[rocm@tripper ~]$
[rocm@tripper ~]$ dkms status
amdgpu, 2.1-96.el7, 3.10.0-862.el7.x86_64, x86_64: installed (original_module exists)
[rocm@tripper ~]$

```
For Ubuntu 16.04
```
rocm@prj47-rack-39:~$ dkms status
amdgpu, 2.1-96, 4.15.0-041500-generic, x86_64: installed
amdgpu, 2.1-96, 4.15.0-43-generic, x86_64: installed
iser, 4.0, 4.15.0-041500-generic, x86_64: installed
iser, 4.0, 4.15.0-43-generic, x86_64: installed
iser, 4.0, 4.15.0-45-generic, x86_64: installed
iser, 4.0, 4.4.0-141-generic, x86_64: installed
iser, 4.0, 4.4.0-142-generic, x86_64: installed
isert, 4.0, 4.15.0-041500-generic, x86_64: installed
isert, 4.0, 4.15.0-43-generic, x86_64: installed
isert, 4.0, 4.15.0-45-generic, x86_64: installed
isert, 4.0, 4.4.0-141-generic, x86_64: installed
isert, 4.0, 4.4.0-142-generic, x86_64: installed
kernel-mft-dkms, 4.9.0, 4.15.0-041500-generic, x86_64: installed
kernel-mft-dkms, 4.9.0, 4.15.0-43-generic, x86_64: installed
kernel-mft-dkms, 4.9.0, 4.15.0-45-generic, x86_64: installed
kernel-mft-dkms, 4.9.0, 4.4.0-141-generic, x86_64: installed
kernel-mft-dkms, 4.9.0, 4.4.0-142-generic, x86_64: installed
knem, 1.1.3.90mlnx1, 4.15.0-041500-generic, x86_64: installed
knem, 1.1.3.90mlnx1, 4.15.0-43-generic, x86_64: installed
knem, 1.1.3.90mlnx1, 4.15.0-45-generic, x86_64: installed
knem, 1.1.3.90mlnx1, 4.4.0-141-generic, x86_64: installed
knem, 1.1.3.90mlnx1, 4.4.0-142-generic, x86_64: installed
mlnx-ofed-kernel, 4.3, 4.15.0-041500-generic, x86_64: installed
mlnx-ofed-kernel, 4.3, 4.15.0-43-generic, x86_64: installed
mlnx-ofed-kernel, 4.3, 4.15.0-45-generic, x86_64: installed
mlnx-ofed-kernel, 4.3, 4.4.0-141-generic, x86_64: installed
mlnx-ofed-kernel, 4.3, 4.4.0-142-generic, x86_64: installed
srp, 4.0, 4.15.0-041500-generic, x86_64: installed
srp, 4.0, 4.15.0-43-generic, x86_64: installed
srp, 4.0, 4.15.0-45-generic, x86_64: installed
srp, 4.0, 4.4.0-141-generic, x86_64: installed
srp, 4.0, 4.4.0-142-generic, x86_64: installed
rocm@prj47-rack-39:~$ dpkg -l | grep rocm
ii  rocm-clang-ocl                         0.4.0-7ce124f                              amd64        OpenCL compilation with clang compiler.
ii  rocm-dev                               2.1.96                                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                       0.0.1                                      amd64        Radeon Open Compute - device libraries
ii  rocm-dkms                              2.1.96                                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl                            1.2.0-2019020110                           amd64        OpenCL/ROCm
ii  rocm-opencl-dev                        1.2.0-2019020110                           amd64        OpenCL/ROCm
ii  rocm-smi                               1.0.0-100-g3cacdb9                         amd64        System Management Interface for ROCm
ii  rocm-utils                             2.1.96                                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-validation-suite                  0.0.22                                     amd64        The ROCm Validation Suite – The ROCm Validation Suite is a system administrator and cluster manager's tool for detecting and troubleshooting common problems affecting AMD GPUs running in high performance computing environments, enabled using the ROCm software stack on a compatible platform.
ii  rocminfo                               1.0.0                                      amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool
rocm@prj47-rack-39:~$ dpkg -l | grep rock
ii  rock-dkms                              2.1-96                                     all          rock-dkms driver in DKMS format.
rocm@prj47-rack-39:~$ dpkg -l | grep hip
ii  hip_base                               1.5.19025                                  amd64        HIP: Heterogenous-computing Interface for Portability [BASE]
ii  hip_doc                                1.5.19025                                  amd64        HIP: Heterogenous-computing Interface for Portability [DOCUMENTATION]
ii  hip_hcc                                1.5.19025                                  amd64        HIP: Heterogenous-computing Interface for Portability [HCC]
ii  hip_samples                            1.5.19025                                  amd64        HIP: Heterogenous-computing Interface for Portability [SAMPLES]
ii  whiptail                               0.52.18-1ubuntu2                           amd64        Displays user-friendly dialog boxes from shell scripts
rocm@prj47-rack-39:~$ apt show rocm-libs
Package: rocm-libs
Version: 2.2.31
Priority: optional
Section: devel
Maintainer: Advanced Micro Devices Inc.
Installed-Size: 13.3 kB
Depends: rocfft, rocrand, hipblas, rocblas
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 768 B
APT-Sources: <http://repo.radeon.com/rocm/apt/debian xenial/main> amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack

rocm@prj47-rack-39:~$
```

---

### 评论 #5 — shailensobhee (2025-06-11T08:57:40Z)

If people keep bumping here for doing this, hope this is helpful. From the ROCm Manual, you can do this:
`sudo update-alternatives --display rocm`

Example output: 
```
rocm - auto mode
  link best version is /opt/rocm-6.3.1
  link currently points to /opt/rocm-6.3.1
  link rocm is /opt/rocm
/opt/rocm-6.3.1 - priority 633299994
```

So, looking at the second line, currently points, you'll see that I'm using ROCm 6.3.1. You will have multiple entries if you installed multiple versions of ROCm. 


---

### 评论 #6 — waltercool (2025-11-10T16:28:56Z)

Any way to obtain this information without being distro specific? Does ROCm offer any way to know the current version?

---

### 评论 #7 — kentrussell (2025-11-10T16:43:34Z)

cat /opt/rocm/.info/version
is OS-agnostic

---
