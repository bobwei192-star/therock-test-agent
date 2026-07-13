# ROCm system lock-up

- **Issue #:** 240
- **State:** closed
- **Created:** 2017-10-28T09:56:18Z
- **Updated:** 2018-06-03T15:19:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/240

ROCm 1.6-180, Ubuntu 16.04, R9-Nano.

I get a system lockup with the trace below. I'm not exactly sure of the cause. It may be related to attempting to write (from the host side) to a buffer with CL_MEM_HOST_NO_ACCESS. The write operation itself fails with error -59, and this is all fine, but immediately after I get the lockup.

```
Oct 28 20:40:22 trei kernel: [  600.138009] [TTM] Failed allocating page table
Oct 28 20:40:22 trei kernel: [  600.138020] kfd2kgd: Failed to create BO on domain CPU. ret -12
Oct 28 20:40:23 trei kernel: [  600.674620] BUG: unable to handle kernel NULL pointer dereference at 00000000000000b8
Oct 28 20:40:23 trei kernel: [  600.674685] IP: drm_mm_remove_node+0x2ba/0x2f0 [drm]
Oct 28 20:40:23 trei kernel: [  600.674702] PGD 0 
Oct 28 20:40:23 trei kernel: [  600.674702] 
Oct 28 20:40:23 trei kernel: [  600.674717] Oops: 0002 [#1] SMP
Oct 28 20:40:23 trei kernel: [  600.674728] Modules linked in: intel_rapl sb_edac edac_core x86_pkg_temp_thermal intel_powerclamp coretemp snd_hda_codec_realtek kvm snd_hda_codec_generic irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_codec_hdmi cryptd snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm input_leds snd_seq_midi snd_seq_midi_event snd_rawmidi snd_seq snd_seq_device snd_timer snd soundcore lpc_ich shpchp ioatdma acpi_power_meter mac_hid parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu mxm_wmi ttm drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops drm igb dca ptp pps_core ahci i2c_algo_bit libahci wmi
Oct 28 20:40:23 trei kernel: [  600.674931] CPU: 13 PID: 1204 Comm: Xorg Not tainted 4.11.0-kfd-compute-rocm-rel-1.6-180 #1
Oct 28 20:40:23 trei kernel: [  600.674957] Hardware name: Supermicro X10DAi/X10DAI, BIOS 2.0 02/02/2016
Oct 28 20:40:23 trei kernel: [  600.674978] task: ffff8883b44f6200 task.stack: ffff9f77cdf28000
Oct 28 20:40:23 trei kernel: [  600.675008] RIP: 0010:drm_mm_remove_node+0x2ba/0x2f0 [drm]
Oct 28 20:40:23 trei kernel: [  600.675025] RSP: 0018:ffff9f77cdf2bb98 EFLAGS: 00010246
Oct 28 20:40:23 trei kernel: [  600.675042] RAX: 0000000000000000 RBX: ffffffffffffffe0 RCX: 0000000000000000
Oct 28 20:40:23 trei kernel: [  600.675064] RDX: 0000000000000000 RSI: 00000000000000b8 RDI: 0000000000000000
Oct 28 20:40:23 trei kernel: [  600.675085] RBP: ffff9f77cdf2bbb8 R08: 00000000000fcb86 R09: ffff88837ea05d60
Oct 28 20:40:23 trei kernel: [  600.675107] R10: ffff88839383d9c0 R11: 0000000000000000 R12: ffff88837ea05d20
Oct 28 20:40:23 trei kernel: [  600.675128] R13: 0000000000000000 R14: 0000000000000000 R15: 000000000000000e
Oct 28 20:40:23 trei kernel: [  600.675151] FS:  00007f5131d58a00(0000) GS:ffff8883ffd40000(0000) knlGS:0000000000000000
Oct 28 20:40:23 trei kernel: [  600.675175] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Oct 28 20:40:23 trei kernel: [  600.675192] CR2: 00000000000000b8 CR3: 0000001033a30000 CR4: 00000000001406e0
Oct 28 20:40:23 trei kernel: [  600.675214] Call Trace:
Oct 28 20:40:23 trei kernel: [  600.675296]  amdgpu_vram_mgr_del+0x4f/0x80 [amdgpu]
Oct 28 20:40:23 trei kernel: [  600.675319]  ttm_bo_cleanup_memtype_use+0x61/0x70 [ttm]
Oct 28 20:40:23 trei kernel: [  600.675338]  ttm_bo_release+0x1c9/0x200 [ttm]
Oct 28 20:40:23 trei kernel: [  600.675374]  ? amdgpu_gem_object_close+0xd9/0x1b0 [amdgpu]
Oct 28 20:40:23 trei kernel: [  600.675395]  ttm_bo_unref+0x2c/0x30 [ttm]
Oct 28 20:40:23 trei kernel: [  600.675428]  amdgpu_bo_unref+0x2a/0x50 [amdgpu]
Oct 28 20:40:23 trei kernel: [  600.675473]  amdgpu_gem_object_free+0xa1/0xc0 [amdgpu]
Oct 28 20:40:23 trei kernel: [  600.675500]  drm_gem_object_free+0x29/0x70 [drm]
Oct 28 20:40:23 trei kernel: [  600.675520]  drm_gem_object_unreference_unlocked+0x40/0x70 [drm]
Oct 28 20:40:23 trei kernel: [  600.675545]  drm_gem_object_handle_unreference_unlocked+0x66/0xb0 [drm]
Oct 28 20:40:23 trei kernel: [  600.675571]  drm_gem_object_release_handle+0x53/0x90 [drm]
Oct 28 20:40:23 trei kernel: [  600.675594]  drm_gem_handle_delete+0x5e/0x90 [drm]
Oct 28 20:40:23 trei kernel: [  600.675615]  drm_gem_close_ioctl+0x20/0x30 [drm]
Oct 28 20:40:23 trei kernel: [  600.675636]  drm_ioctl+0x1fc/0x450 [drm]
Oct 28 20:40:23 trei kernel: [  600.675654]  ? drm_gem_handle_create+0x40/0x40 [drm]
Oct 28 20:40:23 trei kernel: [  600.675673]  ? dentry_free+0x4e/0x90
Oct 28 20:40:23 trei kernel: [  600.675702]  amdgpu_drm_ioctl+0x4c/0x80 [amdgpu]
Oct 28 20:40:23 trei kernel: [  600.675721]  do_vfs_ioctl+0x92/0x5a0
Oct 28 20:40:23 trei kernel: [  600.675735]  ? ____fput+0xe/0x10
Oct 28 20:40:23 trei kernel: [  600.675748]  ? task_work_run+0x83/0xa0
Oct 28 20:40:23 trei kernel: [  600.675762]  SyS_ioctl+0x79/0x90
Oct 28 20:40:23 trei kernel: [  600.675778]  entry_SYSCALL_64_fastpath+0x1e/0xad
Oct 28 20:40:23 trei kernel: [  600.675793] RIP: 0033:0x7f512f781f07
Oct 28 20:40:23 trei kernel: [  600.675805] RSP: 002b:00007ffee1de81a8 EFLAGS: 00003246 ORIG_RAX: 0000000000000010
Oct 28 20:40:23 trei kernel: [  600.675829] RAX: ffffffffffffffda RBX: 000055558a82b8d0 RCX: 00007f512f781f07
Oct 28 20:40:23 trei kernel: [  600.675852] RDX: 00007ffee1de81e0 RSI: 0000000040086409 RDI: 000000000000000e
Oct 28 20:40:23 trei kernel: [  600.675873] RBP: 00007ffee1de81e0 R08: 0000000000000000 R09: 0000000000000000
Oct 28 20:40:23 trei kernel: [  600.675895] R10: 0000000000001000 R11: 0000000000003246 R12: 0000000040086409
Oct 28 20:40:23 trei kernel: [  600.675917] R13: 000000000000000e R14: 000055558ac988c0 R15: 0000555589e73120
Oct 28 20:40:23 trei kernel: [  600.675940] Code: 10 e9 94 fe ff ff 49 8b 84 24 88 00 00 00 4c 8b 41 08 49 89 ca 48 89 41 48 48 89 c8 e9 44 fe ff ff 83 e2 01 75 c9 e9 82 fe ff ff <49> 89 8e b8 00 00 00 e9 67 ff ff ff 48 89 4f 10 e9 5e ff ff ff 
Oct 28 20:40:23 trei kernel: [  600.676028] RIP: drm_mm_remove_node+0x2ba/0x2f0 [drm] RSP: ffff9f77cdf2bb98
Oct 28 20:40:23 trei kernel: [  600.676050] CR2: 00000000000000b8
Oct 28 20:40:23 trei kernel: [  600.691427] ---[ end trace aab7b76101919961 ]---
```