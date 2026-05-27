# crash: events_unbound commit_work [drm_kms_helper]

> **Issue #342**
> **状态**: closed
> **创建时间**: 2018-02-21T03:22:05Z
> **更新时间**: 2018-06-03T14:43:18Z
> **关闭时间**: 2018-06-03T14:43:18Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/342

## 描述

Ubuntu 17.10, ROCm 1.7, Vega64.
While running the OpenCL app GpuOwl, I get a complete GPU freeze. I see this in dmesg:

```
[707581.262503] INFO: task kworker/u34:0:13629 blocked for more than 120 seconds.
[707581.262508]       Tainted: G           OE   4.13.0-32-generic #35-Ubuntu
[707581.262509] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
[707581.262511] kworker/u34:0   D    0 13629      2 0x00000000
[707581.262533] Workqueue: events_unbound commit_work [drm_kms_helper]
[707581.262534] Call Trace:
[707581.262541]  __schedule+0x28b/0x880
[707581.262543]  schedule+0x36/0x80
[707581.262544]  schedule_timeout+0x1f1/0x350
[707581.262631]  ? amdgpu_cgs_read_register+0x14/0x20 [amdgpu]
[707581.262672]  ? dce120_timing_generator_get_crtc_position+0x5d/0xb0 [amdgpu]
[707581.262709]  ? dce120_timing_generator_get_crtc_scanoutpos+0x76/0xd0 [amdgpu]
[707581.262714]  kcl_fence_default_wait+0x1c2/0x250 [amdkcl]
[707581.262715]  ? kcl_fence_default_wait+0x1c2/0x250 [amdkcl]
[707581.262720]  ? dma_fence_free+0x20/0x20
[707581.262723]  dma_fence_wait_timeout+0x38/0xf0
[707581.262724]  reservation_object_wait_timeout_rcu+0x14f/0x2d0
[707581.262763]  amdgpu_dm_do_flip+0x112/0x360 [amdgpu]
[707581.262766]  ? __slab_free+0x14c/0x2d0
[707581.262803]  amdgpu_dm_atomic_commit_tail+0x854/0xa40 [amdgpu]
[707581.262807]  ? pick_next_task_fair+0x48e/0x560
[707581.262809]  ? __switch_to+0xad/0x540
[707581.262817]  commit_tail+0x3f/0x60 [drm_kms_helper]
[707581.262821]  commit_work+0x12/0x20 [drm_kms_helper]
[707581.262825]  process_one_work+0x1e7/0x410
[707581.262827]  worker_thread+0x4b/0x420
[707581.262829]  kthread+0x125/0x140
[707581.262830]  ? process_one_work+0x410/0x410
[707581.262832]  ? kthread_create_on_node+0x70/0x70
[707581.262833]  ? kthread_create_on_node+0x70/0x70
[707581.262836]  ret_from_fork+0x1f/0x30
```

---

## 评论 (10 条)

### 评论 #1 — preda (2018-02-21T11:51:14Z)

More dmesg log from a new occurrence:
[gpu.txt](https://github.com/RadeonOpenCompute/ROCm/files/1743858/gpu.txt)


---

### 评论 #2 — gstoner (2018-02-21T12:35:30Z)

Is this 1.7 or 1.7.1

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Mihai Preda <notifications@github.com>
Sent: Wednesday, February 21, 2018 5:51:16 AM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: Re: [RadeonOpenCompute/ROCm] crash: events_unbound commit_work [drm_kms_helper] (#342)


More dmesg log from a new occurrence:
gpu.txt<https://github.com/RadeonOpenCompute/ROCm/files/1743858/gpu.txt>

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/342#issuecomment-367302451>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuW14WdXSbbf_6So_9_mnbI6Ia6L7ks5tXAMzgaJpZM4SNBWP>.


---

### 评论 #3 — fxkamd (2018-02-21T15:59:13Z)

This looks like a DAL problem.

---

### 评论 #4 — preda (2018-02-21T19:43:49Z)

@gstoner: this is standard 1.7.

I was not seeing this before. Recently I made a few changes to the app, which apparently caused this to trigger. One of the changes was starting using atomic_max() on global memory, but I have no idea if that is related.


---

### 评论 #5 — gstoner (2018-02-21T20:12:42Z)

Preda, 
   Have you tried this headless Aka not running X11  via SSH 

---

### 评论 #6 — gstoner (2018-02-21T20:15:52Z)

Can you also test, beta 2 for us for 1.7.1  http://repo.radeon.com/misc/archive/beta/rocm-1.7.1-beta.2.tar.bz


---

### 评论 #7 — preda (2018-02-21T22:52:45Z)

@gstoner : some preliminary testing seems to indicate that I do __not__ reproduce this in headless (ROCm 1.7). I haven't tried 1.7.1 yet.

(I switched to headless from graphical with "systemctl isolate multi-user.target")


---

### 评论 #8 — gstoner (2018-02-21T23:05:22Z)

Ok this is in the base Linux driver then in graphics section of the code, I will talk to the Linux team 

---

### 评论 #9 — preda (2018-02-22T01:40:19Z)

I have one more trace for them. This I see just after reboot, without starting any OpenCL app, and everything seems to still works fine: X11, clinfo.

Ubuntu 17.10, booted kernel 4.13.0-32, after upgrade to kernel 4.13.0-36.

```
[   34.177103] ------------[ cut here ]------------
[   34.177170] WARNING: CPU: 7 PID: 982 at /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../display/dc/core/dc_surface.c:131 dc_plane_state_release+0x63/0x70 [amdgpu]
[   34.177171] Modules linked in: intel_rapl snd_hda_codec_hdmi x86_pkg_temp_thermal intel_powerclamp coretemp snd_hda_codec_realtek snd_hda_codec_generic kvm irqbypass crct10dif_pclmul crc32_pclmul ghash_clmulni_intel cryptd snd_hda_intel intel_cstate snd_hda_codec snd_hda_core intel_rapl_perf snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi snd_seq input_leds snd_seq_device snd_timer snd lpc_ich soundcore shpchp ioatdma acpi_power_meter mac_hid parport_pc ppdev lp parport ip_tables x_tables autofs4 amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdttm(OE) amdkcl(OE) igb hid_generic drm_kms_helper dca syscopyarea i2c_algo_bit sysfillrect sysimgblt usbhid fb_sys_fops ptp mxm_wmi drm hid ahci pps_core libahci wmi
[   34.177203] CPU: 7 PID: 982 Comm: gnome-shell Tainted: G           OE   4.13.0-32-generic #35-Ubuntu
[   34.177204] Hardware name: Supermicro X10DAi/X10DAI, BIOS 2.0 02/02/2016
[   34.177205] task: ffff9d6538ef5d00 task.stack: ffffbf1a085c8000
[   34.177243] RIP: 0010:dc_plane_state_release+0x63/0x70 [amdgpu]
[   34.177243] RSP: 0018:ffffbf1a085cbb88 EFLAGS: 00010246
[   34.177245] RAX: 0000000000000000 RBX: ffff9d7535a45000 RCX: 0000000000000c6a
[   34.177245] RDX: 000000000000000c RSI: ffff9d653811fa00 RDI: ffff9d753a8b4e00
[   34.177246] RBP: ffffbf1a085cbba0 R08: 0000000000025d60 R09: ffffffffc04c4372
[   34.177247] R10: ffffea9700d8ee80 R11: 0000000080050000 R12: 0000000000000000
[   34.177247] R13: ffff9d753b879000 R14: 0000000000000000 R15: 0000000000000006
[   34.177249] FS:  00007f57d39deac0(0000) GS:ffff9d653ffc0000(0000) knlGS:0000000000000000
[   34.177249] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   34.177250] CR2: 00007f575d3e1000 CR3: 0000002034e14005 CR4: 00000000001606e0
[   34.177251] Call Trace:
[   34.177292]  ? dm_drm_plane_destroy_state+0x23/0x40 [amdgpu]
[   34.177309]  drm_atomic_state_default_clear+0x18b/0x220 [drm]
[   34.177347]  dm_atomic_state_clear+0x2b/0x30 [amdgpu]
[   34.177356]  drm_atomic_state_clear+0x1f/0x30 [drm]
[   34.177364]  __drm_atomic_state_free+0x18/0x60 [drm]
[   34.177374]  drm_atomic_helper_legacy_gamma_set+0xf1/0x170 [drm_kms_helper]
[   34.177383]  drm_mode_gamma_set_ioctl+0x17d/0x1e0 [drm]
[   34.177390]  ? drm_mode_crtc_set_gamma_size+0xb0/0xb0 [drm]
[   34.177397]  drm_ioctl_kernel+0x5d/0xb0 [drm]
[   34.177404]  drm_ioctl+0x31b/0x3d0 [drm]
[   34.177410]  ? drm_mode_crtc_set_gamma_size+0xb0/0xb0 [drm]
[   34.177415]  ? futex_wake+0x8f/0x180
[   34.177438]  amdgpu_drm_ioctl+0x4f/0x90 [amdgpu]
[   34.177441]  do_vfs_ioctl+0xa5/0x610
[   34.177444]  ? __sys_recvmsg+0x51/0x90
[   34.177446]  ? __sys_recvmsg+0x80/0x90
[   34.177447]  SyS_ioctl+0x79/0x90
[   34.177451]  entry_SYSCALL_64_fastpath+0x33/0xa3
[   34.177452] RIP: 0033:0x7f57d0ac1ef7
[   34.177452] RSP: 002b:00007fff5f2281b8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[   34.177454] RAX: ffffffffffffffda RBX: 00005622c2c62060 RCX: 00007f57d0ac1ef7
[   34.177454] RDX: 00007fff5f2281f0 RSI: 00000000c02064a5 RDI: 0000000000000008
[   34.177455] RBP: 00007fff5f2281f0 R08: 00005622c2a40cb0 R09: 00005622c2a3f830
[   34.177456] R10: 0000000000000089 R11: 0000000000000246 R12: 00000000c02064a5
[   34.177456] R13: 0000000000000008 R14: 00005622c2e6b860 R15: 00005622c48fa360
[   34.177457] Code: e4 fe ff ff 48 8b bb 28 01 00 00 48 85 ff 74 10 e8 83 ff ff ff 48 c7 83 28 01 00 00 00 00 00 00 48 89 df e8 20 06 49 d9 5b 5d c3 <0f> ff eb a8 66 0f 1f 84 00 00 00 00 00 0f 1f 44 00 00 55 ba 03 
[   34.177480] ---[ end trace 4ceaf4ecfd5d17c4 ]---
```


---

### 评论 #10 — gstoner (2018-03-08T16:43:29Z)

Ok we have workaround for this on 1.7.1  It in the instruction, you need to shut of Page Retry in the GRUB. 

---
