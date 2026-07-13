# OpenCL program triggers kernel module crash for X399 + 2 VEGA10 GPUs 

- **Issue #:** 758
- **State:** closed
- **Created:** 2019-04-09T16:46:19Z
- **Updated:** 2023-12-11T17:02:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/758

- CPU: Threadripper 1900x
- Memory: 64 GB
- GPU: 2 x VEGA10(VEGA56/VEGA64)
- X399 motherboard(stock setting + above 4G decoding enabled)
- ROCm 2.2
- OS: Both 16.04 and 18.04(kernel 4.15)

ROCm and OpenCL are installed with

```
$ sudo apt install rocm-dkms rocm-opencl-dev
```

I have encountered `amdgpu` kernel module crash when using OpenCL(e.g. `/opt/rocm/opencl/bin/x86_64/clinfo`) on 2 or more VEGA10 GPU installed on X399 motherboard. GPUs are connected with PCI-ex Gen3(x16 + x16 for 2 GPUs configuration)

- Single GPU works fine on ROCm OpenCL.
- OpenCL from AMDGPU pro driver(18.50) works fine for 2 VEGA10 GPUs configuration(clean install + amdgpu pro driver. No ROCm installed).

`dmesg` shows

```
BUG: unable to handle kernel NULL pointer dereference at 0000000000000000
```

so something is not well handled in ROCm 2.2 `amdgpu` driver?

Here is a snippet of `dmesg` log.

Ubuntu 16.04

```
[ 4965.835972] amdgpu 0000:43:00.0: [gfxhub] no-retry page fault (src_id:0 ring:170 vmid:8 pasid:32771, for process  pid 0 thread  pid 0)
[ 4965.835976] amdgpu 0000:43:00.0:   in page starting at address 0x0000000000000000 from 27
[ 4965.835977] amdgpu 0000:43:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x00840B54
[ 4965.835985] amdgpu 0000:43:00.0: [gfxhub] no-retry page fault (src_id:0 ring:154 vmid:8 pasid:32771, for process  pid 0 thread  pid 0)
[ 4965.835987] amdgpu 0000:43:00.0:   in page starting at address 0x0000000000000000 from 27
[ 4965.835988] amdgpu 0000:43:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x00800B34
[ 4965.835992] Evicting PASID 32771 queues
[ 4974.837675] qcm fence wait loop timeout expired
[ 4974.837676] The cp might be in an unrecoverable state due to an unsuccessful queues preemption
[ 4974.837681] amdgpu 0000:43:00.0: GPU reset begin!
[ 4974.837682] Evicting PASID 32771 queues
[ 4975.045759] BUG: unable to handle kernel NULL pointer dereference at 0000000000000000
[ 4975.045801] IP: soc15_baco_program_registers+0x6f/0x180 [amdgpu]
[ 4975.045802] PGD 467bff067 P4D 467bff067 PUD 45fd78067 PMD 0 
[ 4975.045805] Oops: 0000 [#1] SMP NOPTI
[ 4975.045806] Modules linked in: rfcomm bnep arc4 iwlmvm edac_mce_amd mac80211 kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc snd_hda_codec_realtek iwlwifi snd_hda_codec_generic aesni_intel snd_hda_codec_hdmi aes_x86_64 crypto_simd glue_helper cryptd cfg80211 snd_hda_intel snd_seq_midi snd_seq_midi_event btusb snd_hda_codec snd_rawmidi btrtl btbcm btintel snd_hda_core snd_hwdep bluetooth snd_seq snd_pcm ecdh_generic snd_seq_device snd_timer snd ccp soundcore i2c_piix4 wmi_bmof k10temp shpchp mac_hid parport_pc ppdev lp parport autofs4 amdgpu(OE) amdchash(OE) amdttm(OE) amd_sched(OE) mxm_wmi amdkcl(OE) amd_iommu_v2 drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops igb drm dca i2c_algo_bit atlantic ptp ahci pps_core libahci gpio_amdpt wmi gpio_generic
[ 4975.045838] CPU: 14 PID: 1588 Comm: kworker/14:0 Tainted: G           OE    4.15.0-47-generic #50~16.04.1-Ubuntu
[ 4975.045839] Hardware name: Gigabyte Technology Co., Ltd. X399 AORUS XTREME/X399 AORUS XTREME-CF, BIOS F5c 10/25/2018
[ 4975.045872] Workqueue: events kfd_process_hw_exception [amdgpu]
[ 4975.045906] RIP: 0010:soc15_baco_program_registers+0x6f/0x180 [amdgpu]
[ 4975.045907] RSP: 0018:ffffad6b11ee3cd0 EFLAGS: 00010283
[ 4975.045908] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 0000000000000000
[ 4975.045909] RDX: 0000000000000000 RSI: ffff9b2d545b0000 RDI: 0000000000000005
[ 4975.045910] RBP: ffffad6b11ee3d18 R08: 0000000000000000 R09: 0000000000000139
[ 4975.045911] R10: 0000000000000000 R11: 000000000000003a R12: 0000000000000000
[ 4975.045911] R13: ffff9b2d545b0000 R14: 0000000000000000 R15: ffffffffc080ab10
[ 4975.045913] FS:  0000000000000000(0000) GS:ffff9b2d5e580000(0000) knlGS:0000000000000000
[ 4975.045913] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 4975.045914] CR2: 0000000000000000 CR3: 00000004686b2000 CR4: 00000000003406e0
[ 4975.045915] Call Trace:
[ 4975.045949]  vega10_baco_set_state+0x75/0xe0 [amdgpu]
[ 4975.045982]  pp_set_asic_baco_state+0x5a/0x80 [amdgpu]
[ 4975.046010]  soc15_asic_reset+0xac/0x1a0 [amdgpu]
[ 4975.046034]  amdgpu_device_gpu_recover+0x403/0x900 [amdgpu]
[ 4975.046037]  ? __switch_to_asm+0x40/0x70
[ 4975.046067]  amdgpu_amdkfd_gpu_reset+0x20/0x30 [amdgpu]
[ 4975.046097]  kfd_process_hw_exception+0x18/0x20 [amdgpu]
[ 4975.046100]  process_one_work+0x14d/0x410
[ 4975.046101]  worker_thread+0x4b/0x460
[ 4975.046103]  kthread+0x105/0x140
[ 4975.046104]  ? process_one_work+0x410/0x410
[ 4975.046105]  ? kthread_destroy_worker+0x50/0x50
[ 4975.046107]  ret_from_fork+0x22/0x40
[ 4975.046108] Code: 8b 57 04 48 8b 75 c8 41 8b 5f 0c 41 8b 7f 18 45 8b 67 1c 45 8b 77 14 48 8d 04 40 48 8d 84 42 50 1a 00 00 41 8b 57 08 48 8b 04 c6 <03> 1c 90 41 83 7f fc 04 41 8b 47 10 89 45 d4 0f 87 dd 00 00 00 
[ 4975.046155] RIP: soc15_baco_program_registers+0x6f/0x180 [amdgpu] RSP: ffffad6b11ee3cd0
[ 4975.046156] CR2: 0000000000000000
[ 4975.046157] ---[ end trace e9fbabfbe54ce83a ]---
[ 5028.316832] [drm] schedpage0 is not ready, skipping
[ 5028.316835] [drm] schedpage1 is not ready, skipping
[ 5028.316894] [drm:amdgpu_gem_va_ioctl [amdgpu]] *ERROR* Couldn't update BO_VA (-2)
[ 5028.316918] BUG: unable to handle kernel NULL pointer dereference at 0000000000000008
[ 5028.316972] IP: amdgpu_vm_bo_update_mapping+0x100/0x430 [amdgpu]
[ 5028.316974] PGD 0 P4D 0 
[ 5028.316978] Oops: 0000 [#2] SMP NOPTI
[ 5028.316980] Modules linked in: rfcomm bnep arc4 iwlmvm edac_mce_amd mac80211 kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc snd_hda_codec_realtek iwlwifi snd_hda_codec_generic aesni_intel snd_hda_codec_hdmi aes_x86_64 crypto_simd glue_helper cryptd cfg80211 snd_hda_intel snd_seq_midi snd_seq_midi_event btusb snd_hda_codec snd_rawmidi btrtl btbcm btintel snd_hda_core snd_hwdep bluetooth snd_seq snd_pcm ecdh_generic snd_seq_device snd_timer snd ccp soundcore i2c_piix4 wmi_bmof k10temp shpchp mac_hid parport_pc ppdev lp parport autofs4 amdgpu(OE) amdchash(OE) amdttm(OE) amd_sched(OE) mxm_wmi amdkcl(OE) amd_iommu_v2 drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops igb drm dca i2c_algo_bit atlantic ptp ahci pps_core libahci gpio_amdpt wmi gpio_generic
[ 5028.317026] CPU: 10 PID: 1134 Comm: Xorg Tainted: G      D    OE    4.15.0-47-generic #50~16.04.1-Ubuntu
[ 5028.317028] Hardware name: Gigabyte Technology Co., Ltd. X399 AORUS XTREME/X399 AORUS XTREME-CF, BIOS F5c 10/25/2018
[ 5028.317078] RIP: 0010:amdgpu_vm_bo_update_mapping+0x100/0x430 [amdgpu]
[ 5028.317080] RSP: 0018:ffffad6b11a1fac8 EFLAGS: 00010246
[ 5028.317082] RAX: 0000000000000000 RBX: ffff9b2d52337800 RCX: 0000000000000000
[ 5028.317084] RDX: 0000000000000000 RSI: 0000000000000000 RDI: ffffad6b11a1fb50
[ 5028.317085] RBP: ffffad6b11a1fb80 R08: 0000000000102f7f R09: 0000000000102f7f
[ 5028.317087] R10: ffff9b2d58e16798 R11: ffff9b2d545b0000 R12: 0000000000000000
[ 5028.317088] R13: ffffad6b11a1fb18 R14: 0000000000000000 R15: 0000000000102f60
[ 5028.317090] FS:  00007f726a76fa00(0000) GS:ffff9b2d5e480000(0000) knlGS:0000000000000000
[ 5028.317092] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 5028.317094] CR2: 0000000000000008 CR3: 0000000c5290e000 CR4: 00000000003406e0
[ 5028.317095] Call Trace:
[ 5028.317110]  ? add_hole+0xd3/0x100 [drm]
[ 5028.317114]  ? _cond_resched+0x1a/0x50
[ 5028.317163]  amdgpu_vm_clear_freed+0xbd/0x1b0 [amdgpu]
[ 5028.317211]  amdgpu_gem_va_ioctl+0x42e/0x560 [amdgpu]
[ 5028.317259]  ? amdgpu_gem_metadata_ioctl+0x1d0/0x1d0 [amdgpu]
[ 5028.317270]  drm_ioctl_kernel+0x6b/0xb0 [drm]
[ 5028.317281]  ? drm_ioctl_kernel+0x6b/0xb0 [drm]
[ 5028.317292]  drm_ioctl+0x3e4/0x450 [drm]
[ 5028.317339]  ? amdgpu_gem_metadata_ioctl+0x1d0/0x1d0 [amdgpu]
[ 5028.317343]  ? vfs_writev+0xb9/0x110
[ 5028.317387]  amdgpu_drm_ioctl+0x4c/0x80 [amdgpu]
[ 5028.317391]  do_vfs_ioctl+0xa4/0x600
[ 5028.317394]  ? __sys_recvmsg+0x80/0x90
[ 5028.317397]  SyS_ioctl+0x79/0x90
[ 5028.317401]  do_syscall_64+0x73/0x130
[ 5028.317404]  entry_SYSCALL_64_after_hwframe+0x3d/0xa2
[ 5028.317406] RIP: 0033:0x7f7268194f47
[ 5028.317407] RSP: 002b:00007fffa4977468 EFLAGS: 00003246 ORIG_RAX: 0000000000000010
[ 5028.317410] RAX: ffffffffffffffda RBX: 0000000000020fff RCX: 00007f7268194f47
[ 5028.317411] RDX: 00007fffa49774b0 RSI: 00000000c0286448 RDI: 000000000000000e
[ 5028.317413] RBP: 00007fffa49774b0 R08: 0000000102f60000 R09: 000000000000000e
[ 5028.317414] R10: 0000000000000002 R11: 0000000000003246 R12: 00000000c0286448
[ 5028.317415] R13: 000000000000000e R14: 0000000000000002 R15: 000055b142b384d8
[ 5028.317417] Code: 48 33 1c 25 28 00 00 00 0f 85 3c 03 00 00 48 81 c4 90 00 00 00 5b 41 5c 41 5d 41 5e 41 5f 5d c3 48 8b 83 d0 00 00 00 44 8b 45 80 <48> 8b 40 08 45 29 f8 45 8d 48 01 48 89 85 48 ff ff ff 48 8b 83 
[ 5028.317495] RIP: amdgpu_vm_bo_update_mapping+0x100/0x430 [amdgpu] RSP: ffffad6b11a1fac8
[ 5028.317496] CR2: 0000000000000008
[ 5028.317498] ---[ end trace e9fbabfbe54ce83b ]---
```

Ubuntu 18.04
```
...
[  326.326176] amdgpu 0000:43:00.0: [gfxhub] no-retry page fault (src_id:0 ring:170 vmid:8 pasid:32768, for process  pid 0 thread  pid 0)
[  326.326179] amdgpu 0000:43:00.0:   in page starting at address 0x0000000000000000 from 27
[  326.326181] amdgpu 0000:43:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x00840B54
[  326.326190] amdgpu 0000:43:00.0: [gfxhub] no-retry page fault (src_id:0 ring:154 vmid:8 pasid:32768, for process  pid 0 thread  pid 0)
[  326.326192] amdgpu 0000:43:00.0:   in page starting at address 0x0000000000000000 from 27
[  326.326193] amdgpu 0000:43:00.0: VM_L2_PROTECTION_FAULT_STATUS:0x00800B34
[  326.326203] Evicting PASID 32768 queues
[  335.328342] qcm fence wait loop timeout expired
[  335.328345] The cp might be in an unrecoverable state due to an unsuccessful queues preemption
[  335.328352] amdgpu 0000:43:00.0: GPU reset begin!
[  335.328355] Evicting PASID 32768 queues
[  335.516507] BUG: unable to handle kernel NULL pointer dereference at 0000000000000000
[  335.516549] IP: soc15_baco_program_registers+0x6c/0x180 [amdgpu]
[  335.516551] PGD ff4e3b067 P4D ff4e3b067 PUD 102e691067 PMD 0 
[  335.516554] Oops: 0000 [#1] SMP NOPTI
[  335.516555] Modules linked in: cmac bnep arc4 nls_iso8859_1 amdgpu(OE) amdchash(OE) amdttm(OE) amd_sched(OE) snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi snd_hda_intel iwlmvm snd_hda_codec snd_hda_core snd_hwdep mac80211 snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi amdkcl(OE) iwlwifi amd_iommu_v2 snd_seq joydev input_leds drm_kms_helper cfg80211 snd_seq_device drm snd_timer fb_sys_fops syscopyarea ccp wmi_bmof sysfillrect edac_mce_amd sysimgblt snd kvm mxm_wmi irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc btusb aesni_intel btrtl btbcm aes_x86_64 btintel crypto_simd glue_helper bluetooth cryptd soundcore k10temp ecdh_generic shpchp mac_hid wmi sch_fq_codel sunrpc parport_pc ppdev lp parport ip_tables x_tables autofs4 igb i2c_algo_bit i2c_piix4 dca atlantic
[  335.516588]  ptp ahci pps_core libahci gpio_amdpt gpio_generic hid_generic usbhid hid
[  335.516593] CPU: 11 PID: 181 Comm: kworker/11:1 Tainted: G           OE    4.15.0-47-generic #50-Ubuntu
[  335.516594] Hardware name: Gigabyte Technology Co., Ltd. X399 AORUS XTREME/X399 AORUS XTREME-CF, BIOS F5c 10/25/2018
[  335.516623] Workqueue: events kfd_process_hw_exception [amdgpu]
[  335.516653] RIP: 0010:soc15_baco_program_registers+0x6c/0x180 [amdgpu]
[  335.516654] RSP: 0018:ffffaecc074a3ce8 EFLAGS: 00010206
[  335.516655] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 0000000000000000
[  335.516656] RDX: 0000000000000000 RSI: ffffa089106c0000 RDI: 0000000000000005
[  335.516657] RBP: ffffaecc074a3d30 R08: 00000000000001aa R09: 0000000000000000
[  335.516658] R10: 0000000000000000 R11: 00000000003d0900 R12: 0000000000000000
[  335.516659] R13: 0000000000000000 R14: ffffa089106c0000 R15: ffffffffc0f7996c
[  335.516660] FS:  0000000000000000(0000) GS:ffffa0893cac0000(0000) knlGS:0000000000000000
[  335.516661] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  335.516662] CR2: 0000000000000000 CR3: 0000000fff960000 CR4: 00000000003406e0
[  335.516663] Call Trace:
[  335.516692]  vega10_baco_set_state+0x7b/0xe0 [amdgpu]
[  335.516719]  pp_set_asic_baco_state+0x5a/0x80 [amdgpu]
[  335.516743]  soc15_asic_reset+0xac/0x1a0 [amdgpu]
[  335.516762]  amdgpu_device_gpu_recover+0x182/0x8a0 [amdgpu]
[  335.516766]  ? __switch_to_asm+0x40/0x70
[  335.516792]  amdgpu_amdkfd_gpu_reset+0x20/0x30 [amdgpu]
[  335.516819]  kfd_process_hw_exception+0x18/0x20 [amdgpu]
[  335.516821]  process_one_work+0x1de/0x410
[  335.516823]  worker_thread+0x32/0x410
[  335.516825]  kthread+0x121/0x140
[  335.516826]  ? process_one_work+0x410/0x410
[  335.516827]  ? kthread_create_worker_on_cpu+0x70/0x70
[  335.516829]  ret_from_fork+0x22/0x40
[  335.516830] Code: 8b 57 08 48 8b 75 c8 41 8b 5f 10 41 8b 7f 1c 45 8b 67 20 45 8b 6f 18 48 8d 04 40 48 8d 84 42 50 1a 00 00 41 8b 57 0c 48 8b 04 c6 <03> 1c 90 41 83 3f 04 41 8b 47 14 89 45 d4 0f 87 dc 00 00 00 41 
[  335.516872] RIP: soc15_baco_program_registers+0x6c/0x180 [amdgpu] RSP: ffffaecc074a3ce8
[  335.516873] CR2: 0000000000000000
[  335.516874] ---[ end trace ed08de0507622c04 ]---
```