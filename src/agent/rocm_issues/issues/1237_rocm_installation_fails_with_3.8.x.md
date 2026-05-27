# rocm installation fails with 3.8.x

> **Issue #1237**
> **状态**: closed
> **创建时间**: 2020-09-23T00:59:43Z
> **更新时间**: 2020-09-25T11:16:03Z
> **关闭时间**: 2020-09-25T11:16:03Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1237

## 描述

After following instructions, following installation command fails:

apt install rocm-dkms -y
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...
Reading state information...
The following packages were automatically installed and are no longer required:
  amdgpu-dkms-firmware libllvm7 linux-image-4.18.0-15-generic
  linux-modules-4.18.0-15-generic linux-modules-extra-4.18.0-15-generic
Use 'apt autoremove' to remove them.
The following additional packages will be installed:
  binfmt-support comgr hip-base hip-doc hip-rocclr hip-samples
  hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libdrm-dev
  libelf-dev libffi-dev libfile-which-perl libpthread-stubs0-dev libpython3.8
  libpython3.8-minimal libpython3.8-stdlib libtinfo-dev libx11-dev libx11-doc
  libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu llvm-amdgpu-9.0
  llvm-amdgpu-9.0-dev llvm-amdgpu-9.0-runtime llvm-amdgpu-runtime
  mesa-common-dev rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake
  rocm-dbgapi rocm-dev rocm-device-libs rocm-gdb rocm-opencl rocm-opencl-dev
  rocm-smi rocm-smi-lib64 rocm-utils rocminfo rocprofiler-dev roctracer-dev
  x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev
Suggested packages:
  libxcb-doc
The following NEW packages will be installed:
  binfmt-support comgr hip-base hip-doc hip-rocclr hip-samples
  hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libdrm-dev
  libelf-dev libffi-dev libfile-which-perl libpthread-stubs0-dev libpython3.8
  libpython3.8-minimal libpython3.8-stdlib libtinfo-dev libx11-dev libx11-doc
  libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu llvm-amdgpu-9.0
  llvm-amdgpu-9.0-dev llvm-amdgpu-9.0-runtime llvm-amdgpu-runtime
  mesa-common-dev rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake
  rocm-dbgapi rocm-dev rocm-device-libs rocm-dkms rocm-gdb rocm-opencl
  rocm-opencl-dev rocm-smi rocm-smi-lib64 rocm-utils rocminfo rocprofiler-dev
  roctracer-dev x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev
0 upgraded, 51 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/129 MB of archives.
After this operation, 870 MB of additional disk space will be used.
Get:1 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-9.0-runtime 1:9.0-1044886 [85.5 kB]
Get:2 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-runtime 1:9.0-1044886 [4536 B]
Get:3 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-9.0 1:9.0-1044886 [3369 kB]
Get:4 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu 1:9.0-1044886 [5236 B]
Get:5 file:/var/opt/amdgpu-pro-local ./ llvm-amdgpu-9.0-dev 1:9.0-1044886 [20.9 MB]
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype
dpkg-preconfigure: unable to re-open stdin:
(Reading database ... 215107 files and directories currently installed.)
Preparing to unpack .../rock-dkms-firmware_1%3a3.8-30_all.deb ...
Unpacking rock-dkms-firmware (1:3.8-30) ...
dpkg: error processing archive /var/cache/apt/archives/rock-dkms-firmware_1%3a3.8-30_all.deb (--unpack):
 trying to overwrite '/usr/share/doc/amdgpu-dkms-firmware/LICENSE', which is also in package amdgpu-dkms-firmware 1:5.4.11.69-1044886
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/rock-dkms-firmware_1%3a3.8-30_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)


---

## 评论 (7 条)

### 评论 #1 — rkothako (2020-09-23T08:06:17Z)

Hi @gggh000 
We have not seen this problem locally.
We are working on it and will give an update soon.

---

### 评论 #2 — rkothako (2020-09-23T09:30:20Z)

Hi @gggh000 
Looks like you have installed amdgpu-pro driver initially and then you are trying to install ROCm on it. is it correct?
Please confirm the steps you followed.

---

### 评论 #3 — gggh000 (2020-09-23T18:04:43Z)

Yes, however I removed by "apt remove amdgpu-dkms -y" and it was working in previous versions like 3.5 and before. 



---

### 评论 #4 — kentrussell (2020-09-23T18:09:31Z)

Don't forget to remove amdgpu-dkms-firmware, as that is where this file comes from, and it would conflict with rock-dkms-firmware

---

### 评论 #5 — rkothako (2020-09-24T04:37:10Z)

Thanks @gggh000 
We are not supporting the mix/combination of both amdgpu-pro and rocm. Hence recommend to not to install both at same time.

---

### 评论 #6 — gggh000 (2020-09-24T23:04:40Z)

thanks, after removing amdgpu-dkms-firmware, it appears to install. 

---

### 评论 #7 — kentrussell (2020-09-25T11:16:03Z)

I am glad that it worked. Since we split the kernel+firmware into 2 separate packages, these are the things that we tend to forget about. Good luck!

---
