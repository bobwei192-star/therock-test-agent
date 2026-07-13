# Problems with installation on 16.04 (toshiba sat with r7 260)

- **Issue #:** 493
- **State:** closed
- **Created:** 2018-08-07T07:34:31Z
- **Updated:** 2021-06-21T15:54:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/493

I have followed the installation instructions several times, from scratch, but still the end result is the same:
1. installed 16.04
`m@dl1:~$ uname -a
Linux dl1 4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:23:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```
`m@dl1:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.4 LTS
Release:	16.04
Codename:	xenial
```

2. did the next part (not including the log, nothing special)
```
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot
```
3. added the repo, still not very interesting
```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
sudo apt update
```
4. installed rocm-dkms, still uneventfull
```
sudo apt install rocm-dkms
```
5.  added video group
`sudo usermod -a -G video $LOGNAME `
and rebooted

6. Now things start to squeak...
```
m@dl1:~$ rocminfo
rocminfo: command not found
```
ok, no big deal, lets find it:
```
m@dl1:~$ sudo /opt/rocm/bin/rocminfo 
[sudo] password for m: 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104
m@dl1:~$ 
```
and:
```
m@dl1:~$ clinfo
The program 'clinfo' is currently not installed. You can install it by typing:
sudo apt install clinfo
```
no big deal, lets install it
```
m@dl1:~$ sudo clinfo
Number of platforms                               0
```

read the faq:
```
m@dl1:~$ dmesg | grep kfd
[    1.231543] kfd kfd: Initialized module
m@dl1:~$ sudo apt-get autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
m@dl1:~$ dmesg | grep amdgpu
[    1.226981] [drm] amdgpu kernel modesetting enabled.
[    1.231685] amdgpu 0000:09:00.0: enabling device (0100 -> 0103)
[    2.153698] [drm] add ip block number 3 <amdgpu_powerplay>
[    2.161257] amdgpu 0000:09:00.0: VRAM: 2048M 0x000000F400000000 - 0x000000F47FFFFFFF (2048M used)
[    2.161259] amdgpu 0000:09:00.0: GTT: 256M 0x0000000000000000 - 0x000000000FFFFFFF
[    2.161340] [drm] amdgpu: 2048M of VRAM memory ready
[    2.161341] [drm] amdgpu: 7902M of GTT memory ready.
[    2.165592] amdgpu: [powerplay] can't get the mac of 5
[    2.167168] amdgpu: [powerplay] VBIOS did not find boot engine clock value in dependency table. Using Memory DPM level 0!
[    7.818082] amdgpu: [powerplay] VI should always have 2 performance levels
[    7.864713] amdgpu 0000:09:00.0: GPU pci config reset
```

So, I really don't know what to do now. this is a fresh install, ,and I followed the readme to the letter.
Any help will be greatly appreciated