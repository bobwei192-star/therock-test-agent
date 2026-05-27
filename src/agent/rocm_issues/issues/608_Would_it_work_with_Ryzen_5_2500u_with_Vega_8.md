# Would it work with Ryzen 5 2500u with Vega 8 

> **Issue #608**
> **状态**: closed
> **创建时间**: 2018-11-11T15:55:46Z
> **更新时间**: 2021-01-07T10:06:54Z
> **关闭时间**: 2021-01-07T10:06:54Z
> **作者**: RanaBan
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/608

## 标签

- **Question** (颜色: #cc317c)

## 描述

I don't know whether Vega 8 GPU is supported or not. I have tried to install it but "clinfo" gives
"terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted"
Then "pip3 install ./tensorflow-1.8.0-cp35-cp35m-manylinux1_x86_64.whl" gives
"tensorflow-1.8.0-cp35-cp35m-manylinux1_x86_64.whl is not a supported wheel on this platform."



---

## 评论 (28 条)

### 评论 #1 — jlgreathouse (2018-11-12T03:28:21Z)

Some ROCm user-level software should work with the GPUs in Raven Ridge APUs if you are using upstream Linux kernels. The ROCm drivers shipped as part of ROCm 1.9.x do not fully work with Raven Ridge GPUs;  there are patches required to the IOMMU drivers which are only part of upstream at this time.

In addition, even with proper driver support, your motherboard may still prevent your APU from being supported. APU support is detected through ACPI CRAT tables, which should be made available by your system BIOS. However, many consumer motherboard vendors either do not include CRAT tables in their BIOS, or include malformed CRAT tables. If this is the case, our `amdkfd` driver will still not work with your GPU.

If your BIOS does provide proper CRAT listings, and you are using an upstream driver (e.g. installing user-land ROCm code on Fedora 29), then OpenCL should work with your Rave Ridge APU. Our HIP and HCC software is not shipped with Raven Ridge support enabled by default, however.

---

### 评论 #2 — Johnreidsilver (2018-11-12T17:41:47Z)

CRAT tables doesn't seem to be an issue with desktop motherboards.
Any plans to enable RR in HIP/HCC ? Any hope for ROCm 2.0 ?

---

### 评论 #3 — jlgreathouse (2018-11-12T18:35:40Z)

It depends on the motherboard. I have one on my desk right now that includes malformed CRAT tables that do not parse correctly (and thus require a driver modification to work properly).

ROCm 2.0 will not enable Raven Ridge APUs in HIP or HCC by default.

---

### 评论 #4 — Johnreidsilver (2018-11-13T11:49:20Z)

Isn't it easier to just inform the MB manufacturer to correct the CRAT table in the next BIOS update instead of customizing every "faulty" MB in the code?

---

### 评论 #5 — jlgreathouse (2018-11-13T12:54:39Z)

Not if the motherboard manufacturers do not update their BIOS to fix the problem, no. That said, chasing every possible incorrect (or missing) CRAT table with a one-off workaround is an untenable solution. We're working on something more long-term, but it's not in place yet.

---

### 评论 #6 — RanaBan (2018-11-16T19:13:29Z)

This is a dell inspiron laptop. It shows an error message every time I switch-on the laptop. I should remove rocm.

---

### 评论 #7 — jlgreathouse (2018-11-16T19:35:42Z)

What error message do you see? "An error message" is not specific enough to help us here.

---

### 评论 #8 — RanaBan (2018-11-17T15:34:48Z)

As given, I ran "/opt/rocm/bin/rocminfo" which should have listed GPUs but given me 
"hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104"

I have found in "https://gpuopen.com/rocm-tensorflow-1-8-release/" that their is a pre-built tensorflow package in radeon repo. I have downloaded and tried to install it using "pip3 install ./tensorflow-1.8.0-cp35-cp35m-manylinux1_x86_64.whl", but it says, 
"tensorflow-1.8.0-cp35-cp35m-manylinux1_x86_64.whl is not a supported wheel on this platform."



---

### 评论 #9 — jlgreathouse (2018-11-17T18:02:29Z)

HI @RanaBan 

I apologize, I thought that "every time I switch-on the laptop" that you were describing an error that happens during boot, rather than an error that happens when you run an application.

What OS and version are you running?
What is the output of `dmesg | grep kfd`?

---

### 评论 #10 — RanaBan (2018-11-18T02:48:49Z)

It stopped giving that crash report. I have attached all log files related
to this. No output given

Ubuntu 18.04.1 LTS

dmesg | grep kfd No output given

On Sat, Nov 17, 2018 at 11:32 PM Joseph Greathouse <notifications@github.com>
wrote:

> HI @RanaBan <https://github.com/RanaBan>
>
> I apologize, I thought that "every time I switch-on the laptop" that you
> were describing an error that happens during boot, rather than an error
> that happens when you run an application.
>
> What OS and version are you running?
> What is the output of dmesg | grep kfd
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/608#issuecomment-439635819>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Aq3XMzv8uVCWzUR1GtV93frzN2_SVwwVks5uwE84gaJpZM4YYjHq>
> .
>


---

### 评论 #11 — jlgreathouse (2018-11-18T16:18:28Z)

Hi @RanaBan 

I do not believe you attached anything to your last message. A further set of questions:

- Could you show the output of `uname -r`
- Could you show the output of `dkms status`

---

### 评论 #12 — RanaBan (2018-11-18T20:18:51Z)

I apologize. I had attached those files from my gmail with the reply to your message. I don't know why they didn't reach. Those are attached with this message in a zip.
[crash_files.zip](https://github.com/RadeonOpenCompute/ROCm/files/2593179/crash_files.zip)

uname -r
4.15.0-38-generic

dkms status
amdgpu, 1.9-224, 4.15.0-38-generic, x86_64: installed

Thanks for giving me your valuable time. 
 

---

### 评论 #13 — jlgreathouse (2018-11-19T16:55:02Z)

Hi @RanaBan 

At this time, ROCm is not supported on our "Raven Ridge" APUs with the driver shipped in ROCm 1.9.x. There are modifications to the IOMMU driver needed that made their way upstream, but which are not part of Linux 4.15.

If you upgrade your kernel to 4.17 or above, you should be able to skip installing the `rock-dkms` package (not "rock" with a _k_) and instead just install the `rocm-dev` package to get all of our user-space tools.

With the upstream kernel and these user-space tools, OpenCL should work on Raven Ridge. At this time, however, our shipping versions of HCC and HIP will not work with Raven Ridge (and thus most of our rocX libraries will not work). Work is in flight to enable this, but I can't give you a precise timeline.

---

### 评论 #14 — 3D-360 (2018-11-19T17:45:49Z)

Joseph Greathouse,

Thanks for the "ROCm on Raven Ridge APUs" update.  I want to let you know that like Rana, my team is anxiously waiting for ROCm on Raven Ridge. We will follow your instructions and install ROCm 1.9.x  onto our systems: Ubuntu 18.04 with kernel 4.17+ on Ryzen 5 2400G APUs.  

We are simulating what will ultimately be an embedded system.  We will start testing with OpenCL on the APU and ROCm on a VEGA 56 card, but ultimately we want to run ROCm Tensor Flow on the APU alone.  We have been working on APU powered systems for years, and our code runs best when the CPU & GPU can share memory.  

Good luck getting  ROCm's HCC, HIP, and everything else working on Raven Ridge.  

---

### 评论 #15 — RanaBan (2018-11-19T18:43:30Z)

> Hi @RanaBan
> 
> At this time, ROCm is not supported on our "Raven Ridge" APUs with the driver shipped in ROCm 1.9.x. There are modifications to the IOMMU driver needed that made their way upstream, but which are not part of Linux 4.15.
> 
> If you upgrade your kernel to 4.17 or above, you should be able to skip installing the `rock-dkms` package (not "rock" with a _k_) and instead just install the `rocm-dev` package to get all of our user-space tools.
> 
> With the upstream kernel and these user-space tools, OpenCL should work on Raven Ridge. At this time, however, our shipping versions of HCC and HIP will not work with Raven Ridge (and thus most of our rocX libraries will not work). Work is in flight to enable this, but I can't give you a precise timeline.

Thanks.

---

### 评论 #16 — RanaBan (2018-11-19T18:45:01Z)

> Joseph Greathouse,
> 
> Thanks for the "ROCm on Raven Ridge APUs" update. I want to let you know that like Rana, my team is anxiously waiting for ROCm on Raven Ridge. We will follow your instructions and install ROCm 1.9.x onto our systems: Ubuntu 18.04 with kernel 4.17+ on Ryzen 5 2400G APUs.
> 
> We are simulating what will ultimately be an embedded system. We will start testing with OpenCL on the APU and ROCm on a VEGA 56 card, but ultimately we want to run ROCm Tensor Flow on the APU alone. We have been working on APU powered systems for years, and our code runs best when the CPU & GPU can share memory.
> 
> Good luck getting ROCm's HCC, HIP, and everything else working on Raven Ridge.

Thanks. I think it will be it will be available soon.

---

### 评论 #17 — emerth (2018-12-18T18:34:01Z)

@jlgreathouse 

"ROCm 2.0 will not enable Raven Ridge APUs in HIP or HCC by default."

I understand about the CRAT thing. Leave it aside.

Will it be possible to enable RR where the mobo presents correct CRAT? Or is that going to be post-2.0?

If it's post-2.0 I guess I'll throw up my hands and sell my 2400G.

---

### 评论 #18 — enihcam (2018-12-26T00:03:14Z)

Will Picasso be supported before it is released?

---

### 评论 #19 — ltzhang (2018-12-29T08:22:19Z)

Is there any recommended motherboard that do have the correct CRAT?

---

### 评论 #20 — luyatshimbalanga (2018-12-29T20:59:33Z)

Post installation result of ROCm 2.0 with Raven Ridge Mobile Ryzen 2500U from HP Envy x360 Convertible running on updated Fedora 29 (kernel 4.19.12)

```
rocminfo 
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
  Name:                    AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
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
  Max Clock Frequency (MHz):2000                               
  BDFID:                   768                                
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16776832KB                         
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
  Max Clock Frequency (MHz):1100                               
  BDFID:                   768                                
  Compute Unit:            11                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  50332672                           
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
```

```
clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (2783.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx902-xnack
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  2783.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Available                                Yes
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx
  Device Topology (AMD)                           PCI-E, 03:00.0
  Max compute units                               11
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1100MHz
  Graphics IP (AMD)                               9.2
  Device Partition                                (core)
    Max number of sub-devices                     11
    Supported partition types                     None
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Compiler Available                              Yes
  Linker Available                                Yes
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
  Global memory size                              7360856064 (6.855GiB)
  Global free memory (AMD)                        7188336 (6.855GiB)
  Global memory channels (AMD)                    2
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           6256727654 (5.827GiB)
  Unified memory for Host and Device              Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             5597
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        6256727654 (5.827GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 16:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902-xnack
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902-xnack
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx902-xnack
```
Interesting is the number of compute units for Vega8: 11.

```
dmesg | grep hcc
[    1.285480] xhci_hcd 0000:03:00.3: hcc params 0x0270ffe5 hci version 0x110 quirks 0x0000000840000410
[    1.288861] xhci_hcd 0000:03:00.4: hcc params 0x0260ffe5 hci version 0x110 quirks 0x0000000840000410
```
Hope it helps.

---

### 评论 #21 — emerth (2018-12-29T22:46:28Z)

@luyatshimbalanga

That shows rocminfo and clinfo can read the APU specs...

Have you been able to run any HCC code on your 2500U?

---

### 评论 #22 — luyatshimbalanga (2018-12-31T06:43:20Z)

@emerth 
Using [this example](https://gist.github.com/scchan/540d410456e3e2682dbf018d3c179008), hcc code succesfully build with a warning message
```
hcc -hc saxpy.cpp -o saxpyclang-8: warning: -amdgpu-target argument 'gfx902' is not recognized; using gfx803 instead [-Winvalid-command-line-argument]
'auto' is not a recognized processor for this target (ignoring processor)
```
It looks like Raven Ridge (gfx902) is not yet supported on [HCC](https://github.com/RadeonOpenCompute/hcc/wiki#how-to-use-hcc) so attempting to use gfx900 parameter led to the following result
```
./saxpy 
HSADevice::CreateKernel(): Unable to create kernel int, int, int, int, int, int, int, float, float*, int, int, int, int, int, int, int) 
  CreateKernel_raw=  _ZZ4mainEN3$_219__cxxamp_trampolineEPfiiiiiiifS0_iiiiiii
  CreateKernel_demangled=  main::$_2::__cxxamp_trampoline(float*, int, int, int, int, int, int, int, float, float*, int, int, int, int, int, int, int)
Aborted (core dumped)
```
Waiting for the ROCm team to bring 2500U (Raven Ridge) into play.

---

### 评论 #23 — emerth (2018-12-31T20:21:36Z)

Thanks @luyatshimbalanga!

I get similar on a 2400G with HCC using target gfx902 & gfx900. I never thought to try gfx803 but I expect it will not work.

For what it's worth I have run some OpenCL samples on a 2400G successfully using an ASUS "Prime X370 Pro" board.

---

### 评论 #24 — jlgreathouse (2019-01-03T17:04:51Z)

Hi all,

Yes, HCC and HIP need modification to use `gfx902+xnack` in order to support Raven Ridge, even if the system BIOS provides proper CRAT entries that will allow our ROCm drivers to properly detect the GPU. This is somewhat straightforward for HCC, but is more complex for HIP. In addition, all of the ROCm libraries would need to be recompiled to support this target as well.

---

### 评论 #25 — luyatshimbalanga (2019-01-05T06:53:01Z)

@jlgreathouse 
Could you estimate the time to get ROCm driver to support both HCC and HIP using`gfx902+0xnack` not to mention improving OpenCL especially for Blender Cycle rendering? I noticed a significant quicker video rendering on KDenlive using ROCm OpenCL than without.

---

### 评论 #26 — emerth (2019-01-08T20:54:54Z)

@jlgreathouse 

Thanks for sticking with us on the quest for ROCm Raven Ridge!

Where might we find details of the mods needed for HCC to produce binaries for gfx902+xnack? Or perhaps even an HCC branch (hope)?

I don't really need HIP to work but with HCC I can start developing code on my 2400G.

---

### 评论 #27 — mirh (2019-02-17T14:12:07Z)

I believe this sums up the issue with xnack: https://github.com/RadeonOpenCompute/hcc/issues/879#ref-issue-332614110

---

### 评论 #28 — ROCmSupport (2021-01-07T10:06:54Z)

Hi All,
ROCm on gfx902 is not officially supported as per https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support
Thank you.

---
