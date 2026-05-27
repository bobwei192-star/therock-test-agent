# Darkable segfaults on specific images when using latest driver version (3354.7)

> **Issue #1654**
> **状态**: closed
> **创建时间**: 2022-01-03T19:20:22Z
> **更新时间**: 2025-11-20T01:57:55Z
> **关闭时间**: 2022-01-25T18:39:05Z
> **作者**: piratenpanda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1654

## 描述

I am using latest opencl-amd on arch which is providing driver version 3354.7

[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/7803629/clinfo.txt)
A typical darktable start without crashes, I also don't see anything in the opencl output when it crashes
[dt-opencl.txt](https://github.com/RadeonOpenCompute/ROCm/files/7803656/dt-opencl.txt)

Bug is described here also with sample images to download:
https://github.com/darktable-org/darktable/issues/10778

The stacktrace of the bug:
https://www.toptal.com/developers/hastebin/elagijalow.yaml

And some more stacktraces in:
https://github.com/darktable-org/darktable/issues/10082

When I disable opencl the bug does not appear so I am quite sure it's a driver issues. Others with NVidia cards can't reproduce this either.

Is there anything else I can provide?

---

## 评论 (5 条)

### 评论 #1 — piratenpanda (2022-01-07T13:46:47Z)

Following the advice in the darktable bugtracker I ran **journalctl -b0 -k**:

```
kernel: WARNING: CPU: 2 PID: 21104 at drivers/gpu/drm/ttm/ttm_bo.c:409 ttm_bo_release+0x2da/0x300 [ttm]
kernel: Modules linked in: snd_seq_dummy snd_seq uas usb_storage nfsv3 nfs_acl rpcsec_gss_krb5 auth_rpcgss nfsv4 dns_resolver nfs lockd grace fscache netfs uv>
kernel:  x_tables hid_logitech_hidpp hid_logitech_dj usbhid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel aesni_intel crypto_simd cryptd xhci_pci xhci_pci>
kernel: CPU: 2 PID: 21104 Comm: kworker/2:1 Not tainted 5.15.13-arch1-1 #1 51d00698bfdb139ecff7a73f09034830de5a04f4
kernel: Hardware name: Gigabyte Technology Co., Ltd. H270M-DS3H/H270M-DS3H-CF, BIOS F8d 03/09/2018
kernel: Workqueue: kfd_process_wq kfd_process_wq_release [amdgpu]
kernel: RIP: 0010:ttm_bo_release+0x2da/0x300 [ttm]
kernel: Code: e8 9b 6c 7d f6 e9 c1 fd ff ff 49 8b 7e 98 b9 28 23 00 00 31 d2 be 01 00 00 00 e8 f1 8f 7d f6 49 8b 46 e8 eb 9e 48 89 e8 eb 99 <0f> 0b e9 47 fd f>
kernel: RSP: 0018:ffffbe6f02a03cc0 EFLAGS: 00010202
kernel: RAX: 0000000000000001 RBX: ffffbe6f02a03d08 RCX: 0000000000000000
kernel: RDX: 0000000000000001 RSI: 0000000000000000 RDI: ffff9675dc2329b8
kernel: RBP: ffff967392e05270 R08: ffff9675dc2329b8 R09: 0000000000000000
kernel: R10: 0000000000000000 R11: 0000000000000000 R12: ffff9674ba95da30
kernel: R13: ffff9675dc232858 R14: ffff9675dc2329b8 R15: dead000000000100
kernel: FS:  0000000000000000(0000) GS:ffff967a8ed00000(0000) knlGS:0000000000000000
kernel: CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
kernel: CR2: 000055b83804c4e8 CR3: 00000005d2e10006 CR4: 00000000003706e0
kernel: DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
kernel: DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
kernel: Call Trace:
kernel:  <TASK>
kernel:  amdgpu_bo_unref+0x1a/0x30 [amdgpu 431cbfe15e135bf6dbdd5236fab7a1247d7dce5b]
kernel:  amdgpu_gem_object_free+0x30/0x50 [amdgpu 431cbfe15e135bf6dbdd5236fab7a1247d7dce5b]
kernel:  amdgpu_amdkfd_gpuvm_free_memory_of_gpu+0x364/0x3d0 [amdgpu 431cbfe15e135bf6dbdd5236fab7a1247d7dce5b]
kernel:  kfd_process_device_free_bos+0x9f/0xf0 [amdgpu 431cbfe15e135bf6dbdd5236fab7a1247d7dce5b]
kernel:  kfd_process_wq_release+0x20d/0x2e0 [amdgpu 431cbfe15e135bf6dbdd5236fab7a1247d7dce5b]
kernel:  process_one_work+0x1e8/0x3c0
kernel:  worker_thread+0x50/0x3c0
kernel:  ? process_one_work+0x3c0/0x3c0
kernel:  kthread+0x132/0x160
kernel:  ? set_kthread_struct+0x50/0x50
kernel:  ret_from_fork+0x22/0x30
kernel:  </TASK>
kernel: ---[ end trace 502f44bede71cd07 ]---
```

---

### 评论 #2 — piratenpanda (2022-01-07T14:00:57Z)

@ROCmSupport anything else you need?

---

### 评论 #3 — illwieckz (2022-01-25T18:36:38Z)

@piratenpanda the [README says](https://github.com/RadeonOpenCompute/ROCm/blob/95493f625cadb3457cedb454e4ebd0df7b991443/README.md?plain=1#L194) that _Graphics use cases are not supported in this release._

Also the [README says](https://github.com/RadeonOpenCompute/ROCm/blob/95493f625cadb3457cedb454e4ebd0df7b991443/README.md?plain=1#L688) Polaris are not supported.

You'll may have some luck by trying Orca or PAL, I have a script to install them, but that's for Ubuntu:

https://gitlab.com/illwieckz/i-love-compute#scripts

The state of OpenCL for AMD on Linux is now worse than it was back in the days of fglrx.

See also : https://rebatir.fr/post/2022-01-25-OpenCL_on_Linux_state_of_AMD_drivers_is_now_worse_than_it_was_back_in_the_days_of_fglrx/

---

### 评论 #4 — piratenpanda (2022-01-25T18:39:05Z)

Bug has been fixed by limiting lower values to 0 in darktable.

---

### 评论 #5 — ROCmSupport (2022-01-28T11:59:54Z)

ROCm does not support gfx8 devices anymore and also graphical scenarios are well tested only on amdgpu/linux-pro.
ROCm is mainly and mostly for compute.
Thanks for the closure @piratenpanda 
Thank you.

---
