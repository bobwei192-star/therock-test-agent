# Ubuntu 18.04 install failed: tensorflow-1.8.0 is not a supported wheel on this platform.

> **Issue #583**
> **状态**: closed
> **创建时间**: 2018-10-23T11:46:12Z
> **更新时间**: 2018-12-24T22:50:04Z
> **关闭时间**: 2018-12-24T22:50:04Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/583

## 描述

Specs:
Radeon Rx 580 GPU 8gb
Intel i5 cpu
Ubuntu 18.04

After following the steps on the gpu open website, I got an error on the last command:
 pip3 install ./tensorflow-1.8.0-cp35-cp35m-manylinux1_x86_64.whl
tensorflow-1.8.0-cp35-cp35m-manylinux1_x86_64.whl is not a supported wheel on this platform.


I followed the steps from this link: https://gpuopen.com/rocm-tensorflow-1-8-release/

I tried:
Downgrading to python 3.5 in a virtual env
Upgrading to python 3.7
Made sure I have the latest driver for the rx 580 (18.30)
I have the latest Open CL as well


Any suggestions on a workaround? 

---

## 评论 (5 条)

### 评论 #1 — jlgreathouse (2018-10-23T18:17:39Z)

Hi @winsteadworks 

Are you willing to try Tensorflow 1.10 instead? The directions at [this site](https://rocm.github.io/dl.html) are more up-to-date than our older GPUOpen blog post.

Note that AMD does *not* support Tensorflow on our amdgpu-pro drivers. As such your mention of "18.30" implies to me that you may also be running the wrong drivers. You should [uninstall the amdgpu-pro drivers](https://support.amd.com/en-us/kb-articles/Pages/AMDGPU-PRO-Install.aspx) and [install ROCm 1.9.1 instead](https://rocm-documentation.readthedocs.io/en/latest/Installation_Guide/Installation-Guide.html#ubuntu-support-installing-from-a-debian-repository).

---

### 评论 #2 — ghost (2018-10-30T07:44:07Z)

@jlgreathouse I installed ROCm 1.9.1, however when I run the /opt/rocm/bin/rocminfo 
and /opt/rocm/opencl/bin/x86_64/clinfo in terminal after installing. It is only showing that I have 1 gpu.

I have 6 8gb Rx 580's total and I am running Ubuntu 18.04.

**Here is the output for /opt/rocm/bin/rocminfo**
```
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
  Name:                    Intel(R) Core(TM) i5-4460  CPU @ 3.20GHz
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
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3400                               
  BDFID:                   0                                  
  Compute Unit:            4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16288456KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16288456KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                                           
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1340                               
  BDFID:                   256                                
  Compute Unit:            36                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  16778240                           
    Dim[2]:                  0                                  
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
      Size:                    8388608KB                          
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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

**Here is /opt/rocm/opencl/bin/x86_64/clinfo output**
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2679.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Ellesmere [Radeon RX 470/480]
  Device Topology:				 PCI[ B#1, D#0, F#0 ]
  Max compute units:				 36
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
  Max clock frequency:				 1340Mhz
  Address bits:					 64
  Max memory allocation:			 7301444403
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26591
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 8589934592
  Constant buffer size:				 7301444403
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 3006477107
  Max global variable size:			 7301444403
  Max global variable preferred total size:	 8589934592
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
  Platform ID:					 0x7fa191eeadf0
  Name:						 gfx803
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2679.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```

---

### 评论 #3 — jlgreathouse (2018-10-30T13:45:24Z)

[Your CPU](https://ark.intel.com/products/80817/Intel-Core-i5-4460-Processor-6M-Cache-up-to-3-40-GHz-) can only have up to 16 PCIe 3 lanes directly connected to the CPU. As such, I suspect that you're hooking up your remaining GPUs through either southbridge-connected PCIe lanes or through a PCIe switch.

In either case, I would guess the problem here is that your connection between the missing GPUs and your CPU does not [support PCIe gen 3 atomics](https://github.com/RadeonOpenCompute/ROCm#supported-cpus), which is a requirement for your GPUs. For example, if your PCIe switch does not support the capability of forwarding PCIe atomics, you will not be able to use the gfx8 GPUs behind it with ROCm.

It is not possible at this time to enable gfx8 devices without the use of PCIe atomics. See [this discussion](451#issuecomment-422836032) for many more details about this.

---

### 评论 #4 — ghost (2018-11-15T07:41:07Z)

@jlgreathouse I have1 graphics card connected to a full pcie slot and then the rest are connected via riser cables to pcie x1 slots on an ASRock H81 Pro BTC motherboard. 

According to this link here: https://rocm.github.io/hardware.html it actually looks like my CPU (Intel i5-4460 - Haswell  @ 3.20GHz × 4 ) and my AMD RX 580 Sapphire Nitro + 8 gb cards are supported.

**Questions**
1. Is this an issue with my motherboard or CPU to run all my cards on rocm?

2. Would it be possible to run them on x1 slots for rocm? If not, is there any work being done to make it possible in the near future?

---

### 评论 #5 — jlgreathouse (2018-11-15T19:33:05Z)

Your GPU is supported in ROCm, and your CPU supports PCIe 3.0 atomics. However, as noted in our [hardware requirements list](https://rocm.github.io/hardware.html#supported-cpus), your GPU requires the ability to communicate PCIe atomics all the way to your CPU root complex. In particular: 

> "The system configuration can have the PCIe slots directly on CPU’s root port or a PCIe switch, but everything between the CPU and the GPU must support atomics. The CPU root must indicate PCIe AtomicOp Completion capabilities and any intermediate switch must indicate PCIe AtomicOp Routing capabilities."

As noted on [Intel's product listing for your CPU](https://ark.intel.com/products/80817/Intel-Core-i5-4460-Processor-6M-Cache-up-to-3-40-GHz-), the valid PCIe configurations for the 16 PCIe 3.0 lanes on your CPU are:
 - 1x16
 - 2x8
 - 1x8+2x4

Your motherboard's "1x16 + 5x1" (and PCIe 2.0 at that) is not directly supported by your CPU. As such, your PCIe lanes likely connect through either an external chip like a South Bridge, or through a PCIe switch.

Especially for consumer crypto-mining markets, most vendors that build motherboards with multiple PCIe slots like this using switches that do not support mechanisms such as PCIe 3.0 atomics. Such capabilities add cost and are not normally requested by folks looking to cram as many low-power GPUs into a box as they can.

However, as noted above, ROCm requires the ability to communicate using PCIe atomics all the way between your GPU to your CPU for our gfx8 GPUs. If you have a non-compliant switch somewhere in the middle, ROCm will not work with those GPUs. As such, the most likely problem here is this particular motherboard.

As for your second question, please see [this much longer discussion](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422835753) about our plans for support for running ROCm on gfx8 GPUs without PCIe atomics. The short version is: at this time, such support is not on our roadmap.

---
