# Warning: Use of non-host signal in host signal wait API (version 4.1.0)

> **Issue #1436**
> **状态**: closed
> **创建时间**: 2021-04-01T20:29:50Z
> **更新时间**: 2023-07-24T10:45:35Z
> **关闭时间**: 2021-05-07T12:20:52Z
> **作者**: jar
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1436

## 描述

I've built the ROCm 4.1.0 toolchain from source similar to #1426, but on Ubuntu 20.04 with AMD Threadripper 1950x and AMD Radeon Vega 64 Frontier Edition.  I get multiple warnings like this when running simple hipified code:

```Warning: (!g_use_interrupt_wait || isIPC()) && "Use of non-host signal in host signal wait API." in virtual hsa_signal_value_t rocr::core::BusyWaitSignal::WaitRelaxed(hsa_signal_condition_t, hsa_signal_value_t, uint64_t, hsa_wait_state_t), <<private builds directory>>/ROCm/ROCR-Runtime/src/core/runtime/default_signal.cpp:87```

The code apparently executes correctly, but do you know the significance of these warnings?  I've looked at the source for the signals warning, but it's not clear if these have performance implications or can just be safely ignored.

---

## 评论 (13 条)

### 评论 #1 — ROCmSupport (2021-04-05T07:58:52Z)

Hi @jar 
Thanks for reaching out.
Can you please share the exact steps to reproduce the problem.
Also share OS, Kernel, rocminfo, clinfo outputs.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-04-09T09:49:04Z)

Hi @jar 
Please respond asap so that we will work and update with resolution.
Thank you.

---

### 评论 #3 — jar (2021-04-12T01:36:57Z)

```
$ uname -a
Linux proxima 5.4.0-54-generic #60-Ubuntu SMP Fri Nov 6 10:37:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```
```
$ rocminfo 
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
  Name:                    AMD Ryzen Threadripper 1950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper 1950X 16-Core Processor
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
  Max Clock Freq. (MHz):   3400                               
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
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32805484(0x1f4926c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32805484(0x1f4926c) KB             
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
  Uuid:                    GPU-0213f2d6875a1104               
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
  BDFID:                   17152                              
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
```
```
$ /opt/rocm-4.0.0/opencl/bin/clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3212.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XTX [Radeon Vega Frontier Edition]
  Device Topology:				 PCI[ B#67, D#0, F#0 ]
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
ERROR: clBuildProgram(-11)
```
The last error here is a bit concerning. Do I need OpenCL?  I get build errors when building 4.1.x ROCm-OpenCL-Runtime because it appears some headers weren't copied or properly referenced from ROCclr.

Is there an updated build script for the entire ROCm stack?  It would be helpful rather than referring to multiple build instructions, possibly dated, across several source repositories.


---

### 评论 #4 — ROCmSupport (2021-04-12T07:26:14Z)

Hi @jar 
We are working on ROCm build instructions and request to follow #1188.

Request you to share stepbystep process for reproducing the error for better understanding.
Thank you.

---

### 评论 #5 — jar (2021-04-12T12:42:42Z)

I cut code from the square.cu example:
```
#include <stdio.h>
#include <cuda_runtime.h>

#define CHECK(cmd) \
{\
    cudaError_t error  = cmd;\
    if (error != cudaSuccess) { \
        fprintf(stderr, "error: '%s'(%d) at %s:%d\n", cudaGetErrorString(error), error,__FILE__, __LINE__); \
        exit(EXIT_FAILURE);\
	  }\
}


int main(int argc, char *argv[])
{
    float *A_d;
    float *A_h;
    size_t N = 1000000;
    size_t Nbytes = N * sizeof(float);

    cudaDeviceProp props;
    CHECK(cudaGetDeviceProperties(&props, 0/*deviceID*/));
    printf ("info: running on device %s\n", props.name);
    A_h = (float*)malloc(Nbytes);
    CHECK(A_h == 0 ? cudaErrorMemoryAllocation : cudaSuccess );
    for (size_t i=0; i<N; i++) 
    {
        A_h[i] = 1.618f + i; 
    }

    CHECK(cudaMalloc(&A_d, Nbytes));
    CHECK(cudaMemcpy(A_d, A_h, Nbytes, cudaMemcpyHostToDevice));
}
```
Compile:
```
/opt/rocm/hip/bin/hipify-perl square.cu > square.cpp
/opt/rocm/hip/bin/hipcc  square.cpp -o square.out
```
Run:
```
$ ./square.out 
info: running on device Vega 10 XTX [Radeon Vega Frontier Edition]
Warning: (!g_use_interrupt_wait || isIPC()) && "Use of non-host signal in host signal wait API." in virtual hsa_signal_value_t rocr::core::BusyWaitSignal::WaitRelaxed(hsa_signal_condition_t, hsa_signal_value_t, uint64_t, hsa_wait_state_t), /home/jar/packages/ROCm/ROCR-Runtime/src/core/runtime/default_signal.cpp:87
Warning: (!g_use_interrupt_wait || isIPC()) && "Use of non-host signal in host signal wait API." in virtual hsa_signal_value_t rocr::core::BusyWaitSignal::WaitRelaxed(hsa_signal_condition_t, hsa_signal_value_t, uint64_t, hsa_wait_state_t), /home/jar/packages/ROCm/ROCR-Runtime/src/core/runtime/default_signal.cpp:87
```
Warnings are related to the `[cuda|hip]Memcpy` calls.

---

### 评论 #6 — ROCmSupport (2021-04-16T10:26:47Z)

Thanks @jar 
I executed it on Vega20 + ROCm 4.1 --> Issue is NOT observed.

taccuser@taccuser-All-Series:~$ ./square.out
**info: running on device Vega 20 [Radeon VII]**

Let me check on Vega10 and share an update.
Thank you.


---

### 评论 #7 — ROCmSupport (2021-04-16T10:32:12Z)

Hi @jar 
I checked it on Vega10 also and issue is NOT observed with ROCm 4.1-26 + 20.04.2 with kernel 5.8.0-48.

**taccuser@taccuser-X399-DESIGNARE-EX:~$ ./square.out
info: running on device Vega 10 XL/XT [Radeon RX Vega 56/64]**
taccuser@taccuser-X399-DESIGNARE-EX:~$

Thank you.

---

### 评论 #8 — jar (2021-04-19T20:32:54Z)

I'm running kernel 5.4.0-54-generic and amdgpu 20.45.  Does this matter?  I don't understand how AMD drivers and kernel relate to the ROCm stack.  It looks like the 20.45 drivers don't support the 5.4 kernel, so I'll have to upgrade to 20.50 and 5.8?  It's still not clear that is the issue.  Without spending a hours digging through the ROCR-Runtime source, is it possible to say whether this warning is indicative of other problems or can it be safely ignored?

---

### 评论 #9 — ROCmSupport (2021-04-20T05:23:30Z)

Hi @jar 
I recommend to install plain rocm (which will have amdgpu connected to it anyways) and try.
Looks like as you have amdgpu already installed, there might be some clash.
I do not have amdgpu installed in my machine and installed plain/clean rocm-dkms which does not throw any warnings/errors.
Thank you.

---

### 评论 #10 — jar (2021-04-20T13:53:07Z)

I have rock-dkms rock-dkms-firmware installed. The amdgpu-dkms is removed.  There are other \*amdgpu\* and \*amdgpu-pro\* packages.  It's not clear to me how any of these packages are related, which are required, and which may cause conflicts.  Is it possible to run both a graphics stack and compute stack?

```
$ dpkg -l | grep -i gpu
ii  amdgpu-core                                     20.45-1164792                                       all          Core meta package for unified amdgpu driver.
rc  amdgpu-dkms                                     1:5.6.20.906300-1164792                             all          amdgpu driver in DKMS format.
ii  amdgpu-lib                                      20.45-1164792                                       amd64        Meta package to install amdgpu userspace components.
ii  amdgpu-lib32                                    20.45-1164792                                       amd64        Meta package to support i386 runtime on amd64 architecture
ii  amdgpu-pin                                      20.45-1164792                                       all          Meta package to pin a specific amdgpu driver version.
ii  amdgpu-pro-core                                 20.45-1164792                                       all          Core meta package for Pro components of the unified amdgpu driver.
ii  clinfo-amdgpu-pro                               20.45-1164792                                       amd64        AMD OpenCL info utility
ii  comgr-amdgpu-pro:amd64                          1.7.0-1164792                                       amd64        Development files for ROCm ROCm Code Object Manager
ii  gst-omx-amdgpu                                  1.0.0.1-1164792                                     amd64        GStreamer OpenMAX plugins
ii  hip-rocr-amdgpu-pro                             20.45-1164792                                       amd64        ROCr HIP Clang Runtime
ii  hsa-runtime-rocr-amdgpu:amd64                   1.2.0-1164792                                       amd64        The user-mode API interfaces used to interact with the Boltzmann
ii  hsakmt-roct-amdgpu:amd64                        1.0.9-1164792                                       amd64        The user-mode API interfaces used to interact with the Boltzmann
ii  intel-gpu-tools                                 1.25-2                                              amd64        tools for debugging the Intel graphics driver
ii  libdrm-amdgpu-amdgpu1:amd64                     1:2.4.100-1164792                                   amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm-amdgpu-amdgpu1:i386                      1:2.4.100-1164792                                   i386         Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm-amdgpu-common                            1.0.0-1164792                                       all          List of AMD/ATI cards' device IDs, revision IDs and marketing names
ii  libdrm-amdgpu-radeon1:amd64                     1:2.4.100-1164792                                   amd64        Userspace interface to radeon-specific kernel DRM services -- runtime
ii  libdrm-amdgpu-radeon1:i386                      1:2.4.100-1164792                                   i386         Userspace interface to radeon-specific kernel DRM services -- runtime
ii  libdrm-amdgpu1:amd64                            2.4.102-1ubuntu1~20.04.1                            amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm-amdgpu1:i386                             2.4.102-1ubuntu1~20.04.1                            i386         Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm2-amdgpu:amd64                            1:2.4.100-1164792                                   amd64        Userspace interface to kernel DRM services -- runtime
ii  libdrm2-amdgpu:i386                             1:2.4.100-1164792                                   i386         Userspace interface to kernel DRM services -- runtime
ii  libegl1-amdgpu-mesa:amd64                       1:20.1.6-1164792                                    amd64        free implementation of the EGL API -- runtime
ii  libegl1-amdgpu-mesa:i386                        1:20.1.6-1164792                                    i386         free implementation of the EGL API -- runtime
ii  libegl1-amdgpu-mesa-drivers:amd64               1:20.1.6-1164792                                    amd64        free implementation of the EGL API -- hardware drivers
ii  libegl1-amdgpu-mesa-drivers:i386                1:20.1.6-1164792                                    i386         free implementation of the EGL API -- hardware drivers
ii  libgbm1-amdgpu:amd64                            1:20.1.6-1164792                                    amd64        generic buffer management API -- runtime
ii  libgbm1-amdgpu:i386                             1:20.1.6-1164792                                    i386         generic buffer management API -- runtime
ii  libgl1-amdgpu-mesa-dri:amd64                    1:20.1.6-1164792                                    amd64        free implementation of the OpenGL API -- DRI modules
ii  libgl1-amdgpu-mesa-dri:i386                     1:20.1.6-1164792                                    i386         free implementation of the OpenGL API -- DRI modules
ii  libgl1-amdgpu-mesa-glx:amd64                    1:20.1.6-1164792                                    amd64        free implementation of the OpenGL API -- GLX runtime
ii  libgl1-amdgpu-mesa-glx:i386                     1:20.1.6-1164792                                    i386         free implementation of the OpenGL API -- GLX runtime
ii  libglapi-amdgpu-mesa:amd64                      1:20.1.6-1164792                                    amd64        free implementation of the GL API -- shared library
ii  libglapi-amdgpu-mesa:i386                       1:20.1.6-1164792                                    i386         free implementation of the GL API -- shared library
ii  libgles1-amdgpu-mesa:amd64                      1:20.1.6-1164792                                    amd64        free implementation of the OpenGL|ES 1.x API -- runtime
ii  libgles1-amdgpu-mesa:i386                       1:20.1.6-1164792                                    i386         free implementation of the OpenGL|ES 1.x API -- runtime
ii  libgles2-amdgpu-mesa:amd64                      1:20.1.6-1164792                                    amd64        free implementation of the OpenGL|ES 2.x API -- runtime
ii  libgles2-amdgpu-mesa:i386                       1:20.1.6-1164792                                    i386         free implementation of the OpenGL|ES 2.x API -- runtime
ii  libllvm10.0-amdgpu:amd64                        1:10.0-1164792                                      amd64        Modular compiler and toolchain technologies, runtime library
ii  libllvm10.0-amdgpu:i386                         1:10.0-1164792                                      i386         Modular compiler and toolchain technologies, runtime library
ii  libosdgpu3.4.0:amd64                            3.4.0-6build1                                       amd64        high performance subdivision surface (subdiv) library - GPU runtime
ii  libosmesa6-amdgpu:amd64                         1:20.1.6-1164792                                    amd64        Mesa Off-screen rendering extension
ii  libosmesa6-amdgpu:i386                          1:20.1.6-1164792                                    i386         Mesa Off-screen rendering extension
ii  libxatracker2-amdgpu:amd64                      1:20.1.6-1164792                                    amd64        X acceleration library -- runtime
ii  libxatracker2-amdgpu:i386                       1:20.1.6-1164792                                    i386         X acceleration library -- runtime
ii  llvm-amdgpu                                     1:10.0-1164792                                      amd64        Low-Level Virtual Machine (LLVM)
ii  llvm-amdgpu-10.0                                1:10.0-1164792                                      amd64        Modular compiler and toolchain technologies
ii  llvm-amdgpu-10.0-dev                            1:10.0-1164792                                      amd64        Modular compiler and toolchain technologies, libraries and headers
ii  llvm-amdgpu-10.0-runtime                        1:10.0-1164792                                      amd64        Modular compiler and toolchain technologies, IR interpreter
ii  llvm-amdgpu-runtime                             1:10.0-1164792                                      amd64        Low-Level Virtual Machine (LLVM), bytecode interpreter
ii  mesa-amdgpu-omx-drivers:amd64                   1:20.1.6-1164792                                    amd64        Mesa OpenMAX video drivers
ii  mesa-amdgpu-va-drivers:amd64                    1:20.1.6-1164792                                    amd64        Mesa VA-API video acceleration drivers
ii  mesa-amdgpu-va-drivers:i386                     1:20.1.6-1164792                                    i386         Mesa VA-API video acceleration drivers
ii  mesa-amdgpu-vdpau-drivers:amd64                 1:20.1.6-1164792                                    amd64        Mesa VDPAU video acceleration drivers
ii  mesa-amdgpu-vdpau-drivers:i386                  1:20.1.6-1164792                                    i386         Mesa VDPAU video acceleration drivers
ii  ocl-icd-libopencl1-amdgpu-pro:amd64             20.45-1164792                                       amd64        AMD OpenCL ICD Loader library
ii  opencl-rocr-amdgpu-pro:amd64                    20.45-1164792                                       amd64        ROCr OpenCL Runtime
ii  rock-dkms                                       1:4.1-26                                            all          amdgpu driver in DKMS format.
ii  rock-dkms-firmware                              1:4.1-26                                            all          firmware blobs used by amdgpu driver in DKMS format
rc  rocm-amdgpu-pro-icd:amd64                       17.50-552542                                        amd64        non-free AMD OpenCL ICD Loaders
ii  rocm-dbgapi                                     0.42.0.40100-26                                     amd64        Library to provide AMD GPU debugger API
ii  switcheroo-control                              2.1-1                                               amd64        D-Bus service to check the availability of dual-GPU
ii  xserver-xorg-amdgpu-video-amdgpu                1:19.1.0-1164792                                    amd64        X.Org X server -- AMD/ATI Radeon display driver
ii  xserver-xorg-video-amdgpu                       19.1.0-1                                            amd64        X.Org X server -- AMDGPU display driver
```

---

### 评论 #11 — ROCmSupport (2021-04-22T05:43:58Z)

Hi @jar 
Its not recommended to use both graphics stack and compute stack in a single machine.
So my suggestion is to follow below steps.

If you wish to install rocm, do the below.
1. Prepare a clean system(Uninstall amdgpu-pro drivers, uninstall old rocm etc.,.), should be clean. Reboot for every uninstall.
2. On a clean system, map the latest ROCm 4.1 repository and install it using "sudo apt install rocm-dkms".
3. Reboot the machine
4. Now do the steps you wish to try.
Thank you.


---

### 评论 #12 — ROCmSupport (2021-05-07T12:20:52Z)

Hi @jar 
Hope this issue is fixed and no more observed now.
We are not able to reproduce with 5.4 and 5.8 kernels on Vega10 and Vega20.
Feel free to file a new issue, if any, for the solutions.
Thank you.


---

### 评论 #13 — tucnak (2023-07-24T10:45:35Z)

What is the nature of this error? I've started seeing

```Warning: (!g_use_interrupt_wait || isIPC()) && "Use of non-host signal in host signal wait API." in virtual hsa_signal_value_t rocr::core::BusyWaitSignal::WaitRelaxed(hsa_signal_condition_t, hsa_signal_value_t, uint64_t, hsa_wait_state_t), ./src/core/runtime/default_signal.cpp:87```

On latest rocm & mainline kernel.

---
