# Unable to install ROCm 1.8.2 on CentOS 7.4 due to dependency on libOpenCL.so.1

> **Issue #472**
> **状态**: closed
> **创建时间**: 2018-07-27T00:22:01Z
> **更新时间**: 2018-08-31T00:12:20Z
> **关闭时间**: 2018-08-30T22:19:59Z
> **作者**: BryantLam
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/472

## 描述

Clean system with CentOS 7.4 and `kernel-headers  kernel-devel  devtoolset-7  dkms`.

```
# yum install rocm-dkms
...
---> Package rocm-dkms.x86_64 0:1.8.192-1 will be installed
...
--> Running transaction check
---> Package rocm-opencl-devel.x86_64 0:1.2.0-2018071635 will be installed
--> Processing Dependency: libOpenCL.so.1()(64bit) for package: rocm-opencl-devel-1.2.0-2018071635.x86_64
--> Finished Dependency Resolution
Error: Package: rocm-opencl-devel-1.2.0-2018071635.x86_64 (rocm)
           Requires: libOpenCL.so.1()(64bit)
```

Running `yum whatprovides libOpenCL.so.1` shows `rocm-opencl`, which I was able to install successfully, but I still cannot resolve the dependency error for `rocm-opencl-devel`.

---

## 评论 (5 条)

### 评论 #1 — jlgreathouse (2018-08-30T21:53:49Z)

I am unable to reproduce this on a fresh CentOS 7.4 (1708) installation.

Performing the following installs ROCm for me:
```shell
sudo yum update # Update packages, install a kernel that has kernel headers in the repos
sudo reboot
```
```shell
sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum install centos-release-scl
sudo yum install devtoolset-7
scl enable devtoolset-7 bash
sudo yum install -y dkms kernel-headers-`uname -r`
sudo echo [ROCm] | sudo tee /etc/yum.repos.d/rocm.repo 
sudo echo name=ROCm | sudo tee /etc/yum.repos.d/rocm.repo 
sudo echo baseurl=http://repo.radeon.com/rocm/yum/rpm | sudo tee /etc/yum.repos.d/rocm.repo 
sudo echo enabled=1 | sudo tee /etc/yum.repos.d/rocm.repo 
sudo echo gpgcheck=0 | sudo tee /etc/yum.repos.d/rocm.repo 
sudo yum install rocm-dkms
sudo usermod -a -G video $LOGNAME 
sudo reboot
```

---

### 评论 #2 — BryantLam (2018-08-30T22:19:59Z)

If you *just* tried these steps, it looks like ROCm was updated two days ago.
http://repo.radeon.com/rocm/yum/rpm/ with timestamp 28-Aug-2018 22:09

Most of the files look like they didn't change, but these two definitely did:
```
rocm-opencl-1.2.0-2018082827.x86_64.rpm            28-Aug-2018 22:06            45309944
rocm-opencl-devel-1.2.0-2018082827.x86_64.rpm      28-Aug-2018 22:06            18813560
```

And probably this package and other packages too:
```
rocm-dkms-1.8.199-Linux.rpm                        28-Aug-2018 22:06                2868
```
because that package differs from my package in the original post:
```
---> Package rocm-dkms.x86_64 0:1.8.192-1 will be installed
```

This problem might only be reproducible using the RPMs from the ROCm 1.8.2 archive:
http://repo.radeon.com/rocm/archive/yum_1.8.2.tar.bz2

For that archive, I worked around this problem by force-installing/ignoring the dependency:
```
sudo yum install rocm-opencl
sudo rpm -ivh --nodeps rocm-opencl-devel*.rpm
sudo yum install rocm-dkms
```

I don't have a problem with this issue anymore and it sounds like it's been fixed, so I'll close it out. I would, however, like some QA for posted releases in http://repo.radeon.com/rocm/archive/.

---

### 评论 #3 — jlgreathouse (2018-08-30T23:51:07Z)

I don't believe anything meaningful changed in those packages as of ROCm 1.8.3 -- the primary update was to the DKMS driver package to fix #510. We updated these packages as part of our procedure of making a ROCm point release.

Downloading the ROCm 1.8.2 RPM files directly from the repo archive, I see the following when attempting to manually install rocm-opencl-devel:
```
$ sudo yum install ./rocm-opencl-devel-1.2.0-2018071635.x86_64.rpm
Loaded plugins: fastestmirror
Examining ./rocm-opencl-devel-1.2.0-2018071635.x86_64.rpm: rocm-opencl-devel-1.2.0-2018071635.x86_64
Marking ./rocm-opencl-devel-1.2.0-2018071635.x86_64.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package rocm-opencl-devel.x86_64 0:1.2.0-2018071635 will be installed
--> Processing Dependency: libOpenCL.so.1()(64bit) for package: rocm-opencl-devel-1.2.0-2018071635.x86_64
Loading mirror speeds from cached hostfile
 * base: mirrors.usinternet.com
 * epel: mirror.compevo.com
 * extras: mirror.oss.ou.edu
 * updates: mirror.web-ster.com
--> Running transaction check
---> Package ocl-icd.x86_64 0:2.2.12-1.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================
 Package                        Arch                Version                          Repository                                               Size
===================================================================================================================================================
Installing:
 rocm-opencl-devel              x86_64              1.2.0-2018071635                 /rocm-opencl-devel-1.2.0-2018071635.x86_64               59 M
Installing for dependencies:
 ocl-icd                        x86_64              2.2.12-1.el7                     epel                                                     43 k

Transaction Summary
===================================================================================================================================================
Install  1 Package (+1 Dependent package)

Total size: 59 M
Total download size: 43 k
Installed size: 59 M
Is this ok [y/d/N]:
```

I think this means we have proper dependency information. `libOpenCL.so.1` is provided by the package `ocl-icd` in the epel repositories. Are you sure you added epel-release-latest-7 to your list of repositories?
`sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm`



---

### 评论 #4 — BryantLam (2018-08-31T00:07:21Z)

@jlgreathouse --  Thanks! This led me to figure out what the actual problem was -- the EPEL repo on my system was disabled by default. Once it was enabled, I could pull the dependency in. Much appreciated for your time.

---

### 评论 #5 — jlgreathouse (2018-08-31T00:12:20Z)

Glad everything is in order now. :)

---
