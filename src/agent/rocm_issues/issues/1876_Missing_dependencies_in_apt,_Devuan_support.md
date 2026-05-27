# Missing dependencies in apt, Devuan support

> **Issue #1876**
> **状态**: closed
> **创建时间**: 2022-12-13T18:42:40Z
> **更新时间**: 2024-05-23T18:22:37Z
> **关闭时间**: 2024-05-23T18:22:37Z
> **作者**: Foxy6670
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1876

## 描述

I tried installing AMD's GPU drivers on Devuan 4 (chimaera)  Linux, only to be met with a few issues.

First and foremost, I would like to mention that Devuan is a version of Debian that doesn't use SystemD to boot. Now, on to the issue.

I first started by going to the AMD support website, and downloading the Ubuntu (x86_64) deb file. After running an `apt install` on it, it installed `amdgpu-install` just fine. However, after running it, I got an error stating that the OS was unrecognized. After changing the /etc/os-release to match Debian Bullseye, I ran it again. It got further, but failed when it had unmet dependencies: 
```
Hit:1 https://dl.google.com/linux/chrome/deb stable InRelease
Hit:2 https://repo.radeon.com/amdgpu/5.4.1/ubuntu focal InRelease
Hit:3 https://repo.radeon.com/rocm/apt/5.4.1 focal InRelease
Get:4 http://pkgmaster.devuan.org/merged chimaera-security InRelease [26.2 kB]
Get:5 http://deb.devuan.org/merged chimaera InRelease [33.5 kB]                
Get:6 http://deb.devuan.org/merged chimaera-updates InRelease [26.1 kB]        
Get:7 http://pkgmaster.devuan.org/merged chimaera-security/non-free Sources [648 B]
Get:8 http://deb.devuan.org/merged chimaera/non-free Sources [81.4 kB]
Get:9 http://pkgmaster.devuan.org/merged chimaera-security/main Sources [122 kB]
Get:10 http://deb.devuan.org/merged chimaera/contrib Sources [43.3 kB]
Get:11 http://deb.devuan.org/merged chimaera/main Sources [8,612 kB]
Get:12 http://pkgmaster.devuan.org/merged chimaera-security/main amd64 Packages [210 kB]
Get:13 http://pkgmaster.devuan.org/merged chimaera-security/main i386 Packages [209 kB]
Get:14 http://pkgmaster.devuan.org/merged chimaera-security/main Translation-en [3,924 B]
Get:15 http://pkgmaster.devuan.org/merged chimaera-security/non-free amd64 Packages [544 B]
Get:16 http://pkgmaster.devuan.org/merged chimaera-security/non-free i386 Packages [540 B]
Get:17 http://deb.devuan.org/merged chimaera/main amd64 Packages [8,313 kB]    
Get:18 http://deb.devuan.org/merged chimaera/main i386 Packages [8,251 kB]     
Get:19 http://deb.devuan.org/merged chimaera/main Translation-en [6,480 kB]    
Get:20 http://deb.devuan.org/merged chimaera/contrib amd64 Packages [50.7 kB]  
Get:21 http://deb.devuan.org/merged chimaera/contrib i386 Packages [45.5 kB]   
Get:22 http://deb.devuan.org/merged chimaera/contrib Translation-en [46.9 kB]  
Get:23 http://deb.devuan.org/merged chimaera/non-free amd64 Packages [98.1 kB] 
Get:24 http://deb.devuan.org/merged chimaera/non-free i386 Packages [79.6 kB]  
Get:25 http://deb.devuan.org/merged chimaera/non-free Translation-en [91.3 kB] 
Get:26 http://deb.devuan.org/merged chimaera-updates/main Sources [4,848 B]    
Get:27 http://deb.devuan.org/merged chimaera-updates/main i386 Packages [15.1 kB]
Get:28 http://deb.devuan.org/merged chimaera-updates/main amd64 Packages [14.7 kB]
Get:29 http://deb.devuan.org/merged chimaera-updates/main Translation-en [7,933 B]
Fetched 32.9 MB in 20s (1,651 kB/s)                                            
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
linux-headers-5.10.0-19-amd64 is already the newest version (5.10.149-2).
linux-headers-5.10.0-19-amd64 set to manually installed.
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-llvm : Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable or
                      libstdc++-11-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable or
                      libgcc-11-dev but it is not installable
             Recommends: gcc-multilib but it is not going to be installed
             Recommends: g++-multilib but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```
This is as far as I have been able to get on my own. I have been trying to install drivers for an AMD RX 550 to work with Hashcat. Help is appreciated, thank you.

---

## 评论 (6 条)

### 评论 #1 — KOLANICH (2023-01-09T11:57:55Z)

I have the similar issue with both Debian `testing` and `unstable`

```
apt install -o Debug::pkgProblemResolver=yes rocm-dkms
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Starting pkgProblemResolver with broken count: 1
Starting 2 pkgProblemResolver with broken count: 1
Investigating (0) rocm-dkms:amd64 < none -> 5.4.0.50400-72~20.04 @un puN Ib >
Broken rocm-dkms:amd64 Depends on rocm-dev:amd64 < none | 5.4.0.50400-72~20.04 @un uH >
  Considering rocm-dev:amd64 1 as a solution to rocm-dkms:amd64 9999
  Re-Instated rocm-core:amd64
  Re-Instated comgr:amd64
  Re-Instated liburi-encode-perl:amd64
  Re-Instated libfile-copy-recursive-perl:amd64
  Re-Instated libfile-which-perl:amd64
  Re-Instated hip-dev:amd64
  Re-Instated hip-doc:amd64
  Re-Instated hipify-clang:amd64
  Re-Instated hsa-rocr:amd64
  Re-Instated libpciaccess-dev:amd64
  Re-Instated libdrm-dev:amd64
  Re-Instated hsakmt-roct-dev:amd64
  Re-Instated hsa-rocr-dev:amd64
  Re-Instated libhsakmt1:amd64
  Re-Instated libhsa-runtime64-1:amd64
  Re-Instated rocminfo:amd64
    Reinst Failed early because of libstdc++-5-dev:amd64
    Reinst Failed early because of libstdc++-7-dev:amd64
  Re-Instated gcc-11-base:amd64
  Re-Instated libasan6:amd64
  Re-Instated libtsan0:amd64
  Re-Instated libgcc-11-dev:amd64
  Re-Instated libstdc++-11-dev:amd64
  Re-Instated rocm-llvm:amd64
  Re-Instated hip-runtime-amd:amd64
  Re-Instated hip-samples:amd64
  Re-Instated hsa-amd-aqlprofile:amd64
  Re-Instated openmp-extras-runtime:amd64
    Reinst Failed early because of rocm-cmake:amd64
Broken rocm-dkms:amd64 Depends on rock-dkms:amd64 < none @un H >
Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-dkms : Depends: rocm-dev but it is not going to be installed
             Depends: rock-dkms but it is not installable
E: Unable to correct problems, you have held broken packages.
```

---

### 评论 #2 — fxzjshm (2023-01-17T17:35:37Z)

@KOLANICH Seems that `rock-dkms` is now provided by `amdgpu-dkms` which is in the AMDGPU stack repository, refer to the [doc](https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4/page/How_to_Install_ROCm.html#d23e2000) for detail, esp. sections titled like "Adding the AMDGPU Stack Repository".

---

### 评论 #3 — KOLANICH (2023-01-17T22:43:07Z)

@fxzjshm, thanks for the info.

1. Can I install only amdgpu parts I don't get with kernels packaged in Debian? Or do I need all the drivers from AMD?
2. Are there any official (I have found some obsolete unofficial, but I guess there should be the ones AMD uses itself somewhere...) docs/recepies/scripts for generating Debian packages from the contents of https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/master/drivers/gpu/drm/amd ? 

---

### 评论 #4 — fxzjshm (2023-01-18T08:01:28Z)

@KOLANICH I used to install only `amdgpu-dkms` and it worked fine. And if your kernel is recent enough, you can also just install `rocm-dev` and use driver provided by kernel.

As to the second point, I don't know...

Probably this is off-topic from the original issue, sorry for any inconvenience...

---

### 评论 #5 — onitake (2023-02-25T15:20:05Z)

@Foxy6670 It looks like your install is failing because Devuan chimeara (or Debian bullseye, which it's based on) doesn't have any of the offered libstdc++ versions.
You should be more successful with Daedalus or Ceres, which have libstdc++-11.

@KOLANICH Yours is a different a different problem, please open a separate bug report for this.

---

### 评论 #6 — ppanchad-amd (2024-05-09T19:09:08Z)

@Foxy6670 Has your issue been resolved? If so, please close ticket. Thanks!

---
