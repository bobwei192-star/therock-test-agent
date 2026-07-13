# amdgpu/rocm stop working after VM stop and unbind from vfio-pci driver

- **Issue #:** 629
- **State:** closed
- **Created:** 2018-11-30T01:36:00Z
- **Updated:** 2024-07-25T14:41:44Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/629

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