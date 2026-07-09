# Installation issue on KDE Neon ROCm 2.0

- **Issue #:** 644
- **State:** closed
- **Created:** 2018-12-23T16:58:37Z
- **Updated:** 2018-12-23T18:05:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/644

It gives an error when using `opt/rocm/bin/rocminfo ` command. The error is; `hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104`

GPU: Vega 64
CPU: Ryzen 5 1600

groups output: furkan adm cdrom sudo dip video plugdev lpadmin sambashare

other outputs

> furkan@furkan-PC:~/Downloads/RosaImageWriter$ dmesg | grep amd          
[    0.000000] Linux version 4.15.0-43-generic (buildd@lgw01-amd64-001) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #46-Ubuntu SMP Thu Dec 6 14:45:28 UTC 2018 (Ubuntu 4.15.0-43.46-generic 4.15.18)
[    0.783213] amd_uncore: AMD NB counters detected
[    0.783215] amd_uncore: AMD LLC counters detected
[    0.783671] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).
[    0.880630] pcie_mp2_amd: AMD(R) PCI-E MP2 Communication Driver Version: 1.0
[    1.069566] [drm] amdgpu kernel modesetting enabled.
[    1.073401] fb: switching to amdgpudrmfb from VESA VGA
[    1.073679] amdgpu 0000:09:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[    1.073716] amdgpu 0000:09:00.0: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
[    1.073717] amdgpu 0000:09:00.0: GTT: 256M 0x000000F5FF000000 - 0x000000F60EFFFFFF
[    1.073784] [drm] amdgpu: 8176M of VRAM memory ready
[    1.073785] [drm] amdgpu: 8176M of GTT memory ready.
[    1.073978] amdgpu 0000:09:00.0: amdgpu: using MSI.
[    1.074049] [drm] amdgpu: irq initialized.
[    1.074149] amdgpu: [powerplay] amdgpu: powerplay sw initialized
[    1.074370] amdgpu 0000:09:00.0: fence driver on ring 0 use gpu addr 0x000000f5ff400040, cpu addr 0x        (ptrval)
[    1.074410] amdgpu 0000:09:00.0: fence driver on ring 1 use gpu addr 0x000000f5ff4000c0, cpu addr 0x        (ptrval)
[    1.074448] amdgpu 0000:09:00.0: fence driver on ring 2 use gpu addr 0x000000f5ff400140, cpu addr 0x        (ptrval)
[    1.074484] amdgpu 0000:09:00.0: fence driver on ring 3 use gpu addr 0x000000f5ff4001c0, cpu addr 0x        (ptrval)
[    1.074532] amdgpu 0000:09:00.0: fence driver on ring 4 use gpu addr 0x000000f5ff400240, cpu addr 0x        (ptrval)
[    1.074565] amdgpu 0000:09:00.0: fence driver on ring 5 use gpu addr 0x000000f5ff4002c0, cpu addr 0x        (ptrval)
[    1.074597] amdgpu 0000:09:00.0: fence driver on ring 6 use gpu addr 0x000000f5ff400340, cpu addr 0x        (ptrval)
[    1.074631] amdgpu 0000:09:00.0: fence driver on ring 7 use gpu addr 0x000000f5ff4003c0, cpu addr 0x        (ptrval)
[    1.074667] amdgpu 0000:09:00.0: fence driver on ring 8 use gpu addr 0x000000f5ff400440, cpu addr 0x        (ptrval)
[    1.074686] amdgpu 0000:09:00.0: fence driver on ring 9 use gpu addr 0x000000f5ff4004e0, cpu addr 0x        (ptrval)
[    1.075063] amdgpu 0000:09:00.0: fence driver on ring 10 use gpu addr 0x000000f5ff400560, cpu addr 0x        (ptrval)
[    1.075098] amdgpu 0000:09:00.0: fence driver on ring 11 use gpu addr 0x000000f5ff4005e0, cpu addr 0x        (ptrval)
[    1.075645] amdgpu 0000:09:00.0: fence driver on ring 12 use gpu addr 0x000000f4008fba80, cpu addr 0x        (ptrval)
[    1.075677] amdgpu 0000:09:00.0: fence driver on ring 13 use gpu addr 0x000000f5ff4006e0, cpu addr 0x        (ptrval)
[    1.075705] amdgpu 0000:09:00.0: fence driver on ring 14 use gpu addr 0x000000f5ff400760, cpu addr 0x        (ptrval)
[    1.075781] amdgpu 0000:09:00.0: fence driver on ring 15 use gpu addr 0x000000f5ff4007e0, cpu addr 0x        (ptrval)
[    1.075810] amdgpu 0000:09:00.0: fence driver on ring 16 use gpu addr 0x000000f5ff400860, cpu addr 0x        (ptrval)
[    1.075839] amdgpu 0000:09:00.0: fence driver on ring 17 use gpu addr 0x000000f5ff4008e0, cpu addr 0x        (ptrval)
[    1.711914] fbcon: amdgpudrmfb (fb0) is primary device
[    1.711974] amdgpu 0000:09:00.0: fb0: amdgpudrmfb frame buffer device
[    1.724226] amdgpu 0000:09:00.0: ring 0(gfx) uses VM inv eng 4 on hub 0
[    1.724229] amdgpu 0000:09:00.0: ring 1(comp_1.0.0) uses VM inv eng 5 on hub 0
[    1.724230] amdgpu 0000:09:00.0: ring 2(comp_1.1.0) uses VM inv eng 6 on hub 0
[    1.724231] amdgpu 0000:09:00.0: ring 3(comp_1.2.0) uses VM inv eng 7 on hub 0
[    1.724233] amdgpu 0000:09:00.0: ring 4(comp_1.3.0) uses VM inv eng 8 on hub 0
[    1.724234] amdgpu 0000:09:00.0: ring 5(comp_1.0.1) uses VM inv eng 9 on hub 0
[    1.724235] amdgpu 0000:09:00.0: ring 6(comp_1.1.1) uses VM inv eng 10 on hub 0
[    1.724236] amdgpu 0000:09:00.0: ring 7(comp_1.2.1) uses VM inv eng 11 on hub 0
[    1.724237] amdgpu 0000:09:00.0: ring 8(comp_1.3.1) uses VM inv eng 12 on hub 0
[    1.724239] amdgpu 0000:09:00.0: ring 9(kiq_2.1.7) uses VM inv eng 13 on hub 0
[    1.724240] amdgpu 0000:09:00.0: ring 10(sdma0) uses VM inv eng 4 on hub 1
[    1.724242] amdgpu 0000:09:00.0: ring 11(sdma1) uses VM inv eng 5 on hub 1
[    1.724243] amdgpu 0000:09:00.0: ring 12(uvd) uses VM inv eng 6 on hub 1
[    1.724244] amdgpu 0000:09:00.0: ring 13(uvd_enc0) uses VM inv eng 7 on hub 1
[    1.724245] amdgpu 0000:09:00.0: ring 14(uvd_enc1) uses VM inv eng 8 on hub 1
[    1.724247] amdgpu 0000:09:00.0: ring 15(vce0) uses VM inv eng 9 on hub 1
[    1.724248] amdgpu 0000:09:00.0: ring 16(vce1) uses VM inv eng 10 on hub 1
[    1.724249] amdgpu 0000:09:00.0: ring 17(vce2) uses VM inv eng 11 on hub 1
[    1.724811] amdgpu 0000:09:00.0: kfd not supported on this ASIC
[    1.724822] [drm] Initialized amdgpu 3.23.0 20150101 for 0000:09:00.0 on minor 0
[    4.026835] EDAC amd64: Node 0: DRAM ECC disabled.
[    4.026837] EDAC amd64: ECC disabled in the BIOS or no ECC capab


I am waiting for your help. Thanks.

