# Crash and excessive messages written to kern.log file with 1.7.60

> **Issue #368**
> **状态**: closed
> **创建时间**: 2018-03-20T17:17:36Z
> **更新时间**: 2018-05-12T23:04:48Z
> **关闭时间**: 2018-05-12T13:11:44Z
> **作者**: Runeerle
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/368

## 描述

Hi,

After I installed ROCm there seems to be an error that generates too many messages in kern.log.
The current kern.log file is 3.4 GiB from just 53 hours of logs. And every log file after the install is large.

**I get up to 285 KiB/s of this text in my kern.log file:**
Mar 20 14:11:33 _name_ kernel: [528534.415895] [drm:handle_cursor_update.isra.30 [amdgpu]] handle_cursor_update: crtc_id=0 with size 128 to 128
Mar 20 14:11:33 _name_ kernel: [528534.416603] [drm:amdgpu_dm_atomic_check [amdgpu]] amdgpu_crtc id:0 crtc_state_flags: enable:1, active:1, planes_changed:0, mode_changed:0,active_changed:0,connectors_changed:0
Mar 20 14:11:33 _name_ kernel: [528534.416682] [drm:amdgpu_dm_atomic_commit_tail [amdgpu]] amdgpu_crtc id:0 crtc_state_flags: enable:1, active:1, planes_changed:1, mode_changed:0,active_changed:0,connectors_changed:0
Mar 20 14:11:33 _name_ kernel: [528534.416748] [drm:modeset_required [amdgpu]] Mode change not required, setting mode_changed to 0
...
The same 4 lines just repeats unmodified as far as I can tell, except for the time-stamp. It also seems to be generated when I move my mouse.


**In addition these lines are added ~every second:**
Mar 20 14:11:33 _name_ kernel: [528534.458385] [drm:prepare_flip_isr [amdgpu]] crtc:0, pflip_stat:AMDGPU_FLIP_SUBMITTED
Mar 20 14:11:33 _name_ kernel: [528534.458452] [drm:amdgpu_dm_do_flip [amdgpu]] amdgpu_dm_do_flip Flipping to hi: 0xf4, low: 0xf9140000 
Mar 20 14:11:33 _name_ kernel: [528534.461795] [drm:dm_pflip_high_irq [amdgpu]] dm_pflip_high_irq - crtc :0[ffff9ad48ec4a000], pflip_stat:AMDGPU_FLIP_NONE
Mar 20 14:11:33 _name_ kernel: [528534.474072] [drm:prepare_flip_isr [amdgpu]] crtc:0, pflip_stat:AMDGPU_FLIP_SUBMITTED
Mar 20 14:11:33 _name_ kernel: [528534.474141] [drm:amdgpu_dm_do_flip [amdgpu]] amdgpu_dm_do_flip Flipping to hi: 0xf4, low: 0xd2d80000 
Mar 20 14:11:33 _name_ kernel: [528534.478487] [drm:dm_pflip_high_irq [amdgpu]] dm_pflip_high_irq - crtc :0[ffff9ad48ec4a000], pflip_stat:AMDGPU_FLIP_NONE
...

**Then, every few seconds this is added:**
Mar 20 14:11:56 _name_ kernel: [528557.291929] [drm:dm_plane_helper_prepare_fb [amdgpu]] No FB bound
Mar 20 14:11:56 _name_ kernel: [528557.292180] [drm:handle_cursor_update.isra.30 [amdgpu]] handle_cursor_update: crtc_id=0 with size 0 to 0
...

**Finally, the first crash seems to come from dc_plane_state_retain:**
Mar 20 14:33:19 _name_ kernel: [529839.855466] ------------[ cut here ]------------
Mar 20 14:33:19 _name_ kernel: [529839.855560] WARNING: CPU: 5 PID: 1398 at /var/lib/dkms/rock/1.7.60-ubuntu/build/amd/amdgpu/../display/dc/core/dc_surface.c:125 dc_plane_state_retain+0x1e/0x30 [amdgpu]
Mar 20 14:33:19 _name_ kernel: [529839.855561] Modules linked in: binfmt_misc snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm intel_rapl snd_seq_midi snd_seq_midi_event x86_pkg_temp_thermal intel_powerclamp snd_rawmidi coretemp crct10dif_pclmul input_leds crc32_pclmul ghash_clmulni_intel pcbc snd_seq snd_seq_device aesni_intel snd_timer aes_x86_64 crypto_simd glue_helper cryptd intel_cstate snd intel_rapl_perf mei_me lpc_ich mei soundcore shpchp mac_hid kvm_intel kvm irqbypass nfsd auth_rpcgss nfs_acl lockd grace sunrpc parport_pc ppdev lp parport autofs4 btrfs xor raid6_pq hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdttm(OE) mxm_wmi amdkcl(OE) i2c_algo_bit drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops e1000e drm alx ptp ahci mdio
Mar 20 14:33:19 _name_ kernel: [529839.855630]  nvme pps_core libahci nvme_core wmi
Mar 20 14:33:19 _name_ kernel: [529839.855640] CPU: 5 PID: 1398 Comm: Xorg Tainted: G        W  OE   4.13.0-36-generic #40~16.04.1-Ubuntu
Mar 20 14:33:19 _name_ kernel: [529839.855641] Hardware name: To Be Filled By O.E.M. To Be Filled By O.E.M./X99 OC Formula, BIOS P1.10 09/02/2014
Mar 20 14:33:19 _name_ kernel: [529839.855644] task: ffff9ad490ab5d00 task.stack: ffffb18f04d88000
Mar 20 14:33:19 _name_ kernel: [529839.855731] RIP: 0010:dc_plane_state_retain+0x1e/0x30 [amdgpu]
Mar 20 14:33:19 _name_ kernel: [529839.855734] RSP: 0018:ffffb18f04d8bb88 EFLAGS: 00010246
Mar 20 14:33:19 _name_ kernel: [529839.855736] RAX: 0000000000000000 RBX: ffff9ad48fbf3380 RCX: 000000000000004f
Mar 20 14:33:19 _name_ kernel: [529839.855738] RDX: ffffffffc03b97a1 RSI: 0000000000000001 RDI: ffff9ad48cfac400
Mar 20 14:33:19 _name_ kernel: [529839.855740] RBP: ffffb18f04d8bb88 R08: 0000000000000003 R09: ffff9ad49ec03500
Mar 20 14:33:19 _name_ kernel: [529839.855742] R10: ffffb18f04d8bb70 R11: 0000000000000040 R12: ffff9ad48f994400
Mar 20 14:33:19 _name_ kernel: [529839.855744] R13: ffff9ad48fbf3900 R14: 0000000000000000 R15: ffff9ad48fbf3300
Mar 20 14:33:19 _name_ kernel: [529839.855747] FS:  00007fc173e20a00(0000) GS:ffff9ad49f340000(0000) knlGS:0000000000000000
Mar 20 14:33:19 _name_ kernel: [529839.855748] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Mar 20 14:33:19 _name_ kernel: [529839.855750] CR2: 00007fc15c0fa000 CR3: 000000084cc44001 CR4: 00000000001606e0
Mar 20 14:33:19 _name_ kernel: [529839.855752] Call Trace:
Mar 20 14:33:19 _name_ kernel: [529839.855846]  dm_drm_plane_duplicate_state+0x53/0x70 [amdgpu]
Mar 20 14:33:19 _name_ kernel: [529839.855876]  drm_atomic_get_plane_state+0x7f/0x120 [drm]
Mar 20 14:33:19 _name_ kernel: [529839.855894]  page_flip_common+0x5b/0xd0 [drm_kms_helper]
Mar 20 14:33:19 _name_ kernel: [529839.855905]  drm_atomic_helper_page_flip+0x59/0xb0 [drm_kms_helper]
Mar 20 14:33:19 _name_ kernel: [529839.855925]  drm_mode_page_flip_ioctl+0x469/0x510 [drm]
Mar 20 14:33:19 _name_ kernel: [529839.855945]  ? drm_mode_cursor2_ioctl+0x10/0x10 [drm]
Mar 20 14:33:19 _name_ kernel: [529839.855962]  drm_ioctl_kernel+0x6b/0xb0 [drm]
Mar 20 14:33:19 _name_ kernel: [529839.855978]  drm_ioctl+0x3e4/0x450 [drm]
Mar 20 14:33:19 _name_ kernel: [529839.855997]  ? drm_mode_cursor2_ioctl+0x10/0x10 [drm]
Mar 20 14:33:19 _name_ kernel: [529839.856003]  ? ep_ptable_queue_proc+0xa0/0xa0
Mar 20 14:33:19 _name_ kernel: [529839.856007]  ? timerqueue_add+0x59/0x90
Mar 20 14:33:19 _name_ kernel: [529839.856066]  amdgpu_drm_ioctl+0x4c/0x80 [amdgpu]
Mar 20 14:33:19 _name_ kernel: [529839.856071]  do_vfs_ioctl+0xa4/0x600
Mar 20 14:33:19 _name_ kernel: [529839.856076]  ? __sys_recvmsg+0x51/0x90
Mar 20 14:33:19 _name_ kernel: [529839.856080]  ? __sys_recvmsg+0x80/0x90
Mar 20 14:33:19 _name_ kernel: [529839.856084]  SyS_ioctl+0x79/0x90
Mar 20 14:33:19 _name_ kernel: [529839.856089]  entry_SYSCALL_64_fastpath+0x24/0xab
Mar 20 14:33:19 _name_ kernel: [529839.856091] RIP: 0033:0x7fc171856f47
Mar 20 14:33:19 _name_ kernel: [529839.856093] RSP: 002b:00007fffdfa24f08 EFLAGS: 00003246 ORIG_RAX: 0000000000000010
Mar 20 14:33:19 _name_ kernel: [529839.856097] RAX: ffffffffffffffda RBX: 000055988180b0f0 RCX: 00007fc171856f47
Mar 20 14:33:19 _name_ kernel: [529839.856098] RDX: 00007fffdfa24f40 RSI: 00000000c01864b0 RDI: 000000000000000d
Mar 20 14:33:19 _name_ kernel: [529839.856100] RBP: 000055987fec1f20 R08: 0000000000116997 R09: 000000000059dfa6
Mar 20 14:33:19 _name_ kernel: [529839.856102] R10: 0000000000000000 R11: 0000000000003246 R12: 000055987ffe9de0
Mar 20 14:33:19 _name_ kernel: [529839.856103] R13: 00005598817ce748 R14: 0000559881179e30 R15: 00007fffdfa25148
Mar 20 14:33:19 _name_ kernel: [529839.856106] Code: eb d9 31 c0 eb d5 0f 1f 80 00 00 00 00 0f 1f 44 00 00 8b 87 cc 01 00 00 55 48 89 e5 85 c0 7e 0b 83 c0 01 89 87 cc 01 00 00 5d c3 <0f> ff 83 c0 01 89 87 cc 01 00 00 5d c3 0f 1f 44 00 00 0f 1f 44 
Mar 20 14:33:19 _name_ kernel: [529839.856161] ---[ end trace e4c26297d508b1de ]---

Here is a filtered log without the repeating messages:
https://gist.github.com/Runeerle/058df599ddc2d517ec8ac6236ccc2798

My configuration:
rocm version 1.7.60, installed from http://repo.radeon.com/rocm/apt/debian, ~4 weeks ago.
I have not yet updated to version 1.7.137.

GPU:
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 550 640SP / RX 560] (rev cf)

uname -a:
Linux _name_ 4.13.0-36-generic #40~16.04.1-Ubuntu SMP Fri Feb 16 23:25:58 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

gcc --version:
gcc (Ubuntu 5.4.1-2ubuntu1~16.04) 5.4.1 2016090

In addition the system have been unstable, even with light usage. When the system dies only the mouse pointer works, even Ctrl+Alt+F1 do not work.


---

## 评论 (9 条)

### 评论 #1 — davclark (2018-03-29T00:33:00Z)

I'm seeing the same. Almost exactly the same installation, but I AM updated to 1.7.137. System was stable on AMDGPU pro - experienced crash after switching to open source drivers.

---

### 评论 #2 — ghost (2018-03-29T11:21:26Z)

This is a unrelated driver issue, I have seen it and fixed it on the dev build system I made. In my case it will and can be duplicated by the r8168 stock nic driver.  kvm_intel kvm irqbypass nfsd auth_rpcgss nfs_acl lockd grace sunrpc parport_pc ppdev lp parport autofs4 btrfs xor raid6_pq hid_generic 

Looking at your drivers I can see that you still have your parallel port tieing up irqs and kvm and nfs?

Are you running remote clients thata tftp boot and then are connected to a 1980's printer :)

Remember you add dkms modules into the kernel on ubuntu it will load alot of crap that you do not want or need. Here is the script I use to first black list a module in /etc/modprobe.d/blacklist.conf
paraport ppdev for example 
blacklist paraport 
blacklist ppdev
blacklist r8169

Then try 
cat /etc/modprobe.d/blacklist.conf | grep blacklist | sed s/blacklist//g  | xargs rmmod
to remove all the blacklisted modules.

---

### 评论 #3 — ghost (2018-03-29T11:27:14Z)

Mar 20 14:33:19 _name_ kernel: [529839.952797] Modules linked in: binfmt_misc snd_hda_codec_realtek snd_hda_codec_generic snd_hda_codec_hdmi snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep snd_pcm intel_rapl snd_seq_midi snd_seq_midi_event x86_pkg_temp_thermal intel_powerclamp snd_rawmidi coretemp crct10dif_pclmul input_leds crc32_pclmul ghash_clmulni_intel pcbc snd_seq snd_seq_device aesni_intel snd_timer aes_x86_64 crypto_simd glue_helper cryptd intel_cstate snd intel_rapl_perf mei_me lpc_ich mei soundcore shpchp mac_hid kvm_intel kvm irqbypass nfsd auth_rpcgss nfs_acl lockd grace sunrpc parport_pc ppdev lp parport autofs4 btrfs xor raid6_pq hid_generic usbhid hid amdkfd(OE) amd_iommu_v2 amdgpu(OE) amdttm(OE) mxm_wmi amdkcl(OE) i2c_algo_bit drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops e1000e drm alx ptp ahci mdio
Mar 20 14:33:19 _name_ kernel: [529839.952861]  nvme pps_core libahci nvme_core wmi

Mar 20 14:33:19 _name_ kernel: [529839.952869] CPU: 5 PID: 1398 Comm: Xorg Tainted: G        W  OE   4.13.0-36-generic #40~16.04.1-Ubuntu

Please try the following to fix the problem 
apt-get install linux-image-4.13.0-32-generic
apt-get --purge remove *4.13.0-36*
When you updated you updated from the 16.04.3 to the 16.04.4 kernel which has this issue :)
Thank you and have a nice day

---

### 评论 #4 — ghost (2018-03-30T09:13:30Z)

You might want to try the following grub line 
GRUB_CMDLINE_LINUX_DEFAULT="init=/lib/sysvinit/init apparmor=0 security="" selinux=0 amdgpu.vm_fragment_size=9 nmi_watchdog=0 pti=off 3 spectre_v2=off nospectre_v2 retp=0 ibrs=0 ibpb=0 amdgpu.hw_i2c=1 isolcpus=5,6,7 nohz_full=5,6,7 processor.max_cstate=1 radeon.clk_support=0 amdgpu.clk_support=1 intel_pstate=disable audit=0 thermal.off=1 clocksource=hpet intel_iommu=on iommu=pt"

---

### 评论 #5 — Runeerle (2018-04-16T13:39:53Z)

I have blacklisted the r8169, ppdev and paraport driver, switched to 4.13.0-32-generic and updated to rocm 1.7.137. However there are **still crashes**.
It also seems the reason the log is so massive is a grub option 'drm.debug=0xe'. 


> GRUB_CMDLINE_LINUX_DEFAULT="init=/lib/sysvinit/init apparmor=0 security="" selinux=0 amdgpu.vm_fragment_size=9 nmi_watchdog=0 pti=off 3 spectre_v2=off nospectre_v2 retp=0 ibrs=0 ibpb=0 amdgpu.hw_i2c=1 isolcpus=5,6,7 nohz_full=5,6,7 processor.max_cstate=1 radeon.clk_support=0 amdgpu.clk_support=1 intel_pstate=disable audit=0 thermal.off=1 clocksource=hpet intel_iommu=on iommu=pt"

This seems to be tuned to a custom mining setup. I can not use the grub line unmodified however. This is my workstation at work, and disabling security is not a real option.

This set of options disable lots of security features:
apparmor=0 -- Disable normal security
selinux=0 -- Useless on Ubuntu (disable security)
pti=off 3  -- Spectre/Meltdown
spectre_v2=off -- Spectre/Meltdown
nospectre_v2 -- Spectre/Meltdown
retp=0 -- Spectre/Meltdown
ibrs=0 -- Spectre/Meltdown
ibpb=0 -- Spectre/Meltdown

Is it likely these security features impact the crash issue?


This will remove 3 of my 12 CPU threads:
isolcpus=5,6,7 -- Remove CPU 5,6 and 7 from the system :(
nohz_full=5,6,7 -- Set CPU  5,6 and 7 to be in adaptive-ticks mode "reduce the number of scheduling-clock interrupts" ?

The system is stable with 100% load on all cores for days, and all crash scenarios have been in ~1-5% load.


More interrupts disabled:
nmi_watchdog=0 -- CPU crash handling (interrupt)

Is the cause related to interrupts?


Disable all CPU energy optimizations:
processor.max_cstate=1 -- Disable all CPU sleep/low-power states. 
intel_pstate=disable -- Disable the Intel CPU frequency/performance handler.

Is the crash related to CPUsleep states?


Enable features for VM's:
intel_iommu=on  -- Used to speed up a VM's access to hardware
iommu=pt" -- Used to speed up a VM's access to hardware

I do not run any VM's, but will this set of options impact the GPU driver anyway?


Other options:
audit=0   -- Disable various logging features. ?
thermal.off=1 -- Disable ACPI thermal support ?
clocksource=hpet -- Change timers from TSC to HPET (slower) ?

I don't see why any of those options can cause a crash, unless they generate interrupts somehow. Are they likely to be related to the crash issue?

GPU driver related options:
amdgpu.vm_fragment_size=9 -- Use 2 MiB page size.
amdgpu.hw_i2c=1 -- Enable temperature sensor?
radeon.clk_support=0 -- Useless?
amdgpu.clk_support=1 -- ?

Only the vm_fragment_size seems relevant, but it seems to be intended to improve crypto-mining.
So far every crash seems to have happened when I have tried to **move the mouse** after writing some text, and all the logs are also related to moving the mouse. So this is not likely to happen in a mining system at all.

Is the best way to get a stable system to switch to AMDGPU pro with my setup, or are there other things I can try?

---

### 评论 #6 — ghost (2018-04-16T14:39:45Z)

Close it is most likely from, the virtualization in the bios. disable it
vxd..

On Mon, Apr 16, 2018 at 8:43 PM, Runeerle <notifications@github.com> wrote:

> I have blacklisted the r8169, ppdev and paraport driver, switched to
> 4.13.0-32-generic and updated to rocm 1.7.137. However there are *still
> crashes*.
> It also seems the reason the log is so massive is a grub option
> 'drm.debug=0xe'.
>
> GRUB_CMDLINE_LINUX_DEFAULT="init=/lib/sysvinit/init apparmor=0
> security="" selinux=0 amdgpu.vm_fragment_size=9 nmi_watchdog=0 pti=off 3
> spectre_v2=off nospectre_v2 retp=0 ibrs=0 ibpb=0 amdgpu.hw_i2c=1
> isolcpus=5,6,7 nohz_full=5,6,7 processor.max_cstate=1 radeon.clk_support=0
> amdgpu.clk_support=1 intel_pstate=disable audit=0 thermal.off=1
> clocksource=hpet intel_iommu=on iommu=pt"
>
> This seems to be tuned to a custom mining setup. I can not use the grub
> line unmodified however. This is my workstation at work, and disabling
> security is not a real option.
>
> This set of options disable lots of security features:
> apparmor=0 -- Disable normal security
> selinux=0 -- Useless on Ubuntu (disable security)
> pti=off 3 -- Spectre/Meltdown
> spectre_v2=off -- Spectre/Meltdown
> nospectre_v2 -- Spectre/Meltdown
> retp=0 -- Spectre/Meltdown
> ibrs=0 -- Spectre/Meltdown
> ibpb=0 -- Spectre/Meltdown
>
> Is it likely these security features impact the crash issue?
>
> This will remove 3 of my 12 CPU threads:
> isolcpus=5,6,7 -- Remove CPU 5,6 and 7 from the system :(
> nohz_full=5,6,7 -- Set CPU 5,6 and 7 to be in adaptive-ticks mode "reduce
> the number of scheduling-clock interrupts" ?
>
> The system is stable with 100% load on all cores for days, and all crash
> scenarios have been in ~1-5% load.
>
> More interrupts disabled:
> nmi_watchdog=0 -- CPU crash handling (interrupt)
>
> Is the cause related to interrupts?
>
> Disable all CPU energy optimizations:
> processor.max_cstate=1 -- Disable all CPU sleep/low-power states.
> intel_pstate=disable -- Disable the Intel CPU frequency/performance
> handler.
>
> Is the crash related to CPUsleep states?
>
> Enable features for VM's:
> intel_iommu=on -- Used to speed up a VM's access to hardware
> iommu=pt" -- Used to speed up a VM's access to hardware
>
> I do not run any VM's, but will this set of options impact the GPU driver
> anyway?
>
> Other options:
> audit=0 -- Disable various logging features. ?
> thermal.off=1 -- Disable ACPI thermal support ?
> clocksource=hpet -- Change timers from TSC to HPET (slower) ?
>
> I don't see why any of those options can cause a crash, unless they
> generate interrupts somehow. Are they likely to be related to the crash
> issue?
>
> GPU driver related options:
> amdgpu.vm_fragment_size=9 -- Use 2 MiB page size.
> amdgpu.hw_i2c=1 -- Enable temperature sensor?
> radeon.clk_support=0 -- Useless?
> amdgpu.clk_support=1 -- ?
>
> Only the vm_fragment_size seems relevant, but it seems to be intended to
> improve crypto-mining.
> So far every crash seems to have happened when I have tried to *move the
> mouse* after writing some text, and all the logs are also related to
> moving the mouse. So this is not likely to happen in a mining system at all.
>
> Is the best way to get a stable system to switch to AMDGPU pro with my
> setup, or are there other things I can try?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/368#issuecomment-381602731>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w5IuKSVzGvdVH6gNMMHFtBnh7G0aks5tpJ_ugaJpZM4SyT6L>
> .
>


---

### 评论 #7 — ghost (2018-04-16T14:41:06Z)

Im building the workstation version of the dev test setup, Would you like
to test it?.  Please contact me directly.

On Mon, Apr 16, 2018 at 9:39 PM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> Close it is most likely from, the virtualization in the bios. disable it
> vxd..
>
> On Mon, Apr 16, 2018 at 8:43 PM, Runeerle <notifications@github.com>
> wrote:
>
>> I have blacklisted the r8169, ppdev and paraport driver, switched to
>> 4.13.0-32-generic and updated to rocm 1.7.137. However there are *still
>> crashes*.
>> It also seems the reason the log is so massive is a grub option
>> 'drm.debug=0xe'.
>>
>> GRUB_CMDLINE_LINUX_DEFAULT="init=/lib/sysvinit/init apparmor=0
>> security="" selinux=0 amdgpu.vm_fragment_size=9 nmi_watchdog=0 pti=off 3
>> spectre_v2=off nospectre_v2 retp=0 ibrs=0 ibpb=0 amdgpu.hw_i2c=1
>> isolcpus=5,6,7 nohz_full=5,6,7 processor.max_cstate=1 radeon.clk_support=0
>> amdgpu.clk_support=1 intel_pstate=disable audit=0 thermal.off=1
>> clocksource=hpet intel_iommu=on iommu=pt"
>>
>> This seems to be tuned to a custom mining setup. I can not use the grub
>> line unmodified however. This is my workstation at work, and disabling
>> security is not a real option.
>>
>> This set of options disable lots of security features:
>> apparmor=0 -- Disable normal security
>> selinux=0 -- Useless on Ubuntu (disable security)
>> pti=off 3 -- Spectre/Meltdown
>> spectre_v2=off -- Spectre/Meltdown
>> nospectre_v2 -- Spectre/Meltdown
>> retp=0 -- Spectre/Meltdown
>> ibrs=0 -- Spectre/Meltdown
>> ibpb=0 -- Spectre/Meltdown
>>
>> Is it likely these security features impact the crash issue?
>>
>> This will remove 3 of my 12 CPU threads:
>> isolcpus=5,6,7 -- Remove CPU 5,6 and 7 from the system :(
>> nohz_full=5,6,7 -- Set CPU 5,6 and 7 to be in adaptive-ticks mode "reduce
>> the number of scheduling-clock interrupts" ?
>>
>> The system is stable with 100% load on all cores for days, and all crash
>> scenarios have been in ~1-5% load.
>>
>> More interrupts disabled:
>> nmi_watchdog=0 -- CPU crash handling (interrupt)
>>
>> Is the cause related to interrupts?
>>
>> Disable all CPU energy optimizations:
>> processor.max_cstate=1 -- Disable all CPU sleep/low-power states.
>> intel_pstate=disable -- Disable the Intel CPU frequency/performance
>> handler.
>>
>> Is the crash related to CPUsleep states?
>>
>> Enable features for VM's:
>> intel_iommu=on -- Used to speed up a VM's access to hardware
>> iommu=pt" -- Used to speed up a VM's access to hardware
>>
>> I do not run any VM's, but will this set of options impact the GPU driver
>> anyway?
>>
>> Other options:
>> audit=0 -- Disable various logging features. ?
>> thermal.off=1 -- Disable ACPI thermal support ?
>> clocksource=hpet -- Change timers from TSC to HPET (slower) ?
>>
>> I don't see why any of those options can cause a crash, unless they
>> generate interrupts somehow. Are they likely to be related to the crash
>> issue?
>>
>> GPU driver related options:
>> amdgpu.vm_fragment_size=9 -- Use 2 MiB page size.
>> amdgpu.hw_i2c=1 -- Enable temperature sensor?
>> radeon.clk_support=0 -- Useless?
>> amdgpu.clk_support=1 -- ?
>>
>> Only the vm_fragment_size seems relevant, but it seems to be intended to
>> improve crypto-mining.
>> So far every crash seems to have happened when I have tried to *move the
>> mouse* after writing some text, and all the logs are also related to
>> moving the mouse. So this is not likely to happen in a mining system at all.
>>
>> Is the best way to get a stable system to switch to AMDGPU pro with my
>> setup, or are there other things I can try?
>>
>> —
>> You are receiving this because you commented.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/368#issuecomment-381602731>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0w5IuKSVzGvdVH6gNMMHFtBnh7G0aks5tpJ_ugaJpZM4SyT6L>
>> .
>>
>
>


---

### 评论 #8 — ghost (2018-04-16T19:32:58Z)

Send me a pm on google, I already have a 4.17 live persistant test version
for you to try desktop xubuntu based.

On Mon, Apr 16, 2018 at 9:41 PM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> Im building the workstation version of the dev test setup, Would you like
> to test it?.  Please contact me directly.
>
> On Mon, Apr 16, 2018 at 9:39 PM, Jason Kurtz <tekcommnv@gmail.com> wrote:
>
>> Close it is most likely from, the virtualization in the bios. disable it
>> vxd..
>>
>> On Mon, Apr 16, 2018 at 8:43 PM, Runeerle <notifications@github.com>
>> wrote:
>>
>>> I have blacklisted the r8169, ppdev and paraport driver, switched to
>>> 4.13.0-32-generic and updated to rocm 1.7.137. However there are *still
>>> crashes*.
>>> It also seems the reason the log is so massive is a grub option
>>> 'drm.debug=0xe'.
>>>
>>> GRUB_CMDLINE_LINUX_DEFAULT="init=/lib/sysvinit/init apparmor=0
>>> security="" selinux=0 amdgpu.vm_fragment_size=9 nmi_watchdog=0 pti=off 3
>>> spectre_v2=off nospectre_v2 retp=0 ibrs=0 ibpb=0 amdgpu.hw_i2c=1
>>> isolcpus=5,6,7 nohz_full=5,6,7 processor.max_cstate=1 radeon.clk_support=0
>>> amdgpu.clk_support=1 intel_pstate=disable audit=0 thermal.off=1
>>> clocksource=hpet intel_iommu=on iommu=pt"
>>>
>>> This seems to be tuned to a custom mining setup. I can not use the grub
>>> line unmodified however. This is my workstation at work, and disabling
>>> security is not a real option.
>>>
>>> This set of options disable lots of security features:
>>> apparmor=0 -- Disable normal security
>>> selinux=0 -- Useless on Ubuntu (disable security)
>>> pti=off 3 -- Spectre/Meltdown
>>> spectre_v2=off -- Spectre/Meltdown
>>> nospectre_v2 -- Spectre/Meltdown
>>> retp=0 -- Spectre/Meltdown
>>> ibrs=0 -- Spectre/Meltdown
>>> ibpb=0 -- Spectre/Meltdown
>>>
>>> Is it likely these security features impact the crash issue?
>>>
>>> This will remove 3 of my 12 CPU threads:
>>> isolcpus=5,6,7 -- Remove CPU 5,6 and 7 from the system :(
>>> nohz_full=5,6,7 -- Set CPU 5,6 and 7 to be in adaptive-ticks mode
>>> "reduce the number of scheduling-clock interrupts" ?
>>>
>>> The system is stable with 100% load on all cores for days, and all crash
>>> scenarios have been in ~1-5% load.
>>>
>>> More interrupts disabled:
>>> nmi_watchdog=0 -- CPU crash handling (interrupt)
>>>
>>> Is the cause related to interrupts?
>>>
>>> Disable all CPU energy optimizations:
>>> processor.max_cstate=1 -- Disable all CPU sleep/low-power states.
>>> intel_pstate=disable -- Disable the Intel CPU frequency/performance
>>> handler.
>>>
>>> Is the crash related to CPUsleep states?
>>>
>>> Enable features for VM's:
>>> intel_iommu=on -- Used to speed up a VM's access to hardware
>>> iommu=pt" -- Used to speed up a VM's access to hardware
>>>
>>> I do not run any VM's, but will this set of options impact the GPU
>>> driver anyway?
>>>
>>> Other options:
>>> audit=0 -- Disable various logging features. ?
>>> thermal.off=1 -- Disable ACPI thermal support ?
>>> clocksource=hpet -- Change timers from TSC to HPET (slower) ?
>>>
>>> I don't see why any of those options can cause a crash, unless they
>>> generate interrupts somehow. Are they likely to be related to the crash
>>> issue?
>>>
>>> GPU driver related options:
>>> amdgpu.vm_fragment_size=9 -- Use 2 MiB page size.
>>> amdgpu.hw_i2c=1 -- Enable temperature sensor?
>>> radeon.clk_support=0 -- Useless?
>>> amdgpu.clk_support=1 -- ?
>>>
>>> Only the vm_fragment_size seems relevant, but it seems to be intended to
>>> improve crypto-mining.
>>> So far every crash seems to have happened when I have tried to *move
>>> the mouse* after writing some text, and all the logs are also related
>>> to moving the mouse. So this is not likely to happen in a mining system at
>>> all.
>>>
>>> Is the best way to get a stable system to switch to AMDGPU pro with my
>>> setup, or are there other things I can try?
>>>
>>> —
>>> You are receiving this because you commented.
>>> Reply to this email directly, view it on GitHub
>>> <https://github.com/RadeonOpenCompute/ROCm/issues/368#issuecomment-381602731>,
>>> or mute the thread
>>> <https://github.com/notifications/unsubscribe-auth/AWn0w5IuKSVzGvdVH6gNMMHFtBnh7G0aks5tpJ_ugaJpZM4SyT6L>
>>> .
>>>
>>
>>
>


---

### 评论 #9 — ghost (2018-05-12T23:04:47Z)

Thank you for closing this, There are some things I Absolutely love and
adore the 64's for, They also make great gifts for linux people I want to
cause night terrors for.

On Sat, May 12, 2018 at 8:11 PM, Gregory Stoner <notifications@github.com>
wrote:

> Closed #368 <https://github.com/RadeonOpenCompute/ROCm/issues/368>.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/368#event-1623188603>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0w130L-G_yhLbXYxSaoSQsxfIEiq2ks5txt-UgaJpZM4SyT6L>
> .
>


---
