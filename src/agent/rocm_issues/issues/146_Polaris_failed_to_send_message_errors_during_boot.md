# Polaris "failed to send message" errors during boot. 

> **Issue #146**
> **状态**: closed
> **创建时间**: 2017-07-03T22:09:45Z
> **更新时间**: 2018-09-10T10:20:11Z
> **关闭时间**: 2017-07-15T16:55:47Z
> **作者**: jstefanop
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/146

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

On a fresh install of ROCm 1.6 on top of Ubuntu 16.04 we are getting the messages below during boot after ring tests. Each GPU hangs for about 10 seconds and boot continues normally. 

Card seems to be initialized and working properly post boot regardless (full openCL performance on par with AMDGPU-PRO). 

This issue is not present during Vega FE boot

`[    3.058782] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[    3.485773] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    4.310558] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    4.723086] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    5.547875] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    5.960395] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    6.785188] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    7.197712] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    8.022497] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    8.435022] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[    9.259809] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[    9.672330] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[   10.502892] amdgpu: [powerplay] 
                failed to send pre message 260 ret is 0 
[   10.924276] amdgpu: [powerplay] 
                failed to send message 260 ret is 0 
[   10.938191] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[   11.346839] amdgpu: [powerplay] 
                failed to send pre message 15b ret is 0 
[   11.767822] amdgpu: [powerplay] 
                failed to send message 15b ret is 0 
[   12.196446] amdgpu: [powerplay] 
                failed to send pre message 155 ret is 0 
[   12.618252] amdgpu: [powerplay] 
                failed to send message 155 ret is 0 
[   12.628554] Virtual CRAT table created for GPU
[   12.630970] Parsing CRAT table with 1 nodes
[   12.632391] Creating topology SYSFS entries
[   12.633893] Topology: Add dGPU node [0x67df:0x1002]
[   12.635339] kfd kfd: Reserved 2 pages for cwsr.
[   12.636769] kfd kfd: added device 1002:67df
[   12.638159] [drm] Initialized amdgpu 3.16.0 20150101 for 0000:01:00.0 on minor 0
[   12.641308] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
[   12.643153] acpi device:16: registered as cooling_device9
[   12.644718] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input9
[   12.646381] [drm] Initialized i915 1.6.0 20160919 for 0000:00:02.0 on minor 1`

---

## 评论 (32 条)

### 评论 #1 — gstoner (2017-07-04T04:30:29Z)

Your sitting at base clock,  there is power play library failure due to VBIOS update.

Greg
On Jul 3, 2017, at 5:09 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


On a fresh install of ROCm 1.6 on top of Ubuntu 16.04 we are getting the messages below during boot after ring tests. Each GPU hangs for about 10 seconds and boot continues normally.

Card seems to be initialized and working properly post boot regardless (full openCL performance on par with AMDGPU-PRO).

This issue is not present during Vega FE boot

[ 3.058782] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device [ 3.485773] amdgpu: [powerplay] failed to send message 260 ret is 0 [ 4.310558] amdgpu: [powerplay] failed to send pre message 260 ret is 0 [ 4.723086] amdgpu: [powerplay] failed to send message 260 ret is 0 [ 5.547875] amdgpu: [powerplay] failed to send pre message 260 ret is 0 [ 5.960395] amdgpu: [powerplay] failed to send message 260 ret is 0 [ 6.785188] amdgpu: [powerplay] failed to send pre message 260 ret is 0 [ 7.197712] amdgpu: [powerplay] failed to send message 260 ret is 0 [ 8.022497] amdgpu: [powerplay] failed to send pre message 260 ret is 0 [ 8.435022] amdgpu: [powerplay] failed to send message 260 ret is 0 [ 9.259809] amdgpu: [powerplay] failed to send pre message 260 ret is 0 [ 9.672330] amdgpu: [powerplay] failed to send message 260 ret is 0 [ 10.502892] amdgpu: [powerplay] failed to send pre message 260 ret is 0 [ 10.924276] amdgpu: [powerplay] failed to send message 260 ret is 0 [ 10.938191] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df [ 11.346839] amdgpu: [powerplay] failed to send pre message 15b ret is 0 [ 11.767822] amdgpu: [powerplay] failed to send message 15b ret is 0 [ 12.196446] amdgpu: [powerplay] failed to send pre message 155 ret is 0 [ 12.618252] amdgpu: [powerplay] failed to send message 155 ret is 0 [ 12.628554] Virtual CRAT table created for GPU [ 12.630970] Parsing CRAT table with 1 nodes [ 12.632391] Creating topology SYSFS entries [ 12.633893] Topology: Add dGPU node [0x67df:0x1002] [ 12.635339] kfd kfd: Reserved 2 pages for cwsr. [ 12.636769] kfd kfd: added device 1002:67df [ 12.638159] [drm] Initialized amdgpu 3.16.0 20150101 for 0000:01:00.0 on minor 0 [ 12.641308] ACPI: Video Device [GFX0] (multi-head: yes rom: no post: no) [ 12.643153] acpi device:16: registered as cooling_device9 [ 12.644718] input: Video Bus as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/LNXVIDEO:00/input/input9 [ 12.646381] [drm] Initialized i915 1.6.0 20160919 for 0000:00:02.0 on minor 1

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/146>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYMVe1RePLJhNz5RNFgSP-3IiGaUks5sKWargaJpZM4OMuBf>.



---

### 评论 #2 — gstoner (2017-07-04T04:50:40Z)

If PPlib fails we drop the clock to minimum frequency.  around 900 mhz or less. on vega10,  which why your seeing low performance.  we have no way for the Driver to drive the clock up with the driver since PPLIB interacts with System mangment unit which controls the clock. We will get a patch out. 

---

### 评论 #3 — jstefanop (2017-07-04T04:58:02Z)

@gstoner this issue is only present on Polaris based cards. Even so, there is no performance impact on the polaris cards. The only real impact is slow boot since, if there are several cards on the system each card takes 10+ seconds to boot. 

This issue is NOT present on Vega FE, Vega FE boots properly and is running at 1600mhz, verified by both smi utility and power consumption. This issue is not the cause of very low Vega performance.  

---

### 评论 #4 — gstoner (2017-07-04T20:03:16Z)

Looking at the slow boot time is there more than 10 GPU in the system. 

---

### 评论 #5 — jstefanop (2017-07-04T20:20:09Z)

Our systems are designed for 16+ but this issue is present even on normal boards with a single gpu running ROCm kernel. Every Polaris based gpu hangs for ~ 10 seconds as amdgpu drm posts them. 

---

### 评论 #6 — gstoner (2017-07-04T20:22:33Z)

How many PLX, and how deep, I mean are you cascading PLX switch like tree 2 to 3 layer deep.

Also

Greg
On Jul 4, 2017, at 3:20 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


Our systems are designed for 16+ but this issue is present even on normal boards with a single gpu running ROCm kernel. Every Polaris based gpu hangs for ~ 10 seconds as amdgpu drm posts them.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/146#issuecomment-312947769>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubdBknyYVqSZgwbPmkREG23KwNIQks5sKp56gaJpZM4OMuBf>.



---

### 评论 #7 — jstefanop (2017-07-04T20:39:45Z)

Only two switches off the root complex. Each switch feeds 8 GPUs. Either way this issue is present with the GPU plugged directly into the root 16x lanes coming from CPU. 

I will try the ryzen setup later to rule out any issues with kabylake i3 we are using on our test bench. 

Are you able to reproduce the issue with your systems? 

---

### 评论 #8 — gstoner (2017-07-04T21:58:25Z)

What are the exact plx you are using?  We only have plx8747 based systems.

Get Outlook for iOS<https://aka.ms/o0ukef>



On Tue, Jul 4, 2017 at 3:39 PM -0500, "jstefanop" <notifications@github.com<mailto:notifications@github.com>> wrote:


Only two switches off the root complex. Each switch feeds 8 GPUs. Either way this issue is present with the GPU plugged directly into the root 16x lanes coming from CPU.

I will try the ryzen setup later to rule out any issues with kabylake i3 we are using on our test bench.

Are you able to reproduce the issue with your systems?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/146#issuecomment-312949767>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuY3qa0TtWKHcSdh5mJdQ_sVOt3SWks5sKqMTgaJpZM4OMuBf>.


---

### 评论 #9 — jstefanop (2017-07-05T21:45:41Z)

Lets forget our custom systems for now, since we are testing on the simplest system possible to reduce variables. 

We can confirm this issue is present on your Ryzen platform as well, so its definitely a driver bug on the ROCm stack. 

Here is the exact test bench rig

Ryzen 5 1400
ASRock AB350 Pro 4
16 GB Dual Channel Corsair 2400 RAM
Power Color 570 4GB on main 16x slot (pcie lanes from CPU) (issue happens across multiple test cards on polaris line from 470/480/580s)
Fresh 16.04.02 with ROCm kernel


---

### 评论 #10 — gstoner (2017-07-06T00:38:47Z)

We use Ryzen, EPYC,, Ryzen ThreadRipper, Intel Xeon E5, Intel Core I7, I5 for testing.   We double check your finding to see if there is an issue is an issue or is a motherboard system bios issue.  

ROCm was Enterprise Server focused, the primary server system under test is SuperMicro SYS-1028 GQ, SYS-7048, SYS-4028 with Xeon E5 v3 & v4 processors. We also have a number Inventec P45 EPYC server and K888 Intel Xeon E5 systems under test.  We also test Lenovo, Dell and HP servers. 

---

### 评论 #11 — jstefanop (2017-07-06T01:03:10Z)

@gstoner yea like i mentioned its not that huge of an issue, since Polaris has its own consumer stack that works fine on all our systems, and this issue is not present on vega with this driver stack. Only reason I mention it is because Polaris cards are officially supported by the ROCm stack. 

---

### 评论 #12 — gstoner (2017-07-06T01:13:31Z)

We are going to dig in on Polaris since MI6 is Polaris 10 based.    One thing we  I need to evaluate is there is the issue in the VBIOS on the RX580 or this device ID issue for that card.    We not in Markham so we do not alway get the newest consumer hardware 

---

### 评论 #13 — gstoner (2017-07-06T01:30:53Z)

Also I am going to check the performance  Vega OpenCL - Windows vs ROCm, plus Polaris and Fiji  Windows vs ROCm vs 17.20
On Jul 5, 2017, at 8:03 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> yea like i mentioned its not that huge of an issue, since Polaris has its own consumer stack that works fine on all our systems, and this issue is not present on vega with this driver stack. Only reason I mention it is because Polaris cards are officially supported by the ROCm stack.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/146#issuecomment-313266961>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuWLWXyJJO6ySb5ZPoDXHop-FCBdNks5sLDJPgaJpZM4OMuBf>.



---

### 评论 #14 — jstefanop (2017-07-15T23:23:13Z)

Was this resolved?


---

### 评论 #15 — gstoner (2017-07-15T23:43:35Z)

We found the issue it on MSI motherboard there is APCI issue in the Linux kernel, we have back patch in 1.6.1 

---

### 评论 #16 — gstoner (2017-07-15T23:44:01Z)

The SBIOS issue and Base Linux kernel issue not ROCm 

---

### 评论 #17 — maxlim0 (2017-08-29T15:27:07Z)

I have same issue. Do you have some way to resolve this?

---

### 评论 #18 — gstoner (2017-08-29T16:46:50Z)

@maxsolyaris. We updated the 4.11 Linux kernel which fixed this issue, on MSI motherboard you also need to update the SBIOS. 

---

### 评论 #19 — rhlug (2017-10-10T16:33:46Z)

FWIW - I'm on latest bios on my MSI X370 A4 Gaming Plus (Sept 21 bios), and I still see these errors on bootup w/ RX470 and RX570 against the 4.11 rocm kernel.

---

### 评论 #20 — delbabrour (2017-12-16T22:43:49Z)

+1 i have this Issue on Msi z270-A Pro only on modded Bios on 570/580
Bios Update didn't Help,

Kernel needs to be updated to 4.14 at least

---

### 评论 #21 — duall (2017-12-20T15:40:26Z)

Updated both kernel 4.14 and BIOS for H110 BTC+. Still having this crash when restarting.

---

### 评论 #22 — gstoner (2017-12-20T16:35:30Z)

4.15 will be part of our next release.  Note 4.14 Linux kernel does not have all the feature need for DGPU yet to run ROCm.  Linux Kernel 4.16 is the   first upstream  release that should have everything you need build the driver for DGPU for ROCm 

Greg

---

### 评论 #23 — ghost (2018-01-01T12:04:27Z)

dear all. i stompled in googling this error. Iam on MSI Z170A Gaming M5 with 7x rx580 and 2~3 of them sitting at base clock(stock bios). A modified bios can not boot at all with linux.(arch)

is there a way to handle this issue?

---

### 评论 #24 — fresm (2018-01-08T20:25:39Z)

I'm using Kernel 4.15.0-rc7 (!) and still getting error messages from my RX 460:
```
amdgpu: [powerplay] 
failed to send message 309 ret is 254
```
```
amdgpu: [powerplay] 
failed to send pre message 14e ret is 254 
```

---

### 评论 #25 — Ben-and-Ellen (2018-03-03T02:44:18Z)

I'm seeing lots of these following errors on my ASUS B250 MINING EXPERT LGA 1151 Intel B250 HDMI SATA 6Gb/s USB 3.1 ATX Intel Motherboard:

Mar 02 18:37:41 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP08.PXSX._DSM: Argum
Mar 02 18:37:41 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP08.PXSX._DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
Mar 02 17:28:17 u-miner-1 kernel: ACPI Warning: \_SB_.PCI0.RP12.PXSX._DSM: Argum
                                   failed to send message 260 ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
                                   failed to send message 15b ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
                                   failed to send pre message 155 ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
                                   failed to send message 155 ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
                                   failed to send pre message 260 ret is 0

I'm using Ubuntu 16.04 LTS
4.4.0-112-generic

Ben


---

### 评论 #26 — gstoner (2018-03-03T04:22:11Z)

Use the 4.13 Linux kernel

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Ben-and-Ellen <notifications@github.com>
Sent: Friday, March 2, 2018 8:44:20 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Polaris "failed to send message" errors during boot. (#146)


I'm seeing lots of these following errors on my ASUS B250 MINING EXPERT LGA 1151 Intel B250 HDMI SATA 6Gb/s USB 3.1 ATX Intel Motherboard:

Mar 02 18:37:41 u-miner-1 kernel: ACPI Warning: _SB_.PCI0.RP08.PXSX.DSM: Argum
Mar 02 18:37:41 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP08.PXSX.DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX.DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX.DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX.DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX.DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX.DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX.DSM: Argum
Mar 02 18:37:42 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX.DSM: Argum
Mar 02 17:28:17 u-miner-1 kernel: ACPI Warning: _SB.PCI0.RP12.PXSX._DSM: Argum
failed to send message 260 ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
failed to send message 15b ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
failed to send pre message 155 ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
failed to send message 155 ret is 0
Mar 02 10:35:52 u-miner-1 kernel: amdgpu: [powerplay]
failed to send pre message 260 ret is 0

I'm using Ubuntu 16.04 LTS
4.4.0-112-generic

Ben

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/146#issuecomment-370110359>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubSKx6P7HOyrrxtgy2sHRHf8QTZDks5tagOEgaJpZM4OMuBf>.


---

### 评论 #27 — temandroid (2018-03-30T11:23:12Z)

Still have this problem on ASUS B250 MINING EXPERT
After reboot have this:
[ 1064.038377] amdgpu: [powerplay]
                failed to send pre message 5c ret is 0
[ 1064.729920] amdgpu: [powerplay]
                failed to send message 5c ret is 0
[ 1065.421900] amdgpu: [powerplay]
                failed to send pre message 5c ret is 0
[ 1066.112248] amdgpu: [powerplay]
                failed to send message 5c ret is 0
[ 1066.804520] amdgpu: [powerplay]
                failed to send pre message 5c ret is 0
[ 1067.495635] amdgpu: [powerplay]
                failed to send message 5c ret is 0
[ 1068.186297] amdgpu: [powerplay]
                failed to send pre message 5c ret is 0
[ 1068.876823] amdgpu: [powerplay]
                failed to send message 5c ret is 0
After cold boot - everything is ok...
4.13.0-37-generic #42x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.4 LTS"
NAME="Ubuntu"
VERSION="16.04.4 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.4 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609
amdgpu-pro-17.50-552542
ROCm 1.7.137


---

### 评论 #28 — MoneroCrusher (2018-05-24T18:09:10Z)

Same problem here
TB250 BTC PRO

---

### 评论 #29 — Asutorufa (2018-06-03T08:19:50Z)

Same problem

```
Jun  3 15:51:38 kernel: [   39.785164] amdgpu: [powerplay] DPM is already running
Jun  3 15:51:38 kernel: [   39.790440] amdgpu: [powerplay] 
Jun  3 15:51:38 kernel: [   39.790440]  failed to send message 309 ret is 254 
Jun  3 15:51:38 kernel: [   39.790464] amdgpu: [powerplay] 
Jun  3 15:51:38 kernel: [   39.790464]  failed to send pre message 14e ret is 254 
```


---

### 评论 #30 — Joe-Lapetoire (2018-06-21T18:01:48Z)

same problem...
Linux 4.4.0-128
Rocm 1.8


---

### 评论 #31 — technatelogy (2018-08-08T21:07:54Z)

I might have figured this out for the B250 mining expert on ubuntu 16.04. If I had a card plugged into the primary A1 slot (the first x16/full size) while mining I would get these errors and rocm-smi would timeout on the card in that particular slot (while throwing more of these errors). But if I don't use it, everything is happy. Note: I am using an older AMDGPU Pro driver (17.40)  and I'm still on the 4.10 kernel, but it's crunching away happily now and I can use rocm-smi without error. So not sure if it's related at all or what it doesn't like about that first x16 slot (did not try the second either) but might be related?

Edit: Oops, actually I see this issue is for ROCm driver, so probably not helpful :/

---

### 评论 #32 — nottux (2018-09-10T10:20:11Z)

same issue for kernels newer than 4.16
4.17 and 4.18 performs bad and 4.19 doesn't even boot
my issue pages: [reddit](https://www.reddit.com/r/linuxquestions/comments/9dvf97/is_anyone_heaving_this_issue_amdgpu_ac_adaptor/), [archlinux](https://bbs.archlinux.org/viewtopic.php?pid=1804761#p1804761), [manjaro](https://forum.manjaro.org/t/new-kernel-causes-amdgpu-error-if-ac-adaptor-is-plugged-in/56508/3)

---
