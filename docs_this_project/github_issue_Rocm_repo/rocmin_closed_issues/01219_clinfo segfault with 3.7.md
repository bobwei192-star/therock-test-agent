# clinfo segfault with 3.7

- **Issue #:** 1219
- **State:** closed
- **Created:** 2020-09-14T22:32:53Z
- **Updated:** 2020-12-16T05:26:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/1219

Followed the install instructions, getting this backtrace.

```
root@kontron:/opt/rocm/opencl/bin# gdb --args ./clinfo
GNU gdb (Ubuntu 8.1-0ubuntu3.2) 8.1.0.20180409-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./clinfo...(no debugging symbols found)...done.
(gdb) r
Starting program: /opt/rocm-3.7.0/opencl/bin/clinfo
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff58d0700 (LWP 2233)]

Thread 1 "clinfo" received signal SIGSEGV, Segmentation fault.
0x00007ffff67ffb20 in roc::Device::setupCpuAgent() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
(gdb) bt
#0  0x00007ffff67ffb20 in roc::Device::setupCpuAgent() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#1  0x00007ffff67ffea2 in roc::Device::populateOCLDeviceConstants() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#2  0x00007ffff68025ee in roc::Device::create() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#3  0x00007ffff6802f13 in roc::Device::init() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#4  0x00007ffff67c532f in amd::Device::init() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#5  0x00007ffff67cf526 in amd::Runtime::init() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#6  0x00007ffff67bfb45 in void std::call_once<clIcdGetPlatformIDsKHR::{lambda()#1}>(std::once_flag&, clIcdGetPlatformIDsKHR::{lambda()#1}&&)::{lambda()#2}::_FUN() () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#7  0x00007ffff6e27827 in __pthread_once_slow (once_control=0x7ffff6a73c80 <clIcdGetPlatformIDsKHR::initOnce>, init_routine=0x7ffff79008a0 <__once_proxy>) at pthread_once.c:116
#8  0x00007ffff67bfc59 in clIcdGetPlatformIDsKHR () from /opt/rocm-3.7.0/opencl/bin/../lib/libamdocl64.so
#9  0x00007ffff7bcfa9d in khrIcdVendorAdd () from /opt/rocm-3.7.0/opencl/bin/../lib/libOpenCL.so.1
#10 0x00007ffff7bd1982 in khrIcdOsVendorsEnumerate () from /opt/rocm-3.7.0/opencl/bin/../lib/libOpenCL.so.1
#11 0x00007ffff6e27827 in __pthread_once_slow (once_control=0x7ffff7dd40f0 <initialized>, init_routine=0x7ffff7bd1790 <khrIcdOsVendorsEnumerate>) at pthread_once.c:116
#12 0x00007ffff7bd0061 in clGetPlatformIDs () from /opt/rocm-3.7.0/opencl/bin/../lib/libOpenCL.so.1
#13 0x00005555555606ac in cl::Platform::get(std::vector<cl::Platform, std::allocator<cl::Platform> >*) ()
#14 0x00005555555562de in main ()
(gdb)
```

Kernel:
```
root@kontron:/opt/rocm/opencl/bin# uname -a
Linux kontron 5.4.0-47-generic #51~18.04.1-Ubuntu SMP Sat Sep 5 14:35:50 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

Ubuntu 18.04.05:
```
root@kontron:/opt/rocm/opencl/bin# cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.5 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.5 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

Installed ROCM packages:
```
root@kontron:/opt/rocm/opencl/bin# dpkg -l | grep rocm
ii  comgr                                 1.6.0.149-rocm-rel-3.7-20-6670e0d               amd64        Library to provide support functions
ii  hsa-rocr-dev                          1.2.30700.0-rocm-rel-3.7-20-99e66a7a            amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for Boltzmann (ROCm) platforms
ii  rocm-clang-ocl                        0.5.0.49-rocm-rel-3.7-20-7b47f7d                amd64        OpenCL compilation with clang compiler.
ii  rocm-cmake                            0.3.0.153-rocm-rel-3.7-20-1d1caa5               amd64        rocm-cmake built using CMake
ii  rocm-dbgapi                           0.30.0-rocm-rel-3.7-20                          amd64        Library to provide AMD GPU debugger API
ii  rocm-dev                              3.7.0-20                                        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                      1.0.0.588-rocm-rel-3.7-20-5ff5319               amd64        Radeon Open Compute - device libraries
ii  rocm-dkms                             3.7.0-20                                        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-gdb                              9.2-rocm-rel-3.7-20                             amd64        ROCgdb
ii  rocm-opencl                           2.0.0.293-rocm-rel-3.7-20-3f18143               amd64        OpenCL: Open Computing Language on ROCclr
ii  rocm-opencl-dev                       2.0.0.293-rocm-rel-3.7-20-3f18143               amd64        OpenCL: Open Computing Language on ROCclr
ii  rocm-smi                              1.0.0-204-rocm-rel-3.7-20-g08ebddd              amd64        System Management Interface for ROCm
ii  rocm-smi-lib64                        2.4.0.15.rocm-rel-3.7-20-d325613                amd64        AMD System Management libraries
ii  rocm-utils                            3.7.0-20                                        amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                              1.30700.0                                       amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool
```

`rocminfo`:
```
root@kontron:/opt/rocm/bin# ./rocminfo
ROCk module is loaded
Able to open /dev/kfd read-write
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen Embedded V1404I with Radeon Vega Gfx
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen Embedded V1404I with Radeon Vega Gfx
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32(0x20) KB
  Chip ID:                 5597(0x15dd)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2000
  BDFID:                   1024
  Internal Node ID:        0
  Compute Unit:            8
  SIMDs per CU:            4
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    4193920(0x3ffe80) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx902
  Uuid:                    GPU-XX
  Marketing Name:          AMD Ryzen Embedded V1404I with Radeon Vega Gfx
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 5597(0x15dd)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1100
  BDFID:                   1024
  Internal Node ID:        0
  Compute Unit:            11
  SIMDs per CU:            4
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        160(0xa0)
  Max Work-item Per CU:    10240(0x2800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```


Any ideas?