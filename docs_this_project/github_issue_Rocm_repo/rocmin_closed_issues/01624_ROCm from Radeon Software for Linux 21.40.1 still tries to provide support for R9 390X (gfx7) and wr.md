# ROCm from Radeon Software for Linux 21.40.1 still tries to provide support for R9 390X (gfx7) and wrecks the kernel

- **Issue #:** 1624
- **State:** closed
- **Created:** 2021-11-22T21:52:01Z
- **Updated:** 2023-04-10T01:58:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/1624

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