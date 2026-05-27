# OpenCL Kernels hang in uninterruptible sleep, same for 'clinfo'

> **Issue #195**
> **状态**: closed
> **创建时间**: 2017-09-04T13:21:33Z
> **更新时间**: 2018-06-03T14:48:30Z
> **关闭时间**: 2018-06-03T14:48:30Z
> **作者**: phschaad
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/195

## 描述

Executing OpenCL kernels (generated with LLVM's AMDGPU backend, exactly according to documentation) leads to the program waiting in uninterruptible sleep forever.
So far I have been able to observe that it usually works 2-3 times, but after that, the hanging starts to appear. `clinfo` always works, but after the hanging appears, `clinfo` starts to hang in uninterruptible sleep too.
With `ps -eo comm,wchan:32` I have been able to identify:
  - `clinfo` hangs at call `amd_sched_entity_fini`
  - the first executable that hangs, stops at call `kfd_process_notifier_release`
  - all programs after that halt at `kfd_create_process`

The GPU used is an R9 Nano (Fiji), running the latest ROCm package (clean install) from the repositories (Ubuntu 16.04).

---

## 评论 (14 条)

### 评论 #1 — gstoner (2017-09-04T19:55:39Z)

Can you run uname -a 
What CPU are you using. Which motherboard?  Are you running with X11  or headless?

Which release of Ubuntu 16.04 SP2 or SP3 

---

### 评论 #2 — gstoner (2017-09-04T20:00:10Z)

Note this is happening down in the base linux kernel driver.  Which is why in need more info. 

---

### 评论 #3 — phschaad (2017-09-04T20:38:42Z)

- `uname -a` gives back: `4.11.0-kfd-compute-rocm-rel-1.6-148 #1 SMP x86_64 x86_64 x86_64 GNU/Linux`
- The CPU is an Intel i7-7700
- The motherboard is a Dell Inc. 0MWYPT
- Running X11
- Ubuntu SP3

---

### 评论 #4 — jedwards-AMD (2017-09-05T14:38:17Z)

Please send the output of 'dmesg' as well. This will indicate if there are any errors from the KFD or the amdgpu driver.

---

### 评论 #5 — phschaad (2017-09-05T16:02:04Z)

[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/1278054/dmesg.txt)
Note: at line 1150 is where it's interesting, there it complains about `clinfo` being blocked for more than 120s and gives a call trace.

---

### 评论 #6 — jedwards-AMD (2017-09-05T18:01:50Z)

I am seeing this message in dmesg:
[  316.383137] mce_notify_irq: 1 callbacks suppressed
[  316.383140] mce: [Hardware Error]: Machine check events logged
.
Then I am seeing messages indicating that the kernel is hung and that a timeout has occurred. The ROCm device is being registered correctly and nothing else in dmesg indicates a problem, so I am wondering if we are seeing a processor hardware issue. Try this:
.
sudo apt-get install mcelog
Run your app and see if it hangs.
The events will be logged to /var/log/mcelog. You can also run:
sudo mcelog --client
to query the mcelog daemon for errors.
.
Lets see if we can catch any errors on the processor.

---

### 评论 #7 — phschaad (2017-09-05T18:14:34Z)

The mcelog output (in the log file) does not look comforting after executing `clinfo`..
Here is the logfile content:
```
mcelog: failed to prefill DIMM database from DMI data
mcelog: Family 6 Model 9e CPU: only decoding architectural errors
Hardware event. This is not a software error.
MCE 0
CPU 0 BANK 6 
MISC 7880010086 ADDR fef1ffc0 
TIME 1504517572 Mon Sep  4 11:32:52 2017
MCG status:
MCi status:
Error overflow
Uncorrected error
MCi_MISC register valid
MCi_ADDR register valid
Processor context corrupt
MCA: corrected filtering (some unreported errors in same region)
Generic CACHE Level-2 Generic Error
STATUS ee0000000040110a MCGSTATUS 0
MCGCAP c0a APICID 0 SOCKETID 0 
CPUID Vendor Intel Family 6 Model 158
mcelog: Family 6 Model 9e CPU: only decoding architectural errors
Hardware event. This is not a software error.
MCE 1
CPU 0 BANK 7 
MISC 3880010086 ADDR fef200c0 
TIME 1504517572 Mon Sep  4 11:32:52 2017
MCG status:
MCi status:
Error overflow
Uncorrected error
MCi_MISC register valid
MCi_ADDR register valid
Processor context corrupt
MCA: corrected filtering (some unreported errors in same region)
Generic CACHE Level-2 Generic Error
STATUS ee0000000040110a MCGSTATUS 0
MCGCAP c0a APICID 0 SOCKETID 0 
CPUID Vendor Intel Family 6 Model 158
mcelog: Family 6 Model 9e CPU: only decoding architectural errors
Hardware event. This is not a software error.
MCE 2
CPU 0 BANK 8 
MISC 43880010086 ADDR fef1ce80 
TIME 1504517572 Mon Sep  4 11:32:52 2017
MCG status:
MCi status:
Error overflow
Uncorrected error
MCi_MISC register valid
MCi_ADDR register valid
Processor context corrupt
MCA: corrected filtering (some unreported errors in same region)
Generic CACHE Level-2 Generic Error
STATUS ee0000000040110a MCGSTATUS 0
MCGCAP c0a APICID 0 SOCKETID 0 
CPUID Vendor Intel Family 6 Model 158
mcelog: Family 6 Model 9e CPU: only decoding architectural errors
Hardware event. This is not a software error.
MCE 3
CPU 0 BANK 9 
MISC 3880010086 ADDR fef1ff00 
TIME 1504517572 Mon Sep  4 11:32:52 2017
MCG status:
MCi status:
Error overflow
Uncorrected error
MCi_MISC register valid
MCi_ADDR register valid
Processor context corrupt
MCA: corrected filtering (some unreported errors in same region)
Generic CACHE Level-2 Generic Error
STATUS ee0000000040110a MCGSTATUS 0
MCGCAP c0a APICID 0 SOCKETID 0 
CPUID Vendor Intel Family 6 Model 158
```

---

### 评论 #8 — phschaad (2017-09-07T11:40:05Z)

Additional data point that might lead to something:
I just noticed that the last program to run before other programs start hanging (sometimes, but not always!) throws me this error:
`Memory access fault by GPU node-1 on address (nil)(may not be exact address). Reason: Unknown.`

---

### 评论 #9 — gstoner (2017-09-07T17:48:54Z)

We test on FIJI Nano extensively with Intel hardware,  Can not replicate the issue.   When you run AMDGPUpro driver do you see this issue.  

---

### 评论 #10 — phschaad (2017-09-07T22:54:54Z)

I thought the standard AMDGPUpro driver was not suitable for running said LLVM AMDGPU generated code, did I get something wrong there?

---

### 评论 #11 — gstoner (2017-09-08T03:40:36Z)

I am trying to see if you have hardware issue.  Llvm backed will not run.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Philipp Schaad <notifications@github.com>
Sent: Thursday, September 7, 2017 5:55:05 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] OpenCL Kernels hang in uninterruptible sleep, same for 'clinfo' (#195)


I thought the standard AMDGPUpro driver was not suitable for running said LLVM AMDGPU generated code, did I get something wrong there?

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/195#issuecomment-327949134>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSNJoNr0oD8hxqPsGvHlsyCgGSQ0ks5sgHQ_gaJpZM4PL6cF>.


---

### 评论 #12 — phschaad (2017-09-08T12:36:05Z)

I will check that out asap and get back to you with it. I know that before installing ROCm on a fresh system install, I had the AMDGPUpro driver running and OpenCL samples in general did not seem to pose a problem.

---

### 评论 #13 — phschaad (2017-09-20T11:43:44Z)

Additional information regarding this problem has surfaced: 
AMDGPUpro driver works, that's one thing. However there were only a few sample OpenCL programs I was able to try.
Secondly: The entire system fails when it is all on the same power supply, and I have noticed the following lines in the dmesg output (they're already to be found in the dmesg I posted here.):
`[    2.132219] amdgpu: [powerplay] Can't find requested voltage id in vdd_dep_on_sclk table!
[    2.137175] amdgpu: [powerplay] Failed to setup PCC HW register! Wrong GPIO assigned for VDDC_PCC_GPIO_PINID!`

I found [this](https://bugs.freedesktop.org/show_bug.cgi?id=100443) reference when looking it up, this is the exact same problem. This seems to be the explanation behind it.

---

### 评论 #14 — gstoner (2017-09-20T14:20:07Z)

This is pointing to a AMDGPU base driver issue, based 4.11 kernel around PPlib maybe. 

---
