# ROCm on Centos 7.9 Kernel version 3.10.0-1160

> **Issue #1693**
> **状态**: closed
> **创建时间**: 2022-02-27T14:32:11Z
> **更新时间**: 2024-01-23T20:11:05Z
> **关闭时间**: 2024-01-23T20:11:04Z
> **作者**: orensg1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1693

## 描述

Hello @ROCmSupport, 
Any updates on support for Centos 7.9 running Kernel version 3.10.0-1160 (#1615).
According to the docs, RHEL 7.9 Kernel version 3.10.0-1160 is supported (https://rocmdocs.amd.com/en/latest/Current_Release_Notes/Current-Release-Notes.html#amd-rocm-release-notes-v5-0-1)
What is the recommended course of action for people running the latest kernel on Centos 7.9?
Do you have any documentation on dealing with this issue?
Thx

---

## 评论 (15 条)

### 评论 #1 — ROCmSupport (2022-02-28T10:36:27Z)

Hi @orensg1 
Thanks for reaching out.
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.0.1/page/Overview_of_ROCm_Installation_Methods.html --> still pointing CentOS 7.9.

docs.amd.com is the new weblink for ROCm documentation, recommend to follow the same.
Thank you.

---

### 评论 #2 — orensg1 (2022-02-28T15:18:07Z)

Thank you but according to the link you sent Kernel version 3.10.0-1160 is not supported.
What is the recommended course of action for people running the latest kernel on Centos 7.9?
Should we downgrade to an older ROCm version? Should we downgrade to an older kernel version? compile from source? any other ideas from someone with similar issues? 

---

### 评论 #3 — ROCmSupport (2022-03-03T10:45:48Z)

I have gone through the doc and its showing wrong version. Sorry for that.
I will make sure that its going to be updated asap. Thank you.

---

### 评论 #4 — orensg1 (2022-03-03T13:08:20Z)

Great! thank you.

---

### 评论 #5 — bertwesarg (2022-03-09T06:41:41Z)

@orensg1 do you experience any issues with kernel 3.10.0-1160?

we just installed ROCm 5.0.2 on CentOS 7.9 with this kernel and the machine does not boot anymore:

```
[   18.741573] [drm] amdgpu kernel modesetting enabled.
[   18.747510] [drm] amdgpu version: 5.13.11.21.50
[   18.752574] [drm] OS DRM version: 5.0.0
[   18.757394] amdkcl: acpi_put_table is not supported
[   18.762897] amdgpu: Ignoring ACPI CRAT on non-APU system
[   18.768843] amdgpu: Virtual CRAT table created for CPU
[   18.774844] amdgpu: Topology: Add CPU node
[   18.780607] amdgpu: PeerDirect support was initialized successfully
[   18.787882] amdgpu 0000:03:00.0: enabling device (0000 -> 0002)
[   18.788590] scsi 1:0:0:0: Direct-Access     ATA      INTEL SSDSC2KG96 0121 PQ: 0 ANSI: 5
[   18.803643] [drm] initializing kernel modesetting (VEGA20 0x1002:0x66A1 0x1002:0x0834 0x02).
[   18.812846] amdgpu 0000:03:00.0: Trusted Memory Zone (TMZ) feature not supported
[   18.813058] mlx5_ib: Mellanox Connect-IB Infiniband driver v4.9-2.2.4
[   18.827957] [drm] register mmio base: 0xF8200000
[   18.833194] [drm] register mmio size: 524288
[   18.838027] [drm] add ip block number 0 <soc15_common>
[   18.843741] [drm] add ip block number 1 <gmc_v9_0>
[   18.849159] [drm] add ip block number 2 <vega20_ih>
[   18.854619] [drm] add ip block number 3 <psp>
[   18.859536] [drm] add ip block number 4 <powerplay>
[   18.864963] [drm] add ip block number 5 <dm>
[   18.869764] [drm] add ip block number 6 <gfx_v9_0>
[   18.875095] [drm] add ip block number 7 <sdma_v4_0>
[   18.880547] [drm] add ip block number 8 <uvd_v7_0>
[   18.885843] [drm] add ip block number 9 <vce_v4_0>
[   18.897277] ata1.00: Enabling discard_zeroes_data
[   18.902351] random: crng init done
[   18.907140] sd 0:0:0:0: [sda] 1875385008 512-byte logical blocks: (960 GB/894 GiB)
[   18.915511] sd 0:0:0:0: [sda] 4096-byte physical blocks
[   18.921549] sd 0:0:0:0: [sda] Write Protect is off
[   18.927088] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[   18.934723] amdgpu 0000:03:00.0: Fetched VBIOS from ROM BAR
[   18.934725] amdgpu: ATOM BIOS: 113-D1631400-107
[   18.934798] [drm] UVD(0) is enabled in VM mode
[   18.934799] [drm] UVD(1) is enabled in VM mode
[   18.934799] [drm] UVD(0) ENC is enabled in VM mode
[   18.934800] [drm] UVD(1) ENC is enabled in VM mode
[   18.934801] [drm] VCE enabled in VM mode
[   18.935026] [drm] GPU posting now...
[   18.935723] amdgpu 0000:03:00.0: MEM ECC is active.
[   18.935723] amdgpu 0000:03:00.0: SRAM ECC is active.
[   18.935729] amdgpu 0000:03:00.0: RAS INFO: ras initialized successfully, hardware ability[7fff] ras_mask[7fff]
[   18.935735] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
[   18.935743] amdgpu 0000:03:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
[   18.935744] amdgpu 0000:03:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[   18.935745] amdgpu 0000:03:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF
[   18.935755] [drm] Detected VRAM RAM=16368M, BAR=16384M
[   18.935756] [drm] RAM width 4096bits HBM
[   18.935816] [drm] amdgpu: 16368M of VRAM memory ready
[   18.935818] [drm] amdgpu: 515705M of GTT memory ready.
[   18.935824] [drm] GART: num cpu pages 131072, num gpu pages 131072
[   18.936061] [drm] PCIE GART of 512M enabled.
[   18.936062] [drm] PTB located at 0x0000008000000000
[   18.936344] amdgpu 0000:03:00.0: PSP runtime database doesn't exist
[   18.936347] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu
[   18.938619] [drm] Found UVD firmware ENC: 1.2 DEC: .43 Family ID: 19
[   18.938639] [drm] PSP loading UVD firmware
[   18.939341] [drm] Found VCE firmware Version: 57.6 Binary ID: 4
[   18.939344] [drm] PSP loading VCE firmware
[   19.108579] [drm] reserve 0x400000 from 0x83fec00000 for PSP TMR
[   19.118924] ata1.00: Enabling discard_zeroes_data
[   19.125411]  sda: sda1 sda2 sda3
[   19.126113] ata2.00: Enabling discard_zeroes_data
[   19.126155] sd 1:0:0:0: [sdb] 1875385008 512-byte logical blocks: (960 GB/894 GiB)
[   19.126157] sd 1:0:0:0: [sdb] 4096-byte physical blocks
[   19.126244] sd 1:0:0:0: [sdb] Write Protect is off
[   19.126260] sd 1:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[   19.126540] ata2.00: Enabling discard_zeroes_data
[   19.127440]  sdb:
[   19.127588] ata2.00: Enabling discard_zeroes_data
[   19.127842] sd 1:0:0:0: [sdb] Attached SCSI removable disk
[   19.183622] ata1.00: Enabling discard_zeroes_data
[   19.189025] sd 0:0:0:0: [sda] Attached SCSI removable disk
[   19.191017] amdgpu 0000:03:00.0: HDCP: optional hdcp ta ucode is not available
[   19.191018] amdgpu 0000:03:00.0: DTM: optional dtm ta ucode is not available
[   19.191019] amdgpu 0000:03:00.0: RAP: optional rap ta ucode is not available
[   19.191020] amdgpu 0000:03:00.0: SECUREDISPLAY: securedisplay ta ucode is not available
[   19.194900] [drm] Display Core initialized with v3.2.164!
[   19.195014] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   19.195014] [drm] Driver supports precise vblank timestamp query.
[   19.196650] [drm] kiq ring mec 2 pipe 1 q 0
[   19.239494] [drm] UVD and UVD ENC initialized successfully.
[   19.439880] [drm] VCE initialized successfully.
[   19.454243] kfd kfd: Allocated 3969056 bytes on gart
[   19.461451] amdgpu: Virtual CRAT table created for GPU
[   19.467792] amdgpu: Topology: Add dGPU node [0x66a1:0x1002]
[   19.474165] kfd kfd: added device 1002:66a1
[   19.496993] amdgpu 0000:03:00.0: SE 4, SH per SE 1, CU per SH 16, active_cu_number 60
[   19.506219] amdgpu 0000:03:00.0: ring gfx uses VM inv eng 0 on hub 0
[   19.513342] amdgpu 0000:03:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[   19.521049] amdgpu 0000:03:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[   19.528739] amdgpu 0000:03:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[   19.536416] amdgpu 0000:03:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[   19.544070] amdgpu 0000:03:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[   19.551703] amdgpu 0000:03:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[   19.559331] amdgpu 0000:03:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[   19.566960] amdgpu 0000:03:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[   19.574690] amdgpu 0000:03:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
[   19.582317] amdgpu 0000:03:00.0: ring sdma0 uses VM inv eng 0 on hub 1
[   19.589500] amdgpu 0000:03:00.0: ring page0 uses VM inv eng 1 on hub 1
[   19.596673] amdgpu 0000:03:00.0: ring sdma1 uses VM inv eng 4 on hub 1
[   19.603837] amdgpu 0000:03:00.0: ring page1 uses VM inv eng 5 on hub 1
[   19.610982] amdgpu 0000:03:00.0: ring uvd_0 uses VM inv eng 6 on hub 1
[   19.618126] amdgpu 0000:03:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
[   19.625777] amdgpu 0000:03:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
[   19.633408] amdgpu 0000:03:00.0: ring uvd_1 uses VM inv eng 9 on hub 1
[   19.640518] amdgpu 0000:03:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1
[   19.648233] amdgpu 0000:03:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1
[   19.655931] amdgpu 0000:03:00.0: ring vce0 uses VM inv eng 12 on hub 1
[   19.663027] amdgpu 0000:03:00.0: ring vce1 uses VM inv eng 13 on hub 1
[   19.670107] amdgpu 0000:03:00.0: ring vce2 uses VM inv eng 14 on hub 1
[   19.954011] BUG: unable to handle kernel NULL pointer dereference at           (null)
[   19.962654] IP: [<ffffffff86da669b>] __list_add+0x1b/0xc0
[   19.968699] PGD 0
[   19.971320] Oops: 0000 [#1] SMP
[   19.975137] Modules linked in: sd_mod crc_t10dif crct10dif_generic mlx5_ib(OE) ib_uverbs(OE) amdgpu(OE+) ib_core(OE) crct10dif_pclmul crct10dif_common crc32c_intel mlx5_core(OE) amd_iommu_v2 amdttm(OE) mlxfw(OE) amd_sched(OE) vfio_mdev(OE) ast amdkcl(OE) vfio_iommu_type1 vfio drm_kms_helper ahci mdev(OE) syscopyarea devlink sysfillrect igb sysimgblt mlx_compat(OE) ttm libahci fb_sys_fops ptp drm libata pps_core dca i2c_algo_bit drm_panel_orientation_quirks nfit libnvdimm dm_mirror dm_region_hash dm_log dm_mod x86_adapt_driver(OE) x86_adapt_defs(POE)
[   20.027890] CPU: 48 PID: 1348 Comm: kworker/48:1 Tainted: P           OE  ------------   3.10.0-1160.45.1.el7.x86_64 #1
[   20.039332] Hardware name: GIGABYTE R282-Z93-00/MZ92-FS0-00, BIOS R25 10/11/2021
[   20.047394] Workqueue: events work_for_cpu_fn
[   20.052447] task: ffff98de091ee300 ti: ffff98ed663cc000 task.ti: ffff98ed663cc000
[   20.060613] RIP: 0010:[<ffffffff86da669b>]  [<ffffffff86da669b>] __list_add+0x1b/0xc0
[   20.069146] RSP: 0018:ffff98ed663cf918  EFLAGS: 00010246
[   20.075139] RAX: 00000000ffffffff RBX: ffff98ed663cf940 RCX: 0000000000000000
[   20.082963] RDX: ffff98ed62d27830 RSI: 0000000000000000 RDI: ffff98ed663cf940
[   20.090788] RBP: ffff98ed663cf930 R08: 0000000000000000 R09: 0000000000000000
[   20.098612] R10: ffff98ed6ea1f380 R11: ffffe9f94098f400 R12: ffff98ed62d27830
[   20.106435] R13: 0000000000000000 R14: 00000000ffffffff R15: ffff98ed62d27830
[   20.114258] FS:  0000000000000000(0000) GS:ffff98ed6ea00000(0000) knlGS:0000000000000000
[   20.123043] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   20.129489] CR2: 0000000000000000 CR3: 0000002322810000 CR4: 0000000000340fe0
[   20.137320] Call Trace:
[   20.140459]  [<ffffffff871881c6>] __mutex_lock_slowpath+0xa6/0x1d0
[   20.147333]  [<ffffffff871875bf>] mutex_lock+0x1f/0x2f
[   20.153297]  [<ffffffffc12e4870>] smu_get_ecc_info+0x20/0x60 [amdgpu]
[   20.160489]  [<ffffffffc1156692>] amdgpu_ras_query_error_status+0x292/0x5d0 [amdgpu]
[   20.168994]  [<ffffffffc1157495>] amdgpu_ras_query_error_count+0xf5/0x170 [amdgpu]
[   20.177343]  [<ffffffffc1158d6a>] amdgpu_ras_late_init+0x1ea/0x250 [amdgpu]
[   20.185090]  [<ffffffffc115e6b9>] amdgpu_umc_ras_late_init+0xc9/0x220 [amdgpu]
[   20.193095]  [<ffffffffc115e500>] ? amdgpu_umc_do_page_retirement.isra.2+0x260/0x260 [amdgpu]
[   20.202428]  [<ffffffffc1152a37>] amdgpu_gmc_ras_late_init+0x27/0x130 [amdgpu]
[   20.210473]  [<ffffffffc11a6259>] gmc_v9_0_late_init+0x79/0xd0 [amdgpu]
[   20.217909]  [<ffffffffc110f5a5>] amdgpu_device_ip_late_init+0x55/0x2d0 [amdgpu]
[   20.226085]  [<ffffffff871875b2>] ? mutex_lock+0x12/0x2f
[   20.232224]  [<ffffffffc1113335>] amdgpu_device_init+0x1255/0x1eb0 [amdgpu]
[   20.239991]  [<ffffffff86dcc1bf>] ? pci_read_config_word+0x3f/0x50
[   20.246987]  [<ffffffff86dd3c90>] ? do_pci_enable_device+0xe0/0x110
[   20.254117]  [<ffffffffc11150bd>] amdgpu_driver_load_kms+0x6d/0x480 [amdgpu]
[   20.262027]  [<ffffffffc110cc8f>] amdgpu_pci_probe+0x1af/0x310 [amdgpu]
[   20.269475]  [<ffffffff86dd726a>] local_pci_probe+0x4a/0xb0
[   20.275877]  [<ffffffff86abaa6a>] work_for_cpu_fn+0x1a/0x30
[   20.282279]  [<ffffffff86abde8f>] process_one_work+0x17f/0x440
[   20.288947]  [<ffffffff86abf0f8>] worker_thread+0x278/0x3c0
[   20.295357]  [<ffffffff86abee80>] ? manage_workers.isra.26+0x2a0/0x2a0
[   20.302739]  [<ffffffff86ac5e61>] kthread+0xd1/0xe0
[   20.308464]  [<ffffffff86ac5d90>] ? insert_kthread_work+0x40/0x40
[   20.315407]  [<ffffffff87195de4>] ret_from_fork_nospec_begin+0xe/0x21
[   20.322689]  [<ffffffff86ac5d90>] ? insert_kthread_work+0x40/0x40
[   20.329623] Code: ff ff ff 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 00 55 48 89 e5 41 55 49 89 f5 41 54 49 89 d4 53 4c 8b 42 08 48 89 fb 49 39 f0 75 2a <4d> 8b 45 00 4d 39 c4 75 68 4c 39 e3 74 3e 4c 39 eb 74 39 49 89
[   20.351350] RIP  [<ffffffff86da669b>] __list_add+0x1b/0xc0
[   20.357698]  RSP <ffff98ed663cf918>
[   20.361998] CR2: 0000000000000000
[   20.366095] ---[ end trace e508f89eb2dfd603 ]--- 
```

---

### 评论 #6 — alanina (2022-03-22T04:28:59Z)

This should be handled in ROCm 5.0.2 . Can you try to uninstall via amdgpu-uninstall and then try to install the 5.0.2 release? There was a quirk in the dkms version provided by RHEL7/CentOS7 that should be handled if you remove the amdgpu-dkms package before installing 5.0.2 (instead of just upgrading to 5.0.2)

---

### 评论 #7 — orensg1 (2022-03-25T01:44:31Z)

> @orensg1 do you experience any issues with kernel 3.10.0-1160?
> 
> we just installed ROCm 5.0.2 on CentOS 7.9 with this kernel and the machine does not boot anymore:
> 
> ```
> [   18.741573] [drm] amdgpu kernel modesetting enabled.
> [   18.747510] [drm] amdgpu version: 5.13.11.21.50
> [   18.752574] [drm] OS DRM version: 5.0.0
> [   18.757394] amdkcl: acpi_put_table is not supported
> [   18.762897] amdgpu: Ignoring ACPI CRAT on non-APU system
> [   18.768843] amdgpu: Virtual CRAT table created for CPU
> [   18.774844] amdgpu: Topology: Add CPU node
> [   18.780607] amdgpu: PeerDirect support was initialized successfully
> [   18.787882] amdgpu 0000:03:00.0: enabling device (0000 -> 0002)
> [   18.788590] scsi 1:0:0:0: Direct-Access     ATA      INTEL SSDSC2KG96 0121 PQ: 0 ANSI: 5
> [   18.803643] [drm] initializing kernel modesetting (VEGA20 0x1002:0x66A1 0x1002:0x0834 0x02).
> [   18.812846] amdgpu 0000:03:00.0: Trusted Memory Zone (TMZ) feature not supported
> [   18.813058] mlx5_ib: Mellanox Connect-IB Infiniband driver v4.9-2.2.4
> [   18.827957] [drm] register mmio base: 0xF8200000
> [   18.833194] [drm] register mmio size: 524288
> [   18.838027] [drm] add ip block number 0 <soc15_common>
> [   18.843741] [drm] add ip block number 1 <gmc_v9_0>
> [   18.849159] [drm] add ip block number 2 <vega20_ih>
> [   18.854619] [drm] add ip block number 3 <psp>
> [   18.859536] [drm] add ip block number 4 <powerplay>
> [   18.864963] [drm] add ip block number 5 <dm>
> [   18.869764] [drm] add ip block number 6 <gfx_v9_0>
> [   18.875095] [drm] add ip block number 7 <sdma_v4_0>
> [   18.880547] [drm] add ip block number 8 <uvd_v7_0>
> [   18.885843] [drm] add ip block number 9 <vce_v4_0>
> [   18.897277] ata1.00: Enabling discard_zeroes_data
> [   18.902351] random: crng init done
> [   18.907140] sd 0:0:0:0: [sda] 1875385008 512-byte logical blocks: (960 GB/894 GiB)
> [   18.915511] sd 0:0:0:0: [sda] 4096-byte physical blocks
> [   18.921549] sd 0:0:0:0: [sda] Write Protect is off
> [   18.927088] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
> [   18.934723] amdgpu 0000:03:00.0: Fetched VBIOS from ROM BAR
> [   18.934725] amdgpu: ATOM BIOS: 113-D1631400-107
> [   18.934798] [drm] UVD(0) is enabled in VM mode
> [   18.934799] [drm] UVD(1) is enabled in VM mode
> [   18.934799] [drm] UVD(0) ENC is enabled in VM mode
> [   18.934800] [drm] UVD(1) ENC is enabled in VM mode
> [   18.934801] [drm] VCE enabled in VM mode
> [   18.935026] [drm] GPU posting now...
> [   18.935723] amdgpu 0000:03:00.0: MEM ECC is active.
> [   18.935723] amdgpu 0000:03:00.0: SRAM ECC is active.
> [   18.935729] amdgpu 0000:03:00.0: RAS INFO: ras initialized successfully, hardware ability[7fff] ras_mask[7fff]
> [   18.935735] [drm] vm size is 262144 GB, 4 levels, block size is 9-bit, fragment size is 9-bit
> [   18.935743] amdgpu 0000:03:00.0: VRAM: 16368M 0x0000008000000000 - 0x00000083FEFFFFFF (16368M used)
> [   18.935744] amdgpu 0000:03:00.0: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
> [   18.935745] amdgpu 0000:03:00.0: AGP: 267894784M 0x0000008400000000 - 0x0000FFFFFFFFFFFF
> [   18.935755] [drm] Detected VRAM RAM=16368M, BAR=16384M
> [   18.935756] [drm] RAM width 4096bits HBM
> [   18.935816] [drm] amdgpu: 16368M of VRAM memory ready
> [   18.935818] [drm] amdgpu: 515705M of GTT memory ready.
> [   18.935824] [drm] GART: num cpu pages 131072, num gpu pages 131072
> [   18.936061] [drm] PCIE GART of 512M enabled.
> [   18.936062] [drm] PTB located at 0x0000008000000000
> [   18.936344] amdgpu 0000:03:00.0: PSP runtime database doesn't exist
> [   18.936347] amdgpu: [powerplay] hwmgr_sw_init smu backed is vega20_smu
> [   18.938619] [drm] Found UVD firmware ENC: 1.2 DEC: .43 Family ID: 19
> [   18.938639] [drm] PSP loading UVD firmware
> [   18.939341] [drm] Found VCE firmware Version: 57.6 Binary ID: 4
> [   18.939344] [drm] PSP loading VCE firmware
> [   19.108579] [drm] reserve 0x400000 from 0x83fec00000 for PSP TMR
> [   19.118924] ata1.00: Enabling discard_zeroes_data
> [   19.125411]  sda: sda1 sda2 sda3
> [   19.126113] ata2.00: Enabling discard_zeroes_data
> [   19.126155] sd 1:0:0:0: [sdb] 1875385008 512-byte logical blocks: (960 GB/894 GiB)
> [   19.126157] sd 1:0:0:0: [sdb] 4096-byte physical blocks
> [   19.126244] sd 1:0:0:0: [sdb] Write Protect is off
> [   19.126260] sd 1:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
> [   19.126540] ata2.00: Enabling discard_zeroes_data
> [   19.127440]  sdb:
> [   19.127588] ata2.00: Enabling discard_zeroes_data
> [   19.127842] sd 1:0:0:0: [sdb] Attached SCSI removable disk
> [   19.183622] ata1.00: Enabling discard_zeroes_data
> [   19.189025] sd 0:0:0:0: [sda] Attached SCSI removable disk
> [   19.191017] amdgpu 0000:03:00.0: HDCP: optional hdcp ta ucode is not available
> [   19.191018] amdgpu 0000:03:00.0: DTM: optional dtm ta ucode is not available
> [   19.191019] amdgpu 0000:03:00.0: RAP: optional rap ta ucode is not available
> [   19.191020] amdgpu 0000:03:00.0: SECUREDISPLAY: securedisplay ta ucode is not available
> [   19.194900] [drm] Display Core initialized with v3.2.164!
> [   19.195014] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
> [   19.195014] [drm] Driver supports precise vblank timestamp query.
> [   19.196650] [drm] kiq ring mec 2 pipe 1 q 0
> [   19.239494] [drm] UVD and UVD ENC initialized successfully.
> [   19.439880] [drm] VCE initialized successfully.
> [   19.454243] kfd kfd: Allocated 3969056 bytes on gart
> [   19.461451] amdgpu: Virtual CRAT table created for GPU
> [   19.467792] amdgpu: Topology: Add dGPU node [0x66a1:0x1002]
> [   19.474165] kfd kfd: added device 1002:66a1
> [   19.496993] amdgpu 0000:03:00.0: SE 4, SH per SE 1, CU per SH 16, active_cu_number 60
> [   19.506219] amdgpu 0000:03:00.0: ring gfx uses VM inv eng 0 on hub 0
> [   19.513342] amdgpu 0000:03:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
> [   19.521049] amdgpu 0000:03:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
> [   19.528739] amdgpu 0000:03:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
> [   19.536416] amdgpu 0000:03:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
> [   19.544070] amdgpu 0000:03:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
> [   19.551703] amdgpu 0000:03:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
> [   19.559331] amdgpu 0000:03:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
> [   19.566960] amdgpu 0000:03:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
> [   19.574690] amdgpu 0000:03:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
> [   19.582317] amdgpu 0000:03:00.0: ring sdma0 uses VM inv eng 0 on hub 1
> [   19.589500] amdgpu 0000:03:00.0: ring page0 uses VM inv eng 1 on hub 1
> [   19.596673] amdgpu 0000:03:00.0: ring sdma1 uses VM inv eng 4 on hub 1
> [   19.603837] amdgpu 0000:03:00.0: ring page1 uses VM inv eng 5 on hub 1
> [   19.610982] amdgpu 0000:03:00.0: ring uvd_0 uses VM inv eng 6 on hub 1
> [   19.618126] amdgpu 0000:03:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
> [   19.625777] amdgpu 0000:03:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
> [   19.633408] amdgpu 0000:03:00.0: ring uvd_1 uses VM inv eng 9 on hub 1
> [   19.640518] amdgpu 0000:03:00.0: ring uvd_enc_1.0 uses VM inv eng 10 on hub 1
> [   19.648233] amdgpu 0000:03:00.0: ring uvd_enc_1.1 uses VM inv eng 11 on hub 1
> [   19.655931] amdgpu 0000:03:00.0: ring vce0 uses VM inv eng 12 on hub 1
> [   19.663027] amdgpu 0000:03:00.0: ring vce1 uses VM inv eng 13 on hub 1
> [   19.670107] amdgpu 0000:03:00.0: ring vce2 uses VM inv eng 14 on hub 1
> [   19.954011] BUG: unable to handle kernel NULL pointer dereference at           (null)
> [   19.962654] IP: [<ffffffff86da669b>] __list_add+0x1b/0xc0
> [   19.968699] PGD 0
> [   19.971320] Oops: 0000 [#1] SMP
> [   19.975137] Modules linked in: sd_mod crc_t10dif crct10dif_generic mlx5_ib(OE) ib_uverbs(OE) amdgpu(OE+) ib_core(OE) crct10dif_pclmul crct10dif_common crc32c_intel mlx5_core(OE) amd_iommu_v2 amdttm(OE) mlxfw(OE) amd_sched(OE) vfio_mdev(OE) ast amdkcl(OE) vfio_iommu_type1 vfio drm_kms_helper ahci mdev(OE) syscopyarea devlink sysfillrect igb sysimgblt mlx_compat(OE) ttm libahci fb_sys_fops ptp drm libata pps_core dca i2c_algo_bit drm_panel_orientation_quirks nfit libnvdimm dm_mirror dm_region_hash dm_log dm_mod x86_adapt_driver(OE) x86_adapt_defs(POE)
> [   20.027890] CPU: 48 PID: 1348 Comm: kworker/48:1 Tainted: P           OE  ------------   3.10.0-1160.45.1.el7.x86_64 #1
> [   20.039332] Hardware name: GIGABYTE R282-Z93-00/MZ92-FS0-00, BIOS R25 10/11/2021
> [   20.047394] Workqueue: events work_for_cpu_fn
> [   20.052447] task: ffff98de091ee300 ti: ffff98ed663cc000 task.ti: ffff98ed663cc000
> [   20.060613] RIP: 0010:[<ffffffff86da669b>]  [<ffffffff86da669b>] __list_add+0x1b/0xc0
> [   20.069146] RSP: 0018:ffff98ed663cf918  EFLAGS: 00010246
> [   20.075139] RAX: 00000000ffffffff RBX: ffff98ed663cf940 RCX: 0000000000000000
> [   20.082963] RDX: ffff98ed62d27830 RSI: 0000000000000000 RDI: ffff98ed663cf940
> [   20.090788] RBP: ffff98ed663cf930 R08: 0000000000000000 R09: 0000000000000000
> [   20.098612] R10: ffff98ed6ea1f380 R11: ffffe9f94098f400 R12: ffff98ed62d27830
> [   20.106435] R13: 0000000000000000 R14: 00000000ffffffff R15: ffff98ed62d27830
> [   20.114258] FS:  0000000000000000(0000) GS:ffff98ed6ea00000(0000) knlGS:0000000000000000
> [   20.123043] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
> [   20.129489] CR2: 0000000000000000 CR3: 0000002322810000 CR4: 0000000000340fe0
> [   20.137320] Call Trace:
> [   20.140459]  [<ffffffff871881c6>] __mutex_lock_slowpath+0xa6/0x1d0
> [   20.147333]  [<ffffffff871875bf>] mutex_lock+0x1f/0x2f
> [   20.153297]  [<ffffffffc12e4870>] smu_get_ecc_info+0x20/0x60 [amdgpu]
> [   20.160489]  [<ffffffffc1156692>] amdgpu_ras_query_error_status+0x292/0x5d0 [amdgpu]
> [   20.168994]  [<ffffffffc1157495>] amdgpu_ras_query_error_count+0xf5/0x170 [amdgpu]
> [   20.177343]  [<ffffffffc1158d6a>] amdgpu_ras_late_init+0x1ea/0x250 [amdgpu]
> [   20.185090]  [<ffffffffc115e6b9>] amdgpu_umc_ras_late_init+0xc9/0x220 [amdgpu]
> [   20.193095]  [<ffffffffc115e500>] ? amdgpu_umc_do_page_retirement.isra.2+0x260/0x260 [amdgpu]
> [   20.202428]  [<ffffffffc1152a37>] amdgpu_gmc_ras_late_init+0x27/0x130 [amdgpu]
> [   20.210473]  [<ffffffffc11a6259>] gmc_v9_0_late_init+0x79/0xd0 [amdgpu]
> [   20.217909]  [<ffffffffc110f5a5>] amdgpu_device_ip_late_init+0x55/0x2d0 [amdgpu]
> [   20.226085]  [<ffffffff871875b2>] ? mutex_lock+0x12/0x2f
> [   20.232224]  [<ffffffffc1113335>] amdgpu_device_init+0x1255/0x1eb0 [amdgpu]
> [   20.239991]  [<ffffffff86dcc1bf>] ? pci_read_config_word+0x3f/0x50
> [   20.246987]  [<ffffffff86dd3c90>] ? do_pci_enable_device+0xe0/0x110
> [   20.254117]  [<ffffffffc11150bd>] amdgpu_driver_load_kms+0x6d/0x480 [amdgpu]
> [   20.262027]  [<ffffffffc110cc8f>] amdgpu_pci_probe+0x1af/0x310 [amdgpu]
> [   20.269475]  [<ffffffff86dd726a>] local_pci_probe+0x4a/0xb0
> [   20.275877]  [<ffffffff86abaa6a>] work_for_cpu_fn+0x1a/0x30
> [   20.282279]  [<ffffffff86abde8f>] process_one_work+0x17f/0x440
> [   20.288947]  [<ffffffff86abf0f8>] worker_thread+0x278/0x3c0
> [   20.295357]  [<ffffffff86abee80>] ? manage_workers.isra.26+0x2a0/0x2a0
> [   20.302739]  [<ffffffff86ac5e61>] kthread+0xd1/0xe0
> [   20.308464]  [<ffffffff86ac5d90>] ? insert_kthread_work+0x40/0x40
> [   20.315407]  [<ffffffff87195de4>] ret_from_fork_nospec_begin+0xe/0x21
> [   20.322689]  [<ffffffff86ac5d90>] ? insert_kthread_work+0x40/0x40
> [   20.329623] Code: ff ff ff 66 2e 0f 1f 84 00 00 00 00 00 0f 1f 00 55 48 89 e5 41 55 49 89 f5 41 54 49 89 d4 53 4c 8b 42 08 48 89 fb 49 39 f0 75 2a <4d> 8b 45 00 4d 39 c4 75 68 4c 39 e3 74 3e 4c 39 eb 74 39 49 89
> [   20.351350] RIP  [<ffffffff86da669b>] __list_add+0x1b/0xc0
> [   20.357698]  RSP <ffff98ed663cf918>
> [   20.361998] CR2: 0000000000000000
> [   20.366095] ---[ end trace e508f89eb2dfd603 ]--- 
> ```

Sorry, it took me some time to get back to this. 
I could not upgrade an old installation by removing and reinstalling the latest version. 
That machine was working with ROCm version 4.3 but I did not manage to upgrade to ROCm 5.0
I had the following firmware error: 
```
[    6.087582] [drm:psp_v11_0_prep_cmd_buf [amdgpu]] *ERROR* Unknown firmware type
[    6.087994] [drm:psp_hw_init [amdgpu]] *ERROR* PSP firmware loading failed
[    6.088156] [drm:amdgpu_device_fw_loading [amdgpu]] *ERROR* hw_init of IP block <psp> failed -22
[    6.088243] amdgpu 0000:1a:00.0: amdgpu_device_ip_init failed
[    6.088310] amdgpu 0000:1a:00.0: Fatal error during GPU init
```
The good news is that a couple of minutes ago I managed to install ROCm 5.0.2 on a fresh installation of Centos 7.9 with kernel version 3.10.0-1160.59.1.
So it is possible, but you might need to try a fresh install or figure out how to completely remove any trace of the old installation.


---

### 评论 #8 — orensg1 (2022-03-25T01:50:07Z)

 

@alanina `amdgpu-uninstall` did not solve my firmware error but a fresh install worked.

---

### 评论 #9 — alanina (2022-03-25T14:28:06Z)

@orensg1 good to see you found a solution. 🙂

---

### 评论 #10 — ROCmSupport (2022-03-28T07:16:20Z)

I am not sure anyone else is facing the similar issue still.
But I tried locally couple of times and not seen this problem with ROCm 5.0.2
Anyhow, I request you to wait for 5.1 which is going to be released very soon.
Thank you.

---

### 评论 #11 — alanina (2022-03-31T17:20:06Z)

ROCm 5.1 just got released today.

---

### 评论 #12 — bertwesarg (2022-04-05T10:34:20Z)

5.1.0 boots on CentOS 7.9 for me now.

---

### 评论 #13 — ROCmSupport (2022-04-11T08:56:20Z)

Hope we can close this ticket as 5.1 boots on CentOS 7.9 now.
@orensg1 , can you please confirm from your side.
Thank you.

---

### 评论 #14 — abhimeda (2024-01-23T19:53:47Z)

@orensg1 Hi, do you think we can close the ticket now?

---

### 评论 #15 — orensg1 (2024-01-23T20:11:04Z)

Yes @abhimeda, I forgot this ticket was still open. Thank you.

---
