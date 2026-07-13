# FuryX, dual CPU, Ubuntu 16.04, ROCm 1.2, can't get GPU agent.

- **Issue #:** 21
- **State:** closed
- **Created:** 2016-08-17T10:17:17Z
- **Updated:** 2017-09-18T22:50:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/21

I installed ROCm 1.2 according to the instructions. Compiling vector_copy went OK, but running it outputs:

Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent failed.

I looked into it a bit, and hsa_iterate_agents() reports only 2 CPU agents. (I'm on a dual- Xeon E5-2630v3 system). No GPU agent reported, although I do have a FuryX running correctly.

I can use the FuryX through OpenCL.

I also tried hcc with saxpy.cpp:
./saxpy
There is no device can be used to do the computation

(by the way, there's an error in that error message as well).

hcc --version:
HCC clang version 3.5.0  (based on HCC 0.10.16313-d90738a-10704f4 LLVM 3.5.0svn)
Target: x86_64-unknown-linux-gnu
Thread model: posix

uname -a
Linux big 4.4.0-kfd-compute-rocm-rel-1.2-31 #1 SMP Fri Jul 22 06:06:24 CDT 2016 x86_64 x86_64 x86_64 GNU/Linux

I suspect this may have something to do with my dual-CPU? maybe hsa_iterate_agents() stops early at two agents before reaching the GPU?

Here is output from clinfo:

Number of platforms:                 1
  Platform Profile:              FULL_PROFILE
  Platform Version:              OpenCL 2.0 AMD-APP (2117.7)
  Platform Name:                 AMD Accelerated Parallel Processing
  Platform Vendor:               Advanced Micro Devices, Inc.
  Platform Extensions:               cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 

  Platform Name:                 AMD Accelerated Parallel Processing
Number of devices:               2
  Device Type:                   CL_DEVICE_TYPE_GPU
  Vendor ID:                     1002h
  Board name:  
  Device Topology:               PCI[ B#129, D#0, F#0 ]
  Max compute units:                 14
  Max work items dimensions:             3
    Max work items[0]:               256
    Max work items[1]:               256
    Max work items[2]:               256
  Max work group size:               256
  Preferred vector width char:           4
  Preferred vector width short:          2
  Preferred vector width int:            1
  Preferred vector width long:           1
  Preferred vector width float:          1
  Preferred vector width double:         1
  Native vector width char:          4
  Native vector width short:             2
  Native vector width int:           1
  Native vector width long:          1
  Native vector width float:             1
  Native vector width double:            1
  Max clock frequency:               555Mhz
  Address bits:                  64
  Max memory allocation:             2699563008
  Image support:                 Yes
  Max number of images read arguments:       128
  Max number of images write arguments:      8
  Max image 2D width:                16384
  Max image 2D height:               16384
  Max image 3D width:                2048
  Max image 3D height:               2048
  Max image 3D depth:                2048
  Max samplers within kernel:            16
  Max size of kernel argument:           1024
  Alignment (bits) of base address:      2048
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                     No
    Quiet NaNs:                  Yes
    Round to nearest even:           Yes
    Round to zero:               Yes
    Round to +ve and infinity:           Yes
    IEEE754-2008 fused multiply-add:         Yes
  Cache type:                    Read/Write
  Cache line size:               64
  Cache size:                    16384
  Global memory size:                3784101888
  Constant buffer size:              65536
  Max number of constant args:           8
  Local memory type:                 Scratchpad
  Local memory size:                 32768
  Max pipe arguments:                0
  Max pipe active reservations:          0
  Max pipe packet size:              0
  Max global variable size:          0
  Max global variable preferred total size:  0
  Max read/write image args:             0
  Max on device events:              0
  Queue on device max size:          0
  Max on device queues:              0
  Queue on device preferred size:        0
  SVM capabilities:  
    Coarse grain buffer:             No
    Fine grain buffer:               No
    Fine grain system:               No
    Atomics:                     No
  Preferred platform atomic alignment:       0
  Preferred global atomic alignment:         0
  Preferred local atomic alignment:      0
  Kernel Preferred work group size multiple:     64
  Error correction support:          0
  Unified memory for Host and Device:        0
  Profiling timer resolution:            1
  Device endianess:              Little
  Available:                     Yes
  Compiler available:                Yes
  Execution capabilities:  
    Execute OpenCL kernels:          Yes
    Execute native function:             No
  Queue on Host properties:  
    Out-of-Order:                No
    Profiling :                  Yes
  Queue on Device properties:  
    Out-of-Order:                No
    Profiling :                  No
  Platform ID:                   0x7f9a2e4868f8
  Name:                      Fiji
  Vendor:                    Advanced Micro Devices, Inc.
  Device OpenCL C version:           OpenCL C 1.2 
  Driver version:                2117.7 (VM)
  Profile:                   FULL_PROFILE
  Version:                   OpenCL 1.2 AMD-APP (2117.7)
  Extensions:                    cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event 

  Device Type:                   CL_DEVICE_TYPE_CPU
  Vendor ID:                     1002h
  Board name:  
  Max compute units:                 32
  Max work items dimensions:             3
    Max work items[0]:               1024
    Max work items[1]:               1024
    Max work items[2]:               1024
  Max work group size:               1024
  Preferred vector width char:           16
  Preferred vector width short:          8
  Preferred vector width int:            4
  Preferred vector width long:           2
  Preferred vector width float:          8
  Preferred vector width double:         4
  Native vector width char:          16
  Native vector width short:             8
  Native vector width int:           4
  Native vector width long:          2
  Native vector width float:             8
  Native vector width double:            4
  Max clock frequency:               2356Mhz
  Address bits:                  64
  Max memory allocation:             33766751232
  Image support:                 Yes
  Max number of images read arguments:       128
  Max number of images write arguments:      64
  Max image 2D width:                8192
  Max image 2D height:               8192
  Max image 3D width:                2048
  Max image 3D height:               2048
  Max image 3D depth:                2048
  Max samplers within kernel:            16
  Max size of kernel argument:           4096
  Alignment (bits) of base address:      1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                     Yes
    Quiet NaNs:                  Yes
    Round to nearest even:           Yes
    Round to zero:               Yes
    Round to +ve and infinity:           Yes
    IEEE754-2008 fused multiply-add:         Yes
  Cache type:                    Read/Write
  Cache line size:               64
  Cache size:                    32768
  Global memory size:                135067004928
  Constant buffer size:              65536
  Max number of constant args:           8
  Local memory type:                 Global
  Local memory size:                 32768
  Max pipe arguments:                16
  Max pipe active reservations:          16
  Max pipe packet size:              3701980160
  Max global variable size:          1879048192
  Max global variable preferred total size:  1879048192
  Max read/write image args:             64
  Max on device events:              0
  Queue on device max size:          0
  Max on device queues:              0
  Queue on device preferred size:        0
  SVM capabilities:  
    Coarse grain buffer:             No
    Fine grain buffer:               No
    Fine grain system:               No
    Atomics:                     No
  Preferred platform atomic alignment:       0
  Preferred global atomic alignment:         0
  Preferred local atomic alignment:      0
  Kernel Preferred work group size multiple:     1
  Error correction support:          0
  Unified memory for Host and Device:        1
  Profiling timer resolution:            1
  Device endianess:              Little
  Available:                     Yes
  Compiler available:                Yes
  Execution capabilities:  
    Execute OpenCL kernels:          Yes
    Execute native function:             Yes
  Queue on Host properties:  
    Out-of-Order:                No
    Profiling :                  Yes
  Queue on Device properties:  
    Out-of-Order:                No
    Profiling :                  No
  Platform ID:                   0x7f9a2e4868f8
  Name:                      Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz
  Vendor:                    GenuineIntel
  Device OpenCL C version:           OpenCL C 1.2 
  Driver version:                2117.7 (sse2,avx)
  Profile:                   FULL_PROFILE
  Version:                   OpenCL 1.2 AMD-APP (2117.7)
  Extensions:                    cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_ext_device_fission cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_spir cl_khr_gl_event
