# Cannot install on WSL

- **Issue #:** 4281
- **State:** closed
- **Created:** 2025-01-21T16:29:28Z
- **Updated:** 2025-01-27T14:48:42Z
- **Labels:** Under Investigation, ROCm 6.2.3, AMD Radeon RX 6800 XT
- **URL:** https://github.com/ROCm/ROCm/issues/4281

### Problem Description

I'm following this doc for WSL installation on a fresh WSL
https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html

When I arrive on this step

`
amdgpu-install -y --usecase=wsl,rocm --no-dkms
`

Nothing happens on the terminal and the terminal is frozen (can't CTRL + C)

The doc uses the 6.2.3 version, but I have the same issue with https://repo.radeon.com/amdgpu-install/latest/ubuntu/jammy/.

Is it the right way to install it on WSL or am I missing somethin

### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 7 5800X 8-Core Processor

### GPU

AMD Radeon RX 6800 XT

### ROCm Version

ROCm 6.2.3

### ROCm Component

_No response_

### Steps to Reproduce

```
thsauvag@Thomas-PC:~$ wget https://repo.radeon.com/amdgpu-install/6.2.3/ubuntu/jammy/amdgpu-install_6.2.60203-1_all.deb
--2025-01-21 17:09:27--  https://repo.radeon.com/amdgpu-install/6.2.3/ubuntu/jammy/amdgpu-install_6.2.60203-1_all.deb
Resolving repo.radeon.com (repo.radeon.com)... 2.22.151.132, 2.22.151.157, 2a02:26f0:9100:9::1748:f955, ...
Connecting to repo.radeon.com (repo.radeon.com)|2.22.151.132|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16932 (17K) [application/octet-stream]
Saving to: ‘amdgpu-install_6.2.60203-1_all.deb.1’

amdgpu-install_6.2.60203-1_al 100%[=================================================>]  16.54K  --.-KB/s    in 0s

2025-01-21 17:09:27 (286 MB/s) - ‘amdgpu-install_6.2.60203-1_all.deb.1’ saved [16932/16932]

thsauvag@Thomas-PC:~$ sudo apt install ./amdgpu-install_6.2.60203-1_all.deb
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'amdgpu-install' instead of './amdgpu-install_6.2.60203-1_all.deb'
The following packages were automatically installed and are no longer required:
  gir1.2-javascriptcoregtk-4.1 gir1.2-webkit2-4.1 htop libnl-3-200 libnl-genl-3-200 linux-tools-5.15.0-112
  linux-tools-5.15.0-112-generic
Use 'sudo apt autoremove' to remove them.
The following packages will be DOWNGRADED:
  amdgpu-install
0 upgraded, 0 newly installed, 1 downgraded, 0 to remove and 0 not upgraded.
Need to get 0 B/16.9 kB of archives.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 /home/thsauvag/amdgpu-install_6.2.60203-1_all.deb amdgpu-install all 6.2.60203-2044426.22.04 [16.9 kB]
dpkg: warning: downgrading amdgpu-install from 6.3.60301-2095006.22.04 to 6.2.60203-2044426.22.04
(Reading database ... 58402 files and directories currently installed.)
Preparing to unpack .../amdgpu-install_6.2.60203-1_all.deb ...
Unpacking amdgpu-install (6.2.60203-2044426.22.04) over (6.3.60301-2095006.22.04) ...
Setting up amdgpu-install (6.2.60203-2044426.22.04) ...
Installing new version of config file /etc/amdgpu-install/amdgpu-setup.conf ...
Installing new version of config file /etc/apt/sources.list.d/amdgpu.list ...
Installing new version of config file /etc/apt/sources.list.d/rocm.list ...
N: Download is performed unsandboxed as root as file '/home/thsauvag/amdgpu-install_6.2.60203-1_all.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)
thsauvag@Thomas-PC:~$ amdgpu-install -y --usecase=wsl,rocm --no-dkms
```
Then, nothing happens.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_