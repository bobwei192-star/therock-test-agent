# FuryX, dual CPU, Ubuntu 16.04, ROCm 1.2, can't get GPU agent.

> **Issue #21**
> **状态**: closed
> **创建时间**: 2016-08-17T10:17:17Z
> **更新时间**: 2017-09-18T22:50:36Z
> **关闭时间**: 2016-10-22T10:59:44Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/21

## 描述

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


---

## 评论 (10 条)

### 评论 #1 — preda (2016-08-17T10:25:49Z)

rocm-smi sees the GPU:

/opt/rocm/bin/rocm-smi -a

# ===================   ROCm System Management Interface   ===================

# GPU[0]      : GPU ID: 0x7300

# 

# GPU[0]      : Temperature: 32.0c

# 

GPU[0]      : GPU Clock Level: 0 (300Mhz)

# GPU[0]      : GPU Memory Clock Level: 0 (500Mhz)

# 

# GPU[0]      : Fan Level: 35 (13.73)%

# 

# GPU[0]      : Current PowerPlay Level: auto

# 

# GPU[0]      : Current OverDrive value: 0%

# 

GPU[0]      : Supported GPU clock frequencies on GPU0
GPU[0]      : 0: 300Mhz *
GPU[0]      : 1: 512Mhz 
GPU[0]      : 2: 724Mhz 
GPU[0]      : 3: 892Mhz 
GPU[0]      : 4: 944Mhz 
GPU[0]      : 5: 984Mhz 
GPU[0]      : 6: 1018Mhz 
GPU[0]      : 7: 1050Mhz 
GPU[0]      : 
GPU[0]      : Supported GPU Memory clock frequencies on GPU0
GPU[0]      : 0: 500Mhz *

# GPU[0]      : 

===================          End of ROCm SMI Log         ===================


---

### 评论 #2 — gstoner (2016-08-17T13:45:55Z)

The fact you can see opencl means you have two drivers loaded.

Did you remove your  Crimson driver first.

Greg

Get Outlook for iOShttps://aka.ms/o0ukef

On Wed, Aug 17, 2016 at 5:18 AM -0500, "Mihai Preda" <notifications@github.com<mailto:notifications@github.com>> wrote:

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
HCC clang version 3.5.0 (based on HCC 0.10.16313-d90738a-10704f4 LLVM 3.5.0svn)
Target: x86_64-unknown-linux-gnu
Thread model: posix

uname -a
Linux big 4.4.0-kfd-compute-rocm-rel-1.2-31 #1https://github.com/RadeonOpenCompute/ROCm/pull/1 SMP Fri Jul 22 06:06:24 CDT 2016 x86_64 x86_64 x86_64 GNU/Linux

I suspect this may have something to do with my dual-CPU? maybe hsa_iterate_agents() stops early at two agents before reaching the GPU?

Here is output from clinfo:

Number of platforms: 1
Platform Profile: FULL_PROFILE
Platform Version: OpenCL 2.0 AMD-APP (2117.7)
Platform Name: AMD Accelerated Parallel Processing
Platform Vendor: Advanced Micro Devices, Inc.
Platform Extensions: cl_khr_icd cl_amd_event_callback cl_amd_offline_devices

Platform Name: AMD Accelerated Parallel Processing
Number of devices: 2
Device Type: CL_DEVICE_TYPE_GPU
Vendor ID: 1002h
Board name:

Device Topology: PCI[ B#129, D#0, F#0 ]
Max compute units: 14
Max work items dimensions: 3
Max work items[0]: 256
Max work items[1]: 256
Max work items[2]: 256
Max work group size: 256
Preferred vector width char: 4
Preferred vector width short: 2
Preferred vector width int: 1
Preferred vector width long: 1
Preferred vector width float: 1
Preferred vector width double: 1
Native vector width char: 4
Native vector width short: 2
Native vector width int: 1
Native vector width long: 1
Native vector width float: 1
Native vector width double: 1
Max clock frequency: 555Mhz
Address bits: 64
Max memory allocation: 2699563008
Image support: Yes
Max number of images read arguments: 128
Max number of images write arguments: 8
Max image 2D width: 16384
Max image 2D height: 16384
Max image 3D width: 2048
Max image 3D height: 2048
Max image 3D depth: 2048
Max samplers within kernel: 16
Max size of kernel argument: 1024
Alignment (bits) of base address: 2048
Minimum alignment (bytes) for any datatype: 128
Single precision floating point capability
Denorms: No
Quiet NaNs: Yes
Round to nearest even: Yes
Round to zero: Yes
Round to +ve and infinity: Yes
IEEE754-2008 fused multiply-add: Yes
Cache type: Read/Write
Cache line size: 64
Cache size: 16384
Global memory size: 3784101888
Constant buffer size: 65536
Max number of constant args: 8
Local memory type: Scratchpad
Local memory size: 32768
Max pipe arguments: 0
Max pipe active reservations: 0
Max pipe packet size: 0
Max global variable size: 0
Max global variable preferred total size: 0
Max read/write image args: 0
Max on device events: 0
Queue on device max size: 0
Max on device queues: 0
Queue on device preferred size: 0
SVM capabilities:

Coarse grain buffer: No
Fine grain buffer: No
Fine grain system: No
Atomics: No
Preferred platform atomic alignment: 0
Preferred global atomic alignment: 0
Preferred local atomic alignment: 0
Kernel Preferred work group size multiple: 64
Error correction support: 0
Unified memory for Host and Device: 0
Profiling timer resolution: 1
Device endianess: Little
Available: Yes
Compiler available: Yes
Execution capabilities:

Execute OpenCL kernels: Yes
Execute native function: No
Queue on Host properties:

Out-of-Order: No
Profiling : Yes
Queue on Device properties:

Out-of-Order: No
Profiling : No
Platform ID: 0x7f9a2e4868f8
Name: Fiji
Vendor: Advanced Micro Devices, Inc.
Device OpenCL C version: OpenCL C 1.2
Driver version: 2117.7 (VM)
Profile: FULL_PROFILE
Version: OpenCL 1.2 AMD-APP (2117.7)
Extensions: cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event

Device Type: CL_DEVICE_TYPE_CPU
Vendor ID: 1002h
Board name:

Max compute units: 32
Max work items dimensions: 3
Max work items[0]: 1024
Max work items[1]: 1024
Max work items[2]: 1024
Max work group size: 1024
Preferred vector width char: 16
Preferred vector width short: 8
Preferred vector width int: 4
Preferred vector width long: 2
Preferred vector width float: 8
Preferred vector width double: 4
Native vector width char: 16
Native vector width short: 8
Native vector width int: 4
Native vector width long: 2
Native vector width float: 8
Native vector width double: 4
Max clock frequency: 2356Mhz
Address bits: 64
Max memory allocation: 33766751232
Image support: Yes
Max number of images read arguments: 128
Max number of images write arguments: 64
Max image 2D width: 8192
Max image 2D height: 8192
Max image 3D width: 2048
Max image 3D height: 2048
Max image 3D depth: 2048
Max samplers within kernel: 16
Max size of kernel argument: 4096
Alignment (bits) of base address: 1024
Minimum alignment (bytes) for any datatype: 128
Single precision floating point capability
Denorms: Yes
Quiet NaNs: Yes
Round to nearest even: Yes
Round to zero: Yes
Round to +ve and infinity: Yes
IEEE754-2008 fused multiply-add: Yes
Cache type: Read/Write
Cache line size: 64
Cache size: 32768
Global memory size: 135067004928
Constant buffer size: 65536
Max number of constant args: 8
Local memory type: Global
Local memory size: 32768
Max pipe arguments: 16
Max pipe active reservations: 16
Max pipe packet size: 3701980160
Max global variable size: 1879048192
Max global variable preferred total size: 1879048192
Max read/write image args: 64
Max on device events: 0
Queue on device max size: 0
Max on device queues: 0
Queue on device preferred size: 0
SVM capabilities:

Coarse grain buffer: No
Fine grain buffer: No
Fine grain system: No
Atomics: No
Preferred platform atomic alignment: 0
Preferred global atomic alignment: 0
Preferred local atomic alignment: 0
Kernel Preferred work group size multiple: 1
Error correction support: 0
Unified memory for Host and Device: 1
Profiling timer resolution: 1
Device endianess: Little
Available: Yes
Compiler available: Yes
Execution capabilities:

Execute OpenCL kernels: Yes
Execute native function: Yes
Queue on Host properties:

Out-of-Order: No
Profiling : Yes
Queue on Device properties:

Out-of-Order: No
Profiling : No
Platform ID: 0x7f9a2e4868f8
Name: Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz
Vendor: GenuineIntel
Device OpenCL C version: OpenCL C 1.2
Driver version: 2117.7 (sse2,avx)
Profile: FULL_PROFILE
Version: OpenCL 1.2 AMD-APP (2117.7)
Extensions: cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_ext_device_fission cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_spir cl_khr_gl_event

## 

You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/21, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DucYhjYaHTo9DOoyP6u4tXzifrrqCks5qgt-ugaJpZM4JmTHM.


---

### 评论 #3 — ghost (2016-08-17T18:23:58Z)

This seems like the kernel driver hasn't been loaded correctly.

Check your dmesg (or post it here), to make sure amdkfd loaded correctly.

My initial suspicion is that you have amdgpuor amdkfd blacklisted under /etc/modprobe.d/ 


---

### 评论 #4 — preda (2016-08-17T23:03:55Z)

I attach full output of dmesg and lsmod
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/423790/dmesg.txt)
[lsmod.txt](https://github.com/RadeonOpenCompute/ROCm/files/423791/lsmod.txt)

To me it seems both amdgpu and amdkfd are loaded. I never installed Catalyst. I have installed amdgpu-pro:

dpkg -l amdgpu-pro :
ii  amdgpu-pro                              16.30.3-306809

cat /etc/modprobe.d/amdgpu-blacklist-radeon.conf 
blacklist radeon
blacklist fglrx

lsmod | grep amd :

amdkfd                184320  0
amd_iommu_v2           20480  1 amdkfd
amdgpu               1929216  6
ttm                    94208  1 amdgpu
drm_kms_helper        139264  1 amdgpu
drm                   356352  9 ttm,drm_kms_helper,amdgpu
i2c_algo_bit           16384  2 igb,amdgpu

dmesg | grep kfd

[    0.000000] Linux version 4.4.0-kfd-compute-rocm-rel-1.2-31 (jenkins@sm15k-37) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.1) ) #1 SMP Fri Jul 22 06:06:24 CDT 2016
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-kfd-compute-rocm-rel-1.2-31 root=UUID=18949a47-531f-41c3-bed4-7b50fec4b441 ro quiet splash vt.handoff=7
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.4.0-kfd-compute-rocm-rel-1.2-31 root=UUID=18949a47-531f-41c3-bed4-7b50fec4b441 ro quiet splash vt.handoff=7
[   17.451272] usb usb1: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 ehci_hcd
[   17.467278] usb usb2: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 ehci_hcd
[   17.468963] usb usb3: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 xhci-hcd
[   17.471205] usb usb4: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 xhci-hcd
[   18.673415] amdkfd: PeerDirect interface was not detected
[   18.673419] kfd kfd: Initialized module

dmesg | grep amdgpu

[   18.661860] amdgpu: module verification failed: signature and/or required key missing - tainting kernel
[   18.665334] [drm] amdgpu kernel modesetting enabled.
[   18.673731] fb: switching to amdgpudrmfb from EFI VGA
[   18.674265] amdgpu 0000:81:00.0: VRAM: 4096M 0x0000000000000000 - 0x00000000FFFFFFFF (4096M used)
[   18.674268] amdgpu 0000:81:00.0: GTT: 4096M 0x0000000100000000 - 0x00000001FFFFFFFF
[   18.674358] [drm] amdgpu: 4096M of VRAM memory ready
[   18.674359] [drm] amdgpu: 4096M of GTT memory ready.
[   18.675632] amdgpu 0000:81:00.0: amdgpu: using MSI.
[   18.675652] [drm] amdgpu: irq initialized.
[   18.681868] amdgpu: powerplay initialized
[   18.682143] amdgpu 0000:81:00.0: fence driver on ring 0 use gpu addr 0x0000000100000008, cpu addr 0xffff8820347f9008
[   18.682170] amdgpu 0000:81:00.0: fence driver on ring 1 use gpu addr 0x000000010000001c, cpu addr 0xffff8820347f901c
[   18.682193] amdgpu 0000:81:00.0: fence driver on ring 2 use gpu addr 0x0000000100000030, cpu addr 0xffff8820347f9030
[   18.682216] amdgpu 0000:81:00.0: fence driver on ring 3 use gpu addr 0x0000000100000044, cpu addr 0xffff8820347f9044
[   18.682238] amdgpu 0000:81:00.0: fence driver on ring 4 use gpu addr 0x0000000100000058, cpu addr 0xffff8820347f9058
[   18.682261] amdgpu 0000:81:00.0: fence driver on ring 5 use gpu addr 0x000000010000006c, cpu addr 0xffff8820347f906c
[   18.682283] amdgpu 0000:81:00.0: fence driver on ring 6 use gpu addr 0x0000000100000080, cpu addr 0xffff8820347f9080
[   18.682309] amdgpu 0000:81:00.0: fence driver on ring 7 use gpu addr 0x0000000100000094, cpu addr 0xffff8820347f9094
[   18.682331] amdgpu 0000:81:00.0: fence driver on ring 8 use gpu addr 0x00000001000000a8, cpu addr 0xffff8820347f90a8
[   18.682383] amdgpu 0000:81:00.0: fence driver on ring 9 use gpu addr 0x00000001000000bc, cpu addr 0xffff8820347f90bc
[   18.682408] amdgpu 0000:81:00.0: fence driver on ring 10 use gpu addr 0x00000001000000d0, cpu addr 0xffff8820347f90d0
[   18.682681] amdgpu 0000:81:00.0: fence driver on ring 11 use gpu addr 0x000000000087f8d0, cpu addr 0xffffc9000d43d8d0
[   18.682804] amdgpu 0000:81:00.0: fence driver on ring 12 use gpu addr 0x00000001000000f8, cpu addr 0xffff8820347f90f8
[   18.682828] amdgpu 0000:81:00.0: fence driver on ring 13 use gpu addr 0x000000010000010c, cpu addr 0xffff8820347f910c
[   18.899386] fbcon: amdgpudrmfb (fb0) is primary device
[   18.915541] amdgpu 0000:81:00.0: fb0: amdgpudrmfb frame buffer device


---

### 评论 #5 — preda (2016-08-20T12:55:35Z)

Let me reframe the situation: is it normal/expected that hsa_iterate_agents() reports _two_ CPU agents?


---

### 评论 #6 — mbevand (2016-10-21T17:42:14Z)

@preda you need to uninstall amdgpu-pro. When @gstoner referred to "crimson", he meant amdgpu-pro. And you need to uninstall it because it is not compatible with ROCm.

(It is my understanding that the rebranding from "Catalyst" to "Crimson" coincides with replacing fglrx with amdgpu-pro... And when people say "don't install Catalyst/fglrx" it also means "don't install Crimson/amdgpu-pro". But now if you asked me what's the difference between the "amdgpu.ko" shipped by Crimson and the "amdgpu.ko" shipped by ROCm, I don't know. The whole situation is frankly very confusing.)


---

### 评论 #7 — preda (2016-10-22T10:59:44Z)

OK, it seems my problem was caused by interaction with amdgpu-pro, closing with uninstalling amdgpu-pro as the solution.


---

### 评论 #8 — bhaskar2khaneja (2017-09-17T21:36:18Z)

I was using an AMD Radeon R9 Nano for graphics and NVIDIA Tesla K40 for compiling CUDA code and when I installed ROCm, I had the exact same issue. After I removed amdgpu-pro driver and re-booted, my machine got stuck in a login loop. I then switched out NVIDIA Tesla K40 with NVIDIA Titan and made it so my machine was now using NVIDIA Titan for graphics and also contained AMD Radeon R9 Nano, and when I reinstalled ROCm and ran './vector_copy' I still got the "getting a gpu agent failed" output. Anybody have any ideas?  

I'm running Ubuntu 16.04.3 LTS and this is the output of uname -a:

`Linux titan 4.11.0-kfd-compute-rocm-rel-1.6-148 #1 SMP Wed Aug 23 12:00:35 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux`

---

### 评论 #9 — gstoner (2017-09-17T23:25:06Z)

It simple you can not have the ROCm base driver installed and AMDGPUpro driver installed at the same time.  You need to remove the AMDGPUpro driver,  before installing the ROCm driver and follow these instructions ( https://rocm.github.io/ROCmInstall.html)explicitly.  Also today you cannot Install ROCm Userland Components on AMDGPUpro based driver 16.30 or newer.    

 It not confusing, this is an independent project that was built to support Server Based GPU  Computing.  

@bhaskar2khaneja  You have a different issue around setting up ROCm and NVIDIA driver upon the same system. 

---

### 评论 #10 — bhaskar2khaneja (2017-09-18T22:34:07Z)

@gstoner Thanks for your prompt response. Might you have any suggestions on how to go about identifying it? 

Would it be crucial to fix this before proceeding with using HIP? I am essentially trying to convert a CUDA library to HIP C++ and have it compile on an AMD GPU.

---
