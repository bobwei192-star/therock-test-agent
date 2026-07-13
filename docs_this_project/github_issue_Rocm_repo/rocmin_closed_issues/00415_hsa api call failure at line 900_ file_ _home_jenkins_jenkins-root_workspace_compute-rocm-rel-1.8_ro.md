# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104

- **Issue #:** 415
- **State:** closed
- **Created:** 2018-05-13T21:29:43Z
- **Updated:** 2019-10-23T03:25:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/415

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
