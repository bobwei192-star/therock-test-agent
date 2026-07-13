# End user Issue - Kernel driver not installed after kernel os update 

- **Issue #:** 420
- **State:** closed
- **Created:** 2018-05-17T15:54:32Z
- **Updated:** 2018-10-01T13:20:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/420

I am running debian/sid with a vega 56, a threadripper 1950x, and a ASUS X399 motherboard. Until recently rocm ran fine on kernel 4.13, but then it suddenly stopped (I may have updated something, I am unsure). I traced the problem to it not loading in the amdgpu module, and switched to a newer kernel with amdgpu, but unsurprisingly rocm wouldn't build for it.

I would like to see if I can get it working again. The module for kernel 4.13 builds fine (it fails in all other kernels I have tested), but when I run clinfo, I get the following output:

    Number of platforms                               0

I get no indication of errors from dmesg:

    # dmesg | grep -i 'amdgpu'
    [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-17-generic root=UUID=408b6525-14cb-4ae4-bb32-d932d53d805c ro tsc=unstable nohz=off amdgpu.vm_fragment_size=9
    [    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.13.0-17-generic root=UUID=408b6525-14cb-4ae4-bb32-d932d53d805c ro tsc=unstable nohz=off amdgpu.vm_fragment_size=9
    [   12.591048] [drm] amdgpu kernel modesetting enabled.
    [   12.636328] fb: switching to amdgpudrmfb from EFI VGA
    [   12.637416] [drm] add ip block number 4 <amdgpu_powerplay>
    [   12.839252] amdgpu 0000:43:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
    [   12.839299] amdgpu 0000:43:00.0: VRAM: 8176M 0x000000F400000000 - 0x000000F5FEFFFFFF (8176M used)
    [   12.839303] amdgpu 0000:43:00.0: GTT: 256M 0x000000F600000000 - 0x000000F60FFFFFFF
    [   12.839505] [drm] amdgpu: 8176M of VRAM memory ready
    [   12.839508] [drm] amdgpu: 48218M of GTT memory ready.
    [   13.966710] fbcon: amdgpudrmfb (fb0) is primary device
    [   14.052300] amdgpu 0000:43:00.0: fb0: amdgpudrmfb frame buffer device
    [   14.088131] amdgpu 0000:43:00.0: ring 0(gfx) uses VM inv eng 4 on hub 0
    [   14.088148] amdgpu 0000:43:00.0: ring 1(comp_1.0.0) uses VM inv eng 5 on hub 0
    [   14.088163] amdgpu 0000:43:00.0: ring 2(comp_1.1.0) uses VM inv eng 6 on hub 0
    [   14.088178] amdgpu 0000:43:00.0: ring 3(comp_1.2.0) uses VM inv eng 7 on hub 0
    [   14.088193] amdgpu 0000:43:00.0: ring 4(comp_1.3.0) uses VM inv eng 8 on hub 0
    [   14.088208] amdgpu 0000:43:00.0: ring 5(comp_1.0.1) uses VM inv eng 9 on hub 0
    [   14.088223] amdgpu 0000:43:00.0: ring 6(comp_1.1.1) uses VM inv eng 10 on hub 0
    [   14.088239] amdgpu 0000:43:00.0: ring 7(comp_1.2.1) uses VM inv eng 11 on hub 0
    [   14.088254] amdgpu 0000:43:00.0: ring 8(comp_1.3.1) uses VM inv eng 12 on hub 0
    [   14.088269] amdgpu 0000:43:00.0: ring 9(kiq_2.1.0) uses VM inv eng 13 on hub 0
    [   14.088284] amdgpu 0000:43:00.0: ring 10(sdma0) uses VM inv eng 4 on hub 1
    [   14.088299] amdgpu 0000:43:00.0: ring 11(sdma1) uses VM inv eng 5 on hub 1
    [   14.088313] amdgpu 0000:43:00.0: ring 12(uvd) uses VM inv eng 6 on hub 1
    [   14.088327] amdgpu 0000:43:00.0: ring 13(uvd_enc0) uses VM inv eng 7 on hub 1
    [   14.088342] amdgpu 0000:43:00.0: ring 14(uvd_enc1) uses VM inv eng 8 on hub 1
    [   14.088357] amdgpu 0000:43:00.0: ring 15(vce0) uses VM inv eng 9 on hub 1
    [   14.088371] amdgpu 0000:43:00.0: ring 16(vce1) uses VM inv eng 10 on hub 1
    [   14.088385] amdgpu 0000:43:00.0: ring 17(vce2) uses VM inv eng 11 on hub 1
    [   14.089244] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:43:00.0 on minor 0



I appreciate this is quite vague, so feel free to ask for any more info.