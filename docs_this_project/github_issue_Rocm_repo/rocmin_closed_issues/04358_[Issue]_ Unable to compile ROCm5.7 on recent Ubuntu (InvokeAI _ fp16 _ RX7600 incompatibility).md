# [Issue]: Unable to compile ROCm5.7 on recent Ubuntu (InvokeAI + fp16 + RX7600 incompatibility)

- **Issue #:** 4358
- **State:** closed
- **Created:** 2025-02-08T15:26:02Z
- **Updated:** 2025-02-18T20:10:16Z
- **Labels:** Under Investigation, ROCm 5.7.0
- **URL:** https://github.com/ROCm/ROCm/issues/4358

### Problem Description

I am trying to compile the oldish version ROCm5.7 because it seems it's the last one fully working on my hardware (any update on this would be *much* appreciated).

Compilation fails on "`aqlprofile started due to rocr`" probably due to my OS (`Ubuntu 24.04`).
Is there a way around?
I need this just to run `PyTorch`-based applications (i.e.: `InvokeAI` and related suites).
Do I even need it (it seems to have been dropped)?
Can I just comment it out in `rocr` dependencies?

### Operating System

OS: NAME="Linux Mint" VERSION="22.1 (Xia)" UBUNTU_CODENAME="noble"

### CPU

CPU:  model name	: AMD Ryzen 9 5950X 16-Core Processor

### GPU

GPU:   Name:                    AMD Ryzen 9 5950X 16-Core Processor   Marketing Name:          AMD Ryzen 9 5950X 16-Core Processor   Name:                    gfx1102                               Marketing Name:          AMD Radeon™ RX 7600 XT                  Name:                    amdgcn-amd-amdhsa--gfx1102         

### ROCm Version

ROCm 5.7

### ROCm Component

_No response_

### Steps to Reproduce

I am following instructions [here](https://github.com/ROCm/ROCm?tab=readme-ov-file#build-rocm-from-source) and I'm using the `Docker` method.
Apparently problem is `aqlprofile` is supported only for older Ubuntu releases (I see just v20.04 and v22.04 on repo).
```
mcon@ikea:~/ROCm$ export ROCM_VERSION=5.7.2
mcon@ikea:~/ROCm$ repo sync
Fetching: 100% (64/64), done in 0.853s
info: A new version of repo is available
warning: repo is not tracking a remote branch, so it will not receive updates
info: Restarting repo with latest version
Checking out: 100% (63/63), done in 3.127s
repo sync has finished successfully.
mcon@ikea:~/ROCm$ docker pull rocm/rocm-build-ubuntu-24.04:6.3
6.3: Pulling from rocm/rocm-build-ubuntu-24.04
de44b265507a: Pull complete 
d70eae50cadc: Pull complete 
5f1f94851a67: Pull complete 
03fa6a4a986c: Pull complete 
2d76206028dc: Pull complete 
f3cb47b6e45f: Pull complete 
98fd60208a5a: Pull complete 
Digest: sha256:b9b8b84a8c5f5d083e9da50e3cfc231dd35e5a061cc3137031719802f2e92b02
Status: Downloaded newer image for rocm/rocm-build-ubuntu-24.04:6.3
docker.io/rocm/rocm-build-ubuntu-24.04:6.3
mcon@ikea:~/ROCm$ docker run -ti \
    -e ROCM_VERSION=${ROCM_VERSION} \
    -e CCACHE_DIR=$HOME/.ccache \
    -e CCACHE_ENABLED=true \
    -e DOCK_WORK_FOLD=/src \
    -w /src \
    -v $PWD:/src \
    -v /etc/passwd:/etc/passwd \
    -v /etc/shadow:/etc/shadow \
    -v ${HOME}/.ccache:${HOME}/.ccache \
    -u $(id -u):$(id -g) \
    rocm/rocm-build-ubuntu-24.04:6.3 bash
mcon@6afbab97987b:/src$ export GPU_ARCHS="gfx1100,gfx1102"
mcon@6afbab97987b:/src$ make -f ROCm/tools/rocm-build/ROCm.mk -j ${NPROC:-$(nproc)} all
OUT_DIR=/src/out/ubuntu-24.04/24.04
ROCM_INSTALL_PATH=/opt/rocm-5.7.2
sudo mkdir -p -m 775 "/opt/rocm-5.7.2" && \
sudo chown -R "1000:1000" "/opt"
0dino!
sudo chown -R "1000:1000" "/home/mcon"
mkdir -p "/src/out/ubuntu-24.04/24.04/logs"
mkdir -p /home/mcon/.ccache
amd_smi_lib started due to
rocm_smi_lib started due to
lightning started due to
hipcc started due to
rocprofiler-register started due to
rocm-cmake started due to
rocprofiler-compute started due to
rocm-core started due to
half started due to rocm-cmake
:              rocm-cmake built
:              rocm-core built
:              half built
:              rocprofiler-compute built
:              hipcc built
:              rocprofiler-register built
:              amd_smi_lib built
:              rocm_smi_lib built
:              lightning built
devicelibs started due to lightning
hipblas-common started due to lightning
miopen-deps started due to lightning hipcc
:              hipblas-common built
:              devicelibs built
rocr started due to lightning rocm_smi_lib devicelibs rocprofiler-register
comgr started due to lightning devicelibs
:              rocr built
openmp_extras started due to lightning devicelibs rocr
aqlprofile started due to rocr
rocminfo started due to rocr
rocm_bandwidth_test started due to rocr
make: *** [ROCm/tools/rocm-build/ROCm.mk:209: /src/out/ubuntu-24.04/24.04/logs/aqlprofile] Error 1
make: *** Waiting for unfinished jobs....
mcon@6afbab97987b:/src$ make -f ROCm/tools/rocm-build/ROCm.mk -j ${NPROC:-$(nproc)} all
OUT_DIR=/src/out/ubuntu-24.04/24.04
ROCM_INSTALL_PATH=/opt/rocm-5.7.2
:              amd_smi_lib built
:              comgr built
:              devicelibs built
:              half built
:              hipblas-common built
:              hipcc built
:              lightning built
:              miopen-deps built
opencl_on_rocclr started due to rocr comgr
dbgapi started due to rocr comgr
aqlprofile started due to rocr
hip_on_rocclr started due to rocr comgr hipcc rocprofiler-register
:              openmp_extras built
:              rocm-cmake built
:              rocm-core built
:              rocm_bandwidth_test built
:              rocm_smi_lib built
:              rocminfo built
:              rocprofiler-compute built
:              rocprofiler-register built
:              rocr built
rpp started due to half lightning hipcc openmp_extras
make: *** [ROCm/tools/rocm-build/ROCm.mk:209: /src/out/ubuntu-24.04/24.04/logs/aqlprofile] Error 1
make: *** Waiting for unfinished jobs....
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

on Docker container I have:
```
mcon@6afbab97987b:/src/out/ubuntu-24.04/24.04/logs$ /opt/rocm-5.7.2/bin/rocminfo --support
ROCk module version 6.10.5 is loaded
Unable to open /dev/kfd read-write: No such file or directory
Failed to get user name to check for video group membership
```
while on host I have:
```
mcon@ikea:~$ /opt/rocm/bin/rocminfo --support
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
  Name:                    AMD Ryzen 9 5950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 5950X 16-Core Processor
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
  Max Clock Freq. (MHz):   3400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32781080(0x1f43318) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32781080(0x1f43318) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32781080(0x1f43318) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32781080(0x1f43318) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1102                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon™ RX 7600 XT           
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
  Max Clock Freq. (MHz):   2493                               
  BDFID:                   11520                              
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
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
  Packet Processor uCode:: 412                                
  SDMA engine uCode::      21                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
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

_No response_