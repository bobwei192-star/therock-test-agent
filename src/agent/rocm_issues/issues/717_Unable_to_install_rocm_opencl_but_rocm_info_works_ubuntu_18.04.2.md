# Unable to install rocm opencl but rocm info works ubuntu 18.04.2

> **Issue #717**
> **状态**: closed
> **创建时间**: 2019-02-21T14:48:07Z
> **更新时间**: 2019-03-09T06:40:32Z
> **关闭时间**: 2019-03-08T20:47:40Z
> **作者**: guruvyasa
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/717

## 描述

I have a new laptop with AMD Radeon RX 560X gpu and Ryzen 5 CPU. After juggling around with kernels in ubuntu 18.04 finally managed to get rocm installed with kernel 4.18.0-041800-generic. I havent tried higher kernel versions yet. 
`
$/opt/rocm/bin/rocminfo 

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
  BDFID:                   1024                               
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    8388224KB                          
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
`
But clinfo fails

`
$/opt/rocm/opencl/bin/x86_64/clinfo 

ERROR: clGetPlatformIDs(-1001)
`

Here is output of  dmesg | grep amdgpu

`
[    3.211254] [drm] amdgpu kernel modesetting enabled.
[    3.212613] [drm] amdgpu version: 19.10.7.418
[    3.223189] amdgpu 0000:01:00.0: can't find IRQ for PCI INT A; please try using pci=biosirq
[    3.246300] [drm:amdgpu_get_bios [amdgpu]] *ERROR* ACPI VFCT table present but broken (too short #2)
[    3.248099] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0x0000
[    3.249577] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0x0000
[    3.250937] [drm:amdgpu_get_bios [amdgpu]] *ERROR* Unable to locate a BIOS ROM
[    3.252222] amdgpu 0000:01:00.0: Fatal error during GPU init
[    3.253493] [drm] amdgpu: finishing device.
[    3.254986] amdgpu: probe of 0000:01:00.0 failed with error -22
[    3.256307] fb: switching to amdgpudrmfb from EFI VGA
[    3.257801] amdgpu 0000:04:00.0: can't find IRQ for PCI INT A; please try using pci=biosirq
[    3.259086] amdgpu 0000:04:00.0: VRAM: 1024M 0x000000F400000000 - 0x000000F43FFFFFFF (1024M used)
[    3.259091] amdgpu 0000:04:00.0: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[    3.259095] amdgpu 0000:04:00.0: AGP: 267419648M 0x000000F800000000 - 0x0000FFFFFFFFFFFF
[    3.259321] [drm] amdgpu: 1024M of VRAM memory ready
[    3.259325] [drm] amdgpu: 6930M of GTT memory ready.
[    3.562486] [drm:construct [amdgpu]] *ERROR* construct: Invalid Connector ObjectID from Adapter Service for connector index:2! type 0 expected 3
[    3.562569] [drm:construct [amdgpu]] *ERROR* construct: Invalid Connector ObjectID from Adapter Service for connector index:3! type 0 expected 3
[    3.625905] amdgpu 0000:04:00.0: fb0: amdgpudrmfb frame buffer device
[    3.648141] amdgpu 0000:04:00.0: ring gfx uses VM inv eng 0 on hub 0
[    3.648193] amdgpu 0000:04:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    3.648245] amdgpu 0000:04:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    3.648296] amdgpu 0000:04:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[    3.648347] amdgpu 0000:04:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[    3.648397] amdgpu 0000:04:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[    3.648447] amdgpu 0000:04:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[    3.648497] amdgpu 0000:04:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[    3.648548] amdgpu 0000:04:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[    3.648598] amdgpu 0000:04:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[    3.648648] amdgpu 0000:04:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[    3.648696] amdgpu 0000:04:00.0: ring vcn_dec uses VM inv eng 1 on hub 1
[    3.648745] amdgpu 0000:04:00.0: ring vcn_enc0 uses VM inv eng 4 on hub 1
[    3.648794] amdgpu 0000:04:00.0: ring vcn_enc1 uses VM inv eng 5 on hub 1
[    3.648843] amdgpu 0000:04:00.0: ring vcn_jpeg uses VM inv eng 6 on hub 1
[    3.653086] [drm] Initialized amdgpu 3.27.0 20150101 for 0000:04:00.0 on minor 0

`

I tried adding pci=biosirq but does not work. Please help me out with this


---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2019-03-08T20:47:40Z)

Hi @guruvyasa 

It appears that your system has both a discrete GPU (a Radeon RX 560X) and an integrated GPU (as part of your Raven Ridge APU). At this time, ROCm [does not support simultaneously running dGPU and iGPUs](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66).

I recommend:

1. Try disabling your iGPU in your laptop's BIOS if you want to use your dGPU for ROCm work
2. Show the output of `dmesg | grep kfd`
3. Moving down to 18.04.1 and running the `rock-dkms` drivers. ROCm does not yet officially support 18.04.2.

---

### 评论 #2 — guruvyasa (2019-03-09T06:40:32Z)

Thank you for the reply. There is no option to disable  iGPU in the BIOS. The output of 
```
$dmesg | grep kfd
[   24.656937] kfd kfd: Allocated 3969056 bytes on gart
[   24.657326] kfd kfd: added device 1002:15dd

```

---
