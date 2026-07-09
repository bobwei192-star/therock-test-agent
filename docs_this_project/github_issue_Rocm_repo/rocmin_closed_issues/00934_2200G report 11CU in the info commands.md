# 2200G report 11CU in the info commands

- **Issue #:** 934
- **State:** closed
- **Created:** 2019-11-14T10:11:55Z
- **Updated:** 2023-12-18T16:15:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/934

After installling ROCm 2.9 into the Limux Mint 19.2 machine, aside from OpenCL programs can only run in sudo mode, another strange issue is that both info commands claim that there are 11 compute units, when the Ryzen 2200G APU spec said that there should only be 8. It is very unlikely that my APU won a lottery, so is it that ROCm hardcoded somthing by mistake?
```
$ sudo /opt/rocm/opencl/bin/x86_64/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 AMD Ryzen 3 2200G with Radeon Vega Graphics
  Device Topology:				 PCI[ B#8, D#0, F#0 ]
  Max compute units:				 11
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
  Max clock frequency:				 1100Mhz
  Address bits:					 64
  Max memory allocation:			 6244881510
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 5597
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
  Global memory size:				 7346919424
  Constant buffer size:				 6244881510
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1949914214
  Max global variable size:			 6244881510
  Max global variable preferred total size:	 7346919424
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 Yes
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 1
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
  Platform ID:					 0x7fd0c2e50d30
  Name:						 gfx902+xnack
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2982.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```

```
$ sudo /opt/rocm/bin/rocminfo
ROCk module is loaded
Failed to get user name to check for video group membership
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
  Name:                    AMD Ryzen 3 2200G with Radeon Vega Graphics
  Marketing Name:          AMD Ryzen 3 2200G with Radeon Vega Graphics
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
  Max Clock Freq. (MHz):   3500                               
  BDFID:                   2048                               
  Internal Node ID:        0                                  
  Compute Unit:            4                                  
  SIMDs per CU:            4                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16776832(0xfffe80) KB              
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
  Marketing Name:          AMD Ryzen 3 2200G with Radeon Vega Graphics
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
  BDFID:                   2048                               
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
      Acessible by all:        FALSE                              
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