# Way to query GPU UUID or S/N?

> **Issue #310**
> **状态**: closed
> **创建时间**: 2018-01-24T11:14:55Z
> **更新时间**: 2023-04-20T10:43:23Z
> **关闭时间**: 2019-10-22T15:37:05Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/310

## 描述

Is there a way to query a per-GPU identifier, such as a GUID, UUID or serial number?


---

## 评论 (38 条)

### 评论 #1 — gstoner (2018-01-25T15:10:40Z)

Currently, we do not have per-gpu HW S/N identifier like Nvidia. We have a unique Linux DRM ID that’s only valid for the session the GPU is active. 

I am working on new SMI tools and API to  add in more of this functionality 

---

### 评论 #2 — preda (2018-01-26T21:25:22Z)

Thanks!

---

### 评论 #3 — bardabarut (2018-11-03T18:36:10Z)

Anything succeeded in this direction?

---

### 评论 #4 — valeriob01 (2019-03-07T09:07:16Z)

A per-gpu identifier would help us much.


---

### 评论 #5 — kentrussell (2019-04-03T10:33:21Z)

Sorry that I am late to the show. The KFD supports this with /sys/class/kfd/kfd/topology/nodes/X/gpu_id, which is a decimal representation of the PCIe location of the device. This will be constant as it's based on the physical PCIe location, not on DRM enumeration, and is unique even for multi-GPU cards

---

### 评论 #6 — bardabarut (2019-04-23T04:33:05Z)

Thanks, but it's not quite that, you need a unique GPU identifier, then what you offer can be received and that's right.

hwinfo --gfxcard | grep -n2 "PCI" | grep "Unique ID:" | awk '{print $ 4}'

---

### 评论 #7 — kentrussell (2019-04-23T12:24:58Z)

I am working on providing an actual Unique ID instead of just using that PCIe location above (which was mediocre at best). It will hopefully make it into 2.5

---

### 评论 #8 — lookfirst (2019-06-02T04:54:02Z)

@kentrussell Can you please re-open this issue since it isn't resolved? This is something I'd definitely like access to as well!

---

### 评论 #9 — kentrussell (2019-06-03T04:11:21Z)

It will be in 2.5, but I can reopen until that comes out. 

---

### 评论 #10 — kentrussell (2019-06-03T13:55:37Z)

I unfortunately missed the 2.5 cutoff for the SMI, but I plan to upload the changes to the krussell/fixes branch once 2.5 is released. The kernel will have the required code, the SMI tie-in code will be missing, but you can just grab the krussell/fixes branch (once 2.5 is released) and just drop the rocm_smi.py file into your system and you're golden. Sorry for the workaround, but at least we'll have something we can do in the interim.

---

### 评论 #11 — preda (2019-06-03T22:38:40Z)

What about an API for OpenCL?

---

### 评论 #12 — kentrussell (2019-06-04T13:14:15Z)

If someone in OpenCL wants to write it, they can go right ahead. It's just referencing a sysfs file called unique_id , so it's fine if someone wants to. There is also the SMI Lib, which will reference it in either 2.5 or 2.6.

---

### 评论 #13 — lookfirst (2019-06-04T13:19:50Z)

```
  /sys# find . -name "*unique*"
./devices/pci0000:00/0000:00:17.0/ata1/host0/scsi_host/host0/unique_id
./devices/pci0000:00/0000:00:17.0/ata6/host5/scsi_host/host5/unique_id
./devices/pci0000:00/0000:00:17.0/ata4/host3/scsi_host/host3/unique_id
./devices/pci0000:00/0000:00:17.0/ata2/host1/scsi_host/host1/unique_id
./devices/pci0000:00/0000:00:17.0/ata5/host4/scsi_host/host4/unique_id
./devices/pci0000:00/0000:00:17.0/ata3/host2/scsi_host/host2/unique_id
```

But `cat` on one of those id's is just a simple number like `1`.

---

### 评论 #14 — kentrussell (2019-06-04T13:28:35Z)

What does "cat /sys/class/drm/card*/device/unique_id" return? Note also that this is only supported on GFX9+
The links that you put above are for the unique_id for your hard disks, so I don't know why they ended up putting 1 for all of them, but that's up to the ATA driver

---

### 评论 #15 — lookfirst (2019-06-04T13:41:20Z)

0

This is on a machine running `[AMD/ATI] Vega 10 [Radeon RX Vega] (rev c3)`

But it also has 12 gpu's and that output only has 6 results, so maybe it
isn't related?

jon


On Tue, Jun 4, 2019 at 8:28 PM Kent Russell <notifications@github.com>
wrote:

> What does "cat /sys/class/drm/card0/device/unique_id" return? Note also
> that this is only supported on GFX9+
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/310?email_source=notifications&email_token=AAAU224LCVHNW3R2IMJ6M6DPYZUY7A5CNFSM4ENML75KYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODW4SARA#issuecomment-498671684>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAAU223T5ITQWZLTRZP5U3LPYZUY7ANCNFSM4ENML75A>
> .
>


---

### 评论 #16 — kentrussell (2019-06-04T13:47:15Z)

Yeah, that seems peculiar. You're using 2.5, so does dmesg say anything after trying to do the cat command?

---

### 评论 #17 — lookfirst (2019-06-05T05:33:53Z)

```
root@:~# dmesg | tail -1
[73290.480420] perf: interrupt took too long (4995 > 4927), lowering kernel.perf_event_max_sample_rate to 40000
root@:~# cat /sys/devices/pci0000:00/0000:00:17.0/ata1/host0/scsi_host/host0/unique_id
1
root@:~# dmesg | tail -1
[73290.480420] perf: interrupt took too long (4995 > 4927), lowering kernel.perf_event_max_sample_rate to 40000
```


---

### 评论 #18 — kentrussell (2019-06-05T11:32:41Z)

Ok if the command that I gave further up doesn't give any results, the unique_id isn't present on the system for the gpu. The path that you list there is for the SATA devices, not for the gpu.

Do you have the 2.5 package installed. I don't know when they are actually releasing it, or if it's out already. 

---

### 评论 #19 — kentrussell (2019-06-07T12:24:18Z)

I missed the 2.5 cutoff for the SMI, but I have uploaded the patches to the SMI's "krussell/fixes" branch. You can use that SMI with the 2.5 release to get the unique_id for the GPUs. But the 2.5 kernel needs to be installed for it to work, 2.4 didn't have the required sysfs file

---

### 评论 #20 — kentrussell (2019-10-22T15:37:05Z)

UUID is available in ROCm. 2.10 will have support for serial number, but only from server Vega20 cards. There is a specialized chip on the server cards that stores the serial number, unfortunately it is not present on consumer cards, which is frustrating. But UUID works for all AMD GPUs

---

### 评论 #21 — preda (2019-11-28T12:08:14Z)

@kentrussell could you please explain the difference between UUID and serial-number in this context?
- Do I understand correctly that for RadeonVII (Vega20) what we have is serial-number?
- What do you mean by "UUID is available in ROCm"?

In order to expose the serial in OpenCL, from what I understand, an extension would need to be defined and added to clGetDeviceInfo() (similar to the existing CL_DEVICE_GLOBAL_FREE_MEMORY_AMD), e.g.

CL_DEVICE_SERIAL_AMD or CL_DEVICE_ID_AMD
And the whole thing submitted to Khronos for approval, I imagine AMD could initiate that if desired.


---

### 评论 #22 — kentrussell (2019-11-28T13:05:46Z)

UUID is a universally unique ID, but is NOT the serial number printed on the sticker on the back of the card. Unfortunately the serial number can only be read on server cards due to the configuration of the card itself, so the Radeon VII will not have this functionality (tentatively planned for ROCm 3.0 now). UUID will never change, but it will not match the serial number printed on the sticker on the back of the card. I implemented the UUID as a solution for people who wanted the serial number on consumer cards, as it was the best option we had available for uniquely identifying consumer cards.

---

### 评论 #23 — valeriob01 (2019-11-29T06:20:41Z)

> Thanks, but it's not quite that, you need a unique GPU identifier, then what you offer can be received and that's right.
> 
> hwinfo --gfxcard | grep -n2 "PCI" | grep "Unique ID:" | awk '{print $ 4}'

"hwinfo --gfxcard" output, UUID does look like this, with a dot:

  Unique ID: IluS.msy7ZveCwh5



---

### 评论 #24 — kentrussell (2019-11-29T13:39:30Z)

That's a different one from what I'm talking about. You can do "cat /sys/class/drm/card0/device/unique_id" to get the one that I'm referring to (provided that your card is card0, if you have multiple cards, replace the 0 with a * to get all unique IDs). It's hard-coded to the card itself and doesn't rely on any software to generate it, thankfully (just to expose it). You can also use the SMI to get the ID via "rocm-smi --showuniqueid"  

---

### 评论 #25 — valeriob01 (2019-11-29T14:25:24Z)

> That's a different one from what I'm talking about. You can do "cat /sys/class/drm/card0/device/unique_id" to get the one that I'm referring to (provided that your card is card0, if you have multiple cards, replace the 0 with a * to get all unique IDs). It's hard-coded to the card itself and doesn't rely on any software to generate it, thankfully (just to expose it). You can also use the SMI to get the ID via "rocm-smi --showuniqueid"

The best way to confuse people: having multiple "Unique IDs".


---

### 评论 #26 — kentrussell (2019-11-29T15:26:14Z)

Totally agreed. HWINFO generates their own UUID, They don't use the functionality that I implemented because they didn't know that it existed, or they just implemented their version far before our implementation, or they have their own UUID format for everything (which I assume is the case, all of their unique IDs have a XXXX.XXXXXXXXXXX format, even though I am pretty sure every other company doesn't use that format). I don't know how they generate their UUID unfortunately, as I am still searching through github to see where they get their UUID from, but it does appear to be a proprietary format unique to HWINFO

I am sure that hwinfo's UUIDs are all consistent with one another, and ours are consistent with one another, unfortunately they don't quite align as you've noticed. I am pretty sure HWINFO's UUID was implemented far before ours was, ours is just something we can expose that's hard-coded on the GPU itself. So as long as you use the same tools, you're set, but mixing-and-matching doesn't seem to align as nicely as we would like.

---

### 评论 #27 — valeriob01 (2019-11-29T15:41:45Z)

This is a thing to remember when selecting tools, it is preferable to rely on UUID that is hard-coded on the gpu than on UUID that is generated by the tool and with a different format. One thing that could be useful is API access to the UUID so that programs can retrieve it.

---

### 评论 #28 — kentrussell (2019-11-29T16:05:53Z)

Exactly. The rocm_smi_lib provides a C/C++ interface which accesses this UUID (see https://github.com/RadeonOpenCompute/rocm_smi_lib/blob/master/src/rocm_smi.cc#L2368). Plus it's part of the sysfs pool so it can be accessed by any tool that can read files, which helps too.  It's up to the various tools guys to implement it. 

@valeriob01 Thanks for the advice suggesting using the same tools where possible. While UUID is Universally Unique, there is no convention requiring that everyone's UUIDs are identical. A slight downside with having multiple tools developed my multiple companies across the globe.

---

### 评论 #29 — valeriob01 (2020-02-02T10:22:07Z)

> Exactly. The rocm_smi_lib provides a C/C++ interface which accesses this UUID (see https://github.com/RadeonOpenCompute/rocm_smi_lib/blob/master/src/rocm_smi.cc#L2368). Plus it's part of the sysfs pool so it can be accessed by any tool that can read files, which helps too. It's up to the various tools guys to implement it.
> 
> @valeriob01 Thanks for the advice suggesting using the same tools where possible. While UUID is Universally Unique, there is no convention requiring that everyone's UUIDs are identical. A slight downside with having multiple tools developed my multiple companies across the globe.

Problem in multi-gpu systems: unique_id for card0 is empty. Files missing.
Other cards work fine...
card0 : empty
card1,2,3 : not empty.


https://github.com/preda/gpuowl/issues/96#issuecomment-581111028


---

### 评论 #30 — kentrussell (2020-02-03T13:40:23Z)

@valeriob01 That's definitely peculiar since they're all the same card. Does dmesg say anything regarding card0 (try attaching the full dmesg here for me to take a look, as well as the full "rocm-smi -a --alldevices" output)?  If there are different sysfs files like that, then maybe there's something going on with that card. Maybe dmesg/SMI output will help me figure out what's up

---

### 评论 #31 — valeriob01 (2020-02-03T13:46:22Z)

Thanks for look in At The issue.

Il Lun 3 Feb 2020, 14:40 Kent Russell <notifications@github.com> ha scritto:

> @valeriob01 <https://github.com/valeriob01> That's definitely peculiar
> since they're all the same card. Does dmesg say anything regarding card0
> (try attaching the full dmesg here for me to take a look, as well as the
> full "rocm-smi -a --alldevices" output)? If there are different sysfs files
> like that, then maybe there's something going on with that card. Maybe
> dmesg/SMI output will help me figure out what's up
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/310?email_source=notifications&email_token=AGFEKPQSQ5WNYXRD56G6YNLRBANERA5CNFSM4ENML75KYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEKT33GY#issuecomment-581418395>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AGFEKPWDZRVJ5J7DD6GKRXDRBANERANCNFSM4ENML75A>
> .
>


---

### 评论 #32 — kentrussell (2020-02-03T13:49:55Z)

> Thanks for look in At The issue. Il Lun 3 Feb 2020, 14:40 Kent Russell <notifications@github.com> ha scritto:
> […](#)
> @valeriob01 <https://github.com/valeriob01> That's definitely peculiar since they're all the same card. Does dmesg say anything regarding card0 (try attaching the full dmesg here for me to take a look, as well as the full "rocm-smi -a --alldevices" output)? If there are different sysfs files like that, then maybe there's something going on with that card. Maybe dmesg/SMI output will help me figure out what's up — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub <#310?email_source=notifications&email_token=AGFEKPQSQ5WNYXRD56G6YNLRBANERA5CNFSM4ENML75KYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEKT33GY#issuecomment-581418395>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/AGFEKPWDZRVJ5J7DD6GKRXDRBANERANCNFSM4ENML75A> .

Not a problem. Once you get a chance to attach the dmesg/SMI output, hopefully it will illuminate the issue and help us to get you back to having 4 identical cards :) 

---

### 评论 #33 — valeriob01 (2020-02-03T13:56:42Z)

> > Thanks for look in At The issue. Il Lun 3 Feb 2020, 14:40 Kent Russell [notifications@github.com](mailto:notifications@github.com) ha scritto:
> > […](#)
> > @valeriob01 https://github.com/valeriob01 That's definitely peculiar since they're all the same card. Does dmesg say anything regarding card0 (try attaching the full dmesg here for me to take a look, as well as the full "rocm-smi -a --alldevices" output)? If there are different sysfs files like that, then maybe there's something going on with that card. Maybe dmesg/SMI output will help me figure out what's up — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub <#310?email_source=notifications&email_token=AGFEKPQSQ5WNYXRD56G6YNLRBANERA5CNFSM4ENML75KYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEKT33GY#issuecomment-581418395>, or unsubscribe https://github.com/notifications/unsubscribe-auth/AGFEKPWDZRVJ5J7DD6GKRXDRBANERANCNFSM4ENML75A .
> 
> Not a problem. Once you get a chance to attach the dmesg/SMI output, hopefully it will illuminate the issue and help us to get you back to having 4 identical cards :)

Thanks, the reason is that we use unique_id to identify the card in the program gpuowl for trustworthiness.

---

### 评论 #34 — kentrussell (2020-02-03T14:18:25Z)

> > > Thanks for look in At The issue. Il Lun 3 Feb 2020, 14:40 Kent Russell [notifications@github.com](mailto:notifications@github.com) ha scritto:
> > > […](#)
> > > @valeriob01 https://github.com/valeriob01 That's definitely peculiar since they're all the same card. Does dmesg say anything regarding card0 (try attaching the full dmesg here for me to take a look, as well as the full "rocm-smi -a --alldevices" output)? If there are different sysfs files like that, then maybe there's something going on with that card. Maybe dmesg/SMI output will help me figure out what's up — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub <#310?email_source=notifications&email_token=AGFEKPQSQ5WNYXRD56G6YNLRBANERA5CNFSM4ENML75KYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEKT33GY#issuecomment-581418395>, or unsubscribe https://github.com/notifications/unsubscribe-auth/AGFEKPWDZRVJ5J7DD6GKRXDRBANERANCNFSM4ENML75A .
> > 
> > 
> > Not a problem. Once you get a chance to attach the dmesg/SMI output, hopefully it will illuminate the issue and help us to get you back to having 4 identical cards :)
> 
> Thanks, the reason is that we use unique_id to identify the card in the program gpuowl for trustworthiness.

That makes sense. If you're using KFD Topology for anything, there is a "location_id" field inside the properties file (e.g. /sys/class/kfd/kfd/topology/nodes/0/properties) which is a decimal representation of the PCI location, so that can always work in a pinch. But the fact that your one card isn't doing what it's supposed to means we should get that figured out, since that GPU might not work properly (based on its behaviour) and thus would mess up some of your gpuowl work.

---

### 评论 #35 — valeriob01 (2020-02-03T14:36:43Z)

> > > > Thanks for look in At The issue. Il Lun 3 Feb 2020, 14:40 Kent Russell [notifications@github.com](mailto:notifications@github.com) ha scritto:
> > > > […](#)
> > > > @valeriob01 https://github.com/valeriob01 That's definitely peculiar since they're all the same card. Does dmesg say anything regarding card0 (try attaching the full dmesg here for me to take a look, as well as the full "rocm-smi -a --alldevices" output)? If there are different sysfs files like that, then maybe there's something going on with that card. Maybe dmesg/SMI output will help me figure out what's up — You are receiving this because you were mentioned. Reply to this email directly, view it on GitHub <#310?email_source=notifications&email_token=AGFEKPQSQ5WNYXRD56G6YNLRBANERA5CNFSM4ENML75KYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEKT33GY#issuecomment-581418395>, or unsubscribe https://github.com/notifications/unsubscribe-auth/AGFEKPWDZRVJ5J7DD6GKRXDRBANERANCNFSM4ENML75A .
> > > 
> > > 
> > > Not a problem. Once you get a chance to attach the dmesg/SMI output, hopefully it will illuminate the issue and help us to get you back to having 4 identical cards :)
> > 
> > 
> > Thanks, the reason is that we use unique_id to identify the card in the program gpuowl for trustworthiness.
> 
> That makes sense. If you're using KFD Topology for anything, there is a "location_id" field inside the properties file (e.g. /sys/class/kfd/kfd/topology/nodes/0/properties) which is a decimal representation of the PCI location, so that can always work in a pinch. But the fact that your one card isn't doing what it's supposed to means we should get that figured out, since that GPU might not work properly (based on its behaviour) and thus would mess up some of your gpuowl work.

Ah, for that gpuowl works extremely resilient to errors...


---

### 评论 #36 — ghost (2023-01-25T03:07:15Z)

do not work on this, serious invasion of privacy
if youre doing fingerprinting this way, youre doing it wrong

---

### 评论 #37 — lookfirst (2023-01-25T04:51:16Z)

Just because @g5543 posted, I had to share this... worked great for me.

```
atitool -i=0 -sid                                                                                                                                 
ATITOOL version 1.14.0.10, Copyright (c) 2019 Advanced Micro Devices, Inc.                                                                                                           

LOT=[REMOVED],WFR=11,WFRX=12,PBI FT=0,PBI WS=0,WFRY=02,FDRY=03,FAB=01,YR=08,WK=34,REV=A1B,CHECKBIT0=0,CHECKBIT1=0,SerialID Data = [UNIQUE ID HERE]                      
LeakageValue = 6.139336 A,LeakageID = [REMOVED]   
```

---

### 评论 #38 — amoiseev (2023-04-19T19:36:10Z)

@kentrussell @gstoner
Any chance the UUID is obtainable from Windows?

---
