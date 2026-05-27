# ROCm can't run on Intel NUC 8 NUC8i3CYSM

> **Issue #939**
> **状态**: closed
> **创建时间**: 2019-11-19T07:52:24Z
> **更新时间**: 2023-12-18T16:12:30Z
> **关闭时间**: 2023-12-18T16:12:30Z
> **作者**: luguang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/939

## 描述

Hi guys,

I tried to install ROCm on Intel NUC 8 NUC8i3CYSM recently. After the installation, I couldn't run rocminfo or clinfo.

Hardware spec:
https://www.intel.com/content/www/us/en/products/boards-kits/nuc/mini-pcs/nuc8i3cysm.html

Intel Core i3-8121U (Gen 8)
RAM: 8GB
PCIe 3
GPU: Radeon RX540 with 2GB RAM
Disk: 128GB SSD

OS: Ubuntu 18.04.3 x64
ROCm: newest version 2.9

It's weird because lspci says it's RX550.
$ lspci | grep VGA
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X] (rev c3)

Before I could install ROCm on NUC, I failed once due to Intel Security check. It failed at last step to install. Then I rebooted to BIOS and disable Intel security technology, and booted to Ubuntu and apt autoremove rocm-dkms and apt install rocm-dkms again. I am not sure whether this is clean enough.

Then I followed the guide at https://rocm.github.io/ROCmInstall.html#installing-from-amd-rocm-repositories, till:

$ /opt/rocm/bin/rocminfo 
ROCk module is loaded
username is member of video group
Killed

And at the console I found some error messages

![1623148944](https://user-images.githubusercontent.com/4979674/69127020-6c0f8880-0ae4-11ea-9c4a-0267310a551d.jpg)

$ /opt/rocm/opencl/bin/x86_64/clinfo 

It hangs there always, then I killed it.

![1769260135](https://user-images.githubusercontent.com/4979674/69127026-6e71e280-0ae4-11ea-9c7f-d6c6dab0c9c8.jpg)

At last I could not restart the box normally because clinfo hangs there. 

What would be the problem?

Thanks,

Gavin

---

## 评论 (4 条)

### 评论 #1 — luguang (2019-11-19T09:17:00Z)

$ ./rocm_smi.py 
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
0    34.0c  3.179W  214Mhz  300Mhz  18.82%  auto  25.0W     1%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================

Part of syslog after rocminfo

Nov 19 15:59:33 ecl-amd kernel: [  309.879633] BUG: unable to handle kernel NULL pointer dereference at 00000000000001fc
Nov 19 15:59:33 ecl-amd kernel: [  309.879769] IP: kfd_create_process+0x466/0x540 [amdgpu]
Nov 19 15:59:33 ecl-amd kernel: [  309.879808] PGD 800000024d7f6067 P4D 800000024d7f6067 PUD 254ff0067 PMD 0 
Nov 19 15:59:33 ecl-amd kernel: [  309.879863] Oops: 0002 [#1] SMP PTI
Nov 19 15:59:33 ecl-amd kernel: [  309.879889] Modules linked in: ccm nls_iso8859_1 arc4 8250_dw snd_soc_skl snd_soc_skl_ipc snd_hda_ext_core iwlmvm s
nd_soc_sst_dsp snd_soc_sst_ipc mac80211 snd_soc_acpi rtsx_pci_ms memstick snd_soc_core snd_hda_codec_realtek snd_hda_codec_hdmi snd_hda_codec_generic 
snd_compress ac97_bus snd_pcm_dmaengine intel_rapl x86_pkg_temp_thermal idma64 intel_powerclamp virt_dma coretemp kvm_intel kvm irqbypass snd_hda_inte
l snd_hda_codec snd_hda_core snd_hwdep btusb btrtl btbcm intel_wmi_thunderbolt wmi_bmof btintel snd_pcm iwlwifi snd_timer snd bluetooth soundcore cfg8
0211 ecdh_generic shpchp intel_pch_thermal mei_me mei intel_lpss_pci intel_lpss mac_hid acpi_pad sch_fq_codel ib_iser rdma_cm iw_cm ib_cm ib_core iscs
i_tcp libiscsi_tcp libiscsi scsi_transport_iscsi ip_tables x_tables autofs4 btrfs zstd_compress
Nov 19 15:59:33 ecl-amd kernel: [  309.880481]  raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1
 raid0 multipath linear amdgpu(OE) amdttm(OE) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc amdkcl(OE) amd_sched(OE) i2c_algo_bit amd_iommu_v
2 drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops aesni_intel e1000e aes_x86_64 crypto_simd glue_helper rtsx_pci_sdmmc cryptd drm ptp pps
_core ahci rtsx_pci libahci sdhci_pci sdhci wmi video
Nov 19 15:59:33 ecl-amd kernel: [  309.880969] CPU: 0 PID: 1345 Comm: rocminfo Tainted: G           OE    4.15.0-55-generic #60-Ubuntu
Nov 19 15:59:33 ecl-amd kernel: [  309.880992] Hardware name: Intel(R) Client Systems NUC8i3CYS/NUC8CYB, BIOS CYCNLi35.86A.0036.2018.0801.1506 08/01/2
018
Nov 19 15:59:33 ecl-amd kernel: [  309.881075] RIP: 0010:kfd_create_process+0x466/0x540 [amdgpu]
Nov 19 15:59:33 ecl-amd kernel: [  309.881092] RSP: 0018:ffffacac01a6fb90 EFLAGS: 00010286
Nov 19 15:59:33 ecl-amd kernel: [  309.881107] RAX: ffffa0ab4d6bdc00 RBX: fffffffffffffff4 RCX: 0000000000000000
Nov 19 15:59:33 ecl-amd kernel: [  309.881126] RDX: 0000000000000040 RSI: 0000000000000000 RDI: ffffa0ab57003800
Nov 19 15:59:33 ecl-amd kernel: [  309.881145] RBP: ffffacac01a6fbc8 R08: ffffa0ab5fc270a0 R09: ffffa0ab4d6bdc00
Nov 19 15:59:33 ecl-amd kernel: [  309.881164] R10: ffffecf78935a000 R11: 666f72500064666b R12: ffffa0ab4e72e100
Nov 19 15:59:33 ecl-amd kernel: [  309.881183] R13: ffffa0ab54890000 R14: ffffa0ab4e72e100 R15: ffffa0ab4d681c00
Nov 19 15:59:33 ecl-amd kernel: [  309.881203] FS:  00007f130c4d5780(0000) GS:ffffa0ab5fc00000(0000) knlGS:0000000000000000
Nov 19 15:59:33 ecl-amd kernel: [  309.881224] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 19 15:59:33 ecl-amd kernel: [  309.881240] CR2: 00000000000001fc CR3: 000000024d2a8002 CR4: 0000000000760ef0
Nov 19 15:59:33 ecl-amd kernel: [  309.881259] PKRU: 55555554
Nov 19 15:59:33 ecl-amd kernel: [  309.881267] Call Trace:
Nov 19 15:59:33 ecl-amd kernel: [  309.881280]  ? cdev_purge+0x70/0x70
Nov 19 15:59:33 ecl-amd kernel: [  309.881329]  kfd_open+0x3b/0xd0 [amdgpu]
Nov 19 15:59:33 ecl-amd kernel: [  309.881343]  chrdev_open+0xc4/0x1b0
Nov 19 15:59:33 ecl-amd kernel: [  309.881355]  do_dentry_open+0x1c2/0x310
Nov 19 15:59:33 ecl-amd kernel: [  309.881367]  ? __inode_permission+0x5b/0x160
Nov 19 15:59:33 ecl-amd kernel: [  309.881380]  ? cdev_put.part.3+0x20/0x20
Nov 19 15:59:33 ecl-amd kernel: [  309.881393]  vfs_open+0x4f/0x80
Nov 19 15:59:33 ecl-amd kernel: [  309.881403]  path_openat+0x66e/0x1770
Nov 19 15:59:33 ecl-amd kernel: [  309.881416]  ? filemap_map_pages+0x36c/0x390
Nov 19 15:59:33 ecl-amd kernel: [  309.881430]  do_filp_open+0x9b/0x110
Nov 19 15:59:33 ecl-amd kernel: [  309.881442]  ? __check_object_size+0xaf/0x1b0
Nov 19 15:59:33 ecl-amd kernel: [  309.881456]  ? __alloc_fd+0x46/0x170
Nov 19 15:59:33 ecl-amd kernel: [  309.881467]  do_sys_open+0x1bb/0x2c0
Nov 19 15:59:33 ecl-amd kernel: [  309.881479]  ? do_sys_open+0x1bb/0x2c0
Nov 19 15:59:33 ecl-amd kernel: [  309.881491]  SyS_openat+0x14/0x20
Nov 19 15:59:33 ecl-amd kernel: [  309.881503]  do_syscall_64+0x73/0x130
Nov 19 15:59:33 ecl-amd kernel: [  309.881517]  entry_SYSCALL_64_after_hwframe+0x3d/0xa2
Nov 19 15:59:33 ecl-amd kernel: [  309.881531] RIP: 0033:0x7f130b99dc8e
Nov 19 15:59:33 ecl-amd kernel: [  309.881542] RSP: 002b:00007ffc516b41a0 EFLAGS: 00000246 ORIG_RAX: 0000000000000101
Nov 19 15:59:33 ecl-amd kernel: [  309.881562] RAX: ffffffffffffffda RBX: 00007f130b675900 RCX: 00007f130b99dc8e
Nov 19 15:59:33 ecl-amd kernel: [  309.881581] RDX: 0000000000080002 RSI: 00007f130b466bc8 RDI: 00000000ffffff9c
Nov 19 15:59:33 ecl-amd kernel: [  309.881622] RBP: 00007f130b6759a8 R08: 00007f130b675900 R09: 0000000000004d44
Nov 19 15:59:33 ecl-amd kernel: [  309.881641] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
Nov 19 15:59:33 ecl-amd kernel: [  309.881659] R13: 00007ffc516b4400 R14: 0000000000000000 R15: 0000000000000000
Nov 19 15:59:33 ecl-amd kernel: [  309.881677] Code: 91 7d 8a fb 48 83 3d 59 a5 22 00 00 0f 84 2d fc ff ff 48 8b 3d 5c 0f 0c fd ba 40 00 00 00 be c0 8
0 40 01 e8 3d 90 8a fb 48 85 c0 <48> 89 83 08 02 00 00 0f 84 b8 00 00 00 48 8b 53 60 48 c7 c1 7d 
Nov 19 15:59:33 ecl-amd kernel: [  309.881782] RIP: kfd_create_process+0x466/0x540 [amdgpu] RSP: ffffacac01a6fb90
Nov 19 15:59:33 ecl-amd kernel: [  309.881801] CR2: 00000000000001fc
Nov 19 15:59:33 ecl-amd kernel: [  309.881811] ---[ end trace 41383f71c50d817e ]---


---

### 评论 #2 — luguang (2019-11-20T02:51:23Z)

$ dmesg | grep kfd
[   13.155802] kfd kfd: skipped device 1002:699f, PCI rejects atomics

It turns out that NUC may not support atomics. I will ask at NUC community.


---

### 评论 #3 — nartmada (2023-12-13T20:12:19Z)

Hi @luguang , please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.


---

### 评论 #4 — nartmada (2023-12-18T16:12:30Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
