# Need findROCM with modern CMake support

> **Issue #1259**
> **状态**: closed
> **创建时间**: 2020-10-15T02:03:53Z
> **更新时间**: 2024-02-01T17:04:39Z
> **关闭时间**: 2024-02-01T17:04:39Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1259

## 描述

Current CMake needs improvements. Please match [FindCUDAToolkit](https://cmake.org/cmake/help/git-stage/module/FindCUDAToolkit.html) and define targets for all the components.
FindHIP and FindROCR are too basic and pre-modern cmake.

---

## 评论 (15 条)

### 评论 #1 — rkothako (2020-10-15T06:58:15Z)

Hi @ye-luo 
Thanks for the ticket.
We are checking with corresponding team internally and will get back to you soon.

---

### 评论 #2 — rkothako (2020-11-18T07:54:33Z)

Hi @ye-luo 
We have plans to upgrade to modern cmake for ROCm and discussions are in progress.
We will inform once we upgrade officially.


---

### 评论 #3 — rkothako (2020-11-18T07:55:08Z)

I request you close this ticket meanwhile.

---

### 评论 #4 — ye-luo (2020-11-18T14:46:26Z)

I will close this ticket when the first bits of progress shows up in the release.

---

### 评论 #5 — ye-luo (2021-12-11T19:11:20Z)

My first ride is pretty rough. Here is the list of issues to track
https://github.com/ROCm-Developer-Tools/HIP/issues/2433
~~https://github.com/ROCm-Developer-Tools/HIP/pull/2434~~ superseded by https://github.com/ROCm-Developer-Tools/HIP/pull/2776
~~https://github.com/ROCm-Developer-Tools/hipamd/pull/7~~
https://github.com/RadeonOpenCompute/ROCm/issues/1636
https://gitlab.kitware.com/cmake/cmake/-/issues/23006

My goal is to get the following working
```
  enable_language(HIP)
  list(PREPEND CMAKE_PREFIX_PATH ${CMAKE_HIP_COMPILER_ROCM_ROOT})
  find_package(hip CONFIG REQUIRED)
  find_package(hipblas CONFIG REQUIRED)
```
but it seems needing multiple fixes. I hope to someone from AMD who has a extensive picture of CMake in ROCm to look at those.

---

### 评论 #6 — ROCmSupport (2021-12-14T09:03:31Z)

Hi @ye-luo 
As discussed in the previous comments, hope you are going to close this ticket. Thank you.

---

### 评论 #7 — Maxzor (2021-12-29T01:28:24Z)

Please do worry less about closing this ticket, than about fixing the current cmake/hipconfig situation.
I am doing an effort, alongside the dedicated packaging team, for native Debian packaging, and the general assumption that the ROCm toolkit is all under one directory - binaries, libraries, be it in the default /opt/rocm or somewhere else... feels pretty wrong.
  - https://salsa.debian.org/rocm-team
  - https://salsa.debian.org/users/maxzor/projects

The hipconfig and hipvars scripts are especially weak.

I am trying to get the hip [cmake test suite](https://github.com/ROCm-Developer-Tools/HIP/tree/develop/tests) (on top of the external [test-suite](https://github.com/rocm-developer-tools/hip-testsuite) and [example](https://github.com/rocm-developer-tools/hip-examples) repos) working with a decoupled install. ROCm libraries in `/usr/{lib, share}/rocm` and binaries in `/usr/bin/rocm` : I am currently fighting the whole build system of ROCm and this is exhausting. **This person's work really looks like going in the good direction**, into making more robust design decisions.


---

### 评论 #8 — ye-luo (2022-03-31T04:37:36Z)

I just noticed another trouble https://github.com/RadeonOpenCompute/ROCm/issues/1717

---

### 评论 #9 — torehl (2022-04-04T21:18:19Z)

@Maxzor 

> I am doing an effort, alongside the dedicated packaging team, for native Debian packaging, and the general assumption that the ROCm toolkit is all under one directory - binaries, libraries, be it in the default /opt/rocm or somewhere else... feels pretty wrong.

I completely agree. - Been trying to make ROCm work in a module environment, and think this needs fixing in order for it to work properly. Also opened https://gitlab.freedesktop.org/drm/amd/-/issues/1961 in hope of getting them to allow for "--prefix" and "--modulefiles" to generate  modules files for ROCm install.

I tried tar'ing to keep soft links and moved it to /cm/shared/apps/amd/rocm/5.1.0 (Bright (soon Nvidia) CM), and configured a modules file, the enduser could compile on login node w/o AMD GPUs. I could also build targeted clang and gcc. But during runtime, it seems to have issues picking up soflinked dso's of underlying directories, and I think this is related to what you describe. Looks like I need to copy all dso's into the main lib directory in the same way Nvidia cuda has it.

---

### 评论 #10 — keryell (2022-04-05T21:02:29Z)

> Hi @ye-luo As discussed in the previous comments, hope you are going to close this ticket. Thank you.

@ROCmSupport Is the problem solved?

---

### 评论 #11 — cgmb (2022-04-05T21:33:33Z)

@torehl, if you haven't checked it out before, maybe give [Spack](https://spack.readthedocs.io) a try. AMD contributes build recipes to Spack for much of the ROCm stack, and [it integrates with lmod](https://spack.readthedocs.io/en/latest/module_file_support.html).

---

### 评论 #12 — keryell (2022-04-27T18:30:36Z)

> @torehl, if you haven't checked it out before, maybe give [Spack](https://spack.readthedocs.io) a try. AMD contributes build recipes to Spack for much of the ROCm stack, and [it integrates with lmod](https://spack.readthedocs.io/en/latest/module_file_support.html).

Spack is great but I have not been able to have the full latest ROCm stack compiling on Ubuntu 21.10.
I have moved recently to 22.04, so I can probably give it a try again.

---

### 评论 #13 — ronlieb (2022-05-16T18:09:56Z)

@ROCmSupport   please address this issue

---

### 评论 #14 — nartmada (2024-02-01T16:59:16Z)

Sorry for the delay @ronlieb and @ye-luo.  I had a chat with the internal team and they said the support has been implemented in cmake 3.21.X and available to the public.  

https://cmake.org/cmake/help/latest/search.html?q=hip

Please check and let me know if this is still an issue.  Thanks for your patience.



---

### 评论 #15 — ye-luo (2024-02-01T17:04:39Z)

Working fine now.

---
