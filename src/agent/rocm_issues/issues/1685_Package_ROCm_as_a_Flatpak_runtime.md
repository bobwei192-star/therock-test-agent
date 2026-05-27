# Package ROCm as a Flatpak runtime.

> **Issue #1685**
> **状态**: closed
> **创建时间**: 2022-02-19T10:55:04Z
> **更新时间**: 2024-10-17T18:06:32Z
> **关闭时间**: 2024-10-17T18:06:31Z
> **作者**: RushingAlien
> **标签**: Feature Request, Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1685

## 标签

- **Feature Request** (颜色: #fbca04)
- **Under Investigation** (颜色: #0052cc)

## 描述

Hello. I wonder if it is possible for ROCm to be packaged as a flatpak runtime. Flatpak apps run itself inside a sandbox, using libraries decoupled from the main system/host. Blender 3.1 is looking ot have HIP support, but it will be unachievable on the Flatpak version on Flathub without ROCm being available as a flatpak runtime. Thanks

---

## 评论 (23 条)

### 评论 #1 — ROCmSupport (2022-02-23T08:18:39Z)

Hi @RushingAlien 
Thanks for reaching out.
I will talk to Product team and will update asap.
Thank you.

---

### 评论 #2 — nanonyme (2022-02-26T14:45:56Z)

Note specifically what would be desired most likely here is distribution as a runtime extension. (GL extension's are used for all display driver purposes confusingly including Vulkan, OpenCL etc) Then this can be combined with existing runtimes and apps.

---

### 评论 #3 — ROCmSupport (2022-03-04T08:43:44Z)

Hi @RushingAlien 
We do not have plans to create complete ROCm as a flatpak runtime, which is not our strategy,
But cases like Blender can be handled in a different way, like: Corresponding libraries/runtime to be part of the Blender install process or when it is installed, it should pull the appropriate driver and shared libraries.
I am still not sure that whether this comes under ROCm or not, still gathering more points.

---

### 评论 #4 — erkinalp (2022-03-24T05:13:34Z)

Containerised packages like snap and flatpak do not work well with quick development cycles. They are catered more towards end users.

---

### 评论 #5 — nanonyme (2022-03-24T06:22:03Z)

While your claim has nothing to do with the request to provide ROCm for flatpak blender, that is also not really true as a blanket statement. There are various ways to quick rebuild with flatpak-builder including utilisation of ccache. If anything, flatpak normally makes quick development cycles easier through ensuring you have consistent SDK to develop against and development results in binaries that are guaranteed to work in target platform. This implies less time wasted in QA. In the special case of ROCm this does not help much since ROCm is expected to be consumed widely outside flatpak as well.

---

### 评论 #6 — RushingAlien (2022-09-12T15:43:45Z)

Hello there! I have an attempt to package some rocm stuff as flatpak, over [here](https://github.com/RushingAlien/org.freedesktop.Platform.GL.rocm) namely rocm-cmake and rocm-llvm, however, I'm pretty new to this thing and have been struggling. Help will be appreciated. 

Namely, I struggle to understand the rocm stack. What is needed, what is not, what is dependent with what. Things of the sort.
for example, currently, building rocm-llvm failed for me, i assume this is because i'm missing rocm-cmake headers, but i'm not so sure, confirmation would help. I would post logs of the build process, but i lost it, will post the error log once i build it again

---

### 评论 #7 — RushingAlien (2022-09-13T00:08:57Z)

ok, compiling took hours, anyways, here:
```
collect2: fatal error: ld terminated with signal 9 [Killed]
compilation terminated.
[3990/4545] Linking CXX shared library lib/libclang-cpp.so.14git
ninja: build stopped: subcommand failed.
Error: module rocm-llvm: Child process exited with code 1
```

---

### 评论 #8 — xuhuisheng (2022-09-13T03:30:45Z)

@RushingAlien 
Here is my building scripts: <https://github.com/xuhuisheng/rocm-build.git>
The scripts based on the ROCm-5.2.3 and ubuntu-20.04.

---

### 评论 #9 — RushingAlien (2022-09-13T07:26:47Z)

```
[3983/4545] Linking CXX executable bin/clang-repl
FAILED: bin/clang-repl 
```
I think this is quite important

---

### 评论 #10 — orowith2os (2023-04-08T01:06:14Z)

I'm continuing work, and attempting to contact someone at AMD to help with packaging it here: https://github.com/orowith2os/rocm-flatpak

---

### 评论 #11 — saadrahim (2023-04-12T18:18:48Z)

Hi @orowith2os ,
Appreciate your work on enabling flatpak for ROCm. Is there something specific in terms of help that you looking for?

---

### 评论 #12 — orowith2os (2023-04-13T14:48:12Z)

I'd appreciate docs on:

- What order to build everything in
- what options to build everything with (in a very minimal config)
- and a decent build server so it doesn't take an hour to build LLVM alone

---

### 评论 #13 — orowith2os (2023-04-13T14:48:51Z)

I'm making decent progress so far, it's really just the build times that are making it annoying. I've also put things on hold while I figure out some personal stuff.

---

### 评论 #14 — saadrahim (2023-04-13T15:22:02Z)

I am starting to see a few parallel efforts to enable flatpak. See #1897 . Would it help to provide a central repository for all the efforts? It would still be community driven but work need not be duplicated?

---

### 评论 #15 — orowith2os (2023-04-13T16:30:48Z)

Some repository maintained under the ROCm banner would be nice, ideally my repository would be the base for it, since that's where the effort is right now. My repo is also based off of some previous attempts.

After it's ready for public use, it should be submitted to Flathub unless they're willing to allow it to be managed externally.

There's one more attempt that made it a bit farther than I did, but that's using buildstream, and I prefer flatpak-builder.

---

### 评论 #16 — user82622 (2023-12-21T00:07:09Z)

Anyone got this to work?

---

### 评论 #17 — pobthebuilder (2024-01-22T04:16:59Z)

> Anyone got this to work?

yes; some time ago here.
https://github.com/pobthebuilder/rocm-flatpak

i just pushed an update to freedesktop sdk 23.08 and buildstream2.

you can test this with my resolve-flatpak or the standard darktable flatpak.
https://github.com/pobthebuilder/resolve-flatpak

---

### 评论 #18 — RushingAlien (2024-01-22T06:48:44Z)

Is this with HIP or only OpenCL?

---

### 评论 #19 — abhimeda (2024-01-22T22:48:56Z)

@RushingAlien  Hi, could we close this ticket?

---

### 评论 #20 — RushingAlien (2024-02-11T14:50:21Z)

Hi, no, let's not close this as it's not full rocm, as  it seems to be opencl only with missing HIP support.

But I think we're gettign closer to that thanks to this guide : https://nhaehnle.blogspot.com/2024/02/building-hip-environment-from-scratch.html, a build guide by another AMD dev. Big revelation to me was that we don't need to build rocm-llvm, we can build the downstream parts seperately against upstream LLVM instead, which is already an available runtime.

---

### 评论 #21 — pobthebuilder (2024-02-17T21:00:23Z)

i am just spinning some updates to my rocm-flatpak package. i can look to add HIP support if it's useful.

---

### 评论 #22 — pobthebuilder (2024-02-18T01:41:07Z)

i moved rocm-flatpak forward to 5.7.1 and added HIP and hipcc. i don't use hip, but i tested it like the link you mentioned:
https://nhaehnle.blogspot.com/2024/02/building-hip-environment-from-scratch.html

using HelloWorld.cpp linked there:
https://raw.githubusercontent.com/ROCm/HIP-Examples/master/HIP-Examples-Applications/HelloWorld/HelloWorld.cpp

/usr/lib/x86_64-linux-gnu/GL/ROCm/bin/clang \
        -x hip \
        --offload-arch=gfx1100 \
        --rocm-path=/usr/lib/x86_64-linux-gnu/GL/ROCm \
        -L/usr/lib/x86_64-linux-gnu/GL/default/lib \
        -L/usr/lib/x86_64-linux-gnu/GL/ROCm/lib \
        -rpath /usr/lib/x86_64-linux-gnu/GL/ROCm/lib \
        -rpath /usr/lib/x86_64-linux-gnu/GL/default/lib \
        -lstdc++ \
        -lhsa-runtime64 \
        -lamdhip64 \
        HelloWorld.cpp 

patches welcome.

---

### 评论 #23 — sohaibnd (2024-10-17T18:06:32Z)

Hi @RushingAlien, as mentioned before, there are no plans to officially package ROCm as a flatpak so I'm going close this ticket but feel free to continue discussing progress on your own flatpaks for ROCm here.

---
