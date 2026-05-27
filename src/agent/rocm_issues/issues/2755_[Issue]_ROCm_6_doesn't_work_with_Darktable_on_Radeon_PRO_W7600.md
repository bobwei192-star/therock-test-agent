# [Issue]: ROCm 6 doesn't work with Darktable on Radeon PRO W7600

> **Issue #2755**
> **状态**: closed
> **创建时间**: 2023-12-19T21:29:52Z
> **更新时间**: 2023-12-21T23:31:19Z
> **关闭时间**: 2023-12-21T23:17:02Z
> **作者**: illwieckz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2755

## 描述

### Problem Description

Running Darktable with ROCm OpenCL fills the `dmesg` log with errors and makes Darktable crash.

I run a professionnal workstation sporting an AMD Radeon PRO W7600 and an AMD Ryzen Threadripper PRO 3955WX.
I installed AMDGPU-PRO 6.0 with ROCm 6.0, I installed the dkms module and the ROCm OpenCL stack.

### Operating System

Ubuntu 23.10 Mantic Minautor

### CPU

AMD Ryzen Threadripper PRO 3955WX

### GPU

Other

### Other

AMD Radeon PRO W7600

### ROCm Version

ROCm 6.0.0

### ROCm Component

ROCm

### Steps to Reproduce

```sh
wget 'https://repo.radeon.com/amdgpu-install/6.0/ubuntu/jammy/amdgpu-install_6.0.60000-1_all.deb'
sudo gdebi 'amdgpu-install_6.0.60000-1_all.deb'
sudo apt-get update
sudo apt-get install 'amdgpu-dkms' 'rocm-opencl-runtime'
sudo reboot

sudo apt-get install 'darktable'
darktable
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen Threadripper PRO 3955WX 16-Cores
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper PRO 3955WX 16-Cores
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
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3900                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    263724068(0xfb81c24) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    263724068(0xfb81c24) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    263724068(0xfb81c24) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1102                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon PRO W7600               
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      2048(0x800) KB                     
  Chip ID:                 29824(0x7480)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1940                               
  BDFID:                   33536                              
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 550                                
  SDMA engine uCode::      16                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1102         
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

### Additional Information

Some `dmesg` log:

```
[245121.541853] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[245121.541869] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x000000019e601000 from client 10
[245121.541876] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B32
[245121.541881] amdgpu 0000:83:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPC (0x5)
[245121.541886] amdgpu 0000:83:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[245121.541891] amdgpu 0000:83:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[245121.541895] amdgpu 0000:83:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[245121.541899] amdgpu 0000:83:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[245121.541903] amdgpu 0000:83:00.0: amdgpu: 	 RW: 0x0
[245192.524439] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[245192.524452] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x0000000000801000 from client 10
[245192.524458] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B32
[245192.524463] amdgpu 0000:83:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPC (0x5)
[245192.524468] amdgpu 0000:83:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[245192.524472] amdgpu 0000:83:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[245192.524476] amdgpu 0000:83:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[245192.524480] amdgpu 0000:83:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[245192.524484] amdgpu 0000:83:00.0: amdgpu: 	 RW: 0x0
[245214.965680] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[245214.965691] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00007f086c002000 from client 10
[245214.965695] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B32
[245214.965698] amdgpu 0000:83:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPC (0x5)
[245214.965701] amdgpu 0000:83:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[245214.965704] amdgpu 0000:83:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[245214.965707] amdgpu 0000:83:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[245214.965710] amdgpu 0000:83:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[245214.965713] amdgpu 0000:83:00.0: amdgpu: 	 RW: 0x0
[245219.905322] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[245219.905336] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00007f086c002000 from client 10
[245219.905342] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B32
[245219.905346] amdgpu 0000:83:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPC (0x5)
[245219.905351] amdgpu 0000:83:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[245219.905355] amdgpu 0000:83:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[245219.905359] amdgpu 0000:83:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[245219.905363] amdgpu 0000:83:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[245219.905367] amdgpu 0000:83:00.0: amdgpu: 	 RW: 0x0
[245220.301490] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[245220.301503] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00007f086c002000 from client 10
[245220.301508] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B32
[245220.301512] amdgpu 0000:83:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPC (0x5)
[245220.301517] amdgpu 0000:83:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[245220.301520] amdgpu 0000:83:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[245220.301524] amdgpu 0000:83:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[245220.301527] amdgpu 0000:83:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[245220.301531] amdgpu 0000:83:00.0: amdgpu: 	 RW: 0x0
[245287.498754] darktable[423198]: segfault at 0 ip 0000000000000000 sp 00007ffe371c06d8 error 14 in darktable[5582f96ce000+1000] likely on CPU 16 (core 0, socket 0)
[245287.498771] Code: Unable to access opcode bytes at 0xffffffffffffffd6.
[245296.577249] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[245296.577263] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00007f086c002000 from client 10
[245296.577269] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B32
[245296.577274] amdgpu 0000:83:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPC (0x5)
[245296.577279] amdgpu 0000:83:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[245296.577283] amdgpu 0000:83:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[245296.577287] amdgpu 0000:83:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[245296.577291] amdgpu 0000:83:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[245296.577296] amdgpu 0000:83:00.0: amdgpu: 	 RW: 0x0
[245297.009658] amdgpu 0000:83:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:0 pasid:0, for process  pid 0 thread  pid 0)
[245297.009671] amdgpu 0000:83:00.0: amdgpu:   in page starting at address 0x00007f086c002000 from client 10
[245297.009677] amdgpu 0000:83:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00000B32
[245297.009682] amdgpu 0000:83:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPC (0x5)
[245297.009687] amdgpu 0000:83:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[245297.009691] amdgpu 0000:83:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[245297.009695] amdgpu 0000:83:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[245297.009699] amdgpu 0000:83:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[245297.009703] amdgpu 0000:83:00.0: amdgpu: 	 RW: 0x0
```
