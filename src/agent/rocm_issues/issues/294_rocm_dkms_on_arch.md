# rocm dkms on arch

> **Issue #294**
> **状态**: closed
> **创建时间**: 2018-01-02T00:55:14Z
> **更新时间**: 2021-01-05T10:02:03Z
> **关闭时间**: 2021-01-05T09:47:23Z
> **作者**: ghost
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/294

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Dear ROCm Team.

I am trying creating a aur PKG on arch for ROCm. As your work is really great, the arch community should benefit from it. For a good start i took the dkms package you are providing for ubuntu.
http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-utils/rocm-utils_1.7.60_amd64.deb

As i understood the dependecies are small it should be doable easy? All includes files are in the package allready, no crossdeps so far. 

So i extracted the sources and brought em /usr/share and /usr/src. 

dkms add -m rock -v 1.7.60

worked and dkms is linking the dkms conf and sources right. 
Stupid as i am the next i tried just build it, which obviously failed :) - (dkms autoinstall)

the dmks buildlog is here https://pastebin.com/UuNRsEXQ
It looks like some vars arent defined. Where is it done in your package so i can adjust it for arch.

Maybe one of the more expirienced ones here can point me into the right direction?

Cheers
derdigge

PS: sorry for my bad english


---

## 评论 (23 条)

### 评论 #1 — Narthorn (2018-01-14T09:14:00Z)

You need to add arch as a build target in the Makefile, as in https://aur.archlinux.org/cgit/aur.git/tree/0003-add-archlinux-as-build-option.patch?h=amdgpu-pro-installer&id=ede737884af35e3fe5be94e8864a336a14839de4.

Unfortunately, that's not enough, as the rock-dkms package is only meant to compile against kernel versions up to 4.13, while arch uses 4.14 (soon 4.15). The package probably needs to be patched by the ROCm team or someone knowledgeable to make it build properly against 4.14 and 4.15.

It should build fine against linux-lts (4.9), though, if that's what you're going for.
Edit: Spoke too soon! It does build fine, but fails to load unless the kernel is built with CONFIG_KALLSYMS_ALL=y.

---

### 评论 #2 — Ezzestus (2018-01-18T07:24:29Z)

I am also looking for incormation on this topic. Also would be willing to try and help/contribute to an aur PKGBUILD though I have not delved very deep into that aspect of arch.

---

### 评论 #3 — bradmccormack (2018-01-18T12:27:35Z)

@Narthorn It's probably worth patching the Kernel config as part of the package to apply CONFIG_KALLSYMS_ALL=y then install via DKMS.

Is that really all that is required?

I must admit, before I looked at this issue I downloaded the source and was looking at a directory structure like
```
atmi/               HIP/           ROCK-Kernel-Driver/  ROCT-Thunk-Interface/
compiler-rt/        HIP-Examples/  ROCm-Device-Libs/
hcc/                lld/           ROCR-Runtime/
hcc-clang-upgrade/  llvm/          ROC-smi/
```

I wasn't so sure about the distinction between ROCm-Device-Libs ROC-smi etc. Some of them I could obviously safely ignore but the others ... I wasn't so sure.





---

### 评论 #4 — Ezzestus (2018-01-19T00:56:25Z)

has anyone got a working PKGBUILD?

---

### 评论 #5 — Ezzestus (2018-01-22T14:10:57Z)

k so I decompress the .deb with `ar -x ocm-utils_1.7.60_amd64.deb` and I get three files. control.tar.gz, data.tar.gz and debian-binary. Then I decompress the data.tar.gz with `tar -xzf data.tar.gz` and I get an opt folder that contains a rocm folder taht contains nothing except .info. Am I missing Something?

---

### 评论 #6 — ghost (2018-01-22T14:26:49Z)

Sorry for late reply, was on holiday. To be honest i didnt get it work. To much "patch arround".
For those are after "mining issues" i can confirm that Linux 4.14.14-1-ARCH works with grub param "amdgpu.vm_fragment_size=9" mining eth steady.

If one trying to continue this, it will become unmaintainable with archs rolling kernels. Patches will be become invalid every now and then. A static kernel could be used but thats not the arch way.



---

### 评论 #7 — Ezzestus (2018-01-22T18:01:48Z)

I mean if I understand the kernel related stuff is ultimatly going to be mainlined. Micheal from phoronix seems to think it will be by 4.17. if thats true its just a matter of figuring out 4.15 and 4.16. @Narthorn you got it to build against 4.15? Did it work and would you be willing to share some insight into what you did? @derdigge did you have to change anything other then that kernel parameter? I may just have to use 4.14. I want to be able to mine but I also want to game.

---

### 评论 #8 — 949f45ac (2018-04-09T06:44:32Z)

@Ezzestus The issue creator penned it slightly wrong. Sources for the dkms are provided by ubuntu package rock-dkms, direct download link is http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms_1.7.137-ubuntu_all.deb
Also according to Phoronix, some Vega compute patches are excluded from 4.17 – I assume they are present in rock-dkms.

---

### 评论 #9 — Ezzestus (2018-07-17T03:37:46Z)

Ya, at this point it sounds like linux 4.19 will get this rolling. Heres hoping.

---

### 评论 #10 — HarlemSquirrel (2018-09-15T06:02:51Z)

I'm trying to get just openCL installed with this [PKGBUILD](https://gist.github.com/HarlemSquirrel/ea923e07f492ed6cc451a60584ada630) I wrote but am having some issues. 

It installs but I cannot run `clinfo`

```
$ /opt/rocm/opencl/bin/x86_64/clinfo  
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
[1]    9238 abort (core dumped)  /opt/rocm/opencl/bin/x86_64/clinfo
```

---

### 评论 #11 — ruben2000de (2018-11-15T14:00:18Z)

@HarlemSquirrel I have the same problem with Manjaro. opencl-mesa not working at all and opencl-amd(18.30) via AUR results in only invalid shares. rocm via AUR is also outdated.

---

### 评论 #12 — iamkucuk (2018-11-18T20:12:28Z)

Can someone add an AUR package for newbie users like me? I would be super grateful if someone provide an updated package like that.

---

### 评论 #13 — HarlemSquirrel (2018-11-18T22:01:02Z)

I tried but couldn't get it working. 

---

### 评论 #14 — drewmccal (2018-12-03T02:12:08Z)

I second Arch support!

---

### 评论 #15 — ghost (2018-12-23T17:26:49Z)

It seems that ROCm is now installable from the AUR (rocr-runtime). HIP is also available. I made a [PKGBUILD](https://gist.github.com/antifermion/bfc1a218af478a38da1a75118dd4ace9) (not sure how replace the outdated existing package, though) for OpenCL. I can compile and run OpenCL as well as HIP programs.

---

### 评论 #16 — iamkucuk (2018-12-24T09:51:04Z)

> rocr-runtime

Can you make a documentation for how to install ROCm stack on arch based system with the same outputs of the installation process for ubuntu? I find using ubuntu is very inconvenient and I would like to switch to arch based distro if possible. The community (at least I) will be very grateful if you provide a document like this.

---

### 评论 #17 — lss4 (2019-04-10T00:24:59Z)

~~Not sure if any AUR maintainers are here, but as of today the packages on AUR (rocm-opencl-runtime and its dependencies) don't seem to work properly. After install, clinfo sees nothing (even after recreating a symlink that incorrectly linked to the build path instead of install path, see AUR comments). I'm using trizen as AUR helper and apparently I'm experiencing other issues mentioned in recent AUR comments as well.~~

~~I recall it used to work properly with rocm-opencl-git (which was what I used before switching to rocm-opencl-runtime), but that PKGBUILD is not on AUR anymore.~~

~~EDIT: It seems there might be some issues with trizen. Built the package manually via makepkg and this time it was recognized right away. Although the libOpenCL.so symlink is still wrong, it turned out being unrelated to the issues I've been having, so I'll just try reinstall everything again and see if the problem would go away.~~

EDIT: For other systems the current AUR packages work, they were probably broken due to linking issues (caused by system upgrades, which can be solved by rebuilding the packages).

As for the system that still doesn't work... guess ROCm doesn't support Tonga (which that system has), so it's not really an issue.

---

### 评论 #18 — Lukew0rm (2019-04-23T13:32:14Z)

Has anyone succeeded in installing ROCm for Raven Ridge mobile using Arch or Arch-based distros such as Manjaro?
I am currently on kernel 5.0.9 and I have a notebook with Ryzen 2500u.
Which package from the AUR should I try to install? rocm-opencl-runtime? Some others?
Should ROCm work just after installing it or should I apply some tweaks?

---

### 评论 #19 — baerbock (2019-07-07T09:51:17Z)

@Lukew0rm Manjaro is a beginner's distribution, not meant for real tasks.

"Tweak" it as much you want.

---

### 评论 #20 — acxz (2020-02-29T01:32:10Z)

I know this is some time ago, but I just want to put this here in case others come across it. The ArchLinux community including me and some other folks have started picking up development on getting the ROCm stack working here: https://github.com/rocm-arch/rocm-arch. Feel free to submit PRs or issues! It would be best if the Arch community works together on one set of PKGBUILDs instead of splintering away.

---

### 评论 #21 — Rmalavally (2020-06-07T21:18:30Z)

The user contributed ArchLinux installation instructions are available at:

https://community.amd.com/thread/253882

_**Note**: The installation instructions for ArchLinux are contributed by users. Arch Linux is not currently supported by AMD ROCm and there is no obligation to correct issues that are observed or occur.  Please submit any issues you encounter at the rocm-arch `issue tracker`_._



---

### 评论 #22 — acxz (2020-06-07T23:29:42Z)

@Rmalavally I think with that post this issue can be closed, since all specific ROCm questions on Arch Linux will come over our way at https://github.com/rocm-arch/rocm-arch.

As for specific build issues the rocm-arch community has, we will open up targeted issues at the respective repos issue tracker.

@Rmalavally Thank you so much for creating that post!

---

### 评论 #23 — ROCmSupport (2021-01-05T09:47:23Z)

Closing this issue as per above comments.
Thank you.

---
