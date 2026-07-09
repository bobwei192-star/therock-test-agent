# [Issue]: rocminfo doesn't show GPU

- **Issue #:** 3897
- **State:** closed
- **Created:** 2024-10-15T08:11:33Z
- **Updated:** 2024-10-18T13:36:06Z
- **Labels:** Under Investigation, AMD Radeon Pro W7900, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3897

### Problem Description

NAME="Ubuntu"
VERSION="24.04.1 LTS (Noble Numbat)"
CPU: 
model name	: Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
GPU:
  Name:                    Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
  Marketing Name:          Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz



### Operating System

24.04.1 LTS (Noble Numbat)

### CPU

amd radeon hd 8750m

### GPU

AMD Radeon Pro W7900

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

just run rocminfo

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

/opt/rocm/bin/rocminfo --support
ROCk module version 6.8.5 is loaded
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
  Name:                    Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz
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
  Max Clock Freq. (MHz):   2600                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            4                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    12124424(0xb90108) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    12124424(0xb90108) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    12124424(0xb90108) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***             


### Additional Information

dpkg -l | grep rocm
ii  rocm                                             6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) software stack meta package
ii  rocm-cmake                                       0.13.0.60202-116~24.04                    amd64        rocm-cmake built using CMake
ii  rocm-core                                        6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-dbgapi                                      0.76.0.60202-116~24.04                    amd64        Library to provide AMD GPU debugger API
ii  rocm-debug-agent                                 2.0.3.60202-116~24.04                     amd64        Radeon Open Compute Debug Agent (ROCdebug-agent)
ii  rocm-developer-tools                             6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                                 1.0.0.60202-116~24.04                     amd64        Radeon Open Compute - device libraries
ii  rocm-gdb                                         14.2.60202-116~24.04                      amd64        ROCgdb
ii  rocm-hip-libraries                               6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime                                 6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime-dev                             6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-sdk                                     6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-language-runtime                            6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-llvm                                        18.0.0.24355.60202-116~24.04              amd64        ROCm core compiler
ii  rocm-ml-libraries                                6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-ml-sdk                                      6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl                                      2.0.0.60202-116~24.04                     amd64        clr built using CMake
ii  rocm-opencl-dev                                  2.0.0.60202-116~24.04                     amd64        clr built using CMake
ii  rocm-opencl-icd-loader                           1.2.60202-116~24.04                       amd64        OpenCL-ICD-Loader built using CMake
ii  rocm-opencl-runtime                              6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl-sdk                                  6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-openmp-sdk                                  6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) OpenMP Software development Kit.
ii  rocm-smi-lib                                     7.3.0.60202-116~24.04                     amd64        AMD System Management libraries
ii  rocm-utils                                       6.2.2.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                                         1.0.0.60202-116~24.04                     amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool


lsmod | grep amdgpu
amdgpu              19632128  0
amddrm_ttm_helper      12288  1 amdgpu
amdttm                110592  2 amdgpu,amddrm_ttm_helper
amddrm_buddy           20480  1 amdgpu
amdxcp                 12288  1 amdgpu
drm_exec               12288  1 amdgpu
drm_suballoc_helper    16384  1 amdgpu
amd_sched              61440  1 amdgpu
amdkcl                 32768  3 amd_sched,amdttm,amdgpu
drm_display_helper    237568  2 amdgpu,i915
i2c_algo_bit           16384  2 amdgpu,i915
video                  73728  3 acer_wmi,amdgpu,i915