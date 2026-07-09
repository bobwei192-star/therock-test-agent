# Using KVM via  a PCIe Passthrough environment  vega10/rocm1.9 results in  "amdgpu: probe of 0000:00:09.0 failed with error -22"

- **Issue #:** 545
- **State:** closed
- **Created:** 2018-09-17T14:34:49Z
- **Updated:** 2019-02-08T17:22:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/545

Hi!

I am trying to run the latest release of ROCm on clean Ubuntu 18.04LTE (4.15.0-29-generic). I am working with VM and vega10 device (mi25) passedthrough to it (qemu-kvm, vfio).

After installing rocm-dkms and trying to modprobe updated amdgpu I got the following output in the dmesg: 

```
[  295.006250] [drm] initializing kernel modesetting (VEGA10 0x1002:0x6860 0x1002:0x6C75 0x01).
[  295.006265] [drm] register mmio base: 0xFC080000
[  295.006266] [drm] register mmio size: 524288
[  295.006294] [drm] add ip block number 0 <soc15_common>
[  295.006295] [drm] add ip block number 1 <gmc_v9_0>
[  295.006296] [drm] add ip block number 2 <vega10_ih>
[  295.006296] [drm] add ip block number 3 <psp>
[  295.006297] [drm] add ip block number 4 <powerplay>
[  295.006298] [drm] add ip block number 5 <dm>
[  295.006299] [drm] add ip block number 6 <gfx_v9_0>
[  295.006300] [drm] add ip block number 7 <sdma_v4_0>
[  295.006300] [drm] add ip block number 8 <uvd_v7_0>
[  295.006301] [drm] add ip block number 9 <vce_v4_0>
[  295.009878] [drm] UVD(0) is enabled in VM mode
[  295.009879] [drm] UVD(0) ENC is enabled in VM mode
[  295.009880] [drm] VCE enabled in VM mode
[  295.066693] ATOM BIOS: 113-D0512100-RC1
[  295.066705] [drm] GPU posting now...
[  300.128068] [drm:atom_op_jump [amdgpu]] *ERROR* atombios stuck in loop for more than 5secs aborting
[  300.128131] [drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing D156 (len 275, WS 16, PS 4) @ 0xD258
[  300.128190] [drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing A712 (len 192, WS 8, PS 4) @ 0xA7C5
[  300.128247] [drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing 9B24 (len 323, WS 0, PS 8) @ 0x9B7A
[  300.128251] amdgpu 0000:00:09.0: gpu post error!
[  300.128253] amdgpu 0000:00:09.0: Fatal error during GPU init
[  300.149609] [drm] amdgpu: finishing device.
[  300.182212] amdgpu: probe of 0000:00:09.0 failed with error -22
```
Does ROCm works with 4.15.0-29-generic kernel? Or I have to install newer one?
Would appreciate any help! Thank you!

Best, 
   Alex

UPD: the same issue with Ubuntu 18.04lte on the host machine...