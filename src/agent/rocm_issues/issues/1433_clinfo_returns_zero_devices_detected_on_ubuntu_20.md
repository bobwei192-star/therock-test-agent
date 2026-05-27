# clinfo returns zero devices detected on ubuntu 20

> **Issue #1433**
> **状态**: closed
> **创建时间**: 2021-03-30T01:38:19Z
> **更新时间**: 2023-04-26T08:03:59Z
> **关闭时间**: 2021-03-30T05:52:57Z
> **作者**: mvlp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1433

## 描述

I followed the installation guide and everything apparently went smoothly. However, the clinfo command reports that the GPU was not found. My configuration is as follows: 

- OS: Ubuntu 20.04.2 LTS
- Kernel: Linux 5.8.0-48-generic
- Package: rocm-dkms Version: 4.1.0.40100-26
- Hardware info:
-[0000:00]-+-00.0  Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers
           +-02.0  Intel Corporation UHD Graphics 620
           +-08.0  Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model
           +-14.0  Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller
           +-14.2  Intel Corporation Sunrise Point-LP Thermal subsystem
           +-16.0  Intel Corporation Sunrise Point-LP CSME HECI 1
           +-17.0  Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode]
           +-1c.0-[02]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon 540/540X/550/550X / RX 540X/550/550X]
           +-1c.4-[03]----00.0  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-1d.0-[04]--
           +-1d.2-[05]----00.0  Realtek Semiconductor Co., Ltd. RTL8822BE 802.11a/b/g/n/ac WiFi adapter
           +-1d.3-[06]----00.0  O2 Micro, Inc. SD/MMC Card Reader Controller
           +-1f.0  Intel Corporation Sunrise Point LPC Controller/eSPI Controller
           +-1f.2  Intel Corporation Sunrise Point-LP PMC
           +-1f.3  Intel Corporation Sunrise Point-LP HD Audio
           \-1f.4  Intel Corporation Sunrise Point-LP SMBus

```
clinfo:
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3241.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```

```
rocminfo:
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
  Name:                    Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
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
  Max Clock Freq. (MHz):   4000                               
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
      Size:                    7913504(0x78c020) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    7913504(0x78c020) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*** Done ***
```

---

## 评论 (6 条)

### 评论 #1 — amartincolby (2021-03-30T05:05:03Z)

I encountered the exact same problem. I don't know what exactly happened, whether it was terminal permissions or whatnot, but if you run those commands as `sudo`, they should return the correct response. Try rebooting your system again after successful installation to see if the two commands function as expected.

---

### 评论 #2 — ROCmSupport (2021-03-30T05:52:57Z)

Thanks @mvlp for reaching out.
We are not officially supporting "Lexa PRO" and so things might break.
Request you to follow our hardware support section in our documentation @ [https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support](url)
Thank you.

---

### 评论 #3 — mvlp (2021-03-30T13:27:40Z)

@amartincolby , including 'sudo' command generates the same output.

@ROCmSupport, can you suggest a non official workaround?



---

### 评论 #4 — avimanyu786 (2021-06-09T10:12:54Z)

Hi @mvlp ,

I think you can fix it by installing the `mesa-opencl-icd` package:

```
sudo apt install mesa-opencl-icd
```
I'd suggest you also double check whether you are running ROCm's own `clinfo` rather than the clinfo package provided by Ubuntu's package manager(apt). To do that you can directly run `/opt/rocm/opencl/bin/clinfo` on a terminal and later make an alias via `.bashrc`. To avoid any future confusions, I have uninstalled the Ubuntu clinfo package.




---

### 评论 #5 — avimanyu786 (2021-06-09T18:18:18Z)

Further investigated this. The command is referring to the mesa version(`mesa.icd`) located at `/etc/OpenCL/vendors/`. That isn't supposed to happen. I've done a clean install of ROCm 4.2. https://github.com/RadeonOpenCompute/ROCm/issues/511 seems to be a good reference to narrow out a solution.
> Hi @mvlp ,
> 
> I think you can fix it by installing the `mesa-opencl-icd` package:
> 
> ```
> sudo apt install mesa-opencl-icd
> ```
> 
> I'd suggest you also double check whether you are running ROCm's own `clinfo` rather than the clinfo package provided by Ubuntu's package manager(apt). To do that you can directly run `/opt/rocm/opencl/bin/clinfo` on a terminal and later make an alias via `.bashrc`. To avoid any future confusions, I have uninstalled the Ubuntu clinfo package.



---

### 评论 #6 — sparky-corona (2023-04-26T08:03:28Z)

Hello, today I had the same issue, but after a sleep and awake cycle.


Before the sleep everthing was detected and worked well as you can see here.

`clinfo`
`Number of platforms                               1`
 `Platform Name                                   NVIDIA CUDA`
  `Platform Vendor                                 NVIDIA Corporation`
  `Platform Version                                OpenCL 3.0 CUDA 12.0.151`
  `Platform Profile                                FULL_PROFILE`
  `Platform Extensions                             cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_fp64 cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts cl_nv_create_buffer cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_device_uuid cl_khr_pci_bus_info cl_khr_external_semaphore cl_khr_external_memory cl_khr_external_semaphore_opaque_fd cl_khr_external_memory_opaque_fd`
  `Platform Host timer resolution           0ns`
  `Platform Extensions function suffix             NV`

  `Platform Name                                   NVIDIA CUDA`
`Number of devices                                 1`
  `Device Name                                     NVIDIA GeForce RTX 2070`
  `Device Vendor                                   NVIDIA Corporation`
  `Device Vendor ID                                0x10de`
 `Device Version                                  OpenCL 3.0 CUDA`
  `Driver Version                                  525.105.17`
  `Device OpenCL C Version                         OpenCL C 1.2 `
  `Device Type                                     GPU`
  `Device Topology (NV)                            PCI-E, 07:00.0`
  `Device Profile                                  FULL_PROFILE`
  `Device Available                                Yes`
  `Compiler Available                              Yes`
  `Linker Available                                Yes`
  `Max compute units                               36`
  `Max clock frequency                             1455MHz`
  `Compute Capability (NV)                         7.5`
  `Device Partition                                (core)`
   `Max number of sub-devices                     1`
    `Supported partition types                     None`
    `Supported affinity domains                    (n/a)`
  `Max work item dimensions                        3`
  `Max work item sizes                             1024x1024x64`
  `Max work group size                             1024`
  `Preferred work group size multiple              32`
  `Warp size (NV)                                  32`
  `Max sub-groups per work group                   0`
  `Preferred / native vector sizes`                 
    `char                                                 1 / 1`
   `short                                                1 / 1`       
    `int                                                  1 / 1`       
    `long                                                 1 / 1`       
   `half                                                 0 / 0        (n/a)`
    `float                                                1 / 1`
    `double                                               1 / 1        (cl_khr_fp64)`
  `Half-precision Floating-point support           (n/a)`
  `Single-precision Floating-point support         (core)`
    `Denormals                                     Yes`
    `Infinity and NANs                             Yes`
    `Round to nearest                              Yes`
    `Round to zero                                 Yes`
    `Round to infinity                             Yes`
    `IEEE754-2008 fused multiply-add               Yes`
    `Support is emulated in software               No`
    `Correctly-rounded divide and sqrt operations  Yes`
  `Double-precision Floating-point support         (cl_khr_fp64)`
    `Denormals                                     Yes`
    `Infinity and NANs                             Yes`
    `Round to nearest                              Yes`
    `Round to zero                                 Yes`
    `Round to infinity                             Yes`
    `IEEE754-2008 fused multiply-add               Yes`
    `Support is emulated in software               No`
  `Address bits                                    64, Little-Endian`
  `Global memory size                              8353153024 (7.779GiB)`
  `Error Correction support                        No`
  `Max memory allocation                           2088288256 (1.945GiB)`
  `Unified memory for Host and Device              No`
  `Integrated memory (NV)                          No`
  `Shared Virtual Memory (SVM) capabilities        (core)`
    `Coarse-grained buffer sharing                 Yes`
    `Fine-grained buffer sharing                   No`
    `Fine-grained system sharing                   No`
    `Atomics                                       No`
  `Minimum alignment for any data type             128 bytes`
  `Alignment of base address                       4096 bits (512 bytes)`
  `Preferred alignment for atomics`        
    `SVM                                           0 bytes`
    `Global                                        0 bytes`
    `Local                                         0 bytes`
  `Max size for global variable                    0`
  `Preferred total size of global vars             0`
  `Global Memory cache type                        Read/Write`
  `Global Memory cache size                        1179648 (1.125MiB)`
  `Global Memory cache line size                   128 bytes`
  `Image support                                   Yes`
    `Max number of samplers per kernel             32`
    `Max size for 1D images from buffer            268435456 pixels`
    `Max 1D or 2D image array size                 2048 images`
    `Max 2D image size                             32768x32768 pixels`
    `Max 3D image size                             16384x16384x16384 pixels`
    `Max number of read image args                 256`
    `Max number of write image args                32`
    `Max number of read/write image args           0`
  `Max number of pipe args                         0`
  `Max active pipe reservations                    0`
  `Max pipe packet size                            0`
  `Local memory type                               Local`
  `Local memory size                               49152 (48KiB)`
  `Registers per block (NV)                        65536`
  `Max number of constant args                     9`
  `Max constant buffer size                        65536 (64KiB)`
  `Max size of kernel argument                     4352 (4.25KiB)`
  `Queue properties (on host)`                      
    `Out-of-order execution                        Yes`
    `Profiling                                     Yes`
  `Queue properties (on device)`                    
    `Out-of-order execution                        No`
    `Profiling                                     No`
    `Preferred size                                0`
    `Max size                                      0`
  `Max queues on device                            0`
  `Max events on device                            0`
  `Prefer user sync for interop                    No`
  `Profiling timer resolution                      1000ns`
  `Execution capabilities`                          
    `Run OpenCL kernels                            Yes`
    `Run native kernels                            No`
    `Sub-group independent forward progress        No`
    `Kernel execution timeout (NV)                 Yes`
  `Concurrent copy and kernel execution (NV)       Yes`
    `Number of async copy engines                  3`
    `IL version                                    (n/a)`
  `printf() buffer size                            1048576 (1024KiB)`
  `Built-in kernels                                (n/a)`
  `Device Extensions                               cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_fp64 cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts cl_nv_create_buffer cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_device_uuid cl_khr_pci_bus_info cl_khr_external_semaphore cl_khr_external_memory cl_khr_external_semaphore_opaque_fd cl_khr_external_memory_opaque_fd`

`NULL platform behavior`
  `clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  NVIDIA CUDA`
  `clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [NV]`
  `clCreateContext(NULL, ...) [default]            Success [NV]`
  `clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No platform`
  `clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform`
  `clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No platform`
  `clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform`
  `clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  Invalid device type for platform`
  `clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No platform`

`ICD loader properties`
  `ICD loader Name                                 OpenCL ICD Loader`
  `ICD loader Vendor                               OCL Icd free software`
  `ICD loader Version                              2.2.11`
  `ICD loader Profile                              OpenCL 2.1`
	`NOTE:	your OpenCL library only supports OpenCL 2.1,
		but some installed platforms support OpenCL 3.0.
		Programs using 3.0 features may crash
		or behave unexpectedly`


After the sleep clinfo returned

`Number of platforms  0`


I already tried unloading and reloading UVM driver, which fixes the problem temporarily until the next sleep when I start my script manually in terminal as the output of dmesg shows.


`[266182.483989] nvidia-uvm: Unloaded the UVM driver.`
`[266182.535330] nvidia_uvm: module uses symbols from proprietary module nvidia, inheriting taint.`
`[266182.538176] nvidia-uvm: Loaded the UVM driver, major device number 507.`


My script is just simply:

`sudo rmmod nvidia_uvm`
`sudo modprobe nvidia_uvm`


I also tried to add the script to the sleep routine in /lib/systemd/nvidia ....which did NOT work.


Any suggestions?

---
