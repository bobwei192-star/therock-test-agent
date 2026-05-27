# Don't ship versioned folders in unversioned Debian packages

> **Issue #1160**
> **状态**: closed
> **创建时间**: 2020-06-22T17:00:29Z
> **更新时间**: 2021-01-12T14:55:17Z
> **关闭时间**: 2021-01-12T08:19:56Z
> **作者**: DaDummy
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1160

## 描述

While it is understandable that support for side-by-side installs of different ROCm versions is intended, this is a concept that does not seem to be properly implemented for the ROCm Debian packages.

And since the 3.5.1 release now has shown that mixed versions are getting shipped on the package repository, the symlink-approach for providing a stable path should be dropped as too unreliable to provide any real benefit.

Instead, please either adjust the packaging to install to stable unversioned paths, so things stop breaking on every other update or actually introduce versioned packages (with the version number in their names), support installing multiple of those in parallel, utilize the powerful alternatives system that comes with Debian and Debian-based distributions: https://wiki.debian.org/DebianAlternatives and then provide unversioned meta-packages that depend on the then-current versioned package similar to how e.g. Linux Kernels are distributed.

Breaking user's setups on every single update and now even patch-release is not fun. Please let's find a solution to put an end to that.

---

## 评论 (9 条)

### 评论 #1 — DaDummy (2020-06-22T17:20:42Z)

I just realized part of that mixed state resulted from some packages being re-released with the **same version**, but **changed contents**.

Come on ROC-Team, you can do better than this :(

---

### 评论 #2 — bd4 (2020-06-22T17:51:56Z)

I just ran into this with the 3.5.1 release. In particular, llvm-amdgpu is still in /opt/rocm-3.5.0 and the new hipcc in /opt/rocm-3.5.1/hip/bin (symlinked to /opt/rocm/bin) can't find it.

I am trying to hack around the broken packages by symlinking `/opt/rocm-3.5.0/llvm` into `/opt/rocm-3.5.1` and various other subdirectories which are now split across the two version directories - lib and include at least.

---

### 评论 #3 — DaDummy (2020-06-22T21:09:16Z)

As a temporary fix: Try reinstalling llvm-amdgpu:
```bash
sudo apt update
sudo apt reinstall llvm-amdgpu
```

If that package was rebuilt without changing the version number, too, it wasn't automatically updated by apt.

---

### 评论 #4 — bd4 (2020-06-22T22:17:24Z)

Thanks @DaDummy, confirmed that `apt install --reinstall llvm-amdgpu` causes it to move to the correct location.

I ran `dpkg -S /opt/rocm-3.5.0` to find remaining broken packages, and reinstalled those as well:
```
apt install --reinstall rocm-opencl-dev rocm-opencl rocprofiler-dev hsakmt-roct hsakmt-roct-dev llvm-amdgpu
```
Seems to have done the trick, on both an Ubuntu LTS and a debian stable machine.

---

### 评论 #5 — bd4 (2020-06-22T23:40:19Z)

Note that this also affects the docker images in strange ways, if you need to install any packages beyond the default set. In particular I am using 3.5 tag, and it does not include rocprim and rocthrust by default, so I apt install them, but then end up with a mixed install since the repo has moved on to 3.5.1 and all the pre-installed packages are still at 3.5.0.

---

### 评论 #6 — baryluk (2020-08-25T02:33:59Z)

This is still broken in 3.7

As other have said, only versioned packages should be installed and provide the actual files.

The non versioned packages should be virtual and depend on latest versioned packages.

Multiple versioned packages should be co-installable, and managed via debian alternatives mechanisms. All binaries should have versions in their name, with the symlinks to also provide non-versioned names.

This is easy and works so well.

I mentioned that before in https://github.com/RadeonOpenCompute/ROCm/issues/1134

---

### 评论 #7 — ROCmSupport (2021-01-12T08:05:06Z)

Thanks all for sharing updates on this.
As, now,  side-by-side install is matured and versioned packages are properly made, request you to validate with the latest ROCm 4.0 and update the same. 
Thank you.

---

### 评论 #8 — ROCmSupport (2021-01-12T08:19:56Z)

To conclude the issue, we do not have plans to separate versioned and non-versioned packages in different paths/folders.
Versioned packages are working good now with the latest ROCm 4.0 and so request to try the same.
Thank you.

---

### 评论 #9 — baryluk (2021-01-12T14:55:17Z)

Still broken in 4.0.


---
