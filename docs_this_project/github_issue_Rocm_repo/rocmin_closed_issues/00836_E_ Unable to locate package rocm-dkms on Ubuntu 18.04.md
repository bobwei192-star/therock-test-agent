# E: Unable to locate package rocm-dkms on Ubuntu 18.04

- **Issue #:** 836
- **State:** closed
- **Created:** 2019-07-09T00:18:01Z
- **Updated:** 2023-07-29T20:30:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/836

So i followed the offical how-to, but failed already during installation:
```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
OK
```
```
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
```
```
sudo apt update
Hit:1 http://de.archive.ubuntu.com/ubuntu bionic InRelease
Hit:2 http://de.archive.ubuntu.com/ubuntu bionic-updates InRelease                                                               
Hit:3 http://de.archive.ubuntu.com/ubuntu bionic-backports InRelease                                                             
Hit:4 http://security.ubuntu.com/ubuntu bionic-security InRelease                                                              
Ign:5 http://repo.radeon.com/rocm/apt/debian xenial InRelease           
Ign:6 http://dl.google.com/linux/chrome/deb stable InRelease                                      
Err:7 http://repo.radeon.com/rocm/apt/debian xenial Release                                       
  404  Not Found [IP: 13.82.220.49 80]
Hit:8 http://dl.google.com/linux/chrome/deb stable Release
Reading package lists... Done                      
N: Ignoring file 'rocm' in directory '/etc/apt/sources.list.d/' as it has no filename extension
E: The repository 'http://repo.radeon.com/rocm/apt/debian xenial Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```
```
sudo apt-get install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
N: Ignoring file 'rocm' in directory '/etc/apt/sources.list.d/' as it has no filename extension
E: Unable to locate package rocm-dkms
```
I have new clean installation of Ubuntu 18.04.
