# Check if TensorFlow use GPU 

> **Issue #1286**
> **状态**: closed
> **创建时间**: 2020-11-12T19:05:43Z
> **更新时间**: 2020-11-18T17:25:32Z
> **关闭时间**: 2020-11-18T17:25:32Z
> **作者**: YuriyTigiev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1286

## 描述

How to correctly check that the TensorFlow use GPU 

I used a script from the internet to check if TensorFlow uses gpu. 
The script shows that TensorFlow uses the only CPU, but I have two GPU RX580  with Crossfire Motherboard
How can I check if all installed and configured properly and TensorFlow use CPU and GPUs? 

Below my configuration 

```
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import to_categorical
from tensorflow.python.client import device_lib

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return local_device_protos
print(get_available_gpus())
```

Results 

```
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 1595132555139158661
, name: "/device:XLA_CPU:0"
device_type: "XLA_CPU"
memory_limit: 17179869184
locality {
}
incarnation: 15875141988421877768
physical_device_desc: "device: XLA_CPU device"
]
```

Configuration 


`Tensorflow Version: 2.3.1`



```
OS
--------------------------------------------------------------------------------
(base) yuriy@yuriy-System-Product-Name:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
```



```
Display
----------------------------------------------------------------------------------------
(base) yuriy@yuriy-System-Product-Name:~$ sudo lshw -C display
[sudo] password for yuriy: 
  *-display                 
       description: VGA compatible controller
       product: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:01:00.0
       version: ef
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:141 memory:e0000000-efffffff memory:f0000000-f01fffff ioport:e000(size=256) memory:f7200000-f723ffff memory:c0000-dffff
  *-display
       description: Display controller
       product: HD Graphics 530
       vendor: Intel Corporation
       physical id: 2
       bus info: pci@0000:00:02.0
       version: 06
       width: 64 bits
       clock: 33MHz
       capabilities: pciexpress msi pm bus_master cap_list
       configuration: driver=i915 latency=0
       resources: irq:140 memory:f6000000-f6ffffff memory:b0000000-bfffffff ioport:f000(size=64)
  *-display
       description: VGA compatible controller
       product: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:03:00.0
       version: ef
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom
       configuration: driver=amdgpu latency=0
       resources: irq:145 memory:c0000000-cfffffff memory:d0000000-d01fffff ioport:d000(size=256) memory:f7000000-f703ffff memory:f7040000-f705ffff

```


```
rocminfo
------------------------------------------------------------------------------------------
(base) yuriy@yuriy-System-Product-Name:~$ /opt/rocm/bin/rocminfo
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
  Name:                    Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
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
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4200                               
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
      Size:                    32758240(0x1f3d9e0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32758240(0x1f3d9e0) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
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
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1268                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
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
      Size:                    8388608(0x800000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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



```
clinfo
------------------------------------------------------------------------------------------------
(base) yuriy@yuriy-System-Product-Name:~$ /opt/rocm/opencl/bin/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3204.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
  Device Topology:				 PCI[ B#1, D#0, F#0 ]
  Max compute units:				 32
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
  Max clock frequency:				 1268Mhz
  Address bits:					 64
  Max memory allocation:			 7301444400
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
  Constant buffer size:				 7301444400
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 3006477104
  Max global variable size:			 7301444400
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
  Platform ID:					 0x7fa2d5862cd0
  Name:						 gfx803
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 3204.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 


```

---

## 评论 (8 条)

### 评论 #1 — rkothako (2020-11-13T07:46:05Z)

Thanks @YuriyTigiev 
Actually the code is correct and it works too.
Looks like GPUs in your machine are not detected once you import tensorflow.

I am able to see GPU devices when I try the same.

>>> device_lib.list_local_devices()
2020-11-13 02:43:17.914503: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties:
pciBusID: 0000:63:00.0 name: **Vega 10** [Radeon Instinct MI25]     ROCm AMD GPU ISA: gfx900
coreClock: 1.5GHz coreCount: 56 deviceMemorySize: 15.98GiB deviceMemoryBandwidth: 450.61GiB/s
2020-11-13 02:43:17.914593: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-11-13 02:43:17.914622: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-11-13 02:43:17.914685: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-11-13 02:43:17.914710: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-11-13 02:43:17.914905: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-11-13 02:43:17.914938: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-11-13 02:43:17.914954: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      0
2020-11-13 02:43:17.914968: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 0:   N
2020-11-13 02:43:17.915197: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/device:GPU:0 with 15385 MB memory) -> physical GPU (device: 0, name: Vega 10 [Radeon Instinct MI25], pci bus id: 0000:63:00.0)
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 13676232255965554329
, name: "/device:XLA_CPU:0"
device_type: "XLA_CPU"
memory_limit: 17179869184
locality {
}
incarnation: 10806548938991833760
physical_device_desc: "device: XLA_CPU device"
, name: "/device:XLA_GPU:0"
device_type: "XLA_GPU"
memory_limit: 17179869184
locality {
}
incarnation: 15585289024294504566
physical_device_desc: "device: XLA_GPU device"
, name: "/device:GPU:0"
device_type: "GPU"
memory_limit: 16133306496
locality {
  bus_id: 2
  numa_node: 1
  links {
  }
}
incarnation: 11683350509989147072
physical_device_desc: "device: 0, name: **Vega 10** [Radeon Instinct MI25], pci bus id: 0000:63:00.0"
]


---

### 评论 #2 — YuriyTigiev (2020-11-13T11:07:47Z)

Sorry, but I don't understand how did you check your card.
Is it shell or python command device_lib.list_local_devices() ?
Could you briefly write steps for checking my configuration.

I have two identical cards, but  rocminfo displays only one of them. Why ?
I have  a motherboard which supports AMD CrossFire. Is it could be an issue ? 




```
yuriy@PC-Ubuntu:~$ /opt/rocm/bin/rocminfo
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
  Name:                    Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz
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
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4400                               
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
      Size:                    32757572(0x1f3d744) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32757572(0x1f3d744) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
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
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1268                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
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
      Size:                    8388608(0x800000) KB               
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
      Name:                    amdgcn-amd-amdhsa--gfx803          
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




> I am able to see GPU devices when I try the same.



---

### 评论 #3 — YuriyTigiev (2020-11-13T13:47:44Z)

Additional info. Still detect only one card

```
yuriy@PC-Ubuntu:/opt/rocm/bin$ python3 rocm_smi.py


======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr   SCLK    MCLK     Fan    Perf  PwrCap  VRAM%  GPU%  
0    32.0c  30.194W  588Mhz  1750Mhz  29.8%  auto  120.0W    6%   0%    
================================================================================
============================= End of ROCm SMI Log ==============================

```

---

### 评论 #4 — xuhuisheng (2020-11-13T20:24:48Z)

Two rx580 cards? Might meet the PCIe atomic issue, one PCIe support atomic,  the other didnot.
dmesg|grep kfd can see the reject info.

---

### 评论 #5 — YuriyTigiev (2020-11-14T05:50:02Z)

> Two rx580 cards? Might meet the PCIe atomic issue, one PCIe support atomic, the other didnot.
> dmesg|grep kfd can see the reject info.

yuriy@PC-Ubuntu:~$ dmesg|grep kfd
[    2.334689] kfd kfd: Allocated 3969056 bytes on gart
[    2.335193] kfd kfd: added device 1002:67df
[    2.368583] kfd kfd: skipped device 1002:67df, PCI rejects atomics


Is it a bug or ....?  Can an user use a few AMD video cards with tensorflow-rocm? 



---

### 评论 #6 — xuhuisheng (2020-11-14T06:24:28Z)

I think it is a bug, but AMD said this is a feature.
The gfx803 like RX580, RX480 need both cpu and motherboard support PCIe Atomics. Yes, only gfx803 need this, Anyother cards didnot need PCIe atomics feature. Then we will meet some trouble on this PCIe atomics feature.

The PCIe atomics feature is so complicated, it cost a large section to describe on README. https://github.com/RadeonOpenCompute/ROCm#supported-cpus

1. If you used a cpu older than haswell (i3 4xxx),  4xxx can support PCIe atomics. 3xxx didnot. The kfd will reject gfx803.
2. If PCIe on motherboard didnot direct connect to CPU, e.g. connect to south bridge, the PCIe atomics will be disabled. the kfd will reject gfx803. I learned that the cpu has limited passthrough count, like i3/i5/i7 maybe could not support more than a PCIe 16x large possibility, so the second PCIe can only passthrough sourch bridge, then second card is rejected because of not connect directly to CPU.
3. If you used a PCIe connector, and connector didnot support PCIe atomics, the kfd will reject gfx803.

Related discussions that which motherboard could support PCIe atomics : https://github.com/RadeonOpenCompute/ROCm/issues/1146

So when we want to multiple gfx803 on one PC:

1. cpu newer than haswell and has more passthrough count, maybe e5-26xx-v4?
2. motherboard have more than one PCIe gen3 socket, and theses sockets have to connect CPU directly. Sorry I donot know which motherboard can do this.
3. donot use PCIe connector.

---

### 评论 #7 — YuriyTigiev (2020-11-14T08:29:32Z)

I have shared a screenshot of my pc configuration. Could you help me and check if my hardware sets the requirements for rocm?

![image](https://user-images.githubusercontent.com/22752322/99143143-acacce00-2674-11eb-812d-a8e9c68c7b13.png)


---

### 评论 #8 — ROCmSupport (2020-11-18T07:27:12Z)

Hi @YuriyTigiev 
As one of the cards are rejected in your configuration, we recommend to have PCI atomics supported config to proceed further.
Thank you.

---
