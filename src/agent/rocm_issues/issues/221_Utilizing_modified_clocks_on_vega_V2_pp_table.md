# Utilizing modified clocks on vega V2 pp_table

> **Issue #221**
> **状态**: closed
> **创建时间**: 2017-10-05T17:24:13Z
> **更新时间**: 2018-05-12T18:44:27Z
> **关闭时间**: 2017-10-31T00:27:23Z
> **作者**: rhlug
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/221

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I overwrote the pp_table with some custom clocks for my RX Vega 56 on states 5, 6 and 7.  So now I have the following:

$ cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz 
4: 1312Mhz 
5: 1320Mhz 
6: 1325Mhz 
7: 1330Mhz 

When I start to utilize the GPU, the sclk never changes from state #0.  I get errors about it.

[  960.778779] amdgpu: [powerplay] Cannot find requested DCEFCLK!
[  961.172699] amdgpu: [powerplay] Cannot find requested DCEFCLK!
[ 1150.402251] amdgpu: [powerplay] Cannot find requested DCEFCLK!




---

## 评论 (29 条)

### 评论 #1 — rhlug (2017-10-05T18:31:18Z)

After pp_table change,  rocm-smi fails to even change to level 1, 2, or 3, which were unmodified.

cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz 
4: 1312Mhz 
5: 1320Mhz 
6: 1325Mhz 
7: 1330Mhz 

 /opt/rocm/bin/rocm-smi  --setsclk 2
====================    ROCm System Management Interface    ====================
GPU[0] 		: Successfully set GPU Clock frequency mask to Level 2
====================           End of ROCm SMI Log          ====================

Oct  5 13:18:42 localhost kernel: [ 3119.741300] amdgpu: [powerplay] Failed to send message: 0x21
Oct  5 13:18:42 localhost kernel: [ 3119.741347] amdgpu: [powerplay] Failed to send message: 0x22

cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz 
4: 1312Mhz 
5: 1320Mhz 
6: 1325Mhz 
7: 1330Mhz 


If I revert to original pp_table, I'm still stuck on Level sclk 0

cat pp_table.original > /sys/class/drm/card0/device/pp_table 
cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz 
4: 1312Mhz 
5: 1474Mhz 
6: 1538Mhz 
7: 1590Mhz 

And rocm-smi cant even change it...

/opt/rocm/bin/rocm-smi  --setsclk 3
====================    ROCm System Management Interface    ====================
GPU[0] 		: Successfully set GPU Clock frequency mask to Level 3
====================           End of ROCm SMI Log          ====================

tail -n2 /var/log/syslog
Oct  5 13:29:18 rig21 kernel: [ 3755.786758] amdgpu: [powerplay] Failed to send message: 0x21
Oct  5 13:29:18 rig21 kernel: [ 3755.786905] amdgpu: [powerplay] Failed to send message: 0x22

 cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz 
4: 1312Mhz 
5: 1474Mhz 
6: 1538Mhz 
7: 1590Mhz 

A reboot resolves it..



---

### 评论 #2 — rhlug (2017-10-17T14:18:11Z)

Issues persist with pp_table in rocm-1.6.180

---

### 评论 #3 — gstoner (2017-10-17T15:15:05Z)

This is with custom PPtable correct,   One thing this is all set up by the base Linux driver, in the  PPLIB, so this where you find the logic https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/master/drivers/gpu/drm/amd/powerplay    This same on all AMD Linux drivers 

---

### 评论 #4 — rhlug (2017-10-17T16:51:22Z)

Yes, lets say I just change P-states 5, 6, and 7 for core frequencies.

```
# hexdump pp_table.new > 1
# hexdump pp_table.original > 2
# diff -Naur 1 2
--- 1	2017-10-17 11:46:51.311354644 -0500
+++ 2	2017-10-17 11:46:53.391371195 -0500
@@ -13,9 +13,9 @@
 00000c0 0000 1c00 0183 0100 0000 0000 0000 0000
 00000d0 bc88 0001 0002 0000 0000 0000 b400 01ef
 00000e0 0300 0000 0000 0000 0000 0080 0002 0004
-00000f0 0000 0000 0000 a000 0203 0500 0000 0000
-0000100 0001 0000 0594 0002 0006 0000 0100 0000
-0000110 8800 0207 0700 0000 0000 0001 0000 0400
+00000f0 0000 0000 0000 c800 023f 0500 0000 0000
+0000100 0001 0000 58c8 0002 0006 0000 0100 0000
+0000110 1800 026d 0700 0000 0000 0001 0000 0400
 0000120 ea60 0000 4000 0119 0000 4adc 0001 9000
 0000130 015f 0000 0800 6e28 0000 2c00 00c9 0100
 0000140 0bf8 0001 8002 0138 0300 5f90 0001 f404

# cat pp_table.new > /sys/class/drm/card0/device/pp_table 

# cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz
2: 1138Mhz
3: 1269Mhz
4: 1312Mhz
5: 1320Mhz
6: 1325Mhz
7: 1330Mhz
```

While it appears to work according to the sclks you see, something under the hood has broken, and you cant switch to those p-states.... or recover from them.

A couple times I've re-applied pp_table.original, and I've regained funcitonality after doing

```
/opt/rocm/bin/rocm-smi -r
```


I realize vega10 has its own pp_table, so the ../drivers/gpu/drm/amd/powerplay/ for polaris10 are different.  I've never need custom pp_table on polaris10 because I could just mod the bios.   But I can test pp_table functionality on polaris10 to see if that works.



---

### 评论 #5 — gstoner (2017-10-18T13:13:37Z)

They are working on update to ROCm-SMI,  they are reworking the reset logic.  Note  They changed out SMU and SMU interface work on Vega10,  we had a compute profile under GFX that no longer work the same way.   Linux team is also still rolling out update to PPlib on Vega10 if you track the Linux kernel updates 

---

### 评论 #6 — rhlug (2017-10-20T18:00:17Z)

I did verify that a pp_table modification on a Polaris 10 card (w/ amdgpu-pro 17.40) works without a hitch.   That polaris 10 card even had a modified bios.   My next test will be Polaris 10 card w/ ROCm 1.6.180.

```
# cat /sys/class/drm/card0/device/pp_dpm_sclk 
0: 302Mhz 
1: 466Mhz 
2: 751Mhz 
3: 1019Mhz 
4: 1074Mhz 
5: 1082Mhz 
6: 1102Mhz 
7: 1132Mhz *

# ./mod_pptable.t 114200
Modifying core-state-7 to 114200
  Skip 834 bytes
  Len 6 bytes
  Hex 18BE01
Packed into 812 bytes and wrote to pp_table

# cat pp_table > /sys/class/drm/card0/device/pp_table 
# cat /sys/class/drm/card0/device/pp_dpm_sclk 
0: 302Mhz 
1: 466Mhz 
2: 751Mhz 
3: 1019Mhz 
4: 1074Mhz 
5: 1082Mhz 
6: 1120Mhz 
7: 1142Mhz *
```

---

### 评论 #7 — eriktorsner (2017-10-25T13:39:33Z)

To add a datapoint. I experience the same problem. I have a single Vega 56 running in Ubuntu 16.04.3 using the amdgpu-17.40-483984 driver and ROCm 1.6.180.

```
erik@test01:~$ uname -a && cat /opt/rocm/.info/version && cat /etc/issue.net 
Linux rig01 4.11.0-kfd-compute-rocm-rel-1.6-180 #1 SMP Tue Oct 10 08:15:38 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux
1.6.180
Ubuntu 16.04.3 LTS
```

I've even tried to overwrite the pp_table with itselt, i.e directly after a boot i do:
```
sudo cp /sys/class/drm/card0/device/pp_table ~/pp_table_org
sudo cp ~/pp_table_org  /sys/class/drm/card0/device/pp_table
```

The errors I get are:
```
Oct 25 15:31:27 test01 kernel: [  979.660882] amdgpu: [powerplay] Cannot find requested DCEFCLK!
Oct 25 15:31:27 test01 kernel: [  979.763336] amdgpu: [powerplay] [DisableDiDtConfig] Attempt to Disable DiDt feature Failed!
```
Now, the real question is where to report this bug? From what I can tell, this bug isn't really in the ROCm package, it's more likely something in the 17.40 drivers, right? Just a hunch. But I'd be tempted to think that some part of the driver doesn't take the modified Vega 10 binary structures into account when rereading pp_table.

@rhlug, did you see similar issues in 17.30? I was never able to get my Vega 56 to be recognized until 17.40 came along.



---

### 评论 #8 — rhlug (2017-10-26T20:07:24Z)

@eriktorsner I've never installed 17.30 or 17.40 pro drivers on my dev machine.   Only the 1.6.148 and 1.6.180 rocm drivers on the dev setup.   The polaris 10 production systems I tested on 17.30 and 17.40, and both pp_table modifications worked fine.

I just havent had any time lately to test anything else.  My guess.. it wont matter, its simply broken.

---

### 评论 #9 — rhlug (2017-10-27T14:11:07Z)

Just to confirm, Polaris10 pp_table on ROCm 1.6.180 works as expected.

```
# cat /sys/class/drm/card1/device/pp_dpm_sclk
0: 301Mhz *
1: 461Mhz 
2: 751Mhz 
3: 1011Mhz 
4: 1041Mhz 
5: 1061Mhz 
6: 1101Mhz 
7: 1121Mhz 

# cat pp_table > /sys/class/drm/card1/device/pp_table 

# cat /sys/class/drm/card1/device/pp_dpm_sclk
0: 301Mhz 
1: 461Mhz 
2: 751Mhz 
3: 1011Mhz 
4: 1041Mhz 
5: 1061Mhz 
6: 1120Mhz *
7: 1140Mhz 

# /opt/rocm/bin/rocm-smi -d 1 --setsclk 7

# cat /sys/class/drm/card1/device/pp_dpm_sclk
0: 301Mhz 
1: 461Mhz 
2: 751Mhz 
3: 1011Mhz 
4: 1041Mhz 
5: 1061Mhz 
6: 1120Mhz 
7: 1140Mhz *
```

---

### 评论 #10 — eriktorsner (2017-10-27T15:20:38Z)

I have to agree, it just seem broken on Linux, not just the pp_table. My biggest gripe right now is the requirement on the CPU/motherboard combo to support AtomicOps to even get started. Tried 2 differnt board but the best I've got is to have it support one Vega card at a time.

I'm going to have a go at the 4.15 kernel but I still see no progress, it's going to have to be Windows 10 for the time being. 


---

### 评论 #11 — gstoner (2017-10-27T15:45:25Z)

@eriktorsner ROCm was built for the need of high-performance computing,  we need which atomic operation help with multi-writer queues performance, signalling and lower queue overheads.    WIth haswell or newer CPU you have zero issues,  Also with Ryzen, Thread ripper and EPYC there are zero issues.   Remember normally you use x8 or x16 lanes for GPU's which always come off the CPU complex PCIe root i/o not off the southbridge controller.    Minning work is driving people to try and run GPU on PCIe x1 so they stuff as many GPU in box cheaply.   

---

### 评论 #12 — gstoner (2017-10-27T15:46:36Z)

Guy the way PPLIB and SMU firmware work changed in Vega10 from Polaris and Fiji.  We lost some our compute profile options as well and have been working firmware team to address this 

---

### 评论 #13 — eriktorsner (2017-10-27T16:04:42Z)

Thanks for helping me fill in the blanks @gstoner, this is a new field for me and I realize I'm stumbling a bit. I've had so much help from your comments in this and other threads, just want to say I appreciate it!

I've tried an Intel Pentium G4440 (Skylake) with 2 differnt boards. On the first, only the x16 slot was PCIe 3.0 while all others was 2.0. So I went out to get a fairly modern MSI Z270 A-pro that has PCIe 3.0 on all slots, but on that board I got the "...rejects Atomics" on all PCIe slots, including the x16 one.

I've figured out it's probably comes down to the CPU but I haven't taken the time to go out and buy another one. Would a gen 7 Core i3 do the job? I am a little bit puzzled that my current G4440 could handle Atomic on one slot on one board but not luck at all on the 2nd that supposedly have 100 Gen 3 slots.  Is there such a thing as a PCIe root controller that cheaps out and only enable Atomics on one of the slots? 



---

### 评论 #14 — boxerab (2017-10-27T16:08:45Z)

I have had good luck with Asus Z170-K + i7-6700 + Polaris .

It would be nice to have a list of all known supported configurations of
MB + CPU + GPU

---

### 评论 #15 — jamilbk (2017-10-27T18:00:21Z)

@eriktorsner Skylake only has 16 PCIe lanes directly to the PCIe slots. The Z270 offers 30 total, 16 of those go straight to the CPU while the remaining 14 pass through a DMI bridge. It's those 14 that are probably giving you trouble -- most motherboards AFAIK have the one primary x16 slot (directly connected to the CPU, supporting PCIe 3.0 Atomics) while the other slots are "multiplexed" through the chipset and hence probably causing the issues you see.

So realistically, the problem is not the chipset per se, but the lanes from the CPU. Skylake has 20 total (16 for the primary slot for a GPU, 4 to the chipset), Ryzen has 24 total (typically x16 or two x8 for GPUs), Threadripper 64 total (typically two x16 and two x8 for GPUs), and EPYC 128 total. It's up to the motherboard manufacturer how they allocate those lanes on the board.

My Gigabyte X399 motherboard for Threadripper has 4 PCIe slots directly attached to the CPU, two x16 and two x8, hence I'm able to run ROCm on four Vegas on that system.

Hope this made sense 👍 

EDIT: Here is a diagram for X399 which hopefully clarifies things (credit http://www.guru3d.com/articles-pages/asus-rog-zenith-x399-extreme-review,2.html)

![untitled-5](https://user-images.githubusercontent.com/167144/32118416-7ecda964-bb06-11e7-993b-3c7902a8a611.jpg)


---

### 评论 #16 — eriktorsner (2017-10-27T18:14:24Z)

Makes a lot of sense, thanks!

---

### 评论 #17 — jstefanop (2017-10-27T20:02:19Z)

@gstoner any chance that you guys will update rocm-smi to give us full control over clocks/voltages(both core and HBM)/mem timings without currently needing to hack the crap out of the kernel to do the same thing?

---

### 评论 #18 — rhlug (2017-11-04T19:06:19Z)

Why is this closed.  Did it get fixed?  

---

### 评论 #19 — rhlug (2017-11-18T19:07:20Z)

Verified that amdgpu-pro 17.40 has broken Vega pp_table implementation as well.

---

### 评论 #20 — anoother (2018-03-23T08:52:07Z)

I know this is not really a ROCm issue, but seeing as it's being discussed: Has anyone managed to get a working pp_table implementation for Vega?

I'm unable to even find a pp_table file, even with the latest staging kernels from agd5f

---

### 评论 #21 — gstoner (2018-03-23T11:08:48Z)

@jstefanop   I am working with management to see if we can get you guys what you want full control overclock/voltages(both core and HBM)/mem timings.  It is really bureaucracy issue for my team.  We know what to do.   We want to give you even more information on system SMI interface is going to evolve so you have much more information on what the GPU is doing.   I  working with the management team to open up the clock.  We need it as well to tune at system level even in Deep Learning.   With some of the new algorithms, we are slamming hard on the GPU  which is driving a lot of fun with managing peak currents. 

---

### 评论 #22 — rhlug (2018-03-23T13:52:35Z)

@anoother see https://github.com/RadeonOpenCompute/ROCm/issues/348#issuecomment-374649835 

pp_table's are working on 4.4.0-112 with rock-dkms 1.7.137.

I've been unable to find any newer kernel that provides functional pp_table for vega10 powerplay itself.  So only older kernels that inherit it from rock-dkms.    I tried 4.13 hwe, 4.15, and a 4.16 nightly build from march 20, none of those worked.

Alex Deucher is aware of the issue, and he said they are looking at it.



---

### 评论 #23 — anoother (2018-03-23T15:03:21Z)

@rhlug Thanks.

Not sure if I'm prepared to run such an old amdgpu driver; Might have to have seperate boot options for compute and productivity/gaming...

---

### 评论 #24 — jstefanop (2018-03-23T18:09:28Z)

@gstoner good news....I think this is a right direction for AMD, especially with the growing number of specialized Compute fields utilizing GPUs, each with their own requirements. Having a single power/clock/timing profile for a GPU as a one size fits all no longer fits the current Machine Learning/crypto algorithm landscape. You guys took the first step with the driver open source initiative, I think opening up the hardware controls in this way will further solidify your advantage in this space. 

As far as the bureaucracy...tell your management team CPU clocks/voltages/mem timings have always been open and with a ridiculous number of tunning parameters users have always had for decades for both Intel and AMD CPUs....I could never understand the logic of closing all this for GPUs. 

---

### 评论 #25 — gstoner (2018-03-23T18:59:10Z)

@jstefanop I know I was at MIPS, Intel few other places before AMD ; ).

---

### 评论 #26 — rhlug (2018-03-28T16:13:47Z)

@anoother i can confirm that pp_tables are functional for vega on latest nightly kernel.  i'm running it with mesa/clover and getting over 40mh/s ethash per card on 6x vega 56 rig.   Hope to soon test latest kernel with 18.10.   I will report back.

---

### 评论 #27 — gstoner (2018-03-28T17:43:55Z)

In 1.8 I asked the team to remove in the kernel driver the restriction that limits the stack to x8 PCIe lane, it run Gen2 x1 lane.  

---

### 评论 #28 — anoother (2018-04-04T22:31:39Z)

@rhlug Are you running an upstream kernel? Where from, and which commit hash?

I just tried building against upstream and was unable to compile the dkms module (rock-dkms 1.7.137-ubuntu).

Sorry to bump the issue with this

---

### 评论 #29 — bananajamma (2018-05-12T18:38:57Z)

To add to what @gstoner said, check this out:

> We released ROCM 1.8 Beta http://repo.radeon.com/rocm/misc/beta_1.8.0/ which linux driver team put in the restriction on the number lanes of PCIe needed to be supported. It was x8, this restriction has been removed. This was not PCIe Atomics issue. But for Vega10 only we removed this restriction as well for now. We are looking at addressing this in  Polaris and Fiji in the future release since it involves microcode changes. You also pick up REHL/Centos 7.4 support in this beta.

https://github.com/RadeonOpenCompute/ROCm/issues/364#issuecomment-386809567

---
