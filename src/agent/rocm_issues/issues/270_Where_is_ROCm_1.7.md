# Where is ROCm 1.7

> **Issue #270**
> **状态**: closed
> **创建时间**: 2017-12-15T03:58:34Z
> **更新时间**: 2018-01-06T12:44:42Z
> **关闭时间**: 2017-12-20T04:04:07Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/270

## 描述

AMD Inverstors Relations release from Nov 13, http://ir.amd.com/phoenix.zhtml?c=74093&p=RssLanding&cat=news&id=2316438 talked about the "new ROCm 1.7":

"""
At SC17, AMD (NASDAQ:AMD) and its ecosystem partners announce immediate availability of a suite of new, high performance systems powered by AMD EPYC™ CPUs and AMD Radeon Instinct™ GPUs to accelerate innovation in supercomputing. AMD combines this broad portfolio with software, featuring the new ROCm 1.7 open platform with updated development tools and libraries, enabling complete AMD EPYC-based PetaFLOPS systems. 

AMD EPYC and AMD Radeon Instinct performance is fully supported by the new ROCm 1.7 release. Expanding on the most versatile open source software platform for heterogeneous computing systems, ROCm 1.7 delivers math libraries and software development support using modern programming languages to unlock the power of GPU acceleration and other accelerators like FPGAs. The ROCm 1.7 release includes multi-GPU support for the latest Radeon™ GPU hardware, as well as support for TensorFlow and Caffe in the MIOpen libraries.

The foundation for heterogeneous computing strategies is in place through the new AMD technology solution set formed from EPYC, Radeon Instinct, and ROCm 1.7. The availability of the P47 platform and the release of ROCm 1.7 are milestones that demonstrate how optimization and innovation are thriving at the hardware level.
"""


---

## 评论 (26 条)

### 评论 #1 — dfad44 (2017-12-16T02:19:07Z)

My guess, http://repo.radeon.com/misc/archive/beta/ is what's available for now. Hopefully Mr. G. Stoner can share some light on its progress for Ubuntu, perhaps waiting on update to be upstreamed for Kernel 4.15.

Twiddling thumbs!

---

### 评论 #2 — briansp2020 (2017-12-18T20:05:31Z)

Looks like 1.7 has landed!!! I can't wait to go home and try it.
No sign of Tensorflow 1.4 though...

Edit: Typed wrong version number.

---

### 评论 #3 — gstoner (2017-12-18T20:24:06Z)

We are rolling out Ubuntu today for ROCm 1.7  


---

### 评论 #4 — preda (2017-12-18T21:51:24Z)

I did an "sudo apt upgrade" on top of my existing ROCm 1.6, Ubuntu 16.04.3 installation, and it broke it.
I see that the rocm kernel stayed the same (1.6-180), even if some packages were upgraded to 1.7.

Is the new ROCm 1.7 coming with a new kernel? (if so, how to install that)
Is it supported on newer Ubuntu (then 16.04.3)?


---

### 评论 #5 — gstoner (2017-12-18T22:04:46Z)

It is new driver that uses DKMS so you want clean ubuntu kernel to start with. 

---

### 评论 #6 — preda (2017-12-18T22:09:17Z)

Should I try an install on Ubuntu 17.10? is there a chance?

---

### 评论 #7 — preda (2017-12-18T22:19:32Z)

If I do "apt install rocm", it attempts to install the kernel
linux-image-4.11.0-kfd-compute-rocm-rel-1.6-180
Why, if it does not need it?

$sudo apt install rocm
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  compute-firmware cxlactivitylogger g++-7-multilib g++-multilib gcc-7-multilib gcc-multilib hcc hip_base hip_doc hip_hcc hip_samples
  lib32asan4 lib32atomic1 lib32cilkrts5 lib32gcc-7-dev lib32gcc1 lib32gomp1 lib32itm1 lib32mpx2 lib32quadmath0 lib32stdc++-7-dev
  lib32stdc++6 lib32ubsan0 libc6-dev-i386 libc6-dev-x32 libc6-i386 libc6-x32 libunwind-dev libunwind8 libx32asan4 libx32atomic1
  libx32cilkrts5 libx32gcc-7-dev libx32gcc1 libx32gomp1 libx32itm1 libx32quadmath0 libx32stdc++-7-dev libx32stdc++6 libx32ubsan0
  linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-180 linux-image-4.11.0-kfd-compute-rocm-rel-1.6-180 rocm-dev rocm-device-libs
  rocm-profiler rocm-smi rocm-utils
Suggested packages:
  lib32stdc++6-7-dbg libx32stdc++6-7-dbg linux-firmware-image-4.11.0-kfd-compute-rocm-rel-1.6-180
The following NEW packages will be installed:
  compute-firmware cxlactivitylogger g++-7-multilib g++-multilib gcc-7-multilib gcc-multilib hcc hip_base hip_doc hip_hcc hip_samples
  lib32asan4 lib32atomic1 lib32cilkrts5 lib32gcc-7-dev lib32gcc1 lib32gomp1 lib32itm1 lib32mpx2 lib32quadmath0 lib32stdc++-7-dev
  lib32stdc++6 lib32ubsan0 libc6-dev-i386 libc6-dev-x32 libc6-i386 libc6-x32 libunwind-dev libunwind8 libx32asan4 libx32atomic1
  libx32cilkrts5 libx32gcc-7-dev libx32gcc1 libx32gomp1 libx32itm1 libx32quadmath0 libx32stdc++-7-dev libx32stdc++6 libx32ubsan0
  linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-180 linux-image-4.11.0-kfd-compute-rocm-rel-1.6-180 rocm rocm-dev rocm-device-libs
  rocm-profiler rocm-smi rocm-utils


---

### 评论 #8 — boxerab (2017-12-18T22:33:48Z)

When I tried to upgrade on Ubuntu 16, my installation was broken.

---

### 评论 #9 — preda (2017-12-18T22:34:13Z)

If I did an "sudo apt upgrade" on a good ROCm 1.6 (ubuntu 16.04.3), is there a way to roll back? to move back to ROCm 1.6. Otherwise I can't get any opencl on my Vega.

---

### 评论 #10 — preda (2017-12-18T22:47:56Z)

[   96.776676] BUG: unable to handle kernel paging request at ffffbc0bcf791000
[   96.776715] IP: memset_erms+0x9/0x10
[   96.776728] PGD 103f89b067 
[   96.776728] PUD 203f001067 
[   96.776738] PMD 1033c0e067 
[   96.776747] PTE 0

[   96.776770] Oops: 0002 [#1] SMP
[   96.776781] Modules linked in: intel_rapl sb_edac edac_core x86_pkg_temp_thermal intel_powerclamp coretemp kvm snd_hda_codec_realtek snd_hda_codec_generic irqbypass snd_hda_codec_hdmi crct10dif_pclmul crc32_pclmul ghash_clmulni_intel snd_hda_intel cryptd snd_hda_codec snd_seq_midi snd_hda_core snd_seq_midi_event snd_hwdep snd_rawmidi input_leds snd_pcm snd_seq snd_seq_device snd_timer snd soundcore lpc_ich shpchp ioatdma acpi_power_meter mac_hid parport_pc ppdev lp parport autofs4 amdkfd amd_iommu_v2 amdgpu igb ttm dca drm_kms_helper ptp syscopyarea sysfillrect hid_generic sysimgblt usbhid fb_sys_fops mxm_wmi ahci pps_core drm hid i2c_algo_bit libahci wmi
[   96.776979] CPU: 15 PID: 2518 Comm: gpuowl Not tainted 4.11.0-kfd-compute-rocm-rel-1.6-180 #1
[   96.777004] Hardware name: Supermicro X10DAi/X10DAI, BIOS 2.0 02/02/2016
[   96.777025] task: ffff9d31f499e200 task.stack: ffffbc0bce9a8000
[   96.777045] RIP: 0010:memset_erms+0x9/0x10
[   96.777059] RSP: 0018:ffffbc0bce9abd00 EFLAGS: 00010286
[   96.777076] RAX: ffff9d31f5c818ff RBX: 0000000000000008 RCX: 0000000000001000
[   96.777098] RDX: 0000000000009000 RSI: 00000000000000ff RDI: ffffbc0bcf791000
[   96.777120] RBP: ffffbc0bce9abd48 R08: ffff9d423fdde440 R09: ffffbc0bcf789000
[   96.777141] R10: ffff9d31f5c81800 R11: 0000000000000501 R12: ffff9d31f6652560
[   96.777163] R13: ffff9d41f4142f80 R14: ffffbc0bce9abdf8 R15: ffff9d31f6652400
[   96.777185] FS:  00007fd052475740(0000) GS:ffff9d423fdc0000(0000) knlGS:0000000000000000
[   96.777209] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[   96.777227] CR2: ffffbc0bcf791000 CR3: 00000010364b6000 CR4: 00000000001406e0
[   96.777249] Call Trace:
[   96.777267]  ? kfd_event_create+0x36c/0x550 [amdkfd]
[   96.777287]  kfd_ioctl_create_event+0x8a/0x160 [amdkfd]
[   96.777308]  kfd_ioctl+0x241/0x3f0 [amdkfd]
[   96.777325]  ? kfd_ioctl_destroy_event+0x20/0x20 [amdkfd]
[   96.777346]  ? common_mmap+0x48/0x50
[   96.777359]  ? apparmor_mmap_file+0x18/0x20
[   96.777376]  do_vfs_ioctl+0x92/0x5a0
[   96.777389]  SyS_ioctl+0x79/0x90
[   96.777402]  entry_SYSCALL_64_fastpath+0x1e/0xad
[   96.777417] RIP: 0033:0x7fd0514fef07
[   96.777429] RSP: 002b:00007ffe817c1818 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[   96.777452] RAX: ffffffffffffffda RBX: 00007ffe817c18f0 RCX: 00007fd0514fef07
[   96.777474] RDX: 00007ffe817c1870 RSI: 00000000c0204b08 RDI: 0000000000000006
[   96.777495] RBP: 00007ffe817c18e8 R08: 0000000000000000 R09: 604ac00101003000
[   96.777517] R10: 0000000000000011 R11: 0000000000000246 R12: 0000000000000000
[   96.777538] R13: 00007fd04d005d60 R14: 0000000000000001 R15: 0000000001d565b0
[   96.777560] Code: 48 c1 e9 03 40 0f b6 f6 48 b8 01 01 01 01 01 01 01 01 48 0f af c6 f3 48 ab 89 d1 f3 aa 4c 89 c8 c3 90 49 89 f9 40 88 f0 48 89 d1 <f3> aa 4c 89 c8 c3 90 49 89 fa 40 0f b6 ce 48 b8 01 01 01 01 01 
[   96.777637] RIP: memset_erms+0x9/0x10 RSP: ffffbc0bce9abd00
[   96.777654] CR2: ffffbc0bcf791000

---

### 评论 #11 — gstoner (2017-12-18T23:06:32Z)

There are new install instructions when you install with DKMS,  you will need to follow.  They are just rolling these out now.    Guy this is DKMS install you will need Ubuntu 16.04 standard kernel install which driver attaches to.   

Prior to any install, you need to execute the following commands:
sudo apt-get clean all, we have some new step that are being posted. 



---

### 评论 #12 — preda (2017-12-18T23:15:44Z)

Where can I find the new installation steps?

Maybe you can post them here in the meantime, if there's delay in publishing them. The thing is that a simple "apt upgrade" does break the good install, so probably you want to fix that too.

"sudo apt clean all" ? doesn't seem to do anything.

---

### 评论 #13 — preda (2017-12-18T23:18:16Z)

For my part, I'd be happy with even just a rollback to "good old" ROCm 1.6, which should fix my system.

---

### 评论 #14 — gstoner (2017-12-19T00:57:00Z)

We archive all the release goto repo.radeon.com. You find 1.6.4 there

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Mihai Preda <notifications@github.com>
Sent: Monday, December 18, 2017 5:18:17 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] Where is ROCm 1.7 (#270)


For my part, I'd be happy with even just a rollback to "good old" ROCm 1.6, which should fix my system.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/270#issuecomment-352589019>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuRbQyG6DOAPKUxFwgr-mXq43BEsbks5tBvK5gaJpZM4RC_FM>.


---

### 评论 #15 — preda (2017-12-19T01:37:16Z)

OK thanks. It appears repo.radeon.com has also rolled-back to 1.6 (for now).
The versions of different packages can be seen here: http://repo.radeon.com/rocm/apt/debian/dists/xenial/main/binary-amd64/Packages

---

### 评论 #16 — hwchong (2017-12-19T08:52:42Z)

I'm getting this error: 

Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package rocm-dkms

Looks like the repo hasn't been updated yet. 

---

### 评论 #17 — extraymond (2017-12-20T00:48:43Z)

It's up now. Really excited to try rocm!!!

---

### 评论 #18 — gstoner (2017-12-20T01:43:10Z)

One. Check to make sure your user name is in the.         “ gpu”Unix permisions group post install

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: extraymond <notifications@github.com>
Sent: Tuesday, December 19, 2017 6:48:45 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] Where is ROCm 1.7 (#270)


It's up now. Really excited to try rocm!!!

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/270#issuecomment-352931564>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSOU4N4B8i2IPv8x7VfQHfBRl_v2ks5tCFltgaJpZM4RC_FM>.


---

### 评论 #19 — extraymond (2017-12-20T01:51:52Z)

@gstoner Thx for the heads-up

I can already use Opencl without being in the group(which doesn't exist in my system), what should I expect to be in the group? I have created the gpu group and added my user into it.

---

### 评论 #20 — gstoner (2017-12-20T03:34:30Z)

Here is the exact command   sudo usermod -a -G video <username>

Sorry I was at Dinner with the Family downtown for event 

---

### 评论 #21 — extraymond (2017-12-20T03:58:38Z)

Ah! OK, I thought the group name was "gpu". I'll try again with "vdeo" and see what's changed.
Have a good time.


---

### 评论 #22 — gstoner (2017-12-20T04:00:14Z)

Here is the full command 
sudo usermod -a -G video <username>

---

### 评论 #23 — gstoner (2017-12-20T04:00:36Z)

sudo usermod -a -G video "username"

---

### 评论 #24 — gstoner (2017-12-20T04:02:39Z)

Looks like when using  "<" username ">" without the quotes git was not displaying it. 

---

### 评论 #25 — VincentSC (2018-01-04T17:16:24Z)

To add all users with bash-access to 'video':
`for u in $(less /etc/passwd | grep bash | cut -d : -f 1); do sudo usermod -a -G video $u; done`

---

### 评论 #26 — VincentSC (2018-01-06T12:44:42Z)

@gstoner, simply use back-quotes, then it looks like this: `sudo usermod -a -G video <username>`

---
