# [Issue]: With MI300 GPUs, rocm-smi --showpids lists processes that don't actually use the GPU(s)

- **Issue #:** 4411
- **State:** open
- **Created:** 2025-02-24T09:21:20Z
- **Updated:** 2025-04-25T06:45:37Z
- **Labels:** Under Investigation, AMD Instinct MI300A, ROCm 6.3.3
- **URL:** https://github.com/ROCm/ROCm/issues/4411

### Problem Description

We have a daemon that uses the amd-smi/rocm-smi API to update the GPU information every couple of seconds. The daemon itself doesn't have any OpenCL/HIP/... code, so it doesn't actually "use" the GPU(s). On our machine with MI300 GPUs, rocm --showpids lists the daemon as KFD process:

```
$ rocm-smi --showpids


============================ ROCm System Management Interface ============================
===================================== KFD Processes ======================================
KFD process information:
PID    	PROCESS NAME	GPU(s)	VRAM USED	SDMA USED	CU OCCUPANCY	
1058463	<daemon>     	0     	0        	0        	0           	
==========================================================================================
================================== End of ROCm SMI Log ===================================
```
```
$ rocm-smi --showpidgpus


============================ ROCm System Management Interface ============================
================================== GPUs Indexed by PID ===================================
PID 1058463 is using 0 DRM device(s)
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

And more importantly, we cannot change the compute/memory mode, unless we shut down the daemon:

```
# rocm-smi --setcomputepartition TPX


============================ ROCm System Management Interface ============================
============================== Set compute partition to TPX ==============================
GPU[0]		: Device is currently busy, try again later
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

* It also happens with older ROCm versions
* It happens with all MI300 compute modes (SPX, TPX, CPX).
* It doesn't happen on machines with Radeon or MI210 GPUs.
* Using `rsmi_shut_down()` to shut down ROCm doesn't help. The process has to exit to make sure that rocm-smi --showpids doesn't list it anymore.
* The same happens with amd-smi and its API.


### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD Proto Sample : SH5-MI300A-A0

### GPU

AMD Instinct MI300A

### ROCm Version

6.3.3

### ROCm Component

_No response_

### Steps to Reproduce

It can be reproduced with this example:

```
#include <iostream>
#include <unistd.h>

#include <rocm_smi/rocm_smi.h>

int main() {
   // Initialize the ROCm SMI library
   rsmi_status_t status = rsmi_init(0);
   if (status != RSMI_STATUS_SUCCESS) {
      std::cerr << "Failed to initialize ROCm SMI library" << std::endl;
      return -1;
   }

   // Get the number of GPU devices
   uint32_t device_count = 0;
   status = rsmi_num_monitor_devices(&device_count);
   if (status != RSMI_STATUS_SUCCESS) {
      std::cerr << "Failed to get GPU device count" << std::endl;
      rsmi_shut_down();
      return -1;
   }

   std::cout << "Number of GPUs detected: " << device_count << std::endl;

   // Iterate over each GPU and get memory usage
   for (uint32_t i = 0; i < device_count; i++) {
      uint64_t used_memory = 0;
      status = rsmi_dev_memory_usage_get(i, RSMI_MEM_TYPE_VRAM, &used_memory);
      if (status == RSMI_STATUS_SUCCESS) {
         std::cout << "GPU " << i << " VRAM Used: " << used_memory / (1024 * 1024) << " MB" << std::endl;
      } else {
         std::cerr << "Failed to get memory usage for GPU " << i << std::endl;
      }
   }

   std::cout << "Shutting down ROCm" << std::endl;
   // Shutdown the ROCm SMI library
   rsmi_shut_down();

   // Sleep for 100 seconds to simulate the daemon behaviour
   std::cout << "Sleeping for 100 seconds" << std::endl;
   sleep(100);

   return 0;
}
```

While the process is sleeping, rocm-smi lists the process as KFD process.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module version 6.10.5 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.14
Runtime Ext Version:     1.6
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
  Name:                    AMD Proto Sample : SH5-MI300A-A0   
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Proto Sample : SH5-MI300A-A0   
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
  Max Clock Freq. (MHz):   3700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            48                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    131174896(0x7d191f0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    131174896(0x7d191f0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131174896(0x7d191f0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131174896(0x7d191f0) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx940                             
  Uuid:                    GPU-8a034d0fdebb161c               
  Marketing Name:          AMD Instinct MI300A                
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
    L2:                      4096(0x1000) KB                    
    L3:                      262144(0x40000) KB                 
  Chip ID:                 29856(0x74a0)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2100                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            228                                
  SIMDs per CU:            4                                  
  Shader Engines:          24                                 
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    TRUE                               
  Memory Properties:       APU
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    2048(0x800)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 166                                
  SDMA engine uCode::      22                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    98381172(0x5dd2d74) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    98381172(0x5dd2d74) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    98381172(0x5dd2d74) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 4                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx940:sramecc+:xnack-
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

### Additional Information

_No response_