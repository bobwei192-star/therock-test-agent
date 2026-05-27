# RIP: vega10_print_clock_levels

> **Issue #429**
> **状态**: closed
> **创建时间**: 2018-06-05T15:08:45Z
> **更新时间**: 2019-03-12T19:17:13Z
> **关闭时间**: 2019-03-12T19:17:13Z
> **作者**: rhlug
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/429

## 描述

4x vegas, ubuntu 16.04 (4.13.0-37-lowlatency),  rocm-dkms 1.8-118

```
# uname -a
Linux localhost 4.13.0-37-lowlatency #42~16.04.1-Ubuntu SMP PREEMPT Wed Mar 7 17:14:26 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

# dkms status
amdgpu, 1.8-118, 4.13.0-37-lowlatency, x86_64: installed

# lspci | grep VGA
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)
06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)
0a:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)

# clinfo | grep "Device Board"
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega
  Device Board Name (AMD)                         Radeon RX Vega

# cat /sys/class/drm/card0/device/*sclk
0: 852Mhz *
1: 991Mhz 
2: 1084Mhz 
3: 1138Mhz 
4: 1200Mhz 
5: 1401Mhz 
6: 1536Mhz 
7: 1630Mhz 
```

Any powerplay interaction makes kernel shit itself.   This is valid pp_table I'm running on 4.17rc2 with no issues.

```
# cat ppt/0 > /sys/class/drm/card0/device/pp_table 
# cat /sys/class/drm/card0/device/*sclk
Killed
```

dmesg
```

[   81.109731] amdgpu: [powerplay] Failed to register high thermal interrupt!
[   81.109732] amdgpu: [powerplay] amdgpu: powerplay initialization failed
[   84.191782] BUG: unable to handle kernel NULL pointer dereference at 0000000000000954
[   84.191938] IP: vega10_print_clock_levels+0x10e/0x240 [amdgpu]
[   84.192029] PGD 4801b8067 
[   84.192029] P4D 4801b8067 
[   84.192071] PUD 4801b9067 
[   84.192114] PMD 0 

[   84.192213] Oops: 0000 [#1] PREEMPT SMP NOPTI
[   84.192280] Modules linked in: intel_rapl x86_pkg_temp_thermal intel_powerclamp coretemp kvm irqbypass intel_cstate intel_rapl_perf hci_uart input_leds joydev btbcm serdev btqca btintel shpchp acpi_als bluetooth ecdh_generic kfifo_buf industrialio intel_lpss_acpi acpi_pad intel_lpss ib_iser rdma_cm iw_cm ib_cm ib_core iscsi_tcp libiscsi_tcp libiscsi scsi_transport_iscsi autofs4 btrfs xor raid6_pq multipath linear hid_microsoft usbhid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdchash(OE) amd_sched(OE) amdttm(OE) crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc amdkcl(OE) i2c_algo_bit aesni_intel drm_kms_helper e1000e syscopyarea aes_x86_64 sysfillrect sysimgblt ptp fb_sys_fops pps_core crypto_simd ahci glue_helper libahci drm cryptd video i2c_hid hid
[   84.193341] CPU: 3 PID: 1711 Comm: cat Tainted: G           OE   4.13.0-37-lowlatency #42~16.04.1-Ubuntu
[   84.193490] Hardware name: System manufacturer System Product Name/PRIME Z370-A, BIOS 0428 10/26/2017
[   84.193634] task: ffff9ed3047e8000 task.stack: ffffbc8242908000
[   84.193750] RIP: 0010:vega10_print_clock_levels+0x10e/0x240 [amdgpu]
[   84.193849] RSP: 0018:ffffbc824290bd48 EFLAGS: 00010297
[   84.193930] RAX: 0000000000000000 RBX: ffff9ed30c0a8000 RCX: ffffffffc09ba4e0
[   84.194041] RDX: ffff9ed30b0be000 RSI: 0000000000000000 RDI: ffff9ed30c0a8000
[   84.194152] RBP: ffffbc824290bd80 R08: ffff9ed30c0a90b0 R09: ffff9ed2fcd3a900
[   84.194264] R10: ffffffff865e5a25 R11: ffff9ed3047e8000 R12: ffff9ed30b0be000
[   84.194375] R13: 0000000000000000 R14: 0000000000000000 R15: ffff9ed300285a80
[   84.194486] FS:  00007fedb107c700(0000) GS:ffff9ed31ecc0000(0000) knlGS:0000000000000000
[   84.194613] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   84.194702] CR2: 0000000000000954 CR3: 000000048b054005 CR4: 00000000003606e0
[   84.194813] Call Trace:
[   84.194877]  pp_dpm_print_clock_levels+0x83/0xc0 [amdgpu]
[   84.194978]  amdgpu_get_pp_dpm_sclk+0x32/0x50 [amdgpu]
[   84.195060]  dev_attr_show+0x23/0x60
[   84.195116]  sysfs_kf_seq_show+0xab/0x130
[   84.195178]  kernfs_seq_show+0x27/0x30
[   84.195237]  seq_read+0xa7/0x470
[   84.195288]  kernfs_fop_read+0x111/0x190
[   84.195349]  ? security_file_permission+0xa1/0xc0
[   84.195423]  __vfs_read+0x1b/0x40
[   84.195473]  vfs_read+0x93/0x130
[   84.195524]  SyS_read+0x55/0xc0
[   84.195574]  entry_SYSCALL_64_fastpath+0x24/0xab
[   84.195645] RIP: 0033:0x7fedb0b98260
[   84.195701] RSP: 002b:00007ffda7401248 EFLAGS: 00000246 ORIG_RAX: 0000000000000000
[   84.195819] RAX: ffffffffffffffda RBX: 00007fedb0e65b20 RCX: 00007fedb0b98260
[   84.195931] RDX: 0000000000020000 RSI: 00007fedb0ec2000 RDI: 0000000000000003
[   84.196042] RBP: 0000000000021010 R08: ffffffffffffffff R09: 0000000000000000
[   84.199792] R10: 000000000000037b R11: 0000000000000246 R12: 0000000000022000
[   84.203487] R13: 00007fedb0e65b78 R14: 0000000000001000 R15: 0000000000020000
[   84.207117] Code: 48 c7 c6 77 23 a1 c0 4c 01 e7 41 83 c7 01 49 83 c6 01 e8 26 4e 42 c6 01 c3 41 0f b7 85 88 04 00 00 44 39 f8 7f 90 e9 3a ff ff ff <41> 80 bd 54 09 00 00 00 0f 85 2a ff ff ff be 23 00 00 00 e8 fa 
[   84.214868] RIP: vega10_print_clock_levels+0x10e/0x240 [amdgpu] RSP: ffffbc824290bd48
[   84.218891] CR2: 0000000000000954
[   84.222923] ---[ end trace c4bd549cb57fe5c6 ]---
```




---

## 评论 (3 条)

### 评论 #1 — gstoner (2018-06-05T16:41:41Z)

I just let the Linux team know about the issue with the 4.13 Linux kernel pplib/smu firmware.   I asked them to add this as a test to continuous integration testing. 

We are pushing this team on improving it testing across the board.   

---

### 评论 #2 — candiceflower (2018-07-10T11:32:27Z)

@rhlug could you provide ppt/0 that you used to me for having a try?

---

### 评论 #3 — jlgreathouse (2019-03-12T19:17:13Z)

Recent versions of ROCm allow custom PowerPlay table installation through the OverDrive mechanism. rocm-smi can help with this. Since we don't know what type of "valid pp_table" the original report was using, I'll assume this is fixed now.

---
