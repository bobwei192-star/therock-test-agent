# "kfd2kgd: amdgpu: failed to validate PT BOs"

> **Issue #365**
> **状态**: closed
> **创建时间**: 2018-03-18T20:22:44Z
> **更新时间**: 2018-06-03T13:20:14Z
> **关闭时间**: 2018-06-03T13:20:14Z
> **作者**: DiamondLovesYou
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/365

## 描述

I am unable to run `rocminfo`, let alone anything else related to this ecosystem, as this issue happens during initialization. I built all the packages from source and narrowed down the specific syscall to [this line]( https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/1f08bc194197107eb09b9af0bf37078b6bee67b2/src/fmm.c#L1491).

[dmesg](https://gist.github.com/DiamondLovesYou/3394875f3db5f5a9a5d1b8a32e0fb56c#file-dmesg)
[Linux .config](https://gist.github.com/DiamondLovesYou/3394875f3db5f5a9a5d1b8a32e0fb56c#file-config)

I'm using @fxkamd's branches of `ROCK-Kernel-Driver` and `ROCT-Thunk-Interface`, built from source.

My hardware is a Amd Ryzen 1950X on an ASUS ROG ZENITH EXTREME board. 64Gb RAM ECC, spread over 4 dimms, overclocked to 2933Mhz from 2400Mhz. MSI Radeon 580 8Gb, and an nvidia 1070Ti (this is blacklisted on the linux side, I use it exclusively for passthrough). No PCIe switches/bridges/etc.

The odd thing about my issue is that I have had ROCm working in the past, on older kernel versions.

Btw, what on Earth is a "BO"? I'm not finding any documentation on what exactly that is.

---

## 评论 (5 条)

### 评论 #1 — gstoner (2018-03-25T15:31:28Z)

BO = Buffered Object  I send this to KFD team 

---

### 评论 #2 — fxkamd (2018-03-26T18:17:31Z)

Hi @DiamondLovesYou, thanks for testing my experimental upstreaming branch. ;) I pushed a fix for a similar problem last Friday. See the patch below. If you git pull today, it should already include the fix. Could you give that a try?

(edit: removed the patch, github is really bad at formatting it. Here is a link to the [patch](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/commit/d98b285c73e07e0bc51ff810404b2f3b2774e903))

---

### 评论 #3 — DiamondLovesYou (2018-03-27T20:07:51Z)

I get an Oops. I updated the dmesg log in my gist linked inplace. The oops itself I've pasted here:
```
[  236.421417] BUG: unable to handle kernel NULL pointer dereference at 0000000000000018
[  236.421449] IP: gmc_v8_0_set_pte_pde+0x1b/0x30 [amdgpu]
[  236.421450] PGD 0 P4D 0 
[  236.421453] Oops: 0002 [#1] PREEMPT SMP
[  236.421455] Modules linked in: rfcomm nf_conntrack_netlink nfnetlink xfrm_user xfrm_algo xt_addrtype br_netfilter xt_CHECKSUM iptable_mangle ipt_MASQUERADE nf_nat_masquerade_ipv4 iptable_nat nf_nat_ipv4 nf_nat nf_conntrack_ipv4 nf_defrag_ipv4 xt_conntrack nf_conntrack libcrc32c ipt_REJECT nf_reject_ipv4 xt_tcpudp bridge stp llc ftdi_sio usbserial snd_usb_audio snd_usbmidi_lib ebtable_filter ebtables ip6table_filter ip6_tables iptable_filter cmac bnep binfmt_misc nls_iso8859_1 uas usb_storage eeepc_wmi asus_wmi wmi_bmof sparse_keymap video mxm_wmi snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm amd64_edac_mod snd_seq_midi edac_mce_amd snd_seq_midi_event kvm_amd snd_rawmidi kvm crct10dif_pclmul crc32_pclmul ghash_clmulni_intel
[  236.421485]  snd_seq pcbc snd_seq_device aesni_intel snd_timer aes_x86_64 crypto_simd glue_helper btusb cryptd btrtl btbcm btintel bluetooth snd joydev input_leds soundcore ccp ecdh_generic i2c_piix4 k10temp shpchp wmi vfio_pci vfio_virqfd irqbypass ip_tables x_tables autofs4 vfio_iommu_type1 vfio hid_generic usbhid hid amdkfd amdgpu chash gpu_sched ttm drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops igb ahci drm libahci dca ptp libata pps_core i2c_algo_bit gpio_amdpt gpio_generic pinctrl_amd
[  236.421511] CPU: 1 PID: 7692 Comm: rocminfo Not tainted 4.16.0-rc1+ #8
[  236.421513] Hardware name: System manufacturer System Product Name/ROG ZENITH EXTREME, BIOS 0902 12/21/2017
[  236.421535] RIP: 0010:gmc_v8_0_set_pte_pde+0x1b/0x30 [amdgpu]
[  236.421536] RSP: 0018:ffffbbca955c3ae8 EFLAGS: 00010202
[  236.421538] RAX: 000000fffffff000 RBX: 0000000000000001 RCX: 000000f400568001
[  236.421539] RDX: 0000000000000018 RSI: 0000000000000018 RDI: ffff9398d22c0000
[  236.421541] RBP: 000000f400568000 R08: 0000000000000001 R09: 0000000000000000
[  236.421542] R10: ffffffffc040bd90 R11: ffff9390d645d800 R12: 0000000000000018
[  236.421543] R13: 0000000000000000 R14: 0000000000000001 R15: ffffbbca955c3b58
[  236.421545] FS:  00007f0197861780(0000) GS:ffff9390de240000(0000) knlGS:0000000000000000
[  236.421546] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  236.421548] CR2: 0000000000000018 CR3: 000000079b999000 CR4: 00000000001406e0
[  236.421548] Call Trace:
[  236.421570]  amdgpu_vm_cpu_set_ptes+0x6b/0xf0 [amdgpu]
[  236.421590]  amdgpu_vm_update_directories+0x1c9/0x3e0 [amdgpu]
[  236.421609]  ? amdgpu_vm_free_mapping.isra.17+0x20/0x20 [amdgpu]
[  236.421634]  vm_update_pds+0x29/0x50 [amdgpu]
[  236.421658]  amdgpu_amdkfd_gpuvm_map_memory_to_gpu+0x2c3/0x5d0 [amdgpu]
[  236.421680]  ? amdgpu_amdkfd_gpuvm_alloc_memory_of_gpu+0xe1/0x920 [amdgpu]
[  236.421687]  kfd_process_alloc_gpuvm+0x86/0x1e0 [amdkfd]
[  236.421692]  kfd_process_device_init_vm.part.7+0xe7/0x200 [amdkfd]
[  236.421695]  ? __check_object_size+0xa5/0x1b0
[  236.421700]  kfd_ioctl_acquire_vm+0x98/0xb0 [amdkfd]
[  236.421704]  kfd_ioctl+0x225/0x3b0 [amdkfd]
[  236.421708]  ? kfd_ioctl_free_memory_of_gpu+0xc0/0xc0 [amdkfd]
[  236.421711]  ? unmap_region+0xd9/0x120
[  236.421714]  ? update_load_avg+0x56/0x640
[  236.421716]  ? update_curr+0x11f/0x190
[  236.421718]  ? update_curr+0x59/0x190
[  236.421721]  do_vfs_ioctl+0xa4/0x620
[  236.421724]  ? finish_task_switch+0xa4/0x280
[  236.421726]  ? __schedule+0x1af/0x700
[  236.421728]  SyS_ioctl+0x74/0x80
[  236.421731]  do_syscall_64+0x78/0x190
[  236.421734]  entry_SYSCALL_64_after_hwframe+0x21/0x86
[  236.421736] RIP: 0033:0x7f0196cf9ef7
[  236.421737] RSP: 002b:00007fff7a2d97e8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[  236.421739] RAX: ffffffffffffffda RBX: 0000000000000000 RCX: 00007f0196cf9ef7
[  236.421740] RDX: 00007fff7a2d9890 RSI: 0000000040084b15 RDI: 0000000000000003
[  236.421741] RBP: 00007fff7a2d9890 R08: 0000000000000004 R09: 0000000000000000
[  236.421742] R10: 000000000000055a R11: 0000000000000246 R12: 0000000040084b15
[  236.421743] R13: 0000000000000003 R14: 0000000000001000 R15: 0000564bb576e290
[  236.421745] Code: 8b 80 d8 00 00 00 e9 c5 4d 7e c5 0f 1f 44 00 00 0f 1f 44 00 00 48 b8 00 f0 ff ff ff 00 00 00 c1 e2 03 48 21 c1 48 01 f2 4c 09 c1 <48> 89 0a 31 c0 c3 0f 1f 44 00 00 66 2e 0f 1f 84 00 00 00 00 00 
[  236.421783] RIP: gmc_v8_0_set_pte_pde+0x1b/0x30 [amdgpu] RSP: ffffbbca955c3ae8
[  236.421784] CR2: 0000000000000018
[  236.421795] ---[ end trace e48a181303c0d3c1 ]---            
```

---

### 评论 #4 — fxkamd (2018-03-27T21:01:44Z)

I can't reproduce this problem. You can try working around it with by adding this parameter to your kernel command line (in grub): amdgpu.vm_update_mode=0

---

### 评论 #5 — DiamondLovesYou (2018-03-28T02:42:59Z)

That does it. No oops! And I see all the devices. Also, `vector_copy` works! Thanks!

---
