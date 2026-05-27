# error Bad return status for module build on kernel: 4.11.0-kfd-compute-rocm-rel-1.6-148 (Vega FE)

> **Issue #199**
> **状态**: closed
> **创建时间**: 2017-09-06T00:38:40Z
> **更新时间**: 2017-09-06T23:58:02Z
> **关闭时间**: 2017-09-06T23:58:02Z
> **作者**: Xuno
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/199

## 描述




#Ubuntu 16.04.3   (4.10.0-33-generic)
#Device Vega FE
#Driver installed amdgpu-pro-17.30-465504
```
$wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
$sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main &#62; /etc/apt/sources.list.d/rocm.list'

$sudo apt-get update
$sudo apt-get install rocm

Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  compute-firmware cxlactivitylogger hcc hip_base hip_doc hip_hcc hip_samples libunwind-dev
  linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148 linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148 rocm-dev rocm-device-libs rocm-profiler
  rocm-smi rocm-utils
Suggested packages:
  linux-firmware-image-4.11.0-kfd-compute-rocm-rel-1.6-148
The following NEW packages will be installed:
  compute-firmware cxlactivitylogger hcc hip_base hip_doc hip_hcc hip_samples libunwind-dev
  linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148 linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148 rocm rocm-dev rocm-device-libs
  rocm-profiler rocm-smi rocm-utils
0 upgraded, 16 newly installed, 0 to remove and 0 not upgraded.
Need to get 0 B/329 MB of archives.
After this operation, 1,985 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Selecting previously unselected package compute-firmware.
(Reading database ... 311097 files and directories currently installed.)
Preparing to unpack .../compute-firmware_1.2.557_all.deb ...
Unpacking compute-firmware (1.2.557) ...
Selecting previously unselected package libunwind-dev.
Preparing to unpack .../libunwind-dev_1.1-4.1_amd64.deb ...
Unpacking libunwind-dev (1.1-4.1) ...
Selecting previously unselected package rocm-utils.
Preparing to unpack .../rocm-utils_1.0.0_amd64.deb ...
Unpacking rocm-utils (1.0.0) ...
Selecting previously unselected package hcc.
Preparing to unpack .../hcc_1.0.17312_amd64.deb ...
Unpacking hcc (1.0.17312) ...
Selecting previously unselected package hip_base.
Preparing to unpack .../hip%5fbase_1.2.17305_amd64.deb ...
Unpacking hip_base (1.2.17305) ...
Selecting previously unselected package hip_doc.
Preparing to unpack .../hip%5fdoc_1.2.17305_amd64.deb ...
Unpacking hip_doc (1.2.17305) ...
Selecting previously unselected package hip_hcc.
Preparing to unpack .../hip%5fhcc_1.2.17305_amd64.deb ...
Unpacking hip_hcc (1.2.17305) ...
Selecting previously unselected package hip_samples.
Preparing to unpack .../hip%5fsamples_1.2.17305_amd64.deb ...
Unpacking hip_samples (1.2.17305) ...
Selecting previously unselected package linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148.
Preparing to unpack .../linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148_4.11.0-kfd-compute-rocm-rel-1.6-148-1_amd64.deb ...
Unpacking linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148 (4.11.0-kfd-compute-rocm-rel-1.6-148-1) ...
Selecting previously unselected package linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148.
Preparing to unpack .../linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148_4.11.0-kfd-compute-rocm-rel-1.6-148-1_amd64.deb ...
Unpacking linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148 (4.11.0-kfd-compute-rocm-rel-1.6-148-1) ...
Selecting previously unselected package rocm-device-libs.
Preparing to unpack .../rocm-device-libs_0.0.1_amd64.deb ...
Unpacking rocm-device-libs (0.0.1) ...
Selecting previously unselected package rocm-smi.
Preparing to unpack .../rocm-smi_1.0.0-25-gbdb99b4_amd64.deb ...
Unpacking rocm-smi (1.0.0-25-gbdb99b4) ...
Selecting previously unselected package cxlactivitylogger.
Preparing to unpack .../cxlactivitylogger_5.1.6400_amd64.deb ...
Unpacking cxlactivitylogger (5.1.6400) ...
Selecting previously unselected package rocm-profiler.
Preparing to unpack .../rocm-profiler_5.1.6400_amd64.deb ...
Unpacking rocm-profiler (5.1.6400) ...
Selecting previously unselected package rocm-dev.
Preparing to unpack .../rocm-dev_1.6.148_amd64.deb ...
Unpacking rocm-dev (1.6.148) ...
Selecting previously unselected package rocm.
Preparing to unpack .../rocm_1.6.148_amd64.deb ...
Unpacking rocm (1.6.148) ...
Processing triggers for man-db (2.7.5-1) ...
Setting up compute-firmware (1.2.557) ...
Setting up libunwind-dev (1.1-4.1) ...
Setting up rocm-utils (1.0.0) ...
Setting up hcc (1.0.17312) ...
Setting up hip_base (1.2.17305) ...
Setting up hip_doc (1.2.17305) ...
Setting up hip_hcc (1.2.17305) ...
Setting up hip_samples (1.2.17305) ...
Setting up linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148 (4.11.0-kfd-compute-rocm-rel-1.6-148-1) ...
Setting up linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148 (4.11.0-kfd-compute-rocm-rel-1.6-148-1) ...
ERROR (dkms apport): kernel package linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148 is not supported
Error! Bad return status for module build on kernel: 4.11.0-kfd-compute-rocm-rel-1.6-148 (x86_64)
Consult /var/lib/dkms/amdgpu-pro/17.30-465504/build/make.log for more information.
update-initramfs: Generating /boot/initrd.img-4.11.0-kfd-compute-rocm-rel-1.6-148
W: mdadm: /etc/mdadm/mdadm.conf defines no arrays.
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.11.0-kfd-compute-rocm-rel-1.6-148
Found initrd image: /boot/initrd.img-4.11.0-kfd-compute-rocm-rel-1.6-148
Found linux image: /boot/vmlinuz-4.10.0-33-generic
Found initrd image: /boot/initrd.img-4.10.0-33-generic
Found linux image: /boot/vmlinuz-4.4.0-87-generic
Found initrd image: /boot/initrd.img-4.4.0-87-generic
Found memtest86+ image: /memtest86+.elf
Found memtest86+ image: /memtest86+.bin
done
Setting up rocm-device-libs (0.0.1) ...
Setting up rocm-smi (1.0.0-25-gbdb99b4) ...
Setting up cxlactivitylogger (5.1.6400) ...
Setting up rocm-profiler (5.1.6400) ...
Setting up rocm-dev (1.6.148) ...
Setting up rocm (1.6.148) ...
KERNEL=="kfd", MODE="0666"
```







Log:
[make_log.zip](https://github.com/RadeonOpenCompute/ROCm/files/1279379/make_log.zip)


---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-09-06T13:34:18Z)

Did you remove the old driver first. 

Before you ran 

$wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
$sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main &#62; /etc/apt/sources.list.d/rocm.list'

$sudo apt-get update
$sudo apt-get install rocm

I just ran install this morning on Ubuntu with out issue 


---

### 评论 #2 — jedwards-AMD (2017-09-06T14:21:46Z)

From the log, it appears you are trying to install the dkms amdgpu PRO driver modules on top of the ROCm driver set. This isn't supported, and isn't required. If you want the amdgpu PRO product, use that. If you want ROCm don't install any of the amdgpu PRO software. The ROCm kernel package comes will all of the drivers required to run on the ROCm software stack.

---

### 评论 #3 — Xuno (2017-09-06T21:29:12Z)

Thanks.
After removing AMDGPU Pro ROCm re-installed ok.
But w/o AMD OpenGL, only with Mesa. 

Now back to AMDGPU-PRO Driver 17.30 with ROCm Platform 1.5  (sudo apt install -y rocm-amdgpu-pro)
and HIP (sudo apt install hcc hip_hcc).
[Release-Notes, Driver 17.30](http://support.amd.com/en-us/kb-articles/Pages/AMDGPU-PRO-Driver-for-Linux-Release-Notes.aspx)

> AMDGPU-PRO Driver 17.30 : ROCm Platform 1.5 in supported distributions (Ubuntu 16.04.3)



---
