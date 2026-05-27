# hashcat v4.1 mode 11300 doesn't work with ROCm 1.8.1

> **Issue #437**
> **状态**: closed
> **创建时间**: 2018-06-18T19:34:07Z
> **更新时间**: 2018-09-19T02:48:57Z
> **关闭时间**: 2018-09-19T02:48:57Z
> **作者**: hashuser1
> **标签**: Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/437

## 标签

- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

So I thought this issue was with hashcat but the admins on that project are stating the issue is with ROCm. Im going to post the issue I opened with hashcat and their response. I cant write code so please be gentle. How can I fix the JiT compiler issue?
--------------------------------------------------------------------------------------------------------------------------------

Ive been doing some testing and hashcat v3.5 and 4.1 do not work correctly when using mode 11300 (bicoin wallet) with ROCm 1.8.1.

Im using xubuntu 16.04.4, 4.13.0-45-generic.

I created a test wallet.dat with a known password and used btcrecover scripts to extract the hash. With ROCm 1.8.1 installed, hashcat does not find the password with the password in a wordlist. I thought it could be the drivers so I did a clean install and tried the AMDGPU-PRO Beta Mining Driver 17.40 with optional rocm. With the AMDGPU driver installed v.3.5 does find the password in the wordlist, but v4.1 still does not.


---------------------------------------------------------------------------------------------------------------------------------

The good thing is, hashcat informs you about the invalid kernel processing on startup:* Device #2: ATTENTION! OpenCL kernel self-test failed. However, it's not a hashcat problem. I've traced the intermediate keys up to the comparison kernel (where AES comes into play). Both the AES key and the IV is correctly computed on rocm.

The next step would be to initialize the AES key scheduler array and on here (using the same shared library code) rocm start computing invalid values. All other tested OpenCL runtimes (NVidia, Intel, pocl, etc) compute it correctly.

The key scheduler access a shared memory region of the GPU to make it faster. You can however disable this behavior and make it access constant memory region. If we do this you can see how rocm starts to crack without changing any of the code portion. You can reproduce locally by commenting out line 24 in inc_vendor.cl and remove the kernel/ cache folder entirely.

Note that the same shared AES function are used in many other kernels (truecrypt 6221 for example) and they work fine over there. This is not a problem in how shared memory is accessed.I was able to further track down the issue to this data copy from constant memory to shared memory in m11300_comp() function in m11300.cl:

    s_td0[i] = td0[i];

 So basically there's nothing we can do to make this more easy. If this doesn't work it's for sure a JiT compiler problem.
--




---

## 评论 (34 条)

### 评论 #1 — b-sumner (2018-06-18T20:48:29Z)

What is the hashcat issue number?  Can you give a command line and .hash file contents along the lines of the existing example* in the hashcat repo that will definitely exercise mode 11300?

---

### 评论 #2 — hashuser1 (2018-06-19T17:55:05Z)

hashcat issue #1596. 

The command I was using "./hashcat64.bin -m 11300 hash.txt. wordlist.txt". I would rather not give you the exact hash Im trying to crack. But you can download bitcoin-core and make a wallet using bitcoin-qt with your own known password and add it to a wordlist (most linux systems have a wordlist stored at /usr/share/dict/words or /usr/dict/words) . I used the attach script to extract the hash.
[wallet_hash_extractor.txt](https://github.com/RadeonOpenCompute/ROCm/files/2116297/wallet_hash_extractor.txt)



---

### 评论 #3 — b-sumner (2018-06-19T18:37:47Z)

Would it be possible for you to post the hash to "xyzzy" here?  It is already in example.dict

---

### 评论 #4 — hashuser1 (2018-06-19T18:41:26Z)

Think the minimum is 10 characters when using the qt wallet. But yes, if
you give me a 10 character password I will make you a wallet and post the
hash.

On Tue, Jun 19, 2018, 11:37 b-sumner <notifications@github.com> wrote:

> Would it be possible for you to post the hash to "xyzzy" here? It is
> already in example.dict
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-398502125>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AmebeYorMI-6QWYE2QFhT7HKkqMgaLsLks5t-UUAgaJpZM4UsWVL>
> .
>


---

### 评论 #5 — b-sumner (2018-06-19T19:20:07Z)

Thank you very much.  How about "zzzzzzzzzz" (10 z's), also located in example.dict.

---

### 评论 #6 — hashuser1 (2018-06-19T19:43:32Z)

As requested.
[hash.txt](https://github.com/RadeonOpenCompute/ROCm/files/2116675/hash.txt)


---

### 评论 #7 — b-sumner (2018-06-19T20:06:06Z)

Thanks.  I see that a debug build of the compiler is asserting.  We'll follow up on this.

---

### 评论 #8 — hashuser1 (2018-06-19T21:28:29Z)

So this was a known issue?

On Tue, Jun 19, 2018, 13:06 b-sumner <notifications@github.com> wrote:

> Thanks. I see that a debug build of the compiler is asserting. We'll
> follow up on this.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-398527730>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AmebeTl464iPpiCk5db6jY1Lb64qD4yOks5t-Vm0gaJpZM4UsWVL>
> .
>


---

### 评论 #9 — gstoner (2018-06-19T21:32:26Z)

no it is not known issue 

---

### 评论 #10 — hashuser1 (2018-07-08T22:12:00Z)

Any update on this? Additionally, is there any work around to get this to work? Like if I try CENTOS instead or try a newer/older kernel in Ubuntu. I don't understand if the  problem is with Rocm and the way it can't perform math functions correctly or just a bug in version 1.8 and the version of Ubuntu I'm using? I guess I'm saying can you prove this ever worked with any version since 1.6? 

---

### 评论 #11 — ghost (2018-07-13T03:41:20Z)

I just noticed the same behavior, can you try compiling hash cat with https://developer.amd.com/amd-aocc/ . Then try the amd sdk 2.6 .

---

### 评论 #12 — hashuser1 (2018-07-13T21:23:51Z)

I will make an attempt. I would appreciate an answer though. Has this ever worked with any version of ROCm since 1.6? And please understand, Im not pointing any fingers (the problem still could be hashcat), I just want to know if Ive wasted 7 months of letting hashcat run under different settings just to find out it will never solve the problem.

---

### 评论 #13 — hashuser1 (2018-07-13T22:19:58Z)

Followed instructions listed here.
https://developer.amd.com/wordpress/media/2017/04/AOCC-1.2.1-Install-Guide.pdf

Hashcat is still giving the following error
"Device #1: ATTENTION! OpenCL kernel self-test failed."

Maybe I edited the make file incorrectly?
[makefile_edited.txt](https://github.com/RadeonOpenCompute/ROCm/files/2194333/makefile_edited.txt)
[Makefile_original.txt](https://github.com/RadeonOpenCompute/ROCm/files/2194334/Makefile_original.txt)
[make_output.txt](https://github.com/RadeonOpenCompute/ROCm/files/2194365/make_output.txt)







---

### 评论 #14 — hashuser1 (2018-07-13T22:29:42Z)

Cant find the AMD SDK 2.6, its not listed at either of the following links.
https://developer.amd.com/tools-and-sdks/ 
http://developer.amd.com/sdks/AMDAPPSDK/downloads/Pages/default.aspx

---

### 评论 #15 — hashuser1 (2018-07-27T00:41:57Z)

I noticed 1.8.2 was released. I tried using centOS 7.5 and hashcat is still giving the error "
"Device #1: ATTENTION! OpenCL kernel self-test failed." I tried compiling using devtoolset and another try using AOCC. Still broken.

 Is this problem limited to Polaris? Or should I just give up and use NVIDIA hardware? 


---

### 评论 #16 — ghost (2018-07-27T00:49:01Z)

No this is a known issue that there is a thread on relating to NVIDIA
causing opencl to fail.

On Fri, Jul 27, 2018 at 8:42 AM, hashuser1 <notifications@github.com> wrote:

> I noticed 1.8.2 was released. I tried using centOS 7.5 and hashcat is
> still giving the error "
> "Device #1 <https://github.com/RadeonOpenCompute/ROCm/pull/1>: ATTENTION!
> OpenCL kernel self-test failed." I tried compiling using devtoolset and
> another try using AOCC. Still broken.
>
> Is this problem limited to Polaris? Or should I just give up and use
> NVIDIA hardware?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-408277049>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AWn0wxHtIbIXwKGVzlcjvI9ms6fZK-DMks5uKmHZgaJpZM4UsWVL>
> .
>


---

### 评论 #17 — hashuser1 (2018-07-27T01:51:41Z)

Do you have a link to that thread? Currently hashcat admins are claiming
that opencl on both Intel and nvidia are performing fine using mode 11300.

On Thu, Jul 26, 2018, 17:49 The Doctor <notifications@github.com> wrote:

> No this is a known issue that there is a thread on relating to NVIDIA
> causing opencl to fail.
>
> On Fri, Jul 27, 2018 at 8:42 AM, hashuser1 <notifications@github.com>
> wrote:
>
> > I noticed 1.8.2 was released. I tried using centOS 7.5 and hashcat is
> > still giving the error "
> > "Device #1 <https://github.com/RadeonOpenCompute/ROCm/pull/1>:
> ATTENTION!
> > OpenCL kernel self-test failed." I tried compiling using devtoolset and
> > another try using AOCC. Still broken.
> >
> > Is this problem limited to Polaris? Or should I just give up and use
> > NVIDIA hardware?
> >
> > —
> > You are receiving this because you commented.
> > Reply to this email directly, view it on GitHub
> > <
> https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-408277049
> >,
> > or mute the thread
> > <
> https://github.com/notifications/unsubscribe-auth/AWn0wxHtIbIXwKGVzlcjvI9ms6fZK-DMks5uKmHZgaJpZM4UsWVL
> >
> > .
> >
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-408278061>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AmebeegZo2LZOBCNtBQwOCIMbiCaCd27ks5uKmOGgaJpZM4UsWVL>
> .
>


---

### 评论 #18 — hashuser1 (2018-08-20T23:06:53Z)

Any update?

---

### 评论 #19 — b-sumner (2018-08-20T23:20:33Z)

We've fixed the cause of the assertion that was being hit here and by other unrelated applications.  Following that, hashcat 4.2 successfully finds the password for hash.txt.   I'm not really clear on when those compiler fixes will appear in a release.  

---

### 评论 #20 — hashuser1 (2018-08-21T03:10:11Z)

How can I get the updates?

On Mon, Aug 20, 2018, 16:20 b-sumner <notifications@github.com> wrote:

> We've fixed the cause of the assertion that was being hit here and by
> other unrelated applications. Following that, hashcat 4.2 successfully
> finds the password for hash.txt. I'm not really clear on when those
> compiler fixes will appear in a release.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-414495165>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Amebecdn_MQgozgJb4A6M2-jx-81IcAzks5uS0REgaJpZM4UsWVL>
> .
>


---

### 评论 #21 — hashuser1 (2018-09-11T15:47:04Z)

I'm a little confused. I opened a ticket with AMD directly and their team
claims there is nothing wrong. Can you please talk to them and allow the
right hand to know what the left one is doing?

Your service request : SR #{ticketno:[8200822583]} has been reviewed and
> updated.
>
> Response and Service Request History:
>
> I really appreciate your patience while I look into your issue.
>
> Feedback from the SW team is that the issue isn't observed in Hashcat
> v4.2.1 using ROCm 1.8.x and works just fine.
>

On Mon, Aug 20, 2018, 20:10 Manuel Ortega <manuel.ortega.jr@gmail.com>
wrote:

> How can I get the updates?
>
> On Mon, Aug 20, 2018, 16:20 b-sumner <notifications@github.com> wrote:
>
>> We've fixed the cause of the assertion that was being hit here and by
>> other unrelated applications. Following that, hashcat 4.2 successfully
>> finds the password for hash.txt. I'm not really clear on when those
>> compiler fixes will appear in a release.
>>
>> —
>> You are receiving this because you authored the thread.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-414495165>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/Amebecdn_MQgozgJb4A6M2-jx-81IcAzks5uS0REgaJpZM4UsWVL>
>> .
>>
>


---

### 评论 #22 — hashuser1 (2018-09-11T16:09:07Z)

I guess to clarify. When you tested 4.2, did the opencl self check pass?
Because I cannot get the self check to pass. Are you using extra grub
comments? And are you using rx580s and 1950x processor?

On Tue, Sep 11, 2018, 08:46 Manuel Ortega <manuel.ortega.jr@gmail.com>
wrote:

> I'm a little confused. I opened a ticket with AMD directly and their team
> claims there is nothing wrong. Can you please talk to them and allow the
> right hand to know what the left one is doing?
>
> Your service request : SR #{ticketno:[8200822583]} has been reviewed and
> > updated.
> >
> > Response and Service Request History:
> >
> > I really appreciate your patience while I look into your issue.
> >
> > Feedback from the SW team is that the issue isn't observed in Hashcat
> > v4.2.1 using ROCm 1.8.x and works just fine.
> >
>
> On Mon, Aug 20, 2018, 20:10 Manuel Ortega <manuel.ortega.jr@gmail.com>
> wrote:
>
>> How can I get the updates?
>>
>> On Mon, Aug 20, 2018, 16:20 b-sumner <notifications@github.com> wrote:
>>
>>> We've fixed the cause of the assertion that was being hit here and by
>>> other unrelated applications. Following that, hashcat 4.2 successfully
>>> finds the password for hash.txt. I'm not really clear on when those
>>> compiler fixes will appear in a release.
>>>
>>> —
>>> You are receiving this because you authored the thread.
>>> Reply to this email directly, view it on GitHub
>>> <https://github.com/RadeonOpenCompute/ROCm/issues/437#issuecomment-414495165>,
>>> or mute the thread
>>> <https://github.com/notifications/unsubscribe-auth/Amebecdn_MQgozgJb4A6M2-jx-81IcAzks5uS0REgaJpZM4UsWVL>
>>> .
>>>
>>


---

### 评论 #23 — b-sumner (2018-09-14T20:04:03Z)

I'm running on gfx803, but I only have one installed.  Running the hash you provided against example.dict:

hashcat (v4.2.1-51-gc8dbcf9) starting...

OpenCL Platform #1: Advanced Micro Devices, Inc.
================================================
* Device #1: gfx803, 3481/4096 MB allocatable, 64MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1
...
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:198432-198443
Candidates.#1....: 0 -> zzzzzzzzzzz
Hardware.Mon.#1..: Temp: 68c Fan: 27% Core: 874MHz Mem: 500MHz Bus:0

Started: Fri Sep 14 12:55:46 2018
Stopped: Fri Sep 14 13:00:23 2018

Can you post here what hashcat says for you?  I see you have two gfx803.  Does selftest fail on both devices or just one?  If just one, does it run if you remove the other?  Does it run with just the other?

---

### 评论 #24 — hashuser1 (2018-09-14T20:26:27Z)

Are you using the AOCC compiled binary or the precompiled binary? The output below is from the precomiled binary (both devices fail self test). When I try to compile using AOCC it gives an error about missing <Alloc.h>. See hashcat issue# #1691. 

./hashcat64.bin -b -m 11300
hashcat (v4.2.1) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

OpenCL Platform #1: Advanced Micro Devices, Inc.
================================================
* Device #1: gfx803, 3481/4096 MB allocatable, 36MCU
* Device #2: gfx803, 3481/4096 MB allocatable, 36MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 11300 - Bitcoin/Litecoin wallet.dat (Iterations: 199999)

* Device #1: ATTENTION! OpenCL kernel self-test failed.

Your device driver installation is probably broken.
See also: https://hashcat.net/faq/wrongdriver

* Device #2: ATTENTION! OpenCL kernel self-test failed.

Your device driver installation is probably broken.
See also: https://hashcat.net/faq/wrongdriver

Speed.Dev.#1.....:     2557 H/s (72.67ms) @ Accel:128 Loops:32 Thr:256 Vec:1
Speed.Dev.#2.....:     2572 H/s (72.57ms) @ Accel:128 Loops:32 Thr:256 Vec:1
Speed.Dev.#*.....:     5129 H/s

Started: Fri Sep 14 13:21:23 2018
Stopped: Fri Sep 14 13:21:57 2018


---

### 评论 #25 — hashuser1 (2018-09-14T20:30:04Z)

I also noticed your gfx803 has  64MCU while mine are showing 36MCU. Is my configuration messed up?

---

### 评论 #26 — b-sumner (2018-09-14T20:34:52Z)

I'm not sure what you mean by "AOCC compiled binary or precompiled binary".   I simply cloned the hascat repo, and followed the directions in BUILD.md, except I stopped before "make install".

I think gfx803 comes in different packages.  I apparently have one with more CUs.

---

### 评论 #27 — hashuser1 (2018-09-14T20:39:15Z)

Can I see the output from 'clang -v' on the machine you compiled it on? Or did you compile using gcc? In the ticket listed above (SR #{ticketno:[8200822583]}), I was told you were compiling using AMD AOCC.

https://developer.amd.com/amd-aocc/ 



---

### 评论 #28 — jlgreathouse (2018-09-14T20:41:01Z)

A 36 CU gfx803 is likely Polaris 10. @b-sumner is likely using Fiji, which has 64 CUs.

---

### 评论 #29 — hashuser1 (2018-09-14T20:48:06Z)

Ok, now we are getting somewhere. If I dont use AOCC and just follow the instructions listed in BUILD.md the selftest errors go away.

 clang -v
clang version 4.0 
Target: amdgcn--amdhsa
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64

./hashcat -b -m 11300
hashcat (v4.2.1-51-gc8dbcf9) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

OpenCL Platform #1: Advanced Micro Devices, Inc.
================================================
* Device #1: gfx803, 3481/4096 MB allocatable, 36MCU
* Device #2: gfx803, 3481/4096 MB allocatable, 36MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 11300 - Bitcoin/Litecoin wallet.dat (Iterations: 199999)

Speed.#1.........:     2558 H/s (72.62ms) @ Accel:128 Loops:32 Thr:256 Vec:1
Speed.#2.........:     2575 H/s (72.47ms) @ Accel:128 Loops:32 Thr:256 Vec:1
Speed.#*.........:     5133 H/s

Started: Fri Sep 14 13:40:49 2018
Stopped: Fri Sep 14 13:41:20 2018



---

### 评论 #30 — b-sumner (2018-09-14T20:48:18Z)

I used gcc 5.4.0 to build hashcat.

---

### 评论 #31 — hashuser1 (2018-09-14T21:36:44Z)

Ok, even though the self test is passing using GCC. Its still not finding the correct answer. I made 2 new wallets and encrypted them with passphrases that are included in example.txt. The wallets unlock using the core wallet with the same password. But still no success finding the hash using hashcat. Can you test the following hashes with the included example.txt?

[test.txt](https://github.com/RadeonOpenCompute/ROCm/files/2384962/test.txt)
[test2.txt](https://github.com/RadeonOpenCompute/ROCm/files/2384964/test2.txt)

[example.txt](https://github.com/RadeonOpenCompute/ROCm/files/2384966/example.txt)





---

### 评论 #32 — b-sumner (2018-09-14T22:34:53Z)

The fix may not have arrived in a released compiler (I'm using the tip which finds the answers in both cases).

You should be able to try the new compiler in the ROCM 1.9 release very soon.

---

### 评论 #33 — jlgreathouse (2018-09-14T22:35:42Z)

ROCm 1.9.0 was released a few minutes ago. :)

---

### 评论 #34 — jlgreathouse (2018-09-19T02:48:57Z)

I received an internal report that this was fixed with ROCm 1.9, so closing this issue.

---
