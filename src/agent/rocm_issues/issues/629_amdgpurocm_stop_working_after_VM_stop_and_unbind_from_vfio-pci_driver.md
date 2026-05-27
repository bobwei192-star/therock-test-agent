# amdgpu/rocm stop working after VM stop and unbind from vfio-pci driver

> **Issue #629**
> **状态**: closed
> **创建时间**: 2018-11-30T01:36:00Z
> **更新时间**: 2024-07-25T14:41:44Z
> **关闭时间**: 2024-07-25T14:41:44Z
> **作者**: Avatat
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/629

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Hi,
I use ROCm (1.9.307) on:
Ubuntu 18.10 with 4.19.5-041905-generic Kernel
E5-1650 v2, 32 GB RAM
Radeon RX 480 8 GB

Sometimes I need unbind GPU from amdgpu driver and use it in VM (QEMU 3.0.93, libvirt 4.6.0). To this moment, everything works great, but...
When I stop VM, libvirt unbind all devices (including GPU) from vfio-pci driver and rebind it back to the original ones. It works for USB controller and soundcard, but ROCm is crashing when I'm trying to use it's tools:
```
# rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104

# clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```

`rocm-smi` is crashing too, but it break all driver/kernel. Dmesg after `rocm-smi` run:
```
[ 3347.631574] BUG: unable to handle kernel paging request at ffff8f42872e9254
[ 3347.631598] PGD 4cea01067 P4D 4cea01067 PUD 0
[ 3347.631612] Oops: 0000 [#1] SMP PTI
[ 3347.631624] CPU: 0 PID: 3822 Comm: python Not tainted 4.19.5-041905-generic #201811271131
[ 3347.631646] Hardware name: Hewlett-Packard HP Z420 Workstation/1589, BIOS J61 v03.94 07/10/2018
[ 3347.631718] RIP: 0010:smu7_get_sclk_od+0x1e/0x40 [amdgpu]
[ 3347.631733] Code: 01 48 89 e5 5d c3 66 0f 1f 44 00 00 0f 1f 44 00 00 48 8b 87 a0 01 00 00 55 8b 90 58 02 00 00 48 89 e5 5d 83 ea 01 48 8d 14 52 <8b> 8c 90 60 02 00 00 8b 10 83 ea 01 48 8d 14 52 8b 44 90 08 31 d2
[ 3347.631780] RSP: 0018:ffffb7d784af3cf0 EFLAGS: 00010297
[ 3347.631795] RAX: ffff8f36872e9000 RBX: ffff8f3683e02400 RCX: 0000000000000000
[ 3347.631826] RDX: 00000002fffffffd RSI: ffffffffc0b88120 RDI: ffff8f3683e02400
[ 3347.631845] RBP: ffffb7d784af3d08 R08: ffff8f368abbc0b8 R09: ffff8f36815db540
[ 3347.631864] R10: ffffb7d784af3e60 R11: ffff8f36876c9200 R12: ffff8f3683e02418
[ 3347.631883] R13: 00000000ffffffff R14: ffff8f3683196000 R15: 0000000000000001
[ 3347.631903] FS:  00007f29a709a740(0000) GS:ffff8f368f800000(0000) knlGS:0000000000000000
[ 3347.631924] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 3347.631940] CR2: ffff8f42872e9254 CR3: 0000000803a54003 CR4: 00000000001606f0
[ 3347.631959] Call Trace:
[ 3347.632003]  ? pp_dpm_get_sclk_od+0x51/0x70 [amdgpu]
[ 3347.632042]  amdgpu_get_pp_sclk_od+0x36/0x60 [amdgpu]
[ 3347.632059]  dev_attr_show+0x21/0x50
[ 3347.632071]  sysfs_kf_seq_show+0xa4/0x130
[ 3347.632085]  kernfs_seq_show+0x27/0x30
[ 3347.632097]  seq_read+0x157/0x400
[ 3347.632107]  kernfs_fop_read+0x35/0x180
[ 3347.632120]  __vfs_read+0x3a/0x180
[ 3347.632131]  ? security_file_permission+0x93/0xc0
[ 3347.632145]  ? security_file_permission+0x93/0xc0
[ 3347.632159]  vfs_read+0x8f/0x140
[ 3347.632169]  ksys_read+0x55/0xc0
[ 3347.632180]  __x64_sys_read+0x1a/0x20
[ 3347.632192]  do_syscall_64+0x5a/0x110
[ 3347.632205]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[ 3347.632219] RIP: 0033:0x7f29a757ef31
[ 3347.632230] Code: fe ff ff 50 48 8d 3d 46 6e 0a 00 e8 59 35 02 00 66 0f 1f 84 00 00 00 00 00 48 8d 05 c9 f7 0d 00 8b 00 85 c0 75 13 31 c0 0f 05 <48> 3d 00 f0 ff ff 77 57 c3 66 0f 1f 44 00 00 41 54 49 89 d4 55 48
[ 3347.632277] RSP: 002b:00007fff4820cfa8 EFLAGS: 00000246 ORIG_RAX: 0000000000000000
[ 3347.632298] RAX: ffffffffffffffda RBX: 0000564deda4bbc0 RCX: 00007f29a757ef31
[ 3347.632317] RDX: 0000000000001000 RSI: 0000564deda5f704 RDI: 0000000000000003
[ 3347.632336] RBP: 00007f29a76562a0 R08: 0000564ded8c7010 R09: 0000000000000000
[ 3347.632355] R10: 0000000000000070 R11: 0000000000000246 R12: 0000000000001001
[ 3347.632374] R13: 0000564deda5f704 R14: 0000000000000d68 R15: 00007f29a7655760
[ 3347.632393] Modules linked in: vhost_net vhost tap vfio_pci vfio_virqfd vfio_iommu_type1 vfio xt_conntrack ipt_REJECT nf_reject_ipv4 devlink ebtable_filter ebtables ip6table_filter ip6_tables xt_CHECKSUM iptable_mangle ipt_MASQUERADE iptable_nat nf_nat_ipv4 nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 xt_tcpudp iptable_filter bpfilter bridge stp llc nls_iso8859_1 intel_rapl sb_edac x86_pkg_temp_thermal intel_powerclamp coretemp kvm_intel snd_hda_codec_hdmi kvm snd_hda_codec_realtek snd_hda_codec_generic irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_intel snd_hda_codec intel_cstate snd_hda_core snd_hwdep joydev intel_rapl_perf snd_pcm input_leds snd_timer hp_wmi snd serio_raw sparse_keymap wmi_bmof soundcore ioatdma dca tpm_infineon mac_hid sch_fq_codel ib_iser rdma_cm iw_cm
[ 3347.632602]  ib_cm ib_core iscsi_tcp libiscsi_tcp libiscsi scsi_transport_iscsi ip_tables x_tables autofs4 btrfs zstd_compress raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu chash gpu_sched i2c_algo_bit ttm drm_kms_helper aesni_intel syscopyarea aes_x86_64 sysfillrect crypto_simd sysimgblt cryptd glue_helper fb_sys_fops psmouse isci firewire_ohci drm ahci e1000e firewire_core libsas i2c_i801 libahci lpc_ich crc_itu_t scsi_transport_sas wmi
[ 3347.632758] CR2: ffff8f42872e9254
[ 3347.632768] ---[ end trace 8e1013ea8741c463 ]---
[ 3347.632815] RIP: 0010:smu7_get_sclk_od+0x1e/0x40 [amdgpu]
[ 3347.632830] Code: 01 48 89 e5 5d c3 66 0f 1f 44 00 00 0f 1f 44 00 00 48 8b 87 a0 01 00 00 55 8b 90 58 02 00 00 48 89 e5 5d 83 ea 01 48 8d 14 52 <8b> 8c 90 60 02 00 00 8b 10 83 ea 01 48 8d 14 52 8b 44 90 08 31 d2
[ 3347.632877] RSP: 0018:ffffb7d784af3cf0 EFLAGS: 00010297
[ 3347.632892] RAX: ffff8f36872e9000 RBX: ffff8f3683e02400 RCX: 0000000000000000
[ 3347.632911] RDX: 00000002fffffffd RSI: ffffffffc0b88120 RDI: ffff8f3683e02400
[ 3347.632930] RBP: ffffb7d784af3d08 R08: ffff8f368abbc0b8 R09: ffff8f36815db540
[ 3347.632949] R10: ffffb7d784af3e60 R11: ffff8f36876c9200 R12: ffff8f3683e02418
[ 3347.632968] R13: 00000000ffffffff R14: ffff8f3683196000 R15: 0000000000000001
[ 3347.632987] FS:  00007f29a709a740(0000) GS:ffff8f368f800000(0000) knlGS:0000000000000000
[ 3347.633020] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 3347.633035] CR2: ffff8f42872e9254 CR3: 0000000803a54003 CR4: 00000000001606f0
```

What can I do with that? I can't test in on newer 4.20 rc4 Kernel, because ROCm is not working on it...

---

## 评论 (9 条)

### 评论 #1 — maxcr (2018-11-30T15:18:44Z)

I remember reading somewhere on the level1 forums that you need to set a manual reset command because VFIO can become bugged in guest OS and does not release control. High level shit, not ROCm problem buddy.

---

### 评论 #2 — maxcr (2018-11-30T15:28:44Z)

https://wiki.archlinux.org/index.php/PCI_passthrough_via_OVMF#Passing_through_a_device_that_does_not_support_resetting

---

### 评论 #3 — Avatat (2018-11-30T15:53:42Z)

But my RX 480 has `/sys/bus/pci/devices/0000\:05\:00.0/reset` file, and VM shutdown correctly, GPU bind correctly to `amdgpu`, I can see Ubuntu terminal on a monitor connected to the GPU.

It's `amdgpu` related problem I think: `[ 3347.631718] RIP: 0010:smu7_get_sclk_od+0x1e/0x40 [amdgpu]`.

---

### 评论 #4 — TheGoddessInari (2018-12-02T08:02:32Z)

`amdgpu` doesn't correctly support hot removal of a GPU currently. I'm really hoping that it and #603 can get taken care of in a reasonable time-frame, as it really limits the usefulness of ROCM/amdgpu in a multi-use/development system.

AFAIK, there's nothing pending in 4.20 or even the current 4.21-WIP tree that improves the situation at all.

---

### 评论 #5 — Avatat (2018-12-02T08:51:54Z)

Probably it has low priority because users group who use AMD GPU for computing and gaming at one time is very small ;)
A simple workaround is to compute inside VM with redirected GPU or reboot the computer after done work on VM with GPU.

---

### 评论 #6 — aqxa1 (2021-05-20T12:24:01Z)

I'm not sure if it's exactly the same issue, but this affects the RX 6800 as well (which doesn't have the reset bug), albeit with slightly different symptoms. Rocminfo:

```
ROCk module is loaded
Unable to open /dev/kfd read-write: Resource temporarily unavailable
```
The issue only occurs after using the GPU in a VM. Affects both 5.11.21 and 5.12.4 kernels. And ROCM is the only part of the GPU that fails to work; normal GPU operations (gaming/videos/etc) work perfectly after returning from the VM.

---

### 评论 #7 — dedani (2023-07-16T13:09:27Z)

this is still true in mid 2023.

I'd like to change drivers from `vfio-pci` to `amdgpu` and back, doing it once will just make ROCM stop working. All other things will work ok, such as using the device in a VM (after changing the driver back etc...). E.g. running a ROCM blender benchmark will no longer list *any* amd gpus.

This is what I do for switching.
```
NEWDRIVER=vfio-pci
OLDDRIVER=amdgpu
PCIE=08:00.0
echo $NEWDRIVER > /sys/bus/pci/devices/0000\:$PCIE/driver_override
echo 0000:$PCIE > /sys/bus/pci/drivers/$OLDDRIVER/unbind
echo 0000:$PCIE > /sys/bus/pci/drivers_probe
```

```
# sudo lspci -nnk | egrep -A3 "VGA|Display|3D"
08:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 23 WKS-XL [Radeon PRO W6600] [1002:73e3]
Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:0e0c]
Kernel driver in use: **amdgpu or vfio-pci**
Kernel modules: amdgpu
--
10:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 22 [Radeon RX 6700/6700 XT/6750 XT / 6800M/6850M XT] [1002:73df] (rev c1)
Subsystem: Gigabyte Technology Co., Ltd Device [1458:232d]
Kernel driver in use: amdgpu
Kernel modules: amdgpu
```

If I now start a VM with the card in `08:00.0` it all works fine. In the host, however I can no longer do any ROCM things.

```
# rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Resource temporarily unavailable
dani is member of render group
```

`dmesg` gives:

```
[  200.125286] amdgpu 0000:08:00.0: amdgpu: amdgpu: finishing device.
[  200.131168] ------------[ cut here ]------------
[  200.131170] WARNING: CPU: 9 PID: 3649 at drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c:599 amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.131422] Modules linked in: snd_seq_dummy snd_hrtimer snd_seq rfcomm zram wireguard libchacha20poly1305 chacha_x86_64 poly1305_x86_64 curve25519_x86_64 libcurve25519_generic libchacha ip6_udp_tunnel udp_tunnel af_packet nft_fib_inet nft_fib_ipv4 nft_fib_ipv6 nft_fib nft_reject_inet nf_reject_ipv4 nf_reject_ipv6 nft_reject nft_ct nft_chain_nat nf_tables ebtable_nat ebtable_broute ip6table_nat ip6table_mangle ip6table_raw ip6table_security iptable_nat nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 iptable_mangle iptable_raw iptable_security ip_set nfnetlink ebtable_filter ebtables ip6table_filter ip6_tables iptable_filter bpfilter qrtr cmac algif_hash algif_skcipher af_alg bnep nls_iso8859_1 nls_cp437 vfat fat iwlmvm mac80211 snd_hda_codec_realtek snd_hda_codec_generic libarc4 ledtrig_audio snd_hda_codec_hdmi uvcvideo videobuf2_vmalloc uvc videobuf2_memops btusb snd_hda_intel videobuf2_v4l2 btrtl snd_intel_dspcfg snd_intel_sdw_acpi snd_usb_audio btbcm videodev snd_hda_codec btintel snd_usbmidi_lib btmtk iwlwifi
[  200.131452]  intel_rapl_msr snd_rawmidi it87 snd_hda_core videobuf2_common intel_rapl_common snd_seq_device snd_hwdep bluetooth mc hwmon_vid edac_mce_amdgigabyte_wmi snd_pcm wmi_bmof mxm_wmi pcspkr cfg80211 snd_timer acpi_cpufreq k10temp efi_pstore i2c_piix4 ecdh_generic snd igb soundcore joydev dca rfkill tiny_power_button thermal button fuse configfs dmi_sysfs ip_tables x_tables hid_generic usbhid amdgpu crct10dif_pclmul crc32_pclmul polyval_clmulni polyval_generic gf128mul ghash_clmulni_intel sha512_ssse3 i2c_algo_bit drm_ttm_helper ttm video drm_suballoc_helper iommu_v2 xhci_pci xhci_pci_renesas drm_buddy gpu_sched xhci_hcd aesni_intel drm_display_helper crypto_simd cryptd cec nvme sp5100_tco usbcore rc_core nvme_core wmi btrfs blake2b_generic libcrc32c crc32c_intel xor sg dm_multipath dm_mod raid6_pq scsi_dh_rdac scsi_dh_emc scsi_dh_alua msr kvm_amd ccp kvm vfio_pci vfio_pci_core vfio_iommu_type1 vfio irqbypass efivarfs
[  200.131487] CPU: 9 PID: 3649 Comm: bash Not tainted 6.4.2-1-default #1 openSUSE Tumbleweed 44279f67043987f2a4149a1dd94f4478c9404e2a
[  200.131489] Hardware name: Gigabyte Technology Co., Ltd. X570 AORUS MASTER/X570 AORUS MASTER, BIOS F37b 02/08/2023
[  200.131490] RIP: 0010:amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.131724] Code: c0 74 33 48 8b 4e 10 48 83 39 00 74 29 89 d1 48 8d 04 88 8b 08 85 c9 74 11 f0 ff 08 74 07 31 c0 c3 cc cc cc cc e9 6a fd ff ff <0f> 0b b8 ea ff ff ff c3 cc cc cc cc b8 ea ff ff ff c3 cc cc cc cc
[  200.131726] RSP: 0018:ffffa22446e9fc68 EFLAGS: 00010246
[  200.131727] RAX: ffff925b40343a00 RBX: ffff925b01900000 RCX: 0000000000000000
[  200.131728] RDX: 0000000000000000 RSI: ffff925b01919250 RDI: ffff925b01900000
[  200.131729] RBP: ffff925b01925de2 R08: 0000000000000000 R09: ffffffff9746fa40
[  200.131730] R10: 0000000000000000 R11: 0000000000000000 R12: ffff925b01900010
[  200.131731] R13: ffff925b01925d72 R14: ffff92698f07a150 R15: ffff925b478ae620
[  200.131731] FS:  00007f1226087540(0000) GS:ffff92698e680000(0000) knlGS:0000000000000000
[  200.131733] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  200.131734] CR2: 00007f06dc50f380 CR3: 00000001f66e6000 CR4: 0000000000750ee0
[  200.131734] PKRU: 55555554
[  200.131735] Call Trace:
[  200.131737]  <TASK>
[  200.131738]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.131978]  ? __warn+0x81/0x130
[  200.131982]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.132213]  ? report_bug+0x171/0x1a0
[  200.132216]  ? handle_bug+0x3c/0x80
[  200.132219]  ? exc_invalid_op+0x17/0x70
[  200.132222]  ? asm_exc_invalid_op+0x1a/0x20
[  200.132224]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.132454]  gfx_v10_0_hw_fini+0x1e/0x160 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.132679]  amdgpu_device_fini_hw+0x1ed/0x330 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.132832]  ? blocking_notifier_chain_unregister+0x36/0x50
[  200.132834]  amdgpu_pci_remove+0x51/0x140 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.132985]  ? __pm_runtime_resume+0x58/0x80
[  200.132987]  pci_device_remove+0x3a/0xa0
[  200.132990]  device_release_driver_internal+0x19f/0x200
[  200.132993]  unbind_store+0xa1/0xb0
[  200.132995]  kernfs_fop_write_iter+0x136/0x1d0
[  200.132997]  vfs_write+0x1ef/0x3b0
[  200.133000]  ksys_write+0x67/0xe0
[  200.133002]  do_syscall_64+0x60/0x90
[  200.133003]  ? do_syscall_64+0x6c/0x90
[  200.133005]  ? do_dup2+0x88/0xc0
[  200.133007]  ? syscall_exit_to_user_mode+0x1b/0x40
[  200.133009]  ? do_syscall_64+0x6c/0x90
[  200.133010]  ? do_syscall_64+0x6c/0x90
[  200.133011]  ? do_syscall_64+0x6c/0x90
[  200.133012]  ? do_syscall_64+0x6c/0x90
[  200.133014]  entry_SYSCALL_64_after_hwframe+0x72/0xdc
[  200.133015] RIP: 0033:0x7f12261c5184
[  200.133036] Code: ff eb b7 0f 1f 00 90 90 90 90 90 90 90 90 90 90 90 90 90 90 f3 0f 1e fa 90 90 80 3d fd 29 0f 00 00 74 13 b8 01 00 00 00 0f 05 <48> 3d 00 f0 ff ff 77 54 c3 0f 1f 00 48 83 ec 28 48 89 54 24 18 48
[  200.133037] RSP: 002b:00007ffdf0ff4c78 EFLAGS: 00000202 ORIG_RAX: 0000000000000001
[  200.133038] RAX: ffffffffffffffda RBX: 000000000000000d RCX: 00007f12261c5184
[  200.133039] RDX: 000000000000000d RSI: 000055942c5e4100 RDI: 0000000000000001
[  200.133039] RBP: 000055942c5e4100 R08: 0000000000000073 R09: 0000000000000001
[  200.133040] R10: 0000000000000000 R11: 0000000000000202 R12: 000000000000000d
[  200.133040] R13: 00007f12262aa780 R14: 000000000000000d R15: 00007f12262a5d60
[  200.133042]  </TASK>
[  200.133042] ---[ end trace 0000000000000000 ]---
[  200.133051] ------------[ cut here ]------------
[  200.133051] WARNING: CPU: 9 PID: 3649 at drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c:599 amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.133226] Modules linked in: snd_seq_dummy snd_hrtimer snd_seq rfcomm zram wireguard libchacha20poly1305 chacha_x86_64 poly1305_x86_64 curve25519_x86_64 libcurve25519_generic libchacha ip6_udp_tunnel udp_tunnel af_packet nft_fib_inet nft_fib_ipv4 nft_fib_ipv6 nft_fib nft_reject_inet nf_reject_ipv4 nf_reject_ipv6 nft_reject nft_ct nft_chain_nat nf_tables ebtable_nat ebtable_broute ip6table_nat ip6table_mangle ip6table_raw ip6table_security iptable_nat nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 iptable_mangle iptable_raw iptable_security ip_set nfnetlink ebtable_filter ebtables ip6table_filter ip6_tables iptable_filter bpfilter qrtr cmac algif_hash algif_skcipher af_alg bnep nls_iso8859_1 nls_cp437 vfat fat iwlmvm mac80211 snd_hda_codec_realtek snd_hda_codec_generic libarc4 ledtrig_audio snd_hda_codec_hdmi uvcvideo videobuf2_vmalloc uvc videobuf2_memops btusb snd_hda_intel videobuf2_v4l2 btrtl snd_intel_dspcfg snd_intel_sdw_acpi snd_usb_audio btbcm videodev snd_hda_codec btintel snd_usbmidi_lib btmtk iwlwifi
[  200.133244]  intel_rapl_msr snd_rawmidi it87 snd_hda_core videobuf2_common intel_rapl_common snd_seq_device snd_hwdep bluetooth mc hwmon_vid edac_mce_amdgigabyte_wmi snd_pcm wmi_bmof mxm_wmi pcspkr cfg80211 snd_timer acpi_cpufreq k10temp efi_pstore i2c_piix4 ecdh_generic snd igb soundcore joydev dca rfkill tiny_power_button thermal button fuse configfs dmi_sysfs ip_tables x_tables hid_generic usbhid amdgpu crct10dif_pclmul crc32_pclmul polyval_clmulni polyval_generic gf128mul ghash_clmulni_intel sha512_ssse3 i2c_algo_bit drm_ttm_helper ttm video drm_suballoc_helper iommu_v2 xhci_pci xhci_pci_renesas drm_buddy gpu_sched xhci_hcd aesni_intel drm_display_helper crypto_simd cryptd cec nvme sp5100_tco usbcore rc_core nvme_core wmi btrfs blake2b_generic libcrc32c crc32c_intel xor sg dm_multipath dm_mod raid6_pq scsi_dh_rdac scsi_dh_emc scsi_dh_alua msr kvm_amd ccp kvm vfio_pci vfio_pci_core vfio_iommu_type1 vfio irqbypass efivarfs
[  200.133264] CPU: 9 PID: 3649 Comm: bash Tainted: G        W          6.4.2-1-default #1 openSUSE Tumbleweed 44279f67043987f2a4149a1dd94f4478c9404e2a
[  200.133266] Hardware name: Gigabyte Technology Co., Ltd. X570 AORUS MASTER/X570 AORUS MASTER, BIOS F37b 02/08/2023
[  200.133266] RIP: 0010:amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.133437] Code: c0 74 33 48 8b 4e 10 48 83 39 00 74 29 89 d1 48 8d 04 88 8b 08 85 c9 74 11 f0 ff 08 74 07 31 c0 c3 cc cc cc cc e9 6a fd ff ff <0f> 0b b8 ea ff ff ff c3 cc cc cc cc b8 ea ff ff ff c3 cc cc cc cc
[  200.133438] RSP: 0018:ffffa22446e9fc68 EFLAGS: 00010246
[  200.133439] RAX: ffff925b40343770 RBX: ffff925b01900000 RCX: 0000000000000000
[  200.133439] RDX: 0000000000000000 RSI: ffff925b01919268 RDI: ffff925b01900000
[  200.133440] RBP: ffff925b01925de2 R08: 0000000000000000 R09: ffffffff9746fa40
[  200.133440] R10: 0000000000000000 R11: 0000000000000000 R12: ffff925b01900010
[  200.133441] R13: ffff925b01925d72 R14: ffff92698f07a150 R15: ffff925b478ae620
[  200.133442] FS:  00007f1226087540(0000) GS:ffff92698e680000(0000) knlGS:0000000000000000
[  200.133442] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  200.133443] CR2: 00007f06dc50f380 CR3: 00000001f66e6000 CR4: 0000000000750ee0
[  200.133444] PKRU: 55555554
[  200.133444] Call Trace:
[  200.133445]  <TASK>
[  200.133445]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.133616]  ? __warn+0x81/0x130
[  200.133617]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.133787]  ? report_bug+0x171/0x1a0
[  200.133789]  ? handle_bug+0x3c/0x80
[  200.133790]  ? exc_invalid_op+0x17/0x70
[  200.133792]  ? asm_exc_invalid_op+0x1a/0x20
[  200.133793]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.133963]  gfx_v10_0_hw_fini+0x2f/0x160 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.134139]  amdgpu_device_fini_hw+0x1ed/0x330 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.134290]  ? blocking_notifier_chain_unregister+0x36/0x50
[  200.134291]  amdgpu_pci_remove+0x51/0x140 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.134441]  ? __pm_runtime_resume+0x58/0x80
[  200.134443]  pci_device_remove+0x3a/0xa0
[  200.134444]  device_release_driver_internal+0x19f/0x200
[  200.134447]  unbind_store+0xa1/0xb0
[  200.134448]  kernfs_fop_write_iter+0x136/0x1d0
[  200.134450]  vfs_write+0x1ef/0x3b0
[  200.134452]  ksys_write+0x67/0xe0
[  200.134453]  do_syscall_64+0x60/0x90
[  200.134455]  ? do_syscall_64+0x6c/0x90
[  200.134456]  ? do_dup2+0x88/0xc0
[  200.134457]  ? syscall_exit_to_user_mode+0x1b/0x40
[  200.134459]  ? do_syscall_64+0x6c/0x90
[  200.134460]  ? do_syscall_64+0x6c/0x90
[  200.134461]  ? do_syscall_64+0x6c/0x90
[  200.134462]  ? do_syscall_64+0x6c/0x90
[  200.134464]  entry_SYSCALL_64_after_hwframe+0x72/0xdc
[  200.134465] RIP: 0033:0x7f12261c5184
[  200.134469] Code: ff eb b7 0f 1f 00 90 90 90 90 90 90 90 90 90 90 90 90 90 90 f3 0f 1e fa 90 90 80 3d fd 29 0f 00 00 74 13 b8 01 00 00 00 0f 05 <48> 3d 00 f0 ff ff 77 54 c3 0f 1f 00 48 83 ec 28 48 89 54 24 18 48
[  200.134470] RSP: 002b:00007ffdf0ff4c78 EFLAGS: 00000202 ORIG_RAX: 0000000000000001
[  200.134471] RAX: ffffffffffffffda RBX: 000000000000000d RCX: 00007f12261c5184
[  200.134471] RDX: 000000000000000d RSI: 000055942c5e4100 RDI: 0000000000000001
[  200.134472] RBP: 000055942c5e4100 R08: 0000000000000073 R09: 0000000000000001
[  200.134472] R10: 0000000000000000 R11: 0000000000000202 R12: 000000000000000d
[  200.134473] R13: 00007f12262aa780 R14: 000000000000000d R15: 00007f12262a5d60
[  200.134474]  </TASK>
[  200.134474] ---[ end trace 0000000000000000 ]---
[  200.134803] ------------[ cut here ]------------
[  200.134804] WARNING: CPU: 9 PID: 3649 at drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c:599 amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.134977] Modules linked in: snd_seq_dummy snd_hrtimer snd_seq rfcomm zram wireguard libchacha20poly1305 chacha_x86_64 poly1305_x86_64 curve25519_x86_64 libcurve25519_generic libchacha ip6_udp_tunnel udp_tunnel af_packet nft_fib_inet nft_fib_ipv4 nft_fib_ipv6 nft_fib nft_reject_inet nf_reject_ipv4 nf_reject_ipv6 nft_reject nft_ct nft_chain_nat nf_tables ebtable_nat ebtable_broute ip6table_nat ip6table_mangle ip6table_raw ip6table_security iptable_nat nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 iptable_mangle iptable_raw iptable_security ip_set nfnetlink ebtable_filter ebtables ip6table_filter ip6_tables iptable_filter bpfilter qrtr cmac algif_hash algif_skcipher af_alg bnep nls_iso8859_1 nls_cp437 vfat fat iwlmvm mac80211 snd_hda_codec_realtek snd_hda_codec_generic libarc4 ledtrig_audio snd_hda_codec_hdmi uvcvideo videobuf2_vmalloc uvc videobuf2_memops btusb snd_hda_intel videobuf2_v4l2 btrtl snd_intel_dspcfg snd_intel_sdw_acpi snd_usb_audio btbcm videodev snd_hda_codec btintel snd_usbmidi_lib btmtk iwlwifi
[  200.134996]  intel_rapl_msr snd_rawmidi it87 snd_hda_core videobuf2_common intel_rapl_common snd_seq_device snd_hwdep bluetooth mc hwmon_vid edac_mce_amdgigabyte_wmi snd_pcm wmi_bmof mxm_wmi pcspkr cfg80211 snd_timer acpi_cpufreq k10temp efi_pstore i2c_piix4 ecdh_generic snd igb soundcore joydev dca rfkill tiny_power_button thermal button fuse configfs dmi_sysfs ip_tables x_tables hid_generic usbhid amdgpu crct10dif_pclmul crc32_pclmul polyval_clmulni polyval_generic gf128mul ghash_clmulni_intel sha512_ssse3 i2c_algo_bit drm_ttm_helper ttm video drm_suballoc_helper iommu_v2 xhci_pci xhci_pci_renesas drm_buddy gpu_sched xhci_hcd aesni_intel drm_display_helper crypto_simd cryptd cec nvme sp5100_tco usbcore rc_core nvme_core wmi btrfs blake2b_generic libcrc32c crc32c_intel xor sg dm_multipath dm_mod raid6_pq scsi_dh_rdac scsi_dh_emc scsi_dh_alua msr kvm_amd ccp kvm vfio_pci vfio_pci_core vfio_iommu_type1 vfio irqbypass efivarfs
[  200.135016] CPU: 9 PID: 3649 Comm: bash Tainted: G        W          6.4.2-1-default #1 openSUSE Tumbleweed 44279f67043987f2a4149a1dd94f4478c9404e2a
[  200.135017] Hardware name: Gigabyte Technology Co., Ltd. X570 AORUS MASTER/X570 AORUS MASTER, BIOS F37b 02/08/2023
[  200.135018] RIP: 0010:amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.135188] Code: c0 74 33 48 8b 4e 10 48 83 39 00 74 29 89 d1 48 8d 04 88 8b 08 85 c9 74 11 f0 ff 08 74 07 31 c0 c3 cc cc cc cc e9 6a fd ff ff <0f> 0b b8 ea ff ff ff c3 cc cc cc cc b8 ea ff ff ff c3 cc cc cc cc
[  200.135189] RSP: 0018:ffffa22446e9fc60 EFLAGS: 00010246
[  200.135189] RAX: ffff925b40343a20 RBX: ffff925a88154800 RCX: 0000000000000000
[  200.135190] RDX: 0000000000000000 RSI: ffff925a88154808 RDI: ffff925b01900000
[  200.135190] RBP: ffff925b01925dc2 R08: 0000000000000000 R09: 00000000010000fa
[  200.135191] R10: 0000000000000001 R11: dead000000000122 R12: ffff925b01900000
[  200.135192] R13: ffff925b01925d72 R14: ffff92698f07a150 R15: ffff925b478ae620
[  200.135192] FS:  00007f1226087540(0000) GS:ffff92698e680000(0000) knlGS:0000000000000000
[  200.135193] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  200.135193] CR2: 00007f06dc50f380 CR3: 00000001f66e6000 CR4: 0000000000750ee0
[  200.135194] PKRU: 55555554
[  200.135194] Call Trace:
[  200.135195]  <TASK>
[  200.135195]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.135373]  ? __warn+0x81/0x130
[  200.135375]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.135545]  ? report_bug+0x171/0x1a0
[  200.135547]  ? handle_bug+0x3c/0x80
[  200.135549]  ? exc_invalid_op+0x17/0x70
[  200.135550]  ? asm_exc_invalid_op+0x1a/0x20
[  200.135552]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.135722]  smu_smc_hw_cleanup+0x46/0x3b0 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.135924]  amdgpu_device_fini_hw+0x1ed/0x330 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.136079]  ? blocking_notifier_chain_unregister+0x36/0x50
[  200.136081]  amdgpu_pci_remove+0x51/0x140 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.136231]  ? __pm_runtime_resume+0x58/0x80
[  200.136233]  pci_device_remove+0x3a/0xa0
[  200.136234]  device_release_driver_internal+0x19f/0x200
[  200.136236]  unbind_store+0xa1/0xb0
[  200.136238]  kernfs_fop_write_iter+0x136/0x1d0
[  200.136240]  vfs_write+0x1ef/0x3b0
[  200.136242]  ksys_write+0x67/0xe0
[  200.136243]  do_syscall_64+0x60/0x90
[  200.136244]  ? do_syscall_64+0x6c/0x90
[  200.136246]  ? do_dup2+0x88/0xc0
[  200.136247]  ? syscall_exit_to_user_mode+0x1b/0x40
[  200.136249]  ? do_syscall_64+0x6c/0x90
[  200.136250]  ? do_syscall_64+0x6c/0x90
[  200.136251]  ? do_syscall_64+0x6c/0x90
[  200.136252]  ? do_syscall_64+0x6c/0x90
[  200.136254]  entry_SYSCALL_64_after_hwframe+0x72/0xdc
[  200.136255] RIP: 0033:0x7f12261c5184
[  200.136259] Code: ff eb b7 0f 1f 00 90 90 90 90 90 90 90 90 90 90 90 90 90 90 f3 0f 1e fa 90 90 80 3d fd 29 0f 00 00 74 13 b8 01 00 00 00 0f 05 <48> 3d 00 f0 ff ff 77 54 c3 0f 1f 00 48 83 ec 28 48 89 54 24 18 48
[  200.136260] RSP: 002b:00007ffdf0ff4c78 EFLAGS: 00000202 ORIG_RAX: 0000000000000001
[  200.136261] RAX: ffffffffffffffda RBX: 000000000000000d RCX: 00007f12261c5184
[  200.136262] RDX: 000000000000000d RSI: 000055942c5e4100 RDI: 0000000000000001
[  200.136262] RBP: 000055942c5e4100 R08: 0000000000000073 R09: 0000000000000001
[  200.136263] R10: 0000000000000000 R11: 0000000000000202 R12: 000000000000000d
[  200.136263] R13: 00007f12262aa780 R14: 000000000000000d R15: 00007f12262a5d60
[  200.136264]  </TASK>
[  200.136265] ---[ end trace 0000000000000000 ]---
[  200.136266] amdgpu 0000:08:00.0: amdgpu: Fail to disable thermal alert!
[  200.139617] amdgpu 0000:08:00.0: amdgpu: failed to clear page tables on GEM object close (-19)
[  200.139623] amdgpu 0000:08:00.0: amdgpu: failed to clear page tables on GEM object close (-19)
[  200.139626] amdgpu 0000:08:00.0: amdgpu: failed to clear page tables on GEM object close (-19)
[  200.190261] ------------[ cut here ]------------
[  200.190265] WARNING: CPU: 8 PID: 3649 at drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c:599 amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.190564] Modules linked in: snd_seq_dummy snd_hrtimer snd_seq rfcomm zram wireguard libchacha20poly1305 chacha_x86_64 poly1305_x86_64 curve25519_x86_64 libcurve25519_generic libchacha ip6_udp_tunnel udp_tunnel af_packet nft_fib_inet nft_fib_ipv4 nft_fib_ipv6 nft_fib nft_reject_inet nf_reject_ipv4 nf_reject_ipv6 nft_reject nft_ct nft_chain_nat nf_tables ebtable_nat ebtable_broute ip6table_nat ip6table_mangle ip6table_raw ip6table_security iptable_nat nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 iptable_mangle iptable_raw iptable_security ip_set nfnetlink ebtable_filter ebtables ip6table_filter ip6_tables iptable_filter bpfilter qrtr cmac algif_hash algif_skcipher af_alg bnep nls_iso8859_1 nls_cp437 vfat fat iwlmvm mac80211 snd_hda_codec_realtek snd_hda_codec_generic libarc4 ledtrig_audio snd_hda_codec_hdmi uvcvideo videobuf2_vmalloc uvc videobuf2_memops btusb snd_hda_intel videobuf2_v4l2 btrtl snd_intel_dspcfg snd_intel_sdw_acpi snd_usb_audio btbcm videodev snd_hda_codec btintel snd_usbmidi_lib btmtk iwlwifi
[  200.190601]  intel_rapl_msr snd_rawmidi it87 snd_hda_core videobuf2_common intel_rapl_common snd_seq_device snd_hwdep bluetooth mc hwmon_vid edac_mce_amdgigabyte_wmi snd_pcm wmi_bmof mxm_wmi pcspkr cfg80211 snd_timer acpi_cpufreq k10temp efi_pstore i2c_piix4 ecdh_generic snd igb soundcore joydev dca rfkill tiny_power_button thermal button fuse configfs dmi_sysfs ip_tables x_tables hid_generic usbhid amdgpu crct10dif_pclmul crc32_pclmul polyval_clmulni polyval_generic gf128mul ghash_clmulni_intel sha512_ssse3 i2c_algo_bit drm_ttm_helper ttm video drm_suballoc_helper iommu_v2 xhci_pci xhci_pci_renesas drm_buddy gpu_sched xhci_hcd aesni_intel drm_display_helper crypto_simd cryptd cec nvme sp5100_tco usbcore rc_core nvme_core wmi btrfs blake2b_generic libcrc32c crc32c_intel xor sg dm_multipath dm_mod raid6_pq scsi_dh_rdac scsi_dh_emc scsi_dh_alua msr kvm_amd ccp kvm vfio_pci vfio_pci_core vfio_iommu_type1 vfio irqbypass efivarfs
[  200.190643] CPU: 8 PID: 3649 Comm: bash Tainted: G        W          6.4.2-1-default #1 openSUSE Tumbleweed 44279f67043987f2a4149a1dd94f4478c9404e2a
[  200.190646] Hardware name: Gigabyte Technology Co., Ltd. X570 AORUS MASTER/X570 AORUS MASTER, BIOS F37b 02/08/2023
[  200.190647] RIP: 0010:amdgpu_irq_put+0x46/0x70 [amdgpu]
[  200.190929] Code: c0 74 33 48 8b 4e 10 48 83 39 00 74 29 89 d1 48 8d 04 88 8b 08 85 c9 74 11 f0 ff 08 74 07 31 c0 c3 cc cc cc cc e9 6a fd ff ff <0f> 0b b8 ea ff ff ff c3 cc cc cc cc b8 ea ff ff ff c3 cc cc cc cc
[  200.190930] RSP: 0018:ffffa22446e9fc78 EFLAGS: 00010246
[  200.190932] RAX: ffff925a80ff1228 RBX: ffff925b01900000 RCX: 0000000000000000
[  200.190933] RDX: 0000000000000000 RSI: ffff925b01900c48 RDI: ffff925b01900000
[  200.190934] RBP: ffff925b01925d92 R08: 0000000000000000 R09: 0000000080200012
[  200.190935] R10: 0000000000001000 R11: 0000000000000050 R12: ffff925b01900010
[  200.190936] R13: ffff925b01925d72 R14: ffff92698f07a150 R15: ffff925b478ae620
[  200.190936] FS:  00007f1226087540(0000) GS:ffff92698e600000(0000) knlGS:0000000000000000
[  200.190938] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  200.190939] CR2: 00007fe06400e7c8 CR3: 00000001f66e6000 CR4: 0000000000750ee0
[  200.190939] PKRU: 55555554
[  200.190940] Call Trace:
[  200.190942]  <TASK>
[  200.190943]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.191224]  ? __warn+0x81/0x130
[  200.191227]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.191506]  ? report_bug+0x171/0x1a0
[  200.191509]  ? handle_bug+0x3c/0x80
[  200.191512]  ? exc_invalid_op+0x17/0x70
[  200.191514]  ? asm_exc_invalid_op+0x1a/0x20
[  200.191517]  ? amdgpu_irq_put+0x46/0x70 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.191802]  gmc_v10_0_hw_fini+0x53/0x80 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.192093]  amdgpu_device_fini_hw+0x1ed/0x330 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.192367]  ? blocking_notifier_chain_unregister+0x36/0x50
[  200.192371]  amdgpu_pci_remove+0x51/0x140 [amdgpu ae24122be274b7099dc75100f702af080593b595]
[  200.192643]  ? __pm_runtime_resume+0x58/0x80
[  200.192646]  pci_device_remove+0x3a/0xa0
[  200.192649]  device_release_driver_internal+0x19f/0x200
[  200.192652]  unbind_store+0xa1/0xb0
[  200.192654]  kernfs_fop_write_iter+0x136/0x1d0
[  200.192657]  vfs_write+0x1ef/0x3b0
[  200.192660]  ksys_write+0x67/0xe0
[  200.192662]  do_syscall_64+0x60/0x90
[  200.192664]  ? do_syscall_64+0x6c/0x90
[  200.192665]  ? do_dup2+0x88/0xc0
[  200.192668]  ? syscall_exit_to_user_mode+0x1b/0x40
[  200.192670]  ? do_syscall_64+0x6c/0x90
[  200.192671]  ? do_syscall_64+0x6c/0x90
[  200.192673]  ? do_syscall_64+0x6c/0x90
[  200.192674]  ? do_syscall_64+0x6c/0x90
[  200.192675]  entry_SYSCALL_64_after_hwframe+0x72/0xdc
[  200.192677] RIP: 0033:0x7f12261c5184
[  200.192700] Code: ff eb b7 0f 1f 00 90 90 90 90 90 90 90 90 90 90 90 90 90 90 f3 0f 1e fa 90 90 80 3d fd 29 0f 00 00 74 13 b8 01 00 00 00 0f 05 <48> 3d 00 f0 ff ff 77 54 c3 0f 1f 00 48 83 ec 28 48 89 54 24 18 48
[  200.192701] RSP: 002b:00007ffdf0ff4c78 EFLAGS: 00000202 ORIG_RAX: 0000000000000001
[  200.192703] RAX: ffffffffffffffda RBX: 000000000000000d RCX: 00007f12261c5184
[  200.192704] RDX: 000000000000000d RSI: 000055942c5e4100 RDI: 0000000000000001
[  200.192705] RBP: 000055942c5e4100 R08: 0000000000000073 R09: 0000000000000001
[  200.192706] R10: 0000000000000000 R11: 0000000000000202 R12: 000000000000000d
[  200.192707] R13: 00007f12262aa780 R14: 000000000000000d R15: 00007f12262a5d60
[  200.192708]  </TASK>
[  200.192709] ---[ end trace 0000000000000000 ]---
[  204.372169] vfio-pci 0000:08:00.0: vgaarb: changed VGA decodes: olddecodes=none,decodes=io+mem:owns=none
[  241.791762] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[  242.661617] tun: Universal TUN/TAP device driver, 1.6
[  242.661894] br0: port 1(vnet0) entered blocking state
[  242.661896] br0: port 1(vnet0) entered disabled state
[  242.661904] vnet0: entered allmulticast mode
[  242.661931] vnet0: entered promiscuous mode
[  242.662008] br0: port 1(vnet0) entered blocking state
[  242.662009] br0: port 1(vnet0) entered forwarding state
[  244.512197] vfio-pci 0000:08:00.0: vfio_ecap_init: hiding ecap 0x19@0x270
[  244.512207] vfio-pci 0000:08:00.0: vfio_ecap_init: hiding ecap 0x1b@0x2d0
[  244.512214] vfio-pci 0000:08:00.0: vfio_ecap_init: hiding ecap 0x26@0x410
[  244.512215] vfio-pci 0000:08:00.0: vfio_ecap_init: hiding ecap 0x27@0x440
```

---

### 评论 #8 — ChristianKoenigAMD (2024-07-25T14:25:50Z)

Well what you try to do here is intentionally not working.

When the VM is terminated the driver inside the VM doesn't unloads and so doesn't tell the PSP that it's ok to re-load some other driver. The PSP (Platform Security Processor) will then intentionally block loading amdgpu on the host side again.

IIRC we added a workaround in the latest driver which basically executes a hard reset of the GPU when it finds that the PSP is blocking us. But that was something added rather recently.

---

### 评论 #9 — schung-amd (2024-07-25T14:41:44Z)

Hi @Avatat and @dedani, I was able to reproduce this behaviour, but as @ChristianKoenigAMD states this workflow is currently unsupported so I'll be closing this issue. For now, you may be able to recover ROCm functionality after unbinding and rebinding amdgpu by unloading and reloading the driver:
```
sudo rmmod amdgpu
sudo modprobe amdgpu
```
which requires amdgpu to not be in use; I had to temporarily kill the display manager with `sudo systemctl stop display-manager` before and `sudo systemctl start display-manager` afterward on Ubuntu 22.04. Alternatively, you can simply reboot your system as noted by @Avatat.   

---
