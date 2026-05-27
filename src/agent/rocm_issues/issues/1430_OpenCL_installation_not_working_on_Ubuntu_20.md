# OpenCL installation not working on Ubuntu 20

> **Issue #1430**
> **状态**: closed
> **创建时间**: 2021-03-26T21:32:02Z
> **更新时间**: 2021-04-01T05:07:02Z
> **关闭时间**: 2021-04-01T05:07:01Z
> **作者**: amartincolby
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1430

## 描述

Coming over from https://github.com/RadeonOpenCompute/ROCm/issues/1411 but I am opening a new ticket because that issue is trying to use an unsupported card. Long story short, the OpenCL installation on Ubuntu 20 does not appear to be working correctly. I am running a Vega Frontier Edition Air, so my card is supported. I uninstalled everything before starting the ROCm installation and it all went smoothly. The problem arises when I try to run the two installation confirmation checks:
```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```
Neither succeeds unless I run them as root with `sudo`. The first simply produces
```
ROCk module is loaded
Unable to open /dev/kfd read-write: Permission denied
aaron is member of render group
```
The second produces:
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3241.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```
If I prepend `sudo` to the commands, they produce the expected output.

This is more than simply the confirmation. When I try to run Luxmark or Blender, neither finds the graphics card as a valid OpenCL device. I tried running those applications as root in the hope that they would find the cards, but alas, no.

----

Editing to specify that I am using Ubuntu 20.04.2 LTS.

---

## 评论 (9 条)

### 评论 #1 — ableeker (2021-03-27T15:23:24Z)

I'm running only OpenCL on Ubuntu 20.10, on a Vega 64 (gfx900), and it's working well. clinfo is working too, running without, as well as running with sudo. I didn't have rocminfo, but when I install it, it's running well without sudo too. It's also running Folding@Home, Blender, Luxmark, darktable, and some apps, all of them recognising, and using OpenCL on the GPU.

I've only installed OpenCL, which is all I need from RoC, using the following command:

`sudo apt install rocm-opencl`

I haven't installed rocm-dkms, because I'm running 20.10. I've made myself a member of both the video, and the render group, just to be sure.

The installation guide mentions the kfd udev rule 70-kfd.rules:

`echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules`

Maybe that group should be render, but it may fix the kfd error message.

---

### 评论 #2 — amartincolby (2021-03-28T00:28:46Z)

I am not sure what was happening. Linux logs had basically no information. But after another uninstall, reboot, reinstall, reboot, then another reboot for good measure, the two test commands now work as expected. Unfortunately, I am now left with even less information than before since both LuxMark and Blender still do not recognize the OpenCL device. I did some testing in _0 A.D._ to confirm good gaming performance and it worked perfectly. If anyone has any logs or tests I can run to better diagnose this, I am open to trying anything.

---

### 评论 #3 — amartincolby (2021-03-28T21:11:09Z)

I have been experimenting and can get the OpenCL device to be recognized by Blender and Luxmark if I use the `amdgpu-install` script from the official driver package with the `--opencl=rocr` flag.

I opened a ticket on the ROCr issue list (https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/119) but the long and the short of it is that the only piece of logging that provides any insight for both LuxMark and Blender is this entry when they crash:
```
Mar 28 16:12:45 aaron-desktop blender_blender.desktop[3523]: Memory access fault by GPU node-1 (Agent handle: 0x7f4b9b12d000) on address 0x2c9dd000. Reason: Page not present or supervisor privilege.
```
This does not _appear_ to be related to the ROCm dkms install failing to reveal the device to Blender and Luxmark, but since I am grasping at straws, I thought it may be of some small value.

---

### 评论 #4 — ROCmSupport (2021-03-29T04:56:18Z)

Hi @amartincolby 
Thanks for reaching out.
I will check this for you and get back asap.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-03-29T04:59:03Z)

> 
> 
> I am not sure what was happening. Linux logs had basically no information. But after another uninstall, reboot, reinstall, reboot, then another reboot for good measure, the two test commands now work as expected. Unfortunately, I am now left with even less information than before since both LuxMark and Blender still do not recognize the OpenCL device. I did some testing in _0 A.D._ to confirm good gaming performance and it worked perfectly. If anyone has any logs or tests I can run to better diagnose this, I am open to trying anything.

If clinfo commands shows the information properly, it means OpenCL finds the devices well. So Blender, Luxmark or any other app should detect GPU at-least.
Can you please help me with the outputs of /opt/rocm/opencl/bin/clinfo and /opt/rocm/bin/rocminfo.
Thank you.

---

### 评论 #6 — amartincolby (2021-03-30T05:02:37Z)

Log dumps attached
<details closed>
<summary>/opt/rocm/opencl/bin/clinfo</summary>
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3241.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XTX [Radeon Vega Frontier Edition]
  Device Topology:				 PCI[ B#7, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1600Mhz
  Address bits:					 64
  Max memory allocation:			 14588628168
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 16384
  Max image 3D height:				 16384
  Max image 3D depth:				 8192
  Max samplers within kernel:			 26723
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 14588628168
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1703726280
  Max global variable size:			 14588628168
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f1da36b6d10
  Name:						 gfx900:xnack-
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3241.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program
</details>
<details closed>
<summary>/opt/rocm/bin/rocminfo</summary>
ROCk module is loaded
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
  Name:                    AMD FX(tm)-8350 Eight-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD FX(tm)-8350 Eight-Core Processor
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
    L1:                      16384(0x4000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16341288(0xf95928) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16341288(0xf95928) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-0213fbccac4a48c4               
  Marketing Name:          Vega 10 XTX [Radeon Vega Frontier Edition]
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
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   1792                               
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
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900:xnack-   
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
</details>
And this is the log when attempting to start Luxrender. I ran this a minute after running the above two commands.

```
2021-03-30 01:01:07 - RUNTIME ERROR: No OpenCL device selected or available
```

---

### 评论 #7 — ROCmSupport (2021-03-30T06:42:25Z)

Strange to see this error with Luxmark.
Can you please export below env before launching Luxmark and share an update.
export LD_LIBRARY_PATH=/opt/rocm/opencl/lib

Thank you.

---

### 评论 #8 — amartincolby (2021-03-31T22:04:44Z)

SUCCESS! And Luxmark successfully ran! I am now validating behaviors. I am encountering a problem with getting the Blender viewport render to work on the GPU, but I suspect that that problem is associated with Blender since it involves a split kernel failure.

---

### 评论 #9 — ROCmSupport (2021-04-01T05:07:01Z)

Thanks @amartincolby for the confirmation. Good to know that issue is gone with the workaround.
I am closing it now.
Feel free to open a new issue, if any.
Thank you.

---
