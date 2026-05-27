# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

> **Issue #415**
> **状态**: closed
> **创建时间**: 2018-05-13T21:29:43Z
> **更新时间**: 2019-10-23T03:25:21Z
> **关闭时间**: 2018-06-13T19:54:46Z
> **作者**: minzak
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/415

## 描述

I'm use Debian 9 with 4.16. kernel with Nitro+ RX570

```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
sudo apt update
sudo apt-get install -y rocm-opencl-dev rocm-dkms rocminfo
sudo usermod -a -G video $LOGNAME 

GRUB_CMDLINE_LINUX_DEFAULT="selinux=0 amdgpu.vm_fragment_size=9 nmi_watchdog=0 pti=off 3 spectre_v2=off nospectre_v2 nopti retp=0 ibrs=0 ibpb=0"
update-initramfs -u
update-grub
```
```
root@z820:~# lspci | grep -i AMD
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev ef)
05:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580]
root@z820:~#
```

All installed, but need make correct PATHs and etc.
What should i do also?

```
root@z820:/opt/rocm/bin# ./rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
```

```
root@z820:/opt/rocm/bin#
root@z820:/opt/rocm/opencl/bin/x86_64# ./clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted
```


```
root@z820:/opt/rocm# tree -d
.
├── bin
├── hcc
│   ├── bin
│   ├── include
│   │   ├── clang-c
│   │   ├── experimental
│   │   │   └── impl
│   │   ├── llvm
│   │   │   └── Target
│   │   │       └── AMDGPU
│   │   │           └── Disassembler
│   │   └── llvm-c
│   ├── lib
│   │   ├── clang
│   │   │   └── 7.0.0
│   │   │       ├── include
│   │   │       │   ├── cuda_wrappers
│   │   │       │   ├── sanitizer
│   │   │       │   └── xray
│   │   │       ├── lib
│   │   │       │   └── linux
│   │   │       └── share
│   │   └── cmake
│   │       └── hcc
│   ├── libexec
│   ├── rocdl
│   │   ├── hc
│   │   ├── irif
│   │   ├── lib
│   │   ├── ockl
│   │   ├── oclc
│   │   ├── ocml
│   │   └── opencl
│   └── share
│       ├── clang
│       ├── man
│       │   └── man1
│       ├── opt-viewer
│       ├── scan-build
│       └── scan-view
├── hip
│   ├── bin
│   ├── cmake
│   │   └── FindHIP
│   ├── docs
│   │   └── docs
│   │       └── RuntimeAPI
│   │           └── html
│   │               └── search
│   ├── include
│   │   └── hip
│   │       ├── hcc_detail
│   │       │   └── cuda
│   │       └── nvcc_detail
│   ├── lib
│   │   └── cmake
│   │       └── hip
│   └── samples
│       ├── 0_Intro
│       │   ├── bit_extract
│       │   ├── hcc_dialects
│       │   ├── module_api
│       │   ├── module_api_global
│       │   └── square
│       ├── 1_Utils
│       │   ├── hipBusBandwidth
│       │   ├── hipCommander
│       │   │   └── perf
│       │   │       └── scripts
│       │   ├── hipDispatchLatency
│       │   └── hipInfo
│       └── 2_Cookbook
│           ├── 0_MatrixTranspose
│           ├── 10_inline_asm
│           ├── 11_texture_driver
│           ├── 12_cmake_hip_add_executable
│           ├── 1_hipEvent
│           ├── 2_Profiler
│           ├── 3_shared_memory
│           ├── 4_shfl
│           ├── 5_2dshfl
│           ├── 6_dynamic_shared
│           ├── 7_streams
│           ├── 8_peer2peer
│           └── 9_unroll
├── hsa
│   ├── bin
│   ├── include
│   │   └── hsa
│   ├── lib
│   └── sample
├── hsa-amd-aqlprofile
│   └── lib
├── include
│   ├── hcc -> /opt/rocm/hcc/include
│   ├── hip -> /opt/rocm/hip/include/hip
│   ├── hsa -> ../hsa/include/hsa
│   └── libhsakmt -> ../libhsakmt/include/libhsakmt
├── lib
│   └── cmake
│       ├── hcc -> /opt/rocm/hcc/lib/cmake/hcc
│       └── hip -> /opt/rocm/hip/lib/cmake/hip
├── libhsakmt
│   ├── include
│   │   └── libhsakmt
│   │       └── linux
│   └── lib
└── opencl
    ├── bin
    │   └── x86_64
    ├── include
    │   └── CL
    └── lib
        └── x86_64
            └── bitcode

115 directories

root@z820:/opt/rocm#
```


---

## 评论 (29 条)

### 评论 #1 — leophys (2018-05-18T08:38:50Z)

Same issue here.
Platform: Ubuntu 16.04 on Xen with pci passthrough
```
# lspci
00:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii PRO [Radeon R9 290]
# uname -a 
Linux cracker 4.13.16-041316-generic #201711240901 SMP Fri Nov 24 09:02:42 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```
Did the same as reported above. Added `/opt/rocm/bin` to `$PATH`.
Same error output as above:
```
# clinfo
Number of platforms                               0
# rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
```

---

### 评论 #2 — kochd (2018-05-22T09:37:32Z)

Same here Linux 4.17.0-rc5

<pre>
[101515.255337] Parsing CRAT table with 1 nodes
[101515.255341] Ignoring ACPI CRAT on non-APU system
[101515.255343] Virtual CRAT table created for CPU
[101515.255343] Parsing CRAT table with 1 nodes
[101515.255344] Creating topology SYSFS entries
[101515.255354] Topology: Add CPU node
[101515.255355] Finished initializing topology
[101515.255402] kfd kfd: Initialized module
</pre>

---

### 评论 #3 — gstoner (2018-06-03T14:26:39Z)


You know the source code for ROCm Info is here https://github.com/RadeonOpenCompute/rocminfo 

Line 900 it failure on getting System Info
 // Acquire and display system information
  system_info_t sys_info;

@kochd  @ leophys you are both using custom kernel driver,  you mostly seeing  an issue that the driver did not load correctly 

---

### 评论 #4 — sunway513 (2018-06-04T01:29:01Z)

Firstly check if the KFD module is successfully loaded:
`lsmod | grep kfd`
Then try if the information can be retrieved correctly with root access:
`sudo /opt/rocm/bin/rocminfo`

---

### 评论 #5 — jedwards-AMD (2018-06-04T14:39:13Z)

As indicated by the above post, this is usually an issue with the amdkfd or amdgpu driver loading and exposing the device. Things to check are:
.
'dmesg | grep amdgpu'
'dmesg | grep amdkfd'

Also, check that the user you are running as is part of the "video" group and that the /dev/kfd device is available and has 666 permissions. I also suggest that you run this command and post any errors:
'strace ./clinfo'.

This should indicate if there are any configuration errors with you system.

---

### 评论 #6 — expertcloudconsulting (2018-06-08T08:21:41Z)

Yes its amdgpu driver loaded by default with RX570 -what next please to resolve below after i run rcominfo-
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

Please note I have docker container on  ubuntu 16.04 environment as stated in -
https://github.com/RadeonOpenCompute/ROCm-docker/blob/master/quick-start.md

the sample ./vector-copy is also failing to execute with below error-
Initializing the hsa runtime failed.

have got below HCC version details -

HCC clang version 7.0.0 (ssh://gerritgit/compute/ec/hcc-tot/clang 86791fc4961dc8ffde77bde20d7dfa5e5cbeff5e) (ssh://gerritgit/compute/ec/hcc-tot/llvm 0ccef158132e1222d549edf2da33d4bc0be6c2d1) (based on HCC 1.2.18184-74f5fa9-86791fc-0ccef15 )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/bin


Please advise - thanks.

---

### 评论 #7 — jedwards-AMD (2018-06-11T14:36:37Z)

The error you are seeing clearly indicates that the device is not accessible in some way. This error is very generic and could be caused by a range of problems, from your driver not loading, your docker image not exposing the devices correctly or a mismatch between your driver and your libhsakmt library. The first thing to do is verify things work 'on the metal'. If you can run clinfo or rocminfo on the actual system you know that your drivers are fine. Next, when you start up your docker image, check that both the /dev/kfd and /dev/dri devices are exposed.

---

### 评论 #8 — expertcloudconsulting (2018-06-11T15:53:09Z)

Problem solved!
The rocminfo output is coming as expected by running the container with root privilege..

---

### 评论 #9 — schwarzschild-radius (2018-08-28T12:40:54Z)

How was the issue solved? I am still getting the problem. I tried using the latest version of rocm but ended up in the same.

---

### 评论 #10 — jlgreathouse (2018-08-28T13:14:14Z)

@pradeepisro if you just did an install today, you may be seeing problem #510. If you're running Ubuntu, please ensure you're not running kernel 4.15.0-33 at the moment, as the ROCk kernel drivers are currently not working properly with it. We are working to fix this.

---

### 评论 #11 — calvintam236 (2018-08-31T04:57:27Z)

@jlgreathouse I'm seeing this error with 4.15.0-33 with the 1.8.199 release..

Everything below are run as root via SSH.
```console
$ dpkg -l |grep rocm
ii  rocm-clang-ocl                             0.3.0-7997136                                amd64        OpenCL compilation with clang compiler.
ii  rocm-dev                                   1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                           0.0.1                                        amd64        Radeon Open Compute - device libraries
ii  rocm-opencl                                1.2.0-2018082755                             amd64        OpenCL/ROCm
ii  rocm-opencl-dev                            1.2.0-2018082755                             amd64        OpenCL/ROCm
ii  rocm-smi                                   1.0.0-46-g81ef66f                            amd64        System Management Interface for ROCm
ii  rocm-utils                                 1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                                   1.0.0                                        amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool

$ lspci -tv
-[0000:00]-+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1450
           +-00.2  Advanced Micro Devices, Inc. [AMD] Device 1451
           +-01.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-01.3-[01-07]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 43bb
           |               +-00.1  Advanced Micro Devices, Inc. [AMD] Device 43b7
           |               \-00.2-[02-07]--+-00.0-[03]----00.0  Intel Corporation I211 Gigabit Network Connection
           |                               +-01.0-[04]--
           |                               +-04.0-[05]--
           |                               +-06.0-[06]--
           |                               \-07.0-[07]--
           +-02.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-03.1-[08]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-03.2-[09]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 67df
           |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
           +-04.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-07.1-[0a]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 145a
           |            +-00.2  Advanced Micro Devices, Inc. [AMD] Device 1456
           |            \-00.3  Advanced Micro Devices, Inc. [AMD] Device 145c
           +-08.0  Advanced Micro Devices, Inc. [AMD] Device 1452
           +-08.1-[0b]--+-00.0  Advanced Micro Devices, Inc. [AMD] Device 1455
           |            +-00.2  Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode]
           |            \-00.3  Advanced Micro Devices, Inc. [AMD] Device 1457
           +-14.0  Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller
           +-14.3  Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge
           +-18.0  Advanced Micro Devices, Inc. [AMD] Device 1460
           +-18.1  Advanced Micro Devices, Inc. [AMD] Device 1461
           +-18.2  Advanced Micro Devices, Inc. [AMD] Device 1462
           +-18.3  Advanced Micro Devices, Inc. [AMD] Device 1463
           +-18.4  Advanced Micro Devices, Inc. [AMD] Device 1464
           +-18.5  Advanced Micro Devices, Inc. [AMD] Device 1465
           +-18.6  Advanced Micro Devices, Inc. [AMD] Device 1466
           \-18.7  Advanced Micro Devices, Inc. [AMD] Device 1467

$ lsmod | grep amd
kvm_amd                86016  0
kvm                   598016  1 kvm_amd

$ dmesg
[    0.000000] Linux version 4.15.0-33-generic (buildd@lgw01-amd64-010) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 (Ubuntu 4.15.0-33.36~16.04.1-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.15.0-33-generic root=/dev/mapper/demon--vg-root ro splash quiet amdgpu.vm_fragment_size=9 vt.handoff=7
[    0.000000] KERNEL supported cpus:
[    0.000000]   Intel GenuineIntel
[    0.000000]   AMD AuthenticAMD
[    0.000000]   Centaur CentaurHauls
[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'compacted' format.
[    0.000000] e820: BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009d3ff] usable
[    0.000000] BIOS-e820: [mem 0x000000000009d400-0x000000000009ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x0000000003ffffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000004000000-0x000000000400ffff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x0000000004010000-0x0000000009bfffff] usable
[    0.000000] BIOS-e820: [mem 0x0000000009c00000-0x0000000009ffffff] reserved
[    0.000000] BIOS-e820: [mem 0x000000000a000000-0x00000000b674dfff] usable
[    0.000000] BIOS-e820: [mem 0x00000000b674e000-0x00000000b6768fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000b6769000-0x00000000ba967fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000ba968000-0x00000000baacffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000baad0000-0x00000000baad9fff] ACPI data
[    0.000000] BIOS-e820: [mem 0x00000000baada000-0x00000000babe2fff] usable
[    0.000000] BIOS-e820: [mem 0x00000000babe3000-0x00000000bafa3fff] ACPI NVS
[    0.000000] BIOS-e820: [mem 0x00000000bafa4000-0x00000000bba3dfff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000bba3e000-0x00000000bdffffff] usable
[    0.000000] BIOS-e820: [mem 0x00000000be000000-0x00000000bfffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fea00000-0x00000000fea0ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000feb80000-0x00000000fec01fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec10000-0x00000000fec10fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fec30000-0x00000000fec30fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed00fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed40000-0x00000000fed44fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fed80000-0x00000000fed8ffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fedc2000-0x00000000fedcffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fedd4000-0x00000000fedd5fff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000feefffff] reserved
[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000023f37ffff] usable
[    0.000000] NX (Execute Disable) protection: active
[    0.000000] SMBIOS 3.0 present.
[    0.000000] DMI: System manufacturer System Product Name/ROG STRIX B350-F GAMING, BIOS 3401 12/04/2017
[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable
[    0.000000] e820: last_pfn = 0x23f380 max_arch_pfn = 0x400000000
[    0.000000] MTRR default type: uncachable
[    0.000000] MTRR fixed ranges enabled:
[    0.000000]   00000-9FFFF write-back
[    0.000000]   A0000-BFFFF write-through
[    0.000000]   C0000-FFFFF write-protect
[    0.000000] MTRR variable ranges enabled:
[    0.000000]   0 base 000000000000 mask FFFF80000000 write-back
[    0.000000]   1 base 000080000000 mask FFFFC0000000 write-back
[    0.000000]   2 disabled
[    0.000000]   3 disabled
[    0.000000]   4 disabled
[    0.000000]   5 disabled
[    0.000000]   6 disabled
[    0.000000]   7 disabled
[    0.000000] TOM2: 0000000240000000 aka 9216M
[    0.000000] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
[    0.000000] e820: update [mem 0xc0000000-0xffffffff] usable ==> reserved
[    0.000000] e820: last_pfn = 0xbe000 max_arch_pfn = 0x400000000
[    0.000000] Scanning 1 areas for low memory corruption
[    0.000000] Base memory trampoline at [        (ptrval)] 97000 size 24576
[    0.000000] Using GB pages for direct mapping
[    0.000000] BRK [0x5bf3d000, 0x5bf3dfff] PGTABLE
[    0.000000] BRK [0x5bf3e000, 0x5bf3efff] PGTABLE
[    0.000000] BRK [0x5bf3f000, 0x5bf3ffff] PGTABLE
[    0.000000] BRK [0x5bf40000, 0x5bf40fff] PGTABLE
[    0.000000] BRK [0x5bf41000, 0x5bf41fff] PGTABLE
[    0.000000] BRK [0x5bf42000, 0x5bf42fff] PGTABLE
[    0.000000] BRK [0x5bf43000, 0x5bf43fff] PGTABLE
[    0.000000] BRK [0x5bf44000, 0x5bf44fff] PGTABLE
[    0.000000] BRK [0x5bf45000, 0x5bf45fff] PGTABLE
[    0.000000] BRK [0x5bf46000, 0x5bf46fff] PGTABLE
[    0.000000] RAMDISK: [mem 0x351ca000-0x368dcfff]
[    0.000000] ACPI: Early table checksum verification disabled
[    0.000000] ACPI: RSDP 0x00000000000F05B0 000024 (v02 ALASKA)
[    0.000000] ACPI: XSDT 0x00000000B674E098 0000A4 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FACP 0x00000000B6757D08 000114 (v06 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI BIOS Warning (bug): Optional FADT field Pm2ControlBlock has valid Length but zero Address: 0x0000000000000000/0x1 (20170831/tbfadt-658)
[    0.000000] ACPI: DSDT 0x00000000B674E1D0 009B33 (v02 ALASKA A M I    01072009 INTL 20120913)
[    0.000000] ACPI: FACS 0x00000000BAF8CE00 000040
[    0.000000] ACPI: APIC 0x00000000B6757E20 0000DE (v03 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FPDT 0x00000000B6757F00 000044 (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: FIDT 0x00000000B6757F48 00009C (v01 ALASKA A M I    01072009 AMI  00010013)
[    0.000000] ACPI: SSDT 0x00000000B6766CA0 00195E (v01 AMD    AmdTable 00000001 INTL 20120913)
[    0.000000] ACPI: SSDT 0x00000000B6758040 008C4C (v02 AMD    AMD ALIB 00000002 MSFT 04000000)
[    0.000000] ACPI: SSDT 0x00000000B6760C90 002AC4 (v01 AMD    AMD AOD  00000001 INTL 20120913)
[    0.000000] ACPI: MCFG 0x00000000B6763758 00003C (v01 ALASKA A M I    01072009 MSFT 00010013)
[    0.000000] ACPI: SSDT 0x00000000B6763798 002314 (v01 AMD    AMD CPU  00000001 AMD  00000001)
[    0.000000] ACPI: CRAT 0x00000000B6765AB0 000F50 (v01 AMD    AMD CRAT 00000001 AMD  00000001)
[    0.000000] ACPI: CDIT 0x00000000B6766A00 000029 (v01 AMD    AMD CDIT 00000001 AMD  00000001)
[    0.000000] ACPI: HPET 0x00000000B6766A30 000038 (v01 ALASKA A M I    01072009 AMI  00000005)
[    0.000000] ACPI: SSDT 0x00000000B6766A68 000024 (v01 AMDFCH FCHZP    00001000 INTL 20120913)
[    0.000000] ACPI: UEFI 0x00000000B6766A90 000042 (v01                 00000000      00000000)
[    0.000000] ACPI: IVRS 0x00000000B6766AD8 0000D0 (v02 AMD    AMD IVRS 00000001 AMD  00000000)
[    0.000000] ACPI: SSDT 0x00000000B6766BA8 0000F8 (v01 AMD    AMD PT   00001000 INTL 20120913)
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] system APIC only can use physical flat
[    0.000000] Setting APIC routing to physical flat.
[    0.000000] No NUMA configuration found
[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000023f37ffff]
[    0.000000] NODE_DATA(0) allocated [mem 0x23f355000-0x23f37ffff]
[    0.000000] tsc: Fast TSC calibration failed
[    0.000000] tsc: Using PIT calibration value
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
[    0.000000]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000023f37ffff]
[    0.000000]   Device   empty
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000001000-0x000000000009cfff]
[    0.000000]   node   0: [mem 0x0000000000100000-0x0000000003ffffff]
[    0.000000]   node   0: [mem 0x0000000004010000-0x0000000009bfffff]
[    0.000000]   node   0: [mem 0x000000000a000000-0x00000000b674dfff]
[    0.000000]   node   0: [mem 0x00000000b6769000-0x00000000ba967fff]
[    0.000000]   node   0: [mem 0x00000000baada000-0x00000000babe2fff]
[    0.000000]   node   0: [mem 0x00000000bba3e000-0x00000000bdffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000023f37ffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000001000-0x000000023f37ffff]
[    0.000000] On node 0 totalpages: 2080548
[    0.000000]   DMA zone: 64 pages used for memmap
[    0.000000]   DMA zone: 21 pages reserved
[    0.000000]   DMA zone: 3996 pages, LIFO batch:0
[    0.000000]   DMA32 zone: 12017 pages used for memmap
[    0.000000]   DMA32 zone: 769032 pages, LIFO batch:31
[    0.000000]   Normal zone: 20430 pages used for memmap
[    0.000000]   Normal zone: 1307520 pages, LIFO batch:31
[    0.000000] Reserved but unavailable: 100 pages
[    0.000000] ACPI: PM-Timer IO Port: 0x808
[    0.000000] ACPI: Local APIC address 0xfee00000
[    0.000000] system APIC only can use physical flat
[    0.000000] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
[    0.000000] IOAPIC[0]: apic_id 17, version 33, address 0xfec00000, GSI 0-23
[    0.000000] IOAPIC[1]: apic_id 18, version 33, address 0xfec01000, GSI 24-55
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 low level)
[    0.000000] ACPI: IRQ0 used by override.
[    0.000000] ACPI: IRQ9 used by override.
[    0.000000] Using ACPI (MADT) for SMP configuration information
[    0.000000] ACPI: HPET id: 0x10228201 base: 0xfed00000
[    0.000000] smpboot: Allowing 16 CPUs, 0 hotplug CPUs
[    0.000000] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009d000-0x0009dfff]
[    0.000000] PM: Registered nosave memory: [mem 0x0009e000-0x0009ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000dffff]
[    0.000000] PM: Registered nosave memory: [mem 0x000e0000-0x000fffff]
[    0.000000] PM: Registered nosave memory: [mem 0x04000000-0x0400ffff]
[    0.000000] PM: Registered nosave memory: [mem 0x09c00000-0x09ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xb674e000-0xb6768fff]
[    0.000000] PM: Registered nosave memory: [mem 0xba968000-0xbaacffff]
[    0.000000] PM: Registered nosave memory: [mem 0xbaad0000-0xbaad9fff]
[    0.000000] PM: Registered nosave memory: [mem 0xbabe3000-0xbafa3fff]
[    0.000000] PM: Registered nosave memory: [mem 0xbafa4000-0xbba3dfff]
[    0.000000] PM: Registered nosave memory: [mem 0xbe000000-0xbfffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xc0000000-0xf7ffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfc000000-0xfe9fffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfea00000-0xfea0ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfea10000-0xfeb7ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfeb80000-0xfec01fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec02000-0xfec0ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec10000-0xfec10fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec11000-0xfec2ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec30000-0xfec30fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfec31000-0xfecfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed00000-0xfed00fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed01000-0xfed3ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed40000-0xfed44fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed45000-0xfed7ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed80000-0xfed8ffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfed90000-0xfedc1fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedc2000-0xfedcffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd0000-0xfedd3fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd4000-0xfedd5fff]
[    0.000000] PM: Registered nosave memory: [mem 0xfedd6000-0xfedfffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfee00000-0xfeefffff]
[    0.000000] PM: Registered nosave memory: [mem 0xfef00000-0xfeffffff]
[    0.000000] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
[    0.000000] e820: [mem 0xc0000000-0xf7ffffff] available for PCI devices
[    0.000000] Booting paravirtualized kernel on bare hardware
[    0.000000] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
[    0.000000] random: get_random_bytes called from start_kernel+0x99/0x51b with crng_init=0
[    0.000000] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:16 nr_cpu_ids:16 nr_node_ids:1
[    0.000000] percpu: Embedded 46 pages/cpu @        (ptrval) s151552 r8192 d28672 u262144
[    0.000000] pcpu-alloc: s151552 r8192 d28672 u262144 alloc=1*2097152
[    0.000000] pcpu-alloc: [0] 00 01 02 03 04 05 06 07 [0] 08 09 10 11 12 13 14 15 
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 2048016
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.15.0-33-generic root=/dev/mapper/demon--vg-root ro splash quiet amdgpu.vm_fragment_size=9 vt.handoff=7
[    0.000000] Calgary: detecting Calgary via BIOS EBDA area
[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
[    0.000000] Memory: 8070328K/8322192K available (12300K kernel code, 2469K rwdata, 4252K rodata, 2404K init, 2416K bss, 251864K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=16, Nodes=1
[    0.000000] ftrace: allocating 39127 entries in 153 pages
[    0.000000] Hierarchical RCU implementation.
[    0.000000] 	RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=16.
[    0.000000] 	Tasks RCU enabled.
[    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=16
[    0.000000] NR_IRQS: 524544, nr_irqs: 1096, preallocated irqs: 16
[    0.000000] spurious 8259A interrupt: IRQ7.
[    0.000000] vt handoff: transparent VT on vt#7
[    0.000000] Console: colour dummy device 80x25
[    0.000000] console [tty0] enabled
[    0.000000] ACPI: Core revision 20170831
[    0.000000] ACPI: 7 ACPI AML tables successfully acquired and loaded
[    0.000000] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484873504 ns
[    0.000000] hpet clockevent registered
[    0.000000] APIC: Switch to symmetric I/O mode setup
[    0.004000] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
[    0.024000] tsc: Fast TSC calibration failed
[    0.032000] tsc: PIT calibration matches HPET. 1 loops
[    0.032000] tsc: Detected 3692.505 MHz processor
[    0.032000] Calibrating delay loop (skipped), value calculated using timer frequency.. 7385.01 BogoMIPS (lpj=14770020)
[    0.032000] pid_max: default: 32768 minimum: 301
[    0.032000] Security Framework initialized
[    0.032000] Yama: becoming mindful.
[    0.032000] AppArmor: AppArmor initialized
[    0.032000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes)
[    0.032000] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes)
[    0.032000] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.032000] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes)
[    0.036121] mce: CPU supports 23 MCE banks
[    0.036140] LVT offset 1 assigned for vector 0xf9
[    0.036206] LVT offset 2 assigned for vector 0xf4
[    0.036217] Last level iTLB entries: 4KB 1024, 2MB 1024, 4MB 512
[    0.036218] Last level dTLB entries: 4KB 1536, 2MB 1536, 4MB 768, 1GB 0
[    0.036219] Spectre V2 : Mitigation: Full AMD retpoline
[    0.036220] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
[    0.043587] Freeing SMP alternatives memory: 36K
[    0.052000] smpboot: CPU0: AMD Ryzen 7 1700X Eight-Core Processor (family: 0x17, model: 0x1, stepping: 0x1)
[    0.052000] Performance Events: Fam17h core perfctr, AMD PMU driver.
[    0.052000] ... version:                0
[    0.052000] ... bit width:              48
[    0.052000] ... generic registers:      6
[    0.052000] ... value mask:             0000ffffffffffff
[    0.052000] ... max period:             00007fffffffffff
[    0.052000] ... fixed-purpose events:   0
[    0.052000] ... event mask:             000000000000003f
[    0.052000] Hierarchical SRCU implementation.
[    0.052000] smp: Bringing up secondary CPUs ...
[    0.052000] x86: Booting SMP configuration:
[    0.052000] .... node  #0, CPUs:        #1
[    0.052000] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
[    0.052000]   #2  #3  #4  #5  #6  #7  #8  #9 #10 #11 #12 #13 #14 #15
[    0.082198] smp: Brought up 1 node, 16 CPUs
[    0.082198] smpboot: Max logical packages: 1
[    0.082198] smpboot: Total of 16 processors activated (118160.16 BogoMIPS)
[    0.084312] devtmpfs: initialized
[    0.084312] x86/mm: Memory block size: 128MB
[    0.084489] evm: security.selinux
[    0.084490] evm: security.SMACK64
[    0.084490] evm: security.SMACK64EXEC
[    0.084490] evm: security.SMACK64TRANSMUTE
[    0.084491] evm: security.SMACK64MMAP
[    0.084491] evm: security.apparmor
[    0.084491] evm: security.ima
[    0.084492] evm: security.capability
[    0.084504] PM: Registering ACPI NVS region [mem 0x04000000-0x0400ffff] (65536 bytes)
[    0.084504] PM: Registering ACPI NVS region [mem 0xbabe3000-0xbafa3fff] (3936256 bytes)
[    0.084504] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.084504] futex hash table entries: 4096 (order: 6, 262144 bytes)
[    0.084504] pinctrl core: initialized pinctrl subsystem
[    0.084504] RTC time:  4:41:33, date: 08/31/18
[    0.084504] NET: Registered protocol family 16
[    0.084504] audit: initializing netlink subsys (disabled)
[    0.084504] audit: type=2000 audit(1535690493.084:1): state=initialized audit_enabled=0 res=1
[    0.084504] cpuidle: using governor ladder
[    0.084504] cpuidle: using governor menu
[    0.084504] ACPI: bus type PCI registered
[    0.084504] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.084504] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
[    0.084504] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
[    0.084504] PCI: Using configuration type 1 for base access
[    0.084504] mtrr: your CPUs had inconsistent variable MTRR settings
[    0.084504] mtrr: probably your BIOS does not setup all CPUs.
[    0.084504] mtrr: corrected configuration.
[    0.085023] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.085023] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.085024] ACPI: Added _OSI(Module Device)
[    0.085024] ACPI: Added _OSI(Processor Device)
[    0.085024] ACPI: Added _OSI(3.0 _SCP Extensions)
[    0.085024] ACPI: Added _OSI(Processor Aggregator Device)
[    0.085024] ACPI: Added _OSI(Linux-Dell-Video)
[    0.085024] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
[    0.085024] ACPI: Executed 2 blocks of module-level executable AML code
[    0.089708] ACPI Error: Needed [Integer/String/Buffer], found [Region]         (ptrval) (20170831/exresop-424)
[    0.089713] Executing subtree for Buffer/Package/Region
[    0.089714] ACPI Exception: AE_AML_OPERAND_TYPE, Could not execute arguments for [IOB2] (Region) (20170831/nsinit-426)
[    0.098337] ACPI: Interpreter enabled
[    0.098352] ACPI: (supports S0 S3 S4 S5)
[    0.098353] ACPI: Using IOAPIC for interrupt routing
[    0.098620] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.098897] ACPI: Enabled 4 GPEs in block 00 to 1F
[    0.107692] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])
[    0.107696] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI]
[    0.107878] acpi PNP0A08:00: _OSC: platform does not support [PCIeHotplug]
[    0.108055] acpi PNP0A08:00: _OSC: OS now controls [PME AER PCIeCapability]
[    0.108066] acpi PNP0A08:00: [Firmware Info]: MMCONFIG for domain 0000 [bus 00-3f] only partially covers this bridge
[    0.108402] PCI host bridge to bus 0000:00
[    0.108404] pci_bus 0000:00: root bus resource [io  0x0000-0x03af window]
[    0.108405] pci_bus 0000:00: root bus resource [io  0x03e0-0x0cf7 window]
[    0.108406] pci_bus 0000:00: root bus resource [io  0x03b0-0x03df window]
[    0.108407] pci_bus 0000:00: root bus resource [io  0x0d00-0xefff window]
[    0.108408] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
[    0.108408] pci_bus 0000:00: root bus resource [mem 0x000c0000-0x000dffff window]
[    0.108409] pci_bus 0000:00: root bus resource [mem 0xc0000000-0xfec2ffff window]
[    0.108410] pci_bus 0000:00: root bus resource [mem 0xfee00000-0xffffffff window]
[    0.108411] pci_bus 0000:00: root bus resource [bus 00-ff]
[    0.108417] pci 0000:00:00.0: [1022:1450] type 00 class 0x060000
[    0.108493] pci 0000:00:00.2: [1022:1451] type 00 class 0x080600
[    0.108583] pci 0000:00:01.0: [1022:1452] type 00 class 0x060000
[    0.108651] pci 0000:00:01.3: [1022:1453] type 01 class 0x060400
[    0.108758] pci 0000:00:01.3: PME# supported from D0 D3hot D3cold
[    0.108838] pci 0000:00:02.0: [1022:1452] type 00 class 0x060000
[    0.108915] pci 0000:00:03.0: [1022:1452] type 00 class 0x060000
[    0.108977] pci 0000:00:03.1: [1022:1453] type 01 class 0x060400
[    0.109086] pci 0000:00:03.1: PME# supported from D0 D3hot D3cold
[    0.109158] pci 0000:00:03.2: [1022:1453] type 01 class 0x060400
[    0.109270] pci 0000:00:03.2: PME# supported from D0 D3hot D3cold
[    0.109353] pci 0000:00:04.0: [1022:1452] type 00 class 0x060000
[    0.109434] pci 0000:00:07.0: [1022:1452] type 00 class 0x060000
[    0.109497] pci 0000:00:07.1: [1022:1454] type 01 class 0x060400
[    0.109534] pci 0000:00:07.1: enabling Extended Tags
[    0.109615] pci 0000:00:07.1: PME# supported from D0 D3hot D3cold
[    0.109697] pci 0000:00:08.0: [1022:1452] type 00 class 0x060000
[    0.109761] pci 0000:00:08.1: [1022:1454] type 01 class 0x060400
[    0.109791] pci 0000:00:08.1: enabling Extended Tags
[    0.109869] pci 0000:00:08.1: PME# supported from D0 D3hot D3cold
[    0.109986] pci 0000:00:14.0: [1022:790b] type 00 class 0x0c0500
[    0.110199] pci 0000:00:14.3: [1022:790e] type 00 class 0x060100
[    0.110417] pci 0000:00:18.0: [1022:1460] type 00 class 0x060000
[    0.110471] pci 0000:00:18.1: [1022:1461] type 00 class 0x060000
[    0.110523] pci 0000:00:18.2: [1022:1462] type 00 class 0x060000
[    0.110577] pci 0000:00:18.3: [1022:1463] type 00 class 0x060000
[    0.110630] pci 0000:00:18.4: [1022:1464] type 00 class 0x060000
[    0.110682] pci 0000:00:18.5: [1022:1465] type 00 class 0x060000
[    0.110734] pci 0000:00:18.6: [1022:1466] type 00 class 0x060000
[    0.110787] pci 0000:00:18.7: [1022:1467] type 00 class 0x060000
[    0.110923] pci 0000:01:00.0: [1022:43bb] type 00 class 0x0c0330
[    0.110945] pci 0000:01:00.0: reg 0x10: [mem 0xfe6a0000-0xfe6a7fff 64bit]
[    0.111018] pci 0000:01:00.0: PME# supported from D3hot D3cold
[    0.111079] pci 0000:01:00.1: [1022:43b7] type 00 class 0x010601
[    0.111123] pci 0000:01:00.1: reg 0x24: [mem 0xfe680000-0xfe69ffff]
[    0.111130] pci 0000:01:00.1: reg 0x30: [mem 0xfe600000-0xfe67ffff pref]
[    0.111167] pci 0000:01:00.1: PME# supported from D3hot D3cold
[    0.111207] pci 0000:01:00.2: [1022:43b2] type 01 class 0x060400
[    0.111277] pci 0000:01:00.2: PME# supported from D3hot D3cold
[    0.120022] pci 0000:00:01.3: PCI bridge to [bus 01-07]
[    0.120026] pci 0000:00:01.3:   bridge window [io  0xe000-0xefff]
[    0.120028] pci 0000:00:01.3:   bridge window [mem 0xfe500000-0xfe6fffff]
[    0.120138] pci 0000:02:00.0: [1022:43b4] type 01 class 0x060400
[    0.120225] pci 0000:02:00.0: PME# supported from D3hot D3cold
[    0.120296] pci 0000:02:01.0: [1022:43b4] type 01 class 0x060400
[    0.120380] pci 0000:02:01.0: PME# supported from D3hot D3cold
[    0.120443] pci 0000:02:04.0: [1022:43b4] type 01 class 0x060400
[    0.120524] pci 0000:02:04.0: PME# supported from D3hot D3cold
[    0.120586] pci 0000:02:06.0: [1022:43b4] type 01 class 0x060400
[    0.120668] pci 0000:02:06.0: PME# supported from D3hot D3cold
[    0.120728] pci 0000:02:07.0: [1022:43b4] type 01 class 0x060400
[    0.120810] pci 0000:02:07.0: PME# supported from D3hot D3cold
[    0.120881] pci 0000:01:00.2: PCI bridge to [bus 02-07]
[    0.120886] pci 0000:01:00.2:   bridge window [io  0xe000-0xefff]
[    0.120888] pci 0000:01:00.2:   bridge window [mem 0xfe500000-0xfe5fffff]
[    0.120956] pci 0000:03:00.0: [8086:1539] type 00 class 0x020000
[    0.121000] pci 0000:03:00.0: reg 0x10: [mem 0xfe500000-0xfe51ffff]
[    0.121032] pci 0000:03:00.0: reg 0x18: [io  0xe000-0xe01f]
[    0.121048] pci 0000:03:00.0: reg 0x1c: [mem 0xfe520000-0xfe523fff]
[    0.121212] pci 0000:03:00.0: PME# supported from D0 D3hot D3cold
[    0.132031] pci 0000:02:00.0: PCI bridge to [bus 03]
[    0.132037] pci 0000:02:00.0:   bridge window [io  0xe000-0xefff]
[    0.132040] pci 0000:02:00.0:   bridge window [mem 0xfe500000-0xfe5fffff]
[    0.132095] pci 0000:02:01.0: PCI bridge to [bus 04]
[    0.132147] pci 0000:02:04.0: PCI bridge to [bus 05]
[    0.132197] pci 0000:02:06.0: PCI bridge to [bus 06]
[    0.132246] pci 0000:02:07.0: PCI bridge to [bus 07]
[    0.132355] pci 0000:08:00.0: [1002:67df] type 00 class 0x030000
[    0.132379] pci 0000:08:00.0: reg 0x10: [mem 0xe0000000-0xefffffff 64bit pref]
[    0.132388] pci 0000:08:00.0: reg 0x18: [mem 0xf0000000-0xf01fffff 64bit pref]
[    0.132394] pci 0000:08:00.0: reg 0x20: [io  0xd000-0xd0ff]
[    0.132401] pci 0000:08:00.0: reg 0x24: [mem 0xfe900000-0xfe93ffff]
[    0.132407] pci 0000:08:00.0: reg 0x30: [mem 0xfe940000-0xfe95ffff pref]
[    0.132459] pci 0000:08:00.0: supports D1 D2
[    0.132460] pci 0000:08:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.132538] pci 0000:08:00.1: [1002:aaf0] type 00 class 0x040300
[    0.132556] pci 0000:08:00.1: reg 0x10: [mem 0xfe960000-0xfe963fff 64bit]
[    0.132619] pci 0000:08:00.1: supports D1 D2
[    0.144026] pci 0000:00:03.1: PCI bridge to [bus 08]
[    0.144029] pci 0000:00:03.1:   bridge window [io  0xd000-0xdfff]
[    0.144031] pci 0000:00:03.1:   bridge window [mem 0xfe900000-0xfe9fffff]
[    0.144034] pci 0000:00:03.1:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.144124] pci 0000:09:00.0: [1002:67df] type 00 class 0x030000
[    0.144157] pci 0000:09:00.0: reg 0x10: [mem 0xc0000000-0xcfffffff 64bit pref]
[    0.144168] pci 0000:09:00.0: reg 0x18: [mem 0xd0000000-0xd01fffff 64bit pref]
[    0.144174] pci 0000:09:00.0: reg 0x20: [io  0xc000-0xc0ff]
[    0.144181] pci 0000:09:00.0: reg 0x24: [mem 0xfe800000-0xfe83ffff]
[    0.144187] pci 0000:09:00.0: reg 0x30: [mem 0xfe840000-0xfe85ffff pref]
[    0.144269] pci 0000:09:00.0: supports D1 D2
[    0.144270] pci 0000:09:00.0: PME# supported from D1 D2 D3hot D3cold
[    0.144381] pci 0000:09:00.1: [1002:aaf0] type 00 class 0x040300
[    0.144409] pci 0000:09:00.1: reg 0x10: [mem 0xfe860000-0xfe863fff 64bit]
[    0.144503] pci 0000:09:00.1: supports D1 D2
[    0.156033] pci 0000:00:03.2: PCI bridge to [bus 09]
[    0.156037] pci 0000:00:03.2:   bridge window [io  0xc000-0xcfff]
[    0.156039] pci 0000:00:03.2:   bridge window [mem 0xfe800000-0xfe8fffff]
[    0.156042] pci 0000:00:03.2:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.156127] pci 0000:0a:00.0: [1022:145a] type 00 class 0x130000
[    0.156160] pci 0000:0a:00.0: enabling Extended Tags
[    0.156226] pci 0000:0a:00.2: [1022:1456] type 00 class 0x108000
[    0.156243] pci 0000:0a:00.2: reg 0x18: [mem 0xfe300000-0xfe3fffff]
[    0.156254] pci 0000:0a:00.2: reg 0x24: [mem 0xfe400000-0xfe401fff]
[    0.156260] pci 0000:0a:00.2: enabling Extended Tags
[    0.156331] pci 0000:0a:00.3: [1022:145c] type 00 class 0x0c0330
[    0.156344] pci 0000:0a:00.3: reg 0x10: [mem 0xfe200000-0xfe2fffff 64bit]
[    0.156363] pci 0000:0a:00.3: enabling Extended Tags
[    0.156389] pci 0000:0a:00.3: PME# supported from D0 D3hot D3cold
[    0.156441] pci 0000:00:07.1: PCI bridge to [bus 0a]
[    0.156444] pci 0000:00:07.1:   bridge window [mem 0xfe200000-0xfe4fffff]
[    0.156518] pci 0000:0b:00.0: [1022:1455] type 00 class 0x130000
[    0.156550] pci 0000:0b:00.0: enabling Extended Tags
[    0.156612] pci 0000:0b:00.2: [1022:7901] type 00 class 0x010601
[    0.156639] pci 0000:0b:00.2: reg 0x24: [mem 0xfe708000-0xfe708fff]
[    0.156646] pci 0000:0b:00.2: enabling Extended Tags
[    0.156673] pci 0000:0b:00.2: PME# supported from D3hot D3cold
[    0.156715] pci 0000:0b:00.3: [1022:1457] type 00 class 0x040300
[    0.156726] pci 0000:0b:00.3: reg 0x10: [mem 0xfe700000-0xfe707fff]
[    0.156749] pci 0000:0b:00.3: enabling Extended Tags
[    0.156775] pci 0000:0b:00.3: PME# supported from D0 D3hot D3cold
[    0.156830] pci 0000:00:08.1: PCI bridge to [bus 0b]
[    0.156833] pci 0000:00:08.1:   bridge window [mem 0xfe700000-0xfe7fffff]
[    0.157173] ACPI: PCI Interrupt Link [LNKA] (IRQs 4 5 7 10 11 14 15) *0
[    0.157230] ACPI: PCI Interrupt Link [LNKB] (IRQs 4 5 7 10 11 14 15) *0
[    0.157279] ACPI: PCI Interrupt Link [LNKC] (IRQs 4 5 7 10 11 14 15) *0
[    0.157340] ACPI: PCI Interrupt Link [LNKD] (IRQs 4 5 7 10 11 14 15) *0
[    0.157395] ACPI: PCI Interrupt Link [LNKE] (IRQs 4 5 7 10 11 14 15) *0
[    0.157440] ACPI: PCI Interrupt Link [LNKF] (IRQs 4 5 7 10 11 14 15) *0
[    0.157485] ACPI: PCI Interrupt Link [LNKG] (IRQs 4 5 7 10 11 14 15) *0
[    0.157530] ACPI: PCI Interrupt Link [LNKH] (IRQs 4 5 7 10 11 14 15) *0
[    0.158150] SCSI subsystem initialized
[    0.158168] libata version 3.00 loaded.
[    0.158168] pci 0000:08:00.0: vgaarb: setting as boot VGA device
[    0.158168] pci 0000:08:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.158168] pci 0000:09:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    0.158168] pci 0000:09:00.0: vgaarb: bridge control possible
[    0.158168] pci 0000:08:00.0: vgaarb: bridge control possible
[    0.158168] vgaarb: loaded
[    0.158168] ACPI: bus type USB registered
[    0.158168] usbcore: registered new interface driver usbfs
[    0.158168] usbcore: registered new interface driver hub
[    0.158168] usbcore: registered new device driver usb
[    0.158168] EDAC MC: Ver: 3.0.0
[    0.158168] PCI: Using ACPI for IRQ routing
[    0.160478] PCI: pci_cache_line_size set to 64 bytes
[    0.160538] e820: reserve RAM buffer [mem 0x0009d400-0x0009ffff]
[    0.160539] e820: reserve RAM buffer [mem 0x09c00000-0x0bffffff]
[    0.160539] e820: reserve RAM buffer [mem 0xb674e000-0xb7ffffff]
[    0.160540] e820: reserve RAM buffer [mem 0xba968000-0xbbffffff]
[    0.160541] e820: reserve RAM buffer [mem 0xbabe3000-0xbbffffff]
[    0.160541] e820: reserve RAM buffer [mem 0xbe000000-0xbfffffff]
[    0.160542] e820: reserve RAM buffer [mem 0x23f380000-0x23fffffff]
[    0.160616] NetLabel: Initializing
[    0.160617] NetLabel:  domain hash size = 128
[    0.160617] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.160627] NetLabel:  unlabeled traffic allowed by default
[    0.160635] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0
[    0.160635] hpet0: 3 comparators, 32-bit 14.318180 MHz counter
[    0.164032] clocksource: Switched to clocksource hpet
[    0.171530] VFS: Disk quotas dquot_6.6.0
[    0.171545] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.171627] AppArmor: AppArmor Filesystem Enabled
[    0.171652] pnp: PnP ACPI init
[    0.171808] system 00:00: [mem 0xf8000000-0xfbffffff] has been reserved
[    0.171812] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
[    0.171875] system 00:01: [mem 0xfeb80000-0xfebfffff] could not be reserved
[    0.171878] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.171982] pnp 00:02: Plug and Play ACPI device, IDs PNP0b00 (active)
[    0.172157] system 00:03: [io  0x0300-0x030f] has been reserved
[    0.172158] system 00:03: [io  0x0230-0x023f] has been reserved
[    0.172159] system 00:03: [io  0x0290-0x029f] has been reserved
[    0.172162] system 00:03: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.172411] pnp 00:04: [dma 0 disabled]
[    0.172445] pnp 00:04: Plug and Play ACPI device, IDs PNP0501 (active)
[    0.172663] system 00:05: [io  0x04d0-0x04d1] has been reserved
[    0.172665] system 00:05: [io  0x040b] has been reserved
[    0.172666] system 00:05: [io  0x04d6] has been reserved
[    0.172667] system 00:05: [io  0x0c00-0x0c01] has been reserved
[    0.172667] system 00:05: [io  0x0c14] has been reserved
[    0.172668] system 00:05: [io  0x0c50-0x0c51] has been reserved
[    0.172669] system 00:05: [io  0x0c52] has been reserved
[    0.172670] system 00:05: [io  0x0c6c] has been reserved
[    0.172671] system 00:05: [io  0x0c6f] has been reserved
[    0.172672] system 00:05: [io  0x0cd0-0x0cd1] has been reserved
[    0.172673] system 00:05: [io  0x0cd2-0x0cd3] has been reserved
[    0.172674] system 00:05: [io  0x0cd4-0x0cd5] has been reserved
[    0.172675] system 00:05: [io  0x0cd6-0x0cd7] has been reserved
[    0.172676] system 00:05: [io  0x0cd8-0x0cdf] has been reserved
[    0.172676] system 00:05: [io  0x0800-0x089f] has been reserved
[    0.172677] system 00:05: [io  0x0b00-0x0b0f] has been reserved
[    0.172678] system 00:05: [io  0x0b20-0x0b3f] has been reserved
[    0.172679] system 00:05: [io  0x0900-0x090f] has been reserved
[    0.172680] system 00:05: [io  0x0910-0x091f] has been reserved
[    0.172681] system 00:05: [mem 0xfec00000-0xfec00fff] could not be reserved
[    0.172683] system 00:05: [mem 0xfec01000-0xfec01fff] could not be reserved
[    0.172684] system 00:05: [mem 0xfedc0000-0xfedc0fff] has been reserved
[    0.172685] system 00:05: [mem 0xfee00000-0xfee00fff] has been reserved
[    0.172686] system 00:05: [mem 0xfed80000-0xfed8ffff] could not be reserved
[    0.172687] system 00:05: [mem 0xfec10000-0xfec10fff] has been reserved
[    0.172688] system 00:05: [mem 0xff000000-0xffffffff] has been reserved
[    0.172690] system 00:05: Plug and Play ACPI device, IDs PNP0c02 (active)
[    0.173100] pnp: PnP ACPI: found 6 devices
[    0.179490] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.179550] pci 0000:02:00.0: PCI bridge to [bus 03]
[    0.179552] pci 0000:02:00.0:   bridge window [io  0xe000-0xefff]
[    0.179556] pci 0000:02:00.0:   bridge window [mem 0xfe500000-0xfe5fffff]
[    0.179563] pci 0000:02:01.0: PCI bridge to [bus 04]
[    0.179572] pci 0000:02:04.0: PCI bridge to [bus 05]
[    0.179580] pci 0000:02:06.0: PCI bridge to [bus 06]
[    0.179589] pci 0000:02:07.0: PCI bridge to [bus 07]
[    0.179598] pci 0000:01:00.2: PCI bridge to [bus 02-07]
[    0.179600] pci 0000:01:00.2:   bridge window [io  0xe000-0xefff]
[    0.179603] pci 0000:01:00.2:   bridge window [mem 0xfe500000-0xfe5fffff]
[    0.179609] pci 0000:00:01.3: PCI bridge to [bus 01-07]
[    0.179610] pci 0000:00:01.3:   bridge window [io  0xe000-0xefff]
[    0.179612] pci 0000:00:01.3:   bridge window [mem 0xfe500000-0xfe6fffff]
[    0.179616] pci 0000:00:03.1: PCI bridge to [bus 08]
[    0.179617] pci 0000:00:03.1:   bridge window [io  0xd000-0xdfff]
[    0.179619] pci 0000:00:03.1:   bridge window [mem 0xfe900000-0xfe9fffff]
[    0.179621] pci 0000:00:03.1:   bridge window [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.179624] pci 0000:00:03.2: PCI bridge to [bus 09]
[    0.179625] pci 0000:00:03.2:   bridge window [io  0xc000-0xcfff]
[    0.179627] pci 0000:00:03.2:   bridge window [mem 0xfe800000-0xfe8fffff]
[    0.179629] pci 0000:00:03.2:   bridge window [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.179632] pci 0000:00:07.1: PCI bridge to [bus 0a]
[    0.179634] pci 0000:00:07.1:   bridge window [mem 0xfe200000-0xfe4fffff]
[    0.179638] pci 0000:00:08.1: PCI bridge to [bus 0b]
[    0.179640] pci 0000:00:08.1:   bridge window [mem 0xfe700000-0xfe7fffff]
[    0.179645] pci_bus 0000:00: resource 4 [io  0x0000-0x03af window]
[    0.179646] pci_bus 0000:00: resource 5 [io  0x03e0-0x0cf7 window]
[    0.179647] pci_bus 0000:00: resource 6 [io  0x03b0-0x03df window]
[    0.179647] pci_bus 0000:00: resource 7 [io  0x0d00-0xefff window]
[    0.179648] pci_bus 0000:00: resource 8 [mem 0x000a0000-0x000bffff window]
[    0.179649] pci_bus 0000:00: resource 9 [mem 0x000c0000-0x000dffff window]
[    0.179650] pci_bus 0000:00: resource 10 [mem 0xc0000000-0xfec2ffff window]
[    0.179651] pci_bus 0000:00: resource 11 [mem 0xfee00000-0xffffffff window]
[    0.179652] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
[    0.179653] pci_bus 0000:01: resource 1 [mem 0xfe500000-0xfe6fffff]
[    0.179654] pci_bus 0000:02: resource 0 [io  0xe000-0xefff]
[    0.179655] pci_bus 0000:02: resource 1 [mem 0xfe500000-0xfe5fffff]
[    0.179656] pci_bus 0000:03: resource 0 [io  0xe000-0xefff]
[    0.179657] pci_bus 0000:03: resource 1 [mem 0xfe500000-0xfe5fffff]
[    0.179658] pci_bus 0000:08: resource 0 [io  0xd000-0xdfff]
[    0.179659] pci_bus 0000:08: resource 1 [mem 0xfe900000-0xfe9fffff]
[    0.179660] pci_bus 0000:08: resource 2 [mem 0xe0000000-0xf01fffff 64bit pref]
[    0.179661] pci_bus 0000:09: resource 0 [io  0xc000-0xcfff]
[    0.179661] pci_bus 0000:09: resource 1 [mem 0xfe800000-0xfe8fffff]
[    0.179662] pci_bus 0000:09: resource 2 [mem 0xc0000000-0xd01fffff 64bit pref]
[    0.179663] pci_bus 0000:0a: resource 1 [mem 0xfe200000-0xfe4fffff]
[    0.179664] pci_bus 0000:0b: resource 1 [mem 0xfe700000-0xfe7fffff]
[    0.179735] NET: Registered protocol family 2
[    0.179890] TCP established hash table entries: 65536 (order: 7, 524288 bytes)
[    0.179976] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
[    0.180107] TCP: Hash tables configured (established 65536 bind 65536)
[    0.180148] UDP hash table entries: 4096 (order: 5, 131072 bytes)
[    0.180168] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes)
[    0.180218] NET: Registered protocol family 1
[    0.180365] pci 0000:08:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
[    0.180473] PCI: CLS 64 bytes, default 64
[    0.180503] Unpacking initramfs...
[    0.443231] Freeing initrd memory: 23628K
[    0.443250] AMD-Vi: IOMMU performance counters supported
[    0.443564] iommu: Adding device 0000:00:01.0 to group 0
[    0.443676] iommu: Adding device 0000:00:01.3 to group 1
[    0.443793] iommu: Adding device 0000:00:02.0 to group 2
[    0.443903] iommu: Adding device 0000:00:03.0 to group 3
[    0.444038] iommu: Adding device 0000:00:03.1 to group 4
[    0.444147] iommu: Adding device 0000:00:03.2 to group 5
[    0.444266] iommu: Adding device 0000:00:04.0 to group 6
[    0.444379] iommu: Adding device 0000:00:07.0 to group 7
[    0.444499] iommu: Adding device 0000:00:07.1 to group 8
[    0.444618] iommu: Adding device 0000:00:08.0 to group 9
[    0.444744] iommu: Adding device 0000:00:08.1 to group 10
[    0.444857] iommu: Adding device 0000:00:14.0 to group 11
[    0.444869] iommu: Adding device 0000:00:14.3 to group 11
[    0.444997] iommu: Adding device 0000:00:18.0 to group 12
[    0.445010] iommu: Adding device 0000:00:18.1 to group 12
[    0.445021] iommu: Adding device 0000:00:18.2 to group 12
[    0.445032] iommu: Adding device 0000:00:18.3 to group 12
[    0.445045] iommu: Adding device 0000:00:18.4 to group 12
[    0.445056] iommu: Adding device 0000:00:18.5 to group 12
[    0.445068] iommu: Adding device 0000:00:18.6 to group 12
[    0.445079] iommu: Adding device 0000:00:18.7 to group 12
[    0.445202] iommu: Adding device 0000:01:00.0 to group 13
[    0.445221] iommu: Adding device 0000:01:00.1 to group 13
[    0.445240] iommu: Adding device 0000:01:00.2 to group 13
[    0.445250] iommu: Adding device 0000:02:00.0 to group 13
[    0.445259] iommu: Adding device 0000:02:01.0 to group 13
[    0.445269] iommu: Adding device 0000:02:04.0 to group 13
[    0.445278] iommu: Adding device 0000:02:06.0 to group 13
[    0.445287] iommu: Adding device 0000:02:07.0 to group 13
[    0.445303] iommu: Adding device 0000:03:00.0 to group 13
[    0.445430] iommu: Adding device 0000:08:00.0 to group 14
[    0.445449] iommu: Using direct mapping for device 0000:08:00.0
[    0.445475] iommu: Adding device 0000:08:00.1 to group 14
[    0.445559] iommu: Adding device 0000:09:00.0 to group 15
[    0.445578] iommu: Using direct mapping for device 0000:09:00.0
[    0.445612] iommu: Adding device 0000:09:00.1 to group 15
[    0.445660] iommu: Adding device 0000:0a:00.0 to group 16
[    0.445762] iommu: Adding device 0000:0a:00.2 to group 17
[    0.445869] iommu: Adding device 0000:0a:00.3 to group 18
[    0.445990] iommu: Adding device 0000:0b:00.0 to group 19
[    0.446103] iommu: Adding device 0000:0b:00.2 to group 20
[    0.446225] iommu: Adding device 0000:0b:00.3 to group 21
[    0.446485] AMD-Vi: Found IOMMU at 0000:00:00.2 cap 0x40
[    0.446485] AMD-Vi: Extended features (0xf77ef22294ada):
[    0.446486]  PPR NX GT IA GA PC GA_vAPIC
[    0.446489] AMD-Vi: Interrupt remapping enabled
[    0.446489] AMD-Vi: virtual APIC enabled
[    0.446622] AMD-Vi: Lazy IO/TLB flushing enabled
[    0.447391] amd_uncore: AMD NB counters detected
[    0.447394] amd_uncore: AMD LLC counters detected
[    0.447988] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    0.448044] Scanning for low memory corruption every 60 seconds
[    0.448628] Initialise system trusted keyrings
[    0.448640] Key type blacklist registered
[    0.448700] workingset: timestamp_bits=36 max_order=21 bucket_order=0
[    0.449433] zbud: loaded
[    0.449809] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.449932] fuse init (API version 7.26)
[    0.451404] Key type asymmetric registered
[    0.451405] Asymmetric key parser 'x509' registered
[    0.451425] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
[    0.451482] io scheduler noop registered
[    0.451483] io scheduler deadline registered
[    0.451513] io scheduler cfq registered (default)
[    0.453535] pcieport 0000:00:01.3: AER enabled with IRQ 26
[    0.453550] pcieport 0000:00:03.1: AER enabled with IRQ 27
[    0.453565] pcieport 0000:00:03.2: AER enabled with IRQ 28
[    0.453578] pcieport 0000:00:07.1: AER enabled with IRQ 29
[    0.453591] pcieport 0000:00:08.1: AER enabled with IRQ 31
[    0.453602] pcieport 0000:00:01.3: Signaling PME with IRQ 26
[    0.453609] pcieport 0000:00:03.1: Signaling PME with IRQ 27
[    0.453618] pcieport 0000:00:03.2: Signaling PME with IRQ 28
[    0.453627] pcieport 0000:00:07.1: Signaling PME with IRQ 29
[    0.453639] pcieport 0000:00:08.1: Signaling PME with IRQ 31
[    0.453686] vesafb: mode is 1280x768x32, linelength=5120, pages=0
[    0.453686] vesafb: scrolling: redraw
[    0.453687] vesafb: Truecolor: size=0:8:8:8, shift=0:16:8:0
[    0.453695] vesafb: framebuffer at 0xe0000000, mapped to 0x        (ptrval), using 3840k, total 3840k
[    0.453764] Console: switching to colour frame buffer device 160x48
[    0.453776] fb0: VESA VGA frame buffer device
[    0.453862] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
[    0.453868] ACPI: Power Button [PWRB]
[    0.453894] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
[    0.453936] ACPI: Power Button [PWRF]
[    0.453991] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454136] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454221] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454355] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454474] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454601] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454669] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454771] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.454898] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.455047] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.455171] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.455293] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.455428] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.455558] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.455698] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.455812] [Firmware Bug]: ACPI MWAIT C-state 0x0 not supported by HW (0x0)
[    0.456059] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
[    0.476975] 00:04: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    0.478631] Linux agpgart interface v0.103
[    0.481168] loop: module loaded
[    0.481279] libphy: Fixed MDIO Bus: probed
[    0.481279] tun: Universal TUN/TAP device driver, 1.6
[    0.481311] PPP generic driver version 2.4.2
[    0.481347] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.481349] ehci-pci: EHCI PCI platform driver
[    0.481356] ehci-platform: EHCI generic platform driver
[    0.481360] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.481361] ohci-pci: OHCI PCI platform driver
[    0.481366] ohci-platform: OHCI generic platform driver
[    0.481369] uhci_hcd: USB Universal Host Controller Interface driver
[    0.481423] QUIRK: Enable AMD PLL fix
[    0.481433] xhci_hcd 0000:01:00.0: xHCI Host Controller
[    0.481437] xhci_hcd 0000:01:00.0: new USB bus registered, assigned bus number 1
[    0.536792] xhci_hcd 0000:01:00.0: hcc params 0x0200ef81 hci version 0x110 quirks 0x40000418
[    0.536912] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.536913] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.536914] usb usb1: Product: xHCI Host Controller
[    0.536915] usb usb1: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.536916] usb usb1: SerialNumber: 0000:01:00.0
[    0.537019] hub 1-0:1.0: USB hub found
[    0.537030] hub 1-0:1.0: 10 ports detected
[    0.542074] xhci_hcd 0000:01:00.0: xHCI Host Controller
[    0.542076] xhci_hcd 0000:01:00.0: new USB bus registered, assigned bus number 2
[    0.542078] xhci_hcd 0000:01:00.0: Host supports USB 3.10 Enhanced SuperSpeed
[    0.542102] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.542116] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003
[    0.542118] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.542119] usb usb2: Product: xHCI Host Controller
[    0.542120] usb usb2: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.542121] usb usb2: SerialNumber: 0000:01:00.0
[    0.542203] hub 2-0:1.0: USB hub found
[    0.542210] hub 2-0:1.0: 4 ports detected
[    0.544318] xhci_hcd 0000:0a:00.3: xHCI Host Controller
[    0.544321] xhci_hcd 0000:0a:00.3: new USB bus registered, assigned bus number 3
[    0.544427] xhci_hcd 0000:0a:00.3: hcc params 0x0270f665 hci version 0x100 quirks 0x00000418
[    0.544510] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002
[    0.544511] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.544512] usb usb3: Product: xHCI Host Controller
[    0.544513] usb usb3: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.544514] usb usb3: SerialNumber: 0000:0a:00.3
[    0.544594] hub 3-0:1.0: USB hub found
[    0.544600] hub 3-0:1.0: 4 ports detected
[    0.544719] xhci_hcd 0000:0a:00.3: xHCI Host Controller
[    0.544721] xhci_hcd 0000:0a:00.3: new USB bus registered, assigned bus number 4
[    0.544723] xhci_hcd 0000:0a:00.3: Host supports USB 3.0  SuperSpeed
[    0.544730] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    0.544740] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003
[    0.544741] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.544742] usb usb4: Product: xHCI Host Controller
[    0.544743] usb usb4: Manufacturer: Linux 4.15.0-33-generic xhci-hcd
[    0.544743] usb usb4: SerialNumber: 0000:0a:00.3
[    0.544815] hub 4-0:1.0: USB hub found
[    0.544821] hub 4-0:1.0: 4 ports detected
[    0.544941] i8042: PNP: No PS/2 controller found.
[    0.545008] mousedev: PS/2 mouse device common for all mice
[    0.545146] rtc_cmos 00:02: RTC can wake from S4
[    0.545350] rtc_cmos 00:02: rtc core: registered rtc_cmos as rtc0
[    0.545404] rtc_cmos 00:02: alarms up to one month, y3k, 114 bytes nvram, hpet irqs
[    0.545408] i2c /dev entries driver
[    0.545437] device-mapper: uevent: version 1.0.3
[    0.545488] device-mapper: ioctl: 4.37.0-ioctl (2017-09-20) initialised: dm-devel@redhat.com
[    0.545956] ledtrig-cpu: registered to indicate activity on CPUs
[    0.546318] NET: Registered protocol family 10
[    0.549217] Segment Routing with IPv6
[    0.549228] NET: Registered protocol family 17
[    0.549285] Key type dns_resolver registered
[    0.550193] RAS: Correctable Errors collector initialized.
[    0.551259] microcode: CPU0: patch_level=0x08001129
[    0.551274] microcode: CPU1: patch_level=0x08001129
[    0.551290] microcode: CPU2: patch_level=0x08001129
[    0.551296] microcode: CPU3: patch_level=0x08001129
[    0.551317] microcode: CPU4: patch_level=0x08001129
[    0.551330] microcode: CPU5: patch_level=0x08001129
[    0.551332] microcode: CPU6: patch_level=0x08001129
[    0.551341] microcode: CPU7: patch_level=0x08001129
[    0.551352] microcode: CPU8: patch_level=0x08001129
[    0.551359] microcode: CPU9: patch_level=0x08001129
[    0.551369] microcode: CPU10: patch_level=0x08001129
[    0.551384] microcode: CPU11: patch_level=0x08001129
[    0.551393] microcode: CPU12: patch_level=0x08001129
[    0.551407] microcode: CPU13: patch_level=0x08001129
[    0.551416] microcode: CPU14: patch_level=0x08001129
[    0.551424] microcode: CPU15: patch_level=0x08001129
[    0.551467] microcode: Microcode Update Driver: v2.2.
[    0.551475] sched_clock: Marking stable (551456366, 0)->(674416178, -122959812)
[    0.551815] registered taskstats version 1
[    0.551823] Loading compiled-in X.509 certificates
[    0.553345] Loaded X.509 cert 'Build time autogenerated kernel key: d918b280ed158d77154089242222928ec1ab43e6'
[    0.553363] zswap: loaded using pool lzo/zbud
[    0.555589] Key type big_key registered
[    0.555591] Key type trusted registered
[    0.556582] Key type encrypted registered
[    0.556584] AppArmor: AppArmor sha1 policy hashing enabled
[    0.556586] ima: No TPM chip found, activating TPM-bypass! (rc=-19)
[    0.556604] evm: HMAC attrs: 0x1
[    0.556909]   Magic number: 14:895:667
[    0.557053] rtc_cmos 00:02: setting system clock to 2018-08-31 04:41:34 UTC (1535690494)
[    0.557337] acpi_cpufreq: overriding BIOS provided _PSD data
[    0.557793] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
[    0.557794] EDD information not available.
[    0.876104] usb 1-6: new full-speed USB device number 2 using xhci_hcd
[    1.030527] Freeing unused kernel memory: 2404K
[    1.068529] Write protecting the kernel read-only data: 20480k
[    1.069968] Freeing unused kernel memory: 2008K
[    1.073157] Freeing unused kernel memory: 1892K
[    1.078734] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[    1.085797] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.085848] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.085855] random: systemd-udevd: uninitialized urandom read (16 bytes read)
[    1.126510] ahci 0000:01:00.1: version 3.0
[    1.126651] ahci 0000:01:00.1: SSS flag set, parallel bus scan disabled
[    1.126686] ahci 0000:01:00.1: AHCI 0001.0301 32 slots 8 ports 6 Gbps 0x33 impl SATA mode
[    1.126687] ahci 0000:01:00.1: flags: 64bit ncq sntf stag pm led clo only pmp pio slum part sxs deso sadm sds apst 
[    1.127138] scsi host0: ahci
[    1.127214] scsi host1: ahci
[    1.127303] scsi host2: ahci
[    1.127410] scsi host3: ahci
[    1.127543] pps_core: LinuxPPS API ver. 1 registered
[    1.127544] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    1.128804] PTP clock support registered
[    1.129950] dca service started, version 1.12.1
[    1.130203] scsi host4: ahci
[    1.130912] scsi host5: ahci
[    1.134190] igb: Intel(R) Gigabit Ethernet Network Driver - version 5.4.0-k
[    1.134193] igb: Copyright (c) 2007-2014 Intel Corporation.
[    1.134743] scsi host6: ahci
[    1.134854] scsi host7: ahci
[    1.134883] ata1: SATA max UDMA/133 abar m131072@0xfe680000 port 0xfe680100 irq 45
[    1.134885] ata2: SATA max UDMA/133 abar m131072@0xfe680000 port 0xfe680180 irq 45
[    1.134886] ata3: DUMMY
[    1.134886] ata4: DUMMY
[    1.134888] ata5: SATA max UDMA/133 abar m131072@0xfe680000 port 0xfe680300 irq 45
[    1.134889] ata6: SATA max UDMA/133 abar m131072@0xfe680000 port 0xfe680380 irq 45
[    1.134890] ata7: DUMMY
[    1.134890] ata8: DUMMY
[    1.135111] ahci 0000:0b:00.2: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0xc impl SATA mode
[    1.135113] ahci 0000:0b:00.2: flags: 64bit ncq sntf ilck pm led clo only pmp fbs pio slum part 
[    1.135115] ahci 0000:0b:00.2: both AHCI_HFLAG_MULTI_MSI flag set and custom irq handler implemented
[    1.135388] scsi host8: ahci
[    1.135465] scsi host9: ahci
[    1.135534] scsi host10: ahci
[    1.135604] scsi host11: ahci
[    1.135624] ata9: DUMMY
[    1.135625] ata10: DUMMY
[    1.135626] ata11: SATA max UDMA/133 abar m4096@0xfe708000 port 0xfe708200 irq 49
[    1.135627] ata12: SATA max UDMA/133 abar m4096@0xfe708000 port 0xfe708280 irq 50
[    1.211146] usb 1-6: New USB device found, idVendor=24ae, idProduct=1006
[    1.211148] usb 1-6: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[    1.211149] usb 1-6: Product: Rapoo 2.4G Wireless Touchpad Keyboard
[    1.211150] usb 1-6: Manufacturer: RAPOO
[    1.216574] hidraw: raw HID events driver (C) Jiri Kosina
[    1.234836] usbcore: registered new interface driver usbhid
[    1.234837] usbhid: USB HID core driver
[    1.235992] input: RAPOO Rapoo 2.4G Wireless Touchpad Keyboard as /devices/pci0000:00/0000:00:01.3/0000:01:00.0/usb1/1-6/1-6:1.0/0003:24AE:1006.0001/input/input2
[    1.236069] hid-generic 0003:24AE:1006.0001: input,hidraw0: USB HID v1.10 Mouse [RAPOO Rapoo 2.4G Wireless Touchpad Keyboard] on usb-0000:01:00.0-6/input0
[    1.236230] input: RAPOO Rapoo 2.4G Wireless Touchpad Keyboard as /devices/pci0000:00/0000:00:01.3/0000:01:00.0/usb1/1-6/1-6:1.1/0003:24AE:1006.0002/input/input3
[    1.241028] usb 2-2: new SuperSpeed USB device number 2 using xhci_hcd
[    1.267603] usb 2-2: New USB device found, idVendor=0781, idProduct=5583
[    1.267606] usb 2-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[    1.267607] usb 2-2: Product: Ultra Fit
[    1.267608] usb 2-2: Manufacturer: SanDisk
[    1.267609] usb 2-2: SerialNumber: 4C530001110228108541
[    1.272187] usb-storage 2-2:1.0: USB Mass Storage device detected
[    1.272301] scsi host12: usb-storage 2-2:1.0
[    1.272344] usbcore: registered new interface driver usb-storage
[    1.273095] usbcore: registered new interface driver uas
[    1.296747] hid-generic 0003:24AE:1006.0002: input,hiddev0,hidraw1: USB HID v1.10 Device [RAPOO Rapoo 2.4G Wireless Touchpad Keyboard] on usb-0000:01:00.0-6/input1
[    1.297030] input: RAPOO Rapoo 2.4G Wireless Touchpad Keyboard as /devices/pci0000:00/0000:00:01.3/0000:01:00.0/usb1/1-6/1-6:1.2/0003:24AE:1006.0003/input/input4
[    1.356277] hid-generic 0003:24AE:1006.0003: input,hidraw2: USB HID v1.10 Keyboard [RAPOO Rapoo 2.4G Wireless Touchpad Keyboard] on usb-0000:01:00.0-6/input2
[    1.368169] pps pps0: new PPS source ptp0
[    1.368171] igb 0000:03:00.0: added PHC on eth0
[    1.368172] igb 0000:03:00.0: Intel(R) Gigabit Ethernet Network Connection
[    1.368173] igb 0000:03:00.0: eth0: (PCIe:2.5Gb/s:Width x1) 88:d7:f6:c7:2d:d8
[    1.368174] igb 0000:03:00.0: eth0: PBA No: FFFFFF-0FF
[    1.368175] igb 0000:03:00.0: Using MSI-X interrupts. 2 rx queue(s), 2 tx queue(s)
[    1.368817] igb 0000:03:00.0 enp3s0: renamed from eth0
[    1.449831] ata1: SATA link down (SStatus 0 SControl 300)
[    1.468202] tsc: Refined TSC clocksource calibration: 3693.062 MHz
[    1.468220] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x6a7777116fa, max_idle_ns: 881590883556 ns
[    1.612609] ata12: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    1.612751] ata12.00: ATA-11: SPCC Solid State Disk, SBFM71.1, max UDMA/133
[    1.612752] ata12.00: 234441648 sectors, multi 16: LBA48 NCQ (depth 31/32), AA
[    1.612870] ata12.00: configured for UDMA/133
[    1.765628] ata2: SATA link down (SStatus 0 SControl 300)
[    2.077003] ata5: SATA link down (SStatus 0 SControl 300)
[    2.088601] ata11: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
[    2.090078] ata11.00: CFA: SINTECHI HighSpeed SD to CF Adapter V1.0, Rev 1.2, max UDMA/100
[    2.090080] ata11.00: 65536 sectors, multi 1: LBA 
[    2.091617] ata11.00: configured for UDMA/100
[    2.301617] scsi 12:0:0:0: Direct-Access     SanDisk  Ultra Fit        1.00 PQ: 0 ANSI: 6
[    2.301934] sd 12:0:0:0: Attached scsi generic sg0 type 0
[    2.302101] sd 12:0:0:0: [sda] 30375936 512-byte logical blocks: (15.6 GB/14.5 GiB)
[    2.302884] sd 12:0:0:0: [sda] Write Protect is off
[    2.302886] sd 12:0:0:0: [sda] Mode Sense: 43 00 00 00
[    2.303875] sd 12:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    2.319663]  sda: sda1 sda2
[    2.322159] sd 12:0:0:0: [sda] Attached SCSI removable disk
[    2.338404] random: fast init done
[    2.388227] ata6: SATA link down (SStatus 0 SControl 300)
[    2.388479] scsi 10:0:0:0: Direct-Access     ATA      SINTECHI HighSpe 1.2  PQ: 0 ANSI: 5
[    2.388593] sd 10:0:0:0: [sdb] 65536 512-byte logical blocks: (33.6 MB/32.0 MiB)
[    2.388599] sd 10:0:0:0: [sdb] Write Protect is off
[    2.388600] sd 10:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[    2.388608] sd 10:0:0:0: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    2.388632] sd 10:0:0:0: Attached scsi generic sg1 type 0
[    2.388826] scsi 11:0:0:0: Direct-Access     ATA      SPCC Solid State 71.1 PQ: 0 ANSI: 5
[    2.388940] sd 11:0:0:0: [sdc] 234441648 512-byte logical blocks: (120 GB/112 GiB)
[    2.388947] sd 11:0:0:0: Attached scsi generic sg2 type 0
[    2.388947] sd 11:0:0:0: [sdc] Write Protect is off
[    2.388949] sd 11:0:0:0: [sdc] Mode Sense: 00 3a 00 00
[    2.388959] sd 11:0:0:0: [sdc] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    2.389334] sd 10:0:0:0: [sdb] Attached SCSI disk
[    2.389514]  sdc: sdc1 sdc2 < sdc5 >
[    2.389754] sd 11:0:0:0: [sdc] Attached SCSI disk
[    2.475342] EXT4-fs (dm-0): mounted filesystem with ordered data mode. Opts: (null)
[    2.496760] clocksource: Switched to clocksource tsc
[    2.625944] systemd[1]: systemd 229 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN)
[    2.644717] systemd[1]: Detected architecture x86-64.
[    2.644964] systemd[1]: Set hostname to <demon>.
[    2.748303] systemd[1]: Listening on Journal Socket (/dev/log).
[    2.748354] systemd[1]: Listening on udev Control Socket.
[    2.748360] systemd[1]: Reached target Remote File Systems (Pre).
[    2.748370] systemd[1]: Listening on fsck to fsckd communication Socket.
[    2.748384] systemd[1]: Listening on LVM2 poll daemon socket.
[    2.748420] systemd[1]: Listening on Journal Audit Socket.
[    2.748427] systemd[1]: Reached target Remote File Systems.
[    3.062076] lp: driver loaded but no devices found
[    3.063657] ppdev: user-space parallel port driver
[    3.182762] EXT4-fs (dm-0): re-mounted. Opts: errors=remount-ro
[    3.219893] systemd-journald[404]: Received request to flush runtime journal from PID 1
[    3.415715] AVX2 version of gcm_enc/dec engaged.
[    3.415716] AES CTR mode by8 optimization enabled
[    3.465187] kvm: Nested Virtualization enabled
[    3.465192] kvm: Nested Paging enabled
[    3.465192] SVM: Virtual VMLOAD VMSAVE supported
[    3.465193] SVM: Virtual GIF supported
[    3.508991] Adding 16777212k swap on /swapfile.  Priority:-2 extents:21 across:21307388k SSFS
[    3.589533] random: crng init done
[    3.589534] random: 7 urandom warning(s) missed due to ratelimiting
[    3.873721] EXT4-fs (sdc1): mounting ext2 file system using the ext4 subsystem
[    3.875916] EXT4-fs (sdc1): mounted filesystem without journal. Opts: (null)
[    4.008126] audit: type=1400 audit(1535690497.943:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/ippusbxd" pid=1025 comm="apparmor_parser"
[    4.008514] audit: type=1400 audit(1535690497.947:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=1023 comm="apparmor_parser"
[    4.008569] audit: type=1400 audit(1535690497.947:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/tcpdump" pid=1027 comm="apparmor_parser"
[    4.009444] audit: type=1400 audit(1535690497.947:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session" pid=1017 comm="apparmor_parser"
[    4.009447] audit: type=1400 audit(1535690497.947:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/lightdm/lightdm-guest-session//chromium" pid=1017 comm="apparmor_parser"
[    4.009501] audit: type=1400 audit(1535690497.947:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=1018 comm="apparmor_parser"
[    4.009504] audit: type=1400 audit(1535690497.947:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=1018 comm="apparmor_parser"
[    4.009506] audit: type=1400 audit(1535690497.947:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=1018 comm="apparmor_parser"
[    4.009508] audit: type=1400 audit(1535690497.947:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=1018 comm="apparmor_parser"
[    4.997949] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[    5.023867] IPv6: ADDRCONF(NETDEV_UP): enp3s0: link is not ready
[    7.689153] igb 0000:03:00.0 enp3s0: igb: enp3s0 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: RX/TX
[    7.689475] IPv6: ADDRCONF(NETDEV_CHANGE): enp3s0: link becomes ready
[   13.473418] aufs 4.15-20180219
[   13.506354] kauditd_printk_skb: 13 callbacks suppressed
[   13.506355] audit: type=1400 audit(1535690507.443:24): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-default" pid=2284 comm="apparmor_parser"
[   13.560476] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[   13.561267] Bridge firewalling registered
[   13.565516] nf_conntrack version 0.5.0 (65536 buckets, 262144 max)
[   13.574893] ip_tables: (C) 2000-2006 Netfilter Core Team
[   13.763564] Initializing XFRM netlink socket
[   13.766254] Netfilter messages via NETLINK v0.30.
[   13.767210] ctnetlink v0.93: registering with nfnetlink.
[   13.955174] IPv6: ADDRCONF(NETDEV_UP): docker0: link is not ready
[   14.195771] docker0: port 1(vethd498f9e) entered blocking state
[   14.195773] docker0: port 1(vethd498f9e) entered disabled state
[   14.195805] device vethd498f9e entered promiscuous mode
[   14.195855] IPv6: ADDRCONF(NETDEV_UP): vethd498f9e: link is not ready
[   14.195857] docker0: port 1(vethd498f9e) entered blocking state
[   14.195858] docker0: port 1(vethd498f9e) entered forwarding state
[   14.195890] docker0: port 1(vethd498f9e) entered disabled state
[   14.392889] eth0: renamed from veth68a9cca
[   14.416359] IPv6: ADDRCONF(NETDEV_CHANGE): vethd498f9e: link becomes ready
[   14.416389] docker0: port 1(vethd498f9e) entered blocking state
[   14.416391] docker0: port 1(vethd498f9e) entered forwarding state
[   14.416421] IPv6: ADDRCONF(NETDEV_CHANGE): docker0: link becomes ready
```


---

### 评论 #12 — jlgreathouse (2018-08-31T21:55:06Z)

@calvintam236 it's probably a bad idea to piggyback your tech support request on an already-closed thread. It's a good way to get your problem ignored. :) This is a common error that is often because of a misconfigured system, so it's not like we're going to reopen issues like this each time a user sees the problem.

That said, it looks like you don't have the package `rocm-dkms` installed. In addition, you don't have the `amdgpu` or `amdkfd` modules loaded, so it's likely that you also do not have the `rock-dkms` package installed.

---

### 评论 #13 — calvintam236 (2018-09-01T07:06:18Z)

@jlgreathouse sorry about that. I did `apt install rocm-dkms`, and I'm still getting this error.

```console
$ dpkg -l | grep rocm
ii  rocm-clang-ocl                             0.3.0-7997136                                amd64        OpenCL compilation with clang compiler.
ii  rocm-dev                                   1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                           0.0.1                                        amd64        Radeon Open Compute - device libraries
ii  rocm-dkms                                  1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl                                1.2.0-2018082755                             amd64        OpenCL/ROCm
ii  rocm-opencl-dev                            1.2.0-2018082755                             amd64        OpenCL/ROCm
ii  rocm-smi                                   1.0.0-46-g81ef66f                            amd64        System Management Interface for ROCm
ii  rocm-utils                                 1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                                   1.0.0                                        amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool

$ dpkg -l | grep rock
ii  rock-dkms                                  1.8-199                                      all          rock-dkms driver in DKMS format.

$ lsmod | grep amd
amdgpu               2719744  44
amdchash               16384  1 amdgpu
amd_sched              24576  1 amdgpu
amdttm                110592  1 amdgpu
kvm_amd                86016  0
kvm                   598016  1 kvm_amd
amdkcl                 28672  3 amdttm,amdgpu,amd_sched
drm_kms_helper        172032  1 amdgpu
drm                   401408  12 amdttm,amdgpu,amdkcl,amd_sched,drm_kms_helper
i2c_algo_bit           16384  2 igb,amdgpu

$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-33-generic (buildd@lgw01-amd64-010) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 (Ubuntu 4.15.0-33.36~16.04.1-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.15.0-33-generic root=/dev/mapper/demon--vg-root ro splash quiet amdgpu.vm_fragment_size=9 vt.handoff=7
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.15.0-33-generic root=/dev/mapper/demon--vg-root ro splash quiet amdgpu.vm_fragment_size=9 vt.handoff=7
[    0.451404] amd_uncore: AMD NB counters detected
[    0.451407] amd_uncore: AMD LLC counters detected
[    0.451991] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    3.445637] amdkcl: loading out-of-tree module taints kernel.
[    3.445660] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    3.582568] [drm] amdgpu kernel modesetting enabled.
[    3.586817] amdkfd: Unknown symbol amd_iommu_unbind_pasid (err 0)
[    3.586869] amdkfd: Unknown symbol amd_iommu_set_invalidate_ctx_cb (err 0)
[    3.586941] amdkfd: Unknown symbol amd_iommu_free_device (err 0)
[    3.586952] amdkfd: Unknown symbol amd_iommu_init_device (err 0)
[    3.586966] amdkfd: Unknown symbol amd_iommu_set_invalid_ppr_cb (err 0)
[    3.586989] amdkfd: Unknown symbol amd_iommu_bind_pasid (err 0)
[    3.608399] fb: switching to amdgpudrmfb from VESA VGA
[    3.608780] [drm] add ip block number 3 <amdgpu_powerplay>
[    3.608982] amdgpu 0000:08:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    3.629160] amdgpu 0000:08:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    3.629162] amdgpu 0000:08:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    3.629290] [drm] amdgpu: 4096M of VRAM memory ready
[    3.629291] [drm] amdgpu: 7974M of GTT memory ready.
[    4.446681] fbcon: amdgpudrmfb (fb0) is primary device
[    4.446751] amdgpu 0000:08:00.0: fb0: amdgpudrmfb frame buffer device
[    4.647976] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:08:00.0 on minor 0
[    4.648907] amdkfd: Unknown symbol amd_iommu_unbind_pasid (err 0)
[    4.648958] amdkfd: Unknown symbol amd_iommu_set_invalidate_ctx_cb (err 0)
[    4.649034] amdkfd: Unknown symbol amd_iommu_free_device (err 0)
[    4.649045] amdkfd: Unknown symbol amd_iommu_init_device (err 0)
[    4.649059] amdkfd: Unknown symbol amd_iommu_set_invalid_ppr_cb (err 0)
[    4.649083] amdkfd: Unknown symbol amd_iommu_bind_pasid (err 0)
[    4.840395] amdgpu 0000:09:00.0: enabling device (0000 -> 0003)
[    4.855125] [drm] add ip block number 3 <amdgpu_powerplay>
[    5.192370] amdgpu 0000:09:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    5.192371] amdgpu 0000:09:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    5.192433] [drm] amdgpu: 4096M of VRAM memory ready
[    5.192436] [drm] amdgpu: 7974M of GTT memory ready.
[    6.048786] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:09:00.0 on minor 1
[    6.488477] amdgpu 0000:09:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    6.488479] amdgpu 0000:08:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=io+mem
```
No idea how to proceed.

---

### 评论 #14 — gstoner (2018-09-01T12:51:07Z)

Your running this via virtualized stack KVM with pass through did you follow the instructions in the documentation for this https://rocm-documentation.readthedocs.io/en/latest/ROCm_Virtualization_Containers/ROCm-Virtualization-&-Containers.html

Get Outlook for iOS<https://aka.ms/o0ukef>

________________________________
From: Calvin Tam <notifications@github.com>
Sent: Saturday, September 1, 2018 2:06 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104 (#415)


@jlgreathouse<https://github.com/jlgreathouse> sorry about that. I did apt install rocm-dkms, and I'm still getting this error.

$ dpkg -l | grep rocm
ii  rocm-clang-ocl                             0.3.0-7997136                                amd64        OpenCL compilation with clang compiler.
ii  rocm-dev                                   1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                           0.0.1                                        amd64        Radeon Open Compute - device libraries
ii  rocm-dkms                                  1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl                                1.2.0-2018082755                             amd64        OpenCL/ROCm
ii  rocm-opencl-dev                            1.2.0-2018082755                             amd64        OpenCL/ROCm
ii  rocm-smi                                   1.0.0-46-g81ef66f                            amd64        System Management Interface for ROCm
ii  rocm-utils                                 1.8.199                                      amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                                   1.0.0                                        amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool

$ dpkg -l | grep rock
ii  rock-dkms                                  1.8-199                                      all          rock-dkms driver in DKMS format.

$ lsmod | grep amd
amdgpu               2719744  44
amdchash               16384  1 amdgpu
amd_sched              24576  1 amdgpu
amdttm                110592  1 amdgpu
kvm_amd                86016  0
kvm                   598016  1 kvm_amd
amdkcl                 28672  3 amdttm,amdgpu,amd_sched
drm_kms_helper        172032  1 amdgpu
drm                   401408  12 amdttm,amdgpu,amdkcl,amd_sched,drm_kms_helper
i2c_algo_bit           16384  2 igb,amdgpu

$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-33-generic (buildd@lgw01-amd64-010) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)) #36~16.04.1-Ubuntu SMP Wed Aug 15 17:21:05 UTC 2018 (Ubuntu 4.15.0-33.36~16.04.1-generic 4.15.18)
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.15.0-33-generic root=/dev/mapper/demon--vg-root ro splash quiet amdgpu.vm_fragment_size=9 vt.handoff=7
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.15.0-33-generic root=/dev/mapper/demon--vg-root ro splash quiet amdgpu.vm_fragment_size=9 vt.handoff=7
[    0.451404] amd_uncore: AMD NB counters detected
[    0.451407] amd_uncore: AMD LLC counters detected
[    0.451991] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    3.445637] amdkcl: loading out-of-tree module taints kernel.
[    3.445660] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    3.582568] [drm] amdgpu kernel modesetting enabled.
[    3.586817] amdkfd: Unknown symbol amd_iommu_unbind_pasid (err 0)
[    3.586869] amdkfd: Unknown symbol amd_iommu_set_invalidate_ctx_cb (err 0)
[    3.586941] amdkfd: Unknown symbol amd_iommu_free_device (err 0)
[    3.586952] amdkfd: Unknown symbol amd_iommu_init_device (err 0)
[    3.586966] amdkfd: Unknown symbol amd_iommu_set_invalid_ppr_cb (err 0)
[    3.586989] amdkfd: Unknown symbol amd_iommu_bind_pasid (err 0)
[    3.608399] fb: switching to amdgpudrmfb from VESA VGA
[    3.608780] [drm] add ip block number 3 <amdgpu_powerplay>
[    3.608982] amdgpu 0000:08:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    3.629160] amdgpu 0000:08:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    3.629162] amdgpu 0000:08:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    3.629290] [drm] amdgpu: 4096M of VRAM memory ready
[    3.629291] [drm] amdgpu: 7974M of GTT memory ready.
[    4.446681] fbcon: amdgpudrmfb (fb0) is primary device
[    4.446751] amdgpu 0000:08:00.0: fb0: amdgpudrmfb frame buffer device
[    4.647976] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:08:00.0 on minor 0
[    4.648907] amdkfd: Unknown symbol amd_iommu_unbind_pasid (err 0)
[    4.648958] amdkfd: Unknown symbol amd_iommu_set_invalidate_ctx_cb (err 0)
[    4.649034] amdkfd: Unknown symbol amd_iommu_free_device (err 0)
[    4.649045] amdkfd: Unknown symbol amd_iommu_init_device (err 0)
[    4.649059] amdkfd: Unknown symbol amd_iommu_set_invalid_ppr_cb (err 0)
[    4.649083] amdkfd: Unknown symbol amd_iommu_bind_pasid (err 0)
[    4.840395] amdgpu 0000:09:00.0: enabling device (0000 -> 0003)
[    4.855125] [drm] add ip block number 3 <amdgpu_powerplay>
[    5.192370] amdgpu 0000:09:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    5.192371] amdgpu 0000:09:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    5.192433] [drm] amdgpu: 4096M of VRAM memory ready
[    5.192436] [drm] amdgpu: 7974M of GTT memory ready.
[    6.048786] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:09:00.0 on minor 1
[    6.488477] amdgpu 0000:09:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=none
[    6.488479] amdgpu 0000:08:00.0: vgaarb: changed VGA decodes: olddecodes=io+mem,decodes=none:owns=io+mem

No idea how to proceed.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/415#issuecomment-417838640>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuTIL_-LxSRdtSTrt_Cl-wQJJG1Wpks5uWjHtgaJpZM4T89wD>.


---

### 评论 #15 — calvintam236 (2018-09-01T18:17:37Z)

@gstoner Well, I'm not running any KVM. I only run Docker, which is not KVM. I have no such problem in other machines to use docker after installing rocm-dkms..

---

### 评论 #16 — gstoner (2018-09-01T20:45:30Z)

@calvintam236 your base driver is not loading,  did you try upgrading the base driver to 1.8.3 current most Ubuntu base driver which broke the KCL for DKMS in base AMDGPU Kernel Driver in 1.8.2 

---

### 评论 #17 — calvintam236 (2018-09-02T07:07:11Z)

@gstoner I ran `apt update` (ROCm via apt), and I am getting `All packages are up to date.`, so I believe I'm on the latest release.

Looks like someone else posted an issue on the same problem as I have at #519. We can continue over there.

---

### 评论 #18 — gstoner (2018-09-02T13:06:22Z)

Did remove the old driver before updating.  What cpu and gpu are you ussing are you on PCIe gen 3 lane off cpu directly  If your on Vega10 Polaris or Fiji card.   Or plx PCIe switch which is off main PCIe toot complex off the main cpu. Aka not running off the south bridge

Get Outlook for iOS<https://aka.ms/o0ukef>

________________________________
From: Calvin Tam <notifications@github.com>
Sent: Sunday, September 2, 2018 2:07 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104 (#415)


@gstoner<https://github.com/gstoner> I ran apt update (ROCm via apt), and I am getting All packages are up to date., so I believe I'm on the latest release.

Looks like someone else posted an issue on the same problem as I have at #519<https://github.com/RadeonOpenCompute/ROCm/issues/519>. We can continue over there.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/415#issuecomment-417909914>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQQ4A4bHXbXFKq_A-jfH7YpSKXFRks5uW4OhgaJpZM4T89wD>.


---

### 评论 #19 — calvintam236 (2018-09-02T18:10:47Z)

@gstoner Hardware spec:
Ryzen 1700X + 2x RX470. They're on PCIe 3 slots. ROCm was working in the last 8 months until last week.

---

### 评论 #20 — jlgreathouse (2018-09-02T18:31:18Z)

Your kfd module is broken for some reason -- likely due to a failed upgrade. The inability to rocm `rocminfo` is because you don't have a working KFD.

I don't know how easy it's going to be for us to walk through how to fix this, and I'm not sure how educational it would be for future readers to try a dozen possible ways of fixing this, since it's likely this issue is specific to your exact installation. The simplest way to fix this would be to reinstall Ubuntu from scratch, though I understand that's not ideal and may cause you a lot of needless hassle. That said, if you're primarily looking to get ROCm back up and running, installing everything from scratch should work if you haven't changed anything about your hardware lately.

Could you attempt to autoremove/purge the package `rock-dkms`? e.g. `sudo apt autoremove rock-dkms` and then reinstall it?

While you are installing it, could you please gather what is printed to the screen and save it / attach it here? I suspect that something is going wrong during the installation but you haven't shown us how your installation process went.

---

### 评论 #21 — calvintam236 (2018-09-02T19:18:50Z)

@jlgreathouse I have attempted `apt purge rocm-dkms && apt autoremove` yesterday and reinstall `rocm-dkms` after reboot. Even I want to the reinstallation Ubuntu, I'm 15 hours flight away from the machine.. It's not an option.

Attached logs for reinstallation today:
```console
$ apt purge rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs
  rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo
Use 'apt autoremove' to remove them.
The following packages will be REMOVED:
  rocm-dkms*
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 1,024 B disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 231071 files and directories currently installed.)
Removing rocm-dkms (1.8.199) ...

$ apt autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs
  rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo
0 upgraded, 0 newly installed, 19 to remove and 0 not upgraded.
After this operation, 1,843 MB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 231070 files and directories currently installed.)
Removing rocm-dev (1.8.199) ...
Removing hip_hcc (1.5.18276) ...
Removing hcc (1.2.18272) ...
Removing hip_doc (1.5.18276) ...
Removing hip_samples (1.5.18276) ...
Removing hip_base (1.5.18276) ...
Removing hsa-amd-aqlprofile (1.0.0) ...
Removing rocm-utils (1.8.199) ...
Removing rocm-clang-ocl (0.3.0-7997136) ...
Removing rocm-opencl-dev (1.2.0-2018082755) ...
Removing rocm-opencl (1.2.0-2018082755) ...
Removing hsa-rocr-dev (1.1.8-15-ge851b7a) ...
Removing hsa-ext-rocr-dev (1.1.8-15-ge851b7a) ...
Removing hsakmt-roct-dev (1.0.8-2-g2076b0c) ...
Removing hsakmt-roct (1.0.8-2-g2076b0c) ...
Removing rock-dkms (1.8-199) ...

-------- Uninstall Beginning --------
Module:  amdgpu
Version: 1.8-199
Kernel:  4.15.0-33-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

amdgpu.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdttm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdkcl.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdkfd.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amdchash.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


amd-sched.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-33-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


Running the post_remove script:
depmod....

Backing up initrd.img-4.15.0-33-generic to /boot/initrd.img-4.15.0-33-generic.old-dkms
Making new initrd.img-4.15.0-33-generic
(If next boot fails, revert to initrd.img-4.15.0-33-generic.old-dkms image)
update-initramfs....

DKMS: uninstall completed.

------------------------------
Deleting module version: 1.8-199
completely from the DKMS tree.
------------------------------
Done.
Removing rocm-device-libs (0.0.1) ...
Removing rocm-smi (1.0.0-46-g81ef66f) ...
Removing rocminfo (1.0.0) ...
dpkg: warning: while removing rocminfo, directory '/opt/rocm' not empty so not removed
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for initramfs-tools (0.122ubuntu8.11) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-33-generic

$ apt install --reinstall linux-image-4.15.0-33-generic
Reading package lists... Done
Building dependency tree       
Reading state information... Done
0 upgraded, 0 newly installed, 1 reinstalled, 0 to remove and 0 not upgraded.
Need to get 7,887 kB of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 http://hk.archive.ubuntu.com/ubuntu xenial-updates/main amd64 linux-image-4.15.0-33-generic amd64 4.15.0-33.36~16.04.1 [7,887 kB]
Fetched 7,887 kB in 0s (9,659 kB/s)                     
Selecting previously unselected package linux-image-4.15.0-33-generic.
(Reading database ... 228288 files and directories currently installed.)
Preparing to unpack .../linux-image-4.15.0-33-generic_4.15.0-33.36~16.04.1_amd64.deb ...
Unpacking linux-image-4.15.0-33-generic (4.15.0-33.36~16.04.1) over (4.15.0-33.36~16.04.1) ...
Setting up linux-image-4.15.0-33-generic (4.15.0-33.36~16.04.1) ...
Processing triggers for linux-image-4.15.0-33-generic (4.15.0-33.36~16.04.1) ...
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-4.15.0-33-generic
/etc/kernel/postinst.d/zz-update-grub:
Generating grub configuration file ...
Warning: Setting GRUB_TIMEOUT to a non-zero value when GRUB_HIDDEN_TIMEOUT is set is no longer supported.
Found linux image: /boot/vmlinuz-4.15.0-33-generic
Found initrd image: /boot/initrd.img-4.15.0-33-generic
Found linux image: /boot/vmlinuz-4.15.0-32-generic
Found initrd image: /boot/initrd.img-4.15.0-32-generic
Found memtest86+ image: /memtest86+.elf
Found memtest86+ image: /memtest86+.bin
Found Windows Recovery Environment (loader) on /dev/sda1
done

(REBOOT)
$ apt install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs
  rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo
The following NEW packages will be installed:
  hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs rocm-dkms
  rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo
0 upgraded, 20 newly installed, 0 to remove and 0 not upgraded.
Need to get 372 MB of archives.
After this operation, 1,843 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-ext-rocr-dev amd64 1.1.8-15-ge851b7a [9,165 kB]
Get:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct amd64 1.0.8-2-g2076b0c [48.9 kB]
Get:3 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsakmt-roct-dev amd64 1.0.8-2-g2076b0c [23.5 kB]
Get:4 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-rocr-dev amd64 1.1.8-15-ge851b7a [386 kB]
Get:5 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocminfo amd64 1.0.0 [18.4 kB]
Get:6 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl amd64 1.2.0-2018082755 [39.8 MB]
Get:7 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-opencl-dev amd64 1.2.0-2018082755 [16.5 MB]                                                                      
Get:8 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-clang-ocl amd64 0.3.0-7997136 [1,548 B]                                                                          
Get:9 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-utils amd64 1.8.199 [768 B]                                                                                      
Get:10 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hcc amd64 1.2.18272 [294 MB]                                                                                         
Get:11 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_base amd64 1.5.18276 [257 kB]                                                                                    
Get:12 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_doc amd64 1.5.18276 [676 kB]                                                                                     
Get:13 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_hcc amd64 1.5.18276 [5,567 kB]                                                                                   
Get:14 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip_samples amd64 1.5.18276 [64.6 kB]                                                                                
Get:15 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-amd-aqlprofile amd64 1.0.0 [55.8 kB]                                                                             
Get:16 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms all 1.8-199 [5,281 kB]                                                                                     
Get:17 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-device-libs amd64 0.0.1 [717 kB]                                                                                
Get:18 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi amd64 1.0.0-46-g81ef66f [9,370 B]                                                                           
Get:19 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dev amd64 1.8.199 [830 B]                                                                                       
Get:20 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dkms amd64 1.8.199 [1,002 B]                                                                                    
Fetched 372 MB in 32s (11.4 MB/s)                                                                                                                                                    
Selecting previously unselected package hsa-ext-rocr-dev.
(Reading database ... 228288 files and directories currently installed.)
Preparing to unpack .../hsa-ext-rocr-dev_1.1.8-15-ge851b7a_amd64.deb ...
Unpacking hsa-ext-rocr-dev (1.1.8-15-ge851b7a) ...
Selecting previously unselected package hsakmt-roct.
Preparing to unpack .../hsakmt-roct_1.0.8-2-g2076b0c_amd64.deb ...
Unpacking hsakmt-roct (1.0.8-2-g2076b0c) ...
Selecting previously unselected package hsakmt-roct-dev.
Preparing to unpack .../hsakmt-roct-dev_1.0.8-2-g2076b0c_amd64.deb ...
Unpacking hsakmt-roct-dev (1.0.8-2-g2076b0c) ...
Selecting previously unselected package hsa-rocr-dev.
Preparing to unpack .../hsa-rocr-dev_1.1.8-15-ge851b7a_amd64.deb ...
Unpacking hsa-rocr-dev (1.1.8-15-ge851b7a) ...
Selecting previously unselected package rocminfo.
Preparing to unpack .../rocminfo_1.0.0_amd64.deb ...
Unpacking rocminfo (1.0.0) ...
Selecting previously unselected package rocm-opencl.
Preparing to unpack .../rocm-opencl_1.2.0-2018082755_amd64.deb ...
Unpacking rocm-opencl (1.2.0-2018082755) ...
Selecting previously unselected package rocm-opencl-dev.
Preparing to unpack .../rocm-opencl-dev_1.2.0-2018082755_amd64.deb ...
Unpacking rocm-opencl-dev (1.2.0-2018082755) ...
Selecting previously unselected package rocm-clang-ocl.
Preparing to unpack .../rocm-clang-ocl_0.3.0-7997136_amd64.deb ...
Unpacking rocm-clang-ocl (0.3.0-7997136) ...
Selecting previously unselected package rocm-utils.
Preparing to unpack .../rocm-utils_1.8.199_amd64.deb ...
Unpacking rocm-utils (1.8.199) ...
Selecting previously unselected package hcc.
Preparing to unpack .../hcc_1.2.18272_amd64.deb ...
Unpacking hcc (1.2.18272) ...
Selecting previously unselected package hip_base.
Preparing to unpack .../hip%5fbase_1.5.18276_amd64.deb ...
Unpacking hip_base (1.5.18276) ...
Selecting previously unselected package hip_doc.
Preparing to unpack .../hip%5fdoc_1.5.18276_amd64.deb ...
Unpacking hip_doc (1.5.18276) ...
Selecting previously unselected package hip_hcc.
Preparing to unpack .../hip%5fhcc_1.5.18276_amd64.deb ...
Unpacking hip_hcc (1.5.18276) ...
Selecting previously unselected package hip_samples.
Preparing to unpack .../hip%5fsamples_1.5.18276_amd64.deb ...
Unpacking hip_samples (1.5.18276) ...
Selecting previously unselected package hsa-amd-aqlprofile.
Preparing to unpack .../hsa-amd-aqlprofile_1.0.0_amd64.deb ...
Unpacking hsa-amd-aqlprofile (1.0.0) ...
Selecting previously unselected package rock-dkms.
Preparing to unpack .../rock-dkms_1.8-199_all.deb ...
Unpacking rock-dkms (1.8-199) ...
Selecting previously unselected package rocm-device-libs.
Preparing to unpack .../rocm-device-libs_0.0.1_amd64.deb ...
Unpacking rocm-device-libs (0.0.1) ...
Selecting previously unselected package rocm-smi.
Preparing to unpack .../rocm-smi_1.0.0-46-g81ef66f_amd64.deb ...
Unpacking rocm-smi (1.0.0-46-g81ef66f) ...
Selecting previously unselected package rocm-dev.
Preparing to unpack .../rocm-dev_1.8.199_amd64.deb ...
Unpacking rocm-dev (1.8.199) ...
Selecting previously unselected package rocm-dkms.
Preparing to unpack .../rocm-dkms_1.8.199_amd64.deb ...
Unpacking rocm-dkms (1.8.199) ...
Setting up hsa-ext-rocr-dev (1.1.8-15-ge851b7a) ...
Setting up hsakmt-roct (1.0.8-2-g2076b0c) ...
Setting up hsakmt-roct-dev (1.0.8-2-g2076b0c) ...
Setting up hsa-rocr-dev (1.1.8-15-ge851b7a) ...
Setting up rocminfo (1.0.0) ...
Setting up rocm-opencl (1.2.0-2018082755) ...
Setting up rocm-opencl-dev (1.2.0-2018082755) ...
Setting up rocm-clang-ocl (0.3.0-7997136) ...
Setting up rocm-utils (1.8.199) ...
Setting up hcc (1.2.18272) ...
Setting up hip_base (1.5.18276) ...
Setting up hip_doc (1.5.18276) ...
Setting up hip_hcc (1.5.18276) ...
Setting up hip_samples (1.5.18276) ...
Setting up hsa-amd-aqlprofile (1.0.0) ...
Setting up rock-dkms (1.8-199) ...
Loading new amdgpu-1.8-199 DKMS files...
First Installation: checking all kernels...
Building only for 4.15.0-33-generic
Building for architecture x86_64
Building initial module for 4.15.0-33-generic
Done.
Forcing installation of amdgpu

amdgpu:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/4.15.0-33-generic/updates/dkms/

amdttm.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/4.15.0-33-generic/updates/dkms/

amdkcl.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/4.15.0-33-generic/updates/dkms/

amdkfd.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/4.15.0-33-generic/updates/dkms/

amdchash.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/4.15.0-33-generic/updates/dkms/

amd-sched.ko:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/4.15.0-33-generic/updates/dkms/

depmod....

Backing up initrd.img-4.15.0-33-generic to /boot/initrd.img-4.15.0-33-generic.old-dkms
Making new initrd.img-4.15.0-33-generic
(If next boot fails, revert to initrd.img-4.15.0-33-generic.old-dkms image)
update-initramfs....

DKMS: install completed.
Setting up rocm-device-libs (0.0.1) ...
Setting up rocm-smi (1.0.0-46-g81ef66f) ...
Setting up rocm-dev (1.8.199) ...
Setting up rocm-dkms (1.8.199) ...
KERNEL=="kfd", MODE="0666"
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for initramfs-tools (0.122ubuntu8.11) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-33-generic

(REBOOT)
$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

$ /opt/rocm/bin/rocm-smi 


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   33c     16.68W   300Mhz   300Mhz   0.0%     auto      0%         0%       
  0   36c     9.145W   300Mhz   300Mhz   0.0%     auto      0%         0%       
================================================================================
====================           End of ROCm SMI Log          ====================
```

---

### 评论 #22 — tomkv (2018-09-15T15:47:23Z)

I was solving the same issue, but with Fedora and Fedora kernel.

Turns out, that there is a dependency in amdgpu on amdkfd: when amdgpu loads and amdkfd is not available, then amdgpu will work fine, but amdkfd won't work if you modprobe it later. So check your initramfs, if you have it configured to include amdkfd - in Fedora, it wasn't.

What you should see:

```console
$ dmesg|grep kfd
[    4.062230] kfd kfd: Initialized module
[    4.583587] kfd kfd: Allocated 3969056 bytes on gart
[    4.583804] kfd kfd: added device 1002:687f
```
With this and fixing the permissions on `/dev/kfd` with the udev rule in README, rocminfo works for me.

---

### 评论 #23 — akostadinov (2018-10-04T12:31:00Z)

I see:
```
[    2.131266] amdgpu 0000:03:00.0: kfd not supported on this ASIC
```

RHEL 7.5, Core 2 Duo 2GHz, Gygabyte GA-P35-DS3L

---

### 评论 #24 — gstoner (2018-10-04T12:40:30Z)

@akostadinov which GPU are you trying to use.  Since this error code does not tell us what it is 

---

### 评论 #25 — akostadinov (2018-10-04T12:45:00Z)

@gstoner , Vega Frontier Edition air cooled:
```
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XTX [Radeon Vega Frontier Edition] (prog-if 00 [VGA controller])
	Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device 6b76
	Flags: bus master, fast devsel, latency 0, IRQ 30
	Memory at d0000000 (64-bit, prefetchable) [size=256M]
	Memory at e0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at b000 [size=256]
	Memory at f5000000 (32-bit, non-prefetchable) [size=512K]
	[virtual] Expansion ROM at f4000000 [disabled] [size=128K]
	Capabilities: [48] Vendor Specific Information: Len=08 <?>
	Capabilities: [50] Power Management version 3
	Capabilities: [64] Express Legacy Endpoint, MSI 00
	Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
	Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
	Capabilities: [150] Advanced Error Reporting
	Capabilities: [200] #15
	Capabilities: [270] #19
	Capabilities: [2a0] Access Control Services
	Capabilities: [2b0] Address Translation Service (ATS)
	Capabilities: [2c0] Page Request Interface (PRI)
	Capabilities: [2d0] Process Address Space ID (PASID)
	Capabilities: [320] Latency Tolerance Reporting
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```

---

### 评论 #26 — jlgreathouse (2018-10-04T14:10:23Z)

@akostadinov it's probably a bad idea to piggyback tech support requests on an already-closed thread. It's a good way to get your problem ignored. :) This is a common error that is often because of a misconfigured system, so we do not plan on reopening issues like this each time a user sees the problem.

That said, could you show the output of:
- `uname -r`
- `dkms status`
- `modinfo amdgpu`
- `modinfo amdkfd`

---

### 评论 #27 — akostadinov (2018-10-04T16:32:30Z)

@jlgreathouse, it just looked like the same issue and followed up on tomkv's comment. But as it appears to be unrelated, I filed a new issue RadeonOpenCompute/ROCK-Kernel-Driver#57 per your advice. Thank you!

---

### 评论 #28 — noobaldrin (2019-10-19T22:46:07Z)

I would like to add to this on how I solved my problem since I've been here recently.
Just in case somebody might come across this issue.

Using `dmesg |grep kfd` I get:
```
[    2.458311] kfd kfd: Allocated 3969056 bytes on gart
[    2.458761] kfd kfd: added device 1002:67df
```

So the kernel driver is loaded but I'm getting error when I do `rocminfo`
```
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc.
```

This one fixed my problem (it was actually my fault for using a custom kernel)
I had in my kernel `HMM_MIRROR` and `DRM_AMDGPU_USERPTR` both disabled so I recompiled both enabled in my kernel then rebooted. `HMM_MIRROR` is required to enable `DRM_AMDGPU_USERPTR`

Not sure if this one is required but I have specifically set GEN3 for PCIE in my `BIOS/UEFI`.
Hope it helps.

I'm using kernel v5.3.7 btw

---

### 评论 #29 — jli113 (2019-10-23T03:25:21Z)

Same issue on kernel v5.0.0-23 using rx5700xt

---
