# Installing on Arch Linux

> **Issue #117**
> **状态**: closed
> **创建时间**: 2017-05-05T12:11:38Z
> **更新时间**: 2020-11-26T08:58:07Z
> **关闭时间**: 2017-07-02T17:14:25Z
> **作者**: almson
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/117

## 描述

Has anyone tried installing ROCm (both kernel and userspace) under Arch Linux? Or perhaps someone has had luck installing the kernel and running the userspace tools from an Ubuntu docker?

---

## 评论 (9 条)

### 评论 #1 — gstoner (2017-05-06T16:35:50Z)

No we have not tried Arch Linux

Greg
On May 5, 2017, at 7:11 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:


Has anyone tried installing ROCm (both kernel and userspace) under Arch Linux? Or perhaps someone has had luck installing the kernel and running the userspace tools from an Ubuntu docker?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/117>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuRyACug49pg9luNFepMd8m-1Ze_qks5r2xH7gaJpZM4NR1eB>.



---

### 评论 #2 — grmat (2017-05-10T21:00:34Z)

@almson have you tried building the kernel?
You can take [linux-git](https://aur.archlinux.org/packages/linux-git/) as a template and replace the source with the ROCK repo. Make sure you have amdgpu support for your device enabled in the config if it's a pre-VI GPU.

I have started creating `PKGBUILD`s for roct, rocr and hcc but those are neither complete nor tested.

I hope ROCK is going upstream soon so we won't have to downgrade the kernel by 3 releases at the first place before trying to play around with ROCm.

---

### 评论 #3 — almson (2017-05-12T07:44:18Z)

@grmat Thank you, I will try it. If you need help testing, I will gladly try your `PKGBUILD`s.

---

### 评论 #4 — grmat (2017-05-12T12:48:26Z)

@almson thanks for the offer. I'll get back to you when I make progress

---

### 评论 #5 — almson (2017-05-12T14:30:44Z)

To compile the kernel:

First, clone the `linux-git` repo and check out the commit for linux 4.9.0

    git clone https://aur.archlinux.org/linux-git.git linux-rocm
    cd linux-rocm
    git checkout 63b0d79

Then, edit PKGBUILD and rename `linux-git.preset` to `linux-rocm.preset`

    diff --git a/PKGBUILD b/PKGBUILD
    index ae5e7b0..c135a8f 100644
    --- a/PKGBUILD
    +++ b/PKGBUILD
    @@ -5,16 +5,16 @@
     # Contributor: misc <tastky@gmail.com>
     # Contributor: NextHendrix <cjones12 at sheffield.ac.uk>
 
    -pkgbase=linux-git
    -_srcname=linux
    -pkgver=4.9.r0.g69973b8
    +pkgbase=linux-rocm
    +_srcname=ROCK-Kernel-Driver
    +pkgver=roc.1.5.0.r0.g757f29e928f0
     pkgrel=1
     arch=('i686' 'x86_64')
     url="http://www.kernel.org/"
     license=('GPL2')
     makedepends=('xmlto' 'docbook-xsl' 'kmod' 'inetutils' 'bc' 'git' 'libelf')
     options=('!strip')
    -source=('git+https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git'
    +source=('git+https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver.git'
             # the main kernel config files
             'config' 'config.x86_64'
             # standard config files for mkinitcpio ramdisk
    diff --git a/linux-git.preset b/linux-rocm.preset
    similarity index 100%
    rename from linux-git.preset
    rename to linux-rocm.preset

Finally, makepkg

    makepkg -s

ROCm offers a docker that can be used to try out the userspace tools: https://github.com/RadeonOpenCompute/ROCm-docker

---

### 评论 #6 — acxz (2020-02-29T01:29:43Z)

I know this is a long time ago, but I just want to put this here in case others come across it. The ArchLinux community including me and some other folks have started picking up development on getting the ROCm stack working here: https://github.com/rocm-arch/rocm-arch. Feel free to submit PRs or issues!

---

### 评论 #7 — IndML101 (2020-09-27T11:32:00Z)

Hi,

I'm trying to install rocm on Manjaro (kerne 5.8.6), but it throws an error while installing rocsolver:

fatal error: error in backend: Cannot select: 0x555f6ea3b378: i64 = FrameIndex<0>
In function: _Z11bdsqrKernelI19rocblas_complex_numIdEdPS1_EviiiiPT0_lS4_lT1_iilS5_iilS5_iilPiiS3_S3_S3_S3_S4_l
clang-11: error: clang frontend command failed with exit code 70 (use -v to see invocation)
clang version 11.0.0 (https://aur.archlinux.org/llvm-amdgpu.git 38fffda570a017745da11c40ed8991c3c70a3281)
Target: x86_64-pc-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
clang-11: note: diagnostic msg: Error generating preprocessed source(s).
make[2]: *** [rocsolver/library/src/CMakeFiles/rocsolver.dir/build.make:342: rocsolver/library/src/CMakeFiles/rocsolver.dir/auxiliary/rocauxiliary_bdsqr.cpp.o] Error 70
make[2]: *** Waiting for unfinished jobs....
make[2]: Leaving directory '/home/gubberex/Downloads/rocsolver/src/build'
make[1]: *** [CMakeFiles/Makefile2:131: rocsolver/library/src/CMakeFiles/rocsolver.dir/all] Error 2
make[1]: Leaving directory '/home/gubberex/Downloads/rocsolver/src/build'
make: *** [Makefile:171: all] Error 2
make: Leaving directory '/home/gubberex/Downloads/rocsolver/src/build'
==> ERROR: A failure occurred in build().
    Aborting...



Any clues?

---

### 评论 #8 — etdecode (2020-11-25T20:15:08Z)

> 
> 
> Hi,
> 
> I'm trying to install rocm on Manjaro (kerne 5.8.6), but it throws an error while installing rocsolver:
> 
> fatal error: error in backend: Cannot select: 0x555f6ea3b378: i64 = FrameIndex<0>
> In function: _Z11bdsqrKernelI19rocblas_complex_numIdEdPS1_EviiiiPT0_lS4_lT1_iilS5_iilS5_iilPiiS3_S3_S3_S3_S4_l
> clang-11: error: clang frontend command failed with exit code 70 (use -v to see invocation)
> clang version 11.0.0 (https://aur.archlinux.org/llvm-amdgpu.git 38fffda570a017745da11c40ed8991c3c70a3281)
> Target: x86_64-pc-linux-gnu
> Thread model: posix
> InstalledDir: /opt/rocm/llvm/bin
> clang-11: note: diagnostic msg: Error generating preprocessed source(s).
> make[2]: *** [rocsolver/library/src/CMakeFiles/rocsolver.dir/build.make:342: rocsolver/library/src/CMakeFiles/rocsolver.dir/auxiliary/rocauxiliary_bdsqr.cpp.o] Error 70
> make[2]: *** Waiting for unfinished jobs....
> make[2]: Leaving directory '/home/gubberex/Downloads/rocsolver/src/build'
> make[1]: *** [CMakeFiles/Makefile2:131: rocsolver/library/src/CMakeFiles/rocsolver.dir/all] Error 2
> make[1]: Leaving directory '/home/gubberex/Downloads/rocsolver/src/build'
> make: *** [Makefile:171: all] Error 2
> make: Leaving directory '/home/gubberex/Downloads/rocsolver/src/build'
> ==> ERROR: A failure occurred in build().
> Aborting...
> 
> Any clues?

---
From my understanding, the kernel is not supported because the gcc compiler has to match with rocm package compiler.
I'm not sure you've shared the error actually.
Try changing kernel to 5.6 and check gcc version.

---

### 评论 #9 — ROCmSupport (2020-11-26T08:58:06Z)

As this ticket is already closed, recommend to open a new ticket for any new issues to get fast response.
Thank you.

---
