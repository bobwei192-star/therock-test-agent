# ROCm-1.3 problem

> **Issue #46**
> **状态**: closed
> **创建时间**: 2016-11-12T04:40:09Z
> **更新时间**: 2017-01-03T19:18:37Z
> **关闭时间**: 2017-01-03T19:18:37Z
> **作者**: briansp2020
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/46

## 描述

Hi,
I just installed ROCm-1.3 and am having problems. Even simple examples (vector_copy) no longer work. dmesg shows

> [  834.418133] amdkfd: PeerDirect interface was not detected
[  843.452878] kfd: qcm fence wait loop timeout expired
[  843.452880] kfd: unmapping queues failed.
[  843.452881] kfd: the cp might be in an unrecoverable state due to an unsuccessful queues preemption
[  852.457134] kfd: qcm fence wait loop timeout expired
[  852.457136] kfd: unmapping queues failed.
[  852.457137] kfd: the cp might be in an unrecoverable state due to an unsuccessful queues preemption
[  852.457139] amdkfd: Resetting wave fronts on dev ffff88043c0db000

My set up is i7-6700 ASUS Z170M-E D3 + 2 Fury Nano. I did not have any issue when I was using ROCm-1.2.

I upgraded from ROCm-1.2 set up. Maybe that caused some issue? When I tried 
> sudo apt-get upgrade

It said the packages were held back. So, I did
> sudo apt-get install rocm

and it upgraded. After ward, I did
> sudo apt-get autoremove

to remove packages that apt-get said no longer needed.

Any ideas?

---

## 评论 (25 条)

### 评论 #1 — briansp2020 (2016-11-12T05:06:58Z)

I uninstalled all the packages and installed again and now it works.


---

### 评论 #2 — briansp2020 (2016-11-12T05:11:34Z)

Actually, not quite.
After rebooting, vector_copy works.
However, HIP/samples/0_Intro/bit_extract hang. Once it hangs, subsequently trying to run vector_copy also fails with the following error.

> Initializing the hsa runtime failed.


---

### 评论 #3 — briansp2020 (2016-11-13T14:45:33Z)

Has anyone been able to duplicate this problem?
Would I have a better luck if I try Ubuntu 14.04? At the moment, It seems that's the version most developers are running. I can't run any GPU code other than the simple vector copy sample...


---

### 评论 #4 — gstoner (2016-11-13T16:30:29Z)

On Ubuntu 16.04,with you will bump into this issue and it's a bug in ubuntu:

http://stackoverflow.com/questions/37096062/get-a-basic-c-program-to-compile-using-clang-on-ubuntu-16

On Nov 13, 2016, at 8:45 AM, Brian <notifications@github.com<mailto:notifications@github.com>> wrote:

Has anyone been able to duplicate this problem?
Would I have a better luck if I try Ubuntu 14.04? At the moment, It seems that's the version most developers are running. I can't run any GPU code other than the simple vector copy sample...

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/46#issuecomment-260190409, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuaNkFnbb5NHZMr3kjORXRFJg2ADPks5q9yKNgaJpZM4KwUz1.


---

### 评论 #5 — briansp2020 (2016-11-13T21:15:40Z)

I just installed 14.04.5 and ROCm and I still see both this problem & the linker problem. It does not look like these problems I'm experiencing is related to Ubuntu version.

> briansp@FijiX2:~$ lsb_release -a
> No LSB modules are available.
> Distributor ID: Ubuntu
> Description:    Ubuntu 14.04.5 LTS
> Release:    14.04
> Codename:   trusty
> briansp@FijiX2:~$ cd git/
> briansp@FijiX2:~/git$ git clone https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP
> Cloning into 'HIP'...
> remote: Counting objects: 9140, done.
> remote: Compressing objects: 100% (236/236), done.
> remote: Total 9140 (delta 148), reused 0 (delta 0), pack-reused 8897
> Receiving objects: 100% (9140/9140), 3.70 MiB | 4.09 MiB/s, done.
> Resolving deltas: 100% (6299/6299), done.
> Checking connectivity... done.
> briansp@FijiX2:~/git$ cd HIP/
> briansp@FijiX2:~/git/HIP$ ls
> bin             CONTRIBUTING.md  include     packaging   samples  util
> cmake           docs             INSTALL.md  README.md   src
> CMakeLists.txt  hipify-clang     LICENSE     RELEASE.md  tests
> briansp@FijiX2:~/git/HIP$ cd samples/
> briansp@FijiX2:~/git/HIP/samples$ ls
> 0_Intro  1_Utils  2_Cookbook  7_Advanced
> briansp@FijiX2:~/git/HIP/samples$ cd 0_Intro/
> briansp@FijiX2:~/git/HIP/samples/0_Intro$ ls
> bit_extract  hcc_dialects  module_api  square
> briansp@FijiX2:~/git/HIP/samples/0_Intro$ cd bit_extract/
> briansp@FijiX2:~/git/HIP/samples/0_Intro/bit_extract$ make
> /opt/rocm/hip/bin/hipcc -stdlib=libc++ bit_extract.cpp -o bit_extract
> briansp@FijiX2:~/git/HIP/samples/0_Intro/bit_extract$ ./bit_extract 


---

### 评论 #6 — gstoner (2016-11-13T23:03:07Z)

What are your system details

Get Outlook for iOShttps://aka.ms/o0ukef

On Sun, Nov 13, 2016 at 2:15 PM -0700, "Brian" <notifications@github.com<mailto:notifications@github.com>> wrote:

I just installed 14.04.5 and ROCm and I still see both this problem & the linker problem. It does not look like these problems I'm experiencing is related to Ubuntu version.

briansp@FijiX2:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 14.04.5 LTS
Release: 14.04
Codename: trusty
briansp@FijiX2:~$ cd git/
briansp@FijiX2:~/git$ git clone https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP
Cloning into 'HIP'...
remote: Counting objects: 9140, done.
remote: Compressing objects: 100% (236/236), done.
remote: Total 9140 (delta 148), reused 0 (delta 0), pack-reused 8897
Receiving objects: 100% (9140/9140), 3.70 MiB | 4.09 MiB/s, done.
Resolving deltas: 100% (6299/6299), done.
Checking connectivity... done.
briansp@FijiX2:~/git$ cd HIP/
briansp@FijiX2:~/git/HIP$ ls
bin CONTRIBUTING.md include packaging samples util
cmake docs INSTALL.md README.md src
CMakeLists.txt hipify-clang LICENSE RELEASE.md tests
briansp@FijiX2:~/git/HIP$ cd samples/
briansp@FijiX2:~/git/HIP/samples$ ls
0_Intro 1_Utils 2_Cookbook 7_Advanced
briansp@FijiX2:~/git/HIP/samples$ cd 0_Intro/
briansp@FijiX2:~/git/HIP/samples/0_Intro$ ls
bit_extract hcc_dialects module_api square
briansp@FijiX2:~/git/HIP/samples/0_Intro$ cd bit_extract/
briansp@FijiX2:~/git/HIP/samples/0_Intro/bit_extract$ make
/opt/rocm/hip/bin/hipcc -stdlib=libc++ bit_extract.cpp -o bit_extract
briansp@FijiX2:~/git/HIP/samples/0_Intro/bit_extract$ ./bit_extract

## 

You are receiving this because you commented.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/46#issuecomment-260213439, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuddrVNgBeZRubBOXZmQ6-Nb4VHfRks5q9339gaJpZM4KwUz1.


---

### 评论 #7 — briansp2020 (2016-11-13T23:54:52Z)

My set up is i7-6700 ASUS Z170M-E D3 + 2 Fury Nano. BIOS 2001.
Samsung 950 NVMe SSD. 16GB Mem.


---

### 评论 #8 — jedwards-AMD (2016-11-15T18:04:31Z)

Hi Brian,

From your description you have 2 cards, both Fury Nano's. What slots are these installed in? From what I understand there is 1 x16 slot (the grey slot) and 2 x4 slots (the black slots) on a ASUS Z170M-E motherboard.


---

### 评论 #9 — briansp2020 (2016-11-15T18:12:47Z)

The board is a mATX and only has 2 x16 connector. One is x16 electrically (one closes to the CPU) and the other (farthest from CPU)  is x4 electrically.
https://www.asus.com/us/Motherboards/Z170M-E-D3/
Are you looking at some other board?


---

### 评论 #10 — jedwards-AMD (2016-11-15T18:48:51Z)

I was looking at another board, but this is good information. From your output it appears that sample is hanging before it even finds a device. Could you remove the card on the x4 slot an see if you can reproduce the error. If it fails, please send the stack trace of the sample (build the sample in debug by adding -g to the HIPCC_FLAGS line).


---

### 评论 #11 — briansp2020 (2016-11-15T19:17:52Z)

I have both Fiji on a water block with a plastic header. So, it won't be easy to remove just 1. When I go home, I'll get the stack trace with both card in the machine. Hopefully, that will give you some clues.

Thanks for your help.


---

### 评论 #12 — briansp2020 (2016-11-16T04:08:38Z)

I built it with -g and ran it with gdb.

> briansp@FijiX2:~/git/HIP/samples/0_Intro/bit_extract$ gdb bit_extract
> GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
> Copyright (C) 2014 Free Software Foundation, Inc.
> License GPLv3+: GNU GPL version 3 or later http://gnu.org/licenses/gpl.html
> This is free software: you are free to change and redistribute it.
> There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
> and "show warranty" for details.
> This GDB was configured as "x86_64-linux-gnu".
> Type "show configuration" for configuration details.
> For bug reporting instructions, please see:
> http://www.gnu.org/software/gdb/bugs/.
> Find the GDB manual and other documentation resources online at:
> http://www.gnu.org/software/gdb/documentation/.
> For help, type "help".
> Type "apropos word" to search for commands related to "word"...
> Reading symbols from bit_extract...done.
> (gdb) r
> Starting program: /home/briansp/git/HIP/samples/0_Intro/bit_extract/bit_extract 
> [Thread debugging using libthread_db enabled]
> Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
> [New Thread 0x7ffff4878700 (LWP 3209)]
> 
> ### HCC STATUS_CHECK Error: HSA_STATUS_ERROR_OUT_OF_RESOURCES (0x1008) at file:/home/scchan/code/github/radeonopencompute/hcc.1.3/hcc/lib/hsa/mcwamp_hsa.cpp line:2721
> 
> Program received signal SIGABRT, Aborted.
> 0x00007ffff6289c37 in __GI_raise (sig=sig@entry=6)
>     at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
> 56  ../nptl/sysdeps/unix/sysv/linux/raise.c: No such file or directory.
> (gdb) stack
> Undefined command: "stack".  Try "help".
> (gdb) list
> 51  in ../nptl/sysdeps/unix/sysv/linux/raise.c
> (gdb) backtrace
> #0  0x00007ffff6289c37 in __GI_raise (sig=sig@entry=6)
>     at ../nptl/sysdeps/unix/sysv/linux/raise.c:56
> #1  0x00007ffff628d028 in __GI_abort () at abort.c:89
> #2  0x00007ffff4889e41 in Kalmar::HSAContext::HSAContext() ()
>    from /opt/rocm/hcc/lib/libmcwamp_hsa.so
> #3  0x00007ffff4888608 in _GLOBAL__sub_I_mcwamp_hsa.cpp ()
>    from /opt/rocm/hcc/lib/libmcwamp_hsa.so
> #4  0x00007ffff7dea10a in call_init (l=<optimized out>, argc=argc@entry=1, 
>     argv=argv@entry=0x7fffffffdf98, env=env@entry=0x7fffffffdfa8)
>     at dl-init.c:78
> #5  0x00007ffff7dea1f3 in call_init (env=<optimized out>, 
>     argv=<optimized out>, argc=<optimized out>, l=<optimized out>)
>     at dl-init.c:36
> #6  _dl_init (main_map=main_map@entry=0xac7b10, argc=1, argv=0x7fffffffdf98, 
>     env=0x7fffffffdfa8) at dl-init.c:126
> #7  0x00007ffff7deec30 in dl_open_worker (a=a@entry=0x7fffffffda08)
>     at dl-open.c:577
> #8  0x00007ffff7de9fc4 in _dl_catch_error (
>     objname=objname@entry=0x7fffffffd9f8, 
>     errstring=errstring@entry=0x7fffffffda00, 
>     mallocedp=mallocedp@entry=0x7fffffffd9f0, 
>     operate=operate@entry=0x7ffff7dee960 <dl_open_worker>, 
>     args=args@entry=0x7fffffffda08) at dl-error.c:187
> #9  0x00007ffff7dee37b in _dl_open (file=0x7fffffffdcf9 "libmcwamp_hsa.so", 
>     mode=-2147479551, caller_dlopen=<optimized out>, nsid=-2, argc=1, 
>     argv=0x7fffffffdf98, env=0x7fffffffdfa8) at dl-open.c:661
> #10 0x00007ffff78e502b in dlopen_doit (a=a@entry=0x7fffffffdc20) at dlopen.c:66
> #11 0x00007ffff7de9fc4 in _dl_catch_error (objname=0xac7550, 
>     errstring=0xac7558, mallocedp=0xac7548, 
>     operate=0x7ffff78e4fd0 <dlopen_doit>, args=0x7fffffffdc20)
>     at dl-error.c:187
> #12 0x00007ffff78e562d in _dlerror_run (
>     operate=operate@entry=0x7ffff78e4fd0 <dlopen_doit>, 
>     args=args@entry=0x7fffffffdc20) at dlerror.c:163
> #13 0x00007ffff78e50c1 in __dlopen (file=<optimized out>, mode=<optimized out>)
>     at dlopen.c:87
> #14 0x0000000000409b29 in Kalmar::CLAMP::PlatformDetect::detect() ()
> #15 0x0000000000407631 in Kalmar::CLAMP::GetOrInitRuntime() ()
> #16 0x0000000000408c8a in Kalmar::KalmarBootstrap::KalmarBootstrap() ()
> #17 0x00000000004082d7 in __hcc_shared_library_init ()
> #18 0x0000000000468bed in __libc_csu_init ()
> ---Type <return> to continue, or q <return> to quit---
> #19 0x00007ffff6274ed5 in __libc_start_main (
>     main=0x468050 <main(int, char**)>, argc=1, argv=0x7fffffffdf98, 
>     init=0x468ba0 <__libc_csu_init>, fini=<optimized out>, 
>     rtld_fini=<optimized out>, stack_end=0x7fffffffdf88) at libc-start.c:246
> #20 0x0000000000467f72 in _start ()

Is this what you meant?


---

### 评论 #13 — jedwards-AMD (2016-11-16T16:19:04Z)

This error indicates that the HSA runtime couldn't be initialized correctly. This seems to be different than a hang; if this happens the application would abort. In other words, if vector_copy is working, this error shouldn't occur.

Can you post the output of the vector_copy sample? Also, I would like to see the output of the following command 'lspci -vvvv -d 0x1002:0x7300'.


---

### 评论 #14 — briansp2020 (2016-11-16T23:51:31Z)

I forgot to mention that I'm using UEFI BIOS for the Fiji https://community.amd.com/community/gaming/blog/2016/04/05/radeon-r9-fury-nano-uefi-firmware

I don't know whether that matters or not. I'll run lspci & vector_copy and post when I get home.


---

### 评论 #15 — briansp2020 (2016-11-17T04:23:29Z)

lspci output.

> briansp@FijiX2:~/dev$ lspci -vvvv -d 0x1002:0x7300
> 01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series](rev ca) (prog-if 00 [VGA controller])
>     Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Radeon R9 FURY X / NANO
>     Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
>     Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ >SERR- <PERR- INTx-
>     Latency: 0
>     Interrupt: pin A routed to IRQ 135
>     Region 0: Memory at e0000000 (64-bit, prefetchable) [size=256M]
>     Region 2: Memory at f0000000 (64-bit, prefetchable) [size=2M]
>     Region 4: I/O ports at e000 [size=256]
>     Region 5: Memory at f7e00000 (32-bit, non-prefetchable) [size=256K]
>     Expansion ROM at f7e40000 [disabled] [size=128K]
>     Capabilities: <access denied>
>     Kernel driver in use: amdgpu
> 
> 07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series](rev ca) (prog-if 00 [VGA controller])
>     Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Radeon R9 FURY X / NANO
>     Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
>     Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
>     Latency: 0
>     Interrupt: pin A routed to IRQ 137
>     Region 0: Memory at c0000000 (64-bit, prefetchable) [size=256M]
>     Region 2: Memory at d0000000 (64-bit, prefetchable) [size=2M]
>     Region 4: I/O ports at c000 [size=256]
>     Region 5: Memory at f7c00000 (32-bit, non-prefetchable) [size=256K]
>     Expansion ROM at f7c40000 [disabled] [size=128K]
>     Capabilities: <access denied>
>     Kernel driver in use: amdgpu


---

### 评论 #16 — briansp2020 (2016-11-17T04:24:50Z)

vector_copy output

> briansp@FijiX2:~/dev/sample$ ./vector_copy 
> Initializing the hsa runtime succeeded.
> Checking finalizer 1.0 extension support succeeded.
> Generating function table for finalizer succeeded.
> Getting a gpu agent succeeded.
> Querying the agent name succeeded.
> The agent name is gfx803.
> Querying the agent maximum queue size succeeded.
> The maximum queue size is 131072.
> Creating the queue succeeded.
> "Obtaining machine model" succeeded.
> "Getting agent profile" succeeded.
> Create the program succeeded.
> Adding the brig module to the program succeeded.
> Query the agents isa succeeded.
> Finalizing the program succeeded.
> Destroying the program succeeded.
> Create the executable succeeded.
> Loading the code object succeeded.
> Freeze the executable succeeded.
> Extract the symbol from the executable succeeded.
> Extracting the symbol from the executable succeeded.
> Extracting the kernarg segment size from the executable succeeded.
> Extracting the group segment size from the executable succeeded.
> Extracting the private segment from the executable succeeded.
> Creating a HSA signal succeeded.
> Finding a fine grained memory region succeeded.
> Allocating argument memory for input parameter succeeded.
> Allocating argument memory for output parameter succeeded.
> Finding a kernarg memory region succeeded.
> Allocating kernel argument memory buffer succeeded.
> Dispatching the kernel succeeded.
> Passed validation.
> Freeing kernel argument memory buffer succeeded.
> Destroying the signal succeeded.
> Destroying the executable succeeded.
> Destroying the code object succeeded.
> Destroying the queue succeeded.
> Freeing in argument memory buffer succeeded.
> Freeing out argument memory buffer succeeded.
> Shutting down the runtime succeeded.


---

### 评论 #17 — briansp2020 (2016-11-17T04:29:39Z)

I ran bit_extract again and this time, it hung. I hit ctrl-c and got the following output.

> briansp@FijiX2:~/git/HIP/samples/0_Intro/bit_extract$ gdb bit_extract 
> GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.2) 7.7.1
> Copyright (C) 2014 Free Software Foundation, Inc.
> License GPLv3+: GNU GPL version 3 or later http://gnu.org/licenses/gpl.html
> This is free software: you are free to change and redistribute it.
> There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
> and "show warranty" for details.
> This GDB was configured as "x86_64-linux-gnu".
> Type "show configuration" for configuration details.
> For bug reporting instructions, please see:
> http://www.gnu.org/software/gdb/bugs/.
> Find the GDB manual and other documentation resources online at:
> http://www.gnu.org/software/gdb/documentation/.
> For help, type "help".
> Type "apropos word" to search for commands related to "word"...
> Reading symbols from bit_extract...done.
> (gdb) r
> Starting program: /home/briansp/git/HIP/samples/0_Intro/bit_extract/bit_extract 
> [Thread debugging using libthread_db enabled]
> Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
> [New Thread 0x7ffff4878700 (LWP 2631)]
> ^C
> Program received signal SIGINT, Interrupt.
> 0x00007ffff631e2a7 in sched_yield () at ../sysdeps/unix/syscall-template.S:81
> 81  ../sysdeps/unix/syscall-template.S: No such file or directory.
> (gdb) 


---

### 评论 #18 — briansp2020 (2016-11-22T01:19:11Z)

@jedwards-AMD
Did the information I provided, help at all? Are you still looking into this?


---

### 评论 #19 — jedwards-AMD (2016-11-29T16:54:38Z)

Hi Brian,

Sorry for the late response. Several of our team members were out last week for the Thanksgiving holidays. We are still looking into the situation and we think we have a solution. I will update you soon.

---

### 评论 #20 — briansp2020 (2016-11-29T18:45:08Z)

@jedwards-AMD
It sounds like you found the cause of the issue. Can you tell me what the cause is and/or a workaround, if there is any? Does this mean that I'll still have the same issue with 1.3.1?

Thanks!

---

### 评论 #21 — jedwards-AMD (2016-11-30T17:24:53Z)

Unfortunately the issue is most likely with the capabilities of the x4 PCIe slot the second card is inserted in. To verify this is the case I need you to attach the output of the following commands to the post:
.
sudo lspci -xxxx &> pciedumphex.txt
sudo lspci -vvvv &> pciedump.txt
sudo lspci -t &> pcietopo.txt
.
I am going to have to cross reference these two files to make sure that slot supports the necessary PCIe 3.0 capabilities to support ROCm.


---

### 评论 #22 — briansp2020 (2016-12-01T03:38:55Z)

pciedumphex.txt : https://gist.github.com/briansp2020/40489677ca4dd47f49de9a151616e233
pciedump.txt : https://gist.github.com/briansp2020/72b7f9954c181a70783c67593bf2e313
pcietopo.txt : https://gist.github.com/briansp2020/5c22d491ba21016675f68fa5deca12e8

ROCm 1.2 worked. So, I'm not sure why 1.3 is having this issue if it was a hardware problem. Also, if I don't provide any parameter, shouldn't the runtime pick the first GPU in x16 slot?

---

### 评论 #23 — jedwards-AMD (2016-12-01T05:18:19Z)

It appears that your second device is on a PCI Bridge (00:1c.4) that doesn't support atomic operations. This is probably the cause of the hang for the HIP sample (bit_extract). It is possible that the HIP sample or the HCC runtime changed to include both devices; this would explain the different behavior between the 1.2 and 1.3 releases. I will follow up on that, but removing the card from the 00:1c.4 PCI bridge should fix the issue for now.

---

### 评论 #24 — vpa1977 (2016-12-16T13:35:27Z)

Maybe it is something similiar, but I have a problem with A8-7600 + R390 setup. 
After installing clean Ubuntu 16.04 and rocm 1.3 from debian repository and rebooting the screen goes white and system hangs.

---

### 评论 #25 — jedwards-AMD (2016-12-16T17:04:13Z)

This configuration is not supported by ROCm. The A8-7600 doesn't support PCIe atomic operations and I doubt your mother board has a x16 PCIe 3.0 port for the video card. Further, the AMD Radeon R9 390 is not on the list of ROCm supported video cards.

---
