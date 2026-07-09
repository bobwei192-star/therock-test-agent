# [Driver] BUG: unable to handle page fault for address: ffffa7c13eaffff8

- **Issue #:** 2198
- **State:** closed
- **Created:** 2023-05-31T06:13:30Z
- **Updated:** 2023-06-29T14:13:12Z
- **Labels:** Verified Issue, 5.5.0, 5.6.0
- **URL:** https://github.com/ROCm/ROCm/issues/2198

This one is the worst, only seems to occur when I put two GPUs in the system.

Sometime just happens, but easy to reproduce running https://github.com/RadeonOpenCompute/rocm_bandwidth_test

2x 7900XTX
ASROCK ROMED8-2T
EPYC 7662
Ubuntu 22.04, Kernel 6.2.14-060214-generic, ROCm 5.5

```
[   91.370818] BUG: unable to handle page fault for address: ffffa7c13eaffff8                              
[   91.370827] #PF: supervisor write access in kernel mode
[   91.370831] #PF: error_code(0x0002) - not-present page                                                  
[   91.370833] PGD 100000067 P4D 100000067 PUD 0                                                           
[   91.370838] Oops: 0002 [#1] PREEMPT SMP NOPTI
[   91.370842] CPU: 107 PID: 2937 Comm: rocm-bandwidth- Tainted: G        W  OE      6.2.14-060214-generic #202305010032                                                                                              
[   91.370847] Hardware name: To Be Filled By O.E.M. ROMED8-2T/ROMED8-2T, BIOS P3.50 07/19/2022            
[   91.370850] RIP: 0010:amdgpu_gmc_set_pte_pde+0x23/0x40 [amdgpu]                                         
[   91.371127] Code: 90 90 90 90 90 90 90 0f 1f 44 00 00 48 b8 00 f0 ff ff ff ff 00 00 55 48 21 c1 8d 04 d5 00 00 00 00 4c 09 c1 48 01 c6 48 89 e5 <48> 89 0e 31 c0 5d 31 d2 31 c9 31 f6 45 31 c0 e9 b9 38 ab c2 66 0f
[   91.371132] RSP: 0018:ffffa7b3ca3677c0 EFLAGS: 00010282                                                 
[   91.371136] RAX: 00000000fffffff8 RBX: 0000000000000000 RCX: 000300013c66f077                           
[   91.371139] RDX: 00000000ffffffff RSI: ffffa7c13eaffff8 RDI: ffff937f64980000                           
[   91.371142] RBP: ffffa7b3ca3677c0 R08: 0003000000000077 R09: ffffa7c03eb00000                                                                                                                                      
[   91.371145] R10: 0000000000000000 R11: 0000000000000000 R12: 0000000000000000                           
[   91.371149] R13: ffff937f64980000 R14: ffff937f28d64ff0 R15: ffffa7c03eb00000                           
[   91.371152] FS:  00007f9121cd7780(0000) GS:ffff93bd4e8c0000(0000) knlGS:0000000000000000                
[   91.371156] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033                                           
[   91.371159] CR2: ffffa7c13eaffff8 CR3: 000000013ca36000 CR4: 0000000000350ee0                                                                                                                                      
[   91.371162] Call Trace:                                                                                 
[   91.371166]  <TASK>                                                                                                                                                                                                
[   91.371169]  amdgpu_gart_map+0x7c/0xc0 [amdgpu]                                                                                                                                                                    
[   91.371412]  amdgpu_gart_bind+0x1a/0x50 [amdgpu]                                                                                                                                                                   
[   91.371652]  amdgpu_ttm_gart_bind+0xa0/0xc0 [amdgpu]                                                                                                                                                               
[   91.371890]  amdgpu_ttm_recover_gart+0x5f/0x80 [amdgpu]                                                                                                                                                            
[   91.372128]  amdgpu_gtt_mgr_recover+0x46/0x80 [amdgpu]                                                                                                                                                             
[   91.372375]  gmc_v11_0_hw_init+0x29/0x100 [amdgpu]                                                                                                                                                                 
[   91.372637]  gmc_v11_0_resume+0x14/0x30 [amdgpu]                                                                                                                                                                   
[   91.372894]  amdgpu_device_ip_resume_phase1+0xe0/0x220 [amdgpu]                                                                                                                                                    
[   91.373129]  ? kgd2kfd_resume_iommu+0x4a/0x90 [amdgpu]                                                                                                                                                             
[   91.373410]  ? __pfx_pci_pm_runtime_resume+0x10/0x10                                                                                                                                                               
[   91.373417]  amdgpu_device_resume+0xb3/0x3b0 [amdgpu]                                                                                                                                                              
[   91.373654]  ? __pfx_pci_pm_runtime_resume+0x10/0x10                                                                                                                                                               
[   91.373658]  amdgpu_pmops_runtime_resume+0x84/0x100 [amdgpu]                 
[   91.373897]  pci_pm_runtime_resume+0xa3/0xf0                                                                                                                                                                       
[   91.373901]  __rpm_callback+0x50/0x170                                                                  
[   91.373906]  rpm_callback+0x6d/0x80                                                                     
[   91.373910]  ? __pfx_pci_pm_runtime_resume+0x10/0x10                         
[   91.373914]  rpm_resume+0x605/0x860                                                                     
[   91.373918]  __pm_runtime_resume+0x4e/0x80                                                              
[   91.373922]  amdgpu_driver_open_kms+0x54/0x250 [amdgpu]                      
[   91.374159]  drm_file_alloc+0x1a1/0x260 [drm]                                                           
[   91.374201]  drm_open_helper+0x6c/0x140 [drm]                                                           
[   91.374233]  ? drm_minor_acquire+0xb1/0x180 [drm]                                                       
[   91.374267]  drm_open+0x7f/0x170 [drm]
[   91.374299]  drm_stub_open+0xa9/0xe0 [drm]
[   91.374330]  chrdev_open+0xc5/0x240
[   91.374336]  ? fsnotify_perm.part.0+0x79/0x190
[   91.374341]  ? __pfx_chrdev_open+0x10/0x10
[   91.374344]  do_dentry_open+0x1f8/0x430
[   91.374348]  vfs_open+0x2d/0x40
[   91.374351]  do_open+0x200/0x4d0
[   91.374357]  ? open_last_lookups+0x8e/0x420
[   91.374361]  path_openat+0x135/0x2e0
[   91.374365]  ? mutex_lock+0x12/0x50
[   91.374370]  do_filp_open+0xaf/0x170
[   91.374377]  do_sys_openat2+0xbf/0x180
[   91.374380]  __x64_sys_openat+0x6c/0xa0
[   91.374384]  do_syscall_64+0x5b/0x90
[   91.374389]  ? exit_to_user_mode_prepare+0x30/0xb0
[   91.374396]  ? syscall_exit_to_user_mode+0x29/0x50
[   91.374400]  ? do_syscall_64+0x67/0x90
[   91.374403]  entry_SYSCALL_64_after_hwframe+0x72/0xdc
[   91.374409] RIP: 0033:0x7f91213146eb
[   91.374412] Code: 25 00 00 41 00 3d 00 00 41 00 74 4b 64 8b 04 25 18 00 00 00 85 c0 75 67 44 89 e2 48 89 ee bf 9c ff ff ff b8 01 01 00 00 0f 05 <48> 3d 00 f0 ff ff 0f 87 91 00 00 00 48 8b 54 24 28 64 48 2b 14 25
[   91.374418] RSP: 002b:00007fff42271880 EFLAGS: 00000246 ORIG_RAX: 0000000000000101
[   91.374422] RAX: ffffffffffffffda RBX: 0000000000000002 RCX: 00007f91213146eb
[   91.374425] RDX: 0000000000080002 RSI: 00007fff42271900 RDI: 00000000ffffff9c
[   91.374428] RBP: 00007fff42271900 R08: 0000000000000000 R09: 00007fff42271695
[   91.374430] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000080002
[   91.374433] R13: 00007fff42271900 R14: 646e65725f6d7264 R15: 00007fff422719f0
[   91.374438]  </TASK>
[   91.374439] Modules linked in: joydev input_leds hid_generic usbhid hid xt_conntrack nft_chain_nat xt_MASQUERADE nf_nat nf_conntrack_netlink nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 xfrm_user xfrm_algo xt_addr
type nft_compat nf_tables nfnetlink br_netfilter bridge stp llc overlay ipmi_ssif intel_rapl_msr intel_rapl_common amd64_edac edac_mce_amd kvm_amd mei_hdcp(OE) mei_pxp(OE) mei_iaf(OE) kvm irqbypass rapl binfmt_misc
 nls_iso8859_1 snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_intel_sdw_acpi snd_hda_codec snd_hda_core snd_hwdep mei_gsc(OE) snd_pcm mei_me(OE) snd_timer snd mei(OE) soundcore ccp acpi_ipmi ptdma k10temp ip
mi_si ipmi_devintf ipmi_msghandler mac_hid sch_fq_codel dm_multipath scsi_dh_rdac scsi_dh_emc scsi_dh_alua msr ramoops pstore_blk reed_solomon pstore_zone efi_pstore ip_tables x_tables autofs4 btrfs blake2b_generic
 raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear cdc_ether usbnet mii
[   91.374506]  amdgpu i915 iommu_v2 gpu_sched drm_buddy video wmi i2c_algo_bit drm_ttm_helper ttm drm_display_helper cec rc_core drm_kms_helper syscopyarea sysfillrect sysimgblt nvme crct10dif_pclmul crc32_pclmul 
polyval_clmulni polyval_generic ghash_clmulni_intel sha512_ssse3 aesni_intel crypto_simd cryptd ahci nvme_core drm bnxt_en libahci xhci_pci nvme_common xhci_pci_renesas i2c_piix4
[   91.374557] CR2: ffffa7c13eaffff8
[   91.374560] ---[ end trace 0000000000000000 ]---
[   91.474884] RIP: 0010:amdgpu_gmc_set_pte_pde+0x23/0x40 [amdgpu]
[   91.475142] Code: 90 90 90 90 90 90 90 0f 1f 44 00 00 48 b8 00 f0 ff ff ff ff 00 00 55 48 21 c1 8d 04 d5 00 00 00 00 4c 09 c1 48 01 c6 48 89 e5 <48> 89 0e 31 c0 5d 31 d2 31 c9 31 f6 45 31 c0 e9 b9 38 ab c2 66 0f
[   91.475147] RSP: 0018:ffffa7b3ca3677c0 EFLAGS: 00010282
[   91.475151] RAX: 00000000fffffff8 RBX: 0000000000000000 RCX: 000300013c66f077
[   91.475154] RDX: 00000000ffffffff RSI: ffffa7c13eaffff8 RDI: ffff937f64980000
[   91.475157] RBP: ffffa7b3ca3677c0 R08: 0003000000000077 R09: ffffa7c03eb00000
[   91.475160] R10: 0000000000000000 R11: 0000000000000000 R12: 0000000000000000
[   91.475163] R13: ffff937f64980000 R14: ffff937f28d64ff0 R15: ffffa7c03eb00000
[   91.475166] FS:  00007f9121cd7780(0000) GS:ffff93bd4e8c0000(0000) knlGS:0000000000000000
[   91.475169] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   91.475172] CR2: ffffa7c13eaffff8 CR3: 000000013ca36000 CR4: 0000000000350ee0
```