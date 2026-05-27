# Which OpenGL version did ROCm support?

> **Issue #235**
> **状态**: closed
> **创建时间**: 2017-10-25T03:19:32Z
> **更新时间**: 2018-06-03T15:15:29Z
> **关闭时间**: 2018-06-03T15:15:29Z
> **作者**: lintcoder
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/235

## 标签

- **Question** (颜色: #cc317c)

## 描述

Now I have built ROCK-Kernel-Driver, ROCT-Thunk-Interface and ROCR-Runtime from branch roc-1.6.3 on my ubunu16.04-arm64 server which is running on Cavium Thunder X.
then I install mesa with 'sudo apt-get install mesa-common-dev mesa-utils',  checking with 'glxinfo | grep OpenGL' , output is as follows:

OpenGL vendor string: VMware, Inc.
OpenGL renderer string: Gallium 0.4 on llvmpipe (LLVM 4.0, 128 bits)
OpenGL core profile version string: 3.3 (Core Profile) Mesa 17.0.7
OpenGL core profile shading language version string: 3.30
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile
OpenGL core profile extensions:
OpenGL version string: 3.0 Mesa 17.0.7
OpenGL shading language version string: 1.30
OpenGL context flags: (none)
OpenGL extensions:
OpenGL ES profile version string: OpenGL ES 3.0 Mesa 17.0.7
OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.00
OpenGL ES profile extensions

I wonder if ROCm kernel driver support more higher version of OpenGL?

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-10-25T03:54:11Z)

This is not running on the GPU, one thing if you need  Vega support you will need to update Mesa from an external package repo like  https://launchpad.net/~paulo-miguel-dias/+archive/ubuntu/mesa) or build Mesa from source. 

---

### 评论 #2 — lintcoder (2017-10-25T06:36:27Z)

@gstoner I am not sure what you mean. With the situation I've refered, some cases in https://cgit.freedesktop.org/mesa/demos/ and https://github.com/KhronosGroup/VK-GL-CTS can run successfully on my platform

---

### 评论 #3 — zhaojunfan (2017-10-25T07:18:22Z)

@gstoner , 
# 1. I use the link you said.  https://launchpad.net/~paulo-miguel-dias/+archive/ubuntu/mesa),
sudo add-apt-repository ppa:paulo-miguel-dias/mesa
sudo apt-get update
Reading package lists... Done
W: The repository 'http://packages.amd.com/rocm/apt/debian trusty Release' does not have a Release file.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
E: Failed to fetch http://packages.amd.com/rocm/apt/debian/dists/trusty/main/binary-amd64/Packages  404  Not Found
E: Some index files failed to download. They have been ignored, or old ones used instead.

So I can not get the packages!!!


# 2, I have problem about building Mesa source code with ROCM on AARCH64.
I download the newest code mesa-17.2.3.tar.gz, and try to build it.
   1). ./configure this pass.
    2). make this have errors.
console output:
make[7]: Entering directory '/home/cavium/MESA/mesa-17.2.3/src/mesa/drivers/dri/i965'
  CC       brw_binding_tables.lo
gcc: error: unrecognized command line option ‘-msse2’
Makefile:1113: recipe for target 'brw_binding_tables.lo' failed
make[7]: *** [brw_binding_tables.lo] Error 1
make[7]: Leaving directory '/home/cavium/MESA/mesa-17.2.3/src/mesa/drivers/dri/i965'
Makefile:900: recipe for target 'all' failed
make[6]: *** [all] Error 2
make[6]: Leaving directory '/home/cavium/MESA/mesa-17.2.3/src/mesa/drivers/dri/i965'
Makefile:777: recipe for target 'all-recursive' failed
make[5]: *** [all-recursive] Error 1
make[5]: Leaving directory '/home/cavium/MESA/mesa-17.2.3/src/mesa/drivers/dri'
Makefile:3029: recipe for target 'all-recursive' failed
make[4]: *** [all-recursive] Error 1
make[4]: Leaving directory '/home/cavium/MESA/mesa-17.2.3/src/mesa'
Makefile:1882: recipe for target 'all' failed
make[3]: *** [all] Error 2
make[3]: Leaving directory '/home/cavium/MESA/mesa-17.2.3/src/mesa'
Makefile:855: recipe for target 'all-recursive' failed
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory '/home/cavium/MESA/mesa-17.2.3/src'
Makefile:646: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/cavium/MESA/mesa-17.2.3/src'
Makefile:652: recipe for target 'all-recursive' failed
make: *** [all-recursive] Error 1

So have you built Mesa with ROCM on AARCH64? And If you have, Please tell me how you did it. Thanks!!

---

### 评论 #4 — gstoner (2017-10-25T12:03:49Z)

Our normal mode of operation is headless for ROCm, we use the core product on our server products.  Looks like your wanting Workstation products.  

Also above your failing in Intel directory i965 is not AMD part 

---

### 评论 #5 — jamilbk (2017-10-25T14:51:14Z)

@zhaojunfan Your `apt-get` commands are failing because of the `http://packages.amd.com/rocm/apt/debian` repository, not because of any instructions @gstoner gave you. I *believe* that repository was deprecated in favor of `repo.radeon.com` so I'd suggest doing a search/replace and see if that fixes your issue.

---
