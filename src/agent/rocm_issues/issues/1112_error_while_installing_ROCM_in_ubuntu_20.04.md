# error while installing ROCM in ubuntu 20.04

> **Issue #1112**
> **状态**: closed
> **创建时间**: 2020-05-18T11:42:09Z
> **更新时间**: 2020-12-04T09:49:28Z
> **关闭时间**: 2020-12-04T09:49:28Z
> **作者**: balasundram
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1112

## 描述

after adding the rocm repository, when i run the sudo apt get i get the error like

E: Type 'gpg' is not known on line 1 in source list /etc/apt/sources.list.d/rocm.list
E: The list of sources could not be read.
i need to use rocm for making use of radeon  560  graphic card.
![error](https://user-images.githubusercontent.com/54479906/82209131-63303000-992a-11ea-83f6-5aa3d6ad941f.png)



---

## 评论 (12 条)

### 评论 #1 — ableeker (2020-05-18T16:55:41Z)

What's the content of the file? It looks like you've put too much in there. The gpg part isn't part of the content. The only text that should be in the file is the following:

`deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main`

---

### 评论 #2 — balasundram (2020-05-19T07:59:58Z)

I ran this code, do let me know if the syntax in which i am supposed to use this, i am new to this game.
wget -q -O - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -

"echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list"
am i supposed to break this code and enter in the terminal??



---

### 评论 #3 — ableeker (2020-05-19T21:14:13Z)

I'm assuming these commands are from the installation guide?

These commands should work. There maybe a couple of issues here, though. These are 2 commands, for instance, on separate lines. Yes, they should be used in a terminal window. The second one (starting with echo) has double quotes around them in your comment, you shouldn't use quotes around the command in the terminal, and I'm assuming you didn't. Both of these commands in themselves combine two separate commands. So if you can't run these commands in this form, you could just split them up.

The first part of the first command (starting with wget) downloads a gpg key from the address in the command. You can also enter just the address in a browser, and it should prompt you to save it somewhere. Or you could download it by entering the following command in the terminal:

`wget -Orocm.gpg.key http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key`

When you've got the file saved, it then wants to add it to the key ring. You can do that by going in the terminal to the download location, and entering the following command:

`sudo apt-key add rocm.gpg.key`

The second command should create a file with some content. You could also do that by first issuing the following comand:

`sudo nano /etc/apt/sources.list.d/rocm.list`

Then copy, or enter the following content in that file, and save it:

`deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main`

When you've done that, you can install ROCm by issuing the following commands:

`sudo apt update`
`sudo apt install rocm-dev`

You might want to install rocm-dkms, but that doesn't work for Ubuntu 20.04, as it needs 18.04, or at least kernel 5.3. That's why I've installed rocm-dev, which works on standard 20.04.

---

### 评论 #4 — balasundram (2020-05-20T03:39:11Z)

I fallowed your instructions, installed rocm-dev. 
then when i checked with the rocminfo and clinfo commands, i got  HSA API CALL error for rocminfo, and getdevice(-1) error for clinfo.
![clinfo](https://user-images.githubusercontent.com/54479906/82402144-540bc800-9a79-11ea-92b8-badc1a5b3b5e.png)
![rocminfo](https://user-images.githubusercontent.com/54479906/82402145-553cf500-9a79-11ea-898f-7b3f6f130bb2.png)
I am trying to set up a AMD RADEON RX 560x gpu based machine learning setup in my linux ubuntu 20.04. I am having trouble with ROCM, so is there any other way around??


---

### 评论 #5 — ableeker (2020-05-20T20:49:09Z)

Did you complete the installation instructions in the guide? After installing rocm-dev you need to add yourself to the video group (and possibly to the render group). To do that you enter the following command:

`sudo usermod -a -G video $LOGNAME`

And then you have to create an udev file:

`sudo nano /etc/udev/rules.d/70-kfd.rules`

The content of this file should be the following:

`SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"`

And to make clinfo work you have to install libtinfo5, or libncurses5. This isn't in the guide unfortunately.

---

### 评论 #6 — rkothako (2020-05-21T10:48:57Z)

Hi @ableeker,
Current ROCm3.3 officially supports Ubuntu 18.04. It might work with 20.04 now but we can not claim as ROCm 3.3 was not validated on Ubuntu 20.04 as it was not available when ROCm 3.3 released.

Ubuntu 20.04 support started internally, validation is in progress and we are going to officially announce Ubuntu 20.04 support for ROCm by Jun or July. By that time, we will update installation guide properly as per the needs.

---

### 评论 #7 — ableeker (2020-05-21T20:47:41Z)

@rkothako, that's great!

---

### 评论 #8 — ouening (2020-05-22T07:24:37Z)

Hi @ableeker , I followed your instruction to install rocm-dev in Ubuntu20.04, but when I excute commond:
```
opt/rocm-3.3.0/bin/rocminfo
```
I got errors:
```
ROCk module is loaded
turing is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
How can I fix it? Thank you!

---

### 评论 #9 — alfabuster (2020-05-22T12:28:34Z)

Hi @ouening , I've got the same error around 1 week ago. I think on this moment we can't fix problem. I think this problem will resolved in the next rocm release 3.4 or 4.0, I don't know the right number, but we can only wait for fixing problem in the next releases...

---

### 评论 #10 — ableeker (2020-05-23T12:04:48Z)

ROCm 3.3 works on my computer running Ubuntu 20.04 with an RX Vega 64. This is what I do to install rocm-dev.

> sudo apt update
> sudo apt dist-upgrade
> sudo apt install libnuma-dev
> sudo reboot
> 
> Download http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key
> sudo apt-key add rocm.gpg.key
> 
> sudo nano /etc/apt/sources.list.d/rocm.list
> deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main
> 
> sudo apt update
> sudo apt install rocm-dev
> 
> sudo usermod -a -G video $LOGNAME
> sudo usermod -a -G render $LOGNAME
> 
> sudo nano /etc/adduser.conf
> ADD_EXTRA_GROUPS=1
> EXTRA_GROUPS="render,video"
> 
> sudo nano /etc/udev/rules.d/70-kfd.rules
> SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"
> 
> sudo apt install libtinfo5
> 
> /opt/rocm/bin/rocminfo
> /opt/rocm/opencl/bin/x86_64/clinfo`

rocminfo:

ROCk module is loaded
ableeker is member of video group

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

clinfo:

Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3098.0)
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
  Driver Version                                  3098.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Vega 10 XL/XT [Radeon RX Vega 56/64]
  Device Topology (AMD)                           PCI-E, 03:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               64
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1630MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              8573157376 (7.984GiB)
  Global free memory (AMD)                        8372224 (7.984GiB)
  Global memory channels (AMD)                    64
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7287183769 (6.787GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    7287183769 (6.787GiB)
  Preferred total size of global vars             8573157376 (7.984GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26751
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
    Max number of read/write image args           64
  Max number of pipe args                         16
  Max active pipe reservations                    16
  Max pipe packet size                            2992216473 (2.787GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        7287183769 (6.787GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)                      
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)                    
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                262144 (256KiB)
    Max size                                      8388608 (8MiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  P2P devices (AMD)                               <printDeviceInfo:147: get number of CL_DEVICE_P2P_DEVICES_AMD : error -30>
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Thu Jan  1 01:00:00 1970)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             64
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

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

---

### 评论 #11 — Sprinterfreak (2020-12-04T01:23:48Z)

Following the recipe from @ableeker and little additional tweeks, i also got it finaly running on Ubuntu 20.04.1.

```
# Additional required packages for running boinc-client-opencl
apt-get install rccl miopen-opencl mesa-opencl-icd ocl-icd-opencl-dev

# Link clinfo into PATH, otherwise boinc doesn't recognize the gpu
ln -s /opt/rocm/opencl/bin/clinfo /usr/local/bin/clinfo
```

Issues
* rocminfo somehow segfaults and getting stuck unkillable



---

### 评论 #12 — ROCmSupport (2020-12-04T09:45:04Z)

Now ROCm is officially supported for Ubuntu 20.04 and installation works well.
Request you to file any issues as separate tickets.
Our support team will respond asap.

---
