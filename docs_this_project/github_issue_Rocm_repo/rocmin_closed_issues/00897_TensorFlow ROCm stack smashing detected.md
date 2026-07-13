# TensorFlow ROCm stack smashing detected 

- **Issue #:** 897
- **State:** closed
- **Created:** 2019-09-30T09:01:49Z
- **Updated:** 2019-10-01T09:13:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/897

CPU: Ryzen 2600
GPU: RX570 4GB
Operating System: Linux version 4.15.0-64-generic (buildd@lgw01-amd64-038) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #73-Ubuntu SMP Thu Sep 12 13:16:13 UTC 2019

2019-09-30 16:53:48.733643: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libhip_hcc.so
*** stack smashing detected ***: <unknown> terminated
Aborted (core dumped)

wei@WeiCh:~/Downloads$ dmesg | grep amd
[    0.000000] Linux version 4.15.0-64-generic (buildd@lgw01-amd64-038) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #73-Ubuntu SMP Thu Sep 12 13:16:13 UTC 2019 (Ubuntu 4.15.0-64.73-generic 4.15.18)
[    0.541457] amd_uncore: AMD NB counters detected
[    0.541459] amd_uncore: AMD LLC counters detected
[    0.541906] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[   20.305090] amdkcl: loading out-of-tree module taints kernel.
[   20.305108] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   20.712614] [drm] amdgpu kernel modesetting enabled.
[   20.712615] [drm] amdgpu version: 5.0.79
[   20.912825] fb: switching to amdgpudrmfb from EFI VGA
[   20.912978] amdgpu 0000:09:00.0: enabling device (0006 -> 0007)
[   21.200915] amdgpu 0000:09:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[   21.200916] amdgpu 0000:09:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   21.201004] [drm] amdgpu: 4096M of VRAM memory ready
[   21.201006] [drm] amdgpu: 7991M of GTT memory ready.
[   21.515494] amdgpu: [powerplay] hwmgr_sw_init smu backed is polaris10_smu
[   22.091956] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.091958] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.125741] fbcon: amdgpudrmfb (fb0) is primary device
[   22.125838] amdgpu 0000:09:00.0: fb0: amdgpudrmfb frame buffer device
[   22.147189] [drm] Initialized amdgpu 3.34.0 20150101 for 0000:09:00.0 on minor 0
[   22.180749] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.180750] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.220552] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.220553] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.252466] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.252467] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.292466] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.292467] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.324452] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.324453] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.364506] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.364507] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.412441] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.412442] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.444393] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.444394] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.500402] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.500403] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.540467] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.540468] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.
[   22.576510] EDAC amd64: Node 0: DRAM ECC disabled.
[   22.576511] EDAC amd64: ECC disabled in the BIOS or no ECC capability, module will not load.


