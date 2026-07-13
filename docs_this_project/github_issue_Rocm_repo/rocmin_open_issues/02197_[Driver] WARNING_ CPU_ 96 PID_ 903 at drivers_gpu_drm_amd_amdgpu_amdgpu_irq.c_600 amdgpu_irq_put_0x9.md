# [Driver] WARNING: CPU: 96 PID: 903 at drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c:600 amdgpu_irq_put+0x9f/0xb0 [amdgpu]

- **Issue #:** 2197
- **State:** open
- **Created:** 2023-05-31T04:08:28Z
- **Updated:** 2024-07-31T23:09:45Z
- **Labels:** 5.5.0
- **URL:** https://github.com/ROCm/ROCm/issues/2197

Got this launching a bunch of OpenCL kernels. I'll sometimes get it just booting the system

1x 7900XTX
ASROCK ROMED8-2T
EPYC 7662
Ubuntu 22.04, Kernel 6.2.14-060214-generic, ROCm 5.5

And it's spammed all over my dmesg, happens 10+ times.

```
[11654.666176] ------------[ cut here ]------------
[11654.666178] WARNING: CPU: 96 PID: 903 at drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c:600 amdgpu_irq_put+0x9f/0xb0 [amdgpu]
[11654.666437] Modules linked in: tls xt_conntrack nft_chain_nat xt_MASQUERADE nf_nat nf_conntrack_netlink nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 xfrm_user xfrm_algo xt_addrtype nft_compat nf_tables nfnetlink br_netfilter bridge stp llc overlay ipmi_ssif intel_rapl_msr intel_rapl_common amd64_edac edac_mce_amd kvm_amd mei_hdcp(OE) mei_pxp(OE) mei_iaf(OE) kvm irqbypass rapl binfmt_misc nls_iso8859_1 snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_intel_sdw_acpi snd_hda_codec snd_hda_core snd_hwdep snd_pcm mei_gsc(OE) joydev input_leds snd_timer mei_me(OE) snd ccp mei(OE) soundcore acpi_ipmi ptdma k10temp ipmi_si ipmi_devintf ipmi_msghandler mac_hid sch_fq_codel dm_multipath scsi_dh_rdac scsi_dh_emc scsi_dh_alua ramoops msr reed_solomon pstore_blk pstore_zone efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear hid_generic cdc_ether usbhid usbnet hid
[11654.666481]  mii amdgpu i915 iommu_v2 gpu_sched drm_buddy video wmi drm_ttm_helper i2c_algo_bit ttm drm_display_helper cec rc_core drm_kms_helper syscopyarea sysfillrect sysimgblt crct10dif_pclmul crc32_pclmul polyval_clmulni polyval_generic ghash_clmulni_intel sha512_ssse3 aesni_intel crypto_simd cryptd nvme drm ahci bnxt_en nvme_core libahci xhci_pci nvme_common xhci_pci_renesas i2c_piix4
[11654.666498] CPU: 96 PID: 903 Comm: kworker/96:1 Tainted: G        W  OE      6.2.14-060214-generic #202305010032
[11654.666500] Hardware name: To Be Filled By O.E.M. ROMED8-2T/ROMED8-2T, BIOS P3.50 07/19/2022
[11654.666501] Workqueue: pm pm_runtime_work
[11654.666503] RIP: 0010:amdgpu_irq_put+0x9f/0xb0 [amdgpu]
[11654.666759] Code: 31 f6 31 ff e9 52 9f 66 da 44 89 e2 48 89 de 4c 89 f7 e8 94 fc ff ff 5b 41 5c 41 5d 41 5e 5d 31 d2 31 f6 31 ff e9 31 9f 66 da <0f> 0b b8 ea ff ff ff eb c3 b8 fe ff ff ff eb bc 90 90 90 90 90 90
[11654.666761] RSP: 0018:ffffbb9f02ecfc40 EFLAGS: 00010246
[11654.666763] RAX: 0000000000000000 RBX: ffffa084f0f224d8 RCX: 0000000000000000
[11654.666764] RDX: 0000000000000000 RSI: 0000000000000000 RDI: 0000000000000000
[11654.666765] RBP: ffffbb9f02ecfc60 R08: 0000000000000000 R09: 0000000000000000
[11654.666766] R10: 0000000000000000 R11: 0000000000000000 R12: 0000000000000000
[11654.666767] R13: 0000000000000001 R14: ffffa084f0f20000 R15: ffffa084f0f20000
[11654.666768] FS:  0000000000000000(0000) GS:ffffa0c30e600000(0000) knlGS:0000000000000000
[11654.666770] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[11654.666771] CR2: 00007fe81d9628e8 CR3: 0000000d93010000 CR4: 0000000000350ee0
[11654.666773] Call Trace:
[11654.666773]  <TASK>
[11654.666775]  gmc_v11_0_hw_fini+0x24/0x80 [amdgpu]
[11654.667030]  gmc_v11_0_suspend+0xe/0x20 [amdgpu]
[11654.667284]  amdgpu_device_ip_suspend_phase2+0x25d/0x490 [amdgpu]
[11654.667518]  amdgpu_device_suspend+0x142/0x1b0 [amdgpu]
[11654.667752]  amdgpu_pmops_runtime_suspend+0xdf/0x200 [amdgpu]
[11654.667989]  ? __pfx_pci_pm_runtime_suspend+0x10/0x10
[11654.667991]  pci_pm_runtime_suspend+0x6a/0x1f0
[11654.667993]  ? __pfx_pci_pm_runtime_suspend+0x10/0x10
[11654.667995]  __rpm_callback+0x50/0x170
[11654.667998]  ? __pfx_pci_pm_runtime_suspend+0x10/0x10
[11654.668000]  rpm_callback+0x6d/0x80
[11654.668003]  ? __pfx_pci_pm_runtime_suspend+0x10/0x10
[11654.668004]  rpm_suspend+0x122/0x730
[11654.668007]  ? raw_spin_rq_unlock+0x10/0x40
[11654.668009]  ? finish_task_switch.isra.0+0x85/0x2a0
[11654.668012]  pm_runtime_work+0xc6/0xe0
[11654.668013]  process_one_work+0x225/0x430
[11654.668016]  worker_thread+0x50/0x3e0
[11654.668018]  ? __pfx_worker_thread+0x10/0x10
[11654.668020]  kthread+0xe9/0x110
[11654.668022]  ? __pfx_kthread+0x10/0x10
[11654.668025]  ret_from_fork+0x2c/0x50
[11654.668028]  </TASK>
[11654.668028] ---[ end trace 0000000000000000 ]---
```