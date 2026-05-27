# supporting other distributions

> **Issue #28**
> **状态**: closed
> **创建时间**: 2016-08-31T17:49:55Z
> **更新时间**: 2017-10-23T09:28:07Z
> **关闭时间**: 2016-09-06T21:49:31Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/28

## 描述

Hi - I wanted to inquire on the availability of packages for other distributions - from RHEL/SLES to desktops such as OpenSUSE.

I understand this project on the whole is FOSS, but it is a big /complex toolchain and seemingly the FOSS path is unused (take #27 as a kernel of truth towards this ).  Ubuntu is a good start but there needs to be some builds available for other distributions.  It would probably operate best if using the upstream build systems, such as Novell/SuSE's Open Build System (OBS), whether you still host a local repository (like for Ubuntu) or use build.opensuse.org for hosting.  Fedora has something similar as does really many distros - however I know several projects/corporation have used OBS, such as Intel Tizen... it also supports building against many other distros, if that's of interest.   My main point is though that support should be increased in a manner similar to ZFSonLinux.

Surely you have more resources than a LLNL project porting an existing software? :-)


---

## 评论 (6 条)

### 评论 #1 — gstoner (2016-08-31T18:43:07Z)

So the limited repo support to date was about Engineering team focus bring up rich set of capabilities and not just spending our time porting them to new Distros. Remember  release 1.0 was this last April.   If you look we had large number new capabilities we need to develop even in each subsequent release since version 1.0.     To do this we need to be near the Tip of Tree Linux Kernel to get key feature supported for the class of hardware and some of the capabilities we needed.    Because of this we started with  two foundation Debian Ubuntu and RPM - Fedora, the latter to help our effort to bring up REHL in the future.  These are the two roots that fead large number of distributions.

One thing our KFD has only supported with 4.x Linux Kernel since it first public release, we upstream number of the bit over the last two year.   Currently we are leveraging 4.4 Linux Kernel for ROCm 1.2, to support  REHL/CENTOS 7.2 on X86  ( turns out ARM AArch64 is already 4.x Linux kernel) we have to back port to 3.10.0-327.  Right now we looking at REHL7.3/7.4 for ROCm Support.    One thing we doing in ROCm 1.2 is re-architect the Kernel driver to simplify our porting effort with  REHL and latter SuSE is much older Linux Kernel.   There is work underway by the OpenSuSE community to bring ROCm over which uses more modern Linux Kernel.  Also we are seeing community bringing ROCm to Gentoo and FreeBSD.

One thing with 1.3  we will have completed our promise to be fully open source,  we will be dropping the HSAIL Finalizer/SC compiler and moving exclusively to LLVM to GCN ISA Compiler for all tool chains.   This has Assembler in it which  will be used for compiling the trap handler. For ROCm 1.2 we compiled them with this path.

On the OBS system they are great when you have code that only runs on CPU since you can do continuous integration and testing.  They fall apart when a GPU comes into the picture.  Since they have virtualized environment sans GPU’s.  It is some thing we talking to number of the groups about.

The stack is also being ported to non-x86 Processors,  more info to come.

We are still a small team, but maybe not as small as the LLNL group.

Greg

On Aug 31, 2016, at 12:49 PM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

Hi - I wanted to inquire on the availability of packages for other distributions - from RHEL/SLES to desktops such as OpenSUSE.

I understand this project on the whole is FOSS, but it is a big /complex toolchain and seemingly the FOSS path is unused (take #27https://github.com/RadeonOpenCompute/ROCm/issues/27 as a kernel of truth towards this ). Ubuntu is a good start but there needs to be some builds available for other distributions. It would probably operate best if using the upstream build systems, such as Novell/SuSE's Open Build System (OBS), whether you still host a local repository (like for Ubuntu) or use build.opensuse.orghttp://build.opensuse.org for hosting. Fedora has something similar as does really many distros - however I know several projects/corporation have used OBS, such as Intel Tizen... it also supports building against many other distros, if that's of interest. My main point is though that support should be increased in a manner similar to ZFSonLinux.

Surely you have more more resources than a LLNL project porting an existing software? :-)

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/28, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuSZrKMvxJnB6hFMKdxnP0Xs9QYC0ks5qlb7EgaJpZM4Jx4b7.


---

### 评论 #2 — nevion (2016-08-31T19:39:28Z)

@gstoner Thanks for your great reply!

I understand you need access to latest stable stuff, this is actually what drives my choice in SUSE as a distro because of it's usually stable "official" repo overlays, like Kernel:Stable - which your OBS project for instance would build against.  Further, most of the features you need sound like most of all the upcoming distro releases will have (unless you have new ones requiring latest again).  Gentoo is no surprise, they've long had expertise at making an ebuild to do something like this (FreeBSD is a surprise, though).

I tried searching on SUSE efforts but I didn't find anything, I might be able to get something started if you had a public fedora repo somewhre you can point me to - I've maintained a number of low key repos over the years that would probably help jumpstart inclusion in upstream.  Do you know who is working on the SUSE effort, btw?  It would be good to collaborate with them too.

As for the initial target (to not get drawn down in distro details) and timing, I think it's appropriate to make this an issue to contend with now, because you've hit that _huge_ milestone already and incrementally dealing with the assembler in 1.3.

Also, I understand what you mean for the most part with current CI systems being virtual machines and not being able to put up with GPU testing, but I'm not sure how that affects the building of software that OBS normally supplies.  I haven't used the CI stuff they've been coming out (OpenQA), which is a related but separate effort.


---

### 评论 #3 — nevion (2016-09-06T22:01:23Z)

@gstoner actually can you reopen this and make available the build scripts you guys used to generate the repository you have?

I'll host and eventually get it in my own upstream distro and will help answer why I had #29 


---

### 评论 #4 — nevion (2016-09-08T23:48:50Z)

@gstoner or @arodrigx7  @jedwards-AMD bump? 


---

### 评论 #5 — nevion (2017-04-03T01:04:01Z)

@gstoner @jedwards-AMD can you give a summary of where RHEL 7 support is at and where it's going?  I've been spreading the word about ROCm - I know several interested parties in ROCm, but it's important that it supports the enterprise distros.  Also interested in hearing updates for [open]SUSE.

---

### 评论 #6 — preda (2017-10-23T09:28:07Z)

I would also be interested in instructions for building from source (that I need for Ubuntu 17.10).

---
