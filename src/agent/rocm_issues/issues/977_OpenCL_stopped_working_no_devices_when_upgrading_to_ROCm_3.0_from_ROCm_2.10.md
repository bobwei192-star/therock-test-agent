# OpenCL stopped working "no devices" when upgrading to ROCm 3.0 from ROCm 2.10

> **Issue #977**
> **状态**: closed
> **创建时间**: 2019-12-20T13:49:13Z
> **更新时间**: 2021-01-29T13:17:40Z
> **关闭时间**: 2021-01-29T13:17:40Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/977

## 描述

I updated from ROCm 2.10 to ROCm 3.0, and OpenCL stopped working by reporting 0 devices.
There are no errors in dmesg.

Kernel: Linux 5.4.5 and 5.5.0-rc2 (same behavior on both), GPU RadeonVII.
rocm-smi reports correctly all the GPUs, so it seems the hardware is detected and initialized correctly:
```
~/rocm-opencl$ ~/ROC-smi/rocm-smi 
GPU  Temp   AvgPwr  SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
0    33.0c  27.0W   809Mhz  351Mhz  20.0%   auto  250.0W    0%   0%    
[etc]
```

But both /usr/bin/clinfo and /opt/rocm/opencl/bin/x86_64/clinfo report no devices:
```
/opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```
```
/usr/bin/clinfo  
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3052.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform
```

The ROCm packages that I have installed:
```
hsa-rocr-dev/Ubuntu 16.04,now 1.1.9.0-rocm-rel-3.0-6-7128d0d amd64 [installed,automatic]
hsakmt-roct/Ubuntu 16.04,now 1.0.9-298-gea01eb3 amd64 [installed,automatic]
rocm-opencl/Ubuntu 16.04,now 2.0.0-rocm-rel-3.0-6-9a4afec amd64 [installed]
```

---

## 评论 (71 条)

### 评论 #1 — preda (2019-12-20T13:58:30Z)

Moving back to ROCm 2.10 (from 3.0) produces working OpenCL, I see these packages are installed
```
hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev rocm-opencl
hsa-ext-rocr-dev/Ubuntu 16.04,now 1.1.9-139-g0d1ca36 amd64 [installed,automatic]
hsa-rocr-dev/Ubuntu 16.04,now 1.1.9-139-g0d1ca36 amd64 [installed,automatic]
hsakmt-roct-dev/Ubuntu 16.04,now 1.0.9-245-gc0e4b8d amd64 [installed,automatic]
hsakmt-roct/Ubuntu 16.04,now 1.0.9-245-gc0e4b8d amd64 [installed,automatic]
rocm-opencl/Ubuntu 16.04,now 1.2.0-rocm-rel-2.10-14-31325c4 amd64 [installed]
```


---

### 评论 #2 — preda (2019-12-20T14:02:17Z)

Moving forward to ROCm 3.0 again with the same set of packages installed OpenCL finds no devices
```
hsa-ext-rocr-dev/Ubuntu 16.04,now 1.1.9.0-rocm-rel-3.0-6-7128d0d amd64 [installed,auto-removable]
hsa-rocr-dev/Ubuntu 16.04,now 1.1.9.0-rocm-rel-3.0-6-7128d0d amd64 [installed,automatic]
hsakmt-roct-dev/Ubuntu 16.04,now 1.0.9-298-gea01eb3 amd64 [installed,auto-removable]
hsakmt-roct/Ubuntu 16.04,now 1.0.9-298-gea01eb3 amd64 [installed,automatic]
rocm-opencl/Ubuntu 16.04,now 2.0.0-rocm-rel-3.0-6-9a4afec amd64 [installed]
```


---

### 评论 #3 — btspce (2019-12-20T15:45:55Z)

Same on Raven Ridge 2700u APU upgraded from 2.10 to 3.0.
Fedora 31 kernel 5.3.16-300.fc31.x86_64 


$ clinfo
Number of platforms                               0

$ rocminfo
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 PRO 2700U w/ Radeon Vega Mobile Gfx
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32KB                               
  Chip ID:                 5597                               
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):2200                               
  BDFID:                   1024                               
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    33554048KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 5597                               
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1300                               
  BDFID:                   1024                               
  Compute Unit:            11                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  67109888                           
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            160                                
  Max Work-item Per CU:    10240                              
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64KB                               
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
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
*** Done ***


---

### 评论 #4 — btspce (2019-12-20T16:50:20Z)

After switching out hsakmt package from Fedora to the one provided by ROCm I now got these packages installed.
install rocm-utils rocm-opencl-devel rocminfo hsa-ext-rocr-dev
Packages Altered:
    Install hsa-ext-rocr-dev-1.1.9.0_rocm_rel_3.0_6_7128d0dc-1.x86_64 @ROCm
    Install hsa-rocr-dev-1.1.9.0_rocm_rel_3.0_6_7128d0dc-1.x86_64     @ROCm
    Install hsakmt-roct-1.0.9_298_gea01eb3-1.x86_64                   @ROCm
    Install rocm-clang-ocl-0.5.0.47_rocm_rel_3.0_6_cfddddb-1.x86_64   @ROCm
    Install rocm-opencl-2.0.0-rocm_rel_3.0_6_9a4afec13.x86_64         @ROCm
    Install rocm-opencl-devel-2.0.0-rocm_rel_3.0_6_9a4afec13.x86_64   @ROCm
    Install rocm-utils-3.0.6-1.x86_64                                 @ROCm
    Install rocminfo-1.0.0-1.x86_64                                   @ROCm


And clinfo

$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3052.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform

---

### 评论 #5 — rkothako (2019-12-21T08:21:42Z)

Thanks @preda and @btspce 
Can you please let know the exact steps to reproduce this problem.

---

### 评论 #6 — btspce (2019-12-21T08:37:19Z)

A simple upgrade from ROCm 2.10 to 3.0 of the packages at http://repo.radeon.com/rocm/yum/rpm when they became availible.  clinfo shows 0 devices availbile directly after upgrade and after reboot. Removing packages and reverting back to 2.10 solves the problem.

$ sudo dnf update
Packages Altered:
    Upgraded hsa-ext-rocr-dev-1.1.9.0_rocm_rel_3.0_6_7128d0dc-1.x86_64 @ROCm
    Upgraded hsa-rocr-dev-1.1.9.0_rocm_rel_3.0_6_7128d0dc-1.x86_64     @ROCm
    Upgraded hsakmt-roct-1.0.9_298_gea01eb3-1.x86_64                   @ROCm
    Upgraded rocm-clang-ocl-0.5.0.47_rocm_rel_3.0_6_cfddddb-1.x86_64   @ROCm
    Upgraded rocm-opencl-2.0.0-rocm_rel_3.0_6_9a4afec13.x86_64         @ROCm
    Upgraded rocm-opencl-devel-2.0.0-rocm_rel_3.0_6_9a4afec13.x86_64   @ROCm
    Upgraded rocm-utils-3.0.6-1.x86_64                                 @ROCm
    Upgraded rocminfo-1.0.0-1.x86_64                                   @ROCm

$ clinfo
Number of platforms 1
Platform Name AMD Accelerated Parallel Processing
Platform Vendor Advanced Micro Devices, Inc.
Platform Version OpenCL 2.1 AMD-APP (3052.0)
Platform Profile FULL_PROFILE
Platform Extensions cl_khr_icd cl_amd_event_callback cl_amd_offline_devices
Platform Host timer resolution 1ns
Platform Extensions function suffix AMD

Platform Name AMD Accelerated Parallel Processing
Number of devices 0

NULL platform behavior
clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...) No platform
clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...) No platform
clCreateContext(NULL, ...) [default] No platform
clCreateContext(NULL, ...) [other] No platform
clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT) No devices found in platform
clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU) No devices found in platform
clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU) No devices found in platform
clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR) No devices found in platform
clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM) No devices found in platform
clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL) No devices found in platform


---

### 评论 #7 — preda (2019-12-21T08:44:01Z)

> Thanks @preda and @btspce
> Can you please let know the exact steps to reproduce this problem.

The steps are: starting with a working OpenCL-only ROCm 2.10 installation, do a
```
$ sudo apt upgrade
```
which updates the packages as already indicated. At this point OpenCL stops detecting any devices, and this persists after a reboot. rocm-smi continues to detect correctly all the GPUs at all times.


---

### 评论 #8 — ddobreff (2019-12-21T18:14:40Z)

You need to install comgr too. Its no longer a part of rocm-opencl package for unknown reason - libamd_comgr.so 

---

### 评论 #9 — preda (2019-12-21T23:56:10Z)

> You need to install comgr too. Its no longer a part of rocm-opencl package for unknown reason - libamd_comgr.so

I did try and installed comgr too, it didn't fix it.

Maybe AMD could use the information from this thread to fix the 3.0 upgrade and update the instructions:
- introduce a package dependency of rocm-opencl on comgr if needed
- remove the old amdocl64.icd during the upgrade if required


---

### 评论 #10 — btspce (2019-12-22T19:58:43Z)

3.0 is not working. I made an error in an previous comment and ended up with both 2.2 repo and 3.0 in my rocm.repo after switching back and forth a few times. I have deleted my previous comment that stated that this was fixed.

---

### 评论 #11 — btspce (2019-12-22T20:03:49Z)

When reinstalling 3.0 packages I noticed this:

Running scriptlet: hsa-rocr-dev-1.1.9.0_rocm_rel_3.0_6_7128d0dc-1.x86_6   8/9 
/var/tmp/rpm-tmp.HOl0fW: line 1: [: missing `]'


---

### 评论 #12 — btspce (2019-12-22T20:13:51Z)

clinfo shows:

Number of P2P devices (AMD)                     0
P2P devices (AMD)                               <printDeviceInfo:147: get number of CL_DEVICE_P2P_DEVICES_AMD : error -30>

When hsa-ext-rocr-dev-1.1.9.0-rocm-rel-3.0-6-7128d0dc-Linux.rpm is installed for image support clinfo crashes and so does Darktable. Last version that worked was hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm from ROCm 2.9

$ clinfo
Segmentation fault (core dumped)




---

### 评论 #13 — OlegSmelov (2019-12-23T09:08:06Z)

For those wondering how to revert to a previous version on Debian-based distros:

```sh
sudo apt autoremove rocm-dkms rock-dkms
sudo vim /etc/apt/sources.list.d/rocm.list
```

Replace `http://repo.radeon.com/rocm/apt/debian/` with `http://repo.radeon.com/rocm/apt/2.10.0/`

```sh
sudo apt update
sudo apt install rocm-dkms # or any other set of packages you need

---

### 评论 #14 — rkothako (2019-12-23T17:01:46Z)

Thanks all. 
Clinfo works good with 3.0 upgrade from 2.10 as below
   - sudo apt install rocm-dkms [2.10] 
   - sudo apt upgrade  [ use this to upgrade to 3.0]
Clinfo fail to find devices when we do upgrade as below
  - sudo apt install rock-dkms rocm-opencl-dev  [ 2.10 - install opencl only rocm ]
  - sudo apt upgrade [upgrade to 3.0]

We have logged an internal issue for proper fix.
Currently we are working on this issue.

---

### 评论 #15 — preda (2019-12-28T10:42:24Z)

> Thanks all.
> Clinfo works good with 3.0 upgrade from 2.10 as below
> 
>     * sudo apt install rocm-dkms [2.10]
> 
>     * sudo apt upgrade  [ use this to upgrade to 3.0]
>       Clinfo fail to find devices when we do upgrade as below
> 
>     * sudo apt install rock-dkms rocm-opencl-dev  [ 2.10 - install opencl only rocm ]
> 
>     * sudo apt upgrade [upgrade to 3.0]
> 
> 
> We have logged an internal issue for proper fix.
> Currently we are working on this issue.

@rkothako could you please clarify what are the working steps for an upgrade from 2.10 to 3.0 OpenCL-only without dkms? i.e. I'm not using rocm-dkms, and most likely rocm-dkms would fail to compile anyway on the kernel I'm using (5.5).

And you could also please explain what is the problem that is fixed by the working upgrade steps (to help our understanding), thanks.


---

### 评论 #16 — csuji (2020-01-01T21:40:28Z)

Same here after upgrading from 2.10 to 3.0-6 with  Vega Frontier card.
```
clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3052.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 
  Driver Version                                  3052.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Vega 10 XTX [Radeon Vega Frontier Edition]
...
NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900

```

How do you guys do regression testing???


---

### 评论 #17 — wxsatman (2020-01-02T00:36:43Z)

New to ROCm stack but have used AMD OpenCL before.

I just tried to ROCm on OpenSuse from Yum repository and I assume I am having the same problem?

I first upgraded to Kernel 5.4 so Kernel support should be there 

/opt/rocm/bin/rocminfo gives reasonable results (splits ThreadRipper into 4 agents??) then shows as below for GPU.

When I run /opt/rocm/opencl/bin/x86_64/clinfo I get as below:

Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

So as I guess this thread indicates OpenCL just does not work with ROCm 3.0??    

If this is not the case how do you fix this?

How could this happen was OpenCL really not tested before this was released?   Yikes!

When will a fix be available?


Partial Output from rocminfo:
*******                  
Agent 5                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XT [Radeon RX Vega 64]     
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    4                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1750           

---

### 评论 #18 — wxsatman (2020-01-02T00:54:19Z)

I will note that I looked at the rpm's that were installed from repository, as below, and noticed that opencl* has a 2.0.0 as part of version where other important rocm stuff has 3.0.0 is it right or should there be a later version of the opencl* packages??

linux-k3mw:/home/goesmgr # rpm -qa | grep rocm
hipcub-2.9.0.88_rocm_rel_3.0_6_6ee0aed-1.x86_64
rocrand-2.10.0.656_rocm_rel_3.0_6_b9f838b-1.x86_64
rocprim-2.9.0.950_rocm_rel_3.0_6_b85751b-1.x86_64
rocm-utils-3.0.0-1.x86_64
rocm-clang-ocl-0.5.0.47_cfddddb-1.x86_64
rocm-opencl-2.0.0-_9a4afec13.x86_64
rocalution-1.6.3.460_rocm_rel_3.0_6_2382876-1.x86_64
rocm-cmake-0.3.0.134_e6d1ef3-1.x86_64
rocm-libs-3.0.0-1.x86_64
rocblas-2.12.1.1749_rocm_rel_3.0_6_ca5535b-1.x86_64
rocfft-0.9.9.760_rocm_rel_3.0_6_aee1339-1.x86_64
rocm-debug-agent-1.0.0-1.x86_64
rocm-dev-3.0.0-1.x86_64
procmail-3.22-lp150.2.3.x86_64
rocm-profiler-5.6.7262-g93fb592.x86_64
rocm-smi-1.0.0_192_g01752f2-1.x86_64
rocm-device-libs-1.0.0.559_628eea4-1.x86_64
hipsparse-1.3.3.208_rocm_rel_3.0_6_f98f82e-1.x86_64
rocm-opencl-devel-2.0.0-_9a4afec13.x86_64
rocminfo-1.0.0-1.x86_64
rocthrust-2.9.0.413_rocm_rel_3.0_6_957b1e9-1.x86_64
rocm-smi-lib64-2.2.0.8.local_build_0_8ffe1bc-1.x86_64
rocsparse-1.5.15.691_rocm_rel_3.0_6_aee785e-1.x86_64
hipblas-0.18.0.281_rocm_rel_3.0_6_da8f5a2-1.x86_64


---

### 评论 #19 — preda (2020-01-04T22:53:47Z)

@rkothako : is there a way to upgrade from ROCm 2.10 to ROCm 3.0, OpenCL only, without dkms? Please let me know how I can do this upgrade.


---

### 评论 #20 — rkothako (2020-01-06T12:12:43Z)

Hi @preda and all,
We have found the root cause the problem and the workaround is given below.
After upgrading OpenCL-only-ROCm from 2.10 to 3.0, just install the packages on top of it: comgr rocm-smi-lib64
(sudo apt install comgr rocm-smi-lib64)
Then clinfo will start working.


---

### 评论 #21 — csuji (2020-01-07T08:18:47Z)

Does not work for me with Ubuntu 18.04.3 LTS and kernel 5.0.0-37-generic, Vega Frontier card. Can you please post a step by step guide and test the next release with some common distributions? Thanks!

---

### 评论 #22 — rkothako (2020-01-07T08:59:05Z)

Steps to follow:
1. Install OpenCL only ROCm for 2.10
sudo apt install rock-dkms rocm-opencl-dev
2. Upgrade to ROCm 3.0
sudo apt upgrade
3. Run clinfo 
/opt/rocm/opencl/bin/x86_64/clinfo --> Clinfo fails to run
4. Install comgr rocm-smi-lib64
sudo apt install comgr rocm-smi-lib64
5. Run clinfo 
/opt/rocm/opencl/bin/x86_64/clinfo --> Clinfo runs well


---

### 评论 #23 — preda (2020-01-07T10:19:59Z)

> Steps to follow:
> 
>     1. Install OpenCL only ROCm for 2.10
>        sudo apt install rock-dkms rocm-opencl-dev
> 
>     2. Upgrade to ROCm 3.0
>        sudo apt upgrade
> 
>     3. Run clinfo
>        /opt/rocm/opencl/bin/x86_64/clinfo --> Clinfo fails to run
> 
>     4. Install comgr rocm-smi-lib64
>        sudo apt install comgr rocm-smi-lib64
> 
>     5. Run clinfo
>        /opt/rocm/opencl/bin/x86_64/clinfo --> Clinfo runs well

@rkothako thank you, but I am talking about an install *without* rock-dkms, as is required when using a recent kernel that is not supported by rock-dkms. Did you try your instructions on a system with Linux kernel 5.4 or 5.5?

---

### 评论 #24 — csuji (2020-01-07T10:33:03Z)

@rkothako Thanks, this works for /opt/rocm clinfo. Problem is now (or still since I though that was the fix) that leela zero (https://github.com/leela-zero/leela-zero Go engine with OpenCL) fails to compile all 290 kernel it tries during tuning (worked with 2.10):
`./leelaz --benchmark -t6 -w somenet_downloaded_network.gz
Failed to compile: 290 kernels.
Failed to find a working configuration.
Check your OpenCL drivers.
Minimum error: 100.000000. Error bound: 0.000100
terminate called after throwing an instance of 'std::runtime_error'
  what():  Tuner failed to find working configuration.
Aborted (core dumped)
`
KataGo (https://github.com/lightvector/KataGo) also fails to tune with 3.0 AND  2.10 (did not check older versions)
I think these are good test cases for your OpenCL implementation as they try a lot of kernels during tuning. Perhaps you could include them in some regression tests!

---

### 评论 #25 — wxsatman (2020-01-08T17:01:07Z)

rkohato & all

Looked and I have the comgr and rocm-smi packages installed and it is not working.

I am using OpenSuse and 5.4 Kernel as a result the rock-dkms is not used/needed.

I have a "clean" install of just the 3.0 version from the latest zypper repository:

zypper ar http://repo.radeon.com/rocm/zyp/zypper/ rocm-repo

In my post earlier it shows the rocm related packages that were installed.

To the developers here:  Why don't you try to just do a clean OpenSuse Linux install and then add your repository and the packages.    Then run clinfo and straighten out that issue and then run some real testing on common OpenCL Kernels and applications.     Then post updates with a readme of tested configurations.

I do not see anyone but the most experienced users wanting to try/use the ROCm stuff at this point.    Little point in spending all this effort on ROCm if no one can actually use it!
 

---

### 评论 #26 — jcdutton (2020-01-14T12:44:43Z)

I have a similar problem. Kernel 5.4.6 from mainline.  ROCm from git: Version 3.0
rocminfo show the GPU. clinfo show no GPUs.
I turned some debug on in clinfo, and it outputs this:
[clinfo-debug.txt](https://github.com/RadeonOpenCompute/ROCm/files/4059157/clinfo-debug.txt)

It looks to me that the following error messages are what is wrong:
:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:1714: Trying to allocate host memory
hsa_amd_memory_pool_allocate stat: 1008
:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:1718: Fail allocation host memory
:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:354: Couldn't allocate a transfer buffer!
:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:798: Couldn't allocate transfer buffer objects for read
:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:568: Error creating new instance of Device.

Unfortunately, the failure is happening within the binary only amd lib, so further analysis is difficult.


---

### 评论 #27 — jcdutton (2020-01-14T13:26:29Z)

Doing an strace gives some more info:
This call is failing:
[pid 12036] mbind(0x7f2650200000, 1052672, 0x8001 /* MPOL_??? */, [0x0000000000000002], 3, 0) = -1 EINVAL (Invalid argument)
As this is from within a binary only lib, I do not have the associated source code.
This is rocdevice.cpp:1714:
hsa_status_t stat = hsa_amd_memory_pool_allocate(segment, size, 0, &ptr);
the function "hsa_amd_memory_pool_allocate" is in the binary only lib.

More of the strace:
[pid 12036] write(2, ":1:/usr/src/rocm/ROCm-OpenCL-Run"..., 115:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:1714: Trying to allocate host memory
) = 115
[pid 12036] mmap(NULL, 2105344, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_NORESERVE, -1, 0) = 0x7f26501fe000
[pid 12036] munmap(0x7f26501fe000, 8192) = 0
[pid 12036] munmap(0x7f2650301000, 1044480) = 0
[pid 12036] mmap(0x7f2650200000, 1052672, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f2650200000
[pid 12036] get_mempolicy(NULL, NULL, 0, NULL, 0) = 0
[pid 12036] mbind(0x7f2650200000, 1052672, 0x8001 /* MPOL_??? */, [0x0000000000000002], 3, 0) = -1 EINVAL (Invalid argument)
[pid 12036] mbind(0x7f2650200000, 1052672, MPOL_DEFAULT, NULL, 0, 0) = 0
[pid 12036] munmap(0x7f2650200000, 1052672) = 0
[pid 12036] mmap(NULL, 2105344, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_NORESERVE, -1, 0) = 0x7f26501fe000
[pid 12036] munmap(0x7f26501fe000, 8192) = 0
[pid 12036] munmap(0x7f2650301000, 1044480) = 0
[pid 12036] mmap(0x7f2650200000, 1052672, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f2650200000
[pid 12036] get_mempolicy(NULL, NULL, 0, NULL, 0) = 0
[pid 12036] mbind(0x7f2650200000, 1052672, 0x8001 /* MPOL_??? */, [0x0000000000000002], 3, 0) = -1 EINVAL (Invalid argument)
[pid 12036] mbind(0x7f2650200000, 1052672, MPOL_DEFAULT, NULL, 0, 0) = 0
[pid 12036] munmap(0x7f2650200000, 1052672) = 0
[pid 12036] fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
[pid 12036] write(1, "hsa_amd_memory_pool_allocate sta"..., 40) = 40
[pid 12036] write(2, ":1:/usr/src/rocm/ROCm-OpenCL-Run"..., 112:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:1718: Fail allocation host memory
) = 112
[pid 12036] write(2, ":1:/usr/src/rocm/ROCm-OpenCL-Run"..., 120:1:/usr/src/rocm/ROCm-OpenCL-Runtime/opencl/runtime/device/rocm/rocdevice.cpp:354: Couldn't allocate a transfer buffer!



---

### 评论 #28 — jcdutton (2020-01-14T22:49:03Z)

I think I have worked out what the problem is when running clinfo not finding vega gpu card:
[pid  4130] mbind(0x7f6ed7266000, 4096, 0x8001 /* MPOL_??? */, [0x0000000000000001], 3, 0) = 0
[pid  4130] mbind(0x7f6dc0400000, 1052672, 0x8001 /* MPOL_??? */, [0x0000000000000002], 3, 0) = -1 EINVAL (Invalid argument)

This is trying to mbind to node0 (success) and then tries to mbind to node1 (fails).
The rocminfo output shows the following:
Agent 1  (CPU)
...
Segment: GLOBAL; FLAGS: KERNARG, FINE GRAINED
Size: 33554048KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Alignment: 4KB
Acessible by all: TRUE
...
Agent 2 (CPU)
Segment: GROUP
Size: 64KB
Allocatable: FALSE
Alloc Granule: 0KB
Alloc Alignment: 0KB
Acessible by all: FALSE

So, the RAM is attached to node0(Agent1), but no RAM is attached to node1(Agent2).
The AMD binary blob tries both nodes. The AMD binary blob is giving up if node1 has no RAM attached.

I have a AMD Threadripper 1950 which has a similar pattern of RAM install. All attached to node0, no RAM attached to node1.


---

### 评论 #29 — jcdutton (2020-01-19T23:11:47Z)

@preda @btspce @wxsatman 
FIX FOUND:
My PC has 2 RAM chips.  16GB per chip.  Previously both chips were on node0. As per the motherboard manual for installing 2 chips.
If I move the RAM so that 1 chip is on node0 and the other chip is on node1.
clinfo now detects my GPU.
So, my advice for the people seeing this problem is to re-arrange the RAM chips into different slots.
This bug still needs fixing though. Or at least a more useful error message so the user knows they need to move RAM chips about.



---

### 评论 #30 — MatPoliquin (2020-02-07T21:35:18Z)

I have a similar issue with clinfo, after installing rocm 3.0 in a fresh install of Ubuntu 19.04 with kernel 5.0. My gpu is a RX580

Output of clinfo
`Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
`

---

### 评论 #31 — preda (2020-02-10T20:40:06Z)

Is AMD still investigating how to get OpenCL to keep working after an update to ROCm 3.0? Otherwise maybe the oficial solution could be posted here..


---

### 评论 #32 — ableeker (2020-02-12T18:41:20Z)

In #474 cryptomilk suggests to symlink rocm libamdocl64.so to /usr/lib64/libamdoclcl.so. I installed 3.10. I found libamdocl64.so in /opt/rocm/opencl/lib/x86_64, so I symlinked libamdoclcl.so to it. This didn't work however, clinfo still claims to have found no devices. And opencl programs, luxmark 3.1 for instance, still refuse to work. If I remove 3.0, and install 2.10, everything's working fine again.

---

### 评论 #33 — cryptomilk (2020-02-13T08:33:05Z)

Not really. libamdoclcl64.so (double cl) seems to be only part of the proprietary driver. It shouldn't be required for ROCm.

Either the kernel interface has changed in 3.0 and hasn't been updated in one of the recent kernels or there is an issue in ROCm 3.0 with upstream kernels which needs fixing. However I think with ROCm 3.1 the issue will be addressed. Just stay with 2.10 till it is released.

---

### 评论 #34 — jcdutton (2020-02-13T09:31:17Z)

Well, I had this problem. I have kernel 5.4.6 working with ROCm 3.0 on a Vega 56 with a AMD 1950X cpu.
I diagnosed the problem to a bug in the AMD binary blob bit of ROCm. ROCm is not 100% open source.
Please see my previous posts here for the work around. I.e. Move RAM chips.
The problem is related to NUMA. So it only affects CPUs that have more than 1 node, which I think, at this point, is only some of the higher end AMD CPUs.
I have a simple C test program, that probes the NUMA configuration in the same way the binary blob tries, and demonstrates the exact case where the clinfo fails.
When I move the RAM chips, my simple C test program passes and clinfo then works.
Unfortunately, the ROCm binary blob is where the probing happens, so it cannot be fixed without help from AMD.


---

### 评论 #35 — dmarcuse (2020-02-13T14:36:21Z)

@jcdutton could you share your code? I'd like to test my system (Ryzen 3700X and Vega 56) and I'm also just curious about it :stuck_out_tongue: 

---

### 评论 #36 — jcdutton (2020-02-13T19:36:11Z)

[rocm3.0-test.c.txt](https://github.com/RadeonOpenCompute/ROCm/files/4200629/rocm3.0-test.c.txt)

Compile with:
gcc -g -O0 -c -o rocm3.0-test.o rocm3.0-test.c
gcc -g  -o rocm3.0-test rocm3.0-test.o -lnuma

Example of good output:
# ./rocm3.0-test 
You have 2 CPU nodes
CPU Node 0 has RAM. OK
CPU Node 1 has RAM. OK
CPU Nodes and RAM layout checked. This should work with ROCM 3.0


---

### 评论 #37 — ableeker (2020-02-13T22:02:32Z)

@jcdutton thanks for the code. It compiled just fine. The output for my computer:

You have 1 CPU nodes
CPU Node 0 has RAM. OK
CPU Nodes and RAM layout checked. This should work with ROCM 3.0

Its a PC with an Intel i5-4460 Haswell CPU, and 16 GB RAM, 4 x 4GB RAM. So all 4 slots are filled. Unfortunately rocm opencl 3.10 isn't working, clinfo says 0 devices, and opencl programs don't work, or crash.

---

### 评论 #38 — jcdutton (2020-02-14T00:16:36Z)

@ableeker 
Ok, good, you don't have the RAM layout bug.
Please post the output from rocminfo


---

### 评论 #39 — dmarcuse (2020-02-14T18:16:20Z)

@jcdutton Thanks for posting your script! Unfortunately it doesn't seem to be accurate for my machine. It reports that it should work, outputting the following on both Linux 5.5 and Linux 5.4:
```
You have 1 CPU nodes
CPU Node 0 has RAM. OK
CPU Nodes and RAM layout checked. This should work with ROCM 3.0
```
However, on Linux 5.5, `clinfo` and `rocminfo` both segfault. Both work properly in Linux 5.4 (LTS), leading me to believe that something was changed in one of the kernel modules in 5.5 that broke compatibility.

---

### 评论 #40 — jcdutton (2020-02-14T18:32:34Z)

@dmarcuse 
Yes, 5.5 is a problem. See https://github.com/RadeonOpenCompute/ROCm/issues/1007
I have the same problem with 5.5.

The test program is only testing one edge case, that causes clinfo to fail to recognize a GPU. There might be other reasons rocm 3.0 does not work.
In which case, running "rocminfo" helps diagnose that.

---

### 评论 #41 — dmarcuse (2020-02-14T19:26:27Z)

Ah, I didn't realize there was a separate issue for 5.5. Hopefully they'll both be fixed soon. 

---

### 评论 #42 — ableeker (2020-02-15T11:58:26Z)

@jcdutton 

ROCk module is loaded
ableeker is member of video group
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XL/XT [Radeon RX Vega 56/64]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1630                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
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
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
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


---

### 评论 #43 — ableeker (2020-02-15T12:22:38Z)

I had installed rocm-opencl, had put the user in the video group, and added the udev rule. This was working well with 2.10, but failed to work with 3.0. For 3.0 I've installed all packages mentioned here as well, except rocm-dkms/rock-dkms, because I'm using Ubuntu 19.10 with kernel 5.3. rocminfo is the only one that sees the device (gfx900) it seems.

rocm clinfo:

Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)


---

### 评论 #44 — jcdutton (2020-02-16T14:32:11Z)

@ableeker
Check that you have the following files:
/opt/rocm/lib/libhsakmt.so.1.0.6
/opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9
/opt/rocm/opencl/lib/x86_64/libamdocl64.so
/opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
/dev/kfd
/usr/lib/x86_64-linux-gnu/libnuma.so.1.0.0
/dev/shm/hsakmt_shared_mem
/dev/shm/sem.hsakmt_semaphore
/etc/OpenCL/vendors/amdocl64.icd


---

### 评论 #45 — ableeker (2020-02-16T17:36:11Z)

@jcdutton
These files aren't all present, /dev/shm is empty, so hsakmt_shared_mem, and sem.hsakmt_semaphore are missing.

---

### 评论 #46 — ableeker (2020-02-16T18:09:20Z)

@jcdutton 
Heh... I had another look, and the files in /dev/shm are now present. So all files in the list are present. But clinfo still claims there are no device, and clopencl applications aren't working.

---

### 评论 #47 — jcdutton (2020-02-20T20:33:47Z)

@ableeker 
You could try:
strace -f clinfo 2>strace.txt
and then post the strace.txt file.
It might give some indication on where it is failing.


---

### 评论 #48 — jkrautter (2020-02-21T08:12:50Z)

Not sure if this will help anyone here, but I compiled both ROCm 3.0 and 2.10 entirely from source on my slackware64-current system and ran into the same problems as described here (rocminfo finds everything, clinfo doesn't). 
The solution was that I messed up my compile order, causing comgr to be compiled without AMDDeviceLibs. During device initialization with clinfo, it was unable to compile some scheduling kernels, which are apparently contained in the device libs. Recompiled comgr, now everything works with ROCm 3.0. It's at least something you can try quickly, recompiling  and installing comgr with AMDDeviceLibs installed.
I have a working system with Ryzen 3 3200G, a Vega 56, ROCm 3.0 and upstream kernel 5.5.4. Additionally, I had to disable the Ryzen's iGPU in BIOS, otherwise clinfo would segfault.

---

### 评论 #49 — ableeker (2020-02-21T18:43:53Z)

[@jcdutton:] I sure can! Here it is.

[strace1.txt](https://github.com/RadeonOpenCompute/ROCm/files/4241180/strace1.txt)


---

### 评论 #50 — jcdutton (2020-02-21T23:45:51Z)

@ableeker
I have looked at the strace.
It appears you are missing:
libtinfo.so.5


---

### 评论 #51 — ableeker (2020-02-22T12:16:22Z)

@jcdutton
I've symlinked libtinfo.so.5 to libtinfo.so.6.1 (which is installed), but that didn't help.

---

### 评论 #52 — jcdutton (2020-02-22T12:35:03Z)

@ableeker 
That will not work. You need to install version 5.
Which distro version do you have?
Installing this might help:
ncurses-compat-libs 

---

### 评论 #53 — ableeker (2020-02-22T17:06:56Z)

@jcdutton
I'm running Ubuntu 19.10 x64. I've removed the symlink, and have installed libncurses5. I've tried all kind of tips from this thread that were suggesting packages were missing, but no luck so far. This tip however, made clinfo actually work! I haven't installed ncurses-compat-libs, but libncurses5 seems to have done the trick. I then tried some applications I know of that use OpenCL, darktable, luxmark, and mandelbulber, and they're working now!
Thanks, great job!

---

### 评论 #54 — BloodyIron (2020-02-22T17:07:26Z)

Thanks to @preda and pointing out "rocm-opencl". I was able to get openCL working on my AMD RX580 now on Ubuntu 19.10. I had to switch back to the ROCM PPA for 2.9, then installed that package, and now I have a working openCL environment (and in-turn DaVinci Resolve) so far anyways.

Thanks! I have not had success with ROCM 3.0 or other methods at this time.

---

### 评论 #55 — ableeker (2020-02-23T12:19:10Z)

I wanted to clean up ROCm and OpenCL, so I removed everything (hopefully 2.10 as well as 3.0), and re-installed only the 3.0 versions of rocm-dev, and rocm-opencl-dev. I was confident that 3.0 would work after this, because this time I had installed libcurses5. Alas!, clinfo reported 0 devices, and programs that use OpenCL refuse to work. Am I missing something? Do I need to install another package for 3.0?

By the way, installing just these 2 packages is working great for me with 2.10. With 2.10 I install rocm-dev, and rocm-opencl-dev, and don't install rocm-dkms, because I'm running Ubuntu 19.10 with kernel 5.3. I install ROCm because I needed a version of OpenCL that's fairly new, but I only need OpenCL. So far, what I've seen is that if you only need OpenCL, programs that use OpenCL will happily work even if you don't install rocm-dev, and only install rocm-opencl-dev (which installs rocm-opencl), or even only rocm-opencl.

[strace.txt](https://github.com/RadeonOpenCompute/ROCm/files/4241208/strace.txt)

---

### 评论 #56 — jcdutton (2020-02-24T00:44:53Z)

@ableeker 
This time it is looking for:
/opt/rocm/lib/libamd_comgr.so
If it was all working, why "fix" it ?

---

### 评论 #57 — ableeker (2020-02-24T18:20:18Z)

@jcdutton
To clean stuff, I've switched between 2.10, and 3.0 dozens of times, and I've installed all kinds of packages (tips from people) trying to get 3.0 working. Besides, I'd like to find a foolproof way to install a working 3.0.

The good news is, I've found it! Prepare the same way as for 2.10: add repo, user in video group, and add udev rule. Then install ROCm OpenGL: install rocm-dkms, or rocm-dev, then install rocm-opengl-dev. Now for me anyway libncurses5 was missing, so I installed that. At this stage clinfo reports 0 devices, because it can't find libamd_comgr.so. So install comgr. And it seems that rocm-smi-lib64 is needed as well. Installing these last two packages is what @rkothako told us to do. Now clinfo should be working. What's more, OpenCL should be working as well!

Now the bad news is, some applications that actually are using OpenCL, and that were working with 2.10, will no longer work with 3.0. Luxmark is unable to compile kernels, and gpuowl crashes with a memory access fault.

---

### 评论 #58 — jcdutton (2020-02-24T23:12:15Z)

@preda 
Please post the output of strace -f clinfo 2>strace.txt
Also note, that rocm does not work with Kernel 5.5. It does work with Kernel 5.4.
clinfo seems to rely on multiple different libs, and by looking at the strace output we can tell which is missing.
https://github.com/RadeonOpenCompute/ROCm/issues/1007


---

### 评论 #59 — ableeker (2020-02-25T07:48:41Z)

I don't know if this applies to everyone, but I also had to install ncurses5 to get OpenCL working.

---

### 评论 #60 — preda (2020-02-28T12:01:35Z)

On Linux 5.6.0-rc1 (that was working fine with ROCm 2.10 OpenCL-only) I upgraded to ROCm 3.1, and aside from setting LD_LIBRARY_PATH, the only additional thing I had to do to get clinfo working was to install libncurses5 (thanks @ableeker ). These are my rocm packages that I have installed
```
comgr/Ubuntu 16.04,now 1.6.0.121-rocm-rel-3.1-35-cbb02f9 amd64 [installed]
hsa-ext-rocr-dev/Ubuntu 16.04,now 1.1.30100.0-rocm-rel-3.1-35-ecafeba1 amd64 [installed,auto-removable]
hsa-rocr-dev/Ubuntu 16.04,now 1.1.30100.0-rocm-rel-3.1-35-ecafeba1 amd64 [installed,automatic]
hsakmt-roct-dev/Ubuntu 16.04,now 1.0.9-319-g02e2b30 amd64 [installed,auto-removable]
hsakmt-roct/Ubuntu 16.04,now 1.0.9-319-g02e2b30 amd64 [installed,automatic]
rocm-opencl/Ubuntu 16.04,now 2.0.0-rocm-rel-3.1-35-8f28d95ad amd64 [installed]
```

Trying to run gpuowl, OpenCL compiles the kernels without issue, but the execution does not proceed correctly. At this point I don't know where the blame lies (i.e. is gpuowl doing something invalid that happened to work before, or is something wrong with the new OpenCL codegen). Unfortunately ATM I'm not planning to debug this deeper and I'll be moving back to 2.10.

But this is already progress, OpenCL is technically working although in gpuowl's case it is not usable (but as I said, I don't know on which side the problem is, yet). It turns out gpuowl could be a useful tool for regression testing, because it does produce big complex kernels (exercising the compiler extensivelly) and at the same time it is self-validating at runtime, thus any codegen problems tend to show up promptly. And can also be used for performance regression testing as well. But that's a different topic.


---

### 评论 #61 — ableeker (2020-02-28T22:54:14Z)

I'm not sure if this should be in the same issue, because I've just tried the new version 3.1. Anyway, I've noticed that I didn't need to install anything apart from rocm-opencl-dev, clinfo and OpenCL worked right after that. What's more, gpuowl was running correctly straight away. I didn't test it thoroughly, but it didn't abort with an memory access anymore, and it did started calculating. LuxMark is working again as well. Version 3.1 is looking rather good to me.

---

### 评论 #62 — ableeker (2020-02-29T11:26:10Z)

@preda
ROCm version 3.1 seems to have fixed a number of issues, gpuowl seems to be working again.

---

### 评论 #63 — ableeker (2020-02-29T13:34:23Z)

AMD has restructured the lot, installing just rocm-dev (or presumably rocm-dkms) will install everything needed for a working OpenCL environment. I didn't need to install comgr, rocm-opencl-dev, or rocm-smi-lib64. Looks like even libncurses5 isn't needed any longer.

---

### 评论 #64 — jasondavies (2020-02-29T13:35:55Z)

I'm getting `CL_INVALID_KERNEL_ARGS` on any trivial OpenCL kernel after updating to 3.1.

---

### 评论 #65 — jasondavies (2020-02-29T13:44:06Z)

> I'm getting `CL_INVALID_KERNEL_ARGS` on any trivial OpenCL kernel after updating to 3.1.

Looks like this only happens when pre-compiling kernels.  Will open a separate issue.

---

### 评论 #66 — jcdutton (2020-02-29T14:14:03Z)

ROCm 3.1 appears to be very different from ROCM 3.0.
If you have problems with ROCm 3.1, its probably best to raise a new ticket.
 This ticket is for ROCm 3.0.
The problems with ROCM 3.0 were due to a multitude of potential problems. But once people have install the correct libs, it normally works. Unless you have the odd problem I had that was cured with moving RAM chips around.


---

### 评论 #67 — ernstp (2020-04-17T12:03:55Z)

The install instructions mention that you should add yourself to the video group, but I also had to add myself to the "render" group because that owned /dev/dri/renderD128

---

### 评论 #68 — clemej (2020-04-25T05:20:44Z)

I can't believe this, but jcdutton's answer fixed the issue for me,  Fresh install of Ubuntu 20.04 on a new system, vega 56, and fresh install of rocm 3.3.0 from the repo.  rocminfo worked but clinfo segfaulted.  Installing `libncurses5` and `libncursesw5`solved the issue. 

The clue is in the strace, which not long before the crash claims it can't find libtinfo.so.5.  But then it complains about comgr before it crashes, leading many to believe that's the problem. 

I strongly recommend amd add a dependency on libncurses5 for Ubuntu, since newer versions don't install it by default.  Oh, and you probably shouldn't segv if its not there either. Hope this helps others.

---

### 评论 #69 — preda (2020-04-25T07:46:19Z)

This issue spell out libncurses5 specifically: #1067 

---

### 评论 #70 — braiam (2020-04-26T03:09:40Z)

Since many find this issue, tracing the clinfo strace seems to be the most generic solution to find out what's wrong:

```
strace -f clinfo 2> trace.txt
grep -e 'EACCES' trace.txt # finds permissions problems
grep -e 'ENOENT' trace.txt | grep so # finds library problems
```

Other errors described in this issue seems to be self-explanatory (missing kernel arguments).

---

### 评论 #71 — ROCmSupport (2021-01-29T13:17:40Z)

Thanks all for the help/suggestions over this thread.
I do not think this issue is still valid now as we are currently on ROCm 4.0 and ROCm upgrade is not supported at present.
We are streamlining our ROCm package versions and so ROCm upgrade support will be available very soon, like in 2 to 3 months.
Internal validation already started and will share an official support on this soon.
Please stay tuned for more updates via our ROCm documentation page.
Thank you.

---
