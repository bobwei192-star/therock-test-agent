# Errors were encountered while processing:  /var/cache/apt/archives/rock-dkms_1.9-211_all.deb

> **Issue #556**
> **状态**: closed
> **创建时间**: 2018-09-24T02:31:18Z
> **更新时间**: 2018-09-24T03:00:41Z
> **关闭时间**: 2018-09-24T03:00:41Z
> **作者**: emmeowzing
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/556

## 描述

While trying to install via `apt`, I continue to receive this message, and I don't know how to solve the conflicting overwrite due to the AMDGPU-PRO driver package. Any tips?
```
$ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  comgr hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev
  rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo rocr_debug_agent
The following NEW packages will be installed:
  comgr hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev
  rock-dkms rocm-clang-ocl rocm-dev rocm-device-libs rocm-dkms rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo
  rocr_debug_agent
0 upgraded, 22 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/406 MB of archives.
After this operation, 1,898 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Selecting previously unselected package comgr.
(Reading database ... 243982 files and directories currently installed.)
Preparing to unpack .../archives/comgr_0.0.0_amd64.deb ...
Unpacking comgr (0.0.0) ...
Selecting previously unselected package hsa-ext-rocr-dev.
Preparing to unpack .../hsa-ext-rocr-dev_1.1.9-8-g51c00c2_amd64.deb ...
Unpacking hsa-ext-rocr-dev (1.1.9-8-g51c00c2) ...
Selecting previously unselected package hsakmt-roct.
Preparing to unpack .../hsakmt-roct_1.0.9-8-g238782c_amd64.deb ...
Unpacking hsakmt-roct (1.0.9-8-g238782c) ...
Selecting previously unselected package hsakmt-roct-dev.
Preparing to unpack .../hsakmt-roct-dev_1.0.9-8-g238782c_amd64.deb ...
Unpacking hsakmt-roct-dev (1.0.9-8-g238782c) ...
Selecting previously unselected package hsa-rocr-dev.
Preparing to unpack .../hsa-rocr-dev_1.1.9-8-g51c00c2_amd64.deb ...
Unpacking hsa-rocr-dev (1.1.9-8-g51c00c2) ...
Selecting previously unselected package rocminfo.
Preparing to unpack .../rocminfo_1.0.0_amd64.deb ...
Unpacking rocminfo (1.0.0) ...
Selecting previously unselected package rocm-opencl.
Preparing to unpack .../rocm-opencl_1.2.0-2018090737_amd64.deb ...
Unpacking rocm-opencl (1.2.0-2018090737) ...
Selecting previously unselected package rocm-opencl-dev.
Preparing to unpack .../rocm-opencl-dev_1.2.0-2018090737_amd64.deb ...
Unpacking rocm-opencl-dev (1.2.0-2018090737) ...
Selecting previously unselected package rocm-clang-ocl.
Preparing to unpack .../rocm-clang-ocl_0.3.0-7997136_amd64.deb ...
Unpacking rocm-clang-ocl (0.3.0-7997136) ...
Selecting previously unselected package rocm-utils.
Preparing to unpack .../rocm-utils_1.9.211_amd64.deb ...
Unpacking rocm-utils (1.9.211) ...
Selecting previously unselected package hcc.
Preparing to unpack .../hcc_1.2.18354_amd64.deb ...
Unpacking hcc (1.2.18354) ...
Selecting previously unselected package hip_base.
Preparing to unpack .../hip%5fbase_1.5.18353_amd64.deb ...
Unpacking hip_base (1.5.18353) ...
Selecting previously unselected package hip_doc.
Preparing to unpack .../hip%5fdoc_1.5.18353_amd64.deb ...
Unpacking hip_doc (1.5.18353) ...
Selecting previously unselected package hip_hcc.
Preparing to unpack .../hip%5fhcc_1.5.18353_amd64.deb ...
Unpacking hip_hcc (1.5.18353) ...
Selecting previously unselected package hip_samples.
Preparing to unpack .../hip%5fsamples_1.5.18353_amd64.deb ...
Unpacking hip_samples (1.5.18353) ...
Selecting previously unselected package hsa-amd-aqlprofile.
Preparing to unpack .../hsa-amd-aqlprofile_1.0.0_amd64.deb ...
Unpacking hsa-amd-aqlprofile (1.0.0) ...
Preparing to unpack .../rock-dkms_1.9-211_all.deb ...
Unpacking rock-dkms (1.9-211) ...
dpkg: error processing archive /var/cache/apt/archives/rock-dkms_1.9-211_all.deb (--unpack):
 trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 18.20-621984
dpkg-deb: error: subprocess paste was killed by signal (Broken pipe)
Selecting previously unselected package rocm-device-libs.
Preparing to unpack .../rocm-device-libs_0.0.1_amd64.deb ...
Unpacking rocm-device-libs (0.0.1) ...
Selecting previously unselected package rocm-smi.
Preparing to unpack .../rocm-smi_1.0.0-72-gec1da05_amd64.deb ...
Unpacking rocm-smi (1.0.0-72-gec1da05) ...
Selecting previously unselected package rocr_debug_agent.
Preparing to unpack .../rocr%5fdebug%5fagent_1.0.0_amd64.deb ...
Unpacking rocr_debug_agent (1.0.0) ...
Selecting previously unselected package rocm-dev.
Preparing to unpack .../rocm-dev_1.9.211_amd64.deb ...
Unpacking rocm-dev (1.9.211) ...
Selecting previously unselected package rocm-dkms.
Preparing to unpack .../rocm-dkms_1.9.211_amd64.deb ...
Unpacking rocm-dkms (1.9.211) ...
Errors were encountered while processing:
 /var/cache/apt/archives/rock-dkms_1.9-211_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
Conflict between this package and `amdgpu`, which already has `amdgpu-dkms`.
```
$ sudo apt -f install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Correcting dependencies... Done
The following additional packages will be installed:
  rock-dkms
The following NEW packages will be installed:
  rock-dkms
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
21 not fully installed or removed.
Need to get 0 B/5,685 kB of archives.
After this operation, 131 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
(Reading database ... 245395 files and directories currently installed.)
Preparing to unpack .../rock-dkms_1.9-211_all.deb ...
Unpacking rock-dkms (1.9-211) ...
dpkg: error processing archive /var/cache/apt/archives/rock-dkms_1.9-211_all.deb (--unpack):
 trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 18.20-621984
dpkg-deb: error: subprocess paste was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/rock-dkms_1.9-211_all.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

---

## 评论 (1 条)

### 评论 #1 — emmeowzing (2018-09-24T02:37:27Z)

Because I don't care much if this bricks my system (I'll just fresh install), I tried the following.
```
$ sudo dpkg -i --force-overwrite /var/cache/apt/archives/rock-dkms_1.9-211_all.deb
(Reading database ... 245395 files and directories currently installed.)
Preparing to unpack .../rock-dkms_1.9-211_all.deb ...
Unpacking rock-dkms (1.9-211) ...
dpkg: warning: overriding problem because --force enabled:
dpkg: warning: trying to overwrite '/usr/share/dkms/modules_to_force_install/amdgpu', which is also in package amdgpu-dkms 18.20-621984
dpkg: warning: overriding problem because --force enabled:
dpkg: warning: trying to overwrite '/etc/modprobe.d/blacklist-radeon.conf', which is also in package amdgpu-dkms 18.20-621984
Setting up rock-dkms (1.9-211) ...
Loading new amdgpu-1.9-211 DKMS files...
First Installation: checking all kernels...
Building only for 4.15.0-34-generic
Building for architecture x86_64
Building initial module for 4.15.0-34-generic
Done.
Forcing installation of amdgpu

amdgpu:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdttm.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdkcl.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdchash.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amd-sched.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

amdkfd.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/4.15.0-34-generic/updates/dkms/

Running the post_install script:
update-initramfs: Generating /boot/initrd.img-4.15.0-34-generic

depmod....

Backing up initrd.img-4.15.0-34-generic to /boot/initrd.img-4.15.0-34-generic.old-dkms
Making new initrd.img-4.15.0-34-generic
(If next boot fails, revert to initrd.img-4.15.0-34-generic.old-dkms image)
update-initramfs....

DKMS: install completed.
Processing triggers for initramfs-tools (0.122ubuntu8.12) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-34-generic
W: Possible missing firmware /lib/firmware/amdgpu/vegam_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_uvd.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_vce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vegam_smc.bin for module amdgpu
```
per [this thread](https://community.amd.com/thread/229198). Now
```
$ sudo apt -f install
Reading package lists... Done
Building dependency tree       
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
21 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Setting up comgr (0.0.0) ...
Setting up hsa-ext-rocr-dev (1.1.9-8-g51c00c2) ...
Setting up hsakmt-roct (1.0.9-8-g238782c) ...
Setting up hsakmt-roct-dev (1.0.9-8-g238782c) ...
Setting up hsa-rocr-dev (1.1.9-8-g51c00c2) ...
Setting up rocminfo (1.0.0) ...
Setting up rocm-opencl (1.2.0-2018090737) ...
Setting up rocm-opencl-dev (1.2.0-2018090737) ...
Setting up rocm-clang-ocl (0.3.0-7997136) ...
Setting up rocm-utils (1.9.211) ...
Setting up hcc (1.2.18354) ...
Setting up hip_base (1.5.18353) ...
Setting up hip_doc (1.5.18353) ...
Setting up hip_hcc (1.5.18353) ...
Setting up hip_samples (1.5.18353) ...
Setting up hsa-amd-aqlprofile (1.0.0) ...
Setting up rocm-device-libs (0.0.1) ...
Setting up rocm-smi (1.0.0-72-gec1da05) ...
Setting up rocr_debug_agent (1.0.0) ...
Setting up rocm-dev (1.9.211) ...
Setting up rocm-dkms (1.9.211) ...
KERNEL=="kfd", MODE="0666"
Processing triggers for libc-bin (2.23-0ubuntu10) ...
brandon@ideaDesktopHome:~$ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-dkms is already the newest version (1.9.211).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

---
