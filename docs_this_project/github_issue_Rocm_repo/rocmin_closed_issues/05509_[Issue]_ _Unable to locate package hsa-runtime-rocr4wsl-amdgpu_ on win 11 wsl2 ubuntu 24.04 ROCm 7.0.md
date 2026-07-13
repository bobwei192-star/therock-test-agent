# [Issue]: 'Unable to locate package hsa-runtime-rocr4wsl-amdgpu' on win 11 wsl2 ubuntu 24.04 ROCm 7.0.2 on ryzen ai max+ 395

- **Issue #:** 5509
- **State:** closed
- **Created:** 2025-10-12T10:02:40Z
- **Updated:** 2025-10-22T20:05:29Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5509

### Problem Description

Host:
```
OS: Windows 11 25H2 10.0.26200
CPU: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
GPU: AMD Radeon(TM) 8060S Graphics
```
wsl2:
```
OS: Ubuntu 24.04.3 LTS (Noble Numbat)
CPU: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
uname: Linux u24 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
```
after installation of https://repo.radeon.com/amdgpu-install/7.0.2/ubuntu/noble/amdgpu-install_7.0.2.70002-1_all.deb amdgpu-install failing:
```
$ sudo amdgpu-install -y --usecase=wsl,rocm --no-dkms
Hit:1 http://security.ubuntu.com/ubuntu noble-security InRelease
Hit:2 https://download.docker.com/linux/ubuntu noble InRelease
Hit:3 https://repo.radeon.com/amdgpu/30.10.2/ubuntu noble InRelease
Hit:4 https://repo.radeon.com/rocm/apt/7.0.2 noble InRelease
Hit:5 http://archive.ubuntu.com/ubuntu noble InRelease
Get:6 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
Hit:7 https://repo.radeon.com/graphics/7.0.2/ubuntu noble InRelease
Hit:8 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:9 https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu noble InRelease
Fetched 126 kB in 0s (293 kB/s)
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package hsa-runtime-rocr4wsl-amdgpu
E: Unable to locate package hsa-runtime-rocr4wsl-amdgpu
```
Similar issue for ROCm 6 suggest manual download and install of hsa-runtime-rocr4wsl-amdgpu, but I don't see that package in ROCm 7 repos, only in ROCm 6

### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat) in wsl2 vm on Windows 11 25H2 10.0.26200

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD Radeon(TM) 8060S Graphics

### ROCm Version

ROCm 7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

```
wget https://repo.radeon.com/amdgpu-install/7.0.2/ubuntu/noble/amdgpu-install_7.0.2.70002-1_all.deb
sudo apt-get install -y ./amdgpu-install_7.0.2.70002-1_all.deb
sudo apt update
sudo apt full-upgrade -y
sudo amdgpu-install -y --usecase=wsl,rocm --no-dkms
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
$ /opt/rocm/bin/rocminfo --support
WSL environment detected.
hsa api call failure at: /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/rocminfo/rocminfo.cc:1304
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
I'm getting the same error from rocminfo built from https://github.com/ROCm/TheRock.git (cmake -DTHEROCK_AMDGPU_TARGETS=gfx1151) and downloaded from https://therock-nightly-tarball.s3.amazonaws.com/therock-dist-linux-gfx1151-7.10.0a20251012.tar.gz

### Additional Information

```
$ sudo modprobe vgem
$ sudo ls -la /dev/dri
total 0
drwxr-xr-x  3 root root        100 Oct 12 09:43 .
drwxr-xr-x 16 root root       3880 Oct 12 09:43 ..
drwxr-xr-x  2 root root         80 Oct 12 09:43 by-path
crw-rw----  1 root video  226,   0 Oct 12 09:43 card0
crw-rw----  1 root render 226, 128 Oct 12 09:43 renderD128
```