# please consider a distro independent binary distribution

> **Issue #1630**
> **状态**: open
> **创建时间**: 2021-11-26T18:38:48Z
> **更新时间**: 2025-01-10T18:20:28Z
> **作者**: esistgut
> **标签**: Feature Request, Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1630

## 标签

- **Feature Request** (颜色: #fbca04)
- **Under Investigation** (颜色: #0052cc)

## 描述

A big fat tar to extract somewhere in `/opt/` would be quite useful for people using distributions other than rpm/deb based ones.

---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2021-12-14T06:51:47Z)

Thanks for reaching out.
I will check for feasibility of this request.
I will update once I hear from the team. Thank you.

---

### 评论 #2 — Maxzor (2021-12-29T03:12:02Z)

I am trying to package ROCm for Debian and this looks to me like the opposite of what I want.

Having a big tarball in /opt/rocm is exactly how AMD currently favors distributing its stack.
It is coupled with the fact that they quite setup their entire build system on that assumption.
Those two elements make for a very hard time packaging it properly into distributions while respecting the Filesystem Hierarchy Standard, which is common to an overwhelming majority of distros.

I'd venture to opinate, that the fact that AMD privileged installing in bulk in /opt, like a student discovering Linux and installing all in $HOME, is the main reason why the software distribution, for this very cool compute platform, lags so bad. It allowed AMD to keep iterating on a very weak config basis (hipvars, ROCM_PATH...)

---

### 评论 #3 — ye-luo (2021-12-29T03:32:13Z)

Installing the whole ROCm in 'untar' fashion is a necessary feature for HPCs which generally don't rely on distro package manager for user facing software packages. Right now I have to manually unpack all RPMs and then move files to a desired location other than `/opt/rocm`. I'd like to have an `untar` route like CUDAtoolkit installer offers.

ROCm needs to serve both HPC and Workstations. So need to keep consolidating "distro packages" and "untar" routes.


---

### 评论 #4 — Maxzor (2021-12-29T03:52:53Z)

We will have both routes for a while and this is not a bad thing:
 - the CPackDeb cmake generator building the AMD nightly binary deb/rpm packages for people looking for cutting-edge at https://repo.radeon.com.
 - distro official integration

I think that currently, the `untar` route is in a better shape than the 'distro package' one, mirroring the HPC focus, compared to general consumer market support from AMD.

I think that AMD should completely ditch the CPackDeb infrastructure which pollutes the whole codebase, and instead setup dedicated per-distro CI/CD, nightly build farms, in a classic Travis or something style.

---

### 评论 #5 — Maxzor (2022-01-30T18:10:24Z)

@ye-luo Hello, I am having discussions around the build system and some cmake recommendations for Debian, you could chime in to make sure your HPC perspective is taken into account as well!
https://lists.debian.org/debian-ai/2022/01/msg00103.html
Note, you do have a cmake variable CMAKE_INSTALL_PREFIX at hand when compiling.

---

### 评论 #6 — ye-luo (2022-01-30T18:26:44Z)

@Maxzor CC me via email (Click my github profile and then homepage).

---

### 评论 #7 — sohaibnd (2024-10-21T19:47:43Z)

Hi @esistgut, apologies for the late response. There is currently work in progress for a self contained installer that does not require a package manager like rpm or deb, and will be coming soon.

@Maxzor With regards to having distro official integration, the distro packages are mainly handled by the the specific distributions themselves and not AMD so it is recommended that users follow the instructions in our [docs](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html) (which pull the packages from [https://repo.radeon.com](https://repo.radeon.com)) to install ROCm.

@Maxzor @ye-luo With regards to your point on using the standard paths for installing software on linux (/usr/bin, etc.), this is being addressed and will hopefully be fixed on rpm at least in an upcoming release. 

I am keeping this issue open right now to track the progress for (1) and (3). Also, if the above comments don't address installation for your specific use case, feel free provide additional feedback so we can look into it.

---

### 评论 #8 — inevity (2025-01-08T12:11:53Z)

@sohaibnd For self contained installer, do you mean this [ROCm Runfile Installer](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/rocm-runfile-installer.html)? If yes, it only support ubuntu. So it is useless for other linux distribution.

---

### 评论 #9 — sohaibnd (2025-01-10T18:20:26Z)

@inevity Yes, that is the self contained installer. Currently, there is only support for Ubuntu 22.04 but support for additional distros will be added in future releases.

---
