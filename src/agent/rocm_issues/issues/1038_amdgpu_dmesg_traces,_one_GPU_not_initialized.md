# amdgpu dmesg traces, one GPU not initialized

> **Issue #1038**
> **状态**: closed
> **创建时间**: 2020-03-08T10:17:24Z
> **更新时间**: 2020-03-09T05:45:27Z
> **关闭时间**: 2020-03-08T12:50:40Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1038

## 描述

Hi, using linux kernel 5.4.24, ROCm 2.10 OpenCL, RadeonVII, linux-firmware/eoan-updates,eoan-updates,now 1.183.4,

I see this in dmesg and one of the GPUs is not initialized. I would appreciate if somebody could give me some insights about the possible origin of the problem:

- is this a GPU hardware problem? (how could I confirm that?)
- could this be a motherboard or CPU hardware problem?
- could this be a result of the particular linux-firmware blobs that are in use? (1.183.4)
- something else?

```
[    4.929211] amdgpu 0000:67:00.0: remove_conflicting_pci_framebuffers: bar 0: 0xe0000000 -> 0xefffffff
[    4.929212] amdgpu 0000:67:00.0: remove_conflicting_pci_framebuffers: bar 2: 0xf0000000 -> 0xf01fffff
[    4.929212] amdgpu 0000:67:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xf0900000 -> 0xf097ffff
[    4.929213] checking generic (c0000000 fa0000) vs hw (e0000000 10000000)
[    4.929214] checking generic (c0000000 fa0000) vs hw (f0000000 200000)
[    4.929214] checking generic (c0000000 fa0000) vs hw (f0900000 80000)
[    4.929222] amdgpu 0000:67:00.0: enabling device (0100 -> 0103)
[    4.929333] [drm] initializing kernel modesetting (VEGA20 0x1002:0x66AF 0x1002:0x081E 0xC1).
[    4.929342] [drm] register mmio base: 0xF0900000
[    4.929342] [drm] register mmio size: 524288
[    4.929356] [drm] add ip block number 0 <soc15_common>
[    4.929357] [drm] add ip block number 1 <gmc_v9_0>
[    4.929357] [drm] add ip block number 2 <vega10_ih>
[    4.929357] [drm] add ip block number 3 <psp>
[    4.929358] [drm] add ip block number 4 <gfx_v9_0>
[    4.929358] [drm] add ip block number 5 <sdma_v4_0>
[    4.929358] [drm] add ip block number 6 <powerplay>
[    4.929359] [drm] add ip block number 7 <dm>
[    4.929359] [drm] add ip block number 8 <uvd_v7_0>
[    4.929359] [drm] add ip block number 9 <vce_v4_0>
[    5.031970] ATOM BIOS: 113-D3600200-106
[    5.031981] [drm] UVD(0) is enabled in VM mode
[    5.031981] [drm] UVD(1) is enabled in VM mode
[    5.031982] [drm] UVD(0) ENC is enabled in VM mode
[    5.031982] [drm] UVD(1) ENC is enabled in VM mode
[    5.031982] [drm] VCE enabled in VM mode
[    5.031987] [drm] GPU posting now...
[    5.032404] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[    5.032412] amdgpu 0000:67:00.0: BAR 2: releasing [mem 0xf0000000-0xf01fffff 64bit pref]
[    5.032413] amdgpu 0000:67:00.0: BAR 0: releasing [mem 0xe0000000-0xefffffff 64bit pref]
[    5.032432] pcieport 0000:66:00.0: BAR 15: releasing [mem 0xe0000000-0xf01fffff 64bit pref]
[    5.032433] pcieport 0000:65:00.0: BAR 15: releasing [mem 0xe0000000-0xf01fffff 64bit pref]
[    5.032434] pcieport 0000:64:00.0: BAR 15: releasing [mem 0xe0000000-0xf01fffff 64bit pref]
[    5.032439] pcieport 0000:64:00.0: BAR 15: assigned [mem 0x382000000000-0x3825ffffffff 64bit pref]
[    5.032440] pcieport 0000:65:00.0: BAR 15: assigned [mem 0x382000000000-0x3825ffffffff 64bit pref]
[    5.032441] pcieport 0000:66:00.0: BAR 15: assigned [mem 0x382000000000-0x3825ffffffff 64bit pref]
[    5.032442] amdgpu 0000:67:00.0: BAR 0: assigned [mem 0x382000000000-0x3823ffffffff 64bit pref]
[    5.032450] amdgpu 0000:67:00.0: BAR 2: assigned [mem 0x382400000000-0x3824001fffff 64bit pref]
[    5.032459] pcieport 0000:64:00.0: PCI bridge to [bus 65-67]
[    5.032460] pcieport 0000:64:00.0:   bridge window [io  0xb000-0xbfff]
[    5.032462] pcieport 0000:64:00.0:   bridge window [mem 0xf0900000-0xf0afffff]
[    5.032463] pcieport 0000:64:00.0:   bridge window [mem 0x382000000000-0x3825ffffffff 64bit pref]
[    5.032465] pcieport 0000:65:00.0: PCI bridge to [bus 66-67]
[    5.032467] pcieport 0000:65:00.0:   bridge window [io  0xb000-0xbfff]
[    5.032471] pcieport 0000:65:00.0:   bridge window [mem 0xf0900000-0xf09fffff]
[    5.032474] pcieport 0000:65:00.0:   bridge window [mem 0x382000000000-0x3825ffffffff 64bit pref]
[    5.032478] pcieport 0000:66:00.0: PCI bridge to [bus 67]
[    5.032480] pcieport 0000:66:00.0:   bridge window [io  0xb000-0xbfff]
[    5.032484] pcieport 0000:66:00.0:   bridge window [mem 0xf0900000-0xf09fffff]
[    5.032486] pcieport 0000:66:00.0:   bridge window [mem 0x382000000000-0x3825ffffffff 64bit pref]
[    5.032498] amdgpu 0000:67:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
[    5.032499] amdgpu 0000:67:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[    5.032500] amdgpu 0000:67:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF
[    5.032505] [drm] Detected VRAM RAM=16368M, BAR=16384M
[    5.032505] [drm] RAM width 4096bits HBM
[    5.032532] [drm] amdgpu: 16368M of VRAM memory ready
[    5.032534] [drm] amdgpu: 11789M of GTT memory ready.
[    5.032540] [drm] GART: num cpu pages 131072, num gpu pages 131072
[    5.032650] [drm] PCIE GART of 512M enabled (table at 0x0000008000000000).
[    5.032766] amdgpu 0000:67:00.0: Direct firmware load for amdgpu/vega20_ta.bin failed with error -2
[    5.032768] amdgpu 0000:67:00.0: psp v11.0: Failed to load firmware "amdgpu/vega20_ta.bin"
[    5.033693] [drm] use_doorbell being set to: [true]
[    5.034029] [drm] use_doorbell being set to: [true]
[    5.034078] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu
[    5.034087] [drm] Found UVD firmware ENC: 1.1 DEC: .23 Family ID: 19
[    5.034089] [drm] PSP loading UVD firmware
[    5.062484] [drm] Found VCE firmware Version: 55.5 Binary ID: 4
[    5.062516] [drm] PSP loading VCE firmware
[    5.565320] [drm] reserve 0x400000 from 0x83fe800000 for PSP TMR
[    5.619025] kvm: disabled by bios
[    5.725481] kvm: disabled by bios
[    5.731037] EDAC skx: ECC is disabled on imc 0
[    5.813895] [drm] Display Core initialized with v3.2.48!
[    5.814428] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[    5.814428] [drm] Driver supports precise vblank timestamp query.
[    5.825639] kvm: disabled by bios
[    5.831223] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
[    5.872739] ------------[ cut here ]------------
[    5.872818] WARNING: CPU: 0 PID: 275 at drivers/gpu/drm/amd/amdgpu/uvd_v7_0.c:1390 uvd_v7_0_ring_insert_nop+0x25/0x140 [amdgpu]
[    5.872819] Modules linked in: kvm_intel(-) nfit x86_pkg_temp_thermal intel_powerclamp kvm crct10dif_pclmul crc32_pclmul ghash_clmulni_intel iwlmvm mac80211 aesni_intel libarc4 crypto_simd amdgpu(+) input_leds cryptd iwlwifi joydev glue_helper intel_cstate amd_iommu_v2 gpu_sched intel_wmi_thunderbolt intel_rapl_perf ttm drm_kms_helper btusb drm btrtl btbcm btintel fb_sys_fops syscopyarea bluetooth sysfillrect sysimgblt cfg80211 mxm_wmi ecdh_generic ecc mei_me ioatdma mei mac_hid sch_fq_codel nct6775 hwmon_vid coretemp parport_pc ppdev lp parport ip_tables x_tables autofs4 hid_generic usbhid hid igb e1000e ahci i2c_algo_bit dca i2c_i801 libahci wmi
[    5.872836] CPU: 0 PID: 275 Comm: kworker/0:3 Not tainted 5.4.24-050424-generic #202003051135
[    5.872837] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./X299 Taichi, BIOS P2.50 11/29/2019
[    5.872840] Workqueue: events work_for_cpu_fn
[    5.872891] RIP: 0010:uvd_v7_0_ring_insert_nop+0x25/0x140 [amdgpu]
[    5.872892] Code: 00 00 0f 1f 00 0f 1f 44 00 00 55 48 89 e5 41 57 41 56 41 55 41 54 41 89 f4 53 48 89 fb f6 87 38 02 00 00 01 0f 84 0b 01 00 00 <0f> 0b 41 d1 ec 0f 84 f5 00 00 00 4c 8b 33 8b 83 50 02 00 00 45 31
[    5.872893] RSP: 0018:ffffac850040fc10 EFLAGS: 00010202
[    5.872894] RAX: ffffffffc0a51c00 RBX: ffff974286f8d358 RCX: 0000000000000010
[    5.872894] RDX: 000000000000000f RSI: 000000000000000f RDI: ffff974286f8d358
[    5.872895] RBP: ffffac850040fc38 R08: 0000000000000200 R09: 0000000000000000
[    5.872895] R10: ffff97428fe17848 R11: 0000000000000000 R12: 000000000000000f
[    5.872896] R13: 0000000000000000 R14: ffff974286f80000 R15: ffff974286f80000
[    5.872896] FS:  0000000000000000(0000) GS:ffff97428fe00000(0000) knlGS:0000000000000000
[    5.872897] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[    5.872897] CR2: 000055b4e9402000 CR3: 0000000478c0a006 CR4: 00000000003606f0
[    5.872898] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
[    5.872898] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
[    5.872899] Call Trace:
[    5.872936]  amdgpu_ring_commit+0x3c/0x70 [amdgpu]
[    5.872981]  uvd_v7_0_ring_test_ring+0x118/0x1a0 [amdgpu]
[    5.873016]  amdgpu_ring_test_helper+0x21/0x80 [amdgpu]
[    5.873061]  uvd_v7_0_hw_init+0xf6/0x670 [amdgpu]
[    5.873121]  amdgpu_device_ip_init+0x345/0x3df [amdgpu]
[    5.873179]  amdgpu_device_init.cold+0x7e0/0xbbc [amdgpu]
[    5.873212]  amdgpu_driver_load_kms+0x5a/0x1c0 [amdgpu]
[    5.873223]  drm_dev_register+0x12f/0x170 [drm]
[    5.873255]  amdgpu_pci_probe+0xf7/0x160 [amdgpu]
[    5.873258]  ? __pm_runtime_resume+0x60/0x80
[    5.873260]  local_pci_probe+0x48/0x80
[    5.873262]  ? __schedule+0x2eb/0x740
[    5.873263]  work_for_cpu_fn+0x1a/0x30
[    5.873264]  process_one_work+0x1eb/0x3b0
[    5.873265]  worker_thread+0x21e/0x400
[    5.873267]  kthread+0x104/0x140
[    5.873268]  ? process_one_work+0x3b0/0x3b0
[    5.873268]  ? kthread_park+0x90/0x90
[    5.873270]  ret_from_fork+0x35/0x40
[    5.873271] ---[ end trace f24dcee1849a647b ]---
[    5.900556] EDAC skx: ECC is disabled on imc 0
[    5.993133] amdgpu 0000:67:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring uvd_0 test failed (-110)
[    5.994608] [drm:amdgpu_device_ip_init [amdgpu]] *ERROR* hw_init of IP block <uvd_v7_0> failed -110
[    5.995898] amdgpu 0000:67:00.0: amdgpu_device_ip_init failed
[    5.996722] amdgpu 0000:67:00.0: Fatal error during GPU init
[    5.997529] [drm] amdgpu: finishing device.
[    5.998074] amdgpu: [powerplay] Failed to send message 0x26, response 0xffffffff
[    5.999129] amdgpu: [powerplay] Failed to set soft min gfxclk !
[    5.999130] amdgpu: [powerplay] Failed to upload DPM Bootup Levels!
[    5.999131] amdgpu: [powerplay] Failed to send message 0xc, response 0xffffffff
[    6.000179] amdgpu: [powerplay] [GetEnabledSMCFeatures] Attemp to get SMU features Low failed!
[    6.000179] amdgpu: [powerplay] dpm has been disabled
[    6.120457] amdgpu 0000:67:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring kiq_2.1.0 test failed (-110)
[    6.121969] [drm:gfx_v9_0_hw_fini [amdgpu]] *ERROR* KCQ disable failed
[    6.362425] [drm] Timeout wait for RLC serdes 0,0
[    6.408330] ------------[ cut here ]------------
[    6.408330] Memory manager not clean during takedown.
[    6.408363] WARNING: CPU: 0 PID: 275 at drivers/gpu/drm/drm_mm.c:939 drm_mm_takedown+0x23/0x30 [drm]
[    6.408363] Modules linked in: isst_if_common nfit x86_pkg_temp_thermal intel_powerclamp kvm crct10dif_pclmul crc32_pclmul ghash_clmulni_intel iwlmvm mac80211 aesni_intel libarc4 crypto_simd amdgpu(+) input_leds cryptd iwlwifi joydev glue_helper intel_cstate amd_iommu_v2 gpu_sched intel_wmi_thunderbolt intel_rapl_perf ttm drm_kms_helper btusb drm btrtl btbcm btintel fb_sys_fops syscopyarea bluetooth sysfillrect sysimgblt cfg80211 mxm_wmi ecdh_generic ecc mei_me ioatdma mei mac_hid sch_fq_codel nct6775 hwmon_vid coretemp parport_pc ppdev lp parport ip_tables x_tables autofs4 hid_generic usbhid hid igb e1000e ahci i2c_algo_bit dca i2c_i801 libahci wmi
[    6.408378] CPU: 0 PID: 275 Comm: kworker/0:3 Tainted: G        W         5.4.24-050424-generic #202003051135
[    6.408379] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./X299 Taichi, BIOS P2.50 11/29/2019
[    6.408382] Workqueue: events work_for_cpu_fn
[    6.408388] RIP: 0010:drm_mm_takedown+0x23/0x30 [drm]
[    6.408389] Code: e8 32 dd 93 c8 66 90 0f 1f 44 00 00 48 8b 47 38 48 83 c7 38 48 39 c7 75 01 c3 55 48 c7 c7 d8 13 7a c0 48 89 e5 e8 38 e0 93 c8 <0f> 0b 5d c3 66 0f 1f 84 00 00 00 00 00 0f 1f 44 00 00 55 48 89 e5
[    6.408390] RSP: 0018:ffffac850040fc18 EFLAGS: 00010286
[    6.408391] RAX: 0000000000000000 RBX: ffff974286f850e0 RCX: 0000000000000006
[    6.408391] RDX: 0000000000000007 RSI: 0000000000000086 RDI: ffff97428fe178c0
[    6.408392] RBP: ffffac850040fc18 R08: 0000000000000570 R09: 0000000000000004
[    6.408392] R10: 0000000000000000 R11: 0000000000000001 R12: ffff974286f84f50
[    6.408393] R13: ffff9742853844e8 R14: ffff974285384400 R15: 0000000000000170
[    6.408393] FS:  0000000000000000(0000) GS:ffff97428fe00000(0000) knlGS:0000000000000000
[    6.408394] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[    6.408394] CR2: 000055b4e9402000 CR3: 0000000478c0a006 CR4: 00000000003606f0
[    6.408395] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
[    6.408395] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
[    6.408396] Call Trace:
[    6.408460]  amdgpu_vram_mgr_fini+0x31/0xb0 [amdgpu]
[    6.408464]  ttm_bo_clean_mm+0xac/0xc0 [ttm]
[    6.408501]  amdgpu_ttm_fini+0x76/0xd0 [amdgpu]
[    6.408534]  amdgpu_bo_fini+0x12/0x40 [amdgpu]
[    6.408576]  gmc_v9_0_sw_fini+0x11b/0x180 [amdgpu]
[    6.408611]  ? amdgpu_sa_bo_manager_fini+0x89/0xa0 [amdgpu]
[    6.408671]  amdgpu_device_fini+0x26b/0x4ac [amdgpu]
[    6.408706]  amdgpu_driver_unload_kms+0x52/0xa0 [amdgpu]
[    6.408764]  amdgpu_driver_load_kms.cold+0x39/0x5c [amdgpu]
[    6.408771]  drm_dev_register+0x12f/0x170 [drm]
[    6.408803]  amdgpu_pci_probe+0xf7/0x160 [amdgpu]
[    6.408806]  ? __pm_runtime_resume+0x60/0x80
[    6.408808]  local_pci_probe+0x48/0x80
[    6.408810]  ? __schedule+0x2eb/0x740
[    6.408811]  work_for_cpu_fn+0x1a/0x30
[    6.408813]  process_one_work+0x1eb/0x3b0
[    6.408814]  worker_thread+0x21e/0x400
[    6.408815]  kthread+0x104/0x140
[    6.408816]  ? process_one_work+0x3b0/0x3b0
[    6.408817]  ? kthread_park+0x90/0x90
[    6.408818]  ret_from_fork+0x35/0x40
[    6.408820] ---[ end trace f24dcee1849a647c ]---
[    6.408827] [drm] amdgpu: ttm finalized
[    6.408841] ------------[ cut here ]------------
[    6.408842] sysfs group 'fw_version' not found for kobject '0000:67:00.0'
[    6.408848] WARNING: CPU: 0 PID: 275 at fs/sysfs/group.c:278 sysfs_remove_group+0x7c/0x80
[    6.408848] Modules linked in: isst_if_common nfit x86_pkg_temp_thermal intel_powerclamp kvm crct10dif_pclmul crc32_pclmul ghash_clmulni_intel iwlmvm mac80211 aesni_intel libarc4 crypto_simd amdgpu(+) input_leds cryptd iwlwifi joydev glue_helper intel_cstate amd_iommu_v2 gpu_sched intel_wmi_thunderbolt intel_rapl_perf ttm drm_kms_helper btusb drm btrtl btbcm btintel fb_sys_fops syscopyarea bluetooth sysfillrect sysimgblt cfg80211 mxm_wmi ecdh_generic ecc mei_me ioatdma mei mac_hid sch_fq_codel nct6775 hwmon_vid coretemp parport_pc ppdev lp parport ip_tables x_tables autofs4 hid_generic usbhid hid igb e1000e ahci i2c_algo_bit dca i2c_i801 libahci wmi
[    6.408859] CPU: 0 PID: 275 Comm: kworker/0:3 Tainted: G        W         5.4.24-050424-generic #202003051135
[    6.408860] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./X299 Taichi, BIOS P2.50 11/29/2019
[    6.408861] Workqueue: events work_for_cpu_fn
[    6.408862] RIP: 0010:sysfs_remove_group+0x7c/0x80
[    6.408863] Code: e7 e8 a8 bb ff ff 5b 41 5c 41 5d 5d c3 4c 89 e7 e8 f9 b6 ff ff eb c9 49 8b 55 00 48 8b 33 48 c7 c7 08 6c 38 8a e8 8f ba d1 ff <0f> 0b eb d8 0f 1f 44 00 00 48 85 f6 74 37 55 48 89 e5 41 55 41 54
[    6.408863] RSP: 0018:ffffac850040fcf8 EFLAGS: 00010282
[    6.408864] RAX: 0000000000000000 RBX: ffffffffc0c08a00 RCX: 0000000000000006
[    6.408864] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff97428fe178c0
[    6.408865] RBP: ffffac850040fd10 R08: 000000000000059c R09: 0000000000000004
[    6.408865] R10: 0000000000000000 R11: 0000000000000001 R12: 0000000000000000
[    6.408866] R13: ffff97428cdc90b0 R14: ffff974286f94da8 R15: ffff974286ee6600
[    6.408866] FS:  0000000000000000(0000) GS:ffff97428fe00000(0000) knlGS:0000000000000000
[    6.408867] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[    6.408867] CR2: 000055b4e9402000 CR3: 0000000478c0a006 CR4: 00000000003606f0
[    6.408868] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
[    6.408868] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
[    6.408869] Call Trace:
[    6.408908]  amdgpu_ucode_sysfs_fini+0x18/0x20 [amdgpu]
[    6.408968]  amdgpu_device_fini+0x47a/0x4ac [amdgpu]
[    6.409001]  amdgpu_driver_unload_kms+0x52/0xa0 [amdgpu]
[    6.409059]  amdgpu_driver_load_kms.cold+0x39/0x5c [amdgpu]
[    6.409066]  drm_dev_register+0x12f/0x170 [drm]
[    6.409098]  amdgpu_pci_probe+0xf7/0x160 [amdgpu]
[    6.409100]  ? __pm_runtime_resume+0x60/0x80
[    6.409101]  local_pci_probe+0x48/0x80
[    6.409102]  ? __schedule+0x2eb/0x740
[    6.409103]  work_for_cpu_fn+0x1a/0x30
[    6.409104]  process_one_work+0x1eb/0x3b0
[    6.409105]  worker_thread+0x21e/0x400
[    6.409106]  kthread+0x104/0x140
[    6.409107]  ? process_one_work+0x3b0/0x3b0
[    6.409108]  ? kthread_park+0x90/0x90
[    6.409109]  ret_from_fork+0x35/0x40
[    6.409110] ---[ end trace f24dcee1849a647d ]---
[    6.409271] amdgpu: probe of 0000:67:00.0 failed with error -110
```

---

## 评论 (4 条)

### 评论 #1 — valeriob01 (2020-03-08T11:02:42Z)

This line:
5.872836] CPU: 0 PID: 275 Comm: kworker/0:3 Not tainted 5.4.24-050424-generic #20200

warns you about the kernel in use, this version is not good.


---

### 评论 #2 — preda (2020-03-08T12:50:40Z)

It seems it was, most likely, a power cable issue. The GPU itself was fine, and the problem most likely was not caused by software.


---

### 评论 #3 — valeriob01 (2020-03-08T12:58:14Z)

> It seems it was, most likely, a power cable issue. The GPU itself was fine, and the problem most likely was not caused by software.

BTW, the same Line shows up with wrong kernel version !!!
It occurred to me with Ubuntu.

---

### 评论 #4 — valeriob01 (2020-03-08T13:12:39Z)

> It seems it was, most likely, a power cable issue. The GPU itself was fine, and the problem most likely was not caused by software.

What cables are you using?



---
