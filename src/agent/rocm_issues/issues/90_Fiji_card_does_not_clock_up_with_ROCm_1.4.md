# Fiji card does not clock up with ROCm 1.4

> **Issue #90**
> **状态**: closed
> **创建时间**: 2017-02-24T02:08:19Z
> **更新时间**: 2018-10-16T01:50:29Z
> **关闭时间**: 2018-08-14T10:41:22Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/90

## 描述

No matter what I do, the Fiji card in question is stuck at 300 MHz core clock. Loading it with work, setting clocks or PowerPlay level all does not do anything.

Radeontop shows:
```
                                                       Graphics pipe  64.17% |                                                                           
```

But the clocks are stuck:
```
$ /opt/rocm/bin/rocm-smi -d 0 -a
===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]          : GPU ID: 0x7300
============================================================================
============================================================================
GPU[0]          : Temperature: 36.0c
============================================================================
============================================================================
GPU[0]          : GPU Clock Level: 0 (300Mhz)
GPU[0]          : GPU Memory Clock Level: 0 (500Mhz)
============================================================================
============================================================================
GPU[0]          : Fan Level: 48 (18.82)%
============================================================================
============================================================================
GPU[0]          : Current PowerPlay Level: manual
============================================================================
============================================================================
GPU[0]          : Current OverDrive value: 0%
============================================================================
============================================================================
GPU[0]          : Minimum SCLK: 974MHz
GPU[0]          : Minimum MCLK: 0MHz
GPU[0]          : Activity threshold: 30%
GPU[0]          : Hysteresis Up: 0ms
GPU[0]          : Hysteresis Down: 5ms
============================================================================
============================================================================
GPU[0]          : Supported GPU clock frequencies on GPU0
GPU[0]          : 0: 300Mhz *
GPU[0]          : 1: 508Mhz 
GPU[0]          : 2: 717Mhz 
GPU[0]          : 3: 874Mhz 
GPU[0]          : 4: 911Mhz 
GPU[0]          : 5: 944Mhz 
GPU[0]          : 6: 974Mhz 
GPU[0]          : 7: 1000Mhz 
GPU[0]          : 
GPU[0]          : Supported GPU Memory clock frequencies on GPU0
GPU[0]          : 0: 500Mhz *
GPU[0]          : 
============================================================================
===================          End of ROCm SMI Log         ===================
```

Also:
```
$ /opt/rocm/bin/rocm-smi -d 0 --setsclk 7

===================   ROCm System Management Interface   ===================


===================   ROCm System Management Interface   ===================
GPU[0]          : Successfully set GPU Clock frequency to Level 7
===================          End of ROCm SMI Log         ===================
```
does nothing.

BTW funnily enough
```
 $ /opt/rocm/bin/rocm-smi -d 0 --setsclk 1000

===================   ROCm System Management Interface   ===================

===================   ROCm System Management Interface   ===================
GPU[0]          : Successfully set GPU Clock frequency to Level 1000
===================          End of ROCm SMI Log         ===================
```
is also supported while --setmlck only takes as argument the index of the memory frequency from the list (i.e. 0) not the memory clock value (500).

---

## 评论 (20 条)

### 评论 #1 — pszi1ard (2017-02-27T18:22:57Z)

@kentrussell here's the output you requested on [another roc-smi issue](https://github.com/RadeonOpenCompute/ROC-smi/issues/1):

```
$ /opt/rocm/bin/rocm-smi -a; /opt/rocm/bin/roc-smi --setsclk 7; /opt/rocm/bin/rocm-smi -a


===================   ROCm System Management Interface   ===================
============================================================================
GPU[0] 		: GPU ID: 0x7300
GPU[1] 		: GPU ID: 0x67b0
============================================================================
============================================================================
GPU[0] 		: Temperature: 32.0c
GPU[1] 		: Temperature: 41.0c
============================================================================
============================================================================
GPU[0] 		: GPU Clock Level: 0 (300Mhz)
GPU[0] 		: GPU Memory Clock Level: 0 (500Mhz)
GPU[1] 		: GPU Clock Level: 0 (300Mhz)
GPU[1] 		: GPU Memory Clock Level: 0 (150Mhz)
============================================================================
============================================================================
GPU[0] 		: Fan Level: 48 (18.82)%
GPU[1] 		: Fan Level: 51 (20.0)%
============================================================================
============================================================================
GPU[0] 		: Current PowerPlay Level: auto
GPU[1] 		: Current PowerPlay Level: auto
============================================================================
============================================================================
GPU[0] 		: Current OverDrive value: 0%
GPU[1] 		: Current OverDrive value: 0%
============================================================================
============================================================================
GPU[0] 		: Minimum SCLK: 974MHz
GPU[0] 		: Minimum MCLK: 0MHz
GPU[0] 		: Activity threshold: 30%
GPU[0] 		: Hysteresis Up: 0ms
GPU[0] 		: Hysteresis Down: 5ms
GPU[1] 		: Minimum SCLK: 1025MHz
GPU[1] 		: Minimum MCLK: 0MHz
GPU[1] 		: Activity threshold: 30%
GPU[1] 		: Hysteresis Up: 0ms
GPU[1] 		: Hysteresis Down: 5ms
============================================================================
============================================================================
GPU[0] 		: Supported GPU clock frequencies on GPU0
GPU[0] 		: 0: 300Mhz *
GPU[0] 		: 1: 508Mhz 
GPU[0] 		: 2: 717Mhz 
GPU[0] 		: 3: 874Mhz 
GPU[0] 		: 4: 911Mhz 
GPU[0] 		: 5: 944Mhz 
GPU[0] 		: 6: 974Mhz 
GPU[0] 		: 7: 1000Mhz 
GPU[0] 		: 
GPU[0] 		: Supported GPU Memory clock frequencies on GPU0
GPU[0] 		: 0: 500Mhz *
GPU[0] 		: 
GPU[1] 		: Supported GPU clock frequencies on GPU1
GPU[1] 		: 0: 300Mhz *
GPU[1] 		: 1: 516Mhz 
GPU[1] 		: 2: 763Mhz 
GPU[1] 		: 3: 882Mhz 
GPU[1] 		: 4: 934Mhz 
GPU[1] 		: 5: 982Mhz 
GPU[1] 		: 6: 1025Mhz 
GPU[1] 		: 7: 1050Mhz 
GPU[1] 		: 
GPU[1] 		: Supported GPU Memory clock frequencies on GPU1
GPU[1] 		: 0: 150Mhz *
GPU[1] 		: 1: 1350Mhz 
GPU[1] 		: 
============================================================================
===================          End of ROCm SMI Log         ===================

-bash: /opt/rocm/bin/roc-smi: No such file or directory


===================   ROCm System Management Interface   ===================
============================================================================
GPU[0] 		: GPU ID: 0x7300
GPU[1] 		: GPU ID: 0x67b0
============================================================================
============================================================================
GPU[0] 		: Temperature: 32.0c
GPU[1] 		: Temperature: 41.0c
============================================================================
============================================================================
GPU[0] 		: GPU Clock Level: 0 (300Mhz)
GPU[0] 		: GPU Memory Clock Level: 0 (500Mhz)
GPU[1] 		: GPU Clock Level: 0 (300Mhz)
GPU[1] 		: GPU Memory Clock Level: 0 (150Mhz)
============================================================================
============================================================================
GPU[0] 		: Fan Level: 48 (18.82)%
GPU[1] 		: Fan Level: 51 (20.0)%
============================================================================
============================================================================
GPU[0] 		: Current PowerPlay Level: auto
GPU[1] 		: Current PowerPlay Level: auto
============================================================================
============================================================================
GPU[0] 		: Current OverDrive value: 0%
GPU[1] 		: Current OverDrive value: 0%
============================================================================
============================================================================
GPU[0] 		: Minimum SCLK: 974MHz
GPU[0] 		: Minimum MCLK: 0MHz
GPU[0] 		: Activity threshold: 30%
GPU[0] 		: Hysteresis Up: 0ms
GPU[0] 		: Hysteresis Down: 5ms
GPU[1] 		: Minimum SCLK: 1025MHz
GPU[1] 		: Minimum MCLK: 0MHz
GPU[1] 		: Activity threshold: 30%
GPU[1] 		: Hysteresis Up: 0ms
GPU[1] 		: Hysteresis Down: 5ms
============================================================================
============================================================================
GPU[0] 		: Supported GPU clock frequencies on GPU0
GPU[0] 		: 0: 300Mhz *
GPU[0] 		: 1: 508Mhz 
GPU[0] 		: 2: 717Mhz 
GPU[0] 		: 3: 874Mhz 
GPU[0] 		: 4: 911Mhz 
GPU[0] 		: 5: 944Mhz 
GPU[0] 		: 6: 974Mhz 
GPU[0] 		: 7: 1000Mhz 
GPU[0] 		: 
GPU[0] 		: Supported GPU Memory clock frequencies on GPU0
GPU[0] 		: 0: 500Mhz *
GPU[0] 		: 
GPU[1] 		: Supported GPU clock frequencies on GPU1
GPU[1] 		: 0: 300Mhz *
GPU[1] 		: 1: 516Mhz 
GPU[1] 		: 2: 763Mhz 
GPU[1] 		: 3: 882Mhz 
GPU[1] 		: 4: 934Mhz 
GPU[1] 		: 5: 982Mhz 
GPU[1] 		: 6: 1025Mhz 
GPU[1] 		: 7: 1050Mhz 
GPU[1] 		: 
GPU[1] 		: Supported GPU Memory clock frequencies on GPU1
GPU[1] 		: 0: 150Mhz *
GPU[1] 		: 1: 1350Mhz 
GPU[1] 		: 
============================================================================
===================          End of ROCm SMI Log         ===================
```

---

### 评论 #2 — pszi1ard (2017-03-03T23:56:46Z)

It turns out that disabling the Hawaii GPU, the Fiji magically starts to behave normally, it clocks up as expected. I assume this is a bug (in the driver)? Do you need any other info to accept the report?

(On a side-note what's the supported way to turn off a GPU using the amdgpu driver?)

---

### 评论 #3 — kentrussell (2017-03-06T11:30:48Z)

That's peculiar, and something we'll try to look into. There isn't an easy way to turn off a GPU using the amdgpu driver to my knowledge. I'll ask around here and see if anyone knows of an easy method to take it out. 

I am a little baffled that the rocm-smi tool didn't catch the Hawaii when you ran the -a flag, since it should iterate over all of the nodes and reported info for all of them. Unless it didn't recognize the Hawaii in the first place, or if the firmware didn't load for it. That would explain a lot. When you boot with the Hawaii and Fiji both in there, does dmesg show anything regarding the Hawaii firmware? And does lspci -vv -d 0x1002:* show both cards being recognized correctly?

---

### 评论 #4 — pszi1ard (2017-03-06T18:48:31Z)

> That's peculiar, and something we'll try to look into. There isn't an easy way to turn off a GPU using the amdgpu driver to my knowledge. I'll ask around here and see if anyone knows of an easy method to take it out.

Well, I managed to remove the second device from the pci tree using ```/sys/class/drm/card0/device/enable```. This made the Hawaii board disappear even from ```lspci``` (as expected). Unfortunately echoing a 1 back into this file did not turn the GPU back on (and ```reset``` or ```rescan``` did not help either).

However, although I never got a confirmation whether this is just not a use case that is "expected/known to work" (or has been tested internally), having disabled the second device (the Hawaii card), I was at least able to run on the Fiji at the nominal clock. Plus the issues I noted on [hcc#197](https://github.com/RadeonOpenCompute/hcc/issues/197) has also disappeared.

> I am a little baffled that the rocm-smi tool didn't catch the Hawaii when you ran the -a flag, since it should iterate over all of the nodes and reported info for all of them. Unless it didn't recognize the Hawaii in the first place, or if the firmware didn't load for it. That would explain a lot. When you boot with the Hawaii and Fiji both in there, does dmesg show anything regarding the Hawaii firmware? And does lspci -vv -d 0x1002:* show both cards being recognized correctly?

Coudl there be some misunderstanding? By default, both GPUs were present, listed both in lspci and rocm-smi (see [above](https://github.com/RadeonOpenCompute/ROCm/issues/90#issuecomment-282804867)).

---

### 评论 #5 — kentrussell (2017-03-10T15:14:10Z)

Sorry, I was speed-reading and missed the Hawaii one. Can you replaced the invalid 2nd command with rocm-smi --setsclk 7 (instead of my mistyped roc-smi --setclk 7)? Thanks!

---

### 评论 #6 — pszi1ard (2017-03-11T01:38:00Z)

@kentrussell I thought I did fix it, but I'm not sure what happened to the above command sequence's execution, ```/opt/rocm/bin/roc-smi``` could not have vanished in between. I'll have to get back to this later because I had to nuke the ROCm install from the dev box to be able to do some development.

In any case, can you look into fixing issues related to the use-case of multiple different devices present in the same system? DO you _need_ me to run the test to be able to progress?


---

### 评论 #7 — kentrussell (2017-03-13T16:23:40Z)

I don't need you to be able to progress, it was just something that I wanted to see since you had the system set up already. I had done it with 2 different ASICs but in the same family (Fiji+Tonga), so I'll see if I can get a working Hawaii and try it with a Fiji and see what happens.

---

### 评论 #8 — pszi1ard (2017-03-13T16:29:27Z)

Thanks. I'll get back if our dev machine frees up and I can put back ROCm to re-run the roc-smi. 

---

### 评论 #9 — kruftindustries (2018-07-20T22:55:57Z)

Hey this is still an issue with new installs. I tried switching kernels back to 4.13.0-38, and -36 from 4.13.0-45, even reinstalled ubuntu 16.04 from an old livecd and followed the installation guide exactly and still have this issue. When messing around with the `/sys/class/drm/cardX/device` and others the best I have gotten out of the cards is clock level 5 out of 7. `--setsclk` 7 gets me clock level 4. Windows 10 fresh install runs 50% faster on the current adrenalin drivers with the compute profile on graphics and faster than I remember when changing the profile to compute. 

---

### 评论 #10 — kentrussell (2018-07-23T12:55:25Z)

I haven't found that issue in my testing (Fiji+Ubuntu16.04, Vega10+CentOS7.4), but I did push a ton of fixes to the 1.9 branch. Unfortunately I missed the 1.9.0 cutoff, so it'll be in 1.9.1 . Running rocm-smi shows all 8 levels, but doing rocm-smi --setsclk 7 results in it going down to level 4? Can you attach the dmesg after trying that out, and copy/paste the output from the SMI? Thanks!

---

### 评论 #11 — kruftindustries (2018-07-23T13:15:04Z)

It shows all cards setting successfully then a check of the device files
shows 4 or 5 with an asterisk next to it. I can get dmesg output later
today. I am using ubuntu desktop if that matters, a similar machine with
vega graphics updated its kernel for me to 4.15, this one did not though.

On Mon, Jul 23, 2018, 7:55 AM Kent Russell <notifications@github.com> wrote:

> I haven't found that issue in my testing (Fiji+Ubuntu16.04,
> Vega10+CentOS7.4), but I did push a ton of fixes to the 1.9 branch.
> Unfortunately I missed the 1.9.0 cutoff, so it'll be in 1.9.1 . Running
> rocm-smi shows all 8 levels, but doing rocm-smi --setsclk 7 results in it
> going down to level 4? Can you attach the dmesg after trying that out, and
> copy/paste the output from the SMI? Thanks!
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/90#issuecomment-407048118>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AV0QhN2BrPfCfKOqi8PfcD8AfPnbTN_0ks5uJcfCgaJpZM4MKvbj>
> .
>


---

### 评论 #12 — kentrussell (2018-07-23T15:43:12Z)

This will seem like a silly question, but you only set it to level 7 right? If it's set to 0 5 6 7 then it will automatically pick the best level based on GPU workload. Is Performance level set to auto or manual when you do that? I'll need to check if any of the kernel code changed and has any new requirements. The Power Profile changes may have caused things to require a specific performance level for that to kick in.

---

### 评论 #13 — kruftindustries (2018-07-23T15:49:12Z)

When set to manual and --setsclk 7 it would do 5, auto would do 4. Also
tried --setsclk 6 7 combinations and set to only 7 after with no change.
The cards are going to full clocks in windows. Cooling is not standard and
the fans are disconnected but the capacity of the loop exceeds the output
of the cards and worst case temperatures do not exceed 56c. I did notice
the fans show something odd like 47% where previously they would show 0%
since they are not connected, maybe that is related?

On Mon, Jul 23, 2018, 10:43 AM Kent Russell <notifications@github.com>
wrote:

> This will seem like a silly question, but you only set it to level 7
> right? If it's set to 0 5 6 7 then it will automatically pick the best
> level based on GPU workload. Is Performance level set to auto or manual
> when you do that? I'll need to check if any of the kernel code changed and
> has any new requirements. The Power Profile changes may have caused things
> to require a specific performance level for that to kick in.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/90#issuecomment-407103695>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AV0QhE8QmZn_IZaBCpPw4rt64gds9oh3ks5uJe8VgaJpZM4MKvbj>
> .
>


---

### 评论 #14 — pszi1ard (2018-08-13T20:20:14Z)

--setsclk does seem to work for me on both Fiji, Polaris, and Vega.

---

### 评论 #15 — kentrussell (2018-08-14T10:41:22Z)

Awesome, glad to see that we're getting this addressed at long last :)

---

### 评论 #16 — pszi1ard (2018-08-14T12:14:18Z)

@kentrussell Thanks for the improvements and the patience with slow feeedback. 

---

### 评论 #17 — kentrussell (2018-08-14T12:15:23Z)

Not a problem, I've got a bunch more fixes coming for 1.9, so keep me posted if anything else goes awry!

---

### 评论 #18 — kruftindustries (2018-10-12T01:33:05Z)

I formatted and re-installed and now the issue is present on a machine with fiji cards and a similar issue with vega frontier cards

---

### 评论 #19 — kruftindustries (2018-10-12T01:44:58Z)

**FIJI**

dude@KI-GPGPU02:$ lspci | grep AMD
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [                                                                                                                                                                   Radeon R9 FURY / NANO Series] (rev c8)
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [                                                                                                                                                                   Radeon R9 FURY / NANO Series] (rev c8)
02:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [                                                                                                                                                                   Radeon R9 FURY / NANO Series] (rev c8)
03:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8
85:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [                                                                                                                                                                   Radeon R9 FURY / NANO Series] (rev c8)
85:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8
86:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [                                                                                                                                                                   Radeon R9 FURY / NANO Series] (rev c8)
86:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae8


dude@KI-GPGPU02:$ dmesg | grep amd
[    0.000000] Linux version 4.13.0-36-generic (buildd@lgw01-amd64-033) (gcc ver                                                                                                                                                                   sion 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.9)) #40~16.04.1-Ubuntu SMP Fri                                                                                                                                                                    Feb 16 23:25:58 UTC 2018 (Ubuntu 4.13.0-36.40~16.04.1-generic 4.13.13)
[    1.941478] amdkcl: loading out-of-tree module taints kernel.
[    1.941509] amdkcl: module verification failed: signature and/or required key                                                                                                                                                                    missing - tainting kernel
[    2.111871] [drm] amdgpu kernel modesetting enabled.
[    2.120459] amdgpu 0000:01:00.0: enabling device (0000 -> 0003)
[    2.132340] [drm] add ip block number 3 <amdgpu_powerplay>
[    3.128200] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4F                                                                                                                                                                   FFFFFFF (4096M used)
[    3.128202] amdgpu 0000:01:00.0: GTT: 1024M 0x0000000000000000 - 0x000000003F                                                                                                                                                                   FFFFFF
[    3.128402] [drm] amdgpu: 4096M of VRAM memory ready
[    3.128403] [drm] amdgpu: 7939M of GTT memory ready.
[    3.341697] amdgpu 0000:01:00.0: fb1: amdgpudrmfb frame buffer device
[    3.547361] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:01:00.0 on mino                                                                                                                                                                   r 1
[    3.547475] amdgpu 0000:02:00.0: enabling device (0000 -> 0003)
[    3.547753] [drm] add ip block number 3 <amdgpu_powerplay>
[    4.548169] amdgpu 0000:02:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4F                                                                                                                                                                   FFFFFFF (4096M used)
[    4.548171] amdgpu 0000:02:00.0: GTT: 1024M 0x0000000000000000 - 0x000000003F                                                                                                                                                                   FFFFFF
[    4.548203] [drm] amdgpu: 4096M of VRAM memory ready
[    4.548205] [drm] amdgpu: 7939M of GTT memory ready.
[    4.762288] amdgpu 0000:02:00.0: fb2: amdgpudrmfb frame buffer device
[    4.968062] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:02:00.0 on mino                                                                                                                                                                   r 2
[    4.968164] amdgpu 0000:03:00.0: enabling device (0000 -> 0003)
[    4.968443] [drm] add ip block number 3 <amdgpu_powerplay>
[    5.964237] amdgpu 0000:03:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4F                                                                                                                                                                   FFFFFFF (4096M used)
[    5.964239] amdgpu 0000:03:00.0: GTT: 1024M 0x0000000000000000 - 0x000000003F                                                                                                                                                                   FFFFFF
[    5.964269] [drm] amdgpu: 4096M of VRAM memory ready
[    5.964270] [drm] amdgpu: 7939M of GTT memory ready.
[    6.177819] amdgpu 0000:03:00.0: fb3: amdgpudrmfb frame buffer device
[    6.383567] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:03:00.0 on mino                                                                                                                                                                   r 3
[    6.383784] amdgpu 0000:85:00.0: enabling device (0000 -> 0003)
[    6.384132] [drm] add ip block number 3 <amdgpu_powerplay>
[    7.380223] amdgpu 0000:85:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4F                                                                                                                                                                   FFFFFFF (4096M used)
[    7.380226] amdgpu 0000:85:00.0: GTT: 1024M 0x0000000000000000 - 0x000000003F                                                                                                                                                                   FFFFFF
[    7.380266] [drm] amdgpu: 4096M of VRAM memory ready
[    7.380268] [drm] amdgpu: 7939M of GTT memory ready.
[    7.596178] amdgpu 0000:85:00.0: fb4: amdgpudrmfb frame buffer device
[    7.801923] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:85:00.0 on mino                                                                                                                                                                   r 4
[    7.802050] amdgpu 0000:86:00.0: enabling device (0000 -> 0003)
[    7.802303] [drm] add ip block number 3 <amdgpu_powerplay>
[    8.796230] amdgpu 0000:86:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4F                                                                                                                                                                   FFFFFFF (4096M used)
[    8.796232] amdgpu 0000:86:00.0: GTT: 1024M 0x0000000000000000 - 0x000000003F                                                                                                                                                                   FFFFFF
[    8.796263] [drm] amdgpu: 4096M of VRAM memory ready
[    8.796264] [drm] amdgpu: 7939M of GTT memory ready.
[    9.011943] amdgpu 0000:86:00.0: fb5: amdgpudrmfb frame buffer device
[    9.217713] [drm] Initialized amdgpu 3.25.0 20150101 for 0000:86:00.0 on mino                                                                                                                                                                   r 5
[   42.323641] amdgpu 0000:86:00.0: vgaarb: changed VGA decodes: olddecodes=io+m                                                                                                                                                                   em,decodes=none:owns=none
[   42.323644] amdgpu 0000:85:00.0: vgaarb: changed VGA decodes: olddecodes=io+m                                                                                                                                                                   em,decodes=none:owns=none
[   42.323647] amdgpu 0000:03:00.0: vgaarb: changed VGA decodes: olddecodes=io+m                                                                                                                                                                   em,decodes=none:owns=none
[   42.323649] amdgpu 0000:02:00.0: vgaarb: changed VGA decodes: olddecodes=io+m                                                                                                                                                                   em,decodes=none:owns=none
[   42.323652] amdgpu 0000:01:00.0: vgaarb: changed VGA decodes: olddecodes=io+m                                                                                                                                                                   em,decodes=none:owns=none


dude@KI-GPGPU02:$ /opt/rocm/bin/rocm-smi


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  5   31c     53.163W  300Mhz   545Mhz   0.0%     manual    0%         0%
  3   29c     54.189W  300Mhz   545Mhz   0.0%     manual    0%         0%
  1   29c     54.131W  300Mhz   545Mhz   0.0%     manual    0%         0%
  4   29c     53.122W  300Mhz   545Mhz   0.0%     manual    0%         0%
  2   30c     54.216W  300Mhz   545Mhz   0.0%     manual    0%         0%
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A        N/A
================================================================================
====================           End of ROCm SMI Log          ====================

dude@KI-GPGPU02:$ /opt/rocm/bin/rocm-smi --setsclk 7


====================    ROCm System Management Interface    ====================
GPU[5]          : Successfully set GPU Clock frequency mask to Level 7
GPU[3]          : Successfully set GPU Clock frequency mask to Level 7
GPU[1]          : Successfully set GPU Clock frequency mask to Level 7
GPU[4]          : Successfully set GPU Clock frequency mask to Level 7
GPU[2]          : Successfully set GPU Clock frequency mask to Level 7
GPU[0]          : PowerPlay not enabled - Cannot set clocks
WARNING: One or more commands failed
====================           End of ROCm SMI Log          ====================

dude@KI-GPGPU02:$ /opt/rocm/bin/rocm-smi


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  5   33c     53.6W    300Mhz   545Mhz   0.0%     manual    0%         0%
  3   31c     53.225W  300Mhz   545Mhz   0.0%     manual    0%         0%
  1   31c     53.135W  300Mhz   545Mhz   0.0%     manual    0%         0%
  4   32c     52.216W  300Mhz   545Mhz   0.0%     manual    0%         0%
  2   32c     54.148W  300Mhz   545Mhz   0.0%     manual    0%         0%
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A        N/A
================================================================================
====================           End of ROCm SMI Log          ====================

---

### 评论 #20 — kruftindustries (2018-10-16T01:47:24Z)

Update- the issue with Vega was unrelated, clocks are fine there. 
The fury X cards have this issue with **Kernel 4.13.0-36**. reverted to 4.13.0-32-generic and re-installed rocm-dkms and back up to full speed, 1135Mhz set in the bios.

---
