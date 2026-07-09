# [Issue]: amdgpu-install failed on Ubuntu 24.04.4 LTS because of missing Release file

- **Issue #:** 5968
- **State:** closed
- **Created:** 2026-02-15T15:20:31Z
- **Updated:** 2026-02-23T15:08:01Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5968

### Problem Description

Installing amdgpu-install_7.2.70200-1_all.deb works on my Ubuntu 24.04.4 LTS, but running amdgpu-install failes because of the repository 'https://repo.radeon.com/amdgpu/7.2/ubuntu noble Release' does not have a Release file.

### Operating System

24.04.4 LTS (Noble Numbat)

### CPU

AMD Ryzen 9 5900X 12-Core Processor

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 7.2

### ROCm Component

_No response_

### Steps to Reproduce

First I run: (based on https://github.com/ROCm/ROCm/issues/5881#issuecomment-3786689561)
```
sudo amdgpu-install --uninstall --rocmrelease=all
sudo apt purge amdgpu-install
sudo apt autoremove
```
Then I reboot.

Then I verify I do not have any old releases or repos laying around:
```
$ sudo grep amdgpu /etc/apt/sources.list /etc/apt/sources.list.d/*
# Returns nothing

$ sudo grep rocm /etc/apt/sources.list /etc/apt/sources.list.d/*
# Returns nothing

$ dpkg -l | grep amdgpu
ii  libdrm-amdgpu1:amd64                           2.4.125-1ubuntu0.1~24.04.1               amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm-amdgpu1:i386                            2.4.125-1ubuntu0.1~24.04.1               i386         Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  xserver-xorg-video-amdgpu                      23.0.0-1ubuntu0.24.04.1                  amd64        X.Org X server -- AMDGPU display driver

$ dpkg -l | grep rocm
# Returns nothing
```
Then I try to install, where it fails:
```
$ sudo dpkg -i ./amdgpu-install_7.2.70200-1_all.deb
Selecting previously unselected package amdgpu-install.
(Reading database ... 498529 files and directories currently installed.)
Preparing to unpack .../amdgpu-install_7.2.70200-1_all.deb ...
Unpacking amdgpu-install (30.30.0.0.30300000-2278356.24.04) ...
Setting up amdgpu-install (30.30.0.0.30300000-2278356.24.04) ...

$ sudo amdgpu-install --usecase=graphics,opencl --accept-eula
Hit:1 http://no.archive.ubuntu.com/ubuntu noble InRelease
Hit:2 http://no.archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:3 http://no.archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu noble-security InRelease
Hit:5 https://repo.jotta.cloud/debian debian InRelease
Hit:6 https://deb.nodesource.com/node_22.x nodistro InRelease
Hit:7 http://download.opensuse.org/repositories/graphics:/darktable/xUbuntu_24.04  InRelease
Hit:8 http://linux.dropbox.com/ubuntu noble InRelease
Ign:9 https://repo.radeon.com/amdgpu/7.2/ubuntu noble InRelease
Hit:10 https://repo.radeon.com/amdgpu/30.30/ubuntu noble InRelease
Get:11 https://repo.radeon.com/rocm/apt/7.2 noble InRelease [2 603 B]
Get:12 https://repo.radeon.com/graphics/7.2/ubuntu noble InRelease [3 192 B]
Hit:13 https://ppa.launchpadcontent.net/mozillateam/ppa/ubuntu noble InRelease
Hit:14 https://ppa.launchpadcontent.net/obsproject/obs-studio/ubuntu noble InRelease
Err:15 https://repo.radeon.com/amdgpu/7.2/ubuntu noble Release
  404  Not Found [IP: 2a02:26f0:a300::1721:7773 443]
Get:16 https://repo.radeon.com/rocm/apt/7.2 noble/main amd64 Packages [60,9 kB]
Get:17 https://repo.radeon.com/graphics/7.2/ubuntu noble/main i386 Packages [8 849 B]
Get:18 https://repo.radeon.com/graphics/7.2/ubuntu noble/main amd64 Packages [10,6 kB]
Reading package lists... Done
E: The repository 'https://repo.radeon.com/amdgpu/7.2/ubuntu noble Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_