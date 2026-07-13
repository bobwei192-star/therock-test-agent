# Debug - MSI x99 NIC e1000 driver issue 

- **Issue #:** 281
- **State:** closed
- **Created:** 2017-12-21T22:17:06Z
- **Updated:** 2020-11-18T11:34:59Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/281

Any GPU tool or application is started it gets immediately killed. Kernel message below.

```
[ 3063.518775] BUG: unable to handle kernel paging request at ffffaad345941000
[ 3063.520296] IP: memset_erms+0x9/0x10
[ 3063.521807] PGD 4aec9b067
[ 3063.521808] PUD 4aec9c067
[ 3063.523312] PMD 4a1889067
[ 3063.524817] PTE 0
[ 3063.526319]
[ 3063.529273] Oops: 0002 [#5] SMP
[ 3063.530683] Modules linked in: xt_multiport iptable_filter ip_tables x_tables nfsv3 nfs_acl nfs lockd grace fscache binfmt_misc nls_iso8859_1 intel_rapl edac_core x86_pkg_temp_thermal intel_powerclamp coretemp kvm_intel kvm snd_hda_codec_hdmi irqbypass crct10dif_pclmul snd_hda_intel crc32_pclmul snd_hda_codec ghash_clmulni_intel snd_hda_core pcbc snd_hwdep snd_pcm aesni_intel snd_timer snd 8021q soundcore garp aes_x86_64 mrp crypto_simd mei_me stp glue_helper llc input_leds cryptd mei lpc_ich shpchp mac_hid sunrpc lp parport autofs4 hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu mxm_wmi i2c_algo_bit ttm drm_kms_helper syscopyarea sysfillrect e1000e sysimgblt fb_sys_fops ahci drm ptp libahci pps_core wmi
[ 3063.539426] CPU: 12 PID: 2814 Comm: rocminfo Tainted: G      D         4.11.0-kfd-compute-rocm-rel-1.6-180 #1
[ 3063.540901] Hardware name: MSI MS-7885/X99S SLI PLUS (MS-7885), BIOS 1.D0 07/15/2016
[ 3063.542387] task: ffff9950e8ba2a00 task.stack: ffffaad345918000
[ 3063.543884] RIP: 0010:memset_erms+0x9/0x10
[ 3063.545365] RSP: 0018:ffffaad34591bd00 EFLAGS: 00010286
[ 3063.546849] RAX: ffff9950e85568ff RBX: 0000000000000008 RCX: 0000000000001000
[ 3063.548352] RDX: 0000000000009000 RSI: 00000000000000ff RDI: ffffaad345941000
[ 3063.549845] RBP: ffffaad34591bd48 R08: ffff9950ef51e440 R09: ffffaad345939000
[ 3063.551347] R10: ffff9950e8556800 R11: 0000000000000901 R12: ffff9950e2c2bd60
[ 3063.552839] R13: ffff9950e440dd80 R14: ffffaad34591bdf8 R15: ffff9950e2c2bc00
[ 3063.554316] FS:  00007fd2c03b3780(0000) GS:ffff9950ef500000(0000) knlGS:0000000000000000
[ 3063.555801] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 3063.557273] CR2: ffffaad345941000 CR3: 00000004a91b2000 CR4: 00000000001406e0
[ 3063.558766] Call Trace:
[ 3063.560262]  ? kfd_event_create+0x36c/0x550 [amdkfd]
[ 3063.561767]  kfd_ioctl_create_event+0x8a/0x160 [amdkfd]
[ 3063.563272]  kfd_ioctl+0x241/0x3f0 [amdkfd]
[ 3063.564764]  ? kfd_ioctl_destroy_event+0x20/0x20 [amdkfd]
[ 3063.566271]  ? common_mmap+0x48/0x50
[ 3063.567767]  ? apparmor_mmap_file+0x18/0x20
[ 3063.569274]  do_vfs_ioctl+0x92/0x5a0
[ 3063.570772]  SyS_ioctl+0x79/0x90
[ 3063.572264]  entry_SYSCALL_64_fastpath+0x1e/0xad
[ 3063.573747] RIP: 0033:0x7fd2bf8ccf07
[ 3063.575212] RSP: 002b:00007fffe1c93fe8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[ 3063.576714] RAX: ffffffffffffffda RBX: 0000000001a81530 RCX: 00007fd2bf8ccf07
[ 3063.578228] RDX: 00007fffe1c94040 RSI: 00000000c0204b08 RDI: 0000000000000003
[ 3063.579744] RBP: 0000000000000000 R08: 0000000000000000 R09: 70fb000100003000
[ 3063.581260] R10: 000000000000046c R11: 0000000000000246 R12: 0000000000000000
[ 3063.582732] R13: 0000000001a878c0 R14: 0000000000000002 R15: 00007fffe1c94040
[ 3063.584160] Code: 48 c1 e9 03 40 0f b6 f6 48 b8 01 01 01 01 01 01 01 01 48 0f af c6 f3 48 ab 89 d1 f3 aa 4c 89 c8 c3 90 49 89 f9 40 88 f0 48 89 d1 <f3> aa 4c 89 c8 c3 90 49 89 fa 40 0f b6 ce 48 b8 01 01 01 01 01
[ 3063.587152] RIP: memset_erms+0x9/0x10 RSP: ffffaad34591bd00
[ 3063.588645] CR2: ffffaad345941000
[ 3063.590114] ---[ end trace 87f56add3e2b9acb ]---

```