# FreeBSD support

> **Issue #1913**
> **状态**: open
> **创建时间**: 2023-03-01T11:59:20Z
> **更新时间**: 2025-10-16T16:53:58Z
> **作者**: thedaemon
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1913

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Since the last issue was closed and we were asked to open a new issue, is there any movement on FreeBSD support? I would love to be able to just use FreeBSD for my ROCm needs, instead of having to dual boot into Ubuntu. Is there something we the community can do to help in this task?

---

## 评论 (12 条)

### 评论 #1 — thedaemon (2023-03-08T22:26:54Z)

Also OpenBSD support while we are at it?

---

### 评论 #2 — CoryGH (2023-04-02T23:38:52Z)

Found this after seeing the closed issue https://github.com/RadeonOpenCompute/ROCm/issues/138 and hoping there was something active.  I'd like to see ROCm on FreeBSD for machine learning operations.

---

### 评论 #3 — elliejs (2023-11-20T17:51:58Z)

I've gotten a sizeable chunk of this to build, but without the kernel driver FreeBSD support still seems like more than a few patches to makefiles here and there. Adding another name to the pile requesting FreeBSD support.

---

### 评论 #4 — fsmv (2024-02-17T06:22:39Z)

Hi I will become a very loyal AMD GPU customer if this happens

---

### 评论 #5 — SimonAdameit (2025-01-02T15:12:06Z)

I'd love to see this happen.

---

### 评论 #6 — dchmelik (2025-05-09T07:47:41Z)

I'd love to see FreeBSD UNIX ROCm (and for any/all strictly UNIX[-like] (non-systemd, etc.) OS:  (Net|Free|DragonFly)BSD &  OpenSolaris/Illumos (Tribblix, OmniOS CE) UNIXes, Slackware GNU/Linux.  ROCm builds on some non-systemd GNU/Linuxes). My only AMDGPU-pro option had been (in 2010s) OS I questioned were worth extreme hassle they deviate from UNIX philosophy, just for newer Radeon. Of course, my first choices are FreeBSD & Slackware (equally #&#8203;1 best computer programming/science OS) but eventually, Unix[-like] variety would be best.

---

### 评论 #7 — selroc (2025-05-09T08:31:23Z)

> I'd love to see FreeBSD UNIX ROCm (and for any/all strictly UNIX[-like] (non-systemd, etc.) OS: (Net|Free|DragonFly)BSD & OpenSolaris/Illumos (Tribblix, OmniOS CE) UNIXes, Slackware GNU/Linux. ROCm builds on some non-systemd GNU/Linuxes). My only AMDGPU-pro option had been (in 2010s) OS I questioned were worth extreme hassle they deviate from UNIX philosophy, just for newer Radeon. Of course, my first choices are FreeBSD & Slackware (equally #​1 best computer programming/science OS) but eventually, Unix[-like] variety would be best.

They had an heartache when I asked them to support Debian (which is Ubuntu's mother) ... I imagine the time it would take to support FreeBSD...


---

### 评论 #8 — dchmelik (2025-05-09T12:17:55Z)

> They had an heartache when I asked them to support Debian (which is Ubuntu's mother) ... I imagine the time it would take to support FreeBSD...

Some (Nvidia/CUDA, etc.) find it easier to add UNIX (*BSD/(Open)Solaris, etc.) than newer specific GNU/Linux packages.
        On your topic (I suggest make ticket) If I gave honest opinion on lack of official Devuan/Debian ROCm, I'd be banned, but let's be clear; makes little/no sense to say '"support" software': only people/users & fellow computer programmers need support... scientists/engineers/programmers/technologists using new/odd definition (slang according to some) could seem a bit strange (so am I other ways) such as possibly too orientated toward technology while not enough towards people, which was uncommon when I was in high school, but this sort of focus (due to neurodiversity) is common now in (especially computer) science/engineering.
        ROCm's decision isn't sensible; it'd take insignificant effort to add Devuan/Debian: already works fine on original (non-systemd) and all (normal) derivatives (Debian, *Ubuntu) basically perfectly except rarely a problem on current/development/testing unofficial *Ubuntu versions/forks (KDE Neon, etc.).  Once ROCm is for Debian, ROCm gets potentially many much higher  experts (long-time Debian programmers, not largely *Ubuntu users) bug-reporting to help all variants including similar *Ubuntu.  I don't get what's holding ROCm (and as result, Radeon, AMD overall) back; they'd have to type no more than seven characters in amdgpu-install (or whatever equivalent) (or accept patch known for years) and then say you're welcome to use/test/bug-report on Debian but can't guarantee newer amdgpu-install works on Debian at least before relevant updates (if at all)... simple as that.  On users' Devuan PCs I administer, I have to use previous Ubuntu amdgpu-install a while, but so what?  Devuan (and most Debian) people generally don't mind working that out and checking when that updates.

---

### 评论 #9 — selroc (2025-05-09T13:52:54Z)

> > They had an heartache when I asked them to support Debian (which is Ubuntu's mother) ... I imagine the time it would take to support FreeBSD...
> 
> Some (Nvidia/CUDA, etc.) find it easier to add UNIX (*BSD/(Open)Solaris, etc.) than newer specific GNU/Linux packages.         On your topic (I suggest make ticket) If I gave honest opinion on lack of official Devuan/Debian ROCm, I'd be banned, but let's be clear; makes little/no sense to say '"support" software': only people/users & fellow computer programmers need support... scientists/engineers/programmers/technologists using new/odd definition (slang according to some) could seem a bit strange (so am I other ways) such as possibly too orientated toward technology while not enough towards people, which was uncommon when I was in high school, but this sort of focus (due to neurodiversity) is common now in (especially computer) science/engineering.         ROCm's decision isn't sensible; it'd take insignificant effort to add Devuan/Debian: already works fine on original (non-systemd) and all (normal) derivatives (Debian, *Ubuntu) basically perfectly except rarely a problem on current/development/testing unofficial *Ubuntu versions/forks (KDE Neon, etc.). Once ROCm is for Debian, ROCm gets potentially many much higher experts (long-time Debian programmers, not largely *Ubuntu users) bug-reporting to help all variants including similar *Ubuntu. I don't get what's holding ROCm (and as result, Radeon, AMD overall) back; they'd have to type no more than seven characters in amdgpu-install (or whatever equivalent) (or accept patch known for years) and then say you're welcome to use/test/bug-report on Debian but can't guarantee newer amdgpu-install works on Debian at least before relevant updates (if at all)... simple as that. On users' Devuan PCs I administer, I have to use previous Ubuntu amdgpu-install a while, but so what? Devuan (and most Debian) people generally don't mind working that out and checking when that updates.

It just took a couple of years before they started looking at Debian as a supported platform.

---

### 评论 #10 — laffer1 (2025-06-08T16:49:18Z)

I'd also like to see *BSD support for rocm.  If it was working on FreeBSD, I could probably port it to MidnightBSD.

---

### 评论 #11 — vedranmiletic (2025-09-04T08:50:57Z)

Did anybody actually explore what is not working on FreeBSD and what source changes would be required to support it?

---

### 评论 #12 — denzuko (2025-10-16T16:47:25Z)

> Did anybody actually explore what is not working on FreeBSD and what source changes would be required to support it?

Seems [elliejs](https://github.com/elliejs) did, and its just the kernel module from what I'm reading in https://github.com/ROCm/ROCm/issues/1913#issuecomment-1819542789. 

While we're on that subject it also seems we wouldn't have basic support for the rx 7000 series [RDNA3] until December 2025 (FreeBSD 15-Release), https://forums.freebsd.org/threads/amd-radeon-7900xtx-unsupported.92057/post-689437 which I believe is a base line for ROCm.

---
