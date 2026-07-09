# [Issue]:  SVM mapping failure during sequential model loads (RDNA3/RX 7900 GRE)

- **Issue #:** 5952
- **State:** open
- **Created:** 2026-02-11T01:49:03Z
- **Updated:** 2026-05-10T10:24:58Z
- **Labels:** AMD Radeon RX 7900 GRE, status: triage
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5952

### Problem Description

I'm currently using the nightly builds from TheRock, but this issue happens even with 7.1 and 7.2.

Note: I've also filed a bug with ComfyUI, but I think this may be more an ROCm issue since I've tried multiple ComfyUI committs and settings.

My ComfyUI WAN 2.2 Image-to-Video workflow fails consistently when transitioning between different AI models (high noise → low noise or vice versa) due to possible SVM mapping failures. The system experiences RAM exhaustion, partial VRAM loading, and eventual process termination or system crash when using FP8 models; when using GGUFs, it simply sits in the loading phase forever seemingly (the VRAM crawls up from 3gb VERY slowly). I was able to run my workflow without issues dozens of times, but now I can barely get past the first high-noise phase. The issue started within the last 3-4 days. I can get it to SOMETIMES run, but I can't pin down any rhyme or reason to when it decides to work.

Specs:

GPU: AMD Radeon RX 7900 GRE
CPU: AMD Ryzen 7 7800X3D
RAM: 32GB DDR5
Motherboard: MSI MAG B650 Tomahawk
OS: Ubuntu 25.10

I've tried:

Kernels: 6.8.0-51, 6.17.0-8, 6.17.0-12, 6.17.0-14, 6.18.7
ROCm: 7.1, 7.2, 7.3 (nightly 7.12.0a20260206)
PyTorch: 2.9.1, 2.10.0
ComfyUI: 0.11.0 through 0.12.3

I'm currently using the built-in graphics drivers and not the ones installed with amdgpu-install, but I've tested both.

dmesg:

```
[Tue Feb 10 19:23:20 2026] [drm] amdgpu kernel modesetting enabled.
[Tue Feb 10 19:23:20 2026] amdgpu: vga_switcheroo: detected switching method \_SB_.PCI0.GP17.VGA_.ATPX handle
[Tue Feb 10 19:23:20 2026] amdgpu: ATPX version 1, functions 0x00000000
[Tue Feb 10 19:23:20 2026] amdgpu: Virtual CRAT table created for CPU
[Tue Feb 10 19:23:20 2026] amdgpu: Topology: Add CPU node
[Tue Feb 10 19:23:20 2026] amdgpu: Overdrive is enabled, please disable it before reporting any bugs unrelated to overdrive.
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: enabling device (0006 -> 0007)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: initializing kernel modesetting (IP DISCOVERY 0x1002:0x744C 0x1EAE:0x790A 0xCE).
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: register mmio base: 0xF6B00000
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: register mmio size: 1048576
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 0 <common_v1_0_0> (soc21_common)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 1 <gmc_v11_0_0> (gmc_v11_0)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 2 <ih_v6_0_0> (ih_v6_0)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 3 <psp_v13_0_0> (psp)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 4 <smu_v13_0_0> (smu)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 5 <dce_v1_0_0> (dm)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 6 <gfx_v11_0_0> (gfx_v11_0)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 7 <sdma_v6_0_0> (sdma_v6_0)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 8 <vcn_v4_0_0> (vcn_v4_0)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 9 <jpeg_v4_0_0> (jpeg_v4_0)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: detected ip block number 10 <mes_v11_0_0> (mes_v11_0)
[Tue Feb 10 19:23:20 2026] amdgpu 0000:03:00.0: amdgpu: Fetched VBIOS from VFCT
[Tue Feb 10 19:23:20 2026] amdgpu: ATOM BIOS: 113-EXT91535-100
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: CP RS64 enable
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: vgaarb: deactivate vga console
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: MEM ECC is not presented.
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: SRAM ECC is not presented.
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: GART: 512M 0x00007FFF00000000 - 0x00007FFF1FFFFFFF
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: amdgpu: 16368M of VRAM memory ready
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: amdgpu: 15335M of GTT memory ready.
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] Loading DMUB firmware via PSP: version=0x07002F00
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [VCN instance 0] Found VCN firmware Version ENC: 1.24 DEC: 9 VEP: 0 Revision: 22
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [VCN instance 1] Found VCN firmware Version ENC: 1.24 DEC: 9 VEP: 0 Revision: 22
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: reserve 0x1300000 from 0x83fc000000 for PSP TMR
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: optional securedisplay ta ucode is not available
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x0000003d, smu fw if version = 0x00000040, smu fw program = 0, smu fw version = 0x004e8200 (78.130.0)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: SMU is initialized successfully!
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] Display Core v3.2.351 initialized on DCN 3.2
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] DP-HDMI FRL PCON supported
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x07002F00
[Tue Feb 10 19:23:21 2026] snd_hda_intel 0000:03:00.1: bound 0000:03:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] DP-1: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] DP-2: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] DP-3: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] HDMI-A-1: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu: HMM registered 16368MB device memory
[Tue Feb 10 19:23:21 2026] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[Tue Feb 10 19:23:21 2026] kfd kfd: amdgpu: Total number of KFD nodes to be created: 1
[Tue Feb 10 19:23:21 2026] amdgpu: Virtual CRAT table created for GPU
[Tue Feb 10 19:23:21 2026] amdgpu: Topology: Add dGPU node [0x744c:0x1002]
[Tue Feb 10 19:23:21 2026] kfd kfd: amdgpu: added device 1002:744c
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: SE 6, SH per SE 2, CU per SH 8, active_cu_number 80
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring sdma1 uses VM inv eng 13 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 4 on hub 8
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 14 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: Using BACO for runtime pm
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: [drm] Registered 4 planes with drm panic
[Tue Feb 10 19:23:21 2026] [drm] Initialized amdgpu 3.64.0 for 0000:03:00.0 on minor 1
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: amdgpu: [drm] Failed to setup vendor infoframe on connector HDMI-A-1: -22
[Tue Feb 10 19:23:21 2026] fbcon: amdgpudrmfb (fb0) is primary device
[Tue Feb 10 19:23:21 2026] amdgpu 0000:03:00.0: [drm] fb0: amdgpudrmfb frame buffer device
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: enabling device (0006 -> 0007)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: initializing kernel modesetting (IP DISCOVERY 0x1002:0x164E 0x1462:0x7D75 0xCB).
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: register mmio base: 0xF6A00000
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: register mmio size: 524288
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 0 <common_v1_0_0> (nv_common)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 1 <gmc_v10_0_0> (gmc_v10_0)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 2 <ih_v5_0_0> (navi10_ih)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 3 <psp_v13_0_0> (psp)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 4 <smu_v13_0_0> (smu)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 5 <dce_v1_0_0> (dm)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 6 <gfx_v10_0_0> (gfx_v10_0)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 7 <sdma_v5_2_0> (sdma_v5_2)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 8 <vcn_v3_0_0> (vcn_v3_0)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: detected ip block number 9 <jpeg_v3_0_0> (jpeg_v3_0)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: Fetched VBIOS from VFCT
[Tue Feb 10 19:23:21 2026] amdgpu: ATOM BIOS: 102-RAPHAEL-008
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: Trusted Memory Zone (TMZ) feature disabled as experimental (default)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: VRAM: 512M 0x000000F400000000 - 0x000000F41FFFFFFF (512M used)
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: amdgpu: 512M of VRAM memory ready
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: amdgpu: 15335M of GTT memory ready.
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] Loading DMUB firmware via PSP: version=0x05002A00
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [VCN instance 0] Found VCN firmware Version ENC: 1.33 DEC: 4 VEP: 0 Revision: 12
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: reserve 0xa00000 from 0xf41e000000 for PSP TMR
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: RAS: optional ras ta ucode is not available
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: RAP: optional rap ta ucode is not available
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: SECUREDISPLAY: optional securedisplay ta ucode is not available
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: SMU is initialized successfully!
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] Display Core v3.2.351 initialized on DCN 3.1.5
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] DP-HDMI FRL PCON supported
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x05002A00
[Tue Feb 10 19:23:21 2026] snd_hda_intel 0000:12:00.1: bound 0000:12:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] HDMI-A-2: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] DP-4: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] DP-5: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: [drm] DP-6: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: kiq ring mec 2 pipe 1 q 0
[Tue Feb 10 19:23:21 2026] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[Tue Feb 10 19:23:21 2026] kfd kfd: amdgpu: Total number of KFD nodes to be created: 1
[Tue Feb 10 19:23:21 2026] amdgpu: Virtual CRAT table created for GPU
[Tue Feb 10 19:23:21 2026] amdgpu: Topology: Add dGPU node [0x164e:0x1002]
[Tue Feb 10 19:23:21 2026] kfd kfd: amdgpu: added device 1002:164e
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: SE 1, SH per SE 1, CU per SH 2, active_cu_number 2
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring gfx_0.1.0 uses VM inv eng 1 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 4 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 5 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring kiq_0.2.1.0 uses VM inv eng 12 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring sdma0 uses VM inv eng 13 on hub 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring vcn_dec_0 uses VM inv eng 0 on hub 8
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring vcn_enc_0.0 uses VM inv eng 1 on hub 8
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring vcn_enc_0.1 uses VM inv eng 4 on hub 8
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: ring jpeg_dec uses VM inv eng 5 on hub 8
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: amdgpu: Runtime PM not available
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: [drm] Registered 4 planes with drm panic
[Tue Feb 10 19:23:21 2026] [drm] Initialized amdgpu 3.64.0 for 0000:12:00.0 on minor 0
[Tue Feb 10 19:23:21 2026] amdgpu 0000:12:00.0: [drm] Cannot find any crtc or sizes
[Tue Feb 10 19:23:31 2026] workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:23:31 2026] workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 5 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:23:32 2026] workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 7 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:23:32 2026] workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 11 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:27:11 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:27:11 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 5 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:27:11 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 7 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:27:12 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 11 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:27:14 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 19 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:31:42 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 35 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:32:03 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 67 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:34:57 2026] workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:34:58 2026] workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 5 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:35:31 2026] workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 7 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:35:34 2026] workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 131 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:37:42 2026] workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 11 times, consider switching to WQ_UNBOUND
[Tue Feb 10 19:43:40 2026] amdgpu: Freeing queue vital buffer 0x7fc107400000, queue evicted
[Tue Feb 10 19:43:40 2026] amdgpu: Freeing queue vital buffer 0x7fc109a00000, queue evicted

```

sudo journalctl -k -b -0 | grep -iE "amdgpu|ring|timeout|mes|kfd|reset"

```
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-6.18.7-061807-generic root=UUID=496c7494-fdff-4521-9069-60d99636feb1 ro quiet splash fsck.mode=force nvme_load=YES amdgpu.ppfeaturemask=0xffffffff amdgpu.cwsr_enable=0 crashkernel=2G-4G:320M,4G-32G:512M,32G-64G:1024M,64G-128G:2048M,128G-:4096M vt.handoff=7
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.18.7-061807-generic root=UUID=496c7494-fdff-4521-9069-60d99636feb1 ro quiet splash fsck.mode=force nvme_load=YES amdgpu.ppfeaturemask=0xffffffff amdgpu.cwsr_enable=0 crashkernel=2G-4G:320M,4G-32G:512M,32G-64G:1024M,64G-128G:2048M,128G-:4096M vt.handoff=7
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: smp: Bringing up secondary CPUs ...
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: ACPI: PM: Registering ACPI NVS region [mem 0x0a200000-0x0a20ffff] (65536 bytes)
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: ACPI: PM: Registering ACPI NVS region [mem 0xad47f000-0xaf47efff] (33554432 bytes)
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: PCI: Ignoring E820 reservations for host bridge windows
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: Initialise system trusted keyrings
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: workingset: timestamp_bits=36 max_order=23 bucket_order=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: integrity: Platform Keyring initialized
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: integrity: Machine keyring initialized
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: Estimated ratio of average max frequency by base frequency (times 1024): 1127
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb usb5: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb usb6: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb usb7: New USB device strings: Mfr=3, Product=2, SerialNumber=1
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: fbcon: Deferring console take-over
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: x86/amd: Previous system reset reason [0x01000800]: system failed to boot before failed boot timer expired
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: resctrl: L3 monitoring detected
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: r8169 0000:0e:00.0 eth0: jumbo features [frames: 16362 bytes, tx checksumming: ko]
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 5-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 6-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 1-5: New USB device strings: Mfr=2, Product=3, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 2-5: New USB device strings: Mfr=2, Product=3, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 5-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 1-5.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 1-6: New USB device strings: Mfr=3, Product=1, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 5-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 1-10: New USB device strings: Mfr=1, Product=2, SerialNumber=3
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: usb 1-12: New USB device strings: Mfr=0, Product=1, SerialNumber=0
Feb 10 19:23:19 vsekar92-MS-7D75 systemd[1]: Reached target integritysetup.target - Local Integrity Protected Volumes.
Feb 10 19:23:19 vsekar92-MS-7D75 systemd[1]: Reached target veritysetup.target - Local Verity Protected Volumes.
Feb 10 19:23:19 vsekar92-MS-7D75 systemd[1]: Mounting dev-mqueue.mount - POSIX Message Queue File System...
Feb 10 19:23:19 vsekar92-MS-7D75 systemd[1]: Mounted dev-mqueue.mount - POSIX Message Queue File System.
Feb 10 19:23:19 vsekar92-MS-7D75 systemd-journald[671]: Collecting audit messages is disabled.
Feb 10 19:23:19 vsekar92-MS-7D75 kernel: bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: [drm] amdgpu kernel modesetting enabled.
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu: vga_switcheroo: detected switching method \_SB_.PCI0.GP17.VGA_.ATPX handle
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu: ATPX version 1, functions 0x00000000
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu: Virtual CRAT table created for CPU
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu: Topology: Add CPU node
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu: Overdrive is enabled, please disable it before reporting any bugs unrelated to overdrive.
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: enabling device (0006 -> 0007)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: initializing kernel modesetting (IP DISCOVERY 0x1002:0x744C 0x1EAE:0x790A 0xCE).
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: register mmio base: 0xF6B00000
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: register mmio size: 1048576
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 0 <common_v1_0_0> (soc21_common)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 1 <gmc_v11_0_0> (gmc_v11_0)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 2 <ih_v6_0_0> (ih_v6_0)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 3 <psp_v13_0_0> (psp)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 4 <smu_v13_0_0> (smu)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 5 <dce_v1_0_0> (dm)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 6 <gfx_v11_0_0> (gfx_v11_0)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 7 <sdma_v6_0_0> (sdma_v6_0)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 8 <vcn_v4_0_0> (vcn_v4_0)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 9 <jpeg_v4_0_0> (jpeg_v4_0)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: detected ip block number 10 <mes_v11_0_0> (mes_v11_0)
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: Fetched VBIOS from VFCT
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu: ATOM BIOS: 113-EXT91535-100
Feb 10 19:23:20 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: CP RS64 enable
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: vgaarb: deactivate vga console
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: MEM ECC is not presented.
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: SRAM ECC is not presented.
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: GART: 512M 0x00007FFF00000000 - 0x00007FFF1FFFFFFF
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: amdgpu: 16368M of VRAM memory ready
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: amdgpu: 15335M of GTT memory ready.
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] Loading DMUB firmware via PSP: version=0x07002F00
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [VCN instance 0] Found VCN firmware Version ENC: 1.24 DEC: 9 VEP: 0 Revision: 22
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [VCN instance 1] Found VCN firmware Version ENC: 1.24 DEC: 9 VEP: 0 Revision: 22
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: reserve 0x1300000 from 0x83fc000000 for PSP TMR
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: RAP: optional rap ta ucode is not available
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: optional securedisplay ta ucode is not available
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x0000003d, smu fw if version = 0x00000040, smu fw program = 0, smu fw version = 0x004e8200 (78.130.0)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: SMU is initialized successfully!
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] Display Core v3.2.351 initialized on DCN 3.2
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] DP-HDMI FRL PCON supported
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x07002F00
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: snd_hda_intel 0000:03:00.1: bound 0000:03:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] DP-1: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] DP-2: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] DP-3: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] HDMI-A-1: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu: HMM registered 16368MB device memory
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: kfd kfd: amdgpu: Allocated 3969056 bytes on gart
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: kfd kfd: amdgpu: Total number of KFD nodes to be created: 1
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu: Virtual CRAT table created for GPU
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu: Topology: Add dGPU node [0x744c:0x1002]
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: kfd kfd: amdgpu: added device 1002:744c
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: SE 6, SH per SE 2, CU per SH 8, active_cu_number 80
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring sdma1 uses VM inv eng 13 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring jpeg_dec uses VM inv eng 4 on hub 8
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 14 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: Using BACO for runtime pm
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: [drm] Registered 4 planes with drm panic
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: [drm] Initialized amdgpu 3.64.0 for 0000:03:00.0 on minor 1
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: amdgpu: [drm] Failed to setup vendor infoframe on connector HDMI-A-1: -22
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: fbcon: amdgpudrmfb (fb0) is primary device
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: fbcon: Deferring console take-over
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:03:00.0: [drm] fb0: amdgpudrmfb frame buffer device
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: enabling device (0006 -> 0007)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: initializing kernel modesetting (IP DISCOVERY 0x1002:0x164E 0x1462:0x7D75 0xCB).
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: register mmio base: 0xF6A00000
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: register mmio size: 524288
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 0 <common_v1_0_0> (nv_common)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 1 <gmc_v10_0_0> (gmc_v10_0)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 2 <ih_v5_0_0> (navi10_ih)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 3 <psp_v13_0_0> (psp)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 4 <smu_v13_0_0> (smu)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 5 <dce_v1_0_0> (dm)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 6 <gfx_v10_0_0> (gfx_v10_0)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 7 <sdma_v5_2_0> (sdma_v5_2)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 8 <vcn_v3_0_0> (vcn_v3_0)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: detected ip block number 9 <jpeg_v3_0_0> (jpeg_v3_0)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: Fetched VBIOS from VFCT
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu: ATOM BIOS: 102-RAPHAEL-008
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: Trusted Memory Zone (TMZ) feature disabled as experimental (default)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: VRAM: 512M 0x000000F400000000 - 0x000000F41FFFFFFF (512M used)
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: GART: 1024M 0x0000000000000000 - 0x000000003FFFFFFF
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: amdgpu: 512M of VRAM memory ready
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: amdgpu: 15335M of GTT memory ready.
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] Loading DMUB firmware via PSP: version=0x05002A00
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [VCN instance 0] Found VCN firmware Version ENC: 1.33 DEC: 4 VEP: 0 Revision: 12
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: reserve 0xa00000 from 0xf41e000000 for PSP TMR
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: RAS: optional ras ta ucode is not available
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: RAP: optional rap ta ucode is not available
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: SECUREDISPLAY: optional securedisplay ta ucode is not available
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: SMU is initialized successfully!
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] Display Core v3.2.351 initialized on DCN 3.1.5
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] DP-HDMI FRL PCON supported
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x05002A00
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: snd_hda_intel 0000:12:00.1: bound 0000:12:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] HDMI-A-2: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] DP-4: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] DP-5: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: [drm] DP-6: PSR support 0, DC PSR ver -1, sink PSR ver 0 DPCD caps 0x0 su_y_granularity 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: kiq ring mec 2 pipe 1 q 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: kfd kfd: amdgpu: Allocated 3969056 bytes on gart
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: kfd kfd: amdgpu: Total number of KFD nodes to be created: 1
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu: Virtual CRAT table created for GPU
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu: Topology: Add dGPU node [0x164e:0x1002]
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: kfd kfd: amdgpu: added device 1002:164e
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: SE 1, SH per SE 1, CU per SH 2, active_cu_number 2
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring gfx_0.1.0 uses VM inv eng 1 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 4 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 5 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring kiq_0.2.1.0 uses VM inv eng 12 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring sdma0 uses VM inv eng 13 on hub 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring vcn_dec_0 uses VM inv eng 0 on hub 8
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring vcn_enc_0.0 uses VM inv eng 1 on hub 8
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring vcn_enc_0.1 uses VM inv eng 4 on hub 8
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: ring jpeg_dec uses VM inv eng 5 on hub 8
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: amdgpu: Runtime PM not available
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: [drm] Registered 4 planes with drm panic
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: [drm] Initialized amdgpu 3.64.0 for 0000:12:00.0 on minor 0
Feb 10 19:23:21 vsekar92-MS-7D75 kernel: amdgpu 0000:12:00.0: [drm] Cannot find any crtc or sizes
Feb 10 19:23:31 vsekar92-MS-7D75 kernel: workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
Feb 10 19:23:31 vsekar92-MS-7D75 kernel: workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 5 times, consider switching to WQ_UNBOUND
Feb 10 19:23:32 vsekar92-MS-7D75 kernel: workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 7 times, consider switching to WQ_UNBOUND
Feb 10 19:23:32 vsekar92-MS-7D75 kernel: workqueue: dm_handle_vmin_vmax_update [amdgpu] hogged CPU for >10000us 11 times, consider switching to WQ_UNBOUND
Feb 10 19:23:44 vsekar92-MS-7D75 kernel: usb 6-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
Feb 10 19:23:54 vsekar92-MS-7D75 kernel: usb 5-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
Feb 10 19:27:10 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
Feb 10 19:27:11 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 5 times, consider switching to WQ_UNBOUND
Feb 10 19:27:11 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 7 times, consider switching to WQ_UNBOUND
Feb 10 19:27:11 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 11 times, consider switching to WQ_UNBOUND
Feb 10 19:27:13 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 19 times, consider switching to WQ_UNBOUND
Feb 10 19:31:41 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 35 times, consider switching to WQ_UNBOUND
Feb 10 19:32:02 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 67 times, consider switching to WQ_UNBOUND
Feb 10 19:34:56 vsekar92-MS-7D75 kernel: workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 4 times, consider switching to WQ_UNBOUND
Feb 10 19:34:57 vsekar92-MS-7D75 kernel: workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 5 times, consider switching to WQ_UNBOUND
Feb 10 19:35:30 vsekar92-MS-7D75 kernel: workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 7 times, consider switching to WQ_UNBOUND
Feb 10 19:35:33 vsekar92-MS-7D75 kernel: workqueue: svm_range_restore_work [amdgpu] hogged CPU for >10000us 131 times, consider switching to WQ_UNBOUND
Feb 10 19:37:41 vsekar92-MS-7D75 kernel: workqueue: amdgpu_amdkfd_restore_userptr_worker [amdgpu] hogged CPU for >10000us 11 times, consider switching to WQ_UNBOUND
Feb 10 19:43:40 vsekar92-MS-7D75 kernel: amdgpu: Freeing queue vital buffer 0x7fc107400000, queue evicted
Feb 10 19:43:40 vsekar92-MS-7D75 kernel: amdgpu: Freeing queue vital buffer 0x7fc109a00000, queue evicted
```


### Operating System

Ubuntu 25.10

### CPU

AMD Ryzen 7800X3D

### GPU

RX 7900 GRE

### ROCm Version

7.x

### ROCm Component

_No response_

### Steps to Reproduce

1) Run any Wan2.2 I2V workflow
2) High noise sampler will run normally
3) The workflow never starts sampling in the low noise sampler - ComfyUI gets killed due to OOM or system crash if using fp8/fp16 models, or it just stays stuck loading the model into VRAM if using GGUF.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.16
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 7800X3D 8-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 7800X3D 8-Core Processor
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
  Max Clock Freq. (MHz):   5053                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    31406488(0x1df3998) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    31406488(0x1df3998) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    31406488(0x1df3998) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    31406488(0x1df3998) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-2d9493875069a81b               
  Marketing Name:          AMD Radeon RX 7900 GRE             
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
    L2:                      6144(0x1800) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2052                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            80                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 602                                
  SDMA engine uCode::      27                                 
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
      Name:                    amdgcn-amd-amdhsa--gfx1100         
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    gfx1036                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      256(0x100) KB                      
  Chip ID:                 5710(0x164e)                       
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   4608                               
  Internal Node ID:        2                                  
  Compute Unit:            2                                  
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       APU
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 26                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    15703244(0xef9ccc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    15703244(0xef9ccc) KB              
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
      Name:                    amdgcn-amd-amdhsa--gfx1036         
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx10-3-generic 
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32   

```
### Additional Information

_No response_