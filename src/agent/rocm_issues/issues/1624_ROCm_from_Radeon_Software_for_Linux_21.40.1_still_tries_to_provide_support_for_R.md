# ROCm from Radeon Software for Linux 21.40.1 still tries to provide support for R9 390X (gfx7) and wrecks the kernel

> **Issue #1624**
> **状态**: closed
> **创建时间**: 2021-11-22T21:52:01Z
> **更新时间**: 2023-04-10T01:58:29Z
> **关闭时间**: 2023-04-10T01:58:29Z
> **作者**: illwieckz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1624

## 描述

I tried this week to run ROCm with Hawaii on a Threadripper PRO based computer, installing ROCm from “Radeon™ Software for Linux® version 21.40.1 for Ubuntu 20.04.3”:

https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-40-1

I was not expecting to get OpenCL to be provided, I was just curious about it, but I was expecting to not get my kernel wrecked and require me to reboot.

It looks like the Hawaii (GFX7) broken support is still provided with current ROCm, and it puts the kernel in a so badly state the user is asked to reboot.

This means, for example, that an user cannot host both a Radeon R9 390X running Orca and a newer card like an Radeon PRO W6600 on the same system: the ROCm driver will break the kernel because of trying to provide support to R9 390X.

Abstract from `dmesg`:

```
[109115.055092] WARNING: CPU: 15 PID: 1860426 at drivers/gpu/drm/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:362 create_queue_nocpsch+0x5d6/0x610 [amdgpu]
[109115.055275] RIP: 0010:create_queue_nocpsch+0x5d6/0x610 [amdgpu]
[109131.437666] Fixing recursive fault but reboot is needed!
```

Whole error log from `dmesg`:

```
[109115.055056] ------------[ cut here ]------------
[109115.055058] Load non-HWS mqd while stopped
[109115.055092] WARNING: CPU: 15 PID: 1860426 at drivers/gpu/drm/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:362 create_queue_nocpsch+0x5d6/0x610 [amdgpu]
[109115.055219] Modules linked in: ufs qnx4 hfsplus hfs minix ntfs msdos jfs xfs cpuid cdc_ether usbnet mii drivetemp nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_hda_intel intel_rapl_msr snd_intel_dspcfg intel_rapl_common snd_intel_sdw_acpi amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usb_audio videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 snd_hda_core snd_usbmidi_lib kvm_amd videobuf2_common snd_hwdep snd_seq_midi joydev input_leds videodev kvm mc snd_pcm snd_seq_midi_event rapl efi_pstore snd_rawmidi snd_seq snd_seq_device snd_timer snd ipmi_si soundcore ipmi_devintf ccp ipmi_msghandler k10temp mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr parport_pc auth_rpcgss nfs_acl ppdev lockd lp grace parport sunrpc ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[109115.055254]  bcache crc64 hid_generic usbhid hid amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper drm_ttm_helper ttm crct10dif_pclmul crc32_pclmul drm_kms_helper ghash_clmulni_intel aesni_intel syscopyarea sysfillrect sysimgblt crypto_simd fb_sys_fops cryptd cec ixgbe rc_core igb xfrm_algo drm dca i2c_algo_bit mdio ahci libahci xhci_pci xhci_pci_renesas i2c_piix4 [last unloaded: acpi_ipmi]
[109115.055272] CPU: 15 PID: 1860426 Comm: clinfo Tainted: G           OE     5.13.0-21-generic #21-Ubuntu
[109115.055274] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[109115.055275] RIP: 0010:create_queue_nocpsch+0x5d6/0x610 [amdgpu]
[109115.055384] Code: c7 c6 b8 b4 f1 c0 48 c7 c7 e8 dc fa c0 e8 42 49 e0 e2 e9 70 ff ff ff 48 c7 c7 18 b5 f1 c0 c6 05 85 16 3d 00 01 e8 29 4c 3f e3 <0f> 0b e9 63 fd ff ff 48 c7 c7 38 b5 f1 c0 e8 16 4c 3f e3 0f 0b b8
[109115.055385] RSP: 0018:ffffb39963edbc00 EFLAGS: 00010286
[109115.055387] RAX: 0000000000000000 RBX: ffff90a872414400 RCX: 0000000000000027
[109115.055388] RDX: ffff90c73d5d89c8 RSI: 0000000000000001 RDI: ffff90c73d5d89c0
[109115.055389] RBP: ffffb39963edbc50 R08: 0000000000000000 R09: ffffb39963edb9f0
[109115.055389] R10: ffffb39963edb9e8 R11: ffff90c73d186d40 R12: ffff90b11c45fc00
[109115.055390] R13: 0000000000000000 R14: ffff90b17dcc8410 R15: ffff90a872ee6300
[109115.055392] FS:  00007f758c717b80(0000) GS:ffff90c73d5c0000(0000) knlGS:0000000000000000
[109115.055393] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[109115.055394] CR2: 00007f75683c4be0 CR3: 00000009dae1e000 CR4: 0000000000350ee0
[109115.055395] Call Trace:
[109115.055398]  pqm_create_queue+0x1c0/0x490 [amdgpu]
[109115.055503]  kfd_ioctl_create_queue+0xd3/0x2c0 [amdgpu]
[109115.055607]  kfd_ioctl+0x335/0x480 [amdgpu]
[109115.055708]  ? kfd_ioctl_dbg_address_watch+0x190/0x190 [amdgpu]
[109115.055807]  ? do_syscall_64+0x6e/0xb0
[109115.055811]  __x64_sys_ioctl+0x91/0xc0
[109115.055813]  do_syscall_64+0x61/0xb0
[109115.055815]  ? exit_to_user_mode_prepare+0x95/0xb0
[109115.055817]  ? syscall_exit_to_user_mode+0x27/0x50
[109115.055819]  ? do_syscall_64+0x6e/0xb0
[109115.055821]  ? do_syscall_64+0x6e/0xb0
[109115.055822]  ? do_syscall_64+0x6e/0xb0
[109115.055823]  entry_SYSCALL_64_after_hwframe+0x44/0xae
[109115.055825] RIP: 0033:0x7f758c83b9cb
[109115.055827] Code: ff ff ff 85 c0 79 8b 49 c7 c4 ff ff ff ff 5b 5d 4c 89 e0 41 5c c3 66 0f 1f 84 00 00 00 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 35 a4 0f 00 f7 d8 64 89 01 48
[109115.055828] RSP: 002b:00007ffc6bc72f98 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[109115.055830] RAX: ffffffffffffffda RBX: 0000000000000000 RCX: 00007f758c83b9cb
[109115.055830] RDX: 00007ffc6bc73010 RSI: 00000000c0584b02 RDI: 000000000000000b
[109115.055831] RBP: 00007ffc6bc73010 R08: 00007f7568467a00 R09: 0000000000080000
[109115.055832] R10: 0000000001100000 R11: 0000000000000246 R12: 00000000c0584b02
[109115.055833] R13: 000000000000000b R14: 0000000000000064 R15: 00007ffc6bc733f0
[109115.055835] ---[ end trace 61c4a29900fbfe5c ]---
[109131.391806] ------------[ cut here ]------------
[109131.391810] Evict when stopped
[109131.391856] WARNING: CPU: 3 PID: 1860476 at drivers/gpu/drm/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:674 evict_process_queues_nocpsch+0x1ce/0x1e0 [amdgpu]
[109131.392094] Modules linked in: ufs qnx4 hfsplus hfs minix ntfs msdos jfs xfs cpuid cdc_ether usbnet mii drivetemp nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_hda_intel intel_rapl_msr snd_intel_dspcfg intel_rapl_common snd_intel_sdw_acpi amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usb_audio videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 snd_hda_core snd_usbmidi_lib kvm_amd videobuf2_common snd_hwdep snd_seq_midi joydev input_leds videodev kvm mc snd_pcm snd_seq_midi_event rapl efi_pstore snd_rawmidi snd_seq snd_seq_device snd_timer snd ipmi_si soundcore ipmi_devintf ccp ipmi_msghandler k10temp mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr parport_pc auth_rpcgss nfs_acl ppdev lockd lp grace parport sunrpc ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[109131.392160]  bcache crc64 hid_generic usbhid hid amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper drm_ttm_helper ttm crct10dif_pclmul crc32_pclmul drm_kms_helper ghash_clmulni_intel aesni_intel syscopyarea sysfillrect sysimgblt crypto_simd fb_sys_fops cryptd cec ixgbe rc_core igb xfrm_algo drm dca i2c_algo_bit mdio ahci libahci xhci_pci xhci_pci_renesas i2c_piix4 [last unloaded: acpi_ipmi]
[109131.392190] CPU: 3 PID: 1860476 Comm: clinfo:sh10 Tainted: G        W  OE     5.13.0-21-generic #21-Ubuntu
[109131.392195] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[109131.392197] RIP: 0010:evict_process_queues_nocpsch+0x1ce/0x1e0 [amdgpu]
[109131.392416] Code: 41 5c 41 5d 41 5e 41 5f 5d c3 80 3d 0e 21 3d 00 00 0f 85 20 ff ff ff 48 c7 c7 b4 30 f6 c0 c6 05 fa 20 3d 00 01 e8 a1 56 3f e3 <0f> 0b e9 06 ff ff ff 66 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 44 00
[109131.392418] RSP: 0018:ffffb39964663ad0 EFLAGS: 00010286
[109131.392422] RAX: 0000000000000000 RBX: ffff90b11c45fc00 RCX: 0000000000000027
[109131.392424] RDX: ffff90c73d2d89c8 RSI: 0000000000000001 RDI: ffff90c73d2d89c0
[109131.392426] RBP: ffffb39964663b00 R08: 0000000000000000 R09: ffffb399646638c0
[109131.392427] R10: ffffb399646638b8 R11: ffff90c73d187298 R12: ffff90a872414400
[109131.392429] R13: ffff90b17dcc8410 R14: ffff90b17dcc8420 R15: 0000000000000000
[109131.392431] FS:  0000000000000000(0000) GS:ffff90c73d2c0000(0000) knlGS:0000000000000000
[109131.392433] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[109131.392435] CR2: 00007f3cf9117fb2 CR3: 00000009dae1e000 CR4: 0000000000350ee0
[109131.392438] Call Trace:
[109131.392441]  kfd_process_evict_queues+0x3e/0x70 [amdgpu]
[109131.392657]  kgd2kfd_quiesce_mm+0x2b/0x70 [amdgpu]
[109131.392867]  amdgpu_amdkfd_evict_userptr+0x3b/0x70 [amdgpu]
[109131.393080]  amdgpu_mn_invalidate_hsa+0x49/0x60 [amdgpu]
[109131.393291]  __mmu_notifier_release+0x196/0x1f0
[109131.393297]  exit_mmap+0x15e/0x1f0
[109131.393300]  ? exit_robust_list+0x5c/0x130
[109131.393305]  ? __cond_resched+0x1a/0x50
[109131.393310]  ? mutex_lock+0x13/0x40
[109131.393313]  mmput+0x5f/0x140
[109131.393317]  exit_mm+0x169/0x1e0
[109131.393320]  do_exit+0x1b4/0x3d0
[109131.393323]  do_group_exit+0x3b/0xb0
[109131.393326]  get_signal+0x16b/0x8b0
[109131.393331]  arch_do_signal_or_restart+0xd9/0x100
[109131.393335]  ? do_futex+0x12c/0x1d0
[109131.393338]  ? __x64_sys_futex+0x78/0x1e0
[109131.393342]  exit_to_user_mode_loop+0xc4/0x160
[109131.393345]  exit_to_user_mode_prepare+0x9f/0xb0
[109131.393347]  syscall_exit_to_user_mode+0x27/0x50
[109131.393351]  do_syscall_64+0x6e/0xb0
[109131.393354]  ? do_syscall_64+0x6e/0xb0
[109131.393356]  ? exit_to_user_mode_prepare+0x37/0xb0
[109131.393358]  ? irqentry_exit_to_user_mode+0x9/0x20
[109131.393362]  ? irqentry_exit+0x19/0x30
[109131.393365]  ? exc_page_fault+0x8f/0x170
[109131.393368]  ? asm_exc_page_fault+0x8/0x30
[109131.393371]  entry_SYSCALL_64_after_hwframe+0x44/0xae
[109131.393375] RIP: 0033:0x7f758c7b2ff9
[109131.393377] Code: Unable to access opcode bytes at RIP 0x7f758c7b2fcf.
[109131.393379] RSP: 002b:00007f74bd7f9bc0 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
[109131.393382] RAX: fffffffffffffe00 RBX: 0000000000000000 RCX: 00007f758c7b2ff9
[109131.393383] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055e00f0a2070
[109131.393385] RBP: 0000000000000000 R08: 0000000000000000 R09: 00000000ffffffff
[109131.393387] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[109131.393388] R13: 000055e00f0a2020 R14: 0000000000000000 R15: 000055e00f0a2070
[109131.393391] ---[ end trace 61c4a29900fbfe5d ]---
[109131.393424] ------------[ cut here ]------------
[109131.393425] Destroy non-HWS queue while stopped
[109131.393443] WARNING: CPU: 3 PID: 1860476 at drivers/gpu/drm/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:478 destroy_queue_nocpsch_locked+0x146/0x1d0 [amdgpu]
[109131.393677] Modules linked in: ufs qnx4 hfsplus hfs minix ntfs msdos jfs xfs cpuid cdc_ether usbnet mii drivetemp nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_hda_intel intel_rapl_msr snd_intel_dspcfg intel_rapl_common snd_intel_sdw_acpi amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usb_audio videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 snd_hda_core snd_usbmidi_lib kvm_amd videobuf2_common snd_hwdep snd_seq_midi joydev input_leds videodev kvm mc snd_pcm snd_seq_midi_event rapl efi_pstore snd_rawmidi snd_seq snd_seq_device snd_timer snd ipmi_si soundcore ipmi_devintf ccp ipmi_msghandler k10temp mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr parport_pc auth_rpcgss nfs_acl ppdev lockd lp grace parport sunrpc ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[109131.393753]  bcache crc64 hid_generic usbhid hid amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper drm_ttm_helper ttm crct10dif_pclmul crc32_pclmul drm_kms_helper ghash_clmulni_intel aesni_intel syscopyarea sysfillrect sysimgblt crypto_simd fb_sys_fops cryptd cec ixgbe rc_core igb xfrm_algo drm dca i2c_algo_bit mdio ahci libahci xhci_pci xhci_pci_renesas i2c_piix4 [last unloaded: acpi_ipmi]
[109131.393777] CPU: 3 PID: 1860476 Comm: clinfo:sh10 Tainted: G        W  OE     5.13.0-21-generic #21-Ubuntu
[109131.393780] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[109131.393781] RIP: 0010:destroy_queue_nocpsch_locked+0x146/0x1d0 [amdgpu]
[109131.393990] Code: 44 89 f0 41 5c 41 5d 41 5e 5d c3 45 31 f6 80 3d 34 29 3d 00 00 75 e8 48 c7 c7 c0 b2 f1 c0 c6 05 24 29 3d 00 01 e8 c9 5e 3f e3 <0f> 0b eb d1 4d 8b b4 24 b8 00 00 00 85 d2 0f 84 e3 fe ff ff 48 89
[109131.393993] RSP: 0018:ffffb39964663ad0 EFLAGS: 00010286
[109131.393995] RAX: 0000000000000000 RBX: ffff90b11c45fc00 RCX: 0000000000000027
[109131.393998] RDX: ffff90c73d2d89c8 RSI: 0000000000000001 RDI: ffff90c73d2d89c0
[109131.394000] RBP: ffffb39964663af0 R08: 0000000000000000 R09: ffffb399646638c0
[109131.394001] R10: ffffb399646638b8 R11: ffff90c73d1877d8 R12: ffff90a872414400
[109131.394003] R13: ffff90b17dcc8410 R14: 0000000000000000 R15: ffff90a872414400
[109131.394005] FS:  0000000000000000(0000) GS:ffff90c73d2c0000(0000) knlGS:0000000000000000
[109131.394008] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[109131.394010] CR2: 00007f3cf9117fb2 CR3: 00000009dae1e000 CR4: 0000000000350ee0
[109131.394012] Call Trace:
[109131.394014]  process_termination_nocpsch+0x9f/0x1e0 [amdgpu]
[109131.394224]  kfd_process_dequeue_from_all_devices+0x49/0x70 [amdgpu]
[109131.394431]  kfd_process_notifier_release+0xf2/0x160 [amdgpu]
[109131.394639]  __mmu_notifier_release+0x74/0x1f0
[109131.394643]  exit_mmap+0x15e/0x1f0
[109131.394645]  ? exit_robust_list+0x5c/0x130
[109131.394649]  ? __cond_resched+0x1a/0x50
[109131.394653]  ? mutex_lock+0x13/0x40
[109131.394656]  mmput+0x5f/0x140
[109131.394660]  exit_mm+0x169/0x1e0
[109131.394663]  do_exit+0x1b4/0x3d0
[109131.394666]  do_group_exit+0x3b/0xb0
[109131.394669]  get_signal+0x16b/0x8b0
[109131.394673]  arch_do_signal_or_restart+0xd9/0x100
[109131.394676]  ? do_futex+0x12c/0x1d0
[109131.394680]  ? __x64_sys_futex+0x78/0x1e0
[109131.394684]  exit_to_user_mode_loop+0xc4/0x160
[109131.394686]  exit_to_user_mode_prepare+0x9f/0xb0
[109131.394689]  syscall_exit_to_user_mode+0x27/0x50
[109131.394692]  do_syscall_64+0x6e/0xb0
[109131.394695]  ? do_syscall_64+0x6e/0xb0
[109131.394697]  ? exit_to_user_mode_prepare+0x37/0xb0
[109131.394700]  ? irqentry_exit_to_user_mode+0x9/0x20
[109131.394703]  ? irqentry_exit+0x19/0x30
[109131.394707]  ? exc_page_fault+0x8f/0x170
[109131.394710]  ? asm_exc_page_fault+0x8/0x30
[109131.394712]  entry_SYSCALL_64_after_hwframe+0x44/0xae
[109131.394716] RIP: 0033:0x7f758c7b2ff9
[109131.394718] Code: Unable to access opcode bytes at RIP 0x7f758c7b2fcf.
[109131.394720] RSP: 002b:00007f74bd7f9bc0 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
[109131.394722] RAX: fffffffffffffe00 RBX: 0000000000000000 RCX: 00007f758c7b2ff9
[109131.394724] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055e00f0a2070
[109131.394726] RBP: 0000000000000000 R08: 0000000000000000 R09: 00000000ffffffff
[109131.394727] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[109131.394728] R13: 000055e00f0a2020 R14: 0000000000000000 R15: 000055e00f0a2070
[109131.394731] ---[ end trace 61c4a29900fbfe5e ]---
[109131.394738] ------------[ cut here ]------------
[109131.394739] kernel BUG at mm/slub.c:316!
[109131.394746] invalid opcode: 0000 [#1] SMP NOPTI
[109131.394749] CPU: 3 PID: 1860476 Comm: clinfo:sh10 Tainted: G        W  OE     5.13.0-21-generic #21-Ubuntu
[109131.394752] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[109131.394754] RIP: 0010:__slab_free+0x21e/0x370
[109131.394758] Code: 75 67 45 84 c9 74 40 48 8b 44 24 78 65 48 2b 04 25 28 00 00 00 0f 85 20 01 00 00 48 8d 65 d8 5b 41 5c 41 5d 41 5e 41 5f 5d c3 <0f> 0b 80 4c 24 5b 80 31 ff e9 77 fe ff ff f3 90 49 8b 04 24 a8 01
[109131.394761] RSP: 0018:ffffb399646639a0 EFLAGS: 00010246
[109131.394764] RAX: ffff90aecbcef350 RBX: ffff90aecbcef340 RCX: ffff90aecbcef340
[109131.394766] RDX: 0000000080800046 RSI: ffffe5fe5e2f3bc0 RDI: ffff90a840042400
[109131.394768] RBP: ffffb39964663a50 R08: 0000000000000001 R09: ffffffffc0bc8750
[109131.394770] R10: ffffb39964663800 R11: ffff90aecbcef340 R12: ffffe5fe5e2f3bc0
[109131.394772] R13: ffff90aecbcef340 R14: ffff90a840042400 R15: ffff90aecbcef340
[109131.394774] FS:  0000000000000000(0000) GS:ffff90c73d2c0000(0000) knlGS:0000000000000000
[109131.394777] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[109131.394779] CR2: 00007f3cf9117fb2 CR3: 00000009dae1e000 CR4: 0000000000350ee0
[109131.394782] Call Trace:
[109131.394783]  ? report_bug+0xa1/0xc0
[109131.394788]  ? handle_bug+0x39/0x90
[109131.394791]  ? exc_invalid_op+0x19/0x70
[109131.394795]  kfree+0x3d9/0x410
[109131.394798]  ? kfd_gtt_sa_free+0x60/0x90 [amdgpu]
[109131.395008]  kfd_gtt_sa_free+0x60/0x90 [amdgpu]
[109131.395212]  free_mqd+0x15/0x20 [amdgpu]
[109131.395420]  process_termination_nocpsch+0xde/0x1e0 [amdgpu]
[109131.395628]  kfd_process_dequeue_from_all_devices+0x49/0x70 [amdgpu]
[109131.395834]  kfd_process_notifier_release+0xf2/0x160 [amdgpu]
[109131.396040]  __mmu_notifier_release+0x74/0x1f0
[109131.396044]  exit_mmap+0x15e/0x1f0
[109131.396046]  ? exit_robust_list+0x5c/0x130
[109131.396051]  ? __cond_resched+0x1a/0x50
[109131.396054]  ? mutex_lock+0x13/0x40
[109131.396058]  mmput+0x5f/0x140
[109131.396062]  exit_mm+0x169/0x1e0
[109131.396065]  do_exit+0x1b4/0x3d0
[109131.396068]  do_group_exit+0x3b/0xb0
[109131.396072]  get_signal+0x16b/0x8b0
[109131.396076]  arch_do_signal_or_restart+0xd9/0x100
[109131.396080]  ? do_futex+0x12c/0x1d0
[109131.396084]  ? __x64_sys_futex+0x78/0x1e0
[109131.396088]  exit_to_user_mode_loop+0xc4/0x160
[109131.396091]  exit_to_user_mode_prepare+0x9f/0xb0
[109131.396094]  syscall_exit_to_user_mode+0x27/0x50
[109131.396098]  do_syscall_64+0x6e/0xb0
[109131.396101]  ? do_syscall_64+0x6e/0xb0
[109131.396104]  ? exit_to_user_mode_prepare+0x37/0xb0
[109131.396106]  ? irqentry_exit_to_user_mode+0x9/0x20
[109131.396110]  ? irqentry_exit+0x19/0x30
[109131.396114]  ? exc_page_fault+0x8f/0x170
[109131.396118]  ? asm_exc_page_fault+0x8/0x30
[109131.396120]  entry_SYSCALL_64_after_hwframe+0x44/0xae
[109131.396125] RIP: 0033:0x7f758c7b2ff9
[109131.396127] Code: Unable to access opcode bytes at RIP 0x7f758c7b2fcf.
[109131.396129] RSP: 002b:00007f74bd7f9bc0 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
[109131.396132] RAX: fffffffffffffe00 RBX: 0000000000000000 RCX: 00007f758c7b2ff9
[109131.396134] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055e00f0a2070
[109131.396136] RBP: 0000000000000000 R08: 0000000000000000 R09: 00000000ffffffff
[109131.396138] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[109131.396140] R13: 000055e00f0a2020 R14: 0000000000000000 R15: 000055e00f0a2070
[109131.396143] Modules linked in: ufs qnx4 hfsplus hfs minix ntfs msdos jfs xfs cpuid cdc_ether usbnet mii drivetemp nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_hda_intel intel_rapl_msr snd_intel_dspcfg intel_rapl_common snd_intel_sdw_acpi amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usb_audio videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 snd_hda_core snd_usbmidi_lib kvm_amd videobuf2_common snd_hwdep snd_seq_midi joydev input_leds videodev kvm mc snd_pcm snd_seq_midi_event rapl efi_pstore snd_rawmidi snd_seq snd_seq_device snd_timer snd ipmi_si soundcore ipmi_devintf ccp ipmi_msghandler k10temp mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr parport_pc auth_rpcgss nfs_acl ppdev lockd lp grace parport sunrpc ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[109131.396202]  bcache crc64 hid_generic usbhid hid amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper drm_ttm_helper ttm crct10dif_pclmul crc32_pclmul drm_kms_helper ghash_clmulni_intel aesni_intel syscopyarea sysfillrect sysimgblt crypto_simd fb_sys_fops cryptd cec ixgbe rc_core igb xfrm_algo drm dca i2c_algo_bit mdio ahci libahci xhci_pci xhci_pci_renesas i2c_piix4 [last unloaded: acpi_ipmi]
[109131.396230] ---[ end trace 61c4a29900fbfe5f ]---
[109131.437627] RIP: 0010:__slab_free+0x21e/0x370
[109131.437637] Code: 75 67 45 84 c9 74 40 48 8b 44 24 78 65 48 2b 04 25 28 00 00 00 0f 85 20 01 00 00 48 8d 65 d8 5b 41 5c 41 5d 41 5e 41 5f 5d c3 <0f> 0b 80 4c 24 5b 80 31 ff e9 77 fe ff ff f3 90 49 8b 04 24 a8 01
[109131.437641] RSP: 0018:ffffb399646639a0 EFLAGS: 00010246
[109131.437645] RAX: ffff90aecbcef350 RBX: ffff90aecbcef340 RCX: ffff90aecbcef340
[109131.437647] RDX: 0000000080800046 RSI: ffffe5fe5e2f3bc0 RDI: ffff90a840042400
[109131.437650] RBP: ffffb39964663a50 R08: 0000000000000001 R09: ffffffffc0bc8750
[109131.437652] R10: ffffb39964663800 R11: ffff90aecbcef340 R12: ffffe5fe5e2f3bc0
[109131.437654] R13: ffff90aecbcef340 R14: ffff90a840042400 R15: ffff90aecbcef340
[109131.437657] FS:  0000000000000000(0000) GS:ffff90c73d2c0000(0000) knlGS:0000000000000000
[109131.437660] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[109131.437662] CR2: 00007f3cf9117fb2 CR3: 00000009dae1e000 CR4: 0000000000350ee0
[109131.437666] Fixing recursive fault but reboot is needed!
[109138.492681] amdgpu: Can't create new usermode queue because -1 queues were already created
[109138.492687] amdgpu: Pasid 0x8069 DQM create queue type 0 failed. ret -1
```

---

## 评论 (15 条)

### 评论 #1 — illwieckz (2021-11-22T21:56:36Z)

The request is: ROCm should not break the system, whatever something is supported or not.

---

### 评论 #2 — ROCmSupport (2021-11-23T06:11:51Z)

Thanks @illwieckz for reaching out.
I certainly understood the problem.
As ROCm stopped supporting gfx7 long back, but today, this is again a topic of discussion as Radeon Software for linux 20.04.1 still supports it but ROCm does not, which there is a gap.
We are working on resolving the gap.
Please stay tuned for updates. Thank you.

---

### 评论 #3 — illwieckz (2021-11-23T14:15:08Z)

Hi @ROCmSupport, thank you for your attention and kind answer.

I'm not against the idea of keeping ROCm stack for gfx7 if it is still working for some users, it would be very unfortunate to remove this code if it works for someone, but then an option is needed to prevent ROCm to attempt to handle gfx7 if both gfx7 and something else if hosted and gfx7 does not work. On my end the last time ROCm worked with gfx7 was in year 2018 ([proof](http://luxmark.info/node/5725)) and it only worked for some short months.

So I guess there are two possible solutions:

- adding options to ROCm to blacklist some architectures (to make possible to blacklist gfx7 on a per-user basis), that can be an environment variable;
- dropping gfx7 support entirely (I would prefer to see it working but something broken is worst than something not being there).

Some notes though:

> As ROCm stopped supporting gfx9 long back.

Hawaii is gfx7.

> This is again a topic of discussion as Radeon Software for linux 20.04.1 still supports it 

Radeon Software for Linux 20.04.1 stopped supporting gfx7 and others with amdgpu-pro 21.30, but I don't know if that was intentional or if a mistake was made: https://gitlab.freedesktop.org/drm/amd/-/issues/1806

AMD now provides no one OpenCL solution for Hawaii. None of ROCm, PAL, Orca are providing working OpenCL today (and Mesa solution is still incomplete then image workflow are unusable):

- AMD ROCm is broken with gfx7 since year 2018 or 2019;
- AMD PAL never supported gfx7;
- AMD Orca stopped working with gfx7 since 2021-08-10.

---

### 评论 #4 — illwieckz (2021-12-04T21:59:57Z)

It's possible to blacklist the card for ROCm by doing (given the unsupported card you want to blacklist is the first one):

```sh
export GPU_DEVICE_ORDINAL='0'
```

Or:

```sh
export GPU_DEVICE_ORDINAL='1,3'
```

To blacklist the second and the fouth one,

Or to blacklist everything:

```sh
export GPU_DEVICE_ORDINAL=','
```

This would make possible to use ROCm to a supported GPU while ignoring the unsupported one.

One big problem is that it would also blacklist the card in Orca (and probably also with PAL) so with this trick you cannot use ROCm with one card and Orca with another.

---

### 评论 #5 — illwieckz (2021-12-04T22:06:33Z)

An environment variable named `ROCR_VISIBLE_DEVICE` as suggested in #994 would be very good to blacklist a card in ROCm but to not blacklist it with another OpenCL driver like Orca or PAL.

---

### 评论 #6 — fxkamd (2021-12-08T03:18:15Z)

The bug you point out is pretty bad. I reproduced it (I still had a Hawaii card lying around) and I'm going to send out a fix in a minute.

There is an environment variable ROCR_VISIBLE_DEVICES that you can probably use as a workaround for now. See here for details: https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/fc99cf8516ef4bfc6311471b717838604a673b73/src/core/inc/amd_filter_device.h#L58

Hawaii support in KFD is obviously mostly untested these days. It also depends on custom firmware that was never pushed upstream due to quality regressions in the graphics driver. Therefore I will also guard KFD support for Hawaii behind the module parameter amdgpu.exp_hw_support=1. That way users will not run ROCm on Hawaii by accident.

---

### 评论 #7 — illwieckz (2021-12-08T15:19:32Z)

> The bug you point out is pretty bad. I reproduced it (I still had a Hawaii card lying around) and I'm going to send out a fix in a minute.

Oh that's awesome! Last time I have seen ROCr OpenCL working on R9 390X was in 2018 ([proof](http://luxmark.info/node/5725)).

> There is an environment variable ROCR_VISIBLE_DEVICES that you can probably use as a workaround for now. See here for details: https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/fc99cf8516ef4bfc6311471b717838604a673b73/src/core/inc/amd_filter_device.h#L58

Interesting!

> Hawaii support in KFD is obviously mostly untested these days. It also depends on custom firmware that was never pushed upstream due to quality regressions in the graphics driver.

The support for R9 390X was never good anyway, see [drm/amd#1816](https://gitlab.freedesktop.org/drm/amd/-/issues/1816), there are stability problems reported since 2015 with crashes occurring with default kernel configuration, it even means one cannot run a Linux live CD/USB to install Linux on a computer with the display plugged into an R9 390X… The computer would crash before completing the installation (in fact, before starting the installation).

> Therefore I will also guard KFD support for Hawaii behind the module parameter amdgpu.exp_hw_support=1. That way users will not run ROCm on Hawaii by accident.

That will be very convenient ! Thank you for this attention.

Note: I own PCIe 2, PCIe 3 and PCIe 4 hosts, so I can test fixes for the R9 390X on those various configurations. I assume main difference would be between PCIe 2 and PCIe 3 because of PCI Atomics (I reproduced the current bug on both PCIe 2 and PCIe 4, haven't tested on PCIe 3).

---

### 评论 #8 — fxkamd (2021-12-08T17:06:14Z)

> Note: I own PCIe 2, PCIe 3 and PCIe 4 hosts, so I can test fixes for the R9 390X on those various configurations. I assume main difference would be between PCIe 2 and PCIe 3 because of PCI Atomics (I reproduced the current bug on both PCIe 2 and PCIe 4, haven't tested on PCIe 3).

I don't think it makes a difference. Hawaii doesn't support PCIe atomics in any case. My test system is PCIe 3.

My KFD patches are here for review: https://lore.kernel.org/amd-gfx/20211208082531.918062-2-Felix.Kuehling@amd.com/T/

---

### 评论 #9 — illwieckz (2021-12-09T10:28:19Z)

> I don't think it makes a difference. Hawaii doesn't support PCIe atomics in any case. My test system is PCIe 3.

OK then, I remember [comments](https://github.com/RadeonOpenCompute/ROCm/issues/484#issuecomment-412644267) about Hawaii and PCIe atomics and [others](https://github.com/RadeonOpenCompute/ROCm/issues/484#issuecomment-409587451) where PCIe 2 or 3 seems to have made a difference, so this was confusing. The current host is PCIe4 on my end (ThreadRipper Pro 3955WX).

> My KFD patches are here for review: https://lore.kernel.org/amd-gfx/20211208082531.918062-2-Felix.Kuehling@amd.com/T/

Great! Do you have a link to the firmware that may be required for this? Display support is so bad with R9 390X with stock firmwares I would be interested in knowing what can be worse (I would also not be surprised if it appears the problems reported with updated firmwares are the ones we already reproduce with usual firmwares).


---

### 评论 #10 — illwieckz (2022-10-06T06:59:30Z)

Hi @fxkamd this message just to say the bug is still reproducible. Or maybe one bug was fixed but there are more bugs remaining?

Here are the software versions I use:

```
$ lsb_release -a
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.1 LTS
Release:	22.04
Codename:	jammy

$ uname -a
Linux gollum 5.15.0-50-generic #56-Ubuntu SMP Tue Sep 20 13:23:26 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

$ dpkg -l 'rocm*' | grep -E '^ii'
ii  rocm-core      5.3.0.50300-63~20.04 amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-ocl-icd   2.0.0.50300-63~20.04 amd64        opencl built using CMake
ii  rocm-opencl    2.0.0.50300-63~20.04 amd64        opencl built using CMake
```

Here is what happens when I call `clinfo --raw`, it never returns and `dmesg` prints things like that.

If I press `Ctrl+C` it still does not return but dmesg prints extra errors with `Fixing recursive fault but reboot is needed!` message.

```
[78134.011275] amdgpu 0000:41:00.0: amdgpu: Disabling VM faults because of PRT request!
[78134.026085] amdgpu 0000:42:00.0: amdgpu: Disabling VM faults because of PRT request!
[78399.759410] ------------[ cut here ]------------
[78399.759414] WARNING: CPU: 15 PID: 1832296 at drivers/gpu/drm/ttm/ttm_bo.c:409 ttm_bo_release+0x323/0x350 [ttm]
[78399.759428] Modules linked in: nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) nvme_fabrics overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_usb_audio snd_hda_intel snd_intel_dspcfg snd_intel_sdw_acpi intel_rapl_msr intel_rapl_common amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usbmidi_lib snd_hda_core kvm_amd videobuf2_vmalloc snd_hwdep videobuf2_memops snd_seq_midi kvm videobuf2_v4l2 videobuf2_common snd_seq_midi_event videodev hid_dr rapl ff_memless snd_rawmidi joydev input_leds snd_pcm mc snd_seq snd_seq_device snd_timer snd ccp soundcore acpi_ipmi ipmi_si k10temp ipmi_devintf ipmi_msghandler mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr auth_rpcgss parport_pc nfs_acl ppdev lockd lp grace parport ramoops pstore_blk reed_solomon sunrpc pstore_zone efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[78399.759493]  uas usb_storage bcache crc64 amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper hid_generic drm_ttm_helper ttm drm_kms_helper syscopyarea usbhid sysfillrect sysimgblt hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel fb_sys_fops aesni_intel cec ixgbe igb rc_core crypto_simd ahci xfrm_algo cryptd drm mdio dca libahci i2c_algo_bit nvme xhci_pci i2c_piix4 nvme_core xhci_pci_renesas
[78399.759518] CPU: 15 PID: 1832296 Comm: kworker/15:1 Tainted: G           OE     5.15.0-50-generic #56-Ubuntu
[78399.759519] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[78399.759521] Workqueue: kfd_process_wq kfd_process_wq_release [amdgpu]
[78399.759650] RIP: 0010:ttm_bo_release+0x323/0x350 [ttm]
[78399.759654] Code: b8 fe ff ff e8 fe 14 0c 00 49 8b 74 24 08 4c 89 ef e8 51 2a 00 00 49 8b 7c 24 98 e9 2f fd ff ff e8 02 a7 66 ef e9 63 fd ff ff <0f> 0b e9 01 fd ff ff e8 11 a5 66 ef e9 e2 fe ff ff be 03 00 00 00
[78399.759655] RSP: 0018:ffffc23fc3567c68 EFLAGS: 00010202
[78399.759656] RAX: 0000000000000001 RBX: ffffc23fc3567cc8 RCX: 0000000080400036
[78399.759657] RDX: 0000000000000001 RSI: 0000000080400036 RDI: ffff9f840841a1b8
[78399.759658] RBP: ffffc23fc3567c90 R08: ffff9f840841a1b8 R09: 0000000000000000
[78399.759659] R10: 0000000000000001 R11: 00000000ffffff00 R12: ffff9f840841a1b8
[78399.759660] R13: ffff9f7e11985270 R14: ffff9f840841a058 R15: dead000000000100
[78399.759661] FS:  0000000000000000(0000) GS:ffff9fbc2d5c0000(0000) knlGS:0000000000000000
[78399.759662] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[78399.759663] CR2: 000055f7c1f8d000 CR3: 000000015a68c000 CR4: 0000000000350ee0
[78399.759664] Call Trace:
[78399.759665]  <TASK>
[78399.759668]  ttm_bo_put+0x34/0x50 [ttm]
[78399.759672]  amdgpu_bo_unref+0x1e/0x30 [amdgpu]
[78399.759770]  amdgpu_gem_object_free+0x34/0x50 [amdgpu]
[78399.759868]  drm_gem_object_free+0x1d/0x30 [drm]
[78399.759884]  amdgpu_amdkfd_gpuvm_free_memory_of_gpu+0x369/0x3e0 [amdgpu]
[78399.760002]  kfd_process_device_free_bos+0xb1/0x110 [amdgpu]
[78399.760114]  kfd_process_wq_release+0x51/0x110 [amdgpu]
[78399.760224]  process_one_work+0x22b/0x3d0
[78399.760227]  worker_thread+0x53/0x420
[78399.760228]  ? process_one_work+0x3d0/0x3d0
[78399.760230]  kthread+0x12a/0x150
[78399.760231]  ? set_kthread_struct+0x50/0x50
[78399.760233]  ret_from_fork+0x22/0x30
[78399.760236]  </TASK>
[78399.760237] ---[ end trace e9d44bd9afd435d6 ]---
[78408.565147] ------------[ cut here ]------------
[78408.565149] Load non-HWS mqd while stopped
[78408.565183] WARNING: CPU: 12 PID: 1868065 at drivers/gpu/drm/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:389 create_queue_nocpsch+0x4f8/0x520 [amdgpu]
[78408.565315] Modules linked in: nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) nvme_fabrics overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_usb_audio snd_hda_intel snd_intel_dspcfg snd_intel_sdw_acpi intel_rapl_msr intel_rapl_common amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usbmidi_lib snd_hda_core kvm_amd videobuf2_vmalloc snd_hwdep videobuf2_memops snd_seq_midi kvm videobuf2_v4l2 videobuf2_common snd_seq_midi_event videodev hid_dr rapl ff_memless snd_rawmidi joydev input_leds snd_pcm mc snd_seq snd_seq_device snd_timer snd ccp soundcore acpi_ipmi ipmi_si k10temp ipmi_devintf ipmi_msghandler mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr auth_rpcgss parport_pc nfs_acl ppdev lockd lp grace parport ramoops pstore_blk reed_solomon sunrpc pstore_zone efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[78408.565351]  uas usb_storage bcache crc64 amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper hid_generic drm_ttm_helper ttm drm_kms_helper syscopyarea usbhid sysfillrect sysimgblt hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel fb_sys_fops aesni_intel cec ixgbe igb rc_core crypto_simd ahci xfrm_algo cryptd drm mdio dca libahci i2c_algo_bit nvme xhci_pci i2c_piix4 nvme_core xhci_pci_renesas
[78408.565372] CPU: 12 PID: 1868065 Comm: clinfo Tainted: G        W  OE     5.15.0-50-generic #56-Ubuntu
[78408.565374] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[78408.565375] RIP: 0010:create_queue_nocpsch+0x4f8/0x520 [amdgpu]
[78408.565490] Code: 89 f2 48 c7 c6 50 8a 13 c1 48 c7 c7 d0 8e 2e c1 e8 1d e8 a1 ee eb 88 48 c7 c7 b0 8a 13 c1 c6 05 2e d5 68 00 01 e8 f9 f2 09 ef <0f> 0b e9 3d fe ff ff 48 c7 c7 d0 8a 13 c1 e8 e6 f2 09 ef 0f 0b b8
[78408.565491] RSP: 0018:ffffc2400744bb70 EFLAGS: 00010282
[78408.565493] RAX: 0000000000000000 RBX: ffff9f7dc1271800 RCX: 0000000000000027
[78408.565494] RDX: ffff9fbc2d520588 RSI: 0000000000000001 RDI: ffff9fbc2d520580
[78408.565495] RBP: ffffc2400744bbc0 R08: 0000000000000003 R09: fffffffffff2d878
[78408.565495] R10: 0000000000000020 R11: 0000000000000001 R12: ffff9f8d152e9000
[78408.565496] R13: ffff9f8d1d1de810 R14: 0000000000000000 R15: 0000000000000000
[78408.565497] FS:  00007fe470d22c40(0000) GS:ffff9fbc2d500000(0000) knlGS:0000000000000000
[78408.565499] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[78408.565500] CR2: 0000000001018040 CR3: 00000010580ba000 CR4: 0000000000350ee0
[78408.565501] Call Trace:
[78408.565502]  <TASK>
[78408.565505]  pqm_create_queue+0x1cc/0x4a0 [amdgpu]
[78408.565623]  kfd_ioctl_create_queue+0xd3/0x2c0 [amdgpu]
[78408.565745]  kfd_ioctl+0x332/0x480 [amdgpu]
[78408.565863]  ? kfd_ioctl_dbg_address_watch+0x190/0x190 [amdgpu]
[78408.565981]  ? __fget_files+0x86/0xc0
[78408.565985]  __x64_sys_ioctl+0x95/0xd0
[78408.565987]  do_syscall_64+0x5c/0xc0
[78408.565990]  ? handle_mm_fault+0xd8/0x2c0
[78408.565993]  ? do_user_addr_fault+0x1e7/0x670
[78408.565996]  ? exit_to_user_mode_prepare+0x37/0xb0
[78408.565998]  ? irqentry_exit_to_user_mode+0x9/0x20
[78408.566000]  ? irqentry_exit+0x1d/0x30
[78408.566001]  ? exc_page_fault+0x89/0x170
[78408.566003]  entry_SYSCALL_64_after_hwframe+0x61/0xcb
[78408.566006] RIP: 0033:0x7fe470e43aff
[78408.566007] Code: 00 48 89 44 24 18 31 c0 48 8d 44 24 60 c7 04 24 10 00 00 00 48 89 44 24 08 48 8d 44 24 20 48 89 44 24 10 b8 10 00 00 00 0f 05 <41> 89 c0 3d 00 f0 ff ff 77 1f 48 8b 44 24 18 64 48 2b 04 25 28 00
[78408.566008] RSP: 002b:00007ffe08f6de60 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[78408.566010] RAX: ffffffffffffffda RBX: 00007ffe08f6df40 RCX: 00007fe470e43aff
[78408.566011] RDX: 00007ffe08f6df40 RSI: 00000000c0584b02 RDI: 000000000000000f
[78408.566011] RBP: 00000000c0584b02 R08: 00000000000000b0 R09: 0000000000000000
[78408.566012] R10: 00007ffe08f6df40 R11: 0000000000000246 R12: 0000000000000000
[78408.566013] R13: 000000000000000f R14: 0000000000000001 R15: 0000000001018000
[78408.566015]  </TASK>
[78408.566015] ---[ end trace e9d44bd9afd435d7 ]---
[78500.536367] ------------[ cut here ]------------
[78500.536370] Evict when stopped
[78500.536413] WARNING: CPU: 6 PID: 1870182 at drivers/gpu/drm/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:693 evict_process_queues_nocpsch+0x1f9/0x210 [amdgpu]
[78500.536693] Modules linked in: nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) nvme_fabrics overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_usb_audio snd_hda_intel snd_intel_dspcfg snd_intel_sdw_acpi intel_rapl_msr intel_rapl_common amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usbmidi_lib snd_hda_core kvm_amd videobuf2_vmalloc snd_hwdep videobuf2_memops snd_seq_midi kvm videobuf2_v4l2 videobuf2_common snd_seq_midi_event videodev hid_dr rapl ff_memless snd_rawmidi joydev input_leds snd_pcm mc snd_seq snd_seq_device snd_timer snd ccp soundcore acpi_ipmi ipmi_si k10temp ipmi_devintf ipmi_msghandler mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr auth_rpcgss parport_pc nfs_acl ppdev lockd lp grace parport ramoops pstore_blk reed_solomon sunrpc pstore_zone efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[78500.536767]  uas usb_storage bcache crc64 amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper hid_generic drm_ttm_helper ttm drm_kms_helper syscopyarea usbhid sysfillrect sysimgblt hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel fb_sys_fops aesni_intel cec ixgbe igb rc_core crypto_simd ahci xfrm_algo cryptd drm mdio dca libahci i2c_algo_bit nvme xhci_pci i2c_piix4 nvme_core xhci_pci_renesas
[78500.536805] CPU: 6 PID: 1870182 Comm: clinfo:shlo2 Tainted: G        W  OE     5.15.0-50-generic #56-Ubuntu
[78500.536809] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[78500.536811] RIP: 0010:evict_process_queues_nocpsch+0x1f9/0x210 [amdgpu]
[78500.537100] Code: de 68 00 41 80 fe 01 0f 87 1b 7b 36 00 41 83 e6 01 0f 85 5c ff ff ff 48 c7 c7 c9 f1 18 c1 c6 05 9a de 68 00 01 e8 68 fc 09 ef <0f> 0b e9 42 ff ff ff e9 07 7b 36 00 66 66 2e 0f 1f 84 00 00 00 00
[78500.537103] RSP: 0018:ffffc23feb127a88 EFLAGS: 00010282
[78500.537107] RAX: 0000000000000000 RBX: ffff9f8d3190b600 RCX: 0000000000000027
[78500.537110] RDX: ffff9fbc2d3a0588 RSI: 0000000000000001 RDI: ffff9fbc2d3a0580
[78500.537112] RBP: ffffc23feb127ad8 R08: 0000000000000003 R09: fffffffffff2e960
[78500.537113] R10: 0000000000000014 R11: 0000000000000001 R12: ffff9f8d2d255610
[78500.537115] R13: 0000000000000000 R14: 0000000000000000 R15: ffff9f7dc1271800
[78500.537117] FS:  0000000000000000(0000) GS:ffff9fbc2d380000(0000) knlGS:0000000000000000
[78500.537120] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[78500.537122] CR2: 00007facee284048 CR3: 000000106d244000 CR4: 0000000000350ee0
[78500.537125] Call Trace:
[78500.537127]  <TASK>
[78500.537130]  ? check_preempt_curr+0x61/0x70
[78500.537139]  kfd_process_evict_queues+0x49/0x90 [amdgpu]
[78500.537414]  kgd2kfd_quiesce_mm+0x3a/0x80 [amdgpu]
[78500.537680]  amdgpu_amdkfd_evict_userptr+0x3f/0x70 [amdgpu]
[78500.537957]  amdgpu_mn_invalidate_hsa+0x49/0x70 [amdgpu]
[78500.538236]  __mmu_notifier_release+0x1a8/0x200
[78500.538243]  exit_mmap+0x1c0/0x200
[78500.538246]  ? skb_queue_tail+0x48/0x60
[78500.538251]  ? sock_def_readable+0x4b/0x80
[78500.538254]  ? exit_robust_list+0x5c/0x140
[78500.538258]  ? __cond_resched+0x1a/0x50
[78500.538263]  ? mutex_lock+0x13/0x50
[78500.538266]  ? uprobe_clear_state+0xac/0x120
[78500.538271]  mmput+0x63/0x150
[78500.538276]  exit_mm+0x154/0x1d0
[78500.538280]  do_exit+0x1a7/0x3c0
[78500.538284]  do_group_exit+0x3b/0xb0
[78500.538288]  get_signal+0x150/0x900
[78500.538292]  arch_do_signal_or_restart+0xde/0x100
[78500.538297]  ? do_futex+0x149/0x1f0
[78500.538301]  ? __x64_sys_futex+0x78/0x1e0
[78500.538304]  exit_to_user_mode_loop+0xc4/0x160
[78500.538309]  exit_to_user_mode_prepare+0xa0/0xb0
[78500.538313]  syscall_exit_to_user_mode+0x27/0x50
[78500.538318]  do_syscall_64+0x69/0xc0
[78500.538321]  ? do_user_addr_fault+0x1e7/0x670
[78500.538325]  ? exit_to_user_mode_prepare+0x37/0xb0
[78500.538329]  ? irqentry_exit_to_user_mode+0x9/0x20
[78500.538333]  ? irqentry_exit+0x1d/0x30
[78500.538336]  ? exc_page_fault+0x89/0x170
[78500.538340]  entry_SYSCALL_64_after_hwframe+0x61/0xcb
[78500.538344] RIP: 0033:0x7f075a338197
[78500.538347] Code: Unable to access opcode bytes at RIP 0x7f075a33816d.
[78500.538349] RSP: 002b:00007f06db7fdc20 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
[78500.538353] RAX: fffffffffffffe00 RBX: 0000000000000000 RCX: 00007f075a338197
[78500.538355] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055c0fd3e77d8
[78500.538357] RBP: 000055c0fd3e77b0 R08: 0000000000000000 R09: 00000000ffffffff
[78500.538359] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[78500.538360] R13: 0000000000000000 R14: 0000000000000004 R15: 000055c0fd3e77d8
[78500.538364]  </TASK>
[78500.538365] ---[ end trace e9d44bd9afd435d8 ]---
[78500.538422] ------------[ cut here ]------------
[78500.538425] Destroy non-HWS queue while stopped
[78500.538445] WARNING: CPU: 22 PID: 1870182 at drivers/gpu/drm/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:505 destroy_queue_nocpsch_locked+0x173/0x1e0 [amdgpu]
[78500.538697] Modules linked in: nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) nvme_fabrics overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_usb_audio snd_hda_intel snd_intel_dspcfg snd_intel_sdw_acpi intel_rapl_msr intel_rapl_common amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usbmidi_lib snd_hda_core kvm_amd videobuf2_vmalloc snd_hwdep videobuf2_memops snd_seq_midi kvm videobuf2_v4l2 videobuf2_common snd_seq_midi_event videodev hid_dr rapl ff_memless snd_rawmidi joydev input_leds snd_pcm mc snd_seq snd_seq_device snd_timer snd ccp soundcore acpi_ipmi ipmi_si k10temp ipmi_devintf ipmi_msghandler mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr auth_rpcgss parport_pc nfs_acl ppdev lockd lp grace parport ramoops pstore_blk reed_solomon sunrpc pstore_zone efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[78500.538765]  uas usb_storage bcache crc64 amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper hid_generic drm_ttm_helper ttm drm_kms_helper syscopyarea usbhid sysfillrect sysimgblt hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel fb_sys_fops aesni_intel cec ixgbe igb rc_core crypto_simd ahci xfrm_algo cryptd drm mdio dca libahci i2c_algo_bit nvme xhci_pci i2c_piix4 nvme_core xhci_pci_renesas
[78500.538796] CPU: 22 PID: 1870182 Comm: clinfo:shlo2 Tainted: G        W  OE     5.15.0-50-generic #56-Ubuntu
[78500.538800] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[78500.538802] RIP: 0010:destroy_queue_nocpsch_locked+0x173/0x1e0 [amdgpu]
[78500.539047] Code: b6 1d 41 e9 68 00 80 fb 01 0f 87 2a 85 36 00 45 31 ff 83 e3 01 75 d2 48 c7 c7 58 88 13 c1 c6 05 22 e9 68 00 01 e8 ee 06 0a ef <0f> 0b eb bb 4c 89 e2 4c 89 f6 4c 89 ef e8 4b f8 ff ff eb ab 4c 89
[78500.539049] RSP: 0018:ffffc23feb127a90 EFLAGS: 00010286
[78500.539052] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 0000000000000027
[78500.539054] RDX: ffff9fbc2d7a0588 RSI: 0000000000000001 RDI: ffff9fbc2d7a0580
[78500.539056] RBP: ffffc23feb127ac0 R08: 0000000000000003 R09: fffffffffff2fc90
[78500.539057] R10: 0000000000000025 R11: 0000000000000001 R12: ffff9f8d3190b600
[78500.539059] R13: ffff9f7dc1271800 R14: ffff9f8d2d255610 R15: 0000000000000000
[78500.539061] FS:  0000000000000000(0000) GS:ffff9fbc2d780000(0000) knlGS:0000000000000000
[78500.539063] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[78500.539065] CR2: 00007faef8a9fe40 CR3: 000000041c160000 CR4: 0000000000350ee0
[78500.539067] Call Trace:
[78500.539069]  <TASK>
[78500.539071]  process_termination_nocpsch+0x9f/0x1e0 [amdgpu]
[78500.539317]  kfd_process_dequeue_from_all_devices+0x62/0xa0 [amdgpu]
[78500.539651]  kfd_process_notifier_release+0x10b/0x1a0 [amdgpu]
[78500.539984]  __mmu_notifier_release+0x80/0x200
[78500.539991]  exit_mmap+0x1c0/0x200
[78500.539994]  ? skb_queue_tail+0x48/0x60
[78500.539999]  ? sock_def_readable+0x4b/0x80
[78500.540002]  ? exit_robust_list+0x5c/0x140
[78500.540006]  ? __cond_resched+0x1a/0x50
[78500.540011]  ? mutex_lock+0x13/0x50
[78500.540014]  ? uprobe_clear_state+0xac/0x120
[78500.540020]  mmput+0x63/0x150
[78500.540025]  exit_mm+0x154/0x1d0
[78500.540030]  do_exit+0x1a7/0x3c0
[78500.540034]  do_group_exit+0x3b/0xb0
[78500.540039]  get_signal+0x150/0x900
[78500.540044]  arch_do_signal_or_restart+0xde/0x100
[78500.540049]  ? do_futex+0x149/0x1f0
[78500.540053]  ? __x64_sys_futex+0x78/0x1e0
[78500.540057]  exit_to_user_mode_loop+0xc4/0x160
[78500.540062]  exit_to_user_mode_prepare+0xa0/0xb0
[78500.540067]  syscall_exit_to_user_mode+0x27/0x50
[78500.540072]  do_syscall_64+0x69/0xc0
[78500.540076]  ? do_user_addr_fault+0x1e7/0x670
[78500.540081]  ? exit_to_user_mode_prepare+0x37/0xb0
[78500.540085]  ? irqentry_exit_to_user_mode+0x9/0x20
[78500.540090]  ? irqentry_exit+0x1d/0x30
[78500.540094]  ? exc_page_fault+0x89/0x170
[78500.540098]  entry_SYSCALL_64_after_hwframe+0x61/0xcb
[78500.540103] RIP: 0033:0x7f075a338197
[78500.540107] Code: Unable to access opcode bytes at RIP 0x7f075a33816d.
[78500.540109] RSP: 002b:00007f06db7fdc20 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
[78500.540113] RAX: fffffffffffffe00 RBX: 0000000000000000 RCX: 00007f075a338197
[78500.540116] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055c0fd3e77d8
[78500.540118] RBP: 000055c0fd3e77b0 R08: 0000000000000000 R09: 00000000ffffffff
[78500.540120] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[78500.540122] R13: 0000000000000000 R14: 0000000000000004 R15: 000055c0fd3e77d8
[78500.540127]  </TASK>
[78500.540129] ---[ end trace e9d44bd9afd435d9 ]---
[78500.540140] ------------[ cut here ]------------
[78500.540142] kernel BUG at mm/slub.c:379!
[78500.540150] invalid opcode: 0000 [#1] SMP NOPTI
[78500.540155] CPU: 22 PID: 1870182 Comm: clinfo:shlo2 Tainted: G        W  OE     5.15.0-50-generic #56-Ubuntu
[78500.540161] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[78500.540163] RIP: 0010:__slab_free+0x1f3/0x370
[78500.540170] Code: 00 44 0f b6 5c 24 1a 8b 74 24 14 44 0f b6 54 24 1b 44 8b 44 24 1c 48 89 44 24 08 48 8b 54 24 20 4c 8b 4c 24 28 e9 bb fe ff ff <0f> 0b 41 f7 46 08 00 0d 21 00 75 96 eb 8b 49 3b 54 24 28 0f 85 60
[78500.540174] RSP: 0018:ffffc23feb1279a0 EFLAGS: 00010246
[78500.540179] RAX: ffff9f86026a5750 RBX: ffff9f86026a5740 RCX: ffff9f86026a5740
[78500.540182] RDX: 0000000080800056 RSI: ffffeeb96509a940 RDI: ffff9f7dc0042400
[78500.540185] RBP: ffffc23feb127a38 R08: 0000000000000001 R09: ffffffffc0c4571d
[78500.540188] R10: ffff9f86026a5740 R11: 0000000000000000 R12: ffffeeb96509a940
[78500.540191] R13: ffff9f86026a5740 R14: ffff9f7dc0042400 R15: ffff9f86026a5740
[78500.540195] FS:  0000000000000000(0000) GS:ffff9fbc2d780000(0000) knlGS:0000000000000000
[78500.540199] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[78500.540203] CR2: 00007faef8a9fe40 CR3: 000000041c160000 CR4: 0000000000350ee0
[78500.540206] Call Trace:
[78500.540208]  <TASK>
[78500.540211]  ? handle_bug+0x39/0x90
[78500.540215]  ? exc_invalid_op+0x19/0x70
[78500.540221]  ? kfd_gtt_sa_free+0x5d/0x90 [amdgpu]
[78500.540541]  kfree+0x21a/0x250
[78500.540548]  kfd_gtt_sa_free+0x5d/0x90 [amdgpu]
[78500.540880]  free_mqd+0x15/0x20 [amdgpu]
[78500.541212]  process_termination_nocpsch+0xde/0x1e0 [amdgpu]
[78500.541504]  kfd_process_dequeue_from_all_devices+0x62/0xa0 [amdgpu]
[78500.541744]  kfd_process_notifier_release+0x10b/0x1a0 [amdgpu]
[78500.541982]  __mmu_notifier_release+0x80/0x200
[78500.541988]  exit_mmap+0x1c0/0x200
[78500.541991]  ? skb_queue_tail+0x48/0x60
[78500.541994]  ? sock_def_readable+0x4b/0x80
[78500.541997]  ? exit_robust_list+0x5c/0x140
[78500.542001]  ? __cond_resched+0x1a/0x50
[78500.542004]  ? mutex_lock+0x13/0x50
[78500.542008]  ? uprobe_clear_state+0xac/0x120
[78500.542012]  mmput+0x63/0x150
[78500.542017]  exit_mm+0x154/0x1d0
[78500.542021]  do_exit+0x1a7/0x3c0
[78500.542025]  do_group_exit+0x3b/0xb0
[78500.542029]  get_signal+0x150/0x900
[78500.542033]  arch_do_signal_or_restart+0xde/0x100
[78500.542037]  ? do_futex+0x149/0x1f0
[78500.542040]  ? __x64_sys_futex+0x78/0x1e0
[78500.542044]  exit_to_user_mode_loop+0xc4/0x160
[78500.542049]  exit_to_user_mode_prepare+0xa0/0xb0
[78500.542053]  syscall_exit_to_user_mode+0x27/0x50
[78500.542057]  do_syscall_64+0x69/0xc0
[78500.542060]  ? do_user_addr_fault+0x1e7/0x670
[78500.542064]  ? exit_to_user_mode_prepare+0x37/0xb0
[78500.542068]  ? irqentry_exit_to_user_mode+0x9/0x20
[78500.542072]  ? irqentry_exit+0x1d/0x30
[78500.542076]  ? exc_page_fault+0x89/0x170
[78500.542079]  entry_SYSCALL_64_after_hwframe+0x61/0xcb
[78500.542084] RIP: 0033:0x7f075a338197
[78500.542087] Code: Unable to access opcode bytes at RIP 0x7f075a33816d.
[78500.542088] RSP: 002b:00007f06db7fdc20 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
[78500.542092] RAX: fffffffffffffe00 RBX: 0000000000000000 RCX: 00007f075a338197
[78500.542094] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055c0fd3e77d8
[78500.542096] RBP: 000055c0fd3e77b0 R08: 0000000000000000 R09: 00000000ffffffff
[78500.542098] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[78500.542100] R13: 0000000000000000 R14: 0000000000000004 R15: 000055c0fd3e77d8
[78500.542104]  </TASK>
[78500.542106] Modules linked in: nfnetlink vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) nvme_fabrics overlay bridge stp llc binfmt_misc ipmi_ssif snd_hda_codec_hdmi snd_usb_audio snd_hda_intel snd_intel_dspcfg snd_intel_sdw_acpi intel_rapl_msr intel_rapl_common amd64_edac snd_hda_codec edac_mce_amd uvcvideo snd_usbmidi_lib snd_hda_core kvm_amd videobuf2_vmalloc snd_hwdep videobuf2_memops snd_seq_midi kvm videobuf2_v4l2 videobuf2_common snd_seq_midi_event videodev hid_dr rapl ff_memless snd_rawmidi joydev input_leds snd_pcm mc snd_seq snd_seq_device snd_timer snd ccp soundcore acpi_ipmi ipmi_si k10temp ipmi_devintf ipmi_msghandler mac_hid sch_fq_codel vhba(OE) nfsd hwmon_vid msr auth_rpcgss parport_pc nfs_acl ppdev lockd lp grace parport ramoops pstore_blk reed_solomon sunrpc pstore_zone efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear
[78500.542174]  uas usb_storage bcache crc64 amdgpu iommu_v2 gpu_sched radeon ast drm_vram_helper hid_generic drm_ttm_helper ttm drm_kms_helper syscopyarea usbhid sysfillrect sysimgblt hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel fb_sys_fops aesni_intel cec ixgbe igb rc_core crypto_simd ahci xfrm_algo cryptd drm mdio dca libahci i2c_algo_bit nvme xhci_pci i2c_piix4 nvme_core xhci_pci_renesas
[78500.542208] ---[ end trace e9d44bd9afd435da ]---
[78500.547089] RIP: 0010:__slab_free+0x1f3/0x370
[78500.547093] Code: 00 44 0f b6 5c 24 1a 8b 74 24 14 44 0f b6 54 24 1b 44 8b 44 24 1c 48 89 44 24 08 48 8b 54 24 20 4c 8b 4c 24 28 e9 bb fe ff ff <0f> 0b 41 f7 46 08 00 0d 21 00 75 96 eb 8b 49 3b 54 24 28 0f 85 60
[78500.547095] RSP: 0018:ffffc23feb1279a0 EFLAGS: 00010246
[78500.547098] RAX: ffff9f86026a5750 RBX: ffff9f86026a5740 RCX: ffff9f86026a5740
[78500.547099] RDX: 0000000080800056 RSI: ffffeeb96509a940 RDI: ffff9f7dc0042400
[78500.547101] RBP: ffffc23feb127a38 R08: 0000000000000001 R09: ffffffffc0c4571d
[78500.547103] R10: ffff9f86026a5740 R11: 0000000000000000 R12: ffffeeb96509a940
[78500.547105] R13: ffff9f86026a5740 R14: ffff9f7dc0042400 R15: ffff9f86026a5740
[78500.547107] FS:  0000000000000000(0000) GS:ffff9fbc2d780000(0000) knlGS:0000000000000000
[78500.547109] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[78500.547111] CR2: 00007faef8a9fe40 CR3: 000000041c160000 CR4: 0000000000350ee0
[78500.547114] Fixing recursive fault but reboot is needed!
```

---

### 评论 #11 — fxkamd (2022-10-17T22:12:09Z)

Looks like you're using the amdgpu driver built into your 5.15 kernel. Are you sure the kernel includes the fix?

---

### 评论 #12 — illwieckz (2023-04-10T01:03:41Z)

Hi @fxkamd I tried again, here are the results of my tests.

I'm running Ubuntu `22.10` with linux kernel `5.15.0` and amdgpu-pro `22.40-1538781.22.04` and rocm `5.4.3`. I verified the GPU is using `amdgpu` kernel driver, and not `radeon`.

- If I use ROCm OpenCL without `amdgpu-dkms` I get the gfx7 device listed but that produces the usual wreckage.
- If I use ROCm OpenCL with `amdgpu-dkms` but the gfx7 device is not listed so there is no wreckage.

So, in some way, when installing fully complete rocm installation there is no wreckage, but that very likely happens because some kernel module is blacklisting the device or something like that, ROCm itself doesn't do any check: when using stock kernel modules, ROCm actually tries to use the gfx7 card.

Actually I'm not against the gfx7 support being disabled by default (possibly with an option to unlock it for those who takes the risk) but that better be done on ROCm side.

Also, since ROCm still tries to use the gfx7 card if not using the provided dkms module (and then still ship some support for it), I would like to know if that disablement on kernel module side can be unlocked so I can test if ROCm gfx7 support works with the dkms kernel modules.

I totally forgot to respond in October 2022 but I experienced the exact same thing at the time: with dkms modules the gfx7 device was simply not listed at all. I'm confirming the behavior is the same today with the more recent versions.

I would like to know how to unlock the gfx7 device when running the dkms modules so I can do extended tests, if that's possible.

As a side remark, I noticed that latest old OpenCL Orca driver (`21.20-1271047-ubuntu-20.04`) for this card works with stock `amdgpu` kernel but crashes the system (endless GPU resets requiring a computer reboot) with `amdgpu-dkms` kernel provided with `amdgpu-pro`, so there may be a regression in `amdgpu-dkms` from amdgpu-pro `22.40-1538781.22.04`.

_Edit:_ It looks like `rocm-dkms` is just a metapackage depending on `amdgpu-dkms` so I removed mention of it in my wording. I also fixed my mention of the (not used) `radeon` driver kernel module as `radeonsi`, this was just muscle memory doing it wrong.

---

### 评论 #13 — illwieckz (2023-04-10T01:10:37Z)

Some info:

```
# dpkg -l amdgpu-dkms rocminfo rocm-opencl
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version                       Architecture Description
+++-==============-=============================-============-================================================
ii  amdgpu-dkms    1:5.18.13.50403-1538762.22.04 all          amdgpu driver in DKMS format.
ii  rocm-opencl    2.0.0.50403-121~22.04         amd64        opencl built using CMake
ii  rocminfo       1.0.0.50403-121~22.04         amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool

# /usr/bin/clinfo
Number of platforms                               0

# /opt/rocm-5.4.3/opencl/bin/clinfo
ERROR: clGetPlatformIDs(-1001)

# rocminfo
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen Threadripper PRO 3955WX 16-Cores
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen Threadripper PRO 3955WX 16-Cores
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
  Max Clock Freq. (MHz):   3900
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            32
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    263754876(0xfb8947c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    263754876(0xfb8947c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    263754876(0xfb8947c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*** Done ***
```

---

### 评论 #14 — illwieckz (2023-04-10T01:48:11Z)

So I enabled `amdgpu.exp_hw_support=1` after seen this option in `amd/amdkfd/kfd_device.c`.

Both `rocminfo` and `clinfo --list` now lists the gfx7 device, but complete `clinfo` hangs, and I get an error printed in `dmesg`, and if I interrupt `clinfo` with `Ctrl+C` I get more error logs in `dmesg`.

Fortunately, this doesn't wreck the kernel like before, so at least, yes, the original bug. There is a new one though.

Also the fact OpenCL applications will hang is a problem.

```
# rocminfo 
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen Threadripper PRO 3955WX 16-Cores
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper PRO 3955WX 16-Cores
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
  Max Clock Freq. (MHz):   3900                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    263754876(0xfb8947c) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    263754876(0xfb8947c) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    263754876(0xfb8947c) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon (TM) R9 390 Series      
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
    L1:                      16(0x10) KB                        
  Chip ID:                 26544(0x67b0)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1080                               
  BDFID:                   16640                              
  Internal Node ID:        1                                  
  Compute Unit:            44                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8388608(0x800000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             
```

```
# clinfo --list
Platform #0: AMD Accelerated Parallel Processing
 `-- Device #0: gfx701
```

```
# dmesg -w &

# clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3513.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx701
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  3513.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         AMD Radeon (TM) R9 390 Series
  Device PCI-e ID (AMD)                           0x67b0
  Device Topology (AMD)                           PCI-E, 0000:41:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               44
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1080MHz
  Graphics IP (AMD)                               7.0
  Device Partition                                (core)
    Max number of sub-devices                     44
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
[  328.021447] kfd kfd: amdgpu: Process 25333 (pasid 0x8003) got unhandled exception
^C
[  422.704149] amdgpu: cp queue preemption time out
[  422.704155] amdgpu: Failed to evict process queues
[  422.704157] amdgpu: Failed to quiesce KFD
[  426.740078] amdgpu: cp queue preemption time out
[  426.740084] amdgpu: Resetting wave fronts (nocpsch) on dev 0000000006b97bde
[  426.740111] ------------[ cut here ]------------
[  426.740115] FW bug: No PASID in KFD interrupt
[  426.740156] WARNING: CPU: 22 PID: 0 at /var/lib/dkms/amdgpu/5.18.13-1538762.22.04/build/amd/amdgpu/../amdkfd/cik_event_interrupt.c:73 cik_event_interrupt_isr+0xab/0x190 [amdgpu]
[  426.740496] Modules linked in: snd_seq_dummy snd_hrtimer vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) nvme_fabrics bridge stp llc binfmt_misc ipmi_ssif intel_rapl_msr intel_rapl_common snd_hda_codec_hdmi amd64_edac snd_hda_intel edac_mce_amd snd_intel_dspcfg snd_usb_audio snd_intel_sdw_acpi hid_dr input_leds joydev snd_usbmidi_lib ff_memless snd_hda_codec snd_seq_midi kvm_amd snd_seq_midi_event snd_rawmidi snd_hda_core kvm snd_hwdep mc snd_seq snd_pcm snd_seq_device rapl nls_iso8859_1 snd_timer ccp acpi_ipmi snd soundcore ipmi_si k10temp ipmi_devintf ipmi_msghandler mac_hid vhba(OE) nfsd hwmon_vid auth_rpcgss nfs_acl msr lockd parport_pc grace ppdev lp parport ramoops pstore_blk reed_solomon efi_pstore pstore_zone sunrpc ip_tables x_tables autofs4 btrfs blake2b_generic zstd_compress dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear uas usb_storage hid_generic usbhid hid ib_uverbs ib_core amdgpu(OE) bcache
[  426.740575]  crc64 amddrm_ttm_helper(OE) amdttm(OE) iommu_v2 amd_sched(OE) ast drm_vram_helper drm_ttm_helper ttm amdkcl(OE) drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops cec crct10dif_pclmul ixgbe rc_core crc32_pclmul ghash_clmulni_intel aesni_intel igb xfrm_algo nvme ahci drm crypto_simd xhci_pci dca cryptd libahci mdio i2c_algo_bit nvme_core xhci_pci_renesas i2c_piix4
[  426.740610] CPU: 22 PID: 0 Comm: swapper/22 Tainted: G           OE     5.15.0-66-generic #73-Ubuntu
[  426.740614] Hardware name: GIGABYTE WRX80-SU8 N/A/WRX80-SU8, BIOS WRX80SU8-F4 06/18/2021
[  426.740616] RIP: 0010:cik_event_interrupt_isr+0xab/0x190 [amdgpu]
[  426.740932] Code: eb 2c 0f b6 1d cd 9d 8c 00 80 fb 01 0f 87 22 76 48 00 83 e3 01 75 15 48 c7 c7 c8 8b f2 c0 c6 05 b1 9d 8c 00 01 e8 d3 52 c2 fb <0f> 0b 31 c0 48 8b 54 24 08 65 48 2b 14 25 28 00 00 00 0f 85 c0 00
[  426.740935] RSP: 0018:ffffa16dc0b7cd58 EFLAGS: 00010082
[  426.740939] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 0000000000000027
[  426.740941] RDX: ffff91d3ad7a0588 RSI: 0000000000000001 RDI: ffff91d3ad7a0580
[  426.740943] RBP: ffffa16dc0b7cd88 R08: 0000000000000003 R09: ffffa16dc0b7ccf0
[  426.740944] R10: 0000000000000022 R11: 0000000000000001 R12: ffffa16dc0b7cdc0
[  426.740946] R13: ffffffffc0dff1e0 R14: ffffa16dc1ac5fd0 R15: ffffa16dc0b7cdc0
[  426.740948] FS:  0000000000000000(0000) GS:ffff91d3ad780000(0000) knlGS:0000000000000000
[  426.740951] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  426.740953] CR2: 00007f55f6adb470 CR3: 00000001029b2000 CR4: 0000000000350ee0
[  426.740955] Call Trace:
[  426.740957]  <IRQ>
[  426.740961]  interrupt_is_wanted+0x15/0x20 [amdgpu]
[  426.741267]  kgd2kfd_interrupt+0xd7/0x230 [amdgpu]
[  426.741562]  amdgpu_amdkfd_interrupt+0x1a/0x30 [amdgpu]
[  426.741849]  amdgpu_irq_dispatch+0x17b/0x270 [amdgpu]
[  426.742124]  amdgpu_ih_process+0xa3/0x130 [amdgpu]
[  426.742391]  amdgpu_irq_handler+0x24/0x60 [amdgpu]
[  426.742656]  __handle_irq_event_percpu+0x42/0x170
[  426.742663]  handle_irq_event+0x59/0xb0
[  426.742668]  handle_edge_irq+0x8c/0x230
[  426.742671]  __common_interrupt+0x52/0xe0
[  426.742676]  common_interrupt+0x89/0xa0
[  426.742681]  </IRQ>
[  426.742682]  <TASK>
[  426.742683]  asm_common_interrupt+0x27/0x40
[  426.742687] RIP: 0010:cpuidle_enter_state+0xd9/0x620
[  426.742693] Code: 3d 04 aa d9 43 e8 a7 95 68 ff 49 89 c7 0f 1f 44 00 00 31 ff e8 e8 a2 68 ff 80 7d d0 00 0f 85 61 01 00 00 fb 66 0f 1f 44 00 00 <45> 85 f6 0f 88 6d 01 00 00 4d 63 ee 49 83 fd 09 0f 87 e7 03 00 00
[  426.742695] RSP: 0018:ffffa16dc0337e28 EFLAGS: 00000246
[  426.742698] RAX: ffff91d3ad7b0b80 RBX: ffff91955c5fc800 RCX: 0000000000000000
[  426.742699] RDX: 0000000000000000 RSI: 0000000000000002 RDI: 0000000000000000
[  426.742701] RBP: ffffa16dc0337e78 R08: 000000635bb1417b R09: 0000000000000000
[  426.742702] R10: 0000000000000001 R11: 071c71c71c71c71c R12: ffffffffbd8e6d00
[  426.742704] R13: 0000000000000001 R14: 0000000000000001 R15: 000000635bb1417b
[  426.742709]  ? cpuidle_enter_state+0xc8/0x620
[  426.742713]  ? tick_nohz_stop_tick+0x16a/0x1d0
[  426.742717]  cpuidle_enter+0x2e/0x50
[  426.742720]  cpuidle_idle_call+0x142/0x1e0
[  426.742725]  do_idle+0x83/0xf0
[  426.742727]  cpu_startup_entry+0x20/0x30
[  426.742730]  start_secondary+0x12a/0x180
[  426.742734]  secondary_startup_64_no_verify+0xc2/0xcb
[  426.742740]  </TASK>
[  426.742741] ---[ end trace e94cff342f635afd ]---
```

---

### 评论 #15 — illwieckz (2023-04-10T01:58:28Z)

Since the current `rocm-opencl` with current `amdgpu-dkms` doesn't wreck the kernel (even if faulty), let's consider this issue fixed. 👍️

I reported the remaining issue in another dedicated thread:

- https://github.com/RadeonOpenCompute/ROCm/issues/2032

---
