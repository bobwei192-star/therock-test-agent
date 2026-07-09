# [CRTC:42:crtc-0] vblank wait timed out

- **Issue #:** 379
- **State:** closed
- **Created:** 2018-04-03T18:05:34Z
- **Updated:** 2018-05-12T13:09:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/379

Dear all, since I installed rocm, I experience random system hangs and crashes.
CPU: G4560, GPU RX560 Kernel: 4.13.0-32-generic #35-Ubuntu SMP
Some suspicious lines from the syslog are below. Is this related to rocm? Will this go away in future kernel versions?

Apr  3 19:49:35 tinsim-nas kernel: [  449.603714] [CRTC:42:crtc-0] vblank wait timed out
Apr  3 19:49:35 tinsim-nas kernel: [  449.603784] ------------[ cut here ]------------
Apr  3 19:49:35 tinsim-nas kernel: [  449.603806] WARNING: CPU: 3 PID: 166 at /build/linux-UKCsxy/linux-4.13.0/drivers/gpu/drm/drm_atomic_helper.c:1236 drm_atomic_helper_wait_for_vblanks.part.19+0x263/0x270 [drm_kms_helper]
Apr  3 19:49:35 tinsim-nas kernel: [  449.603807] Modules linked in: pci_stub vboxpci(OE) vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) bnep xt_CHECKSUM iptable_mangle ipt_MASQUERADE nf_nat_masquerade_ipv4 iptable_nat nf_nat_ipv4 nf_nat nf_conntrack_ipv4 nf_defrag_ipv4 xt_conntrack nf_conntrack libcrc32c ipt_REJECT nf_reject_ipv4 xt_tcpudp bridge stp llc ebtable_filter ebtables ip6table_filter ip6_tables iptable_filter binfmt_misc joydev input_leds intel_rapl x86_pkg_temp_thermal intel_powerclamp crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc snd_seq_midi snd_seq_midi_event snd_rawmidi snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi aesni_intel aes_x86_64 crypto_simd glue_helper snd_hda_intel cryptd intel_cstate intel_rapl_perf snd_hda_codec snd_hda_core snd_seq snd_hwdep snd_pcm snd_seq_device snd_timer hci_uart btbcm
Apr  3 19:49:35 tinsim-nas kernel: [  449.603838]  serdev btqca mei_me snd btintel mei soundcore shpchp intel_pch_thermal bluetooth ecdh_generic acpi_als intel_lpss_acpi intel_lpss kfifo_buf industrialio mac_hid acpi_pad nct6683 coretemp nfsd auth_rpcgss nfs_acl lockd parport_pc grace ppdev sunrpc lp parport ip_tables x_tables autofs4 btrfs xor raid6_pq vfio_pci vfio_virqfd vfio_iommu_type1 vfio hid_logitech_hidpp hid_logitech_dj hid_generic usbhid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdttm(OE) mxm_wmi kvm_intel kvm i915 irqbypass amdkcl(OE) i2c_algo_bit drm_kms_helper e1000e syscopyarea sysfillrect aic7xxx ptp sysimgblt pps_core fb_sys_fops scsi_transport_spi ahci drm libahci wmi video pinctrl_sunrisepoint pinctrl_intel i2c_hid hid
Apr  3 19:49:35 tinsim-nas kernel: [  449.603877] CPU: 3 PID: 166 Comm: kworker/u8:2 Tainted: G        W  OE   4.13.0-32-generic #35-Ubuntu
Apr  3 19:49:35 tinsim-nas kernel: [  449.603879] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./B150M Pro4S/D3, BIOS P7.00 12/06/2016
Apr  3 19:49:35 tinsim-nas kernel: [  449.603885] Workqueue: events_unbound commit_work [drm_kms_helper]
Apr  3 19:49:35 tinsim-nas kernel: [  449.603886] task: ffff930ca6b1c440 task.stack: ffffb45343870000
Apr  3 19:49:35 tinsim-nas kernel: [  449.603890] RIP: 0010:drm_atomic_helper_wait_for_vblanks.part.19+0x263/0x270 [drm_kms_helper]
Apr  3 19:49:35 tinsim-nas kernel: [  449.603891] RSP: 0018:ffffb45343873cc8 EFLAGS: 00010282
Apr  3 19:49:35 tinsim-nas kernel: [  449.603892] RAX: 0000000000000026 RBX: 0000000000000000 RCX: 0000000000000000
Apr  3 19:49:35 tinsim-nas kernel: [  449.603893] RDX: 0000000000000000 RSI: ffff930ccdd96578 RDI: ffff930ccdd96578
Apr  3 19:49:35 tinsim-nas kernel: [  449.603893] RBP: ffffb45343873d38 R08: 0000000000000001 R09: 00000000000004b0
Apr  3 19:49:35 tinsim-nas kernel: [  449.603894] R10: ffffb45343873cc8 R11: 0000000000000000 R12: ffff930b73b1b580
Apr  3 19:49:35 tinsim-nas kernel: [  449.603895] R13: 0000000000000000 R14: 0000000000000000 R15: ffff930cb15df000
Apr  3 19:49:35 tinsim-nas kernel: [  449.603896] FS:  0000000000000000(0000) GS:ffff930ccdd80000(0000) knlGS:0000000000000000
Apr  3 19:49:35 tinsim-nas kernel: [  449.603897] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Apr  3 19:49:35 tinsim-nas kernel: [  449.603897] CR2: 00007f760480b000 CR3: 000000019a20a005 CR4: 00000000003606e0
Apr  3 19:49:35 tinsim-nas kernel: [  449.603898] Call Trace:
Apr  3 19:49:35 tinsim-nas kernel: [  449.603907]  ? wait_woken+0x80/0x80
Apr  3 19:49:35 tinsim-nas kernel: [  449.603912]  drm_atomic_helper_wait_for_vblanks+0x14/0x20 [drm_kms_helper]
Apr  3 19:49:35 tinsim-nas kernel: [  449.604029]  amdgpu_dm_atomic_commit_tail+0x79a/0xa40 [amdgpu]
Apr  3 19:49:35 tinsim-nas kernel: [  449.604034]  ? pick_next_task_fair+0x131/0x560
Apr  3 19:49:35 tinsim-nas kernel: [  449.604038]  ? __switch_to+0xad/0x540
Apr  3 19:49:35 tinsim-nas kernel: [  449.604039]  ? put_prev_entity+0x23/0xf0
Apr  3 19:49:35 tinsim-nas kernel: [  449.604051]  commit_tail+0x3f/0x60 [drm_kms_helper]
Apr  3 19:49:35 tinsim-nas kernel: [  449.604053]  commit_work+0x12/0x20 [drm_kms_helper]
Apr  3 19:49:35 tinsim-nas kernel: [  449.604057]  process_one_work+0x1e7/0x410
Apr  3 19:49:35 tinsim-nas kernel: [  449.604059]  worker_thread+0x4b/0x420
Apr  3 19:49:35 tinsim-nas kernel: [  449.604061]  kthread+0x125/0x140
Apr  3 19:49:35 tinsim-nas kernel: [  449.604062]  ? process_one_work+0x410/0x410
Apr  3 19:49:35 tinsim-nas kernel: [  449.604063]  ? kthread_create_on_node+0x70/0x70
Apr  3 19:49:35 tinsim-nas kernel: [  449.604068]  ret_from_fork+0x1f/0x30
Apr  3 19:49:35 tinsim-nas kernel: [  449.604070] Code: 03 b8 88 01 00 00 48 83 c7 08 e8 f9 2c 16 f7 85 db 0f 85 c9 fe ff ff 49 8b 57 20 41 8b 77 60 48 c7 c7 e0 49 57 c0 e8 ce df 17 f7 <0f> ff e9 ae fe ff ff 66 0f 1f 44 00 00 0f 1f 44 00 00 f6 46 10 
Apr  3 19:49:35 tinsim-nas kernel: [  449.604092] ---[ end trace 1beb95d083f36a4f ]---