# amdgpu-pro 19.20 kernel 5.1.15 clinfo gentoo dkms

> **Issue #831**
> **状态**: closed
> **创建时间**: 2019-07-01T06:30:45Z
> **更新时间**: 2023-01-23T05:39:53Z
> **关闭时间**: 2023-01-23T05:39:53Z
> **作者**: perestoronin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/831

## 描述

amdgpu-pro 19.20 kernel 5.1.15 clinfo gentoo dkms :

clinfo after apply patches [1](https://lkml.org/lkml/2019/5/7/335)  [2](https://www.spinics.net/lists/amd-gfx/msg31745.html) run successful with exit code 0
```
# clinfo
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2841.17)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 7
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Radeon RX Vega
  Device Topology:				 PCI[ B#28, D#0, F#0 ]
  Max compute units:				 56
  Max work items dimensions:			 3
...
  Platform ID:					 0x7fd559b8d1b0
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2841.17 (PAL,HSAIL)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 AMD-APP (2841.17)
  Extensions:					 cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_khr_gl_depth_images cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_subgroups cl_khr_gl_event cl_khr_depth_images cl_khr_mipmap_image cl_khr_mipmap_image_writes 
```
but in  [dmesg](https://github.com/perestoronin/amdgpu-pro-dkms-patches/blob/master/dmesg.txt) remains errors after only first run clinfo:
```[   16.299993] [drm] Initialized amdgpu 3.31.0 20150101 for 0000:1c:00.0 on minor 6
[  112.868624] ------------[ cut here ]------------
[  112.868625] CPU update of VM recommended only for large BAR system
[  112.868656] WARNING: CPU: 0 PID: 3848 at /var/lib/dkms/amdgpu/19.20-812932/build/amd/amdgpu/amdgpu_vm.c:2721 amdgpu_vm_init+0x393/0x460 [amdgpu]
[  112.868656] Modules linked in: nls_cp1251 amdgpu(O) backlight amdttm(O) amd_sched(O) k10temp amdkcl(O) drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops drm efivarfs
[  112.868661] CPU: 0 PID: 3848 Comm: clinfo Tainted: G           O      5.1.15-gentoo #4
[  112.868661] Hardware name: System manufacturer System Product Name/ROG CROSSHAIR VI EXTREME, BIOS 7003 06/04/2019
[  112.868680] RIP: 0010:amdgpu_vm_init+0x393/0x460 [amdgpu]
[  112.868681] Code: ff 48 8b 43 50 48 8b 78 10 48 83 c7 50 e8 15 71 32 c3 e9 66 ff ff ff 48 c7 c7 d8 60 7b c0 c6 05 d5 64 2d 00 01 e8 87 8d b2 c2 <0f> 0b 41 80 bd 60 01 00 00 00 75 a5 e9 82 fd ff ff 4c 8d b3 e0 3f
[  112.868682] RSP: 0018:ffffae018365bb40 EFLAGS: 00010286
[  112.868683] RAX: 0000000000000000 RBX: ffff88de62250000 RCX: 0000000000000000
[  112.868683] RDX: 0000000000000007 RSI: 0000000000000082 RDI: 00000000ffffffff
[  112.868684] RBP: ffff88de9a1ad8b8 R08: 0000000000000001 R09: 0000000000000749
[  112.868684] R10: 0000000000000001 R11: 0000000000000000 R12: ffff88de62250000
[  112.868685] R13: ffff88de9a1ad800 R14: 0000000000000000 R15: 0000000000000000
[  112.868685] FS:  00007f863e46d740(0000) GS:ffff88de6c000000(0000) knlGS:0000000000000000
[  112.868686] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  112.868686] CR2: 00007f863777edc0 CR3: 00000008d735e000 CR4: 00000000003406f0
[  112.868687] Call Trace:
[  112.868707]  amdgpu_driver_open_kms+0x9a/0x200 [amdgpu]
[  112.868711]  drm_file_alloc+0x155/0x220 [drm]
[  112.868715]  drm_open+0xac/0x1f0 [drm]
[  112.868719]  drm_stub_open+0xaf/0xe0 [drm]
[  112.868722]  chrdev_open+0xa3/0x1b0
[  112.868723]  ? cdev_put.part.0+0x20/0x20
[  112.868725]  do_dentry_open+0x12c/0x370
[  112.868726]  path_openat+0x2f9/0x14c0
[  112.868729]  ? syscall_return_via_sysret+0x1f/0x7f
[  112.868730]  ? __switch_to_asm+0x35/0x70
[  112.868731]  ? __switch_to_asm+0x41/0x70
[  112.868732]  ? __switch_to_asm+0x35/0x70
[  112.868733]  ? __switch_to_asm+0x41/0x70
[  112.868733]  ? __switch_to_asm+0x35/0x70
[  112.868735]  ? _raw_spin_unlock_irq+0x13/0x30
[  112.868736]  do_filp_open+0x93/0x100
[  112.868738]  ? ptrace_do_notify+0xc4/0xf0
[  112.868740]  ? _raw_spin_unlock+0x12/0x30
[  112.868741]  do_sys_open+0x183/0x220
[  112.868743]  do_syscall_64+0x48/0x100
[  112.868744]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[  112.868746] RIP: 0033:0x7f863d73593b
[  112.868747] Code: 4e 89 f0 25 00 00 41 00 3d 00 00 41 00 74 40 8b 05 fa ca 20 00 85 c0 75 61 89 f2 b8 01 01 00 00 48 89 fe bf 9c ff ff ff 0f 05 <48> 3d 00 f0 ff ff 0f 87 99 00 00 00 48 8b 4c 24 28 64 48 33 0c 25
[  112.868747] RSP: 002b:00007fffb3cb0240 EFLAGS: 00000246 ORIG_RAX: 0000000000000101
[  112.868748] RAX: ffffffffffffffda RBX: 00007fffb3cb0658 RCX: 00007f863d73593b
[  112.868748] RDX: 0000000000000002 RSI: 0000000000c9b018 RDI: 00000000ffffff9c
[  112.868748] RBP: 0000000000c8f5e0 R08: 0000000000c9b018 R09: 0000000000c9b030
[  112.868749] R10: 0000000000000000 R11: 0000000000000246 R12: 00007fffb3cb05f0
[  112.868749] R13: 0000000000c9afe8 R14: 0000000000c9b018 R15: 00007fffb3cb03e0
[ 112.868750] ---[ end trace b4e1ed02e6a1437f ]---
```

[strace here](https://github.com/perestoronin/amdgpu-pro-dkms-patches/blob/master/log.txt)

Please help me to fix errors in dmesg after first run clinfo.

---

## 评论 (1 条)

### 评论 #1 — perestoronin (2019-07-05T05:56:30Z)

same error after upgrade to kernel 5.1.16 + amdgpu-pro 19.20

---
