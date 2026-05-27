# 'unable to handle kernel paging request' on Vega 64

> **Issue #751**
> **状态**: closed
> **创建时间**: 2019-03-24T12:54:10Z
> **更新时间**: 2023-12-18T18:52:36Z
> **关闭时间**: 2023-12-18T18:52:35Z
> **作者**: mbonaker
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/751

## 描述

# The error message (copy-pasted from `dmesg`)

```
[ 2002.448852] Evicting PASID 32785 queues
[ 2002.453748] Restoring PASID 32785 queues
[ ... skipping about 100 of those repeating lines which don't look all to suspicious to me ... ]
[ 5852.651196] Evicting PASID 32786 queues
[ 5852.657266] Restoring PASID 32786 queues
[ 5867.977833] BUG: unable to handle kernel paging request at ffffefd40d1b2b60
[ 5867.977843] IP: kfree+0x53/0x180
[ 5867.977845] PGD 0 P4D 0 
[ 5867.977848] Oops: 0000 [#1] SMP NOPTI
[ 5867.977850] Modules linked in: bnep ipt_MASQUERADE nf_nat_masquerade_ipv4 nf_conntrack_netlink nfnetlink xfrm_user xfrm_algo iptable_nat nf_conntrack_ipv4 nf_defrag_ipv4 nf_nat_ipv4 xt_addrtype xt_conntrack nf_nat nf_conntrack libcrc32c br_netfilter bridge stp llc aufs ip6table_filter ip6_tables iptable_filter pci_stub vboxpci(OE) vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) bluetooth ecdh_generic binfmt_misc edac_mce_amd kvm_amd kvm snd_hda_codec_realtek snd_hda_codec_generic irqbypass snd_hda_codec_hdmi crct10dif_pclmul crc32_pclmul snd_hda_intel snd_usb_audio ghash_clmulni_intel input_leds snd_hda_codec joydev snd_usbmidi_lib snd_hda_core snd_hwdep pcbc snd_pcm xpad ff_memless aesni_intel snd_seq_midi aes_x86_64 snd_seq_midi_event crypto_simd glue_helper cryptd snd_rawmidi snd_seq snd_seq_device
[ 5867.977882]  snd_timer snd shpchp soundcore fam15h_power k10temp sch_fq_codel mac_hid cuse lm92 nct6775 hwmon_vid parport_pc ppdev lp parport ip_tables x_tables autofs4 uas usb_storage amdgpu(OE) amdchash(OE) amdttm(OE) amd_sched(OE) hid_generic amdkcl(OE) i2c_algo_bit mxm_wmi amd_iommu_v2 drm_kms_helper syscopyarea sysfillrect usbhid sysimgblt r8169 fb_sys_fops hid pata_acpi mii ahci drm nvme pata_atiixp i2c_piix4 nvme_core libahci wmi
[ 5867.977906] CPU: 5 PID: 13658 Comm: python3 Tainted: G           OE    4.15.0-46-generic #49-Ubuntu
[ 5867.977907] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./970A-G/3.1, BIOS P1.20 01/12/2016
[ 5867.977909] RIP: 0010:kfree+0x53/0x180
[ 5867.977911] RSP: 0018:ffffaba30695b8e0 EFLAGS: 00010282
[ 5867.977913] RAX: ffff8ef4e4b7d930 RBX: ffffaba306cad000 RCX: 0000000000003840
[ 5867.977914] RDX: 00000000ffffffe4 RSI: ffff8ef4daad1fd0 RDI: 0000710fc0000000
[ 5867.977915] RBP: ffffaba30695b8f8 R08: 0000000000003880 R09: ffff8ef388479040
[ 5867.977917] R10: ffffefd40d1b2b40 R11: 0000000000000d00 R12: ffffaba306cacf60
[ 5867.977918] R13: ffffffffc02d0c04 R14: 00000000000001fc R15: 0000000000000200
[ 5867.977920] FS:  00007ffb21a81740(0000) GS:ffff8ef4fed40000(0000) knlGS:0000000000000000
[ 5867.977921] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 5867.977923] CR2: ffffefd40d1b2b60 CR3: 00000001ef838000 CR4: 00000000000406e0
[ 5867.977924] Call Trace:
[ 5867.978021]  amdgpu_vram_mgr_new+0x314/0x370 [amdgpu]
[ 5867.978028]  amdttm_bo_mem_space+0x2ef/0x470 [amdttm]
[ 5867.978033]  amdttm_bo_validate+0xbf/0x140 [amdttm]
[ 5867.978036]  ? kmem_cache_alloc_trace+0x14e/0x1b0
[ 5867.978040]  ? _kcl_reservation_object_reserve_shared+0x48/0x190 [amdkcl]
[ 5867.978044]  amdttm_bo_init_reserved+0x285/0x420 [amdttm]
[ 5867.978084]  amdgpu_bo_do_create+0x1e6/0x4f0 [amdgpu]
[ 5867.978124]  ? amdgpu_bo_subtract_pin_size+0x60/0x60 [amdgpu]
[ 5867.978166]  amdgpu_bo_create+0x42/0x1e0 [amdgpu]
[ 5867.978169]  ? _cond_resched+0x19/0x40
[ 5867.978171]  ? kmem_cache_alloc_trace+0x14e/0x1b0
[ 5867.978224]  ? amdgpu_amdkfd_gpuvm_alloc_memory_of_gpu+0x323/0xb80 [amdgpu]
[ 5867.978270]  amdgpu_amdkfd_gpuvm_alloc_memory_of_gpu+0x50f/0xb80 [amdgpu]
[ 5867.978314]  kfd_ioctl_alloc_memory_of_gpu+0xcb/0x260 [amdgpu]
[ 5867.978357]  kfd_ioctl+0x271/0x450 [amdgpu]
[ 5867.978400]  ? kfd_dev_is_large_bar+0x90/0x90 [amdgpu]
[ 5867.978403]  ? __vma_rb_erase+0x1f1/0x270
[ 5867.978407]  do_vfs_ioctl+0xa8/0x630
[ 5867.978409]  SyS_ioctl+0x79/0x90
[ 5867.978411]  do_syscall_64+0x73/0x130
[ 5867.978414]  entry_SYSCALL_64_after_hwframe+0x3d/0xa2
[ 5867.978416] RIP: 0033:0x7ffb213ae5d7
[ 5867.978417] RSP: 002b:00007ffdd4886c08 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[ 5867.978418] RAX: ffffffffffffffda RBX: 00007ff9043d2360 RCX: 00007ffb213ae5d7
[ 5867.978420] RDX: 00007ffdd4886c60 RSI: 00000000c0284b16 RDI: 0000000000000006
[ 5867.978421] RBP: 00007ffdd4886c60 R08: 00007ffdd4886cf0 R09: 00000000c0000001
[ 5867.978422] R10: 0000000000004022 R11: 0000000000000246 R12: 00000000c0284b16
[ 5867.978423] R13: 0000000000000006 R14: 00000001d6400000 R15: 00007ff9043d2360
[ 5867.978424] Code: 00 80 49 01 da 0f 82 39 01 00 00 48 c7 c7 00 00 00 80 48 2b 3d e7 42 20 01 49 01 fa 49 c1 ea 0c 49 c1 e2 06 4c 03 15 c5 42 20 01 <49> 8b 42 20 48 8d 50 ff a8 01 4c 0f 45 d2 49 8b 52 20 48 8d 42 
[ 5867.978447] RIP: kfree+0x53/0x180 RSP: ffffaba30695b8e0
[ 5867.978448] CR2: ffffefd40d1b2b60
[ 5867.978450] ---[ end trace 9ef39b3baa5aa08b ]---
```

# Behaviour

The issue seems to occur sometimes (about 1 in 200000 calls) when the `sess.run` does not finish execution – it gets stuck – like... frozen. My python program then of course does not exit on its own. And the strangest thing is: It suddenly takes a freaking lot of RAM (like 10 GB) that I can by no means release again, unless I restart my computer. Here is a real life illustration of how the process behaves while tf is frozen:
```
# ps --sort -%mem aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
me       13671 37.1 11.2 19321984 2764652 pts/2 Sl+ 13:02 186:10 python3 ./main.py -sp 32ki auto
me        7204  5.1  4.0 6869916 1005076 ?     Sl   12:07  28:36 /snap/pycharm-professional/109/jre64/bin/java -classp
[...]

# free
              total        used        free      shared  buff/cache   available
Mem:       24636156    16067024     6846816      313488     1722316     7896620
Swap:       8368124      442624     7925500

# kill -15 13671

# ps --sort -%mem aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
me        7204  5.1  4.0 6869916 1005076 ?     Sl   12:07  28:39 /snap/pycharm-professional/109/jre64/bin/java -classp
[...]

# free
              total        used        free      shared  buff/cache   available
Mem:       24636156    16034456     6849972      336212     1751728     7906252
Swap:       8368124      437760     7930364
```

# My specs

 - OS is _linux_
 - GPU is _AMD Radeon RX Vega 64_
 - CPU is _AMD FX-8320_
 - RAM is _2 times 4GB and 2 times 8GB of 1333 DDR-3_
 - Mainboard is _ASRock 970A-G 3.1_
 - Tensorflow is the one I get, when installing via `pip3 install tensorflow-rocm` (version 1.13.1 but I had the issue on 1.12.0 also)

# The code I execute

Because of the very infrequent occurrence and the need to restart my computer after each occurrence, it is hard for me to reproduce the problem with minimal code. It would probably take days of consistent work. So what I can provide is my whole source and an example of where it gets stuck. That *sometimes* is in https://repos.lsv.uni-saarland.de/lol-forecaster/generator/blob/db35b21122b2149904f806f87a0396d446f46a22/tfnn.py inside the method `TrainableNeuralNetwork.start_session` and *sometimes* in `TrainableNeuralNetwork.train_one_step` and *sometimes* not at all.

---

## 评论 (2 条)

### 评论 #1 — tasso (2023-12-11T14:41:37Z)

Was this issue resolved with https://github.com/ROCm/ROCm/issues/785?  If so, can we please close issue?

---

### 评论 #2 — tasso (2023-12-18T18:52:35Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request. If this is still an issue, please file a new ticket and we will be more than happy to investigate it. Thanks!

---
