# Will the following setup work with ROCm for DL?

- **Issue #:** 652
- **State:** closed
- **Created:** 2018-12-28T05:55:01Z
- **Updated:** 2019-02-08T23:42:27Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/652

Hi there,

I've run a Cryptonight mining farm for a while now but with the current markets it's barely profitable anymore.
I've always had interest in ML/DL and was wondering if my system could also be used for Deep Learning.

I gathered lots of data on various stuff the past couple years which is mostly lightweight in nature (i.e. just numbers, mostly 5-10 data points describing "1 event", mostly scientific or economic) but massive in amounts (several GB).

My system consists of the following:
- 12x RX 550 Lexa Pro (polaris 12) GPUs with 2GB VRAM each
- 4 GB DDR4 System RAM
- INTEL Celeron G3930 "Kaby Lake", 2x 2.9GHz, Socket 1151
- Biostar TB-250 BTC Pro Motherboard (PCIe Gen can be chosen from 1-3), currently running all GPUs with Gen 2
- All GPUs are conntected through cheap non-label risers & USB cables into 1x PCIe slots.
- Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller

I have 200+ of those systems 
"Rigs"/Machines are grouped in 36-"rig"/machine groups (432 RX 550 per group) and connected to a 1 Gbit switch, that 1 Gbit switch is connected to other switches & a router with 10 Gbit interfaces.

Things that I can upgrade easily:
CPU
System RAM

 I know those are very low compute, low end GPUs with bad PCIe interfaces and low VRAM. Anyhow, I was wondering if one could build a Deep Learning system from it. And I was wondering If I could even profit from such a system, as it uses so many GPUs (i.e. instead of 1 Vega GPU I have 8 RX 550 GPUs), as in, does it provide the possibility to have more hidden layers given that I have low complexity light data?

So instead of turning off the machines & waiting for better times I'd much rather let the system do something potentially useful.

Kind Regards,
MoneroCrusher

some system outputs:

```
root@A12:/# lspci
00:00.0 Host bridge: Intel Corporation Device 590f (rev 06)
00:01.0 PCI bridge: Intel Corporation Sky Lake PCIe Controller (x16) (rev 06)
00:02.0 VGA compatible controller: Intel Corporation Device 5902 (rev 04)
00:08.0 System peripheral: Intel Corporation Sky Lake Gaussian Mixture Model
00:14.0 USB controller: Intel Corporation Device a2af
00:16.0 Communication controller: Intel Corporation Device a2ba
00:17.0 SATA controller: Intel Corporation Device a282
00:1b.0 PCI bridge: Intel Corporation Device a2eb (rev f0)
00:1b.5 PCI bridge: Intel Corporation Device a2ec (rev f0)
00:1b.6 PCI bridge: Intel Corporation Device a2ed (rev f0)
00:1b.7 PCI bridge: Intel Corporation Device a2ee (rev f0)
00:1c.0 PCI bridge: Intel Corporation Device a294 (rev f0)
00:1c.5 PCI bridge: Intel Corporation Device a295 (rev f0)
00:1c.6 PCI bridge: Intel Corporation Device a296 (rev f0)
00:1c.7 PCI bridge: Intel Corporation Device a297 (rev f0)
00:1d.0 PCI bridge: Intel Corporation Device a298 (rev f0)
00:1d.1 PCI bridge: Intel Corporation Device a299 (rev f0)
00:1d.2 PCI bridge: Intel Corporation Device a29a (rev f0)
00:1d.3 PCI bridge: Intel Corporation Device a29b (rev f0)
00:1f.0 ISA bridge: Intel Corporation Device a2c8
00:1f.2 Memory controller: Intel Corporation Device a2a1
00:1f.3 Audio device: Intel Corporation Device a2f0
00:1f.4 SMBus: Intel Corporation Device a2a3
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
02:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
05:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
06:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit                                                           Ethernet Controller (rev 15)
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
07:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
08:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
08:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
09:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
09:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
0a:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
0a:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
0b:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
0c:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
0c:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 699f (rev c7)
0d:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0
--------------------------------------------------------------------------------------------------------------
Clinfo:
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP (2264.10)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 13
  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 01:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 02:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 03:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 04:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 05:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 07:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 08:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 09:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 0a:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 0b:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 0c:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     gfx804
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         AMD Radeon Graphics
  Device Topology (AMD)                           PCI-E, 0d:00.0
  Max compute units                               8
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1150MHz
  Graphics IP (AMD)                               8.0
  Device Partition                                (core)
    Max number of sub-devices                     8
    Supported partition types                     none specified
  Max work item dimensions                        3
  Max work item sizes                             256x256x256
  Max work group size                             256
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              2076475392 (1.934GiB)
  Global free memory (AMD)                        2009244 (1.916GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           1365808128 (1.272GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 bytes
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max constant buffer size                        1365808128 (1.272GiB)
  Max number of constant args                     8
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    SPIR versions                                 1.2
  printf() buffer size                            1048576 (1024KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Name                                     Intel(R) Celeron(R) CPU G3930 @ 2.90GHz
  Device Vendor                                   GenuineIntel
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2264.10)
  Driver Version                                  2264.10 (sse2)
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     CPU
  Device Profile                                  FULL_PROFILE
  Device Board Name (AMD)                         
  Device Topology (AMD)                           (n/a)
  Max compute units                               2
  Max clock frequency                             2900MHz
  Device Partition                                (core, cl_ext_device_fission)
    Max number of sub-devices                     2
    Supported partition types                     equally, by counts, by affinity domain
    Supported affinity domains                    L3 cache, L2 cache, L1 cache, next partitionable
    Supported partition types (ext)               equally, by counts, by affinity domain
    Supported affinity domains (ext)              L3 cache, L2 cache, L1 cache, next fissionable
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             1024
  Preferred work group size multiple              1
  Preferred / native vector sizes                 
    char                                                16 / 16      
    short                                                8 / 8       
    int                                                  4 / 4       
    long                                                 2 / 2       
    half                                                 2 / 2        (n/a)
    float                                                4 / 4       
    double                                               2 / 2        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Address bits                                    64, Little-Endian
  Global memory size                              4063256576 (3.784GiB)
  Error Correction support                        No
  Max memory allocation                           2147483648 (2GiB)
  Unified memory for Host and Device              Yes
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        32768
  Global Memory cache line                        64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             8192x8192 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                64
  Local memory type                               Global
  Local memory size                               32768 (32KiB)
  Max constant buffer size                        65536 (64KiB)
  Max number of constant args                     8
  Max size of kernel argument                     4096 (4KiB)
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1545975399908612637ns (Fri Dec 28 06:36:39 2018)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            Yes
    SPIR versions                                 1.2
  printf() buffer size                            65536 (64KiB)
  Built-in kernels                                
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_ext_device_fission cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_spir cl_khr_gl_event 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No platform
--------------------------------------------------------------------------------------------------------------
Link Speed idle:
root@A12:/# cat /sys/class/hwmon/hwmon2/device/current_link_speed
2.5 GT/s
Link Speed under 100% load:
cat /sys/class/hwmon/hwmon2/device/current_link_speed
5 GT/s
--------------------------------------------------------------------------------------------------------------
root@A12:/pciutils# ./lspci -vvv | grep Atomic
                         AtomicOpsCap: Routing- 32bit+ 64bit+ 128bitCAS+
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn- EgressBlck-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit- 64bit- 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
                         AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
                         AtomicOpsCtl: ReqEn-
```