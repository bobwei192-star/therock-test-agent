# rocminfo got kernel panic

> **Issue #1401**
> **状态**: closed
> **创建时间**: 2021-03-06T12:22:47Z
> **更新时间**: 2021-03-09T08:34:25Z
> **关闭时间**: 2021-03-09T08:34:25Z
> **作者**: bugparty
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1401

## 描述

hello
my hardware is x370 chipset, amd 1800x cpu, amd 470 gpu.
uname -a
Linux rhel 4.18.0-240.15.1.el8_3.x86_64 #1 SMP Mon Mar 1 17:16:16 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

when I execute rocminfo

`/opt/rocm/bin/rocminfo 
ROCk module is loaded
Able to open /dev/kfd read-write
hsa api call failure at: /data/jenkins_workspace/centos_pipeline_job_4.0/rocm-rel-4.0/rocm-4.0-23-20201214/7.7/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
`

`/opt/rocm/opencl/bin/clinfo 
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP (3212.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
`

then the kernel has error messages as follow

[  777.927315] init_user_pages: Failed to get user pages: -1
[  777.927335] init_user_pages: Failed to get user pages: -1
[  777.927340] init_user_pages: Failed to get user pages: -1
[  777.927345] init_user_pages: Failed to get user pages: -1


/opt/rocm/bin/rocm-smi
ERROR:root:ROCm SMI returned 8 (the expected value is 0)

dmesg | grep kfd
[    3.982479] kfd kfd: Allocated 3969056 bytes on gart
[    3.983073] kfd kfd: added device 1002:67df


lspci | grep VGA
08:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] (rev cf)


dmesg | grep amd
[    0.719923] amd_uncore: AMD NB counters detected
[    0.719929] amd_uncore: AMD LLC counters detected
[    0.720155] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    3.753905] [drm] amdgpu kernel modesetting enabled.
[    3.754083] amdgpu 0000:08:00.0: vgaarb: deactivate vga console
[    3.755592] amdgpu 0000:08:00.0: No more image in the PCI ROM
[    3.755673] amdgpu 0000:08:00.0: BAR 2: releasing [mem 0xf0000000-0xf01fffff 64bit pref]
[    3.755674] amdgpu 0000:08:00.0: BAR 0: releasing [mem 0xe0000000-0xefffffff 64bit pref]
[    3.755696] amdgpu 0000:08:00.0: BAR 0: assigned [mem 0x900000000-0x9ffffffff 64bit pref]
[    3.755702] amdgpu 0000:08:00.0: BAR 2: assigned [mem 0x880000000-0x8801fffff 64bit pref]
[    3.755722] amdgpu 0000:08:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[    3.755723] amdgpu 0000:08:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[    3.755795] [drm] amdgpu: 4096M of VRAM memory ready
[    3.755797] [drm] amdgpu: 4096M of GTT memory ready.
[    3.758834] amdgpu: [powerplay] hwmgr_sw_init smu backed is polaris10_smu
[    3.984105] fbcon: amdgpudrmfb (fb0) is primary device
[    4.049444] amdgpu 0000:08:00.0: fb0: amdgpudrmfb frame buffer device
[    4.062065] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:08:00.0 on minor 0
[   10.819590] snd_hda_intel 0000:08:00.1: bound 0000:08:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[   10.825958] EDAC amd64: F17h detected (node 0).
[   10.826010] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.826010] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.826209] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.826210] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.826210] EDAC amd64: using x4 syndromes.
[   10.826215] EDAC amd64: Node 0: DRAM ECC disabled.
[   10.826215] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   10.852584] EDAC amd64: F17h detected (node 0).
[   10.852625] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.852625] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.852628] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.852628] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.852629] EDAC amd64: using x4 syndromes.
[   10.852633] EDAC amd64: Node 0: DRAM ECC disabled.
[   10.852633] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   10.877141] EDAC amd64: F17h detected (node 0).
[   10.877180] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.877180] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.877183] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.877183] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.877184] EDAC amd64: using x4 syndromes.
[   10.877187] EDAC amd64: Node 0: DRAM ECC disabled.
[   10.877188] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   10.905766] EDAC amd64: F17h detected (node 0).
[   10.905804] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.905804] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.905807] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.905807] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.905807] EDAC amd64: using x4 syndromes.
[   10.905811] EDAC amd64: Node 0: DRAM ECC disabled.
[   10.905811] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   10.941722] EDAC amd64: F17h detected (node 0).
[   10.941760] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.941761] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.941763] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.941763] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.941764] EDAC amd64: using x4 syndromes.
[   10.941767] EDAC amd64: Node 0: DRAM ECC disabled.
[   10.941768] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   10.974615] EDAC amd64: F17h detected (node 0).
[   10.974653] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.974654] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.974656] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.974656] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.974657] EDAC amd64: using x4 syndromes.
[   10.974660] EDAC amd64: Node 0: DRAM ECC disabled.
[   10.974661] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   10.999553] EDAC amd64: F17h detected (node 0).
[   10.999591] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.999591] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.999594] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   10.999594] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   10.999594] EDAC amd64: using x4 syndromes.
[   10.999598] EDAC amd64: Node 0: DRAM ECC disabled.
[   10.999599] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.027710] EDAC amd64: F17h detected (node 0).
[   11.027750] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.027751] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.027753] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.027754] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.027754] EDAC amd64: using x4 syndromes.
[   11.027758] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.027759] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.057838] EDAC amd64: F17h detected (node 0).
[   11.057877] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.057877] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.057880] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.057880] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.057880] EDAC amd64: using x4 syndromes.
[   11.057884] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.057885] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.083777] EDAC amd64: F17h detected (node 0).
[   11.083816] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.083816] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.083818] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.083819] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.083819] EDAC amd64: using x4 syndromes.
[   11.083823] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.083823] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.113838] EDAC amd64: F17h detected (node 0).
[   11.113876] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.113877] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.113879] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.113880] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.113880] EDAC amd64: using x4 syndromes.
[   11.113884] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.113884] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.141781] EDAC amd64: F17h detected (node 0).
[   11.141816] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.141816] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.141818] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.141819] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.141819] EDAC amd64: using x4 syndromes.
[   11.141823] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.141823] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.171101] EDAC amd64: F17h detected (node 0).
[   11.171140] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.171141] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.171144] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.171144] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.171145] EDAC amd64: using x4 syndromes.
[   11.171148] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.171149] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.195558] EDAC amd64: F17h detected (node 0).
[   11.195594] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.195595] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.195597] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.195598] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.195598] EDAC amd64: using x4 syndromes.
[   11.195603] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.195603] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.224732] EDAC amd64: F17h detected (node 0).
[   11.224768] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.224768] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.224771] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.224771] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.224772] EDAC amd64: using x4 syndromes.
[   11.224776] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.224776] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   11.249115] EDAC amd64: F17h detected (node 0).
[   11.249153] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.249154] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.249156] EDAC amd64: MC: 0:  4096MB 1:  4096MB
[   11.249156] EDAC amd64: MC: 2:  4096MB 3:  4096MB
[   11.249157] EDAC amd64: using x4 syndromes.
[   11.249161] EDAC amd64: Node 0: DRAM ECC disabled.
[   11.249161] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.



---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-03-09T08:34:24Z)

Thanks @bugparty for reaching out.
We are not supporting gfx8 devices officially. Request you to check our docs and supported hardware sections @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Thank you.

---
