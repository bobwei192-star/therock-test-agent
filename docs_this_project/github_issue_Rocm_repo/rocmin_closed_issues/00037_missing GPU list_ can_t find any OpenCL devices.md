# missing GPU list, can't find any OpenCL devices

- **Issue #:** 37
- **State:** closed
- **Created:** 2016-10-15T16:07:29Z
- **Updated:** 2016-10-18T04:38:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/37

Good Day! Please help solved problem 
Build platform AMD 16 GPU
Now test RocM with 1 card
use 2 software  Ethereum (ETHMINER) and Claymore's AMD 
all software not see any card, normally works with FGLRX 15.12 (not ROCm)
How to tell the program where the list of devices.
THANKS

```
uname -a
Linux KFD 4.4.0-kfd-compute-rocm-rel-1.2-31 #1 SMP Fri Jul 22 06:06:24 CDT 2016 x86_64 x86_64 x86_64 GNU/Linux
```

```
dmesg | grep kfd
[    0.000000] Linux version 4.4.0-kfd-compute-rocm-rel-1.2-31 (jenkins@sm15k-37) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.1) ) #1 SMP Fri Jul 22 06:06:24 CDT 2016
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.4.0-kfd-compute-rocm-rel-1.2-31 root=/dev/mapper/KFD--vg-root ro
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.4.0-kfd-compute-rocm-rel-1.2-31 root=/dev/mapper/KFD--vg-root ro
[    1.078764] usb usb1: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 ehci_hcd
[    1.243041] usb usb2: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 ehci_hcd
[    1.438467] usb usb3: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 xhci-hcd
[    1.641858] usb usb4: Manufacturer: Linux 4.4.0-kfd-compute-rocm-rel-1.2-31 xhci-hcd
[   12.097085] CPU: 4 PID: 476 Comm: systemd-udevd Not tainted 4.4.0-kfd-compute-rocm-rel-1.2-31 #1
[   12.149212] amdkfd: PeerDirect interface was not detected
[   12.149215] kfd kfd: Initialized module
[   22.757640] kfd kfd: Allocated 3944480 bytes on gart for device(1002:67b1)
[   22.757788] kfd kfd: added device (1002:67b1)
```

```
 lspci | grep -i VGA
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii PRO [Radeon R9 290] (rev 80)
```

```
lsmod | grep amd
amdkfd                184320  1
amd_iommu_v2           20480  1 amdkfd
amdgpu               1449984  1
ttm                    94208  1 amdgpu
drm_kms_helper        139264  1 amdgpu
drm                   356352  4 ttm,drm_kms_helper,amdgpu
i2c_algo_bit           16384  2 igb,amdgpu
```

``` /opt/rocm/bin/rocm-smi -a
# ===================   ROCm System Management Interface   ===================
# GPU[0]          : GPU ID: 0x67b1
# 
# GPU[0]          : Temperature: 41.0c
# 
# GPU[0]          : PowerPlay not enabled - Cannot display clocks
# 
# GPU[0]          : Fan Level: 51 (20.0)%
# 
# GPU[0]          : Current PowerPlay Level: auto
# 
# GPU[0]          : Current OverDrive value: 0%
# 
# GPU[0]          : PowerPlay not enabled - Cannot display clocks

===================          End of ROCm SMI Log         ===================

```
```

**clinfo**
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 1.2 AMD-APP (1445.5)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices cl_amd_hsa

  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_CPU
  Vendor ID:                                     1002h
  Board name:
  Max compute units:                             10
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           1024
  Preferred vector width char:                   16
  Preferred vector width short:                  8
  Preferred vector width int:                    4
  Preferred vector width long:                   2
  Preferred vector width float:                  8
  Preferred vector width double:                 4
  Native vector width char:                      16
  Native vector width short:                     8
  Native vector width int:                       4
  Native vector width long:                      2
  Native vector width float:                     8
  Native vector width double:                    4
  Max clock frequency:                           2175Mhz
  Address bits:                                  64
  Max memory allocation:                         8406649856
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            8192
  Max image 2D height:                           8192
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    16
  Max size of kernel argument:                   4096
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    32768
  Global memory size:                            33626599424
  Constant buffer size:                          65536
  Max number of constant args:                   8
  Local memory type:                             Global
  Local memory size:                             32768
  Kernel Preferred work group size multiple:     1
  Error correction support:                      0
  Unified memory for Host and Device:            1
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:
    Execute OpenCL kernels:                      Yes
    Execute native function:                     Yes
  Queue properties:
    Out-of-Order:                                No
    Profiling :                                  Yes
  Platform ID:                                   0x00007fc553302de0
  Name:                                          Intel(R) Xeon(R) CPU E5-2663 v3 @ 2.80GHz
  Vendor:                                        GenuineIntel
  Device OpenCL C version:                       OpenCL C 1.2
  Driver version:                                1445.5 (sse2,avx)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2 AMD-APP (1445.5)
  Extensions:                                    cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_ext_device_fission cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_spir cl_amd_svm cl_khr_gl_event

```
```

./vector_copy
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is Hawaii.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
Passed validation.
Freeing kernel argument memory buffer succeeded.
Destroying the signal succeeded.
Destroying the executable succeeded.
Destroying the code object succeeded.
Destroying the queue succeeded.
Freeing in argument memory buffer succeeded.
Freeing out argument memory buffer succeeded.
Shutting down the runtime succeeded.

```
```
