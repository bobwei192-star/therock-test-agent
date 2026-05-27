# Ubuntu 17.04 with X11-Unity- ROCM amdgpu: kernel hang in dc_surface_retain

> **Issue #190**
> **状态**: closed
> **创建时间**: 2017-08-30T23:38:18Z
> **更新时间**: 2018-06-03T14:48:51Z
> **关闭时间**: 2018-06-03T14:48:51Z
> **作者**: superchkn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/190

## 描述

I'm getting kernel lockups with ROCM 1.6.148 under Ubuntu 17.04. I'm not sure exactly what is triggering this under Unity, however here is the log:

>kernel: [ 2319.432288] ------------[ cut here ]------------
kernel: [ 2319.432337] WARNING: CPU: 12 PID: 2147 at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/kernel/drivers/gpu/drm/amd/amdgpu/../display/dc/core/dc_surface.c:158 dc_surface_retain+0x34/0x50 [amdgpu]
kernel: [ 2319.432337] Modules linked in: ufs qnx4 hfs minix ntfs msdos jfs xfs libcrc32c nls_utf8 hfsplus binfmt_misc nls_iso8859_1 eeepc_wmi asus_wmi sparse_keymap video snd_hda_codec_hdmi snd_hda_intel snd_hda_codec usblp snd_hda_core ccp edac_mce_amd btrfs edac_core xor joydev input_leds snd_usb_audio snd_usbmidi_lib snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi snd_seq uvcvideo kvm_amd snd_seq_device videobuf2_vmalloc kvm videobuf2_memops videobuf2_v4l2 videobuf2_core snd_timer irqbypass videodev raid6_pq snd media soundcore crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc aesni_intel aes_x86_64 crypto_simd glue_helper shpchp cryptd serio_raw i2c_piix4 8250_dw i2c_designware_platform mac_hid i2c_designware_core parport_pc ppdev lp parport ip_tables x_tables autofs4 hid_microsoft hid_generic
kernel: [ 2319.432375]  usbhid hid uas usb_storage amdkfd amd_iommu_v2 mxm_wmi amdgpu ttm drm_kms_helper syscopyarea psmouse sysfillrect sysimgblt fb_sys_fops igb drm dca ptp pps_core ahci i2c_algo_bit libahci gpio_amdpt wmi gpio_generic
kernel: [ 2319.432388] CPU: 12 PID: 2147 Comm: InputThread Not tainted 4.11.0-kfd-compute-rocm-rel-1.6-148 #1
kernel: [ 2319.432389] Hardware name: System manufacturer System Product Name/CROSSHAIR VI HERO, BIOS 1403 06/22/2017
kernel: [ 2319.432390] Call Trace:
kernel: [ 2319.432395]  dump_stack+0x63/0x90
kernel: [ 2319.432398]  __warn+0xcb/0xf0
kernel: [ 2319.432400]  warn_slowpath_null+0x1d/0x20
kernel: [ 2319.432437]  dc_surface_retain+0x34/0x50 [amdgpu]
kernel: [ 2319.432473]  resource_attach_surfaces_to_context+0xb1/0x3e0 [amdgpu]
kernel: [ 2319.432476]  ? __slab_free+0x9e/0x2e0
kernel: [ 2319.432511]  ? resource_is_stream_unchanged+0x49/0x80 [amdgpu]
kernel: [ 2319.432546]  resource_validate_attach_surfaces+0xad/0x160 [amdgpu]
kernel: [ 2319.432582]  dce100_validate_with_context+0x15e/0x1c0 [amdgpu]
kernel: [ 2319.432617]  dc_get_validate_context+0x75/0xe0 [amdgpu]
kernel: [ 2319.432657]  amdgpu_dm_atomic_check+0x48e/0xb80 [amdgpu]
kernel: [ 2319.432670]  drm_atomic_check_only+0x468/0x590 [drm]
kernel: [ 2319.432681]  drm_atomic_commit+0x18/0x50 [drm]
kernel: [ 2319.432686]  drm_atomic_helper_update_plane+0xec/0x140 [drm_kms_helper]
kernel: [ 2319.432695]  __setplane_internal+0x1a9/0x270 [drm]
kernel: [ 2319.432697]  ? __wake_up+0x44/0x50
kernel: [ 2319.432700]  ? ep_read_events_proc+0xc0/0xc0
kernel: [ 2319.432709]  drm_mode_cursor_universal+0xf7/0x1c0 [drm]
kernel: [ 2319.432719]  drm_mode_cursor_common+0x85/0x170 [drm]
kernel: [ 2319.432727]  drm_mode_cursor_ioctl+0x41/0x50 [drm]
kernel: [ 2319.432736]  drm_ioctl+0x1fc/0x450 [drm]
kernel: [ 2319.432744]  ? drm_mode_setplane+0x190/0x190 [drm]
kernel: [ 2319.432771]  amdgpu_drm_ioctl+0x4c/0x80 [amdgpu]
kernel: [ 2319.432773]  do_vfs_ioctl+0x92/0x5a0
kernel: [ 2319.432775]  ? rw_verify_area+0x4e/0xb0
kernel: [ 2319.432777]  SyS_ioctl+0x79/0x90
kernel: [ 2319.432780]  entry_SYSCALL_64_fastpath+0x1e/0xad
kernel: [ 2319.432781] RIP: 0033:0x7f26ffc6e587
kernel: [ 2319.432782] RSP: 002b:00007f26eba96338 EFLAGS: 00003246 ORIG_RAX: 0000000000000010
kernel: [ 2319.432784] RAX: ffffffffffffffda RBX: 0000556cd9345770 RCX: 00007f26ffc6e587
kernel: [ 2319.432784] RDX: 00007f26eba96370 RSI: 00000000c01c64a3 RDI: 000000000000000d
kernel: [ 2319.432785] RBP: 0000556cd8c3b6d0 R08: 0000556cd8d4aab0 R09: 0000000000000a00
kernel: [ 2319.432786] R10: 0000556cd91c0540 R11: 0000000000003246 R12: 00007f26eba965dc
kernel: [ 2319.432786] R13: 0000556cd95869e0 R14: 0000556cd7a59a20 R15: 0000000000000000
kernel: [ 2319.432788] ---[ end trace d5a4ba263591de79 ]---

The card in question is a Sapphire Nitro R9 Fury, which I don't have issues with under the stock Ubuntu kernel nor under Gentoo with the 4.12 series of kernels that I've been running for a while. Well, at least not this particular issue, I'm also getting BUG logs regarding hung CPUs under this kernel I let the screen sleep and am running ethminer. However, that's another issue.

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-09-02T12:12:25Z)

If you run this under 16.04.2 which the kernel was optimized for do you see the issue?    Also, which motherboard and processor are you using? 

---

### 评论 #2 — gstoner (2017-09-02T12:16:48Z)

Searching the Web this looks like a known issue in Linux Kernel 4.11,   We ask the Linux kernel team to address this bug. 

https://lists.freedesktop.org/archives/amd-gfx/2017-June/010036.html
https://bugs.freedesktop.org/show_bug.cgi?id=101714

---

### 评论 #3 — superchkn (2017-09-03T15:53:52Z)

For what I'm doing with OpenCL I can limp along like this until it's fixed, I just wanted to make sure that it had been captured as an issue. I'll have to brush up on my search techniques as I was not able to find this reported anywhere. Thanks!

---

### 评论 #4 — gstoner (2017-09-03T16:07:43Z)

My old bosses used to call me gregle since I would bend search engines to find the data quickly.

---

### 评论 #5 — superchkn (2017-09-03T16:16:59Z)

A name well earned! I'm usually pretty good with searches compared to my peers at work.

---
