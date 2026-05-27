# GPU memory not freed

> **Issue #785**
> **状态**: closed
> **创建时间**: 2019-05-04T13:46:59Z
> **更新时间**: 2019-06-07T12:14:27Z
> **关闭时间**: 2019-06-07T12:14:27Z
> **作者**: twuebi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/785

## 描述

From time to time, I experience an issue similar to #751 when I quit a tensorflow launch using `ctrl + c`. The program quits but the GPU memory is never freed. It's quite annoying since the only way of regaining the lost GPU memory is a reboot.

`dmesg` shows this (the full output is attached):

```
[ 8810.209808] BUG: unable to handle kernel paging request at ffffd15b300f95e0
[ 8810.209818] IP: kfree+0x53/0x180
[ 8810.209819] PGD 0 P4D 0 
[ 8810.209823] Oops: 0000 [#1] SMP PTI
[ 8810.209825] Modules linked in: ipt_MASQUERADE nf_nat_masquerade_ipv4 nf_conntrack_netlink nfnetlink xfrm_user xfrm_algo iptable_nat nf_conntrack_ipv4 nf_defrag_ipv4 nf_nat_ipv4 xt_addrtype iptable_filter xt_conntrack nf_nat nf_conntrack libcrc32c br_netfilter bridge stp llc overlay aufs intel_rapl x86_pkg_temp_thermal amdgpu(OE) intel_powerclamp coretemp snd_hda_codec_realtek kvm_intel amdttm(OE) snd_hda_codec_hdmi snd_hda_codec_generic input_leds amd_sched(OE) kvm joydev irqbypass crct10dif_pclmul snd_hda_intel snd_hda_codec snd_hda_core snd_seq_midi snd_seq_midi_event crc32_pclmul amdkcl(OE) snd_hwdep amd_iommu_v2 ghash_clmulni_intel pcbc drm_kms_helper aesni_intel drm aes_x86_64 crypto_simd snd_rawmidi glue_helper cryptd snd_pcm i2c_algo_bit fb_sys_fops syscopyarea sysfillrect sysimgblt intel_cstate
[ 8810.209860]  intel_rapl_perf snd_seq snd_seq_device snd_timer snd soundcore mac_hid mei_me mei acpi_pad intel_pch_thermal shpchp binfmt_misc sch_fq_codel parport_pc ppdev lp parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq dm_mirror dm_region_hash dm_log hid_generic usbhid hid mxm_wmi e1000e ptp ahci pps_core libahci wmi video
[ 8810.209883] CPU: 2 PID: 5382 Comm: kworker/2:2 Tainted: G           OE    4.15.0-47-generic #50-Ubuntu
[ 8810.209885] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./Z170M Pro4S, BIOS P2.80 05/17/2016
[ 8810.209946] Workqueue: kfd_process_wq kfd_process_wq_release [amdgpu]
[ 8810.209951] RIP: 0010:kfree+0x53/0x180
[ 8810.209952] RSP: 0018:ffffb0a0045bfc38 EFLAGS: 00010286
[ 8810.209954] RAX: ffff937863add300 RBX: ffffb0a003e57000 RCX: 00000000001dda00
[ 8810.209956] RDX: 0000000000020000 RSI: 0000000010000000 RDI: 00006c8b80000000
[ 8810.209957] RBP: ffffb0a0045bfc50 R08: 0000000000378200 R09: ffff9375136ae458
[ 8810.209958] R10: ffffd15b300f95c0 R11: 0000000000000b00 R12: 0000000020000000
[ 8810.209960] R13: ffffffffc0c2ed85 R14: ffff93784cf440a8 R15: ffffb0a003e570a0
[ 8810.209962] FS:  0000000000000000(0000) GS:ffff937876500000(0000) knlGS:0000000000000000
[ 8810.209963] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 8810.209965] CR2: ffffd15b300f95e0 CR3: 000000045200a001 CR4: 00000000003606e0
[ 8810.209966] Call Trace:
[ 8810.210010]  amdgpu_vram_mgr_del+0xd5/0xf0 [amdgpu]
[ 8810.210016]  ttm_bo_cleanup_memtype_use+0x68/0x70 [amdttm]
[ 8810.210020]  ttm_bo_release+0x1d1/0x280 [amdttm]
[ 8810.210022]  ? kmem_cache_free+0x1b3/0x1e0
[ 8810.210024]  ? kmem_cache_free+0x1b3/0x1e0
[ 8810.210027]  amdttm_bo_put+0x1e/0x20 [amdttm]
[ 8810.210057]  amdgpu_bo_unref+0x1e/0x30 [amdgpu]
[ 8810.210102]  amdgpu_amdkfd_gpuvm_free_memory_of_gpu+0x17f/0x240 [amdgpu]
[ 8810.210145]  kfd_process_device_free_bos+0xa0/0xe0 [amdgpu]
[ 8810.210185]  kfd_process_wq_release+0x34/0xa0 [amdgpu]
[ 8810.210188]  process_one_work+0x1de/0x410
[ 8810.210190]  worker_thread+0x32/0x410
[ 8810.210193]  kthread+0x121/0x140
[ 8810.210195]  ? process_one_work+0x410/0x410
[ 8810.210198]  ? kthread_create_worker_on_cpu+0x70/0x70
[ 8810.210202]  ret_from_fork+0x35/0x40
[ 8810.210204] Code: 00 80 49 01 da 0f 82 39 01 00 00 48 c7 c7 00 00 00 80 48 2b 3d 27 38 20 01 49 01 fa 49 c1 ea 0c 49 c1 e2 06 4c 03 15 05 38 20 01 <49> 8b 42 20 48 8d 50 ff a8 01 4c 0f 45 d2 49 8b 52 20 48 8d 42 
[ 8810.210233] RIP: kfree+0x53/0x180 RSP: ffffb0a0045bfc38
[ 8810.210235] CR2: ffffd15b300f95e0
[ 8810.210237] ---[ end trace a34feda881f8be94 ]---
```

[non-freeing-dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/3144416/dmesg.txt)
[non-freeing-amdgpu_vram_mm.txt](https://github.com/RadeonOpenCompute/ROCm/files/3144421/amdgpu_vram_mm.txt)


Info:

TensorFlow version: 1.13
Python version: 3.6.5
GPU model and memory: Radeon VII, 16GB
Kernel:  4.15.0-47-generic with rock-dkms
ROCm/MIOpen version: 2.3

[rocm-dev.txt](https://github.com/RadeonOpenCompute/ROCm/files/3144418/rocm-dev.txt)
[rocm_info.txt](https://github.com/RadeonOpenCompute/ROCm/files/3144419/rocm_info.txt)


---

## 评论 (14 条)

### 评论 #1 — twuebi (2019-05-05T15:52:32Z)

Encountered another instance within the `rocm/tensorflow:rocm2.3-tf1.13-python3` docker container after an out-of-memory error occurred. 

[docker_oom_dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/3145729/docker_oom_dmesg.txt)


---

### 评论 #2 — twuebi (2019-05-09T13:44:27Z)

The problem still occurs after upgrading to rocm2.4. Is there any way of dealing with this issue without rebooting? It is quite annoying to reboot multiple times a day to regain lost memory.

[dmesg_rocm2-4.txt](https://github.com/RadeonOpenCompute/ROCm/files/3162396/dmesg_rocm2-4.txt)


---

### 评论 #3 — kentrussell (2019-05-09T20:06:22Z)

Have you tried just resetting the GPU via GPU reset? (The smi has a --gpureset flag, and you can also do it manually by reading the amdgpu_gpu_recover sysfs file) It might be a workaround until the root of the issue is actually resolved.

---

### 评论 #4 — twuebi (2019-05-09T20:13:52Z)

Yes, does not work. As far as I understand it restores the state of the GPU memory after performing the reset.

---

### 评论 #5 — kentrussell (2019-05-09T20:28:45Z)

Yeah, I wasn't holding my breath on that one. I was hoping that it might have given it the kick that it needed, but I didn't think it was very likely. Just had my fingers crossed

---

### 评论 #6 — kentrussell (2019-05-10T13:07:30Z)

@fxkamd , thoughts?

---

### 评论 #7 — fxkamd (2019-05-10T15:03:04Z)

The backtrace points to a kfree called from the VRAM manager. I see that the DKMS branch changes some kvfree calls to kfree unconditionally, while the corresponding allocation calls are kmalloc or kvmalloc conditionally depending on the kernel version. This would lead to problems on newer kernel versions (4.15 or newer) that allocate the memory with kvmalloc and then try to free it with kfree. This should be fixed on the DKMS branch.

I'm surprised this only manifests as a problem in a special case (tensor flow dying).

---

### 评论 #8 — twuebi (2019-05-10T15:05:21Z)

> I'm surprised this only manifests as a problem in a special case (tensor flow dying).

It does not, it also happens via `SIGINT` quite frequently. (unless that's also a case of tf dying)

---

### 评论 #9 — twuebi (2019-05-10T18:20:13Z)

Replaced the two calls in `amdgpu_vram_mgr_new` and `amdgpu_vram_mgr_del`, did not experience any issues since.

---

### 评论 #10 — fxkamd (2019-05-10T21:02:20Z)

Thanks for confirming that. I'm working on getting a fix into ROCm 2.5.

---

### 评论 #11 — robzor92 (2019-05-29T10:12:58Z)

I have also noticed the same problem, would be great to have it in 2.5 if possible. Thanks!

---

### 评论 #12 — twuebi (2019-05-29T19:43:06Z)

This assumes that you are on Kernel >= 4.15. 

Note: Fixing it yourself means altering the source files of your driver and rebuilding it. If you're comfortable with doing that, here is how I fixed it: 

Replace the two calls to `kfree` in `amdgpu_vram_mgr_new` and `amdgpu_vram_mgr_del` in `/usr/src/amdgpu-<YOUR_VERSION>/amd/amdgpu/amdgpu_vram_mgr.c`  with `kvfree` (lines 392 and 431 in this [file](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.4.x/drivers/gpu/drm/amd/amdgpu/amdgpu_vram_mgr.c)). 

After editing do:

```
sudo dkms remove amdgpu/<YOUR_VERSION> --all
sudo dkms add amdgpu/<YOUR_VERSION>
sudo dkms build amdgpu/<YOUR_VERSION>
sudo dkms install amdgpu/<YOUR_VERSION>
sudo reboot
```

this will remove the old version, add your custom driver, build it and then install it. Afterwards you shouldn't experience this issue anymore. 

---

### 评论 #13 — kentrussell (2019-06-03T13:56:53Z)

We made the 2.5 cutoff for this, so once 2.5 is released, this issue will be covered.

---

### 评论 #14 — kentrussell (2019-06-07T12:14:27Z)

The fix is in 2.5

---
