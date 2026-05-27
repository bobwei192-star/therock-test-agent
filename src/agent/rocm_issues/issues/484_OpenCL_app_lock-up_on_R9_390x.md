# OpenCL app lock-up on R9 390x

> **Issue #484**
> **状态**: closed
> **创建时间**: 2018-08-01T00:26:35Z
> **更新时间**: 2021-11-22T21:55:24Z
> **关闭时间**: 2021-01-06T12:30:50Z
> **作者**: preda
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/484

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

Ubuntu 18.04, Linux kernel 4.15, ROCm 1.8.2, on a system that was running fine with amdgpu-pro 18.20, and the app is also running fine on different GPUs (vega, fuji) with ROCm 1.8.2.

When running on R9 390x, the apps runs a bit (seconds) and then locks up. I see this in dmesg:
[   99.996641] Evicting PASID 32768 queues
[  100.004263] Restoring PASID 32768 queues
[  700.349797] Evicting PASID 32768 queues
[  700.357341] Restoring PASID 32768 queues

The process appears in "Sl+" state
~$ ps auxw | grep openowl
preda     3020  1.0  0.1 271070972 81644 pts/3 Sl+  10:17   0:04 ./openowl -user preda -cpu 390 -block 100

The GPU uses low power (is not busy) after the lock up.

The system is still responding including graphics on this GPU. I can kill the app with "kill -9" and restart it (and the same lockup repeats).

---

## 评论 (41 条)

### 评论 #1 — gstoner (2018-08-01T13:50:41Z)

Can you check the power at load, this is dual ASIC,  also what is the size of power supply in the system. 

---

### 评论 #2 — jlgreathouse (2018-08-01T14:07:44Z)

I believe I am able to reproduce this on my FirePro W9100 on an old Opteron 4386 (a system with the Hawaii GPU connected through PCIe gen 2).

On a second system, with a Ryzen 7 1800X, (with the FirePro W9100 GPU attached through PCIe gen 3), I am unable to reproduce the problem.

@preda could you give us more information about your hardware and software setup, the directions you use to reproduce the problem, etc.? This bug report is very light on details, and that makes it difficult for us to help you solve your problem. (As an aside, we are at ROCm 1.**8**.2, not 1.9.2. It would be useful to correctly list this so that when people see the issue ticket in the future, -- such as if 1.9.2 actually comes out -- they do not get bad information.)

---

### 评论 #3 — jlgreathouse (2018-08-01T15:17:01Z)

To note, on my Ryzen 7 1800X + Radeon W9100 (PCIe gen 3), I have been running `openowl` for over an hour and it is continuing to make forward progress.

---

### 评论 #4 — preda (2018-08-01T22:22:25Z)

@gstoner The power supply is a quality 850W. This is not a power supply problem. At load with GPU only it takes about 330W, at load with CPU+GPU about 510W at the socket. Without load about 150W.

The system is a dual Xeon E5-2630v3, motherboard X10DAi, 4x64GB ECC RAM. Ubuntu 18.04 kernel 4.15.0-29-generic. I attach lshw output for details 
[lshw.txt](https://github.com/RadeonOpenCompute/ROCm/files/2251298/lshw.txt)

What other information specifically would you like me to provide?

@jlgreathouse : fixed ROCm version, thanks for pointing it out, must have been a freudian slip :)

---

### 评论 #5 — gstoner (2018-08-01T22:29:43Z)

The gpu if it is dual gpu the can be power issues with peak currents.   Why I am asking.

Get Outlook for iOS<https://aka.ms/o0ukef>

________________________________
From: Mihai Preda <notifications@github.com>
Sent: Wednesday, August 1, 2018 5:22 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] OpenCL app lock-up on R9 390x (#484)


@gstoner<https://github.com/gstoner> The power supply is a quality 850W. This is not a power supply problem. At load with GPU only it takes about 330W, at load with CPU+GPU about 510W at the socket. Without load about 150W.

The system is a dual Xeon E5-2630v3, motherboard X10DAi, 4x64GB ECC RAM. Ubuntu 18.04 kernel 4.15.0-29-generic. I attach lshw output for details
lshw.txt<https://github.com/RadeonOpenCompute/ROCm/files/2251298/lshw.txt>

What other information specifically would you like me to provide?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/484#issuecomment-409744270>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Ducq4SNC2bm7NmdDjmpjT1zWoOKHAks5uMiojgaJpZM4Vpp3Z>.


---

### 评论 #6 — preda (2018-08-01T22:32:17Z)

It seems to be well within power margin. Also during the repro I was running without load on the CPUs, so more headroom. Also the same system has been running for long time stable with either older ROCm or amdgpu-pro, with similar power use.


---

### 评论 #7 — gstoner (2018-08-01T22:40:35Z)

This helps

Get Outlook for iOS<https://aka.ms/o0ukef>

________________________________
From: Mihai Preda <notifications@github.com>
Sent: Wednesday, August 1, 2018 5:32 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] OpenCL app lock-up on R9 390x (#484)


It seems to be well within power margin. Also during the repro I was running without load on the CPUs, so more headroom. Also the same system has been running for long time stable with either older ROCm or amdgpu-pro, with similar power use.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/484#issuecomment-409746526>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuaIs_POaDhiWwkkiOb3UVvpbHnFdks5uMixygaJpZM4Vpp3Z>.


---

### 评论 #8 — jlgreathouse (2018-08-13T20:00:13Z)

Hi @preda 

I'm still having a lot of trouble recreating this issue. I've been able to observe it on a single system, but that's an old Piledriver-based Opteron with the GPU connected through a PCIe gen 2 slot (that I'm running at home, outside of work). I suspect that we would be unable to debug this probme if it only occurs in such a situation, due to the experimental nature of our Hawaii GPU support in ROCm, and due to our recommended systems including PCIe gen 3.

I can successfully run your application on an AMD A10-7850K CPU connected to a Hawaii GPU on a PCIe gen 3 slot without atomics. I can also successfully run your application on an AMD Ryzen 7 1800X CPU connected to a Hawaii GPU on a PCIe gen 3 slot with atomics.

Is there any chance you could show me the outputs of the following two commands:
`sudo lspci -t`
`sudo lspci -vvv`

Thanks!

---

### 评论 #9 — preda (2018-08-16T13:16:06Z)

Sorry for the delay, I just now got to the concerned computer. Here is the output of lspci:

lspci1.txt](https://github.com/RadeonOpenCompute/ROCm/files/2293775/lspci1.txt)
[lspci2.txt](https://github.com/RadeonOpenCompute/ROCm/files/2293776/lspci2.txt)

Please handle (or close) the issue as you best see fit -- I'm not blocked by it (I can use this Hawaii GPU with amdgpu-pro).


---

### 评论 #10 — preda (2019-01-04T00:12:16Z)

This may be out of date, I don't have access to the 390x system myself anymore, feel free to close as you please.

---

### 评论 #11 — jlgreathouse (2019-01-04T00:16:38Z)

I'd still like to track this, since I was able to reproduce it once. As of ROCm 2.0,0. Hawaii is currently broken because of a bad firmware structure. We hope to have this fixed in our next release, and I can try to circle back to this issue.

---

### 评论 #12 — illwieckz (2019-02-25T01:19:35Z)

I have an R9 390X and I may find time to test things.

Basically I'm without OpenCL since many months now and that makes my photo process slow and painful.
Previously on first weeks of Ubuntu 18.10 I was able to run both rocm (by removing from dkms some modules that failed to build, but not all) and `libclc-amdgcn` (mesa).

I noticed that rocm worked well with my photo setup (darktable) and that mesa opencl got better performance than rocm in some benchmarks like luxmark, but I don't do luxmark 3D render so it's useless to me.

Then suddenly after some week or few month I discovered after some update that I was not able to build any rocm dkms modules at all. And at this point, rocm opencl stopped to work.

The weird thing is that I was still running 4.18 kernels, just updated ones.

I noticed these days after some rocm update that rocm dkms modules now build on 4.18 again, but it leads to an unusable computer as the computer hangs at startup (I'm even not able to use the magic sys keys).

I installed kernel from 18.04 (4.15) but the amdgpu driver from rocm hangs with it too.

I also tried 4.20.12 kernel without dkms (installing `rocm-opencl` and `rocm-dkms`) but I get nothing better.

I also tried amdgpu-pro `18.50-725072` but I I got nothing opencl wise if I don't install the dkms modules, and if I install the amdgpu-pro dkms modules the kernel just hangs at startup too.

Whatever the combination, I'm not able to run OpenCL stuff on my computer.

So, that's the current status when I type `clinfo` (not that dkms module are _never installed_ since kernel does not boot if installed):

- rocm does not work (clinfo hang)
- amdgcn-clc does not work (clinfo hang)
- amdgpu-pro does not work (clinfo hang)

So, really, if there is something I can do to debug rocm on 39 390X I would try to do it.
I don't mind amdgcn-clc since there is no image support

I think a good thing to know is that clinfo started to hang one day with vanilla kernel and vanilla amdgcn-clc after a kernel update (unfortunately I don't rememeber which), it means linux kernel just stopped to work and rocm is probably just facing the same bug.

This is rocminfo output:

```
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD FX(tm)-9590 Eight-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):4700                               
  BDFID:                   0                                  
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32901480KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32901480KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26544                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1080                               
  BDFID:                   256                                
  Compute Unit:            44                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  16778240                           
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8388608KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64KB                               
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
      Workgroup Max Dimension: 
        Dim[0]:                  67109888                           
        Dim[1]:                  1024                               
        Dim[2]:                  16777217                           
      Workgroup Max Size:      1024                               
      Grid Max Dimension:      
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      Grid Max Size:           4294967295                         
      FBarrier Max Size:       32                                 
*** Done ***     
```

This what I got in dmesg with amdgpu-pro (clinfo hanged):

```
[ 1874.570504] cp queue preemption time out
[ 1874.570516] Resetting wave fronts (nocpsch) on dev 00000000ea355777
[ 1874.570536] BUG: unable to handle kernel NULL pointer dereference at 0000000000000038
[ 1874.570540] PGD 0 P4D 0 
[ 1874.570547] Oops: 0000 [#1] SMP NOPTI
[ 1874.570554] CPU: 4 PID: 17050 Comm: clinfo Tainted: G           OE     4.20.12-042012-generic #201902230431
[ 1874.570558] Hardware name: To be filled by O.E.M. To be filled by O.E.M./SABERTOOTH 990FX R2.0, BIOS 2501 04/08/2014
[ 1874.570711] RIP: 0010:amdgpu_ib_schedule+0x4e/0x5b0 [amdgpu]
[ 1874.570717] Code: 00 4c 89 45 a8 48 89 cb 41 89 f4 49 89 ff 48 89 55 b8 0f b6 87 6c 02 00 00 48 85 c9 0f 84 50 03 00 00 48 8b 51 10 48 8b 79 78 <48> 8b 72 38 48 89 7d b0 48 89 75 c8 84 c0 0f 84 fb 04 00 00 48 83
[ 1874.570721] RSP: 0018:ffffb708226e7a70 EFLAGS: 00010286
[ 1874.570725] RAX: 0000000000000001 RBX: ffff92e05f486000 RCX: ffff92e05f486000
[ 1874.570729] RDX: 0000000000000000 RSI: 0000000000000001 RDI: 0000000000000000
[ 1874.570732] RBP: ffffb708226e7ad8 R08: ffffb708226e7af8 R09: ffff92e25e402f00
[ 1874.570736] R10: 0000000000000004 R11: 0000000000000000 R12: 0000000000000001
[ 1874.570739] R13: 0000000000000007 R14: 0000000000ffd000 R15: ffff92e24b905048
[ 1874.570744] FS:  00007fd10b617700(0000) GS:ffff92e25eb00000(0000) knlGS:0000000000000000
[ 1874.570747] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 1874.570751] CR2: 0000000000000038 CR3: 00000007bff0c000 CR4: 00000000000406e0
[ 1874.570754] Call Trace:
[ 1874.570764]  ? __kmalloc+0x183/0x220
[ 1874.570905]  ? amdgpu_job_alloc+0x3c/0xd0 [amdgpu]
[ 1874.571039]  amdgpu_amdkfd_submit_ib+0xbb/0x170 [amdgpu]
[ 1874.571179]  deallocate_vmid.isra.13+0xfb/0x120 [amdgpu]
[ 1874.571317]  destroy_queue_nocpsch_locked+0x186/0x1c0 [amdgpu]
[ 1874.571454]  process_termination_nocpsch+0x6c/0x130 [amdgpu]
[ 1874.571591]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
[ 1874.571727]  kfd_process_notifier_release+0xf4/0x180 [amdgpu]
[ 1874.571734]  __mmu_notifier_release+0x47/0xd0
[ 1874.571741]  exit_mmap+0x34/0x190
[ 1874.571748]  ? __delayacct_add_tsk+0x164/0x170
[ 1874.571753]  ? _cond_resched+0x19/0x30
[ 1874.571759]  mmput+0x57/0x130
[ 1874.571765]  do_exit+0x288/0xb30
[ 1874.571770]  ? mem_cgroup_commit_charge+0x82/0x4d0
[ 1874.571775]  do_group_exit+0x43/0xb0
[ 1874.571781]  get_signal+0x13a/0x6d0
[ 1874.571786]  do_signal+0x34/0x700
[ 1874.571794]  ? __x64_sys_futex+0x14c/0x188
[ 1874.571802]  exit_to_usermode_loop+0x8e/0x100
[ 1874.571807]  do_syscall_64+0xda/0x110
[ 1874.571813]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[ 1874.571817] RIP: 0033:0x7fd118ece2eb
[ 1874.571825] Code: Bad RIP value.
[ 1874.571829] RSP: 002b:00007fd10b616d80 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
[ 1874.571833] RAX: fffffffffffffe00 RBX: 00007fd118ea4128 RCX: 00007fd118ece2eb
[ 1874.571837] RDX: 0000000000000000 RSI: 0000000000000080 RDI: 00007fd118ea4150
[ 1874.571840] RBP: 00007fd118ea414c R08: 0000000000000000 R09: 0000000000000000
[ 1874.571843] R10: 0000000000000000 R11: 0000000000000246 R12: 00007fd118ea4150
[ 1874.571846] R13: 00007fd118ea4100 R14: 000000000000001c R15: 0000000000000000
[ 1874.571851] Modules linked in: zram binfmt_misc snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi snd_usb_audio snd_usbmidi_lib snd_hda_intel snd_hda_codec snd_hda_core joydev edac_mce_amd snd_hwdep snd_pcm kvm_amd snd_seq_dummy ccp snd_seq_oss kvm snd_seq_midi eeepc_wmi snd_seq_midi_event asus_wmi irqbypass input_leds snd_rawmidi sparse_keymap video serio_raw snd_seq wmi_bmof snd_seq_device snd_timer fam15h_power k10temp snd soundcore mac_hid sch_fq_codel vhba(OE) it87 hwmon_vid parport_pc ppdev lp parport ip_tables x_tables autofs4 btrfs zstd_compress algif_skcipher af_alg dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c multipath linear bcache crc64 raid0 raid1 hid_generic usbhid hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel amdgpu chash amd_iommu_v2 gpu_sched i2c_algo_bit ttm drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops aesni_intel drm mxm_wmi aes_x86_64 crypto_simd
[ 1874.571920]  drm_panel_orientation_quirks cryptd cfbfillrect glue_helper cfbimgblt cfbcopyarea r8169 fb realtek i2c_piix4 ahci fbdev libahci i2c_core wmi
[ 1874.571940] CR2: 0000000000000038
[ 1874.571944] ---[ end trace 59d55d9da35b33bb ]---
[ 1874.572064] RIP: 0010:amdgpu_ib_schedule+0x4e/0x5b0 [amdgpu]
[ 1874.572068] Code: 00 4c 89 45 a8 48 89 cb 41 89 f4 49 89 ff 48 89 55 b8 0f b6 87 6c 02 00 00 48 85 c9 0f 84 50 03 00 00 48 8b 51 10 48 8b 79 78 <48> 8b 72 38 48 89 7d b0 48 89 75 c8 84 c0 0f 84 fb 04 00 00 48 83
[ 1874.572072] RSP: 0018:ffffb708226e7a70 EFLAGS: 00010286
[ 1874.572076] RAX: 0000000000000001 RBX: ffff92e05f486000 RCX: ffff92e05f486000
[ 1874.572079] RDX: 0000000000000000 RSI: 0000000000000001 RDI: 0000000000000000
[ 1874.572083] RBP: ffffb708226e7ad8 R08: ffffb708226e7af8 R09: ffff92e25e402f00
[ 1874.572086] R10: 0000000000000004 R11: 0000000000000000 R12: 0000000000000001
[ 1874.572089] R13: 0000000000000007 R14: 0000000000ffd000 R15: ffff92e24b905048
[ 1874.572094] FS:  00007fd10b617700(0000) GS:ffff92e25eb00000(0000) knlGS:0000000000000000
[ 1874.572097] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 1874.572101] CR2: 00007fd118ece2c1 CR3: 00000007bff0c000 CR4: 00000000000406e0
[ 1874.572104] Fixing recursive fault but reboot is needed!
```

While the former clinfo is still stuck, if I start others clinfo it segfaults and I get that in `dmesg`:

```
[ 4261.960120] clinfo[16060]: segfault at 0 ip 0000000000000000 sp 00007ffe3b87e238 error 14 in clinfo[564bb988f000+17000]
[ 4261.960126] Code: Bad RIP value.
[ 4568.543174] clinfo[16761]: segfault at 0 ip 0000000000000000 sp 00007ffe0204f108 error 14 in clinfo[400000+81000]
[ 4568.543180] Code: Bad RIP value.
```

First is `/usr/bin/clinfo`, second is `/opt/amdgpu-pro/bin/clinfo`

---

### 评论 #13 — illwieckz (2019-02-25T01:40:37Z)

Additional notes: I get the similar things in `dmesg` with rocm, when clinfo hangs:

```
[  193.780850] cp queue preemption time out
[  193.780864] Resetting wave fronts (nocpsch) on dev 000000000e50fa01
[  193.780881] BUG: unable to handle kernel NULL pointer dereference at 0000000000000038
[  193.780885] PGD 0 P4D 0 
[  193.780892] Oops: 0000 [#1] SMP NOPTI
[  193.780899] CPU: 2 PID: 6399 Comm: clinfo Tainted: G           OE     4.20.12-042012-generic #201902230431
[  193.780903] Hardware name: To be filled by O.E.M. To be filled by O.E.M./SABERTOOTH 990FX R2.0, BIOS 2501 04/08/2014
[  193.781058] RIP: 0010:amdgpu_ib_schedule+0x4e/0x5b0 [amdgpu]
[  193.781063] Code: 00 4c 89 45 a8 48 89 cb 41 89 f4 49 89 ff 48 89 55 b8 0f b6 87 6c 02 00 00 48 85 c9 0f 84 50 03 00 00 48 8b 51 10 48 8b 79 78 <48> 8b 72 38 48 89 7d b0 48 89 75 c8 84 c0 0f 84 fb 04 00 00 48 83
[  193.781068] RSP: 0018:ffffac1b0ed0ba70 EFLAGS: 00010286
[  193.781072] RAX: 0000000000000001 RBX: ffff925def353c00 RCX: ffff925def353c00
[  193.781076] RDX: 0000000000000000 RSI: 0000000000000001 RDI: 0000000000000000
[  193.781079] RBP: ffffac1b0ed0bad8 R08: ffffac1b0ed0baf8 R09: ffff925e1e402f00
[  193.781082] R10: 0000000000000004 R11: 0000000000000000 R12: 0000000000000001
[  193.781086] R13: 0000000000000007 R14: 0000000000ffd000 R15: ffff925e0d205048
[  193.781090] FS:  00007f6c244a1740(0000) GS:ffff925e1ea80000(0000) knlGS:0000000000000000
[  193.781094] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  193.781097] CR2: 0000000000000038 CR3: 0000000739602000 CR4: 00000000000406e0
[  193.781101] Call Trace:
[  193.781111]  ? __kmalloc+0x183/0x220
[  193.781251]  ? amdgpu_job_alloc+0x3c/0xd0 [amdgpu]
[  193.781385]  amdgpu_amdkfd_submit_ib+0xbb/0x170 [amdgpu]
[  193.781523]  deallocate_vmid.isra.13+0xfb/0x120 [amdgpu]
[  193.781660]  destroy_queue_nocpsch_locked+0x186/0x1c0 [amdgpu]
[  193.781796]  process_termination_nocpsch+0x6c/0x130 [amdgpu]
[  193.781932]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
[  193.782067]  kfd_process_notifier_release+0xf4/0x180 [amdgpu]
[  193.782074]  __mmu_notifier_release+0x47/0xd0
[  193.782081]  exit_mmap+0x34/0x190
[  193.782088]  ? do_futex+0x10e/0x500
[  193.782094]  ? __delayacct_add_tsk+0x164/0x170
[  193.782100]  ? _cond_resched+0x19/0x30
[  193.782106]  mmput+0x57/0x130
[  193.782112]  do_exit+0x288/0xb30
[  193.782118]  ? wake_up_state+0x10/0x20
[  193.782124]  ? signal_wake_up_state+0x19/0x30
[  193.782129]  do_group_exit+0x43/0xb0
[  193.782134]  get_signal+0x13a/0x6d0
[  193.782140]  do_signal+0x34/0x700
[  193.782146]  ? recalc_sigpending+0x1b/0x50
[  193.782150]  ? __set_task_blocked+0x72/0x90
[  193.782157]  exit_to_usermode_loop+0x8e/0x100
[  193.782162]  do_syscall_64+0xda/0x110
[  193.782168]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[  193.782173] RIP: 0033:0x7f6c240a1077
[  193.782181] Code: Bad RIP value.
[  193.782184] RSP: 002b:00005634389e36e0 EFLAGS: 00000246 ORIG_RAX: 000000000000000e
[  193.782189] RAX: 0000000000000000 RBX: 0000000000000000 RCX: 00007f6c240a1077
[  193.782192] RDX: 0000000000000000 RSI: 00005634389e36e0 RDI: 0000000000000002
[  193.782195] RBP: 0000000000000000 R08: 0000000000000000 R09: 00005634389e36e0
[  193.782199] R10: 0000000000000008 R11: 0000000000000246 R12: 0000000000000002
[  193.782202] R13: 00005634389e3880 R14: 0000000000000000 R15: 00000000c0031002
[  193.782206] Modules linked in: zram binfmt_misc joydev snd_usb_audio snd_usbmidi_lib edac_mce_amd eeepc_wmi snd_hda_codec_realtek kvm_amd asus_wmi snd_hda_codec_generic ccp snd_hda_codec_hdmi kvm sparse_keymap snd_seq_dummy snd_hda_intel snd_seq_oss video input_leds irqbypass snd_hda_codec snd_seq_midi wmi_bmof serio_raw snd_hda_core snd_seq_midi_event snd_rawmidi snd_hwdep fam15h_power snd_pcm k10temp snd_seq snd_seq_device snd_timer radeon snd soundcore mac_hid sch_fq_codel vhba(OE) it87 hwmon_vid parport_pc ppdev lp parport ip_tables x_tables autofs4 btrfs zstd_compress algif_skcipher af_alg dm_crypt raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c multipath linear bcache crc64 raid0 raid1 hid_generic usbhid hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel amdgpu chash amd_iommu_v2 gpu_sched mxm_wmi i2c_algo_bit ttm aesni_intel drm_kms_helper syscopyarea sysfillrect aes_x86_64 sysimgblt crypto_simd fb_sys_fops cryptd glue_helper drm
[  193.782276]  drm_panel_orientation_quirks r8169 cfbfillrect cfbimgblt realtek cfbcopyarea fb i2c_piix4 ahci fbdev i2c_core libahci wmi
[  193.782295] CR2: 0000000000000038
[  193.782299] ---[ end trace b710c6b36661a676 ]---
[  193.782419] RIP: 0010:amdgpu_ib_schedule+0x4e/0x5b0 [amdgpu]
[  193.782424] Code: 00 4c 89 45 a8 48 89 cb 41 89 f4 49 89 ff 48 89 55 b8 0f b6 87 6c 02 00 00 48 85 c9 0f 84 50 03 00 00 48 8b 51 10 48 8b 79 78 <48> 8b 72 38 48 89 7d b0 48 89 75 c8 84 c0 0f 84 fb 04 00 00 48 83
[  193.782428] RSP: 0018:ffffac1b0ed0ba70 EFLAGS: 00010286
[  193.782432] RAX: 0000000000000001 RBX: ffff925def353c00 RCX: ffff925def353c00
[  193.782435] RDX: 0000000000000000 RSI: 0000000000000001 RDI: 0000000000000000
[  193.782438] RBP: ffffac1b0ed0bad8 R08: ffffac1b0ed0baf8 R09: ffff925e1e402f00
[  193.782442] R10: 0000000000000004 R11: 0000000000000000 R12: 0000000000000001
[  193.782445] R13: 0000000000000007 R14: 0000000000ffd000 R15: ffff925e0d205048
[  193.782450] FS:  00007f6c244a1740(0000) GS:ffff925e1ea80000(0000) knlGS:0000000000000000
[  193.782453] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  193.782456] CR2: 00007f6c240a104d CR3: 0000000739602000 CR4: 00000000000406e0
[  193.782460] Fixing recursive fault but reboot is needed!
```

Note that both `/opt/rocm/opencl/bin/x86_64/clinfo` and `/usr/bin/clinfo` hangs, and this time all other calls hang. I'm not able to kill them, even with `-9`.

Note that those hangs happen when clinfo run as root, if run as user, I get this:

```
$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
$ /usr/bin/clinfo 
Number of platforms                               0
```

and for some reason `rocminfo` does not work as user too (previous log was made as root):

```
$ rocminfo 
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104
```

My user is in `video` group of course.

I just notice that `rocminfo` hangs to after `clinfo` hanged.

---

### 评论 #14 — illwieckz (2019-02-25T01:57:37Z)

To get the former dmesg log I do that (as root):

I run clinfo:
`/opt/rocm/opencl/bin/x86_64/clinfo`
It stucks immediately

Then I try to kill it from another terminal:
`killall -9 clinfo`
The dmesg get the error log

Note that dmesg filling-up happens when I attempt to kill clinfo.

This latest test was done with Linux `4.20.12-042012-generic` on Ubuntu 18.10.

---

### 评论 #15 — PhilipDeegan (2019-10-05T19:43:52Z)

Should opencl work on the R9 390?

---

### 评论 #16 — illwieckz (2019-11-17T09:57:44Z)

> Should opencl work on the R9 390?

it used to work

Edit: for what I remember, it worked on the past with the provided dkms kernel module, so maybe not everything is upstreamed.

---

### 评论 #17 — illwieckz (2019-11-17T10:04:55Z)

I just redid the test, with Ubunbu 19.10 eoan and Linux  5.3.0-21-generic

Stuff installed correctly, `rocminfo` prints stuff that looks legit, but `clinfo` hangs, and on `clinfo` sigkill, this is printed on dmesg:

```
[357532.062489] cp queue preemption time out
[357532.062501] Resetting wave fronts (nocpsch) on dev 00000000ec32e4a0
[357532.062543] ------------[ cut here ]------------
[357532.062544] FW bug: No PASID in KFD interrupt
[357532.062873] WARNING: CPU: 2 PID: 0 at drivers/gpu/drm/amd/amdgpu/../amdkfd/cik_event_interrupt.c:70 cik_event_interrupt_isr+0x12b/0x140 [amdgpu]
[357532.062874] Modules linked in: nls_iso8859_1 uas usb_storage ufs qnx4 hfsplus hfs minix ntfs msdos jfs xfs cpuid ebtable_filter ebtables ip6table_filter ip6_tables iptable_filter bpfilter pci_stub vboxpci(OE) vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) aufs overlay bridge stp llc zram binfmt_misc snd_usb_audio snd_usbmidi_lib joydev mc edac_mce_amd kvm_amd ccp snd_seq_midi snd_hda_codec_realtek snd_seq_midi_event kvm snd_hda_codec_generic snd_rawmidi snd_hda_codec_hdmi ledtrig_audio irqbypass snd_hda_intel eeepc_wmi snd_hda_codec asus_wmi sparse_keymap input_leds snd_hda_core video wmi_bmof serio_raw snd_hwdep snd_pcm k10temp snd_seq fam15h_power snd_seq_device snd_timer snd soundcore mac_hid sch_fq_codel nfsd vhba(OE) it87 hwmon_vid auth_rpcgss parport_pc nfs_acl lockd ppdev grace lp parport sunrpc ip_tables x_tables autofs4 btrfs zstd_compress dm_crypt raid10 raid0 multipath linear bcache crc64 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1
[357532.062934]  hid_generic usbhid hid amdgpu crct10dif_pclmul crc32_pclmul ghash_clmulni_intel amd_iommu_v2 gpu_sched aesni_intel radeon aes_x86_64 crypto_simd i2c_algo_bit cryptd ttm glue_helper drm_kms_helper syscopyarea r8169 sysfillrect sysimgblt realtek fb_sys_fops mxm_wmi drm i2c_piix4 ahci libahci wmi
[357532.062959] CPU: 2 PID: 0 Comm: swapper/2 Tainted: G           OE     5.3.0-21-generic #22-Ubuntu
[357532.062961] Hardware name: To be filled by O.E.M. To be filled by O.E.M./SABERTOOTH 990FX R2.0, BIOS 2501 04/08/2014
[357532.063132] RIP: 0010:cik_event_interrupt_isr+0x12b/0x140 [amdgpu]
[357532.063136] Code: ff ff 0f b6 05 15 90 24 00 84 c0 74 07 31 c0 e9 58 ff ff ff 48 c7 c7 30 46 a9 c0 88 04 24 c6 05 f9 8f 24 00 01 e8 c0 88 9f da <0f> 0b 0f b6 04 24 e9 37 ff ff ff 66 2e 0f 1f 84 00 00 00 00 00 0f
[357532.063138] RSP: 0018:ffffb3a240130d68 EFLAGS: 00010086
[357532.063141] RAX: 0000000000000000 RBX: ffff9076c9989400 RCX: 0000000000000000
[357532.063143] RDX: 0000000000000001 RSI: ffffffff9cd81fa1 RDI: 0000000000000046
[357532.063145] RBP: ffffb3a240130d88 R08: ffffffff9cd81f80 R09: 0000000000000021
[357532.063146] R10: 0000000000000000 R11: 0000000000000001 R12: ffffb3a24076c880
[357532.063148] R13: 0000000000000087 R14: ffff9076c99895d0 R15: ffffb3a240130db0
[357532.063151] FS:  0000000000000000(0000) GS:ffff9076dea80000(0000) knlGS:0000000000000000
[357532.063153] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[357532.063155] CR2: 000055ea0edcbe80 CR3: 000000012882a000 CR4: 00000000000406e0
[357532.063157] Call Trace:
[357532.063159]  <IRQ>
[357532.063332]  interrupt_is_wanted+0x19/0x20 [amdgpu]
[357532.063498]  kgd2kfd_interrupt+0xb0/0xf0 [amdgpu]
[357532.063638]  ? amdgpu_fence_process+0x46/0xe0 [amdgpu]
[357532.063804]  amdgpu_amdkfd_interrupt+0x1a/0x20 [amdgpu]
[357532.063960]  amdgpu_irq_dispatch+0xda/0x1e0 [amdgpu]
[357532.064117]  amdgpu_ih_process+0x8c/0x110 [amdgpu]
[357532.064273]  amdgpu_irq_handler+0x1f/0x50 [amdgpu]
[357532.064279]  __handle_irq_event_percpu+0x42/0x180
[357532.064283]  handle_irq_event_percpu+0x33/0x80
[357532.064286]  handle_irq_event+0x3b/0x5a
[357532.064290]  handle_edge_irq+0x93/0x1c0
[357532.064295]  handle_irq+0x20/0x30
[357532.064299]  do_IRQ+0x50/0xe0
[357532.064304]  common_interrupt+0xf/0xf
[357532.064306]  </IRQ>
[357532.064311] RIP: 0010:cpuidle_enter_state+0xc5/0x420
[357532.064314] Code: ff e8 bf 73 83 ff 80 7d c7 00 74 17 9c 58 0f 1f 44 00 00 f6 c4 02 0f 85 3d 03 00 00 31 ff e8 22 cf 89 ff fb 66 0f 1f 44 00 00 <45> 85 ed 0f 89 d1 01 00 00 41 c7 44 24 10 00 00 00 00 48 83 c4 18
[357532.064316] RSP: 0018:ffffb3a240097e38 EFLAGS: 00000246 ORIG_RAX: ffffffffffffffd8
[357532.064319] RAX: ffff9076deaaa740 RBX: ffffffff9c969a60 RCX: 000000000000001f
[357532.064320] RDX: 0000000000000000 RSI: 000000001b248665 RDI: 0000000000000000
[357532.064322] RBP: ffffb3a240097e78 R08: 0001452c6b953ba4 R09: 00000000000003b1
[357532.064324] R10: ffff9076deaa94e4 R11: ffff9076deaa94c4 R12: ffff9076d96c6c00
[357532.064325] R13: 0000000000000002 R14: 0000000000000002 R15: ffff9076d96c6c00
[357532.064331]  ? cpuidle_enter_state+0xa1/0x420
[357532.064335]  cpuidle_enter+0x2e/0x40
[357532.064339]  call_cpuidle+0x23/0x40
[357532.064341]  do_idle+0x1dd/0x270
[357532.064345]  cpu_startup_entry+0x20/0x30
[357532.064348]  start_secondary+0x168/0x1c0
[357532.064352]  secondary_startup_64+0xa4/0xb0
[357532.064356] ---[ end trace a442dbca9d863835 ]---
[357536.066491] cp queue preemption time out
[357536.066504] Resetting wave fronts (nocpsch) on dev 00000000ec32e4a0
```

For information, this is `rocminfo` output:

```
ROCk module is loaded
illwieckz is member of video group
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD FX(tm)-9590 Eight-Core Processor
  Marketing Name:          AMD FX(tm)-9590 Eight-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      16384(0x4000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32849688(0x1f53f18) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32849688(0x1f53f18) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
  Marketing Name:          Hawaii XT / Grenada XT [Radeon R9 290X/390X]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26544(0x67b0)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1080                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            44                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8388608(0x800000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***   
```

And `lspci -vvv -nn -s 01:00.0` ouput:

```
01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii XT / Grenada XT [Radeon R9 290X/390X] [1002:67b0] (rev 80) (prog-if 00 [VGA controller])
	Subsystem: Micro-Star International Co., Ltd. [MSI] Radeon R9 390X [1462:2015]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 73
	NUMA node: 0
	Region 0: Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at d0000000 (64-bit, prefetchable) [size=8M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at fea00000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: [48] Vendor Specific Information: Len=08 <?>
	Capabilities: [50] Power Management version 3
		Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold-)
		Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
	Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
		DevCap:	MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
			ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
		DevCtl:	CorrErr- NonFatalErr- FatalErr- UnsupReq-
			RlxdOrd- ExtTag+ PhantFunc- AuxPwr- NoSnoop+
			MaxPayload 128 bytes, MaxReadReq 512 bytes
		DevSta:	CorrErr+ NonFatalErr- FatalErr- UnsupReq+ AuxPwr- TransPend-
		LnkCap:	Port #0, Speed 8GT/s, Width x16, ASPM L0s L1, Exit Latency L0s <64ns, L1 <1us
			ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
		LnkCtl:	ASPM Disabled; RCB 64 bytes Disabled- CommClk+
			ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
		LnkSta:	Speed 5GT/s (downgraded), Width x16 (ok)
			TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
		DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR-, OBFF Not Supported
			 AtomicOpsCap: 32bit- 64bit- 128bitCAS-
		DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
			 AtomicOpsCtl: ReqEn-
		LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
			 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
			 Compliance De-emphasis: -6dB
		LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete-, EqualizationPhase1-
			 EqualizationPhase2-, EqualizationPhase3-, LinkEqualizationRequest-
	Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
		Address: 00000000fee00000  Data: 0000
	Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
	Capabilities: [150 v2] Advanced Error Reporting
		UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
		UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
		CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
		CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
		AERCap:	First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
			MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
		HeaderLog: 00000000 00000000 00000000 00000000
	Capabilities: [200 v1] Resizable BAR <?>
	Capabilities: [270 v1] Secondary PCI Express <?>
	Capabilities: [2b0 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [2c0 v1] Page Request Interface (PRI)
		PRICtl: Enable- Reset-
		PRISta: RF- UPRGI- Stopped+
		Page Request Capacity: 00000020, Page Request Allocation: 00000000
	Capabilities: [2d0 v1] Process Address Space ID (PASID)
		PASIDCap: Exec+ Priv+, Max PASID Width: 10
		PASIDCtl: Enable- Exec- Priv-
	Kernel driver in use: amdgpu
	Kernel modules: radeon, amdgpu
```

I bougth this GPU four years ago and was able to do OpenCL on it for less than a cumulated year. That is a very small success ratio.

---

### 评论 #18 — illwieckz (2019-11-17T12:04:52Z)

For people who may end here because of facing the same problem we face, I managed to get OpenCL working again **without ROCM**, on Ubuntu 19.10. I achieved this using amdgpu-pro package with legacy opencl driver. This is how to achieve this:

**Beware:** some of the installed package has a nasty pre-installation script that test distro versions and fail if it's not Ubuntu 18.04, **leaving your system broken in a way you cannot fix it** without advanced Debian skills: even the provided _amdgpu-uninstall_ tool will not be able to properly fix and uninstall what would be partially installed, even _apt --fix-broken install_ will not be able to fix your system. So you must temporarily edit a system file to make that nasty package happy, and revert this file once driver is installed to restore your system in a clean state.

So, this is a **way to install working legacy OpenCL driver without breaking your system**:

1. go to https://www.amd.com/fr/support/graphics/amd-radeon-r9-series/amd-radeon-r9-300-series/amd-radeon-r9-390x
2. Download the package for “_Ubuntu x86 64-Bit_”
3. Extract the archive (named like `amdgpu-pro-19.30-934563-ubuntu-18.04.tar.xz`)
4. Enter with a root shell in the extracted directory (named lile `amdgpu-pro-19.30-934563-ubuntu-18.04`)
5. Type those commands in this order (EDITED with safer instructions):

```sh
tempfile="$(mktemp)"

chmod a+r "${tempfile}"

sed -e 's/^NAME=".*"$/NAME="Ubuntu"/;s/^VERSION_ID=".*"$/VERSION_ID="18.04"/' '/usr/lib/os-release' > "${tempfile}"

mount -o bind "${tempfile}" '/usr/lib/os-release'

./amdgpu-install --no-dkms --headless --opencl='legacy'

umount '/usr/lib/os-release'

rm "${tempfile}"
```

Then as a user you can check it works by calling `clinfo`:

```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (2906.7)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     Hawaii
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (2906.7)
  Driver Version                                  2906.7
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Board Name (AMD)                         AMD Radeon (TM) R9 390 Series
  Device Topology (AMD)                           PCI-E, 01:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               44
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1080MHz
  Graphics IP (AMD)                               7.2
  Device Partition                                (core)
    Max number of sub-devices                     44
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (n/a)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (n/a)
  Single-precision Floating-point support         (core)
    Denormals                                     No
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              7392280576 (6.885GiB)
  Global free memory (AMD)                        7198160 (6.865GiB)
  Global memory channels (AMD)                    16
  Global memory banks per channel (AMD)           16
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           4244635648 (3.953GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       2048 bits (256 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               32768 (32KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        4244635648 (3.953GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        1573626799391914230ns (Wed Nov 13 07:33:19 2019)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  Yes
    Number of async queues (AMD)                  2
    Max real-time compute queues (AMD)            0
    Max real-time compute units (AMD)             0
    SPIR versions                                 1.2
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_amd_bus_addressable_memory cl_khr_spir cl_khr_gl_event 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   Hawaii
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   Hawaii
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   Hawaii
```

This is output of `darktable-cltest | egrep 'opencl_init|^ ' | grep -v 'compiling program'`:

```
0.020851 [opencl_init] opencl related configuration options:
0.020875 [opencl_init] 
0.020877 [opencl_init] opencl: 1
0.020879 [opencl_init] opencl_library: ''
0.020880 [opencl_init] opencl_memory_requirement: 768
0.020882 [opencl_init] opencl_memory_headroom: 300
0.020884 [opencl_init] opencl_device_priority: '*/!0,*/*/*'
0.020886 [opencl_init] opencl_mandatory_timeout: 200
0.020888 [opencl_init] opencl_size_roundup: 16
0.020889 [opencl_init] opencl_async_pixelpipe: 0
0.020890 [opencl_init] opencl_synch_cache: 0
0.020892 [opencl_init] opencl_number_event_handles: 25
0.020893 [opencl_init] opencl_micro_nap: 1000
0.020895 [opencl_init] opencl_use_pinned_memory: 0
0.020896 [opencl_init] opencl_use_cpu_devices: 0
0.020897 [opencl_init] opencl_avoid_atomics: 0
0.020898 [opencl_init] 
0.021084 [opencl_init] found opencl runtime library 'libOpenCL'
0.021106 [opencl_init] opencl library 'libOpenCL' found on your system and loaded
0.044265 [opencl_init] found 1 platform
0.044292 [opencl_init] found 1 device
0.044310 [opencl_init] device 0 `Hawaii' supports image sizes of 16384 x 16384
0.044312 [opencl_init] device 0 `Hawaii' allows GPU memory allocations of up to 4048MB
[opencl_init] device 0: Hawaii 
     GLOBAL_MEM_SIZE:          7050MB
     MAX_WORK_GROUP_SIZE:      256
     MAX_WORK_ITEM_DIMENSIONS: 3
     MAX_WORK_ITEM_SIZES:      [ 1024 1024 1024 ]
     DRIVER_VERSION:           2906.7
     DEVICE_VERSION:           OpenCL 1.2 AMD-APP (2906.7)
0.159560 [opencl_init] options for OpenCL compiler: -cl-fast-relaxed-math  -DAMD=1 -I"/usr/share/darktable/kernels"
0.249177 [opencl_init] kernel loading time: 0.0894 
0.249185 [opencl_init] OpenCL successfully initialized.
0.249190 [opencl_init] here are the internal numbers and names of OpenCL devices available to darktable:
0.249192 [opencl_init]		0	'Hawaii'
0.249194 [opencl_init] FINALLY: opencl is AVAILABLE on this system.
0.249198 [opencl_init] initial status of opencl enabled flag is ON.
```

And the luxmark benchmark finds the GPU and works correctly:

```
2019-11-17 13:02:52 - [LuxRays] [1831.199] OpenCL Platform 0: Advanced Micro Devices, Inc.
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 0 name: NativeThread
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 0 type: NATIVE_THREAD
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 0 compute units: 1
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 0 preferred float vector width: 4
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 0 max allocable memory: 0MBytes
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 0 max allocable memory block size: 0MBytes
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 1 name: Hawaii
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 1 type: OPENCL_GPU
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 1 compute units: 44
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 1 preferred float vector width: 1
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 1 max allocable memory: 7110MBytes
2019-11-17 13:02:52 - [LuxRays] [1831.199] Device 1 max allocable memory block size: 4048MBytes
2019-11-17 13:02:52 - [LuxRays] [1831.199] Preprocessing DataSet
2019-11-17 13:02:52 - [LuxRays] [1831.199] Total vertex count: 124324
2019-11-17 13:02:52 - [LuxRays] [1831.199] Total triangle count: 217544
2019-11-17 13:02:52 - [LuxRays] [1831.201] Preprocessing DataSet done
2019-11-17 13:02:52 - [LuxRays] [1831.237] Creating 1 intersection device(s)
2019-11-17 13:02:52 - [LuxRays] [1831.237] Allocating intersection device 0: Hawaii (Type = OPENCL_GPU)
2019-11-17 13:02:52 - [LuxCore] [1831.237] OpenCL Devices used:
2019-11-17 13:02:52 - [LuxCore] [1831.237] [HawaiiIntersect]
2019-11-17 13:02:52 - [LuxCore] [1831.237] Device OpenCL version: OpenCL 1.2 AMD-APP (2906.7)
```

And Blender Cycles finds the GPU and works correctly:

```
Cycles:
============================================


CPU device capabilities: SSE2 SSE3 SSE41 AVX

OpenCL device capabilities:
Number of platforms: 1
Platform #0
        Platform Name: AMD Accelerated Parallel Processing
        Platform Vendor: Advanced Micro Devices, Inc.
        Platform Version: OpenCL 2.1 AMD-APP (2906.7)
        Platform Profile: FULL_PROFILE
        Platform Extensions: cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
        Number of devices: 1
                Device: #0
                        Device Name: Hawaii
                        Device Board Name: AMD Radeon (TM) R9 390 Series
                        Device Vendor: Advanced Micro Devices, Inc.
                        Device OpenCL C Version: OpenCL C 1.2 
                        Device Profile: FULL_PROFILE
                        Device Version: OpenCL 1.2 AMD-APP (2906.7)
                        Device Extensions: cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_amd_bus_addressable_memory cl_khr_spir cl_khr_gl_event 
                        Device Max clock frequency (MHz): 1080
                        Device Max compute units: 44
                        Device Max work group size: 256
```

---

### 评论 #19 — pmilleroly27 (2019-11-25T01:13:06Z)

For the last command I got

overriding mode 644 (rw-r--r--)?

I pressed enter, clinfo worked, but system bricked on boot.

I'm guessing the last command is moving the nasty file back and I didn't enter the right command. What command do you enter after

mv /usr/lib/os-release.orig /user/lib/os-release

Testing on POP OS! 19.10 with vega 56. I'm seeing if this install method works on other gpus for an all in one solution for 7970, R9 390, rx 570 and vega 56 for running davinci resolve 16.



---

### 评论 #20 — illwieckz (2019-11-25T23:29:20Z)

> What command do you enter after
> mv /usr/lib/os-release.orig /user/lib/os-release

There is no need for more steps if it worked correctly. Maybe your problem is that you did not reverted correctly the `/usr/lib/os-release` file.

Note that there is a mistake in your command: `mv /usr/lib/os-release.orig /us`**e**`r/lib/os-release`

Can you paste the content of `/usr/lib/os-release`, and if exists, the content of `/usr/lib/os-release.orig` ?

---

### 评论 #21 — illwieckz (2019-11-25T23:37:11Z)

This is a safer procedure, as it does not modify filesystem to patch the `/usr/lib/os-release` file and the patch will not be kept on reboot even if something wrong happens at anytime (a reboot will bring back original `/usr/lib/os-release` in any way):

```sh
tempfile="$(mktemp)"

chmod a+r "${tempfile}"

sed -e 's/^NAME=".*"$/NAME="Ubuntu"/;s/^VERSION_ID=".*"$/VERSION_ID="18.04"/' '/usr/lib/os-release' > "${tempfile}"

mount -o bind "${tempfile}" '/usr/lib/os-release'

./amdgpu-install --no-dkms --headless --opencl='legacy'

umount '/usr/lib/os-release'

rm "${tempfile}"
```

---

### 评论 #22 — pmilleroly27 (2019-11-28T15:49:41Z)

Thanks for the info. I don't think it's worth my time.
This might sound odd, but Linux Mint 19.2 only comes with the radeon kernel module for the r9 390.
Linux Mint 18.3 comes with both radeon and amdgpu.
I disable radeon as others like yourself point out.
I upgraded to 19.2 from they're using kernel 4.15 I installed amdgpu 19.30.
Clinfo everything looks great, but davinci resolve 16 crashes.
I believe the problem with r9 390 for me is more related to it's opencl not working with Davinci Resolve.
Since Linux Mint kernel 4.15 with amdgpu 19.30 on polaris and vega work fine.
Oh well, I'll check on the 7970. Polaris and Vega gpus seem to work fine.
I could try your method with 2700u apu as that processor doesn't work on Linux without kernel 5.3 except with manjaro on my testing, but I don't think 19.30 even supports laptop apus.
I hope amd doesn't leave r9 390 opencl in the dust.
Hopefully it smooths and BMD needs to get they're shit together and put non-free packages in the linux repos like everyone else.
From what I'm seeing Rocm is not dropping opencl? I'm a bit confused they just launched a new update and the release notes seem to suggest opencl is out.

---

### 评论 #23 — pmilleroly27 (2019-11-29T00:33:12Z)

Interestingly enough 7970 is able to boot davinci resolve, but resolve complains about opencl. Despite the program recognizing the 7970 and opencl.
I checked 7970 and opencl in resolve, but the programs keeps asking for an opencl gpu.
Video has black playback. Which I've experienced when installing --headless or rocm-dev even with vega.
Resolve seems to require the full stack whether amdgpu-pro or rocm.
I'll be curious to test resolve 15 with amdgpu 19.30 and then try headless mode with vega/polaris.


---

### 评论 #24 — illwieckz (2019-11-29T01:04:15Z)

Right, I forgot that before doing such things I configured my system long time ago to use the `amdgpu` driver instead of the `radeon` one. This is probably required.

It's possible to check the right module is loaded this way:

```
lspci | grep VGA | cut -f1 -d' ' | xargs -n1 -P1 lspci -nn -v -s | egrep 'VGA|in use:'
```

That would print something like that:

```
01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii XT / Grenada XT [Radeon R9 290X/390X] [1002:67b0] (rev 80) (prog-if 00 [VGA controller])
	Kernel driver in use: amdgpu
```

As R9 390X user I switched from `radeon` driver to `amdgpu` one by adding `amdgpu.cik_support=1 radeon.cik_support=0` to the kernel command line, Radeon 7970 users may use `amdgpu.si_support=1 radeon.si_support=0` instead.

So basically this is a way to enable the right modules whatever you have an R9 390X or an HD 7970:

```sh
cat >/etc/default/grub.d/amdgpu_enable.cfg <<\EOF
# R9 390X and friends
GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} amdgpu.cik_support=1 radeon.cik_support=0"
# HD 7970 and friends
GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} amdgpu.si_support=1 radeon.si_support=0"
EOF

update-grub
```

And reboot.

---

### 评论 #25 — illwieckz (2019-11-29T01:05:13Z)

Note that I don't use Resolve so I can't check, maybe there is a bug in Resolve and the Resolve team can fix it?

---

### 评论 #26 — pmilleroly27 (2019-11-29T04:39:46Z)

Your method did work even on 2700u apu. I originally had a crash, but booted up the laptop today. Booted in, installed davinci resolve and it worked.
R9 390 and old gpus won't work with Davinci Resolve, but thats the program not supporting that opencl not an issue with the opencl itself.
I even tested Davinci 14/15 don't matter, those Hawaii cards are potatoes for that particular application.

---

### 评论 #27 — illwieckz (2020-06-22T01:52:52Z)

For information I tried ROCm's OpenCL again with my R9 390X on Ubuntu 20.04, using stock kernel (`5.4.0-38-generic`) and only installin `rocm-opencl` and `rocminfo` (no `rocm-dkms`, I'm trying to use the stock kernel driver).

Running `clinfo` still hangs and I still get some report on dmesg when I send `SIGKILL` to `clinfo`:

```
[776478.304963] cp queue preemption time out
[776478.304976] Resetting wave fronts (nocpsch) on dev 00000000b93ac3ea
[776478.305018] ------------[ cut here ]------------
[776478.305019] FW bug: No PASID in KFD interrupt
[776478.305199] WARNING: CPU: 5 PID: 3850510 at drivers/gpu/drm/amd/amdgpu/../amdkfd/cik_event_interrupt.c:70 cik_event_interrupt_isr+0x12b/0x140 [amdgpu]
[776478.305199] Modules linked in: snd_seq_dummy cp210x usbserial nls_iso8859_1 nls_utf8 isofs uas usb_storage bluetooth ecdh_generic ecc msr nf_tables nfnetlink ip6table_filter ip6_tables iptable_filter bpfilter aufs vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) overlay bridge stp llc binfmt_misc snd_usb_audio snd_usbmidi_lib joydev mc snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi edac_mce_amd snd_seq_midi snd_hda_intel kvm_amd snd_seq_midi_event snd_intel_dspcfg ccp snd_hda_codec input_leds kvm snd_hda_core eeepc_wmi asus_wmi snd_rawmidi serio_raw snd_hwdep sparse_keymap video snd_seq wmi_bmof k10temp snd_pcm fam15h_power snd_seq_device snd_timer snd soundcore mac_hid sch_fq_codel vhba(OE) it87 hwmon_vid nfsd parport_pc ppdev auth_rpcgss nfs_acl lp lockd parport grace sunrpc ip_tables x_tables autofs4 btrfs zstd_compress dm_crypt raid10 raid0 multipath linear raid1 bcache crc64 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq
[776478.305221]  libcrc32c hid_generic usbhid hid amdgpu crct10dif_pclmul crc32_pclmul amd_iommu_v2 gpu_sched ghash_clmulni_intel radeon aesni_intel crypto_simd i2c_algo_bit cryptd ttm glue_helper mxm_wmi drm_kms_helper syscopyarea sysfillrect sysimgblt r8169 fb_sys_fops realtek drm i2c_piix4 ahci libahci wmi
[776478.305231] CPU: 5 PID: 3850510 Comm: psensor Tainted: G           OE     5.4.0-38-generic #42-Ubuntu
[776478.305232] Hardware name: To be filled by O.E.M. To be filled by O.E.M./SABERTOOTH 990FX R2.0, BIOS 2501 04/08/2014
[776478.305285] RIP: 0010:cik_event_interrupt_isr+0x12b/0x140 [amdgpu]
[776478.305286] Code: ff ff 0f b6 05 02 99 29 00 84 c0 74 07 31 c0 e9 58 ff ff ff 48 c7 c7 80 8c eb c0 88 04 24 c6 05 e6 98 29 00 01 e8 80 b2 41 cc <0f> 0b 0f b6 04 24 e9 37 ff ff ff 66 2e 0f 1f 84 00 00 00 00 00 0f
[776478.305287] RSP: 0000:ffffa071c01ccd88 EFLAGS: 00010082
[776478.305288] RAX: 0000000000000000 RBX: ffff8c7f479ac800 RCX: 0000000000000000
[776478.305289] RDX: 0000000000000001 RSI: ffffffff8eb945c1 RDI: 0000000000000046
[776478.305289] RBP: ffffa071c01ccda8 R08: ffffffff8eb945a0 R09: 0000000000000021
[776478.305290] R10: 0000000000000000 R11: 0000000000000001 R12: ffffa071c06db6b0
[776478.305290] R13: 0000000000000087 R14: ffff8c7f479ac9d0 R15: ffffa071c01ccdd0
[776478.305291] FS:  00007f8c0d069d00(0000) GS:ffff8c7f5eb40000(0000) knlGS:0000000000000000
[776478.305292] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[776478.305292] CR2: 00002d947f62f000 CR3: 00000001a4ffa000 CR4: 00000000000406e0
[776478.305293] Call Trace:
[776478.305294]  <IRQ>
[776478.305348]  interrupt_is_wanted+0x19/0x20 [amdgpu]
[776478.305403]  kgd2kfd_interrupt+0xb0/0xf0 [amdgpu]
[776478.305447]  ? amdgpu_fence_process+0x46/0xe0 [amdgpu]
[776478.305498]  amdgpu_amdkfd_interrupt+0x1a/0x20 [amdgpu]
[776478.305547]  amdgpu_irq_dispatch+0xda/0x1e0 [amdgpu]
[776478.305595]  amdgpu_ih_process+0x8c/0x110 [amdgpu]
[776478.305644]  amdgpu_irq_handler+0x1f/0x50 [amdgpu]
[776478.305647]  __handle_irq_event_percpu+0x42/0x180
[776478.305648]  handle_irq_event_percpu+0x33/0x80
[776478.305649]  handle_irq_event+0x3b/0x5a
[776478.305650]  handle_edge_irq+0x93/0x1c0
[776478.305652]  do_IRQ+0x55/0xf0
[776478.305653]  common_interrupt+0xf/0xf
[776478.305654]  </IRQ>
[776478.305655] RIP: 0033:0x7f8c0d4c36c4
[776478.305656] Code: de 49 89 fc e9 88 fc ff ff 0f 1f 44 00 00 48 8b 7c 24 10 be 10 00 00 00 e8 69 f1 ff ff e9 9a fc ff ff 0f 1f 40 00 4c 8b 50 50 <89> cf 4d 85 d2 74 46 8b 78 30 48 8b 70 38 03 78 20 48 03 70 28 89
[776478.305657] RSP: 002b:00007fffb9ecce90 EFLAGS: 00000202 ORIG_RAX: ffffffffffffffd6
[776478.305658] RAX: 000055d14236e0c0 RBX: 00000000000000aa RCX: 000000000005789e
[776478.305658] RDX: 0000000080000000 RSI: 0000000000000577 RDI: 000055d141bf5388
[776478.305659] RBP: 000055d141bf5378 R08: 0000000000000000 R09: 0000000000000003
[776478.305659] R10: 000000002fbd7c00 R11: 0000000000000578 R12: 00000000000000aa
[776478.305659] R13: 000055d13fde1de0 R14: 000055d14236e380 R15: 0000000000000577
[776478.305661] ---[ end trace e0e84440a61d6ded ]---
```

This is the output of `rocminfo`:

```
ROCk module is loaded
Able to open /dev/kfd read-write
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD FX(tm)-9590 Eight-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD FX(tm)-9590 Eight-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      16384(0x4000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4700                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32849728(0x1f53f40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32849728(0x1f53f40) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Hawaii XT / Grenada XT [Radeon R9 290X/390X]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26544(0x67b0)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1080                               
  BDFID:                   256                                
  Internal Node ID:        1                                  
  Compute Unit:            44                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8388608(0x800000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             
```

Note that I'm able to get working both legacy's OpenCL from latest amdgpu-pro release (`amdgpu-pro-20.20-1089974-ubuntu-20.04`) without tricks and Clover (`libclc`) from Ubuntu packages at the same time without conflict.

Only the amdgpu-pro one has image support so it's still the only one working on Darktable for me, while both are usable by Luxmark.

I've noticed Blender listed only one device, so maybe only one implementation pleased it, I've not spent time to know which one.

I also noticed I was able to install both `pal` and `legacy` implementations at the same time without conflict. While only the `legacy` one works on my end, it means this command works for me and may also work for people using `pal` one:

```sh
./amdgpu-install --no-dkms --headless --opencl='pal,legacy'
```

I still don't have ROCm support, but at least I get a bunch of goodness with my Radeon R9 390X:

```
OpenCL:             1.1 (mesa/clover 20.0.8)
OpenCL:             2.1 (amd-app 3110.6)
OpenGL:             4.6 (mesa/radeonsi 20.0.8)
OpenGL ES:          3.2 (mesa/radeonsi 20.0.8)
Vulkan:             1.2.128/1.2.0.0 (mesa/radv 20.0.8)
Vulkan:             1.2.139/1.2.0.2 (amdvlk 2020.q2.4)
VA-API:             1.7 (libva 2.6.0)
```

Edit: anyway, while `clinfo` hangs while ROCm is installed, it at least prints `OpenCL 2.0 AMD-APP (3137.0)` as `Platform Version`, which is the ROCm one.

---

### 评论 #28 — illwieckz (2020-06-22T20:34:24Z)

So I re-read carefully the [README](https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md) file.

It says:

> ROCm officially supports AMD GPUs that use following chips:
> 
>   * GFX8 GPUs
>     * "Fiji" chips, such as on the AMD Radeon R9 Fury X and Radeon Instinct MI8
>     * "Polaris 10" chips, such as on the AMD Radeon RX 580 and Radeon Instinct MI6
>   * GFX9 GPUs
>     * "Vega 10" chips, such as on the AMD Radeon RX Vega 64 and Radeon Instinct MI25
>     * "Vega 7nm" chips, such as on the Radeon Instinct MI50, Radeon Instinct MI60 or AMD Radeon VII
> 
> The following list of GPUs are enabled in the ROCm software, though full support is not guaranteed:
> 
>   * GFX8 GPUs
>     * "Polaris 11" chips, such as on the AMD Radeon RX 570 and Radeon Pro WX 4100
>     * "Polaris 12" chips, such as on the AMD Radeon RX 550 and Radeon RX 540
>   * GFX7 GPUs
>     * "Hawaii" chips, such as the AMD Radeon R9 390X and FirePro W9100


But it also says:

> These releases of the upstream Linux kernel support the following GPUs in ROCm:
> 
>  * 4.17: Fiji, Polaris 10, Polaris 11
>  * 4.18: Fiji, Polaris 10, Polaris 11, Vega10
>  * 4.20: Fiji, Polaris 10, Polaris 11, Vega10, Vega 7nm

Maybe the issue we face is that the `rocm-dkms` Linux kernel module ships some fixes for Hawaii that was never upstreamed. The thing is that trying to use `rocm-dkms` usually brings more problems than fixes as it may not run properly on a given distro or not build at all.

I would like to know what I can do to make sure upstream kernel has required bits to make ROCm working with Hawaii.

Also, we may note the README also said this:

> Experimental support for our Hawaii (GFX7) GPUs (Radeon R9 290, R9 390, FirePro W9100, S9150, S9170)
> does not require or take advantage of PCIe Atomics. However, we still recommend that you use a CPU
> from the list provided above for compatibility purposes.

I don't have a CPU from the given list (my CPU predates Ryzen, it's an FX-9590 one), but I know I got ROCm working once with Hawaii on my CPU in the past.

The README also said on this topic, meaning my CPU should work:

> * ROCm 2.9.x should support PCIe 2.0 enabled CPUs such as the AMD Opteron, Phenom, Phenom II, Athlon, Athlon X2, Athlon II and older Intel Xeon and Intel Core Architecture and Pentium CPUs. However, we have done very limited testing on these configurations, since our test farm has been catering to CPUs listed above. This is where we need community support. _If you find problems on such setups, please report these issues_.

It's also possible there may be some regressions on that side too.

How to help to make sure potential issue on kernel driver or old CPU support is properly tracked down?

---

### 评论 #29 — illwieckz (2020-06-22T21:37:19Z)

So, I tried installing both `rock-dkms` and `rocm-dkms`, they installed properly, system booted properly, but `clinfo` still hangs.

What's interesting is that it hangs right after testing some atomic stuff, feature that is not supported by this system but not be required by that device:

```
  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Hawaii XT / Grenada XT [Radeon R9 290X/390X]
  Device Topology:				 PCI[ B#1, D#0, F#0 ]
  Max compute units:				 44
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1080Mhz
  Address bits:					 64
  Max memory allocation:			 7301444403
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26544
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 8589934592
  Constant buffer size:				 7301444403
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 3006477107
  Max global variable size:			 7301444403
  Max global variable preferred total size:	 8589934592
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
```

That is the `dmesg` quote when `clinfo` hangs:

```
[   59.941645] ------------[ cut here ]------------
[   59.941646] Load non-HWS mqd while stopped
[   59.941809] WARNING: CPU: 0 PID: 8491 at /var/lib/dkms/amdgpu/3.5-32/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
[   59.941809] Modules linked in: nf_tables nfnetlink ip6table_filter ip6_tables iptable_filter bpfilter aufs vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) overlay bridge stp llc binfmt_misc snd_usb_audio joydev snd_hda_codec_realtek snd_usbmidi_lib snd_hda_codec_generic ledtrig_audio edac_mce_amd mc snd_hda_codec_hdmi snd_seq_midi kvm_amd snd_seq_midi_event snd_hda_intel ccp snd_rawmidi snd_intel_dspcfg kvm input_leds snd_hda_codec serio_raw snd_hda_core snd_hwdep snd_seq eeepc_wmi asus_wmi snd_pcm sparse_keymap video wmi_bmof snd_seq_device fam15h_power k10temp snd_timer snd soundcore mac_hid sch_fq_codel vhba(OE) it87 hwmon_vid parport_pc ppdev nfsd lp auth_rpcgss parport nfs_acl lockd grace sunrpc ip_tables x_tables autofs4 btrfs zstd_compress dm_crypt raid10 raid0 multipath linear raid1 bcache crc64 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c hid_generic usbhid hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel amdgpu(OE) amd_iommu_v2
[   59.941830]  amd_sched(OE) amdttm(OE) aesni_intel crypto_simd cryptd glue_helper mxm_wmi amdkcl(OE) i2c_algo_bit drm_kms_helper syscopyarea sysfillrect r8169 sysimgblt fb_sys_fops realtek i2c_piix4 drm ahci libahci wmi
[   59.941838] CPU: 0 PID: 8491 Comm: clinfo Tainted: G           OE     5.4.0-38-generic #42-Ubuntu
[   59.941839] Hardware name: To be filled by O.E.M. To be filled by O.E.M./SABERTOOTH 990FX R2.0, BIOS 2501 04/08/2014
[   59.941899] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
[   59.941900] Code: 00 48 89 df e8 a2 ea ff ff e9 9e fd ff ff 80 3d 19 68 31 00 00 75 15 48 c7 c7 70 62 b6 c0 c6 05 09 68 31 00 01 e8 fc ee db c2 <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
[   59.941901] RSP: 0018:ffffb2d08a137bb8 EFLAGS: 00010286
[   59.941902] RAX: 0000000000000000 RBX: ffff9a0d87d98400 RCX: 0000000000000006
[   59.941902] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff9a0d9ea178c0
[   59.941903] RBP: ffffb2d08a137c08 R08: 00000000000005c9 R09: 0000000000000004
[   59.941903] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9a0ce2ece400
[   59.941904] R13: 0000000000000000 R14: ffff9a0d8a40be28 R15: ffff9a0d885f3080
[   59.941905] FS:  00007f16ef099740(0000) GS:ffff9a0d9ea00000(0000) knlGS:0000000000000000
[   59.941905] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   59.941906] CR2: 00007f16ab5a0b60 CR3: 00000006ff6b4000 CR4: 00000000000406f0
[   59.941907] Call Trace:
[   59.941969]  pqm_create_queue+0x182/0x450 [amdgpu]
[   59.942028]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
[   59.942087]  kfd_ioctl+0x252/0x460 [amdgpu]
[   59.942146]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
[   59.942149]  do_vfs_ioctl+0x407/0x670
[   59.942150]  ksys_ioctl+0x67/0x90
[   59.942151]  __x64_sys_ioctl+0x1a/0x20
[   59.942153]  do_syscall_64+0x57/0x190
[   59.942155]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[   59.942156] RIP: 0033:0x7f16eedb737b
[   59.942157] Code: 0f 1e fa 48 8b 05 15 3b 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d e5 3a 0d 00 f7 d8 64 89 01 48
[   59.942158] RSP: 002b:00007ffe6af04348 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[   59.942159] RAX: ffffffffffffffda RBX: 0000000000000003 RCX: 00007f16eedb737b
[   59.942159] RDX: 00007ffe6af043c0 RSI: 00000000c0584b02 RDI: 0000000000000009
[   59.942160] RBP: 00007ffe6af043c0 R08: 0000000002300000 R09: 0000000000080000
[   59.942161] R10: 0000000002212008 R11: 0000000000000246 R12: 00000000c0584b02
[   59.942161] R13: 0000000000000009 R14: 0000000002212000 R15: 0000000000000064
[   59.942162] ---[ end trace 512889cfd572c403 ]---
```

And this is `dmesg` quote when I kill `clinfo`:

```
[  398.895321] ------------[ cut here ]------------
[  398.895322] Destroy non-HWS queue while stopped
[  398.895484] WARNING: CPU: 2 PID: 8504 at /var/lib/dkms/amdgpu/3.5-32/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
[  398.895484] Modules linked in: nf_tables nfnetlink ip6table_filter ip6_tables iptable_filter bpfilter aufs vboxnetadp(OE) vboxnetflt(OE) vboxdrv(OE) overlay bridge stp llc binfmt_misc snd_usb_audio joydev snd_hda_codec_realtek snd_usbmidi_lib snd_hda_codec_generic ledtrig_audio edac_mce_amd mc snd_hda_codec_hdmi snd_seq_midi kvm_amd snd_seq_midi_event snd_hda_intel ccp snd_rawmidi snd_intel_dspcfg kvm input_leds snd_hda_codec serio_raw snd_hda_core snd_hwdep snd_seq eeepc_wmi asus_wmi snd_pcm sparse_keymap video wmi_bmof snd_seq_device fam15h_power k10temp snd_timer snd soundcore mac_hid sch_fq_codel vhba(OE) it87 hwmon_vid parport_pc ppdev nfsd lp auth_rpcgss parport nfs_acl lockd grace sunrpc ip_tables x_tables autofs4 btrfs zstd_compress dm_crypt raid10 raid0 multipath linear raid1 bcache crc64 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c hid_generic usbhid hid crct10dif_pclmul crc32_pclmul ghash_clmulni_intel amdgpu(OE) amd_iommu_v2
[  398.895505]  amd_sched(OE) amdttm(OE) aesni_intel crypto_simd cryptd glue_helper mxm_wmi amdkcl(OE) i2c_algo_bit drm_kms_helper syscopyarea sysfillrect r8169 sysimgblt fb_sys_fops realtek i2c_piix4 drm ahci libahci wmi
[  398.895512] CPU: 2 PID: 8504 Comm: clinfo:sh5 Tainted: G        W  OE     5.4.0-38-generic #42-Ubuntu
[  398.895513] Hardware name: To be filled by O.E.M. To be filled by O.E.M./SABERTOOTH 990FX R2.0, BIOS 2501 04/08/2014
[  398.895573] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
[  398.895575] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 89 79 31 00 00 75 e6 48 c7 c7 58 60 b6 c0 c6 05 79 79 31 00 01 e8 6d 00 dc c2 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
[  398.895575] RSP: 0018:ffffb2d089defb60 EFLAGS: 00010286
[  398.895576] RAX: 0000000000000000 RBX: ffff9a0ce2ece400 RCX: 0000000000000006
[  398.895577] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff9a0d9ea978c0
[  398.895577] RBP: ffffb2d089defb88 R08: 00000000000005ee R09: 0000000000000004
[  398.895578] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9a0d87d98400
[  398.895578] R13: ffff9a0d8a40be28 R14: 0000000000000000 R15: ffff9a0d885f3080
[  398.895579] FS:  00007f16ca7fc700(0000) GS:ffff9a0d9ea80000(0000) knlGS:0000000000000000
[  398.895580] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[  398.895581] CR2: 00007f8f6806e400 CR3: 00000006ff6b4000 CR4: 00000000000406e0
[  398.895581] Call Trace:
[  398.895643]  process_termination_nocpsch+0x71/0x160 [amdgpu]
[  398.895703]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
[  398.895762]  kfd_process_notifier_release+0x18a/0x200 [amdgpu]
[  398.895765]  __mmu_notifier_release+0x47/0xd0
[  398.895767]  exit_mmap+0x167/0x1b0
[  398.895769]  ? __switch_to_asm+0x34/0x70
[  398.895771]  ? _cond_resched+0x19/0x30
[  398.895772]  mmput+0x5d/0x130
[  398.895774]  do_exit+0x2fd/0xac0
[  398.895774]  ? _cond_resched+0x19/0x30
[  398.895776]  ? futex_wait_queue_me+0xcf/0x120
[  398.895778]  do_group_exit+0x47/0xb0
[  398.895779]  get_signal+0x169/0x890
[  398.895781]  do_signal+0x34/0x6c0
[  398.895782]  ? do_futex+0x10f/0x1e0
[  398.895784]  ? __x64_sys_futex+0x13f/0x170
[  398.895785]  exit_to_usermode_loop+0xbf/0x160
[  398.895786]  do_syscall_64+0x163/0x190
[  398.895787]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
[  398.895788] RIP: 0033:0x7f16eec88376
[  398.895790] Code: 44 24 60 0f 11 44 24 68 e8 97 38 00 00 e8 82 3c 00 00 89 de 45 31 d2 31 d2 41 89 c0 40 80 f6 80 4c 89 ff b8 ca 00 00 00 0f 05 <48> 3d 00 f0 ff ff 0f 87 26 01 00 00 44 89 c7 e8 b6 3c 00 00 31 f6
[  398.895790] RSP: 002b:00007f16ca7fbd10 EFLAGS: 00000282 ORIG_RAX: 00000000000000ca
[  398.895791] RAX: fffffffffffffe00 RBX: 0000000000000000 RCX: 00007f16eec88376
[  398.895792] RDX: 0000000000000000 RSI: 0000000000000080 RDI: 0000000001d63e90
[  398.895792] RBP: 0000000001d63e68 R08: 0000000000000000 R09: 0000000000000000
[  398.895793] R10: 0000000000000000 R11: 0000000000000282 R12: 0000000001d63e8c
[  398.895793] R13: 0000000001d63e40 R14: 00007f16ca7fbd50 R15: 0000000001d63e90
[  398.895795] ---[ end trace 512889cfd572c404 ]---
```

---

### 评论 #30 — illwieckz (2020-06-22T21:47:31Z)

> I believe I am able to reproduce this on my FirePro W9100 on an old Opteron 4386 (a system with the Hawaii GPU connected through PCIe gen 2).

> I'd still like to track this, since I was able to reproduce it once. As of ROCm 2.0,0. Hawaii is currently broken because of a bad firmware structure. We hope to have this fixed in our next release, and I can try to circle back to this issue.

@jlgreathouse, do you still have that PCIe 2.0 + Hawaii setup? In all case, how can I help you to track this?

---

### 评论 #31 — dagelf (2020-11-15T20:00:42Z)

If I simply swop out my R9 390 with any RX card, everything runs fine. But I don't own any RX cards, had to borrow them to test. 

_I've tried every single version of ROCm on every version of Ubuntu they support 16.04, 18.04 and now 20.04. Same issue. Locks up or crashes. On multiple CPU and motherboard combinations. Wasted countless days so far just trying to get it to work.

**If anyone has ever seen a R9 390 working please let me know exactly what version, what kernel**

It has literally been 4 years now that I've been trying. But just a day every other month. I have some large workflows that I need to run now. I bought 10 of these cards 4 years ago (!!!) to run workloads on... and have been held on a line by Readme's and message and issue threads now the whole time... not to mention the original marketing. it's been a really frustrating situation, I don't think I've been so patient about anything in my whole life. It's a lot of money that I've wasted... so far. Is it ever going to work? Should it? The docs says yes. So ... any help would be greatly appreciated._ 

I've come to realize that my motherboard and CPU are irrelevant, because I get the same crash as most of those above. On Ubuntu 20.04 with both ROCm 1.9 and 1.9.3 I get this:

```
Nov 15 16:26:19 x58a kernel: [ 3085.223218] ------------[ cut here ]------------
Nov 15 16:26:19 x58a kernel: [ 3085.223220] Load non-HWS mqd while stopped
Nov 15 16:26:19 x58a kernel: [ 3085.223331] WARNING: CPU: 2 PID: 5070 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 16:26:19 x58a kernel: [ 3085.223332] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core intel_powerclamp snd_hwdep coretemp amdgpu(OE) snd_pcm snd_seq_midi amd_iommu_v2 kvm_intel snd_seq_midi_event amd_sched(OE) amdttm(OE) cdc_ether kvm snd_rawmidi usbnet snd_seq mxm_wmi r8152 input_leds serio_raw amdkcl(OE) snd_seq_device intel_cstate drm_kms_helper snd_timer mii snd i2c_algo_bit fb_sys_fops syscopyarea sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 pata_jmicron lpc_ich ahci libahci wmi
Nov 15 16:26:19 x58a kernel: [ 3085.223352] CPU: 2 PID: 5070 Comm: clinfo Tainted: G          IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 16:26:19 x58a kernel: [ 3085.223352] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 16:26:19 x58a kernel: [ 3085.223408] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 16:26:19 x58a kernel: [ 3085.223409] Code: 00 48 89 df e8 62 ea ff ff e9 9e fd ff ff 80 3d d2 e9 38 00 00 75 15 48 c7 c7 40 a2 03 c1 c6 05 c2 e9 38 00 01 e8 9c a9 d4 f4 <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 16:26:19 x58a kernel: [ 3085.223409] RSP: 0018:ffff9854022b7bb8 EFLAGS: 00010286
Nov 15 16:26:19 x58a kernel: [ 3085.223410] RAX: 0000000000000000 RBX: ffff88fc9ac87c00 RCX: 0000000000000006
Nov 15 16:26:19 x58a kernel: [ 3085.223411] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff88fc9f8978c0
Nov 15 16:26:19 x58a kernel: [ 3085.223411] RBP: ffff9854022b7c08 R08: 0000000000000533 R09: 0000000000000004
Nov 15 16:26:19 x58a kernel: [ 3085.223412] R10: 0000000000000000 R11: 0000000000000001 R12: ffff88fc7278bc00
Nov 15 16:26:19 x58a kernel: [ 3085.223412] R13: 0000000000000000 R14: ffff88fc72789428 R15: ffff88fc96cc9700
Nov 15 16:26:19 x58a kernel: [ 3085.223413] FS:  00007f0c27614740(0000) GS:ffff88fc9f880000(0000) knlGS:0000000000000000
Nov 15 16:26:19 x58a kernel: [ 3085.223414] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 16:26:19 x58a kernel: [ 3085.223414] CR2: 00007f0c26c9be0c CR3: 00000003d611a000 CR4: 00000000000006e0
Nov 15 16:26:19 x58a kernel: [ 3085.223415] Call Trace:
Nov 15 16:26:19 x58a kernel: [ 3085.223472]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 16:26:19 x58a kernel: [ 3085.223525]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 16:26:19 x58a kernel: [ 3085.223579]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 16:26:19 x58a kernel: [ 3085.223632]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 16:26:19 x58a kernel: [ 3085.223635]  do_vfs_ioctl+0x407/0x670
Nov 15 16:26:19 x58a kernel: [ 3085.223636]  ksys_ioctl+0x67/0x90
Nov 15 16:26:19 x58a kernel: [ 3085.223637]  __x64_sys_ioctl+0x1a/0x20
Nov 15 16:26:19 x58a kernel: [ 3085.223639]  do_syscall_64+0x57/0x190
Nov 15 16:26:19 x58a kernel: [ 3085.223641]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 16:26:19 x58a kernel: [ 3085.223642] RIP: 0033:0x7f0c278aa50b
Nov 15 16:26:19 x58a kernel: [ 3085.223643] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 16:26:19 x58a kernel: [ 3085.223644] RSP: 002b:00007ffc77c67db8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 16:26:19 x58a kernel: [ 3085.223645] RAX: ffffffffffffffda RBX: 00007f0c26cb8210 RCX: 00007f0c278aa50b
Nov 15 16:26:19 x58a kernel: [ 3085.223645] RDX: 00007ffc77c67e30 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 16:26:19 x58a kernel: [ 3085.223646] RBP: 00007ffc77c67e30 R08: 0000000000000000 R09: 0000000000080000
Nov 15 16:26:19 x58a kernel: [ 3085.223646] R10: 000056450b3b1bf0 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 16:26:19 x58a kernel: [ 3085.223647] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 16:26:19 x58a kernel: [ 3085.223648] ---[ end trace 4a21876fc648ece0 ]---


Nov 15 16:29:45 x58a kernel: [ 3290.877132] ------------[ cut here ]------------
Nov 15 16:29:45 x58a kernel: [ 3290.877132] Evict when stopped
Nov 15 16:29:45 x58a kernel: [ 3290.877204] WARNING: CPU: 1 PID: 4070 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:781 evict_process_queues_nocpsch+0x190/0x1a0 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877205] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core intel_powerclamp snd_hwdep coretemp amdgpu(OE) snd_pcm snd_seq_midi amd_iommu_v2 kvm_intel snd_seq_midi_event amd_sched(OE) amdttm(OE) cdc_ether kvm snd_rawmidi usbnet snd_seq mxm_wmi r8152 input_leds serio_raw amdkcl(OE) snd_seq_device intel_cstate drm_kms_helper snd_timer mii snd i2c_algo_bit fb_sys_fops syscopyarea sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 pata_jmicron lpc_ich ahci libahci wmi
Nov 15 16:29:45 x58a kernel: [ 3290.877225] CPU: 1 PID: 4070 Comm: kworker/1:0 Tainted: G        W IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 16:29:45 x58a kernel: [ 3290.877225] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 16:29:45 x58a kernel: [ 3290.877228] Workqueue: events drm_sched_job_timedout [amd_sched]
Nov 15 16:29:45 x58a kernel: [ 3290.877286] RIP: 0010:evict_process_queues_nocpsch+0x190/0x1a0 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877287] Code: 00 01 e9 57 ff ff ff ba 02 00 00 00 eb c9 80 3d 4e f0 38 00 00 75 97 48 c7 c7 6e 3a 09 c1 c6 05 3e f0 38 00 01 e8 1b b0 d4 f4 <0f> 0b eb 80 66 66 2e 0f 1f 84 00 00 00 00 00 90 66 66 66 66 90 55
Nov 15 16:29:45 x58a kernel: [ 3290.877288] RSP: 0018:ffff985402bb7c80 EFLAGS: 00010282
Nov 15 16:29:45 x58a kernel: [ 3290.877289] RAX: 0000000000000000 RBX: ffff88fc7278bc00 RCX: 0000000000000006
Nov 15 16:29:45 x58a kernel: [ 3290.877289] RDX: 0000000000000007 RSI: 0000000000000092 RDI: ffff88fc9f8578c0
Nov 15 16:29:45 x58a kernel: [ 3290.877290] RBP: ffff985402bb7cb0 R08: 000000000000055f R09: 0000000000000004
Nov 15 16:29:45 x58a kernel: [ 3290.877290] R10: 0000000000000000 R11: 0000000000000001 R12: ffff88fc9ac87c00
Nov 15 16:29:45 x58a kernel: [ 3290.877291] R13: ffff88fc72789428 R14: 0000000000000000 R15: ffff88fc9ac87d28
Nov 15 16:29:45 x58a kernel: [ 3290.877292] FS:  0000000000000000(0000) GS:ffff88fc9f840000(0000) knlGS:0000000000000000
Nov 15 16:29:45 x58a kernel: [ 3290.877292] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 16:29:45 x58a kernel: [ 3290.877293] CR2: 00000694275a9410 CR3: 0000000015c0a000 CR4: 00000000000006e0
Nov 15 16:29:45 x58a kernel: [ 3290.877294] Call Trace:
Nov 15 16:29:45 x58a kernel: [ 3290.877352]  kfd_process_evict_queues+0x43/0x70 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877409]  kfd_suspend_all_processes+0x56/0xd0 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877464]  kgd2kfd_suspend.part.0+0x46/0x50 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877519]  kgd2kfd_pre_reset+0x47/0x60 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877574]  amdgpu_amdkfd_pre_reset+0x1a/0x20 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877640]  amdgpu_device_gpu_recover.cold+0x3ce/0xfa2 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877655]  ? drm_err+0x72/0x90 [drm]
Nov 15 16:29:45 x58a kernel: [ 3290.877715]  amdgpu_job_timedout+0x123/0x150 [amdgpu]
Nov 15 16:29:45 x58a kernel: [ 3290.877717]  drm_sched_job_timedout+0x72/0xc0 [amd_sched]
Nov 15 16:29:45 x58a kernel: [ 3290.877719]  process_one_work+0x1eb/0x3b0
Nov 15 16:29:45 x58a kernel: [ 3290.877721]  worker_thread+0x4d/0x400
Nov 15 16:29:45 x58a kernel: [ 3290.877723]  kthread+0x104/0x140
Nov 15 16:29:45 x58a kernel: [ 3290.877724]  ? process_one_work+0x3b0/0x3b0
Nov 15 16:29:45 x58a kernel: [ 3290.877724]  ? kthread_park+0x90/0x90
Nov 15 16:29:45 x58a kernel: [ 3290.877727]  ret_from_fork+0x35/0x40
Nov 15 16:29:45 x58a kernel: [ 3290.877728] ---[ end trace 4a21876fc648ece1 ]---


Nov 15 16:31:01 x58a kernel: [ 3366.845967] ------------[ cut here ]------------
Nov 15 16:31:01 x58a kernel: [ 3366.845969] Destroy non-HWS queue while stopped
Nov 15 16:31:01 x58a kernel: [ 3366.846197] WARNING: CPU: 4 PID: 5070 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 16:31:01 x58a kernel: [ 3366.846197] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core intel_powerclamp snd_hwdep coretemp amdgpu(OE) snd_pcm snd_seq_midi amd_iommu_v2 kvm_intel snd_seq_midi_event amd_sched(OE) amdttm(OE) cdc_ether kvm snd_rawmidi usbnet snd_seq mxm_wmi r8152 input_leds serio_raw amdkcl(OE) snd_seq_device intel_cstate drm_kms_helper snd_timer mii snd i2c_algo_bit fb_sys_fops syscopyarea sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 pata_jmicron lpc_ich ahci libahci wmi
Nov 15 16:31:01 x58a kernel: [ 3366.846226] CPU: 4 PID: 5070 Comm: clinfo Tainted: G        W IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 16:31:01 x58a kernel: [ 3366.846227] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 16:31:01 x58a kernel: [ 3366.846315] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 16:31:01 x58a kernel: [ 3366.846317] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 9f 03 c1 c6 05 72 fb 38 00 01 e8 4d bb d4 f4 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 16:31:01 x58a kernel: [ 3366.846317] RSP: 0018:ffff9854022b7b60 EFLAGS: 00010286
Nov 15 16:31:01 x58a kernel: [ 3366.846319] RAX: 0000000000000000 RBX: ffff88fc7278bc00 RCX: 0000000000000006
Nov 15 16:31:01 x58a kernel: [ 3366.846320] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff88fc9f9178c0
Nov 15 16:31:01 x58a kernel: [ 3366.846321] RBP: ffff9854022b7b88 R08: 00000000000005a2 R09: 0000000000000004
Nov 15 16:31:01 x58a kernel: [ 3366.846321] R10: 0000000000000000 R11: 0000000000000001 R12: ffff88fc9ac87c00
Nov 15 16:31:01 x58a kernel: [ 3366.846322] R13: ffff88fc72789428 R14: 0000000000000000 R15: ffff88fc96cc9700
Nov 15 16:31:01 x58a kernel: [ 3366.846324] FS:  00007f0c27614740(0000) GS:ffff88fc9f900000(0000) knlGS:0000000000000000
Nov 15 16:31:01 x58a kernel: [ 3366.846325] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 16:31:01 x58a kernel: [ 3366.846326] CR2: 00007f06bad719d0 CR3: 00000003d611a000 CR4: 00000000000006e0
Nov 15 16:31:01 x58a kernel: [ 3366.846326] Call Trace:
Nov 15 16:31:01 x58a kernel: [ 3366.846419]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 16:31:01 x58a kernel: [ 3366.846503]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 16:31:01 x58a kernel: [ 3366.846583]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 16:31:01 x58a kernel: [ 3366.846588]  __mmu_notifier_release+0x47/0xd0
Nov 15 16:31:01 x58a kernel: [ 3366.846590]  exit_mmap+0x16c/0x1b0
Nov 15 16:31:01 x58a kernel: [ 3366.846594]  ? do_futex+0x160/0x1e0
Nov 15 16:31:01 x58a kernel: [ 3366.846596]  ? _cond_resched+0x19/0x30
Nov 15 16:31:01 x58a kernel: [ 3366.846599]  mmput+0x5d/0x130
Nov 15 16:31:01 x58a kernel: [ 3366.846601]  do_exit+0x306/0xac0
Nov 15 16:31:01 x58a kernel: [ 3366.846604]  ? __switch_to_asm+0x40/0x70
Nov 15 16:31:01 x58a kernel: [ 3366.846605]  do_group_exit+0x47/0xb0
Nov 15 16:31:01 x58a kernel: [ 3366.846609]  get_signal+0x169/0x890
Nov 15 16:31:01 x58a kernel: [ 3366.846610]  ? __cgroup_account_cputime+0x28/0x30
Nov 15 16:31:01 x58a kernel: [ 3366.846613]  do_signal+0x34/0x6c0
Nov 15 16:31:01 x58a kernel: [ 3366.846615]  ? reschedule_interrupt+0xa/0x20
Nov 15 16:31:01 x58a kernel: [ 3366.846618]  exit_to_usermode_loop+0xbf/0x160
Nov 15 16:31:01 x58a kernel: [ 3366.846619]  do_syscall_64+0x163/0x190
Nov 15 16:31:01 x58a kernel: [ 3366.846621]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 16:31:01 x58a kernel: [ 3366.846622] RIP: 0033:0x7f0c2789889b
Nov 15 16:31:01 x58a kernel: [ 3366.846624] Code: 73 01 c3 48 8b 0d f5 55 0e 00 f7 d8 64 89 01 48 83 c8 ff c3 66 2e 0f 1f 84 00 00 00 00 00 90 f3 0f 1e fa b8 18 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d c5 55 0e 00 f7 d8 64 89 01 48
Nov 15 16:31:01 x58a kernel: [ 3366.846624] RSP: 002b:00007ffc77c68258 EFLAGS: 00000246 ORIG_RAX: 0000000000000018
Nov 15 16:31:01 x58a kernel: [ 3366.846626] RAX: 0000000000000000 RBX: 000056450b4a2510 RCX: 00007f0c2789889b
Nov 15 16:31:01 x58a kernel: [ 3366.846627] RDX: 0000000001004000 RSI: 0000000000000010 RDI: 000056450b4a2510
Nov 15 16:31:01 x58a kernel: [ 3366.846627] RBP: 0000000000000000 R08: 0000000000000000 R09: 000056450b4165f0
Nov 15 16:31:01 x58a kernel: [ 3366.846628] R10: 0000000000000000 R11: 0000000000000246 R12: 00007f0c26f06e40
Nov 15 16:31:01 x58a kernel: [ 3366.846629] R13: 0000000001100000 R14: 000056450b4a2510 R15: 00007f0c26ef0c10
Nov 15 16:31:01 x58a kernel: [ 3366.846631] ---[ end trace 4a21876fc648ece2 ]---


Nov 15 16:43:38 x58a kernel: [  560.677879] ------------[ cut here ]------------
Nov 15 16:43:38 x58a kernel: [  560.677881] Load non-HWS mqd while stopped
Nov 15 16:43:38 x58a kernel: [  560.678085] WARNING: CPU: 6 PID: 9977 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 16:43:38 x58a kernel: [  560.678086] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core snd_hwdep snd_pcm amdgpu(OE) snd_seq_midi snd_seq_midi_event intel_powerclamp amd_iommu_v2 snd_rawmidi coretemp amd_sched(OE) amdttm(OE) snd_seq kvm_intel cdc_ether amdkcl(OE) kvm usbnet drm_kms_helper input_leds snd_seq_device serio_raw r8152 intel_cstate snd_timer mxm_wmi i2c_algo_bit fb_sys_fops snd syscopyarea mii sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 lpc_ich pata_jmicron ahci libahci wmi
Nov 15 16:43:38 x58a kernel: [  560.678111] CPU: 6 PID: 9977 Comm: ocl-tester Tainted: G          IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 16:43:38 x58a kernel: [  560.678111] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 16:43:38 x58a kernel: [  560.678183] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 16:43:38 x58a kernel: [  560.678185] Code: 00 48 89 df e8 62 ea ff ff e9 9e fd ff ff 80 3d d2 e9 38 00 00 75 15 48 c7 c7 40 72 dc c0 c6 05 c2 e9 38 00 01 e8 9c d9 9b d3 <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 16:43:38 x58a kernel: [  560.678186] RSP: 0018:ffffad7a41ec7bb8 EFLAGS: 00010286
Nov 15 16:43:38 x58a kernel: [  560.678187] RAX: 0000000000000000 RBX: ffff89bd16f47000 RCX: 0000000000000006
Nov 15 16:43:38 x58a kernel: [  560.678188] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff89bd1f9978c0
Nov 15 16:43:38 x58a kernel: [  560.678188] RBP: ffffad7a41ec7c08 R08: 0000000000000535 R09: 0000000000000004
Nov 15 16:43:38 x58a kernel: [  560.678189] R10: 0000000000000000 R11: 0000000000000001 R12: ffff89bced2a5a00
Nov 15 16:43:38 x58a kernel: [  560.678190] R13: 0000000000000000 R14: ffff89bd13107c28 R15: ffff89bd16d55000
Nov 15 16:43:38 x58a kernel: [  560.678191] FS:  00007f8623b85000(0000) GS:ffff89bd1f980000(0000) knlGS:0000000000000000
Nov 15 16:43:38 x58a kernel: [  560.678192] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 16:43:38 x58a kernel: [  560.678193] CR2: 00007f8623209e0c CR3: 00000003345ce000 CR4: 00000000000006e0
Nov 15 16:43:38 x58a kernel: [  560.678194] Call Trace:
Nov 15 16:43:38 x58a kernel: [  560.678271]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 16:43:38 x58a kernel: [  560.678344]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 16:43:38 x58a kernel: [  560.678418]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 16:43:38 x58a kernel: [  560.678491]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 16:43:38 x58a kernel: [  560.678495]  do_vfs_ioctl+0x407/0x670
Nov 15 16:43:38 x58a kernel: [  560.678496]  ksys_ioctl+0x67/0x90
Nov 15 16:43:38 x58a kernel: [  560.678498]  __x64_sys_ioctl+0x1a/0x20
Nov 15 16:43:38 x58a kernel: [  560.678500]  do_syscall_64+0x57/0x190
Nov 15 16:43:38 x58a kernel: [  560.678503]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 16:43:38 x58a kernel: [  560.678505] RIP: 0033:0x7f8623e1750b
Nov 15 16:43:38 x58a kernel: [  560.678506] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 16:43:38 x58a kernel: [  560.678507] RSP: 002b:00007ffc7bdaad08 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 16:43:38 x58a kernel: [  560.678508] RAX: ffffffffffffffda RBX: 00007f8623226210 RCX: 00007f8623e1750b
Nov 15 16:43:38 x58a kernel: [  560.678509] RDX: 00007ffc7bdaad80 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 16:43:38 x58a kernel: [  560.678509] RBP: 00007ffc7bdaad80 R08: 0000000000000000 R09: 0000000000080000
Nov 15 16:43:38 x58a kernel: [  560.678510] R10: 00005569aa10cee0 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 16:43:38 x58a kernel: [  560.678511] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 16:43:38 x58a kernel: [  560.678513] ---[ end trace 1b75b3e07244fc29 ]---



Nov 15 17:13:24 x58a kernel: [ 2346.627465] ------------[ cut here ]------------
Nov 15 17:13:24 x58a kernel: [ 2346.627467] Destroy non-HWS queue while stopped
Nov 15 17:13:24 x58a kernel: [ 2346.627674] WARNING: CPU: 6 PID: 9977 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 17:13:24 x58a kernel: [ 2346.627675] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core snd_hwdep snd_pcm amdgpu(OE) snd_seq_midi snd_seq_midi_event intel_powerclamp amd_iommu_v2 snd_rawmidi coretemp amd_sched(OE) amdttm(OE) snd_seq kvm_intel cdc_ether amdkcl(OE) kvm usbnet drm_kms_helper input_leds snd_seq_device serio_raw r8152 intel_cstate snd_timer mxm_wmi i2c_algo_bit fb_sys_fops snd syscopyarea mii sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 lpc_ich pata_jmicron ahci libahci wmi
Nov 15 17:13:24 x58a kernel: [ 2346.627708] CPU: 6 PID: 9977 Comm: ocl-tester Tainted: G        W IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 17:13:24 x58a kernel: [ 2346.627709] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 17:13:24 x58a kernel: [ 2346.627809] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 17:13:24 x58a kernel: [ 2346.627811] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 6f dc c0 c6 05 72 fb 38 00 01 e8 4d eb 9b d3 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 17:13:24 x58a kernel: [ 2346.627812] RSP: 0018:ffffad7a41ec7b60 EFLAGS: 00010286
Nov 15 17:13:24 x58a kernel: [ 2346.627813] RAX: 0000000000000000 RBX: ffff89bced2a5a00 RCX: 0000000000000006
Nov 15 17:13:24 x58a kernel: [ 2346.627814] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff89bd1f9978c0
Nov 15 17:13:24 x58a kernel: [ 2346.627815] RBP: ffffad7a41ec7b88 R08: 000000000000056a R09: 0000000000000004
Nov 15 17:13:24 x58a kernel: [ 2346.627816] R10: 0000000000000000 R11: 0000000000000001 R12: ffff89bd16f47000
Nov 15 17:13:24 x58a kernel: [ 2346.627817] R13: ffff89bd13107c28 R14: 0000000000000000 R15: ffff89bd16d55000
Nov 15 17:13:24 x58a kernel: [ 2346.627819] FS:  00007f8623b85000(0000) GS:ffff89bd1f980000(0000) knlGS:0000000000000000
Nov 15 17:13:24 x58a kernel: [ 2346.627820] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 17:13:24 x58a kernel: [ 2346.627821] CR2: 00007f0a8041f008 CR3: 00000003345ce000 CR4: 00000000000006e0
Nov 15 17:13:24 x58a kernel: [ 2346.627822] Call Trace:
Nov 15 17:13:24 x58a kernel: [ 2346.627922]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 17:13:24 x58a kernel: [ 2346.628026]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 17:13:24 x58a kernel: [ 2346.628127]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 17:13:24 x58a kernel: [ 2346.628131]  __mmu_notifier_release+0x47/0xd0
Nov 15 17:13:24 x58a kernel: [ 2346.628133]  exit_mmap+0x16c/0x1b0
Nov 15 17:13:24 x58a kernel: [ 2346.628137]  ? _cond_resched+0x19/0x30
Nov 15 17:13:24 x58a kernel: [ 2346.628140]  mmput+0x5d/0x130
Nov 15 17:13:24 x58a kernel: [ 2346.628142]  do_exit+0x306/0xac0
Nov 15 17:13:24 x58a kernel: [ 2346.628145]  ? __switch_to_asm+0x40/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628146]  ? __switch_to_asm+0x34/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628148]  ? __switch_to_asm+0x40/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628149]  ? __switch_to_asm+0x40/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628151]  do_group_exit+0x47/0xb0
Nov 15 17:13:24 x58a kernel: [ 2346.628154]  get_signal+0x169/0x890
Nov 15 17:13:24 x58a kernel: [ 2346.628156]  ? __switch_to_asm+0x34/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628158]  ? __switch_to_asm+0x40/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628160]  ? __switch_to_asm+0x34/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628161]  ? __switch_to_asm+0x34/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628164]  do_signal+0x34/0x6c0
Nov 15 17:13:24 x58a kernel: [ 2346.628166]  ? __switch_to_asm+0x40/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628167]  ? __switch_to_asm+0x34/0x70
Nov 15 17:13:24 x58a kernel: [ 2346.628169]  ? __cgroup_account_cputime+0x28/0x30
Nov 15 17:13:24 x58a kernel: [ 2346.628171]  ? sched_clock_cpu+0x11/0xb0
Nov 15 17:13:24 x58a kernel: [ 2346.628174]  exit_to_usermode_loop+0xbf/0x160
Nov 15 17:13:24 x58a kernel: [ 2346.628176]  do_syscall_64+0x163/0x190
Nov 15 17:13:24 x58a kernel: [ 2346.628178]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 17:13:24 x58a kernel: [ 2346.628179] RIP: 0033:0x7f8623e0589b
Nov 15 17:13:24 x58a kernel: [ 2346.628181] Code: 73 01 c3 48 8b 0d f5 55 0e 00 f7 d8 64 89 01 48 83 c8 ff c3 66 2e 0f 1f 84 00 00 00 00 00 90 f3 0f 1e fa b8 18 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d c5 55 0e 00 f7 d8 64 89 01 48
Nov 15 17:13:24 x58a kernel: [ 2346.628182] RSP: 002b:00007ffc7bdab1a8 EFLAGS: 00000246 ORIG_RAX: 0000000000000018
Nov 15 17:13:24 x58a kernel: [ 2346.628184] RAX: 0000000000000000 RBX: 00005569aa2b99c0 RCX: 00007f8623e0589b
Nov 15 17:13:24 x58a kernel: [ 2346.628185] RDX: 0000000001004000 RSI: 0000000000000010 RDI: 00005569aa2b99c0
Nov 15 17:13:24 x58a kernel: [ 2346.628186] RBP: 0000000000000000 R08: 0000000000000000 R09: 00005569aa171f10
Nov 15 17:13:24 x58a kernel: [ 2346.628187] R10: 0000000000000000 R11: 0000000000000246 R12: 00007f8623474e40
Nov 15 17:13:24 x58a kernel: [ 2346.628188] R13: 0000000001100000 R14: 00005569aa2b99c0 R15: 00007f862345ec10
Nov 15 17:13:24 x58a kernel: [ 2346.628190] ---[ end trace 1b75b3e07244fc2a ]---


Nov 15 18:04:37 x58a kernel: [   34.510600] ------------[ cut here ]------------
Nov 15 18:04:37 x58a kernel: [   34.510601] Load non-HWS mqd while stopped
Nov 15 18:04:37 x58a kernel: [   34.510732] WARNING: CPU: 6 PID: 3802 at /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 18:04:37 x58a kernel: [   34.510733] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core amdgpu(OE) snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi amd_iommu_v2 amd_sched(OE) intel_powerclamp cdc_ether amdttm(OE) snd_seq usbnet coretemp r8152 snd_seq_device amdkcl(OE) kvm_intel snd_timer drm_kms_helper mii kvm i2c_algo_bit snd fb_sys_fops syscopyarea input_leds mxm_wmi intel_cstate soundcore sysfillrect serio_raw i7core_edac sysimgblt mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich lpc_ich i2c_i801 pata_jmicron ahci libahci wmi
Nov 15 18:04:37 x58a kernel: [   34.510753] CPU: 6 PID: 3802 Comm: hashcat Tainted: G          IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 18:04:37 x58a kernel: [   34.510753] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 18:04:37 x58a kernel: [   34.510811] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 18:04:37 x58a kernel: [   34.510813] Code: 00 48 89 df e8 62 ea ff ff e9 9e fd ff ff 80 3d d2 e9 38 00 00 75 15 48 c7 c7 40 62 fa c0 c6 05 c2 e9 38 00 01 e8 9c e9 5d ee <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 18:04:37 x58a kernel: [   34.510813] RSP: 0018:ffffb81b81053bb8 EFLAGS: 00010286
Nov 15 18:04:37 x58a kernel: [   34.510814] RAX: 0000000000000000 RBX: ffff9cd5974e0800 RCX: 0000000000000006
Nov 15 18:04:37 x58a kernel: [   34.510815] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff9cd59f9978c0
Nov 15 18:04:37 x58a kernel: [   34.510815] RBP: ffffb81b81053c08 R08: 0000000000000563 R09: 0000000000000004
Nov 15 18:04:37 x58a kernel: [   34.510816] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9cd570d24600
Nov 15 18:04:37 x58a kernel: [   34.510816] R13: 0000000000000000 R14: ffff9cd570f69428 R15: ffff9cd59a564c00
Nov 15 18:04:37 x58a kernel: [   34.510817] FS:  00007f3e0665f700(0000) GS:ffff9cd59f980000(0000) knlGS:0000000000000000
Nov 15 18:04:37 x58a kernel: [   34.510818] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 18:04:37 x58a kernel: [   34.510818] CR2: 00007f3df4001018 CR3: 00000003da286000 CR4: 00000000000006e0
Nov 15 18:04:37 x58a kernel: [   34.510819] Call Trace:
Nov 15 18:04:37 x58a kernel: [   34.510878]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 18:04:37 x58a kernel: [   34.510934]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 18:04:37 x58a kernel: [   34.510990]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 18:04:37 x58a kernel: [   34.511046]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 18:04:37 x58a kernel: [   34.511049]  do_vfs_ioctl+0x407/0x670
Nov 15 18:04:37 x58a kernel: [   34.511050]  ksys_ioctl+0x67/0x90
Nov 15 18:04:37 x58a kernel: [   34.511051]  __x64_sys_ioctl+0x1a/0x20
Nov 15 18:04:37 x58a kernel: [   34.511053]  do_syscall_64+0x57/0x190
Nov 15 18:04:37 x58a kernel: [   34.511056]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 18:04:37 x58a kernel: [   34.511057] RIP: 0033:0x7f3e1354850b
Nov 15 18:04:37 x58a kernel: [   34.511058] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 18:04:37 x58a kernel: [   34.511058] RSP: 002b:00007f3e0665e3d8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 18:04:37 x58a kernel: [   34.511059] RAX: ffffffffffffffda RBX: 00007f3e07700210 RCX: 00007f3e1354850b
Nov 15 18:04:37 x58a kernel: [   34.511060] RDX: 00007f3e0665e450 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 18:04:37 x58a kernel: [   34.511060] RBP: 00007f3e0665e450 R08: 0000000000000000 R09: 0000000000080000
Nov 15 18:04:37 x58a kernel: [   34.511061] R10: 000055c110fa0920 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 18:04:37 x58a kernel: [   34.511061] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 18:04:37 x58a kernel: [   34.511063] ---[ end trace a8af1ce8799332f9 ]---


Nov 15 18:11:13 x58a kernel: [  430.739110] ------------[ cut here ]------------
Nov 15 18:11:13 x58a kernel: [  430.739111] Destroy non-HWS queue while stopped
Nov 15 18:11:13 x58a kernel: [  430.739218] WARNING: CPU: 2 PID: 3797 at /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 18:11:13 x58a kernel: [  430.739219] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core amdgpu(OE) snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi amd_iommu_v2 amd_sched(OE) intel_powerclamp cdc_ether amdttm(OE) snd_seq usbnet coretemp r8152 snd_seq_device amdkcl(OE) kvm_intel snd_timer drm_kms_helper mii kvm i2c_algo_bit snd fb_sys_fops syscopyarea input_leds mxm_wmi intel_cstate soundcore sysfillrect serio_raw i7core_edac sysimgblt mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich lpc_ich i2c_i801 pata_jmicron ahci libahci wmi
Nov 15 18:11:13 x58a kernel: [  430.739240] CPU: 2 PID: 3797 Comm: hashcat Tainted: G        W IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 18:11:13 x58a kernel: [  430.739240] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 18:11:13 x58a kernel: [  430.739298] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 18:11:13 x58a kernel: [  430.739299] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 5f fa c0 c6 05 72 fb 38 00 01 e8 4d fb 5d ee <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 18:11:13 x58a kernel: [  430.739300] RSP: 0018:ffffb81b81d3fb60 EFLAGS: 00010286
Nov 15 18:11:13 x58a kernel: [  430.739301] RAX: 0000000000000000 RBX: ffff9cd53c62a600 RCX: 0000000000000006
Nov 15 18:11:13 x58a kernel: [  430.739301] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff9cd59f8978c0
Nov 15 18:11:13 x58a kernel: [  430.739302] RBP: ffffb81b81d3fb88 R08: 00000000000005a5 R09: 0000000000000004
Nov 15 18:11:13 x58a kernel: [  430.739303] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9cd5974e0800
Nov 15 18:11:13 x58a kernel: [  430.739303] R13: ffff9cd570f69428 R14: 0000000000000000 R15: ffff9cd59a564c00
Nov 15 18:11:13 x58a kernel: [  430.739304] FS:  00007f3e1342fb80(0000) GS:ffff9cd59f880000(0000) knlGS:0000000000000000
Nov 15 18:11:13 x58a kernel: [  430.739305] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 18:11:13 x58a kernel: [  430.739305] CR2: 000056222dd49484 CR3: 00000002ada0a000 CR4: 00000000000006e0
Nov 15 18:11:13 x58a kernel: [  430.739306] Call Trace:
Nov 15 18:11:13 x58a kernel: [  430.739365]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 18:11:13 x58a kernel: [  430.739422]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 18:11:13 x58a kernel: [  430.739478]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 18:11:13 x58a kernel: [  430.739481]  __mmu_notifier_release+0x47/0xd0
Nov 15 18:11:13 x58a kernel: [  430.739483]  exit_mmap+0x16c/0x1b0
Nov 15 18:11:13 x58a kernel: [  430.739485]  ? do_futex+0x160/0x1e0
Nov 15 18:11:13 x58a kernel: [  430.739487]  ? _cond_resched+0x19/0x30
Nov 15 18:11:13 x58a kernel: [  430.739489]  mmput+0x5d/0x130
Nov 15 18:11:13 x58a kernel: [  430.739490]  do_exit+0x306/0xac0
Nov 15 18:11:13 x58a kernel: [  430.739492]  ? hrtimer_try_to_cancel+0x85/0x110
Nov 15 18:11:13 x58a kernel: [  430.739493]  do_group_exit+0x47/0xb0
Nov 15 18:11:13 x58a kernel: [  430.739495]  get_signal+0x169/0x890
Nov 15 18:11:13 x58a kernel: [  430.739495]  ? hrtimer_init_sleeper+0x90/0x90
Nov 15 18:11:13 x58a kernel: [  430.739498]  do_signal+0x34/0x6c0
Nov 15 18:11:13 x58a kernel: [  430.739499]  ? do_futex+0x10f/0x1e0
Nov 15 18:11:13 x58a kernel: [  430.739500]  ? __x64_sys_futex+0x13f/0x170
Nov 15 18:11:13 x58a kernel: [  430.739502]  exit_to_usermode_loop+0xbf/0x160
Nov 15 18:11:13 x58a kernel: [  430.739503]  do_syscall_64+0x163/0x190
Nov 15 18:11:13 x58a kernel: [  430.739504]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 18:11:13 x58a kernel: [  430.739505] RIP: 0033:0x7f3e1378b618
Nov 15 18:11:13 x58a kernel: [  430.739508] Code: Bad RIP value.
Nov 15 18:11:13 x58a kernel: [  430.739509] RSP: 002b:00007fff24cce1f0 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
Nov 15 18:11:13 x58a kernel: [  430.739510] RAX: fffffffffffffdfc RBX: 00007fff24cce290 RCX: 00007f3e1378b618
Nov 15 18:11:13 x58a kernel: [  430.739510] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055c110f2c9d8
Nov 15 18:11:13 x58a kernel: [  430.739511] RBP: 000055c110f2c9d8 R08: 0000000000000000 R09: 00000000ffffffff
Nov 15 18:11:13 x58a kernel: [  430.739511] R10: 00007fff24cce290 R11: 0000000000000246 R12: 0000000000000000
Nov 15 18:11:13 x58a kernel: [  430.739512] R13: 0000000000000000 R14: fffffffeffffffff R15: 0000000000040000
Nov 15 18:11:13 x58a kernel: [  430.739513] ---[ end trace a8af1ce8799332fa ]---



Nov 15 18:24:20 x58a kernel: [   29.688228] ------------[ cut here ]------------
Nov 15 18:24:20 x58a kernel: [   29.688229] Load non-HWS mqd while stopped
Nov 15 18:24:20 x58a kernel: [   29.688337] WARNING: CPU: 3 PID: 3800 at /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 18:24:20 x58a kernel: [   29.688337] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core amdgpu(OE) snd_hwdep snd_pcm intel_powerclamp amd_iommu_v2 coretemp amd_sched(OE) snd_seq_midi amdttm(OE) snd_seq_midi_event kvm_intel cdc_ether snd_rawmidi amdkcl(OE) kvm usbnet snd_seq drm_kms_helper r8152 intel_cstate snd_seq_device i2c_algo_bit mxm_wmi snd_timer fb_sys_fops input_leds serio_raw mii snd syscopyarea sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid gpio_ich pata_acpi i2c_i801 lpc_ich pata_jmicron ahci libahci wmi
Nov 15 18:24:20 x58a kernel: [   29.688358] CPU: 3 PID: 3800 Comm: clinfo Tainted: G          IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 18:24:20 x58a kernel: [   29.688358] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 18:24:20 x58a kernel: [   29.688414] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 18:24:20 x58a kernel: [   29.688415] Code: 00 48 89 df e8 62 ea ff ff e9 9e fd ff ff 80 3d d2 e9 38 00 00 75 15 48 c7 c7 40 92 e5 c0 c6 05 c2 e9 38 00 01 e8 9c b9 72 c6 <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 18:24:20 x58a kernel: [   29.688415] RSP: 0018:ffffa9f2c1ad3bb8 EFLAGS: 00010286
Nov 15 18:24:20 x58a kernel: [   29.688416] RAX: 0000000000000000 RBX: ffff92bdd20ac400 RCX: 0000000000000006
Nov 15 18:24:20 x58a kernel: [   29.688417] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff92bddf8d78c0
Nov 15 18:24:20 x58a kernel: [   29.688417] RBP: ffffa9f2c1ad3c08 R08: 0000000000000513 R09: 0000000000000004
Nov 15 18:24:20 x58a kernel: [   29.688418] R10: 0000000000000000 R11: 0000000000000001 R12: ffff92bd9106f000
Nov 15 18:24:20 x58a kernel: [   29.688418] R13: 0000000000000000 R14: ffff92bd9106d628 R15: ffff92bdd34fb280
Nov 15 18:24:20 x58a kernel: [   29.688419] FS:  00007f6724062740(0000) GS:ffff92bddf8c0000(0000) knlGS:0000000000000000
Nov 15 18:24:20 x58a kernel: [   29.688420] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 18:24:20 x58a kernel: [   29.688420] CR2: 00007f67236e9e0c CR3: 00000003f312e000 CR4: 00000000000006e0
Nov 15 18:24:20 x58a kernel: [   29.688421] Call Trace:
Nov 15 18:24:20 x58a kernel: [   29.688478]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 18:24:20 x58a kernel: [   29.688531]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 18:24:20 x58a kernel: [   29.688585]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 18:24:20 x58a kernel: [   29.688638]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 18:24:20 x58a kernel: [   29.688641]  do_vfs_ioctl+0x407/0x670
Nov 15 18:24:20 x58a kernel: [   29.688642]  ksys_ioctl+0x67/0x90
Nov 15 18:24:20 x58a kernel: [   29.688643]  __x64_sys_ioctl+0x1a/0x20
Nov 15 18:24:20 x58a kernel: [   29.688645]  do_syscall_64+0x57/0x190
Nov 15 18:24:20 x58a kernel: [   29.688647]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 18:24:20 x58a kernel: [   29.688648] RIP: 0033:0x7f67242f850b
Nov 15 18:24:20 x58a kernel: [   29.688649] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 18:24:20 x58a kernel: [   29.688650] RSP: 002b:00007ffe278258a8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 18:24:20 x58a kernel: [   29.688651] RAX: ffffffffffffffda RBX: 00007f6723706210 RCX: 00007f67242f850b
Nov 15 18:24:20 x58a kernel: [   29.688651] RDX: 00007ffe27825920 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 18:24:20 x58a kernel: [   29.688652] RBP: 00007ffe27825920 R08: 0000000000000000 R09: 0000000000080000
Nov 15 18:24:20 x58a kernel: [   29.688652] R10: 0000558531b7cbf0 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 18:24:20 x58a kernel: [   29.688653] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 18:24:20 x58a kernel: [   29.688654] ---[ end trace b203c1ffa30df215 ]---



Nov 15 18:33:12 x58a kernel: [  561.495414] ------------[ cut here ]------------
Nov 15 18:33:12 x58a kernel: [  561.495416] Destroy non-HWS queue while stopped
Nov 15 18:33:12 x58a kernel: [  561.495607] WARNING: CPU: 6 PID: 3803 at /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 18:33:12 x58a kernel: [  561.495608] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core amdgpu(OE) snd_hwdep snd_pcm intel_powerclamp amd_iommu_v2 coretemp amd_sched(OE) snd_seq_midi amdttm(OE) snd_seq_midi_event kvm_intel cdc_ether snd_rawmidi amdkcl(OE) kvm usbnet snd_seq drm_kms_helper r8152 intel_cstate snd_seq_device i2c_algo_bit mxm_wmi snd_timer fb_sys_fops input_leds serio_raw mii snd syscopyarea sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid gpio_ich pata_acpi i2c_i801 lpc_ich pata_jmicron ahci libahci wmi
Nov 15 18:33:12 x58a kernel: [  561.495638] CPU: 6 PID: 3803 Comm: clinfo Tainted: G        W IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 18:33:12 x58a kernel: [  561.495639] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 18:33:12 x58a kernel: [  561.495722] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 18:33:12 x58a kernel: [  561.495725] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 8f e5 c0 c6 05 72 fb 38 00 01 e8 4d cb 72 c6 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 18:33:12 x58a kernel: [  561.495725] RSP: 0018:ffffa9f2c1d0bb60 EFLAGS: 00010286
Nov 15 18:33:12 x58a kernel: [  561.495727] RAX: 0000000000000000 RBX: ffff92bd9106f000 RCX: 0000000000000006
Nov 15 18:33:12 x58a kernel: [  561.495727] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff92bddf9978c0
Nov 15 18:33:12 x58a kernel: [  561.495728] RBP: ffffa9f2c1d0bb88 R08: 0000000000000539 R09: 0000000000000004
Nov 15 18:33:12 x58a kernel: [  561.495728] R10: 0000000000000000 R11: 0000000000000001 R12: ffff92bdd20ac400
Nov 15 18:33:12 x58a kernel: [  561.495729] R13: ffff92bd9106d628 R14: 0000000000000000 R15: ffff92bdd34fb280
Nov 15 18:33:12 x58a kernel: [  561.495730] FS:  00007f67236aa700(0000) GS:ffff92bddf980000(0000) knlGS:0000000000000000
Nov 15 18:33:12 x58a kernel: [  561.495731] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 18:33:12 x58a kernel: [  561.495732] CR2: 00002546fb6b5470 CR3: 00000003f312e000 CR4: 00000000000006e0
Nov 15 18:33:12 x58a kernel: [  561.495733] Call Trace:
Nov 15 18:33:12 x58a kernel: [  561.495820]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 18:33:12 x58a kernel: [  561.495908]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 18:33:12 x58a kernel: [  561.495983]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 18:33:12 x58a kernel: [  561.495987]  __mmu_notifier_release+0x47/0xd0
Nov 15 18:33:12 x58a kernel: [  561.495990]  exit_mmap+0x16c/0x1b0
Nov 15 18:33:12 x58a kernel: [  561.495992]  ? kfree+0x231/0x250
Nov 15 18:33:12 x58a kernel: [  561.495994]  ? _cond_resched+0x19/0x30
Nov 15 18:33:12 x58a kernel: [  561.495997]  mmput+0x5d/0x130
Nov 15 18:33:12 x58a kernel: [  561.495999]  do_exit+0x306/0xac0
Nov 15 18:33:12 x58a kernel: [  561.496003]  ? __check_object_size+0x4d/0x150
Nov 15 18:33:12 x58a kernel: [  561.496004]  do_group_exit+0x47/0xb0
Nov 15 18:33:12 x58a kernel: [  561.496007]  get_signal+0x169/0x890
Nov 15 18:33:12 x58a kernel: [  561.496011]  do_signal+0x34/0x6c0
Nov 15 18:33:12 x58a kernel: [  561.496013]  ? do_vfs_ioctl+0x407/0x670
Nov 15 18:33:12 x58a kernel: [  561.496016]  ? do_user_addr_fault+0x216/0x450
Nov 15 18:33:12 x58a kernel: [  561.496018]  exit_to_usermode_loop+0xbf/0x160
Nov 15 18:33:12 x58a kernel: [  561.496020]  do_syscall_64+0x163/0x190
Nov 15 18:33:12 x58a kernel: [  561.496022]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 18:33:12 x58a kernel: [  561.496023] RIP: 0033:0x7f67242f850b
Nov 15 18:33:12 x58a kernel: [  561.496025] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 18:33:12 x58a kernel: [  561.496025] RSP: 002b:00007f67236a9b98 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 18:33:12 x58a kernel: [  561.496027] RAX: fffffffffffffffc RBX: 00007f671c000c90 RCX: 00007f67242f850b
Nov 15 18:33:12 x58a kernel: [  561.496028] RDX: 00007f67236a9bf0 RSI: 00000000c0184b0c RDI: 0000000000000005
Nov 15 18:33:12 x58a kernel: [  561.496029] RBP: 00007f67236a9bf0 R08: 00007f671c000d40 R09: 0000000000000000
Nov 15 18:33:12 x58a kernel: [  561.496029] R10: 0000000000004022 R11: 0000000000000246 R12: 00000000c0184b0c
Nov 15 18:33:12 x58a kernel: [  561.496030] R13: 0000000000000005 R14: 00007f671c000c90 R15: 00007f67236a9d20
Nov 15 18:33:12 x58a kernel: [  561.496032] ---[ end trace b203c1ffa30df216 ]---


Nov 15 18:51:06 x58a kernel: [ 1040.354836] ------------[ cut here ]------------
Nov 15 18:51:06 x58a kernel: [ 1040.354837] Destroy non-HWS queue while stopped
Nov 15 18:51:06 x58a kernel: [ 1040.355064] WARNING: CPU: 3 PID: 3917 at /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 18:51:06 x58a kernel: [ 1040.355065] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core snd_hwdep amdgpu(OE) snd_pcm snd_seq_midi intel_powerclamp snd_seq_midi_event cdc_ether amd_iommu_v2 snd_rawmidi coretemp usbnet r8152 amd_sched(OE) amdttm(OE) kvm_intel snd_seq kvm amdkcl(OE) snd_seq_device mii drm_kms_helper snd_timer intel_cstate i2c_algo_bit input_leds mxm_wmi snd fb_sys_fops serio_raw syscopyarea sysfillrect soundcore sysimgblt i7core_edac mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 lpc_ich pata_jmicron ahci libahci wmi
Nov 15 18:51:06 x58a kernel: [ 1040.355095] CPU: 3 PID: 3917 Comm: clinfo Tainted: G        W IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 18:51:06 x58a kernel: [ 1040.355096] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 18:51:06 x58a kernel: [ 1040.355182] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 18:51:06 x58a kernel: [ 1040.355184] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 3f da c0 c6 05 72 fb 38 00 01 e8 4d 1b be f3 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 18:51:06 x58a kernel: [ 1040.355185] RSP: 0018:ffffa8d1c319fb60 EFLAGS: 00010286
Nov 15 18:51:06 x58a kernel: [ 1040.355186] RAX: 0000000000000000 RBX: ffff96f331a02400 RCX: 0000000000000006
Nov 15 18:51:06 x58a kernel: [ 1040.355187] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff96f35f8d78c0
Nov 15 18:51:06 x58a kernel: [ 1040.355188] RBP: ffffa8d1c319fb88 R08: 0000000000000566 R09: 0000000000000004
Nov 15 18:51:06 x58a kernel: [ 1040.355188] R10: 0000000000000000 R11: 0000000000000001 R12: ffff96f354f4e400
Nov 15 18:51:06 x58a kernel: [ 1040.355189] R13: ffff96f331a00428 R14: 0000000000000000 R15: ffff96f3568e6100
Nov 15 18:51:06 x58a kernel: [ 1040.355190] FS:  00007f8e7678d700(0000) GS:ffff96f35f8c0000(0000) knlGS:0000000000000000
Nov 15 18:51:06 x58a kernel: [ 1040.355190] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 18:51:06 x58a kernel: [ 1040.355191] CR2: 00007fc81dbf64d0 CR3: 0000000417712000 CR4: 00000000000006e0
Nov 15 18:51:06 x58a kernel: [ 1040.355192] Call Trace:
Nov 15 18:51:06 x58a kernel: [ 1040.355273]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 18:51:06 x58a kernel: [ 1040.355361]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 18:51:06 x58a kernel: [ 1040.355441]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 18:51:06 x58a kernel: [ 1040.355445]  __mmu_notifier_release+0x47/0xd0
Nov 15 18:51:06 x58a kernel: [ 1040.355448]  exit_mmap+0x16c/0x1b0
Nov 15 18:51:06 x58a kernel: [ 1040.355450]  ? kfree+0x231/0x250
Nov 15 18:51:06 x58a kernel: [ 1040.355453]  ? _cond_resched+0x19/0x30
Nov 15 18:51:06 x58a kernel: [ 1040.355455]  mmput+0x5d/0x130
Nov 15 18:51:06 x58a kernel: [ 1040.355458]  do_exit+0x306/0xac0
Nov 15 18:51:06 x58a kernel: [ 1040.355461]  ? __check_object_size+0x4d/0x150
Nov 15 18:51:06 x58a kernel: [ 1040.355463]  do_group_exit+0x47/0xb0
Nov 15 18:51:06 x58a kernel: [ 1040.355466]  get_signal+0x169/0x890
Nov 15 18:51:06 x58a kernel: [ 1040.355470]  do_signal+0x34/0x6c0
Nov 15 18:51:06 x58a kernel: [ 1040.355472]  ? do_vfs_ioctl+0x407/0x670
Nov 15 18:51:06 x58a kernel: [ 1040.355474]  ? do_user_addr_fault+0x216/0x450
Nov 15 18:51:06 x58a kernel: [ 1040.355477]  exit_to_usermode_loop+0xbf/0x160
Nov 15 18:51:06 x58a kernel: [ 1040.355479]  do_syscall_64+0x163/0x190
Nov 15 18:51:06 x58a kernel: [ 1040.355480]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 18:51:06 x58a kernel: [ 1040.355482] RIP: 0033:0x7f8e773db50b
Nov 15 18:51:06 x58a kernel: [ 1040.355483] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 18:51:06 x58a kernel: [ 1040.355484] RSP: 002b:00007f8e7678cb98 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 18:51:06 x58a kernel: [ 1040.355486] RAX: fffffffffffffffc RBX: 00007f8e70000c90 RCX: 00007f8e773db50b
Nov 15 18:51:06 x58a kernel: [ 1040.355486] RDX: 00007f8e7678cbf0 RSI: 00000000c0184b0c RDI: 0000000000000005
Nov 15 18:51:06 x58a kernel: [ 1040.355487] RBP: 00007f8e7678cbf0 R08: 00007f8e70000d40 R09: 0000000000000000
Nov 15 18:51:06 x58a kernel: [ 1040.355488] R10: 0000000000004022 R11: 0000000000000246 R12: 00000000c0184b0c
Nov 15 18:51:06 x58a kernel: [ 1040.355489] R13: 0000000000000005 R14: 00007f8e70000c90 R15: 00007f8e7678cd20
Nov 15 18:51:06 x58a kernel: [ 1040.355491] ---[ end trace 1a605fe000075d96 ]---



Nov 15 18:53:09 x58a kernel: [   84.668948] ------------[ cut here ]------------
Nov 15 18:53:09 x58a kernel: [   84.668949] Load non-HWS mqd while stopped
Nov 15 18:53:09 x58a kernel: [   84.669075] WARNING: CPU: 2 PID: 4287 at /var/lib/dkms/amdgpu/5.6.5.24-1109583/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:439 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 18:53:09 x58a kernel: [   84.669075] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi ledtrig_audio snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core intel_powerclamp snd_hwdep snd_pcm amdgpu(OE) coretemp snd_seq_midi amd_iommu_v2 snd_seq_midi_event snd_rawmidi amd_sched(OE) kvm_intel amdttm(OE) snd_seq cdc_ether kvm usbnet snd_seq_device input_leds snd_timer amdkcl(OE) intel_cstate serio_raw r8152 drm_kms_helper snd mxm_wmi i2c_algo_bit fb_sys_fops mii syscopyarea soundcore sysfillrect i7core_edac sysimgblt mac_hid sch_fq_codel parport_pc ppdev lp parport drm ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 lpc_ich pata_jmicron ahci libahci wmi
Nov 15 18:53:09 x58a kernel: [   84.669097] CPU: 2 PID: 4287 Comm: clinfo Tainted: G          IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 18:53:09 x58a kernel: [   84.669097] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 18:53:09 x58a kernel: [   84.669153] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 18:53:09 x58a kernel: [   84.669155] Code: 00 48 89 df e8 b2 ee ff ff e9 9e fd ff ff 80 3d 42 1c 32 00 00 75 15 48 c7 c7 f8 e7 f0 c0 c6 05 32 1c 32 00 01 e8 6c c7 e1 e7 <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 18:53:09 x58a kernel: [   84.669155] RSP: 0018:ffffbf6081f5fbb8 EFLAGS: 00010286
Nov 15 18:53:09 x58a kernel: [   84.669156] RAX: 0000000000000000 RBX: ffff9d70148e0800 RCX: 0000000000000006
Nov 15 18:53:09 x58a kernel: [   84.669157] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff9d701f8978c0
Nov 15 18:53:09 x58a kernel: [   84.669157] RBP: ffffbf6081f5fc08 R08: 0000000000000533 R09: 0000000000000004
Nov 15 18:53:09 x58a kernel: [   84.669158] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9d6fdaf95c00
Nov 15 18:53:09 x58a kernel: [   84.669158] R13: 0000000000000000 R14: ffff9d6fdd7e0e28 R15: ffff9d70108faf00
Nov 15 18:53:09 x58a kernel: [   84.669159] FS:  00007f91098cb740(0000) GS:ffff9d701f880000(0000) knlGS:0000000000000000
Nov 15 18:53:09 x58a kernel: [   84.669160] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 18:53:09 x58a kernel: [   84.669160] CR2: 00007f9108f52e0c CR3: 0000000379ac0000 CR4: 00000000000006e0
Nov 15 18:53:09 x58a kernel: [   84.669161] Call Trace:
Nov 15 18:53:09 x58a kernel: [   84.669219]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 18:53:09 x58a kernel: [   84.669273]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 18:53:09 x58a kernel: [   84.669335]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 18:53:09 x58a kernel: [   84.669404]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 18:53:09 x58a kernel: [   84.669409]  do_vfs_ioctl+0x407/0x670
Nov 15 18:53:09 x58a kernel: [   84.669410]  ksys_ioctl+0x67/0x90
Nov 15 18:53:09 x58a kernel: [   84.669411]  __x64_sys_ioctl+0x1a/0x20
Nov 15 18:53:09 x58a kernel: [   84.669414]  do_syscall_64+0x57/0x190
Nov 15 18:53:09 x58a kernel: [   84.669418]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 18:53:09 x58a kernel: [   84.669419] RIP: 0033:0x7f9109b6150b
Nov 15 18:53:09 x58a kernel: [   84.669421] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 18:53:09 x58a kernel: [   84.669421] RSP: 002b:00007ffdb7c12e08 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 18:53:09 x58a kernel: [   84.669422] RAX: ffffffffffffffda RBX: 00007f9108f6f210 RCX: 00007f9109b6150b
Nov 15 18:53:09 x58a kernel: [   84.669423] RDX: 00007ffdb7c12e80 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 18:53:09 x58a kernel: [   84.669424] RBP: 00007ffdb7c12e80 R08: 0000000000000000 R09: 0000000000080000
Nov 15 18:53:09 x58a kernel: [   84.669424] R10: 000055ad00a96b70 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 18:53:09 x58a kernel: [   84.669425] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 18:53:09 x58a kernel: [   84.669426] ---[ end trace c547e863588ac49f ]---




Nov 15 19:07:37 x58a kernel: [  953.225623] ------------[ cut here ]------------
Nov 15 19:07:37 x58a kernel: [  953.225625] Destroy non-HWS queue while stopped
Nov 15 19:07:37 x58a kernel: [  953.225821] WARNING: CPU: 0 PID: 4292 at /var/lib/dkms/amdgpu/5.6.5.24-1109583/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:555 destroy_queue_nocpsch_locked+0x18b/0x250 [amdgpu]
Nov 15 19:07:37 x58a kernel: [  953.225822] Modules linked in: nls_iso8859_1 snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi ledtrig_audio snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core intel_powerclamp snd_hwdep snd_pcm amdgpu(OE) coretemp snd_seq_midi amd_iommu_v2 snd_seq_midi_event snd_rawmidi amd_sched(OE) kvm_intel amdttm(OE) snd_seq cdc_ether kvm usbnet snd_seq_device input_leds snd_timer amdkcl(OE) intel_cstate serio_raw r8152 drm_kms_helper snd mxm_wmi i2c_algo_bit fb_sys_fops mii syscopyarea soundcore sysfillrect i7core_edac sysimgblt mac_hid sch_fq_codel parport_pc ppdev lp parport drm ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c uas usb_storage hid_generic usbhid hid pata_acpi gpio_ich i2c_i801 lpc_ich pata_jmicron ahci libahci wmi
Nov 15 19:07:37 x58a kernel: [  953.225850] CPU: 0 PID: 4292 Comm: clinfo Tainted: G        W IOE     5.4.0-52-generic #57-Ubuntu
Nov 15 19:07:37 x58a kernel: [  953.225851] Hardware name: Gigabyte Technology Co., Ltd. X58A-UD3R/X58A-UD3R, BIOS FE 12/23/2010
Nov 15 19:07:37 x58a kernel: [  953.225923] RIP: 0010:destroy_queue_nocpsch_locked+0x18b/0x250 [amdgpu]
Nov 15 19:07:37 x58a kernel: [  953.225925] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d e5 14 32 00 00 75 e6 48 c7 c7 18 e9 f0 c0 c6 05 d5 14 32 00 01 e8 10 c0 e1 e7 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 a0 fe ff ff 48 8d
Nov 15 19:07:37 x58a kernel: [  953.225926] RSP: 0018:ffffbf6081f7fb60 EFLAGS: 00010286
Nov 15 19:07:37 x58a kernel: [  953.225927] RAX: 0000000000000000 RBX: ffff9d6fdaf95c00 RCX: 0000000000000006
Nov 15 19:07:37 x58a kernel: [  953.225928] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff9d701f8178c0
Nov 15 19:07:37 x58a kernel: [  953.225929] RBP: ffffbf6081f7fb88 R08: 0000000000000564 R09: 0000000000000004
Nov 15 19:07:37 x58a kernel: [  953.225930] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9d70148e0800
Nov 15 19:07:37 x58a kernel: [  953.225930] R13: ffff9d6fdd7e0e28 R14: 0000000000000000 R15: ffff9d70108faf00
Nov 15 19:07:37 x58a kernel: [  953.225932] FS:  00007f9108f13700(0000) GS:ffff9d701f800000(0000) knlGS:0000000000000000
Nov 15 19:07:37 x58a kernel: [  953.225933] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 19:07:37 x58a kernel: [  953.225934] CR2: 00005637341b0cf8 CR3: 0000000379ac0000 CR4: 00000000000006f0
Nov 15 19:07:37 x58a kernel: [  953.225934] Call Trace:
Nov 15 19:07:37 x58a kernel: [  953.226014]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 19:07:37 x58a kernel: [  953.226091]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 19:07:37 x58a kernel: [  953.226164]  kfd_process_notifier_release+0x1bb/0x230 [amdgpu]
Nov 15 19:07:37 x58a kernel: [  953.226168]  __mmu_notifier_release+0x47/0xd0
Nov 15 19:07:37 x58a kernel: [  953.226171]  exit_mmap+0x16c/0x1b0
Nov 15 19:07:37 x58a kernel: [  953.226172]  ? kfree+0x231/0x250
Nov 15 19:07:37 x58a kernel: [  953.226175]  ? _cond_resched+0x19/0x30
Nov 15 19:07:37 x58a kernel: [  953.226179]  mmput+0x5d/0x130
Nov 15 19:07:37 x58a kernel: [  953.226181]  do_exit+0x306/0xac0
Nov 15 19:07:37 x58a kernel: [  953.226185]  ? __check_object_size+0x4d/0x150
Nov 15 19:07:37 x58a kernel: [  953.226186]  do_group_exit+0x47/0xb0
Nov 15 19:07:37 x58a kernel: [  953.226189]  get_signal+0x169/0x890
Nov 15 19:07:37 x58a kernel: [  953.226193]  do_signal+0x34/0x6c0
Nov 15 19:07:37 x58a kernel: [  953.226195]  ? do_vfs_ioctl+0x407/0x670
Nov 15 19:07:37 x58a kernel: [  953.226198]  ? do_user_addr_fault+0x216/0x450
Nov 15 19:07:37 x58a kernel: [  953.226202]  exit_to_usermode_loop+0xbf/0x160
Nov 15 19:07:37 x58a kernel: [  953.226203]  do_syscall_64+0x163/0x190
Nov 15 19:07:37 x58a kernel: [  953.226205]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 19:07:37 x58a kernel: [  953.226207] RIP: 0033:0x7f9109b6150b
Nov 15 19:07:37 x58a kernel: [  953.226209] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 19:07:37 x58a kernel: [  953.226209] RSP: 002b:00007f9108f12b98 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 19:07:37 x58a kernel: [  953.226211] RAX: fffffffffffffffc RBX: 00007f9104000c90 RCX: 00007f9109b6150b
Nov 15 19:07:37 x58a kernel: [  953.226211] RDX: 00007f9108f12bf0 RSI: 00000000c0184b0c RDI: 0000000000000005
Nov 15 19:07:37 x58a kernel: [  953.226212] RBP: 00007f9108f12bf0 R08: 00007f9104000d40 R09: 0000000000000000
Nov 15 19:07:37 x58a kernel: [  953.226213] R10: 0000000000004022 R11: 0000000000000246 R12: 00000000c0184b0c
Nov 15 19:07:37 x58a kernel: [  953.226213] R13: 0000000000000005 R14: 00007f9104000c90 R15: 00007f9108f12d20
Nov 15 19:07:37 x58a kernel: [  953.226215] ---[ end trace c547e863588ac4a0 ]---



Nov 15 21:11:59 x58a kernel: [  147.470501] ------------[ cut here ]------------
Nov 15 21:11:59 x58a kernel: [  147.470502] Load non-HWS mqd while stopped
Nov 15 21:11:59 x58a kernel: [  147.470562] WARNING: CPU: 3 PID: 2206 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 21:11:59 x58a kernel: [  147.470562] Modules linked in: snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core edac_mce_amd snd_hwdep amdgpu(OE) snd_pcm snd_seq_midi snd_seq_midi_event kvm_amd amd_iommu_v2 amd_sched(OE) snd_rawmidi kvm amdttm(OE) crct10dif_pclmul snd_seq ghash_clmulni_intel aesni_intel snd_seq_device snd_timer crypto_simd amdkcl(OE) hid_pl cryptd snd ff_memless drm_kms_helper input_leds glue_helper i2c_algo_bit fb_sys_fops joydev soundcore syscopyarea sysfillrect k10temp wmi_bmof sysimgblt ccp mac_hid sch_fq_codel parport_pc ppdev drm lp parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c hid_generic usbhid hid crc32_pclmul r8169 realtek nvme i2c_piix4 ahci nvme_core libahci wmi gpio_amdpt gpio_generic
Nov 15 21:11:59 x58a kernel: [  147.470581] CPU: 3 PID: 2206 Comm: hashcat Tainted: G           OE     5.4.0-52-generic #57-Ubuntu
Nov 15 21:11:59 x58a kernel: [  147.470581] Hardware name: Gigabyte Technology Co., Ltd. B550M S2H/B550M S2H, BIOS F1 05/26/2020
Nov 15 21:11:59 x58a kernel: [  147.470620] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 21:11:59 x58a kernel: [  147.470621] Code: 00 48 89 df e8 62 ea ff ff e9 9e fd ff ff 80 3d d2 e9 38 00 00 75 15 48 c7 c7 40 02 04 c1 c6 05 c2 e9 38 00 01 e8 9c 49 f4 d6 <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 21:11:59 x58a kernel: [  147.470621] RSP: 0018:ffffbbef0213bbb8 EFLAGS: 00010286
Nov 15 21:11:59 x58a kernel: [  147.470622] RAX: 0000000000000000 RBX: ffff9937c250fc00 RCX: 0000000000000006
Nov 15 21:11:59 x58a kernel: [  147.470622] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff9937ce8d78c0
Nov 15 21:11:59 x58a kernel: [  147.470623] RBP: ffffbbef0213bc08 R08: 00000000000004ab R09: 0000000000000004
Nov 15 21:11:59 x58a kernel: [  147.470623] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9937bd59fa00
Nov 15 21:11:59 x58a kernel: [  147.470623] R13: 0000000000000000 R14: ffff99379d1a7c28 R15: ffff9937c717a480
Nov 15 21:11:59 x58a kernel: [  147.470624] FS:  00007eff6f172700(0000) GS:ffff9937ce8c0000(0000) knlGS:0000000000000000
Nov 15 21:11:59 x58a kernel: [  147.470625] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 21:11:59 x58a kernel: [  147.470625] CR2: 00007eff5c001018 CR3: 00000008013b6000 CR4: 0000000000340ee0
Nov 15 21:11:59 x58a kernel: [  147.470625] Call Trace:
Nov 15 21:11:59 x58a kernel: [  147.470663]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 21:11:59 x58a kernel: [  147.470700]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 21:11:59 x58a kernel: [  147.470736]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 21:11:59 x58a kernel: [  147.470770]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 21:11:59 x58a kernel: [  147.470773]  do_vfs_ioctl+0x407/0x670
Nov 15 21:11:59 x58a kernel: [  147.470774]  ksys_ioctl+0x67/0x90
Nov 15 21:11:59 x58a kernel: [  147.470774]  __x64_sys_ioctl+0x1a/0x20
Nov 15 21:11:59 x58a kernel: [  147.470776]  do_syscall_64+0x57/0x190
Nov 15 21:11:59 x58a kernel: [  147.470778]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 21:11:59 x58a kernel: [  147.470779] RIP: 0033:0x7eff7c05f50b
Nov 15 21:11:59 x58a kernel: [  147.470780] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 21:11:59 x58a kernel: [  147.470780] RSP: 002b:00007eff6f1713d8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 21:11:59 x58a kernel: [  147.470781] RAX: ffffffffffffffda RBX: 00007eff70217210 RCX: 00007eff7c05f50b
Nov 15 21:11:59 x58a kernel: [  147.470781] RDX: 00007eff6f171450 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 21:11:59 x58a kernel: [  147.470781] RBP: 00007eff6f171450 R08: 0000000000000000 R09: 0000000000080000
Nov 15 21:11:59 x58a kernel: [  147.470782] R10: 000055a00de29fb0 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 21:11:59 x58a kernel: [  147.470782] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 21:11:59 x58a kernel: [  147.470783] ---[ end trace c7a335220d6b1fd4 ]---




Nov 15 21:12:04 x58a systemd[996]: Started Tracker metadata extractor.
Nov 15 21:12:10 x58a kernel: [  158.417334] ------------[ cut here ]------------
Nov 15 21:12:10 x58a kernel: [  158.417335] Destroy non-HWS queue while stopped
Nov 15 21:12:10 x58a kernel: [  158.417398] WARNING: CPU: 2 PID: 2201 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 21:12:10 x58a kernel: [  158.417399] Modules linked in: snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_intel_dspcfg snd_hda_codec snd_hda_core edac_mce_amd snd_hwdep amdgpu(OE) snd_pcm snd_seq_midi snd_seq_midi_event kvm_amd amd_iommu_v2 amd_sched(OE) snd_rawmidi kvm amdttm(OE) crct10dif_pclmul snd_seq ghash_clmulni_intel aesni_intel snd_seq_device snd_timer crypto_simd amdkcl(OE) hid_pl cryptd snd ff_memless drm_kms_helper input_leds glue_helper i2c_algo_bit fb_sys_fops joydev soundcore syscopyarea sysfillrect k10temp wmi_bmof sysimgblt ccp mac_hid sch_fq_codel parport_pc ppdev drm lp parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c hid_generic usbhid hid crc32_pclmul r8169 realtek nvme i2c_piix4 ahci nvme_core libahci wmi gpio_amdpt gpio_generic
Nov 15 21:12:10 x58a kernel: [  158.417419] CPU: 2 PID: 2201 Comm: hashcat Tainted: G        W  OE     5.4.0-52-generic #57-Ubuntu
Nov 15 21:12:10 x58a kernel: [  158.417419] Hardware name: Gigabyte Technology Co., Ltd. B550M S2H/B550M S2H, BIOS F1 05/26/2020
Nov 15 21:12:10 x58a kernel: [  158.417458] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 21:12:10 x58a kernel: [  158.417459] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 ff 03 c1 c6 05 72 fb 38 00 01 e8 4d 5b f4 d6 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 21:12:10 x58a kernel: [  158.417459] RSP: 0018:ffffbbef02083b60 EFLAGS: 00010286
Nov 15 21:12:10 x58a kernel: [  158.417460] RAX: 0000000000000000 RBX: ffff9937bd59c600 RCX: 0000000000000006
Nov 15 21:12:10 x58a kernel: [  158.417461] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff9937ce8978c0
Nov 15 21:12:10 x58a kernel: [  158.417461] RBP: ffffbbef02083b88 R08: 00000000000004d3 R09: 0000000000000004
Nov 15 21:12:10 x58a kernel: [  158.417461] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9937c250fc00
Nov 15 21:12:10 x58a kernel: [  158.417462] R13: ffff99379d1a7c28 R14: 0000000000000000 R15: ffff9937c717a480
Nov 15 21:12:10 x58a kernel: [  158.417462] FS:  00007eff7bf46b80(0000) GS:ffff9937ce880000(0000) knlGS:0000000000000000
Nov 15 21:12:10 x58a kernel: [  158.417463] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 21:12:10 x58a kernel: [  158.417463] CR2: 00007f2604001358 CR3: 00000008033b8000 CR4: 0000000000340ee0
Nov 15 21:12:10 x58a kernel: [  158.417463] Call Trace:
Nov 15 21:12:10 x58a kernel: [  158.417501]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 21:12:10 x58a kernel: [  158.417537]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 21:12:10 x58a kernel: [  158.417573]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 21:12:10 x58a kernel: [  158.417575]  __mmu_notifier_release+0x47/0xd0
Nov 15 21:12:10 x58a kernel: [  158.417577]  exit_mmap+0x16c/0x1b0
Nov 15 21:12:10 x58a kernel: [  158.417579]  ? __switch_to_asm+0x34/0x70
Nov 15 21:12:10 x58a kernel: [  158.417580]  ? _cond_resched+0x19/0x30
Nov 15 21:12:10 x58a kernel: [  158.417582]  mmput+0x5d/0x130
Nov 15 21:12:10 x58a kernel: [  158.417582]  do_exit+0x306/0xac0
Nov 15 21:12:10 x58a kernel: [  158.417584]  ? hrtimer_try_to_cancel+0x85/0x110
Nov 15 21:12:10 x58a kernel: [  158.417585]  do_group_exit+0x47/0xb0
Nov 15 21:12:10 x58a kernel: [  158.417586]  get_signal+0x169/0x890
Nov 15 21:12:10 x58a kernel: [  158.417587]  ? hrtimer_init_sleeper+0x90/0x90
Nov 15 21:12:10 x58a kernel: [  158.417588]  do_signal+0x34/0x6c0
Nov 15 21:12:10 x58a kernel: [  158.417590]  ? do_futex+0x10f/0x1e0
Nov 15 21:12:10 x58a kernel: [  158.417591]  ? __x64_sys_futex+0x13f/0x170
Nov 15 21:12:10 x58a kernel: [  158.417592]  exit_to_usermode_loop+0xbf/0x160
Nov 15 21:12:10 x58a kernel: [  158.417593]  do_syscall_64+0x163/0x190
Nov 15 21:12:10 x58a kernel: [  158.417594]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 21:12:10 x58a kernel: [  158.417595] RIP: 0033:0x7eff7c2a2618
Nov 15 21:12:10 x58a kernel: [  158.417597] Code: Bad RIP value.
Nov 15 21:12:10 x58a kernel: [  158.417597] RSP: 002b:00007ffcbbf50bf0 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
Nov 15 21:12:10 x58a kernel: [  158.417598] RAX: fffffffffffffdfc RBX: 00007ffcbbf50c90 RCX: 00007eff7c2a2618
Nov 15 21:12:10 x58a kernel: [  158.417598] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055a00ddb6548
Nov 15 21:12:10 x58a kernel: [  158.417598] RBP: 000055a00ddb6548 R08: 0000000000000000 R09: 00000000ffffffff
Nov 15 21:12:10 x58a kernel: [  158.417599] R10: 00007ffcbbf50c90 R11: 0000000000000246 R12: 0000000000000000
Nov 15 21:12:10 x58a kernel: [  158.417599] R13: 0000000000000000 R14: fffffffeffffffff R15: 0000000000040000
Nov 15 21:12:10 x58a kernel: [  158.417600] ---[ end trace c7a335220d6b1fd5 ]---



Nov 15 21:16:53 x58a kernel: [  174.571954] ------------[ cut here ]------------
Nov 15 21:16:53 x58a kernel: [  174.571955] Load non-HWS mqd while stopped
Nov 15 21:16:53 x58a kernel: [  174.572016] WARNING: CPU: 9 PID: 2319 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 21:16:53 x58a kernel: [  174.572017] Modules linked in: snd_hda_codec_realtek snd_hda_codec_generic amdgpu(OE) ledtrig_audio snd_hda_codec_hdmi edac_mce_amd amd_iommu_v2 snd_hda_intel kvm_amd amd_sched(OE) snd_intel_dspcfg kvm snd_hda_codec amdttm(OE) snd_hda_core snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi crct10dif_pclmul ghash_clmulni_intel amdkcl(OE) snd_seq drm_kms_helper snd_seq_device aesni_intel i2c_algo_bit snd_timer fb_sys_fops hid_pl crypto_simd syscopyarea cryptd snd ff_memless sysfillrect joydev input_leds glue_helper ccp wmi_bmof k10temp soundcore sysimgblt mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c hid_generic usbhid hid crc32_pclmul i2c_piix4 r8169 nvme realtek ahci libahci nvme_core wmi gpio_amdpt gpio_generic
Nov 15 21:16:53 x58a kernel: [  174.572036] CPU: 9 PID: 2319 Comm: hashcat Tainted: G           OE     5.4.0-52-generic #57-Ubuntu
Nov 15 21:16:53 x58a kernel: [  174.572037] Hardware name: Gigabyte Technology Co., Ltd. B550M S2H/B550M S2H, BIOS F1 05/26/2020
Nov 15 21:16:53 x58a kernel: [  174.572077] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 21:16:53 x58a kernel: [  174.572078] Code: 00 48 89 df e8 62 ea ff ff e9 9e fd ff ff 80 3d d2 e9 38 00 00 75 15 48 c7 c7 40 82 15 c1 c6 05 c2 e9 38 00 01 e8 9c c9 02 c1 <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 21:16:53 x58a kernel: [  174.572078] RSP: 0018:ffffc20f021f3bb8 EFLAGS: 00010286
Nov 15 21:16:53 x58a kernel: [  174.572079] RAX: 0000000000000000 RBX: ffff9e2a824d0800 RCX: 0000000000000006
Nov 15 21:16:53 x58a kernel: [  174.572079] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff9e2a8ea578c0
Nov 15 21:16:53 x58a kernel: [  174.572080] RBP: ffffc20f021f3c08 R08: 00000000000004b5 R09: 0000000000000004
Nov 15 21:16:53 x58a kernel: [  174.572080] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9e2a8209da00
Nov 15 21:16:53 x58a kernel: [  174.572080] R13: 0000000000000000 R14: ffff9e2a4a68de28 R15: ffff9e2a80d9a700
Nov 15 21:16:53 x58a kernel: [  174.572081] FS:  00007faa62328700(0000) GS:ffff9e2a8ea40000(0000) knlGS:0000000000000000
Nov 15 21:16:53 x58a kernel: [  174.572082] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 21:16:53 x58a kernel: [  174.572082] CR2: 00007faa50001018 CR3: 00000007beecc000 CR4: 0000000000340ee0
Nov 15 21:16:53 x58a kernel: [  174.572082] Call Trace:
Nov 15 21:16:53 x58a kernel: [  174.572122]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 21:16:53 x58a kernel: [  174.572159]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 21:16:53 x58a kernel: [  174.572195]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 21:16:53 x58a kernel: [  174.572230]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 21:16:53 x58a kernel: [  174.572233]  do_vfs_ioctl+0x407/0x670
Nov 15 21:16:53 x58a kernel: [  174.572234]  ksys_ioctl+0x67/0x90
Nov 15 21:16:53 x58a kernel: [  174.572234]  __x64_sys_ioctl+0x1a/0x20
Nov 15 21:16:53 x58a kernel: [  174.572236]  do_syscall_64+0x57/0x190
Nov 15 21:16:53 x58a kernel: [  174.572238]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 21:16:53 x58a kernel: [  174.572239] RIP: 0033:0x7faa6f21550b
Nov 15 21:16:53 x58a kernel: [  174.572240] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 21:16:53 x58a kernel: [  174.572240] RSP: 002b:00007faa623273d8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 21:16:53 x58a kernel: [  174.572241] RAX: ffffffffffffffda RBX: 00007faa633cd210 RCX: 00007faa6f21550b
Nov 15 21:16:53 x58a kernel: [  174.572241] RDX: 00007faa62327450 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 21:16:53 x58a kernel: [  174.572241] RBP: 00007faa62327450 R08: 0000000000000000 R09: 0000000000080000
Nov 15 21:16:53 x58a kernel: [  174.572242] R10: 000055a3a15dafb0 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 21:16:53 x58a kernel: [  174.572242] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 21:16:53 x58a kernel: [  174.572243] ---[ end trace 22879e09d22773d4 ]---


Nov 15 21:16:55 x58a kernel: [  176.473280] ------------[ cut here ]------------
Nov 15 21:16:55 x58a kernel: [  176.473281] Destroy non-HWS queue while stopped
Nov 15 21:16:55 x58a kernel: [  176.473345] WARNING: CPU: 4 PID: 2298 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 21:16:55 x58a kernel: [  176.473345] Modules linked in: snd_hda_codec_realtek snd_hda_codec_generic amdgpu(OE) ledtrig_audio snd_hda_codec_hdmi edac_mce_amd amd_iommu_v2 snd_hda_intel kvm_amd amd_sched(OE) snd_intel_dspcfg kvm snd_hda_codec amdttm(OE) snd_hda_core snd_hwdep snd_pcm snd_seq_midi snd_seq_midi_event snd_rawmidi crct10dif_pclmul ghash_clmulni_intel amdkcl(OE) snd_seq drm_kms_helper snd_seq_device aesni_intel i2c_algo_bit snd_timer fb_sys_fops hid_pl crypto_simd syscopyarea cryptd snd ff_memless sysfillrect joydev input_leds glue_helper ccp wmi_bmof k10temp soundcore sysimgblt mac_hid sch_fq_codel parport_pc ppdev lp drm parport ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c hid_generic usbhid hid crc32_pclmul i2c_piix4 r8169 nvme realtek ahci libahci nvme_core wmi gpio_amdpt gpio_generic
Nov 15 21:16:55 x58a kernel: [  176.473366] CPU: 4 PID: 2298 Comm: hashcat Tainted: G        W  OE     5.4.0-52-generic #57-Ubuntu
Nov 15 21:16:55 x58a kernel: [  176.473366] Hardware name: Gigabyte Technology Co., Ltd. B550M S2H/B550M S2H, BIOS F1 05/26/2020
Nov 15 21:16:55 x58a kernel: [  176.473406] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 21:16:55 x58a kernel: [  176.473407] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 7f 15 c1 c6 05 72 fb 38 00 01 e8 4d db 02 c1 <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 21:16:55 x58a kernel: [  176.473407] RSP: 0018:ffffc20f023fbb60 EFLAGS: 00010286
Nov 15 21:16:55 x58a kernel: [  176.473408] RAX: 0000000000000000 RBX: ffff9e2a8209e000 RCX: 0000000000000006
Nov 15 21:16:55 x58a kernel: [  176.473408] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff9e2a8e9178c0
Nov 15 21:16:55 x58a kernel: [  176.473409] RBP: ffffc20f023fbb88 R08: 00000000000004d9 R09: 0000000000000004
Nov 15 21:16:55 x58a kernel: [  176.473409] R10: 0000000000000000 R11: 0000000000000001 R12: ffff9e2a824d0800
Nov 15 21:16:55 x58a kernel: [  176.473409] R13: ffff9e2a4a68de28 R14: 0000000000000000 R15: ffff9e2a80d9a700
Nov 15 21:16:55 x58a kernel: [  176.473410] FS:  00007faa6f0fcb80(0000) GS:ffff9e2a8e900000(0000) knlGS:0000000000000000
Nov 15 21:16:55 x58a kernel: [  176.473410] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 21:16:55 x58a kernel: [  176.473411] CR2: 0000557608036578 CR3: 0000000808b38000 CR4: 0000000000340ee0
Nov 15 21:16:55 x58a kernel: [  176.473411] Call Trace:
Nov 15 21:16:55 x58a kernel: [  176.473449]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 21:16:55 x58a kernel: [  176.473485]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 21:16:55 x58a kernel: [  176.473520]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 21:16:55 x58a kernel: [  176.473523]  __mmu_notifier_release+0x47/0xd0
Nov 15 21:16:55 x58a kernel: [  176.473525]  exit_mmap+0x16c/0x1b0
Nov 15 21:16:55 x58a kernel: [  176.473527]  ? do_futex+0x160/0x1e0
Nov 15 21:16:55 x58a kernel: [  176.473529]  ? _cond_resched+0x19/0x30
Nov 15 21:16:55 x58a kernel: [  176.473530]  mmput+0x5d/0x130
Nov 15 21:16:55 x58a kernel: [  176.473531]  do_exit+0x306/0xac0
Nov 15 21:16:55 x58a kernel: [  176.473532]  ? hrtimer_try_to_cancel+0x85/0x110
Nov 15 21:16:55 x58a kernel: [  176.473533]  do_group_exit+0x47/0xb0
Nov 15 21:16:55 x58a kernel: [  176.473534]  get_signal+0x169/0x890
Nov 15 21:16:55 x58a kernel: [  176.473535]  ? hrtimer_init_sleeper+0x90/0x90
Nov 15 21:16:55 x58a kernel: [  176.473536]  do_signal+0x34/0x6c0
Nov 15 21:16:55 x58a kernel: [  176.473537]  ? do_futex+0x10f/0x1e0
Nov 15 21:16:55 x58a kernel: [  176.473538]  ? __x64_sys_futex+0x13f/0x170
Nov 15 21:16:55 x58a kernel: [  176.473540]  exit_to_usermode_loop+0xbf/0x160
Nov 15 21:16:55 x58a kernel: [  176.473540]  do_syscall_64+0x163/0x190
Nov 15 21:16:55 x58a kernel: [  176.473542]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 21:16:55 x58a kernel: [  176.473543] RIP: 0033:0x7faa6f458618
Nov 15 21:16:55 x58a kernel: [  176.473545] Code: Bad RIP value.
Nov 15 21:16:55 x58a kernel: [  176.473546] RSP: 002b:00007ffd51767d50 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
Nov 15 21:16:55 x58a kernel: [  176.473546] RAX: fffffffffffffdfc RBX: 00007ffd51767df0 RCX: 00007faa6f458618
Nov 15 21:16:55 x58a kernel: [  176.473547] RDX: 0000000000000000 RSI: 0000000000000189 RDI: 000055a3a1567548
Nov 15 21:16:55 x58a kernel: [  176.473547] RBP: 000055a3a1567548 R08: 0000000000000000 R09: 00000000ffffffff
Nov 15 21:16:55 x58a kernel: [  176.473547] R10: 00007ffd51767df0 R11: 0000000000000246 R12: 0000000000000000
Nov 15 21:16:55 x58a kernel: [  176.473548] R13: 0000000000000000 R14: fffffffeffffffff R15: 0000000000040000
Nov 15 21:16:55 x58a kernel: [  176.473548] ---[ end trace 22879e09d22773d5 ]---



Nov 15 23:04:52 x58a kernel: [  123.005243] ------------[ cut here ]------------
Nov 15 23:04:52 x58a kernel: [  123.005245] Load non-HWS mqd while stopped
Nov 15 23:04:52 x58a kernel: [  123.005343] WARNING: CPU: 1 PID: 1760 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:393 create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 23:04:52 x58a kernel: [  123.005343] Modules linked in: intel_rapl_msr mei_hdcp intel_rapl_common x86_pkg_temp_thermal intel_powerclamp coretemp kvm_intel rtl8xxxu kvm crct10dif_pclmul mac80211 ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi ledtrig_audio amdgpu(OE) cryptd snd_hda_intel snd_intel_dspcfg snd_seq_midi rapl snd_hda_codec snd_seq_midi_event cfg80211 snd_hda_core intel_cstate amd_iommu_v2 snd_hwdep amd_sched(OE) snd_rawmidi joydev amdttm(OE) libarc4 input_leds i915 snd_pcm snd_seq serio_raw amdkcl(OE) snd_seq_device snd_timer drm_kms_helper i2c_algo_bit fb_sys_fops syscopyarea snd sysfillrect sysimgblt mei_me mac_hid soundcore mei sch_fq_codel parport_pc ppdev lp parport drm ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c hid_logitech_hidpp hid_logitech_dj hid_generic uas usbhid hid usb_storage crc32_pclmul ahci libahci lpc_ich i2c_i801 r8169 realtek video
Nov 15 23:04:52 x58a kernel: [  123.005370] CPU: 1 PID: 1760 Comm: clinfo Tainted: G           OE     5.4.0-52-generic #57-Ubuntu
Nov 15 23:04:52 x58a kernel: [  123.005371] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./H81M-DGS R2.0, BIOS P1.60 07/23/2015
Nov 15 23:04:52 x58a kernel: [  123.005446] RIP: 0010:create_queue_nocpsch+0x39f/0x670 [amdgpu]
Nov 15 23:04:52 x58a kernel: [  123.005447] Code: 00 48 89 df e8 62 ea ff ff e9 9e fd ff ff 80 3d d2 e9 38 00 00 75 15 48 c7 c7 40 e2 ef c0 c6 05 c2 e9 38 00 01 e8 9c 69 28 ce <0f> 0b 49 8b 46 10 4c 89 60 08 49 89 04 24 48 8b 45 c8 49 89 44 24
Nov 15 23:04:52 x58a kernel: [  123.005448] RSP: 0018:ffffabf94218bbb8 EFLAGS: 00010286
Nov 15 23:04:52 x58a kernel: [  123.005449] RAX: 0000000000000000 RBX: ffff8e82939a4800 RCX: 0000000000000006
Nov 15 23:04:52 x58a kernel: [  123.005450] RDX: 0000000000000007 RSI: 0000000000000082 RDI: ffff8e829f1178c0
Nov 15 23:04:52 x58a kernel: [  123.005450] RBP: ffffabf94218bc08 R08: 00000000000004e6 R09: 0000000000000004
Nov 15 23:04:52 x58a kernel: [  123.005451] R10: 0000000000000000 R11: 0000000000000001 R12: ffff8e8299833800
Nov 15 23:04:52 x58a kernel: [  123.005451] R13: 0000000000000000 R14: ffff8e8299832428 R15: ffff8e8297e58580
Nov 15 23:04:52 x58a kernel: [  123.005452] FS:  00007f98275a4740(0000) GS:ffff8e829f100000(0000) knlGS:0000000000000000
Nov 15 23:04:52 x58a kernel: [  123.005453] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 23:04:52 x58a kernel: [  123.005454] CR2: 000055d4728e96b0 CR3: 000000041b02a004 CR4: 00000000000606e0
Nov 15 23:04:52 x58a kernel: [  123.005454] Call Trace:
Nov 15 23:04:52 x58a kernel: [  123.005528]  pqm_create_queue+0x182/0x450 [amdgpu]
Nov 15 23:04:52 x58a kernel: [  123.005597]  kfd_ioctl_create_queue+0x227/0x560 [amdgpu]
Nov 15 23:04:52 x58a kernel: [  123.005665]  kfd_ioctl+0x252/0x460 [amdgpu]
Nov 15 23:04:52 x58a kernel: [  123.005731]  ? kfd_ioctl_dbg_address_watch+0x160/0x160 [amdgpu]
Nov 15 23:04:52 x58a kernel: [  123.005734]  do_vfs_ioctl+0x407/0x670
Nov 15 23:04:52 x58a kernel: [  123.005736]  ksys_ioctl+0x67/0x90
Nov 15 23:04:52 x58a kernel: [  123.005737]  __x64_sys_ioctl+0x1a/0x20
Nov 15 23:04:52 x58a kernel: [  123.005739]  do_syscall_64+0x57/0x190
Nov 15 23:04:52 x58a kernel: [  123.005742]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 23:04:52 x58a kernel: [  123.005743] RIP: 0033:0x7f982783a50b
Nov 15 23:04:52 x58a kernel: [  123.005744] Code: 0f 1e fa 48 8b 05 85 39 0d 00 64 c7 00 26 00 00 00 48 c7 c0 ff ff ff ff c3 66 0f 1f 44 00 00 f3 0f 1e fa b8 10 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 55 39 0d 00 f7 d8 64 89 01 48
Nov 15 23:04:52 x58a kernel: [  123.005745] RSP: 002b:00007ffd061054e8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
Nov 15 23:04:52 x58a kernel: [  123.005746] RAX: ffffffffffffffda RBX: 00007f9826c48210 RCX: 00007f982783a50b
Nov 15 23:04:52 x58a kernel: [  123.005747] RDX: 00007ffd06105560 RSI: 00000000c0584b02 RDI: 0000000000000005
Nov 15 23:04:52 x58a kernel: [  123.005747] RBP: 00007ffd06105560 R08: 0000000000000000 R09: 0000000000080000
Nov 15 23:04:52 x58a kernel: [  123.005748] R10: 000055cd89031a50 R11: 0000000000000246 R12: 00000000c0584b02
Nov 15 23:04:52 x58a kernel: [  123.005749] R13: 0000000000000005 R14: 0000000001100000 R15: 0000000000000000
Nov 15 23:04:52 x58a kernel: [  123.005750] ---[ end trace cfaf74393c215caf ]---



Nov 15 23:05:04 x58a kernel: [  135.859644] ------------[ cut here ]------------
Nov 15 23:05:04 x58a kernel: [  135.859646] Destroy non-HWS queue while stopped
Nov 15 23:05:04 x58a kernel: [  135.859747] WARNING: CPU: 1 PID: 1760 at /var/lib/dkms/amdgpu/3.9-19/build/amd/amdgpu/../amdkfd/kfd_device_queue_manager.c:509 destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 23:05:04 x58a kernel: [  135.859747] Modules linked in: intel_rapl_msr mei_hdcp intel_rapl_common x86_pkg_temp_thermal intel_powerclamp coretemp kvm_intel rtl8xxxu kvm crct10dif_pclmul mac80211 ghash_clmulni_intel snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi ledtrig_audio amdgpu(OE) cryptd snd_hda_intel snd_intel_dspcfg snd_seq_midi rapl snd_hda_codec snd_seq_midi_event cfg80211 snd_hda_core intel_cstate amd_iommu_v2 snd_hwdep amd_sched(OE) snd_rawmidi joydev amdttm(OE) libarc4 input_leds i915 snd_pcm snd_seq serio_raw amdkcl(OE) snd_seq_device snd_timer drm_kms_helper i2c_algo_bit fb_sys_fops syscopyarea snd sysfillrect sysimgblt mei_me mac_hid soundcore mei sch_fq_codel parport_pc ppdev lp parport drm ip_tables x_tables autofs4 btrfs xor zstd_compress raid6_pq libcrc32c hid_logitech_hidpp hid_logitech_dj hid_generic uas usbhid hid usb_storage crc32_pclmul ahci libahci lpc_ich i2c_i801 r8169 realtek video
Nov 15 23:05:04 x58a kernel: [  135.859774] CPU: 1 PID: 1760 Comm: clinfo Tainted: G        W  OE     5.4.0-52-generic #57-Ubuntu
Nov 15 23:05:04 x58a kernel: [  135.859774] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./H81M-DGS R2.0, BIOS P1.60 07/23/2015
Nov 15 23:05:04 x58a kernel: [  135.859839] RIP: 0010:destroy_queue_nocpsch_locked+0x16e/0x220 [amdgpu]
Nov 15 23:05:04 x58a kernel: [  135.859841] Code: f0 41 5c 41 5d 41 5e 41 5f 5d c3 45 31 f6 80 3d 82 fb 38 00 00 75 e6 48 c7 c7 e8 df ef c0 c6 05 72 fb 38 00 01 e8 4d 7b 28 ce <0f> 0b eb cf 4d 8b bc 24 c0 00 00 00 85 d2 0f 84 bd fe ff ff 48 8d
Nov 15 23:05:04 x58a kernel: [  135.859841] RSP: 0018:ffffabf94218bb60 EFLAGS: 00010286
Nov 15 23:05:04 x58a kernel: [  135.859843] RAX: 0000000000000000 RBX: ffff8e8299833800 RCX: 0000000000000006
Nov 15 23:05:04 x58a kernel: [  135.859843] RDX: 0000000000000007 RSI: 0000000000000096 RDI: ffff8e829f1178c0
Nov 15 23:05:04 x58a kernel: [  135.859844] RBP: ffffabf94218bb88 R08: 000000000000050e R09: 0000000000000004
Nov 15 23:05:04 x58a kernel: [  135.859844] R10: 0000000000000000 R11: 0000000000000001 R12: ffff8e82939a4800
Nov 15 23:05:04 x58a kernel: [  135.859845] R13: ffff8e8299832428 R14: 0000000000000000 R15: ffff8e8297e58580
Nov 15 23:05:04 x58a kernel: [  135.859846] FS:  00007f98275a4740(0000) GS:ffff8e829f100000(0000) knlGS:0000000000000000
Nov 15 23:05:04 x58a kernel: [  135.859847] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Nov 15 23:05:04 x58a kernel: [  135.859847] CR2: 000055d47291ad20 CR3: 000000041b02a002 CR4: 00000000000606e0
Nov 15 23:05:04 x58a kernel: [  135.859848] Call Trace:
Nov 15 23:05:04 x58a kernel: [  135.859909]  process_termination_nocpsch+0x71/0x160 [amdgpu]
Nov 15 23:05:04 x58a kernel: [  135.859967]  kfd_process_dequeue_from_all_devices+0x40/0x60 [amdgpu]
Nov 15 23:05:04 x58a kernel: [  135.860027]  kfd_process_notifier_release+0x1a7/0x220 [amdgpu]
Nov 15 23:05:04 x58a kernel: [  135.860030]  __mmu_notifier_release+0x47/0xd0
Nov 15 23:05:04 x58a kernel: [  135.860032]  exit_mmap+0x16c/0x1b0
Nov 15 23:05:04 x58a kernel: [  135.860035]  ? do_futex+0x160/0x1e0
Nov 15 23:05:04 x58a kernel: [  135.860037]  ? _cond_resched+0x19/0x30
Nov 15 23:05:04 x58a kernel: [  135.860039]  mmput+0x5d/0x130
Nov 15 23:05:04 x58a kernel: [  135.860041]  do_exit+0x306/0xac0
Nov 15 23:05:04 x58a kernel: [  135.860043]  ? __switch_to_asm+0x40/0x70
Nov 15 23:05:04 x58a kernel: [  135.860044]  ? __switch_to_asm+0x34/0x70
Nov 15 23:05:04 x58a kernel: [  135.860046]  ? __switch_to_asm+0x40/0x70
Nov 15 23:05:04 x58a kernel: [  135.860047]  ? __switch_to_asm+0x34/0x70
Nov 15 23:05:04 x58a kernel: [  135.860048]  do_group_exit+0x47/0xb0
Nov 15 23:05:04 x58a kernel: [  135.860051]  get_signal+0x169/0x890
Nov 15 23:05:04 x58a kernel: [  135.860052]  ? reschedule_interrupt+0xa/0x20
Nov 15 23:05:04 x58a kernel: [  135.860055]  do_signal+0x34/0x6c0
Nov 15 23:05:04 x58a kernel: [  135.860056]  ? __schedule+0x661/0x740
Nov 15 23:05:04 x58a kernel: [  135.860059]  exit_to_usermode_loop+0xbf/0x160
Nov 15 23:05:04 x58a kernel: [  135.860061]  do_syscall_64+0x163/0x190
Nov 15 23:05:04 x58a kernel: [  135.860063]  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Nov 15 23:05:04 x58a kernel: [  135.860064] RIP: 0033:0x7f982782889b
Nov 15 23:05:04 x58a kernel: [  135.860065] Code: 73 01 c3 48 8b 0d f5 55 0e 00 f7 d8 64 89 01 48 83 c8 ff c3 66 2e 0f 1f 84 00 00 00 00 00 90 f3 0f 1e fa b8 18 00 00 00 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d c5 55 0e 00 f7 d8 64 89 01 48
Nov 15 23:05:04 x58a kernel: [  135.860066] RSP: 002b:00007ffd06105988 EFLAGS: 00000246 ORIG_RAX: 0000000000000018
Nov 15 23:05:04 x58a kernel: [  135.860067] RAX: 0000000000000000 RBX: 000055cd89146a00 RCX: 00007f982782889b
Nov 15 23:05:04 x58a kernel: [  135.860067] RDX: 0000000001004000 RSI: 0000000000000010 RDI: 000055cd89146a00
Nov 15 23:05:04 x58a kernel: [  135.860068] RBP: 0000000000000000 R08: 0000000000000000 R09: 00007f982788dfd0
Nov 15 23:05:04 x58a kernel: [  135.860069] R10: 28840000c0055802 R11: 0000000000000246 R12: 00007f9826e96e40
Nov 15 23:05:04 x58a kernel: [  135.860069] R13: 0000000001100000 R14: 000055cd89146a00 R15: 00007f9826e80c10
Nov 15 23:05:04 x58a kernel: [  135.860071] ---[ end trace cfaf74393c215cb0 ]---



$ rocminfo 
ROCk module is loaded
Able to open /dev/kfd read-write
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 3600 6-Core Processor  
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 3600 6-Core Processor  
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32892276(0x1f5e574) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32892276(0x1f5e574) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx701                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Hawaii XT / Grenada XT [Radeon R9 290X/390X]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26544(0x67b0)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1080                               
  BDFID:                   2304                               
  Internal Node ID:        1                                  
  Compute Unit:            44                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8388608(0x800000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx701          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                FALSE                              
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***  


$ clinfo 
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (3204.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback 


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Hawaii XT / Grenada XT [Radeon R9 290X/390X]
  Device Topology:                               PCI[ B#9, D#0, F#0 ]
  Max compute units:                             44
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1080Mhz
  Address bits:                                  64
  Max memory allocation:                         7301444400
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26544
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            8589934592
  Constant buffer size:                          7301444400
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          3006477104
  Max global variable size:                      7301444400
  Max global variable preferred total size:      8589934592
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:                              
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
**crash**

/opt/rocm/hip/samples/0_Intro/square$ ./square.out 
error: 'hipErrorInvalidDevice'(101) at square.cpp:61


```

---

### 评论 #32 — dagelf (2020-11-15T20:03:41Z)

The above runs are on 3 different motherboard and CPU combinations. 2 Intel, 1 AMD. 

---

### 评论 #33 — dagelf (2020-11-15T20:18:17Z)

> > Experimental support for our Hawaii (GFX7) GPUs (Radeon R9 290, R9 390, FirePro W9100, S9150, S9170)
> > does not require or take advantage of PCIe Atomics. However, we still recommend that you use a CPU
> > from the list provided above for compatibility purposes.
> 
> I don't have a CPU from the given list (my CPU predates Ryzen, it's an FX-9590 one), but I know I got ROCm working once with Hawaii on my CPU in the past.

Technically these are Grenada XT and Grenada Pro, but they show up as "Hawaii". I have an actual Hawaii Pro and Hawaii XT too. Can you help? I can't tell you how much I would appreciate it. Can you remember what kernel, and what drivers you were using?

---

### 评论 #34 — Moading (2020-11-15T21:28:35Z)

I started my OpenCL learning on a R9 390. The only way to get OpenCL running on that card is to use the obsolete fglrx and an obsolete distribution that supports it. That combination will give you OpenCL 2.0. Or you could use the AMD drivers for that card on windows 10 which would also give you OpenCL 2.0.

Even today with latest hardware (Radeon VII, ROCm 3.9), some OpenCL features like device side enqueue are not working. This is how bad ROCm is.

---

### 评论 #35 — illwieckz (2020-11-16T04:58:47Z)

> I bought 10 of these cards 4 years ago (!!!) to run workloads on...

Ouch…

> The only way to get OpenCL running on that card is to use the obsolete fglrx and an obsolete distribution that supports it.

I even did not tried that myself…

@dagelf and @Moading please follow those instructions: 

### 0. Requirements

First, get Ubuntu 20.04 LTS. I have not tested more recent stuff and other distributions may be harder to get things working.

### 1. Install my `dpm-query` service

To set a safe power management profile at startup because R9 390X is buggy and will crash otherwise.

```sh
sudo apt-get install --yes fakeroot checkinstall

git clone https://github.com/illwieckz/dpm-query.git
cd dpm-query
./configure --enable-service

printf 'n\n\n\n' \
| fakeroot checkinstall --fstrans \
	--pkgname='dpm-query' \
	--pkgversion='0~git' \
	--pkglicense='ISC' \
	--pkgarch='all' \
	--deldesc='yes'

sudo dpkg -i 'dpm-query_0~git-1_all.deb'

sudo systemctl enable 'dpm-query.service'
```

### 2. Enable the `amdgpu` driver for your card

```sh
sudo mkdir --parents '/etc/default/grub.d'

sudo tee '/etc/default/grub.d/amdgpu_enable.cfg' >/dev/null <<\EOF
# R9 390X and friends
GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} amdgpu.cik_support=1 radeon.cik_support=0"

# HD 7970 and friends
GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT} amdgpu.si_support=1 radeon.si_support=0"
EOF

sudo update-grub
```

### 3. Reboot

```sh
sudo reboot
```

### 4. Install the AMDGPU-PRO legacy Orca OpenCL driver

You can use my helper script that will make it easy for you.

```sh
git clone 'https://gitlab.com/illwieckz/i-love-compute.git'
cd 'i-love-compute/scripts'
./ubuntu-opencl-amdgpupro install --framework=orca
```

### 5. Optional: install Mesa/Clover

Note that you may also try the Mesa/Clover (`libclc`) implementation which is not complete at this time (missing image support so it will not be compatible with photograph workflow, like Darktable), but can perform better than AMD's OpenCL on some supported workflow (like LuxRender). Both can be installed at the same time, it's not a problem:

```sh
sudo apt-get install --yes mesa-opencl-icd
```

### 6. Test

In the end, I get that on my end:

```sh
clinfo --raw | egrep 'CL_PLATFORM_NAME|CL_DEVICE_NAME|CL_DRIVER_VERSION|CL_DEVICE_OPENCL_C_VERSION|CL_DEVICE_TYPE|CL_DEVICE_MAX_COMPUTE_UNITS|CL_DEVICE_MAX_CLOCK_FREQUENCY'
```
```
  CL_PLATFORM_NAME                                Clover
  CL_PLATFORM_NAME                                AMD Accelerated Parallel Processing
[MESA/*]    CL_PLATFORM_NAME                                Clover
[MESA/0]    CL_DEVICE_NAME                                  AMD Radeon (TM) R9 390 Series (HAWAII, DRM 3.35.0, 5.4.0-53-generic, LLVM 10.0.0)
[MESA/0]    CL_DRIVER_VERSION                               20.0.8
[MESA/0]    CL_DEVICE_OPENCL_C_VERSION                      OpenCL C 1.1 
[MESA/0]    CL_DEVICE_TYPE                                  CL_DEVICE_TYPE_GPU
[MESA/0]    CL_DEVICE_MAX_COMPUTE_UNITS                     44
[MESA/0]    CL_DEVICE_MAX_CLOCK_FREQUENCY                   1080
[AMD/*]     CL_PLATFORM_NAME                                AMD Accelerated Parallel Processing
[AMD/0]     CL_DEVICE_NAME                                  Hawaii
[AMD/0]     CL_DRIVER_VERSION                               3180.7
[AMD/0]     CL_DEVICE_OPENCL_C_VERSION                      OpenCL C 1.2 
[AMD/0]     CL_DEVICE_TYPE                                  CL_DEVICE_TYPE_GPU
[AMD/0]     CL_DEVICE_MAX_COMPUTE_UNITS                     44
[AMD/0]     CL_DEVICE_MAX_CLOCK_FREQUENCY                   1080
```

Note: if I saved your life, you can make a donation on: https://liberapay.com/illwieckz/

If the time I spend on figuring out solutions and providing support for AMD GPU owners on various forums and places was valued in dollars, that would be a number with four zeros. I'm not an AMD employee.

---

### 评论 #36 — illwieckz (2020-11-16T05:05:20Z)

Note for AMD people like @jlgreathouse: refreshing the scripts to make it up to date for that previous comment and give support to @dagelf @Moading took me five hours. Can you forward that information to your employers? I'm available for any kind of contract.

---

### 评论 #37 — illwieckz (2020-11-17T04:22:14Z)

One thing more: beware to **NOT** mix the R9 390X GPUs (or other GCN ones) with a pre-GCN one. This will crash the OpenCL driver.

It may not sounds a bad idea for people doing heavy compute to fill all slots with powerful cards and if display is not a concern, to rely on a old graphic card because “it would be enough”. Or your CPU may have an integrated pre-GCN graphic chip. As soon as the radeon driver is loaded for at least one card, even one you don't use for compute, the OpenCL driver will crash.

See https://gitlab.freedesktop.org/drm/amd/-/issues/1193

For example, if your CPU is in fact a Piledriver based APU with a graphic chip branded HD 7000 or HD 8000 but being pre-GCN (Terascale) ones, you'll face the problem and will not be able to use the Orca AMDGPU-PRO OpenCL driver with your R9 390X. If so, you **need** to blacklist the `radeon` driver entirely, relying on the vesa fallback or something like that.

To do that you can do:

```sh
sudo tee /etc/modprobe.d/blacklist-radeon.conf >/dev/null <<\EOF
blacklist radeon
EOF

sudo update-initramfs -k all -u

sudo reboot
```

Note: I don't know if it's enough to fix such situation.

---

### 评论 #38 — ROCmSupport (2021-01-06T12:30:50Z)

Hi All,
R9 390X is no more officially ROCm supported device. Please check for more details: 
[https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)

---

### 评论 #39 — illwieckz (2021-01-06T20:55:26Z)

@ROCmSupport That's really bad practices from AMD, first, support fragmentation is hurting customers so it's hurting AMD. You may look at this [shameful thread from 2020](https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/opengl-vulkan-mesa-gallium3d/1219821-more-opencl-3-0-bits-merged-for-mesa-20-1/page2#post1220712) where AMD customers are complaining about support for Polaris not being supported by ROCm or R600 user who was still using fglrx in 2020…

About the R9 390X itself there was also some other threads were people testified they bought dozens of R9 390X in the past and were still waiting for support _to this day_, with a lot of sadness (like, for example [this comment](https://github.com/RadeonOpenCompute/ROCm/issues/484#issuecomment-727627405) on this thread).

@dagelf said less than two months ago:

> I bought 10 of these cards 4 years ago (!!!) to run workloads on... and have been held on a line by Readme's and message and issue threads now the whole time... not to mention the original marketing. it's been a really frustrating situation, I don't think I've been so patient about anything in my whole life. It's a lot of money that I've wasted...

Why do AMD continue to keep people experiencing their AMD buying as mistakes when it comes to GPU compute?

At the time I bought my R9 390X (GCN 2), the support for R9 Fury (GCN 3) was a disaster, neither free linux graphic driver and proprietary one were working, and this was a (sad) running gag on news websites like phoronix because this disaster lasted months (year?), that's why many people like me bought a GCN 2 (hence the R9 390X) instead at the time GCN 3 was already available _because it was unfortunately the safe option_. But even this card was never really properly supported, except for some short days years ago. Speaking of the R9 390X, [people reported power management problems](https://bugs.freedesktop.org/show_bug.cgi?id=91880) leading to system crashes (even preventing to install distributions) that were _never fixed_.

How can we get that page fixed? There is no ROCm for so many GPUs that are mistakenly marked as supported: https://www.x.org/wiki/RadeonFeature/

You may also want to close issues #565, #691, #694, #702, #784, #871, #906, #913, #1006, #1087 (a lot of people are waiting for Hawaii support being fixed)!

Note that in #702 @jlgreathouse said in 2019:

> Hawaii GPUs (such as your FirePro W8100) are currently broken on ROCm 2.0. We are working to fix this, but these fixes did not make it in to ROCm 2.1.

So much false hope…

---

### 评论 #40 — xuhuisheng (2021-01-06T21:28:19Z)

Not familar with OpenCL.
But there are many compiling issues for gfx701/gfx702, at least ROCm cannot support gfx7 now, I mean rocBLAS, rocSPARSE. they used gfx7 unsupported instinsts.
If there is even kernel or compiler issues, it is hard to support gfx7, indeed.

---

### 评论 #41 — illwieckz (2021-11-22T21:55:23Z)

ROCm still provides today a broken support for R9 R90X (gfx7) making the kernel require a reboot. It means for example one cannot host an R9 390X and a W6600 in the same host, expecting to get one driven by Orca and the other one by ROCm, the kernel will go wrong and OpenCL apps will hang, see #1624.

---
