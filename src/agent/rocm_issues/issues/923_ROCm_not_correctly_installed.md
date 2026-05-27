# ROCm not correctly installed

> **Issue #923**
> **状态**: closed
> **创建时间**: 2019-10-26T13:18:01Z
> **更新时间**: 2023-12-18T17:16:08Z
> **关闭时间**: 2023-12-18T17:16:08Z
> **作者**: creekbed
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/923

## 描述

Hi all. First time posting. I'm new to Linux so I'm endeavoring to tackle the hail of problems I'm getting. I'm aware I may be or have been doing something wrong, or extremely dumb, so that's why I'm here. I wanted to see if ROCm was successfully installed (below you'll see what I did to do so) by running the following commands expecting my GPU to be listed, but I get the following:

```
root@slack:~# /opt/rocm/bin/rocminfo 
ROCk module is loaded
root is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
`
and (I think there's no problem with this one, although at the very bottom there's something wrong):
root@slack:~# /opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:				 2
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.2 pocl 1.3 None+Asserts, LLVM 8.0.1, SLEEF, DISTRO, POCL_DEBUG
  Platform Name:				 Portable Computing Language
  Platform Vendor:				 The pocl project
  Platform Extensions:				 cl_khr_icd
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 Portable Computing Language
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_CPU
  Vendor ID:					 6c636f70h
  Max compute units:				 2
  Max work items dimensions:			 3
    Max work items[0]:				 4096
    Max work items[1]:				 4096
    Max work items[2]:				 4096
  Max work group size:				 4096
  Preferred vector width char:			 16
  Preferred vector width short:			 16
  Preferred vector width int:			 8
  Preferred vector width long:			 4
  Preferred vector width float:			 8
  Preferred vector width double:		 4
  Native vector width char:			 16
  Native vector width short:			 16
  Native vector width int:			 8
  Native vector width long:			 4
  Native vector width float:			 8
  Native vector width double:			 4
  Max clock frequency:				 1350Mhz
  Address bits:					 64
  Max memory allocation:			 1073741824
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 128
  Max image 2D width:				 8192
  Max image 2D height:				 8192
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 16
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 No
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 1048576
  Global memory size:				 2675807232
  Constant buffer size:				 524288
  Max number of constant args:			 8
  Local memory type:				 Global
  Local memory size:				 524288
  Kernel Preferred work group size multiple:	 8
  Error correction support:			 0
  Unified memory for Host and Device:		 1
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 Yes
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Platform ID:					 0x7f119e1a3020
  Name:						 pthread-AMD E1-6010 APU with AMD Radeon R2 Graphics
  Vendor:					 AuthenticAMD
  Device OpenCL C version:			 OpenCL C 1.2 pocl
  Driver version:				 1.3
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 pocl HSTR: pthread-x86_64-pc-linux-gnu-btver2
  Extensions:					 cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_3d_image_writes cl_khr_fp64 cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

Kernel version:
`root@slack:~# uname -r
5.2.0-kali3-amd64` 

Hoping that I did right and that it will suffice, what I did to install ROCm, since my kernel version is 5.2.0 and AMD’s `rock-dkms` package doesn't offer at the moment a kernel driver supported on kernels above 4.18, I installed the upstream kernel driver by going directly to `rocm-dev`, as explained on https://rocm.github.io/ROCmInstall.html.

What can I do or undo to solve this? I'm aiming to run a program that requires ROCm and for the moment it's performing the same as it was before installing ROCm, which means it's not been properly installed. I don't know what else I need to provide in order for you to know what to do.

Thank you. 

---

## 评论 (9 条)

### 评论 #1 — blitzcaster (2019-10-29T17:24:29Z)

I'm also having this problem using upstream kernel driver.

```
$ rocminfo
ROCk module is loaded
rinaldi is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

```
$ clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)
```

```
$ uname -a
Linux tfdev-fx8120 5.0.0-32-generic #34~18.04.2-Ubuntu SMP Thu Oct 10 10:36:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```

```
$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="18.04.3 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.3 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

This is my current GPU setup.
```
Extended renderer info (GLX_MESA_query_renderer):
    Vendor: X.Org (0x1002)
    Device: AMD Radeon (TM) RX 480 Graphics (POLARIS10, DRM 3.27.0, 5.0.0-32-generic, LLVM 8.0.0) (0x67df)
    Version: 19.0.8
    Accelerated: yes
    Video memory: 8192MB
    Unified memory: no
    Preferred profile: core (0x1)
    Max core profile version: 4.5
    Max compat profile version: 4.5
    Max GLES1 profile version: 1.1
    Max GLES[23] profile version: 3.2
Memory info (GL_ATI_meminfo):
    VBO free memory - total: 7851 MB, largest block: 7851 MB
    VBO free aux. memory - total: 5881 MB, largest block: 5881 MB
    Texture free memory - total: 7851 MB, largest block: 7851 MB
    Texture free aux. memory - total: 5881 MB, largest block: 5881 MB
    Renderbuffer free memory - total: 7851 MB, largest block: 7851 MB
    Renderbuffer free aux. memory - total: 5881 MB, largest block: 5881 MB
Memory info (GL_NVX_gpu_memory_info):
    Dedicated video memory: 8192 MB
    Total available memory: 14133 MB
    Currently available dedicated video memory: 7851 MB
```

### Edit:
After some further reading, this could possibly related to https://github.com/RadeonOpenCompute/rocminfo/issues/27#issuecomment-541129285 since I also have this on dmesg.

```
$ dmesg | grep kfd
[    4.303782] kfd kfd: skipped device 1002:67df, PCI rejects atomics
```

I guess there is not hope for me then, since my CPU and PCIe is not supported. 

```
*-cpu
          description: CPU
          product: AMD FX(tm)-8120 Eight-Core Processor
          vendor: Advanced Micro Devices [AMD]
          physical id: 4
          bus info: cpu@0
          version: AMD FX(tm)-8120 Eight-Core Processor
          serial: To Be Filled By O.E.M.
          slot: CPU 1
          size: 1421MHz
          capacity: 3100MHz
          width: 64 bits
          clock: 200MHz
          capabilities: x86-64 fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 cx16 sse4_1 sse4_2 popcnt aes xsave avx lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs xop skinit wdt fma4 nodeid_msr topoext perfctr_core perfctr_nb cpb hw_pstate ssbd ibpb vmmcall arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold lwp cpufreq
          configuration: cores=8 enabledcores=8 threads=8
*-pci:0
          description: Host bridge
          product: RD9x0/RX980 Host Bridge
          vendor: Advanced Micro Devices, Inc. [AMD/ATI]
          physical id: 100
          bus info: pci@0000:00:00.0
          version: 02
          width: 32 bits
          clock: 33MHz
```
@creekbed do you also have kfd dmesg PCI rejects atomics?

---

### 评论 #2 — creekbed (2019-11-02T22:41:05Z)

@blitzcaster I don't get any output. I guess there was no device skipped so it didn't reject it


---

### 评论 #3 — Mike575 (2019-12-09T01:37:58Z)

I also got it this problem.

```
$ rocminfo
ROCk module is NOT loaded, possibly no GPU devices
firefox is member of video group
hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

```
$:/lib/firmware/amdgpu.back$ uname -a
Linux firefox-X570-AORUS-PRO-WIFI 4.15.0-46-generic #49-Ubuntu SMP Wed Feb 6 09:33:07 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```

```
$:/lib/firmware/amdgpu.back$ lspci | grep VGA
0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 20 (rev c1)

```
```
$:/lib/firmware/amdgpu.back$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-46-generic (buildd@lgw01-amd64-038) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #49-Ubuntu SMP Wed Feb 6 09:33:07 UTC 2019 (Ubuntu 4.15.0-46.49-generic 4.15.18)
[    0.400761] amd_uncore: AMD NB counters detected
[    0.400765] amd_uncore: AMD LLC counters detected
[    0.402476] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    0.418587] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[    3.563436] amd_sched: loading out-of-tree module taints kernel.
[    3.563456] amd_sched: module verification failed: signature and/or required key missing - tainting kernel
[    3.684425] amdgpu: Unknown symbol amd_iommu_bind_pasid (err 0)
[    3.684506] amdgpu: Unknown symbol amd_iommu_set_invalidate_ctx_cb (err 0)
[    3.684555] amdgpu: Unknown symbol amd_iommu_free_device (err 0)
[    3.684727] amdgpu: Unknown symbol amd_iommu_unbind_pasid (err 0)
[    3.684740] amdgpu: Unknown symbol amd_iommu_init_device (err 0)
[    3.684822] amdgpu: Unknown symbol amd_iommu_set_invalid_ppr_cb (err 0)
```

```
$ dmesg | grep kfd
None

```


---

### 评论 #4 — vsrikarunyan (2019-12-26T06:06:03Z)

Yes, I too bumped on this one today

```
(base) vsrikarunyan@d-rigg-evolv:~$ rocminfo
ROCk module is loaded
vsrikarunyan is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.0/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

(base) vsrikarunyan@d-rigg-evolv:~$ clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

(base) vsrikarunyan@d-rigg-evolv:~$ uname -a
Linux d-rigg-evolv.edu 5.0.0-37-generic #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

(base) vsrikarunyan@d-rigg-evolv:~$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="18.04.3 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.3 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

```
(base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep amd
[    0.000000] Linux version 5.0.0-37-generic (buildd@lcy01-amd64-023) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 (Ubuntu 5.0.0-37.40~18.04.1-generic 5.0.21)
[    0.681692] amd_uncore: AMD NB counters detected
[    0.681709] amd_uncore: AMD LLC counters detected
[    0.682511] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    0.682526] perf/amd_iommu: Detected AMD IOMMU #1 (2 banks, 4 counters/bank).
[    2.848560] amdkcl: loading out-of-tree module taints kernel.
[    2.848644] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[    2.974422] [drm] amdgpu kernel modesetting enabled.
[    2.974423] [drm] amdgpu version: 5.2.4
[    2.976338] amdgpu 0000:0b:00.0: enabling device (0000 -> 0003)
[    3.077022] amdgpu 0000:0b:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
[    3.077023] amdgpu 0000:0b:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[    3.077024] amdgpu 0000:0b:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF
[    3.077142] [drm] amdgpu: 16368M of VRAM memory ready
[    3.077144] [drm] amdgpu: 64345M of GTT memory ready.
[    3.093710] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu
[    3.692034] amdgpu 0000:0b:00.0: HDCP: hdcp ta ucode is not available
[    3.692036] amdgpu 0000:0b:00.0: DTM: dtm ta ucode is not available
[    4.101555] amdgpu 0000:0b:00.0: ring gfx uses VM inv eng 0 on hub 0
[    4.101556] amdgpu 0000:0b:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    4.101557] amdgpu 0000:0b:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    4.101558] amdgpu 0000:0b:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[    4.101558] amdgpu 0000:0b:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[    4.101559] amdgpu 0000:0b:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[    4.101560] amdgpu 0000:0b:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[    4.101561] amdgpu 0000:0b:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[    4.101562] amdgpu 0000:0b:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[    4.101563] amdgpu 0000:0b:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[    4.101564] amdgpu 0000:0b:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[    4.101564] amdgpu 0000:0b:00.0: ring page0 uses VM inv eng 1 on hub 1
[    4.101565] amdgpu 0000:0b:00.0: ring sdma1 uses VM inv eng 4 on hub 1
[    4.101566] amdgpu 0000:0b:00.0: ring page1 uses VM inv eng 5 on hub 1
[    4.101566] amdgpu 0000:0b:00.0: ring uvd_0 uses VM inv eng 6 on hub 1
[    4.101567] amdgpu 0000:0b:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
[    4.101568] amdgpu 0000:0b:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
[    4.101568] amdgpu 0000:0b:00.0: ring uvd_1 uses VM inv eng 9 on hub 1
[    4.101569] amdgpu 0000:0b:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1
[    4.101569] amdgpu 0000:0b:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1
[    4.101570] amdgpu 0000:0b:00.0: ring vce0 uses VM inv eng 12 on hub 1
[    4.101571] amdgpu 0000:0b:00.0: ring vce1 uses VM inv eng 13 on hub 1
[    4.101571] amdgpu 0000:0b:00.0: ring vce2 uses VM inv eng 14 on hub 1
[    4.101942] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:0b:00.0 on minor 0
[    4.102039] fb0: switching to amdgpudrmfb from VESA VGA
[    4.105052] amdgpu 0000:43:00.0: No more image in the PCI ROM
[    4.105158] amdgpu 0000:43:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
[    4.105160] amdgpu 0000:43:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[    4.105162] amdgpu 0000:43:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF
[    4.105214] [drm] amdgpu: 16368M of VRAM memory ready
[    4.105217] [drm] amdgpu: 64345M of GTT memory ready.
[    4.108846] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu
[    4.688025] amdgpu 0000:43:00.0: HDCP: hdcp ta ucode is not available
[    4.688027] amdgpu 0000:43:00.0: DTM: dtm ta ucode is not available
[    5.234184] fbcon: amdgpudrmfb (fb0) is primary device
[    5.234268] amdgpu 0000:43:00.0: fb0: amdgpudrmfb frame buffer device
[    5.268120] amdgpu 0000:43:00.0: ring gfx uses VM inv eng 0 on hub 0
[    5.268122] amdgpu 0000:43:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    5.268124] amdgpu 0000:43:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    5.268125] amdgpu 0000:43:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[    5.268126] amdgpu 0000:43:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[    5.268127] amdgpu 0000:43:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[    5.268128] amdgpu 0000:43:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[    5.268129] amdgpu 0000:43:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[    5.268130] amdgpu 0000:43:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[    5.268131] amdgpu 0000:43:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[    5.268132] amdgpu 0000:43:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[    5.268133] amdgpu 0000:43:00.0: ring page0 uses VM inv eng 1 on hub 1
[    5.268134] amdgpu 0000:43:00.0: ring sdma1 uses VM inv eng 4 on hub 1
[    5.268135] amdgpu 0000:43:00.0: ring page1 uses VM inv eng 5 on hub 1
[    5.268136] amdgpu 0000:43:00.0: ring uvd_0 uses VM inv eng 6 on hub 1
[    5.268137] amdgpu 0000:43:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
[    5.268138] amdgpu 0000:43:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
[    5.268139] amdgpu 0000:43:00.0: ring uvd_1 uses VM inv eng 9 on hub 1
[    5.268140] amdgpu 0000:43:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1
[    5.268141] amdgpu 0000:43:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1
[    5.268141] amdgpu 0000:43:00.0: ring vce0 uses VM inv eng 12 on hub 1
[    5.268142] amdgpu 0000:43:00.0: ring vce1 uses VM inv eng 13 on hub 1
[    5.268143] amdgpu 0000:43:00.0: ring vce2 uses VM inv eng 14 on hub 1
[    5.268550] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:43:00.0 on minor 1
[    7.876319] EDAC amd64: Node 0: DRAM ECC disabled.
[    7.876321] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[    7.876325] EDAC amd64: Node 1: DRAM ECC disabled.
[    7.876326] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.

```

```
(base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep VGA
[    0.265649] pci 0000:0b:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none
[    0.265649] pci 0000:43:00.0: vgaarb: setting as boot VGA device
[    0.265649] pci 0000:43:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
[    0.711831] fb0: VESA VGA frame buffer device
[    4.102039] fb0: switching to amdgpudrmfb from VESA VGA

```

```
(base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep kfd
[    4.100422] kfd kfd: Allocated 3969056 bytes on gart
[    4.101409] kfd kfd: added device 1002:66af
[    5.231901] kfd kfd: Allocated 3969056 bytes on gart
[    5.232512] kfd kfd: added device 1002:66af
```

ECC Seems to be enabled on my machine. JFYI, I do have an issue with one of my memory bank, but ROCm v2.9 didn't seem to have had any complaints.

```
(base) vsrikarunyan@d-rigg-evolv:~$ sudo dmidecode --type memory | grep Width
	Total Width: Unknown
	Data Width: Unknown
	Total Width: Unknown
	Data Width: Unknown
	Total Width: Unknown
	Data Width: Unknown
	Total Width: Unknown
	Data Width: Unknown
	Total Width: 64 bits
	Data Width: 64 bits
	Total Width: 64 bits
	Data Width: 64 bits
	Total Width: 64 bits
	Data Width: 64 bits
	Total Width: 64 bits
	Data Width: 64 bits

```

---

### 评论 #5 — Mike575 (2019-12-26T15:49:05Z)

updating linux kernal to 5.0.x can figure out this problem.




------------------&nbsp;原始邮件&nbsp;------------------
发件人: "Venkateshwaralu Srikarunyan"<notifications@github.com&gt;; 
发送时间: 2019年12月26日(星期四) 下午2:06
收件人: "RadeonOpenCompute/ROCm"<ROCm@noreply.github.com&gt;; 
抄送: "赖自成"<575840864@qq.com&gt;; "Comment"<comment@noreply.github.com&gt;; 
主题: Re: [RadeonOpenCompute/ROCm] ROCm not correctly installed (#923)




Yes, I too bumped on this one today
 (base) vsrikarunyan@d-rigg-evolv:~$ rocminfo ROCk module is loaded vsrikarunyan is member of video group hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.0/rocminfo/rocminfo.cc:1102 Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events. (base) vsrikarunyan@d-rigg-evolv:~$ clinfo Number of platforms:				 1   Platform Profile:				 FULL_PROFILE   Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)   Platform Name:				 AMD Accelerated Parallel Processing   Platform Vendor:				 Advanced Micro Devices, Inc.   Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices    Platform Name:				 AMD Accelerated Parallel Processing ERROR: clGetDeviceIDs(-1) (base) vsrikarunyan@d-rigg-evolv:~$ uname -a Linux d-rigg-evolv.edu 5.0.0-37-generic #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux (base) vsrikarunyan@d-rigg-evolv:~$ cat /etc/os-release  NAME="Ubuntu" VERSION="18.04.3 LTS (Bionic Beaver)" ID=ubuntu ID_LIKE=debian PRETTY_NAME="Ubuntu 18.04.3 LTS" VERSION_ID="18.04" HOME_URL="https://www.ubuntu.com/" SUPPORT_URL="https://help.ubuntu.com/" BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/" PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy" VERSION_CODENAME=bionic UBUNTU_CODENAME=bionic  (base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep amd [    0.000000] Linux version 5.0.0-37-generic (buildd@lcy01-amd64-023) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 (Ubuntu 5.0.0-37.40~18.04.1-generic 5.0.21) [    0.681692] amd_uncore: AMD NB counters detected [    0.681709] amd_uncore: AMD LLC counters detected [    0.682511] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank). [    0.682526] perf/amd_iommu: Detected AMD IOMMU #1 (2 banks, 4 counters/bank). [    2.848560] amdkcl: loading out-of-tree module taints kernel. [    2.848644] amdkcl: module verification failed: signature and/or required key missing - tainting kernel [    2.974422] [drm] amdgpu kernel modesetting enabled. [    2.974423] [drm] amdgpu version: 5.2.4 [    2.976338] amdgpu 0000:0b:00.0: enabling device (0000 -&gt; 0003) [    3.077022] amdgpu 0000:0b:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used) [    3.077023] amdgpu 0000:0b:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF [    3.077024] amdgpu 0000:0b:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF [    3.077142] [drm] amdgpu: 16368M of VRAM memory ready [    3.077144] [drm] amdgpu: 64345M of GTT memory ready. [    3.093710] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu [    3.692034] amdgpu 0000:0b:00.0: HDCP: hdcp ta ucode is not available [    3.692036] amdgpu 0000:0b:00.0: DTM: dtm ta ucode is not available [    4.101555] amdgpu 0000:0b:00.0: ring gfx uses VM inv eng 0 on hub 0 [    4.101556] amdgpu 0000:0b:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0 [    4.101557] amdgpu 0000:0b:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0 [    4.101558] amdgpu 0000:0b:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0 [    4.101558] amdgpu 0000:0b:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0 [    4.101559] amdgpu 0000:0b:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0 [    4.101560] amdgpu 0000:0b:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0 [    4.101561] amdgpu 0000:0b:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0 [    4.101562] amdgpu 0000:0b:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0 [    4.101563] amdgpu 0000:0b:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0 [    4.101564] amdgpu 0000:0b:00.0: ring sdma0 uses VM inv eng 0 on hub 1 [    4.101564] amdgpu 0000:0b:00.0: ring page0 uses VM inv eng 1 on hub 1 [    4.101565] amdgpu 0000:0b:00.0: ring sdma1 uses VM inv eng 4 on hub 1 [    4.101566] amdgpu 0000:0b:00.0: ring page1 uses VM inv eng 5 on hub 1 [    4.101566] amdgpu 0000:0b:00.0: ring uvd_0 uses VM inv eng 6 on hub 1 [    4.101567] amdgpu 0000:0b:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1 [    4.101568] amdgpu 0000:0b:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1 [    4.101568] amdgpu 0000:0b:00.0: ring uvd_1 uses VM inv eng 9 on hub 1 [    4.101569] amdgpu 0000:0b:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1 [    4.101569] amdgpu 0000:0b:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1 [    4.101570] amdgpu 0000:0b:00.0: ring vce0 uses VM inv eng 12 on hub 1 [    4.101571] amdgpu 0000:0b:00.0: ring vce1 uses VM inv eng 13 on hub 1 [    4.101571] amdgpu 0000:0b:00.0: ring vce2 uses VM inv eng 14 on hub 1 [    4.101942] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:0b:00.0 on minor 0 [    4.102039] fb0: switching to amdgpudrmfb from VESA VGA [    4.105052] amdgpu 0000:43:00.0: No more image in the PCI ROM [    4.105158] amdgpu 0000:43:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used) [    4.105160] amdgpu 0000:43:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF [    4.105162] amdgpu 0000:43:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF [    4.105214] [drm] amdgpu: 16368M of VRAM memory ready [    4.105217] [drm] amdgpu: 64345M of GTT memory ready. [    4.108846] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu [    4.688025] amdgpu 0000:43:00.0: HDCP: hdcp ta ucode is not available [    4.688027] amdgpu 0000:43:00.0: DTM: dtm ta ucode is not available [    5.234184] fbcon: amdgpudrmfb (fb0) is primary device [    5.234268] amdgpu 0000:43:00.0: fb0: amdgpudrmfb frame buffer device [    5.268120] amdgpu 0000:43:00.0: ring gfx uses VM inv eng 0 on hub 0 [    5.268122] amdgpu 0000:43:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0 [    5.268124] amdgpu 0000:43:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0 [    5.268125] amdgpu 0000:43:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0 [    5.268126] amdgpu 0000:43:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0 [    5.268127] amdgpu 0000:43:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0 [    5.268128] amdgpu 0000:43:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0 [    5.268129] amdgpu 0000:43:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0 [    5.268130] amdgpu 0000:43:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0 [    5.268131] amdgpu 0000:43:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0 [    5.268132] amdgpu 0000:43:00.0: ring sdma0 uses VM inv eng 0 on hub 1 [    5.268133] amdgpu 0000:43:00.0: ring page0 uses VM inv eng 1 on hub 1 [    5.268134] amdgpu 0000:43:00.0: ring sdma1 uses VM inv eng 4 on hub 1 [    5.268135] amdgpu 0000:43:00.0: ring page1 uses VM inv eng 5 on hub 1 [    5.268136] amdgpu 0000:43:00.0: ring uvd_0 uses VM inv eng 6 on hub 1 [    5.268137] amdgpu 0000:43:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1 [    5.268138] amdgpu 0000:43:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1 [    5.268139] amdgpu 0000:43:00.0: ring uvd_1 uses VM inv eng 9 on hub 1 [    5.268140] amdgpu 0000:43:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1 [    5.268141] amdgpu 0000:43:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1 [    5.268141] amdgpu 0000:43:00.0: ring vce0 uses VM inv eng 12 on hub 1 [    5.268142] amdgpu 0000:43:00.0: ring vce1 uses VM inv eng 13 on hub 1 [    5.268143] amdgpu 0000:43:00.0: ring vce2 uses VM inv eng 14 on hub 1 [    5.268550] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:43:00.0 on minor 1 [    7.876319] EDAC amd64: Node 0: DRAM ECC disabled. [    7.876321] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    7.876325] EDAC amd64: Node 1: DRAM ECC disabled. [    7.876326] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    7.949320] EDAC amd64: Node 0: DRAM ECC disabled. [    7.949322] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    7.949326] EDAC amd64: Node 1: DRAM ECC disabled. [    7.949327] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.009715] EDAC amd64: Node 0: DRAM ECC disabled. [    8.009718] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.009722] EDAC amd64: Node 1: DRAM ECC disabled. [    8.009723] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.058005] EDAC amd64: Node 0: DRAM ECC disabled. [    8.058007] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.058012] EDAC amd64: Node 1: DRAM ECC disabled. [    8.058013] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.109646] EDAC amd64: Node 0: DRAM ECC disabled. [    8.109648] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.313628] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.353326] EDAC amd64: Node 0: DRAM ECC disabled. [    8.353327] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.353331] EDAC amd64: Node 1: DRAM ECC disabled. [    8.353332] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.409468] EDAC amd64: Node 0: DRAM ECC disabled. [    8.409470] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.409475] EDAC amd64: Node 1: DRAM ECC disabled. [    8.409476] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.457667] EDAC amd64: Node 0: DRAM ECC disabled. [    8.457670] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.457675] EDAC amd64: Node 1: DRAM ECC disabled. [    8.457676] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.525638] EDAC amd64: Node 0: DRAM ECC disabled. [    8.525640] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.525646] EDAC amd64: Node 1: DRAM ECC disabled. [    8.525647] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.565411] EDAC amd64: Node 0: DRAM ECC disabled. [    8.565413] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.565418] EDAC amd64: Node 1: DRAM ECC disabled. [    8.565419] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.625607] EDAC amd64: Node 0: DRAM ECC disabled. [    8.625608] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.625612] EDAC amd64: Node 1: DRAM ECC disabled. [    8.625613] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.677691] EDAC amd64: Node 0: DRAM ECC disabled. [    8.677692] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.677697] EDAC amd64: Node 1: DRAM ECC disabled. [    8.677698] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.725842] EDAC amd64: Node 0: DRAM ECC disabled. [    8.725845] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.725850] EDAC amd64: Node 1: DRAM ECC disabled. [    8.725851] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.769693] EDAC amd64: Node 0: DRAM ECC disabled. [    8.769695] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.769700] EDAC amd64: Node 1: DRAM ECC disabled. [    8.913608] EDAC amd64: Node 1: DRAM ECC disabled. [    8.913609] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.953692] EDAC amd64: Node 0: DRAM ECC disabled. [    8.953694] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.953699] EDAC amd64: Node 1: DRAM ECC disabled. [    8.953699] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.993789] EDAC amd64: Node 0: DRAM ECC disabled. [    8.993791] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    8.993796] EDAC amd64: Node 1: DRAM ECC disabled. [    8.993796] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.029829] EDAC amd64: Node 0: DRAM ECC disabled. [    9.029831] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.029836] EDAC amd64: Node 1: DRAM ECC disabled. [    9.029837] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.069584] EDAC amd64: Node 0: DRAM ECC disabled. [    9.069586] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.069590] EDAC amd64: Node 1: DRAM ECC disabled. [    9.069591] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.201560] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.253567] EDAC amd64: Node 0: DRAM ECC disabled. [    9.253569] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.253573] EDAC amd64: Node 1: DRAM ECC disabled. [    9.253574] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.289567] EDAC amd64: Node 0: DRAM ECC disabled. [    9.289568] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [    9.289572] EDAC amd64: Node 1: DRAM ECC disabled. [    9.289573] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.  (base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep VGA [    0.265649] pci 0000:0b:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none [    0.265649] pci 0000:43:00.0: vgaarb: setting as boot VGA device [    0.265649] pci 0000:43:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none [    0.711831] fb0: VESA VGA frame buffer device [    4.102039] fb0: switching to amdgpudrmfb from VESA VGA  (base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep kfd [    4.100422] kfd kfd: Allocated 3969056 bytes on gart [    4.101409] kfd kfd: added device 1002:66af [    5.231901] kfd kfd: Allocated 3969056 bytes on gart [    5.232512] kfd kfd: added device 1002:66af  
—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub, or unsubscribe.

---

### 评论 #6 — vsrikarunyan (2019-12-28T10:34:16Z)

> updating linux kernal to 5.0.x can figure out this problem.
> […](#)
> ------------------&nbsp;原始邮件&nbsp;------------------ 发件人: "Venkateshwaralu Srikarunyan"<notifications@github.com&gt;; 发送时间: 2019年12月26日(星期四) 下午2:06 收件人: "RadeonOpenCompute/ROCm"<ROCm@noreply.github.com&gt;; 抄送: "赖自成"<575840864@qq.com&gt;; "Comment"<comment@noreply.github.com&gt;; 主题: Re: [RadeonOpenCompute/ROCm] ROCm not correctly installed (#923) Yes, I too bumped on this one today (base) vsrikarunyan@d-rigg-evolv:~$ rocminfo ROCk module is loaded vsrikarunyan is member of video group hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.0/rocminfo/rocminfo.cc:1102 Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events. (base) vsrikarunyan@d-rigg-evolv:~$ clinfo Number of platforms: 1 Platform Profile: FULL_PROFILE Platform Version: OpenCL 2.1 AMD-APP (3052.0) Platform Name: AMD Accelerated Parallel Processing Platform Vendor: Advanced Micro Devices, Inc. Platform Extensions: cl_khr_icd cl_amd_event_callback cl_amd_offline_devices Platform Name: AMD Accelerated Parallel Processing ERROR: clGetDeviceIDs(-1) (base) vsrikarunyan@d-rigg-evolv:~$ uname -a Linux d-rigg-evolv.edu 5.0.0-37-generic #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux (base) vsrikarunyan@d-rigg-evolv:~$ cat /etc/os-release NAME="Ubuntu" VERSION="18.04.3 LTS (Bionic Beaver)" ID=ubuntu ID_LIKE=debian PRETTY_NAME="Ubuntu 18.04.3 LTS" VERSION_ID="18.04" HOME_URL="https://www.ubuntu.com/" SUPPORT_URL="https://help.ubuntu.com/" BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/" PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy" VERSION_CODENAME=bionic UBUNTU_CODENAME=bionic (base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep amd [ 0.000000] Linux version 5.0.0-37-generic (buildd@lcy01-amd64-023) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 (Ubuntu 5.0.0-37.40~18.04.1-generic 5.0.21) [ 0.681692] amd_uncore: AMD NB counters detected [ 0.681709] amd_uncore: AMD LLC counters detected [ 0.682511] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank). [ 0.682526] perf/amd_iommu: Detected AMD IOMMU #1 (2 banks, 4 counters/bank). [ 2.848560] amdkcl: loading out-of-tree module taints kernel. [ 2.848644] amdkcl: module verification failed: signature and/or required key missing - tainting kernel [ 2.974422] [drm] amdgpu kernel modesetting enabled. [ 2.974423] [drm] amdgpu version: 5.2.4 [ 2.976338] amdgpu 0000:0b:00.0: enabling device (0000 -&gt; 0003) [ 3.077022] amdgpu 0000:0b:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used) [ 3.077023] amdgpu 0000:0b:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF [ 3.077024] amdgpu 0000:0b:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF [ 3.077142] [drm] amdgpu: 16368M of VRAM memory ready [ 3.077144] [drm] amdgpu: 64345M of GTT memory ready. [ 3.093710] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu [ 3.692034] amdgpu 0000:0b:00.0: HDCP: hdcp ta ucode is not available [ 3.692036] amdgpu 0000:0b:00.0: DTM: dtm ta ucode is not available [ 4.101555] amdgpu 0000:0b:00.0: ring gfx uses VM inv eng 0 on hub 0 [ 4.101556] amdgpu 0000:0b:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0 [ 4.101557] amdgpu 0000:0b:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0 [ 4.101558] amdgpu 0000:0b:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0 [ 4.101558] amdgpu 0000:0b:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0 [ 4.101559] amdgpu 0000:0b:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0 [ 4.101560] amdgpu 0000:0b:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0 [ 4.101561] amdgpu 0000:0b:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0 [ 4.101562] amdgpu 0000:0b:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0 [ 4.101563] amdgpu 0000:0b:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0 [ 4.101564] amdgpu 0000:0b:00.0: ring sdma0 uses VM inv eng 0 on hub 1 [ 4.101564] amdgpu 0000:0b:00.0: ring page0 uses VM inv eng 1 on hub 1 [ 4.101565] amdgpu 0000:0b:00.0: ring sdma1 uses VM inv eng 4 on hub 1 [ 4.101566] amdgpu 0000:0b:00.0: ring page1 uses VM inv eng 5 on hub 1 [ 4.101566] amdgpu 0000:0b:00.0: ring uvd_0 uses VM inv eng 6 on hub 1 [ 4.101567] amdgpu 0000:0b:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1 [ 4.101568] amdgpu 0000:0b:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1 [ 4.101568] amdgpu 0000:0b:00.0: ring uvd_1 uses VM inv eng 9 on hub 1 [ 4.101569] amdgpu 0000:0b:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1 [ 4.101569] amdgpu 0000:0b:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1 [ 4.101570] amdgpu 0000:0b:00.0: ring vce0 uses VM inv eng 12 on hub 1 [ 4.101571] amdgpu 0000:0b:00.0: ring vce1 uses VM inv eng 13 on hub 1 [ 4.101571] amdgpu 0000:0b:00.0: ring vce2 uses VM inv eng 14 on hub 1 [ 4.101942] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:0b:00.0 on minor 0 [ 4.102039] fb0: switching to amdgpudrmfb from VESA VGA [ 4.105052] amdgpu 0000:43:00.0: No more image in the PCI ROM [ 4.105158] amdgpu 0000:43:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used) [ 4.105160] amdgpu 0000:43:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF [ 4.105162] amdgpu 0000:43:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF [ 4.105214] [drm] amdgpu: 16368M of VRAM memory ready [ 4.105217] [drm] amdgpu: 64345M of GTT memory ready. [ 4.108846] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu [ 4.688025] amdgpu 0000:43:00.0: HDCP: hdcp ta ucode is not available [ 4.688027] amdgpu 0000:43:00.0: DTM: dtm ta ucode is not available [ 5.234184] fbcon: amdgpudrmfb (fb0) is primary device [ 5.234268] amdgpu 0000:43:00.0: fb0: amdgpudrmfb frame buffer device [ 5.268120] amdgpu 0000:43:00.0: ring gfx uses VM inv eng 0 on hub 0 [ 5.268122] amdgpu 0000:43:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0 [ 5.268124] amdgpu 0000:43:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0 [ 5.268125] amdgpu 0000:43:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0 [ 5.268126] amdgpu 0000:43:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0 [ 5.268127] amdgpu 0000:43:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0 [ 5.268128] amdgpu 0000:43:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0 [ 5.268129] amdgpu 0000:43:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0 [ 5.268130] amdgpu 0000:43:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0 [ 5.268131] amdgpu 0000:43:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0 [ 5.268132] amdgpu 0000:43:00.0: ring sdma0 uses VM inv eng 0 on hub 1 [ 5.268133] amdgpu 0000:43:00.0: ring page0 uses VM inv eng 1 on hub 1 [ 5.268134] amdgpu 0000:43:00.0: ring sdma1 uses VM inv eng 4 on hub 1 [ 5.268135] amdgpu 0000:43:00.0: ring page1 uses VM inv eng 5 on hub 1 [ 5.268136] amdgpu 0000:43:00.0: ring uvd_0 uses VM inv eng 6 on hub 1 [ 5.268137] amdgpu 0000:43:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1 [ 5.268138] amdgpu 0000:43:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1 [ 5.268139] amdgpu 0000:43:00.0: ring uvd_1 uses VM inv eng 9 on hub 1 [ 5.268140] amdgpu 0000:43:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1 [ 5.268141] amdgpu 0000:43:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1 [ 5.268141] amdgpu 0000:43:00.0: ring vce0 uses VM inv eng 12 on hub 1 [ 5.268142] amdgpu 0000:43:00.0: ring vce1 uses VM inv eng 13 on hub 1 [ 5.268143] amdgpu 0000:43:00.0: ring vce2 uses VM inv eng 14 on hub 1 [ 5.268550] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:43:00.0 on minor 1 [ 7.876319] EDAC amd64: Node 0: DRAM ECC disabled. [ 7.876321] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 7.876325] EDAC amd64: Node 1: DRAM ECC disabled. [ 7.876326] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 7.949320] EDAC amd64: Node 0: DRAM ECC disabled. [ 7.949322] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 7.949326] EDAC amd64: Node 1: DRAM ECC disabled. [ 7.949327] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.009715] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.009718] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.009722] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.009723] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.058005] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.058007] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.058012] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.058013] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.109646] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.109648] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.313628] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.353326] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.353327] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.353331] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.353332] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.409468] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.409470] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.409475] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.409476] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.457667] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.457670] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.457675] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.457676] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.525638] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.525640] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.525646] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.525647] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.565411] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.565413] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.565418] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.565419] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.625607] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.625608] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.625612] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.625613] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.677691] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.677692] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.677697] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.677698] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.725842] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.725845] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.725850] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.725851] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.769693] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.769695] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.769700] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.913608] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.913609] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.953692] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.953694] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.953699] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.953699] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.993789] EDAC amd64: Node 0: DRAM ECC disabled. [ 8.993791] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 8.993796] EDAC amd64: Node 1: DRAM ECC disabled. [ 8.993796] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.029829] EDAC amd64: Node 0: DRAM ECC disabled. [ 9.029831] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.029836] EDAC amd64: Node 1: DRAM ECC disabled. [ 9.029837] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.069584] EDAC amd64: Node 0: DRAM ECC disabled. [ 9.069586] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.069590] EDAC amd64: Node 1: DRAM ECC disabled. [ 9.069591] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.201560] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.253567] EDAC amd64: Node 0: DRAM ECC disabled. [ 9.253569] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.253573] EDAC amd64: Node 1: DRAM ECC disabled. [ 9.253574] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.289567] EDAC amd64: Node 0: DRAM ECC disabled. [ 9.289568] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. [ 9.289572] EDAC amd64: Node 1: DRAM ECC disabled. [ 9.289573] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load. (base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep VGA [ 0.265649] pci 0000:0b:00.0: vgaarb: VGA device added: decodes=io+mem,owns=none,locks=none [ 0.265649] pci 0000:43:00.0: vgaarb: setting as boot VGA device [ 0.265649] pci 0000:43:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none [ 0.711831] fb0: VESA VGA frame buffer device [ 4.102039] fb0: switching to amdgpudrmfb from VESA VGA (base) vsrikarunyan@d-rigg-evolv:~$ dmesg | grep kfd [ 4.100422] kfd kfd: Allocated 3969056 bytes on gart [ 4.101409] kfd kfd: added device 1002:66af [ 5.231901] kfd kfd: Allocated 3969056 bytes on gart [ 5.232512] kfd kfd: added device 1002:66af — You are receiving this because you commented. Reply to this email directly, view it on GitHub, or unsubscribe.

That did not seem to have helped. 

```
(base) vsrikarunyan@d-rigg-evolv:~$ uname -sr
Linux 5.0.21-050021-generic
```
```
(base) vsrikarunyan@d-rigg-evolv:~$ rocminfo
ROCk module is loaded
vsrikarunyan is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.0/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

(base) vsrikarunyan@d-rigg-evolv:~$ clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3052.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
ERROR: clGetDeviceIDs(-1)

```
And, for what it's worth, rocm-smi seems to be recognising the devices

```
(base) vsrikarunyan@d-rigg-evolv:~$ rocm-smi


========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK    MCLK     Fan     Perf  PwrCap  VRAM%  GPU%  
0    34.0c  18.0W   808Mhz  350Mhz   21.96%  auto  250.0W    0%   0%    
1    39.0c  29.0W   808Mhz  1000Mhz  21.96%  auto  250.0W    3%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================

```

---

### 评论 #7 — jedbrown (2020-05-25T21:26:23Z)

I had the same issue on Debian "bullseye" until adding myself to group `render` (in addition to `video`).
```
$ ls -l /dev/dri/render*
crw-rw---- 1 root render 226, 128 May 24 22:42 /dev/dri/renderD128
```

---

### 评论 #8 — nartmada (2023-12-13T14:39:46Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #9 — nartmada (2023-12-18T17:16:08Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
