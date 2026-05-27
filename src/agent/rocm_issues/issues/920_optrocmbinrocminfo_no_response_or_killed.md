# /opt/rocm/bin/rocminfo no response or killed

> **Issue #920**
> **状态**: closed
> **创建时间**: 2019-10-24T13:05:25Z
> **更新时间**: 2023-12-18T17:15:37Z
> **关闭时间**: 2023-12-18T17:15:37Z
> **作者**: jli113
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/920

## 描述

Ubuntu 18.04 using RX5700XT
/opt/rocm/bin/rocminfo no response or killed
/opt/rocm/opencl/bin/x86_64/clinfo no response or killed

---

## 评论 (10 条)

### 评论 #1 — PlutoniumHeart (2019-12-07T11:21:16Z)

If you are running Linux kernel 5.3, I think there's a bug inside amdgpu, that would crash the driver.

---

### 评论 #2 — giddygazebo (2019-12-07T15:39:56Z)

same problem with 4.15 kernel / ubuntu 16.04.6
```
uname -r
4.15.0-72-generic

Distributor ID: Ubuntu
Description:    Ubuntu 16.04.6 LTS
Release:        16.04
Codename:       xenial

/opt/rocm/bin/rocminfo
ROCk module is loaded
***** is member of video group
Killed
```

---

### 评论 #3 — FranzBl (2019-12-14T06:33:27Z)

![grafik](https://user-images.githubusercontent.com/44602645/70844590-ec0ae300-1e43-11ea-9745-bb2aeb8e57c4.png)
Same problem, see screenshot. First call to rocminfo is killed, subsequent are hanging.

---

### 评论 #4 — FranzBl (2019-12-14T12:34:20Z)

on which kernel rocm is indeed running? Everyone tells something another.

---

### 评论 #5 — tiberiusferreira (2019-12-21T11:02:13Z)

I'm having the same problem on a RX580: 
First tried with the 
```
sudo apt install rocm-dkms
```
Then with the upstream kernel:
```
sudo apt update	
sudo apt install rocm-dev	
echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' 
```
Same result
```
(base) gringos@gringos-ml:~$ uname -a
Linux gringos-ml 5.0.0-37-generic #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

(base) gringos@gringos-ml:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.3 LTS
Release:	18.04
Codename:	bionic
```

```
[   17.200222] [drm] Display Core initialized with v3.2.60!
[   17.249531] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   17.249532] [drm] Driver supports precise vblank timestamp query.
[   17.295665] [drm] UVD and UVD ENC initialized successfully.
[   17.405551] [drm] VCE initialized successfully.
[   17.406686] [drm] fb mappable at 0xE0A30000
[   17.406688] [drm] vram apper at 0xE0000000
[   17.406689] [drm] size 5242880
[   17.406690] [drm] fb depth is 24
[   17.406691] [drm]    pitch is 5120
[   17.406837] fbcon: amdgpudrmfb (fb0) is primary device
[   17.406906] Console: switching to colour frame buffer device 160x64
[   17.406924] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   17.427069] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:01:00.0 on minor 0
[   31.350091] RTL8211E Gigabit Ethernet r8169-300:00: attached PHY driver [RTL8211E Gigabit Ethernet] (mii_bus:phy_addr=r8169-300:00, irq=IGNORE)
[   31.542209] r8169 0000:03:00.0 enp3s0: Link is Down
[   34.473772] r8169 0000:03:00.0 enp3s0: Link is Up - 100Mbps/Full - flow control rx/tx
[   34.473787] IPv6: ADDRCONF(NETDEV_CHANGE): enp3s0: link becomes ready
[   45.260725] rfkill: input handler disabled
[  370.052040] BUG: unable to handle kernel NULL pointer dereference at 0000000000000204
[  370.052045] #PF error: [WRITE]
[  370.052047] PGD 80000001d52e2067 P4D 80000001d52e2067 PUD 20c5c5067 PMD 0
[  370.052053] Oops: 0002 [#1] SMP PTI
[  370.052058] CPU: 3 PID: 1806 Comm: clinfo Tainted: G           OE     5.0.0-37-generic #40~18.04.1-Ubuntu
[  370.052060] Hardware name: Gigabyte Technology Co., Ltd. To be filled by O.E.M./B75M-D3H, BIOS F15 10/23/2013
[  370.052190] RIP: 0010:kfd_create_process+0x44b/0x530 [amdgpu]
[  370.052193] Code: d9 c4 f5 48 83 3d 04 db 2b 00 00 0f 84 48 fc ff ff 48 8b 3d e7 d7 da f6 ba 40 00 00 00 be c0 80 60 00 e8 68 ee c4 f5 48 85 c0 <48> 89 83 10 02 00 00 0f 84 b8 00 00 00 48 8b 53 60 48 c7 c1 41 09
[  370.052195] RSP: 0018:ffff9c424128fbb0 EFLAGS: 00010282
[  370.052198] RAX: ffff8cd4ced85d40 RBX: fffffffffffffff4 RCX: 0000000000000000
[  370.052200] RDX: 0000000000000000 RSI: 0000000000000000 RDI: ffff8cd4ced85d80
[  370.052202] RBP: ffff9c424128fbe8 R08: ffff8cd4d5ba70a0 R09: ffff8cd4d5403800
[  370.052204] R10: ffffdcf2882dd900 R11: 666f72500064666b R12: ffff8cd4ce8f7c00
[  370.052206] R13: ffff8cd4a72a8000 R14: ffff8cd4ce8f7c00 R15: ffff8cd4cb767000
[  370.052208] FS:  00007faeb1513740(0000) GS:ffff8cd4d5b80000(0000) knlGS:0000000000000000
[  370.052211] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  370.052213] CR2: 0000000000000204 CR3: 00000001d5294002 CR4: 00000000000606e0
[  370.052215] Call Trace:
[  370.052223]  ? cdev_purge+0x70/0x70
[  370.052330]  kfd_open+0x3b/0xd0 [amdgpu]
[  370.052334]  chrdev_open+0xc4/0x1b0
[  370.052337]  ? cdev_put.part.2+0x20/0x20
[  370.052341]  do_dentry_open+0x1f8/0x3a0
[  370.052344]  vfs_open+0x2f/0x40
[  370.052347]  path_openat+0x2e8/0x1700
[  370.052351]  ? unlock_page_memcg+0x12/0x20
[  370.052355]  ? page_add_file_rmap+0x18f/0x230
[  370.052360]  ? alloc_set_pte+0x220/0x5f0
[  370.052365]  ? filemap_map_pages+0x18f/0x380
[  370.052368]  do_filp_open+0x9b/0x110
[  370.052371]  ? __check_object_size+0xdb/0x1b0
[  370.052376]  ? strncpy_from_user+0x54/0x190
[  370.052380]  ? __alloc_fd+0x46/0x170
[  370.052384]  do_sys_open+0x1bb/0x2d0
[  370.052386]  ? do_sys_open+0x1bb/0x2d0
[  370.052390]  ? __do_page_fault+0x2b2/0x4d0
[  370.052395]  ? _cond_resched+0x19/0x40
[  370.052398]  __x64_sys_openat+0x20/0x30
[  370.052402]  do_syscall_64+0x5a/0x120
[  370.052406]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[  370.052409] RIP: 0033:0x7faeb0745d2b
[  370.052411] Code: 4e 89 f0 25 00 00 41 00 3d 00 00 41 00 74 40 8b 05 ea c6 20 00 85 c0 75 61 89 f2 b8 01 01 00 00 48 89 fe bf 9c ff ff ff 0f 05 <48> 3d 00 f0 ff ff 0f 87 99 00 00 00 48 8b 4c 24 28 64 48 33 0c 25
[  370.052413] RSP: 002b:00007ffe694866c0 EFLAGS: 00000246 ORIG_RAX: 0000000000000101
[  370.052416] RAX: ffffffffffffffda RBX: 00007faeafd12ee0 RCX: 00007faeb0745d2b
[  370.052418] RDX: 0000000000080002 RSI: 00007faeafb002e8 RDI: 00000000ffffff9c
[  370.052420] RBP: 00007faeafd12f88 R08: 000000000000ff00 R09: 000000000000444e
[  370.052422] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
[  370.052424] R13: 00007ffe69486a28 R14: 00007faeb00b5fe0 R15: 0000000001f34120
[  370.052426] Modules linked in: intel_rapl x86_pkg_temp_thermal snd_hda_codec_realtek intel_powerclamp snd_hda_codec_generic coretemp kvm_intel ledtrig_audio amdgpu(OE) kvm snd_hda_codec_hdmi irqbypass snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep amd_iommu_v2 amdttm(OE) crct10dif_pclmul amd_sched(OE) amdkcl(OE) snd_pcm drm_kms_helper snd_seq_midi crc32_pclmul ghash_clmulni_intel snd_seq_midi_event drm i2c_algo_bit snd_rawmidi fb_sys_fops input_leds aesni_intel snd_seq aes_x86_64 syscopyarea crypto_simd snd_seq_device cryptd sysfillrect sysimgblt snd_timer glue_helper snd soundcore intel_cstate intel_rapl_perf mei_me lpc_ich mei mac_hid sch_fq_codel parport_pc ppdev lp parport ip_tables x_tables autofs4 hid_steam hid_generic pata_acpi usbhid r8169 hid realtek video
[  370.052464] CR2: 0000000000000204
[  370.052467] ---[ end trace b7912757a48ab4a3 ]---
[  370.052575] RIP: 0010:kfd_create_process+0x44b/0x530 [amdgpu]
[  370.052578] Code: d9 c4 f5 48 83 3d 04 db 2b 00 00 0f 84 48 fc ff ff 48 8b 3d e7 d7 da f6 ba 40 00 00 00 be c0 80 60 00 e8 68 ee c4 f5 48 85 c0 <48> 89 83 10 02 00 00 0f 84 b8 00 00 00 48 8b 53 60 48 c7 c1 41 09
[  370.052580] RSP: 0018:ffff9c424128fbb0 EFLAGS: 00010282
[  370.052582] RAX: ffff8cd4ced85d40 RBX: fffffffffffffff4 RCX: 0000000000000000
[  370.052584] RDX: 0000000000000000 RSI: 0000000000000000 RDI: ffff8cd4ced85d80
[  370.052586] RBP: ffff9c424128fbe8 R08: ffff8cd4d5ba70a0 R09: ffff8cd4d5403800
[  370.052587] R10: ffffdcf2882dd900 R11: 666f72500064666b R12: ffff8cd4ce8f7c00
[  370.052589] R13: ffff8cd4a72a8000 R14: ffff8cd4ce8f7c00 R15: ffff8cd4cb767000
[  370.052592] FS:  00007faeb1513740(0000) GS:ffff8cd4d5b80000(0000) knlGS:0000000000000000
[  370.052594] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  370.052596] CR2: 0000000000000204 CR3: 00000001d5294002 CR4: 00000000000606e0
```

---

### 评论 #6 — faizghifari (2019-12-27T14:38:56Z)

I'm having the same issue here, with RX480

In my case, the rocm-smi is running well. But the rocminfo and clinfo stuck with no response. Also always Killed at the first runtime after turning the PC on, just like the @giddygazebo case.

I already tried to run a simple app using the tensorflow-rocm, but it stuck when fitting the model (no response, or maybe killed)

```
faizghifari@faiz-pc:~$ uname -a
Linux faiz-pc 5.0.0-37-generic #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
faizghifari@faiz-pc:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.3 LTS
Release:	18.04
Codename:	bionic
```

---

### 评论 #7 — hardymanm (2020-01-24T00:38:52Z)

The same issue  with Ubuntu 18.04 kernel 4.15.
Hardware Specs:
Dell Inspiron I5 : Processors Intel® Core™ i7-4510U CPU @ 2.00GHz × 4 
Graphics AMD Radeon R7 M265 and Intel® HD Graphics 4400 (HSW GT2) 

/opt/rocm/bin/rocminfo no response or killed
/opt/rocm/opencl/bin/x86_64/clinfo no response or killed

---

### 评论 #8 — raelschiffler (2023-04-07T21:36:02Z)

Did anyone solve this? It's 2023 and I'm trying to resuscitate my RX-480 with same setup as @faizghifari  

---

### 评论 #9 — nartmada (2023-12-12T23:48:51Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #10 — nartmada (2023-12-18T17:15:37Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
