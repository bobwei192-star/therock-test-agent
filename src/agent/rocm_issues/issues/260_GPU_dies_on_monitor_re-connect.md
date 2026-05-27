# GPU dies on monitor re-connect

> **Issue #260**
> **状态**: closed
> **创建时间**: 2017-11-23T21:38:47Z
> **更新时间**: 2018-06-03T15:09:54Z
> **关闭时间**: 2018-06-03T15:09:54Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/260

## 描述

ROCm 1.6-180, Ubuntu 16.04.3, RxVega64.

This is what I do:
1. I disconnect the monitor (HDMI),
2. after a few seconds, I re-connect the same monitor, on the same slot.

The GPU dies, see dmesg trace below.
This seems to happen not every time (not 100% reproducible).


[72902.684747] [drm] link=3, dc_sink_in=          (null) is now Disconnected
[72902.684750] [drm] DCHPD: connector_id=3: Old sink=ffff8eb77657f800 New sink=          (null)
[72904.081797] [drm] [Detect]	[HDMIA][ConnIdx:3] Kogan Monitor: [Block 0] 00 FF FF FF FF FF FF 00 4B 1F 00 30 00 00 00 00 11 18 01 03 80 3C 28 78 EE EE 95 A3 54 4C 99 26 0F 50 54 A5 CB 00 71 4F 81 C0 81 80 95 00 B3 00 D1 C0 01 01 01 01 E2 68 00 A0 A0 40 2E 60 30 20 36 00 55 50 21 00 00 1A 00 00 00 FF 00 4E 41 0A 20 20 20 20 20 20 20 20 20 20 00 00 00 FD 00 17 4C 0F 63 19 00 0A 20 20 20 20 20 20 00 00 00 FC 00 4B 6F 67 61 6E 20 4D 6F 6E 69 74 6F 72 01 2E ^
[72904.081812] [drm] [Detect]	[HDMIA][ConnIdx:3] Kogan Monitor: [Block 1] 02 03 1F F1 4C 01 02 03 04 05 07 90 12 13 14 16 1F 23 09 07 07 83 01 00 00 65 03 0C 00 10 00 02 3A 80 18 71 38 2D 40 58 2C 45 00 FE 1F 11 00 00 1E 01 1D 80 18 71 1C 16 20 58 2C 25 00 FE 1F 11 00 00 9E 01 1D 00 72 51 D0 1E 20 6E 28 55 00 FE 1F 11 00 00 1E 8C 0A D0 8A 20 E0 2D 10 10 3E 96 00 FE 1F 11 00 00 18 01 1D 00 BC 52 D0 1E 20 B8 28 55 40 E8 12 11 00 00 1E 00 00 00 00 00 00 07 ^
[72904.081815] [drm] dc_link_detect: manufacturer_id = 1F4B, product_id = 3000, serial_number = 0, manufacture_week = 17, manufacture_year = 24, display_name = Kogan Monitor, speaker_flag = 1, audio_mode_count = 1
[72904.081816] [drm] dc_link_detect: mode number = 0, format_code = 1, channel_count = 1, sample_rate = 7, sample_size = 7
[72904.081818] [drm] link=3, dc_sink_in=ffff8eb775949c00 is now Connected
[72904.081820] [drm] DCHPD: connector_id=3: Old sink=          (null) New sink=ffff8eb775949c00
[72904.081853] [drm] No preferred mode found
[72904.082224] [drm] No preferred mode found
[72904.082230] [drm] Atomic commit: SET crtc id 0: [ffff8eb778433000]
[72904.082246] [drm] dc_commit_streams: 1 streams
[72904.082248] [drm] core_stream 0x75948800: src: 0, 0, 2560, 1600; dst: 0, 0, 2560, 1600, colorSpace:4
[72904.082249] [drm] 	pix_clk_khz: 268500, h_total: 2720, v_total: 1646, pixelencoder:3, displaycolorDepth:2
[72904.082250] [drm] 	sink name: Kogan Monitor, serial: 0
[72904.082250] [drm] 	link: 3
[72904.101971] [drm] [Mode]	[HDMIA][ConnIdx:3] {2560x1600, 2720x1646@268500Khz}^
[75697.324139] [drm] link=3, dc_sink_in=          (null) is now Disconnected
[75697.324142] [drm] DCHPD: connector_id=3: Old sink=ffff8eb775949c00 New sink=          (null)
[75709.630090] [drm] [Detect]	[HDMIA][ConnIdx:3] Kogan Monitor: [Block 0] 00 FF FF FF FF FF FF 00 4B 1F 00 30 00 00 00 00 11 18 01 03 80 3C 28 78 EE EE 95 A3 54 4C 99 26 0F 50 54 A5 CB 00 71 4F 81 C0 81 80 95 00 B3 00 D1 C0 01 01 01 01 E2 68 00 A0 A0 40 2E 60 30 20 36 00 55 50 21 00 00 1A 00 00 00 FF 00 4E 41 0A 20 20 20 20 20 20 20 20 20 20 00 00 00 FD 00 17 4C 0F 63 19 00 0A 20 20 20 20 20 20 00 00 00 FC 00 4B 6F 67 61 6E 20 4D 6F 6E 69 74 6F 72 01 2E ^
[75709.630105] [drm] [Detect]	[HDMIA][ConnIdx:3] Kogan Monitor: [Block 1] 02 03 1F F1 4C 01 02 03 04 05 07 90 12 13 14 16 1F 23 09 07 07 83 01 00 00 65 03 0C 00 10 00 02 3A 80 18 71 38 2D 40 58 2C 45 00 FE 1F 11 00 00 1E 01 1D 80 18 71 1C 16 20 58 2C 25 00 FE 1F 11 00 00 9E 01 1D 00 72 51 D0 1E 20 6E 28 55 00 FE 1F 11 00 00 1E 8C 0A D0 8A 20 E0 2D 10 10 3E 96 00 FE 1F 11 00 00 18 01 1D 00 BC 52 D0 1E 20 B8 28 55 40 E8 12 11 00 00 1E 00 00 00 00 00 00 07 ^
[75709.630108] [drm] dc_link_detect: manufacturer_id = 1F4B, product_id = 3000, serial_number = 0, manufacture_week = 17, manufacture_year = 24, display_name = Kogan Monitor, speaker_flag = 1, audio_mode_count = 1
[75709.630109] [drm] dc_link_detect: mode number = 0, format_code = 1, channel_count = 1, sample_rate = 7, sample_size = 7
[75709.630114] [drm] link=3, dc_sink_in=ffff8eb77657f000 is now Connected
[75709.630116] [drm] DCHPD: connector_id=3: Old sink=          (null) New sink=ffff8eb77657f000
[75709.630151] [drm] No preferred mode found
[75709.630537] [drm] No preferred mode found
[75709.630543] [drm] Atomic commit: SET crtc id 0: [ffff8eb778433000]
[75709.630559] [drm] dc_commit_streams: 1 streams
[75709.630561] [drm] core_stream 0x7657d000: src: 0, 0, 2560, 1600; dst: 0, 0, 2560, 1600, colorSpace:4
[75709.630562] [drm] 	pix_clk_khz: 268500, h_total: 2720, v_total: 1646, pixelencoder:3, displaycolorDepth:2
[75709.630563] [drm] 	sink name: Kogan Monitor, serial: 0
[75709.630563] [drm] 	link: 3
[75709.659366] [drm] [Mode]	[HDMIA][ConnIdx:3] {2560x1600, 2720x1646@268500Khz}^
[75710.694264] [drm] link=3, dc_sink_in=          (null) is now Disconnected
[75710.694267] [drm] DCHPD: connector_id=3: Old sink=ffff8eb77657f000 New sink=          (null)
[75711.220054] [drm] [Detect]	[HDMIA][ConnIdx:3] Kogan Monitor: [Block 0] 00 FF FF FF FF FF FF 00 4B 1F 00 30 00 00 00 00 11 18 01 03 80 3C 28 78 EE EE 95 A3 54 4C 99 26 0F 50 54 A5 CB 00 71 4F 81 C0 81 80 95 00 B3 00 D1 C0 01 01 01 01 E2 68 00 A0 A0 40 2E 60 30 20 36 00 55 50 21 00 00 1A 00 00 00 FF 00 4E 41 0A 20 20 20 20 20 20 20 20 20 20 00 00 00 FD 00 17 4C 0F 63 19 00 0A 20 20 20 20 20 20 00 00 00 FC 00 4B 6F 67 61 6E 20 4D 6F 6E 69 74 6F 72 01 2E ^
[75711.220068] [drm] [Detect]	[HDMIA][ConnIdx:3] Kogan Monitor: [Block 1] 02 03 1F F1 4C 01 02 03 04 05 07 90 12 13 14 16 1F 23 09 07 07 83 01 00 00 65 03 0C 00 10 00 02 3A 80 18 71 38 2D 40 58 2C 45 00 FE 1F 11 00 00 1E 01 1D 80 18 71 1C 16 20 58 2C 25 00 FE 1F 11 00 00 9E 01 1D 00 72 51 D0 1E 20 6E 28 55 00 FE 1F 11 00 00 1E 8C 0A D0 8A 20 E0 2D 10 10 3E 96 00 FE 1F 11 00 00 18 01 1D 00 BC 52 D0 1E 20 B8 28 55 40 E8 12 11 00 00 1E 00 00 00 00 00 00 07 ^
[75711.220070] [drm] dc_link_detect: manufacturer_id = 1F4B, product_id = 3000, serial_number = 0, manufacture_week = 17, manufacture_year = 24, display_name = Kogan Monitor, speaker_flag = 1, audio_mode_count = 1
[75711.220071] [drm] dc_link_detect: mode number = 0, format_code = 1, channel_count = 1, sample_rate = 7, sample_size = 7
[75711.220073] [drm] link=3, dc_sink_in=ffff8eb77657fc00 is now Connected
[75711.220074] [drm] DCHPD: connector_id=3: Old sink=          (null) New sink=ffff8eb77657fc00
[75711.220101] [drm] No preferred mode found
[75711.220454] [drm] No preferred mode found
[75711.220459] [drm] Atomic commit: SET crtc id 0: [ffff8eb778433000]
[75711.220476] [drm] dc_commit_streams: 1 streams
[75711.220478] [drm] core_stream 0x7657bc00: src: 0, 0, 2560, 1600; dst: 0, 0, 2560, 1600, colorSpace:4
[75711.220479] [drm] 	pix_clk_khz: 268500, h_total: 2720, v_total: 1646, pixelencoder:3, displaycolorDepth:2
[75711.220480] [drm] 	sink name: Kogan Monitor, serial: 0
[75711.220480] [drm] 	link: 3
[75711.245418] [drm] [Mode]	[HDMIA][ConnIdx:3] {2560x1600, 2720x1646@268500Khz}^
[76125.175190] amdgpu: [powerplay] Failed to send message: 0x46
[76136.329828] amdgpu: [powerplay] Failed to send message: 0x23
[76136.330020] amdgpu: [powerplay] Failed to send message: 0x23
[76136.330107] amdgpu: [powerplay] Failed to send message: 0x26
[76136.330179] amdgpu: [powerplay] Failed to send message: 0x26
[76136.330569] amdgpu: [powerplay] Failed to send message: 0x46
[76136.330968] amdgpu: [powerplay] Failed to send message: 0x46
[76136.344367] amdgpu: [powerplay] Failed to send message: 0x26
[76136.344376] BUG: unable to handle kernel paging request at ffff8ec378ae00f4
[76136.344461] IP: vega10_read_sensor+0x13d/0x1c0 [amdgpu]
[76136.344479] PGD 122f21f067 
[76136.344480] PUD 0 

[76136.344503] Oops: 0000 [#1] SMP
[76136.344514] Modules linked in: intel_rapl sb_edac edac_core x86_pkg_temp_thermal intel_powerclamp coretemp kvm snd_hda_codec_realtek snd_hda_codec_generic irqbypass crct10dif_pclmul crc32_pclmul snd_hda_codec_hdmi ghash_clmulni_intel input_leds cryptd snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi snd_seq snd_seq_device snd_timer snd soundcore lpc_ich shpchp ioatdma acpi_power_meter mac_hid parport_pc ppdev lp parport autofs4 hid_generic usbhid hid amdkfd amd_iommu_v2 amdgpu mxm_wmi ttm drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops drm igb dca ptp pps_core ahci i2c_algo_bit libahci wmi
[76136.344715] CPU: 14 PID: 15080 Comm: rocm-smi Not tainted 4.11.0-kfd-compute-rocm-rel-1.6-180 #1
[76136.344742] Hardware name: Supermicro X10DAi/X10DAI, BIOS 2.0 02/02/2016
[76136.344763] task: ffff8ea7113f0000 task.stack: ffffae25cc68c000
[76136.344816] RIP: 0010:vega10_read_sensor+0x13d/0x1c0 [amdgpu]
[76136.344834] RSP: 0018:ffffae25cc68fcd8 EFLAGS: 00010246
[76136.344851] RAX: 00000002fffffffd RBX: ffffae25cc68fd68 RCX: 0000000000000000
[76136.344873] RDX: 0000000000000000 RSI: 0000000000016292 RDI: ffff8eb773480000
[76136.344895] RBP: ffffae25cc68fd08 R08: 000000000005412f R09: 000000000000058b
[76136.344916] R10: ffff8eb6e0775000 R11: ffffffff8b12b0cd R12: ffff8eb773c60000
[76136.344938] R13: 0000000000000000 R14: ffffae25cc68fd6c R15: ffff8eb778ae0000
[76136.344960] FS:  00007f7809d2d700(0000) GS:ffff8eb7bfd80000(0000) knlGS:0000000000000000
[76136.344984] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[76136.345002] CR2: ffff8ec378ae00f4 CR3: 0000001fea813000 CR4: 00000000001406e0
[76136.345024] Call Trace:
[76136.345069]  pp_dpm_read_sensor+0x98/0xd0 [amdgpu]
[76136.345107]  amdgpu_debugfs_pm_info+0x1bf/0x790 [amdgpu]
[76136.345127]  seq_read+0xdb/0x370
[76136.345140]  ? do_filp_open+0x9e/0xf0
[76136.345156]  full_proxy_read+0x54/0x90
[76136.345170]  __vfs_read+0x28/0x130
[76136.345188]  ? security_file_permission+0x9b/0xc0
[76136.345204]  ? rw_verify_area+0x4e/0xb0
[76136.345217]  vfs_read+0x93/0x130
[76136.345228]  SyS_read+0x46/0xa0
[76136.345239]  ? SyS_lseek+0x8a/0xb0
[76136.345253]  entry_SYSCALL_64_fastpath+0x1e/0xad
[76136.345269] RIP: 0033:0x7f780991d500
[76136.345280] RSP: 002b:00007ffd8193db78 EFLAGS: 00000246 ORIG_RAX: 0000000000000000
[76136.345304] RAX: ffffffffffffffda RBX: 000000000217b490 RCX: 00007f780991d500
[76136.345325] RDX: 0000000000002000 RSI: 0000000002333720 RDI: 0000000000000003
[76136.345347] RBP: 0000000000a3e020 R08: 0000000000000000 R09: 00007ffd8193d890
[76136.345369] R10: 0000000000000100 R11: 0000000000000246 R12: 0000000000000003
[76136.345391] R13: 0000000000501520 R14: 00007ffd8193da10 R15: 00007f7807f1a558
[76136.345413] Code: 18 be 26 00 00 00 e8 f3 6b fd ff 85 c0 41 89 c5 0f 85 58 ff ff ff 49 8b 7c 24 18 48 8d 75 d4 e8 3a 8a fe ff 8b 45 d4 48 8d 04 40 <41> 8b 84 87 00 01 00 00 89 03 41 c7 06 04 00 00 00 e9 2d ff ff 
[76136.345522] RIP: vega10_read_sensor+0x13d/0x1c0 [amdgpu] RSP: ffffae25cc68fcd8
[76136.345544] CR2: ffff8ec378ae00f4
[76136.360935] ---[ end trace 7e84fe67df573abe ]---

---

## 评论 (1 条)

### 评论 #1 — Cyclic3 (2017-11-25T08:18:31Z)

I had a similar problem on my box with the amd-staging kernel. I fixed it by adding `tsc=unstable` to my boot options

---
