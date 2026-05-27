# The directory profiler/bin doesn't exist in the folder /opt/rocm

> **Issue #1285**
> **状态**: closed
> **创建时间**: 2020-11-12T18:27:54Z
> **更新时间**: 2020-11-16T07:01:58Z
> **关闭时间**: 2020-11-12T21:32:42Z
> **作者**: YuriyTigiev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1285

## 描述

I have installed ROCM  by instruction from https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu
After installation both utilits works properly 
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo

in the documentation one of the step is add a PATH parameter

`echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin' | sudo tee -a /etc/profile.d/rocm.sh`

but directory /opt/rocm/profiler/bin doesn't exist. Is it ok ?

```
(base) yuriy@yuriy-System-Product-Name:~$ cd /opt/rocm 
(base) yuriy@yuriy-System-Product-Name:/opt/rocm$ ls -l 
total 36
drwxr-xr-x 3 root root 4096 ნოე 12 21:45 amdgcn
drwxr-xr-x 2 root root 4096 ნოე 12 21:45 bin
drwxr-xr-x 4 root root 4096 ნოე 12 21:45 hsa
drwxr-xr-x 3 root root 4096 ნოე 12 21:45 include
drwxr-xr-x 3 root root 4096 ნოე 12 22:04 lib
drwxr-xr-x 4 root root 4096 ნოე 12 21:45 oam
drwxr-xr-x 5 root root 4096 ნოე 12 21:45 opencl
drwxr-xr-x 6 root root 4096 ნოე 12 21:45 rocm_smi
drwxr-xr-x 9 root root 4096 ნოე 12 21:45 share
(base) yuriy@yuriy-System-Product-Name:/opt/rocm$ 
```



---

## 评论 (13 条)

### 评论 #1 — Rmalavally (2020-11-12T21:32:42Z)

Thank you for reaching out. The issue is now resolved, and the directory is corrected at:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu

AMD ROCm Documentation


---

### 评论 #2 — YuriyTigiev (2020-11-13T06:41:53Z)

> Thank you for reaching out. The issue is now resolved, and the directory is corrected at:
> 
> https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu
> 
> AMD ROCm Documentation

But directory `/opt/rocm`  also doesn't contain the director `rocprofiler/bin`. See a list of directories below.
Why?    Which commands or processes should create this directory?

(base) yuriy@yuriy-System-Product-Name:/opt/rocm$ ls -l 
total 36
drwxr-xr-x 3 root root 4096 ნოე 12 21:45 amdgcn
drwxr-xr-x 2 root root 4096 ნოე 12 21:45 bin
drwxr-xr-x 4 root root 4096 ნოე 12 21:45 hsa
drwxr-xr-x 3 root root 4096 ნოე 12 21:45 include
drwxr-xr-x 3 root root 4096 ნოე 12 22:04 lib
drwxr-xr-x 4 root root 4096 ნოე 12 21:45 oam
drwxr-xr-x 5 root root 4096 ნოე 12 21:45 opencl
drwxr-xr-x 6 root root 4096 ნოე 12 21:45 rocm_smi
drwxr-xr-x 9 root root 4096 ნოე 12 21:45 share
(base) yuriy@yuriy-System-Product-Name:/opt/rocm$ 



---

### 评论 #3 — rkothako (2020-11-13T06:43:26Z)

Thanks @YuriyTigiev 
Actually rocprofiler should also be under /opt/rocm.

Can you please share steps you followed to install ROCm.
Thank you.

---

### 评论 #4 — YuriyTigiev (2020-11-13T06:44:25Z)

> Thanks @YuriyTigiev
> Actually rocprofiler should also be under /opt/rocm.
> 
> Can you please share steps you followed to install ROCm.
> Thank you.

Step by step for Ubuntu 
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu

---

### 评论 #5 — rkothako (2020-11-13T06:51:50Z)

Thanks.
Looks like your installation did not go well. There might be problem with uninstallation of old rocm (or) issue with installation of new rocm.

Below installation steps should create rocprofiler also.
1. sudo apt update
2. sudo apt dist-upgrade
3. sudo apt install libnuma-dev
4. wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
5. echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
6. sudo apt update
7. sudo apt install rocm-dkms && sudo reboot

In my case, all folders are visible.

master@master:/opt/rocm$ ls
amdgcn  bin  hip  hsa  hsa-amd-aqlprofile  include  lib  llvm  oam  opencl  rocm_smi  rocprofiler  roctracer  share


---

### 评论 #6 — YuriyTigiev (2020-11-13T07:13:28Z)

I did but without changes. 
Please see my steps and results.

```
(base) yuriy@yuriy-System-Product-Name:~$ sudo apt update
[sudo] password for yuriy: 
Hit:1 http://dl.google.com/linux/chrome/deb stable InRelease
Hit:2 http://us.archive.ubuntu.com/ubuntu focal InRelease                      
Get:3 http://repo.radeon.com/rocm/apt/debian xenial InRelease [1.817 B]
Hit:4 http://archive.canonical.com/ubuntu focal InRelease                      
Hit:5 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:6 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease
Hit:7 http://us.archive.ubuntu.com/ubuntu focal-security InRelease
Fetched 1.817 B in 1s (1.813 B/s)
Reading package lists... Done
Building dependency tree       
Reading state information... Done
All packages are up to date.
(base) yuriy@yuriy-System-Product-Name:~$ sudo apt dist-upgrade
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
(base) yuriy@yuriy-System-Product-Name:~$ sudo apt install libnuma-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libnuma-dev is already the newest version (2.0.12-1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
(base) yuriy@yuriy-System-Product-Name:~$ wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
OK
(base) yuriy@yuriy-System-Product-Name:~$ echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main
(base) yuriy@yuriy-System-Product-Name:~$ sudo apt update
Hit:1 http://dl.google.com/linux/chrome/deb stable InRelease
Hit:2 http://archive.canonical.com/ubuntu focal InRelease                      
Hit:3 http://us.archive.ubuntu.com/ubuntu focal InRelease                      
Hit:4 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease     
Hit:5 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease
Get:6 https://repo.radeon.com/rocm/apt/debian xenial InRelease [1.817 B]
Hit:7 http://us.archive.ubuntu.com/ubuntu focal-security InRelease
Fetched 1.817 B in 1s (1.564 B/s)
Reading package lists... Done
Building dependency tree       
Reading state information... Done
All packages are up to date.
(base) yuriy@yuriy-System-Product-Name:~$ sudo apt install rocm-dkms 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-dkms is already the newest version (3.9.1.30901-19).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.


After restart 


(base) yuriy@yuriy-System-Product-Name:/opt/rocm$ ls -l 
total 88
drwxr-xr-x  3 root root 4096 ნოე 12 21:45 amdgcn
drwxr-xr-x  2 root root 4096 ნოე 12 21:45 bin
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 hipblas
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 hipcub
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 hiprand
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 hipsparse
drwxr-xr-x  4 root root 4096 ნოე 12 21:45 hsa
drwxr-xr-x 11 root root 4096 ნოე 12 23:11 include
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 lib
drwxr-xr-x  6 root root 4096 ნოე 12 23:11 miopen
drwxr-xr-x  4 root root 4096 ნოე 12 21:45 oam
drwxr-xr-x  5 root root 4096 ნოე 12 21:45 opencl
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocalution
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocblas
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocfft
drwxr-xr-x  6 root root 4096 ნოე 12 21:45 rocm_smi
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocprim
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocrand
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocsolver
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocsparse
drwxr-xr-x  4 root root 4096 ნოე 12 23:11 rocthrust
drwxr-xr-x 10 root root 4096 ნოე 12 23:11 share

```

---

### 评论 #7 — rkothako (2020-11-13T07:33:14Z)

Looks like your old ROCm installation did not go well before installing this new ROCm.
Now you tried installing on top of existing ROCm, can not do any upgrade and so it shows the same.
_(base) yuriy@yuriy-System-Product-Name:~$ sudo apt install rocm-dkms 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-dkms is already the newest version (3.9.1.30901-19).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded._

Have 2 ways.
way 1. Uninstall every package along with rocm-dkms using sudo apt autoremove rocm-dkms followed by all other packages, as shown below.
1. Remove all libs first before installing complete rocm.
sudo apt autoremove rocm-libs 
2. Remove rocm 
sudo apt autoremove rocm-dkms
3. Remove any other available packages
Check and remove one by one like..
sudo dpkg -l | grep <pkgname>
sudo apt remove <pkgname>

Make sure to remove all pkgs and also /opt/rocm is clean.
Now install rocm again freshly like suod apt install rocm-dkms --> should install all packages

way 2: You can install all missing/reuired packages one by one
sudo apt install rocprofiler-dev roctracer-dev hip-samples hip-doc hip-base hip-rocclr llvm-amdgpu hsa-amd-aqlprofile


---

### 评论 #8 — YuriyTigiev (2020-11-13T10:57:33Z)

> Looks like your old ROCm installation did not go well before installing this new ROCm.
> Now you tried installing on top of existing ROCm, can not do any upgrade and so it shows the same.
> _(base) yuriy@yuriy-System-Product-Name:~$ sudo apt install rocm-dkms Reading package lists... Done Building dependency tree Reading state information... Done rocm-dkms is already the newest version (3.9.1.30901-19). 0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded._
> 
> Have 2 ways.
> way 1. Uninstall every package along with rocm-dkms using sudo apt autoremove rocm-dkms followed by all other packages, as shown below.
> 
>     1. Remove all libs first before installing complete rocm.
>        sudo apt autoremove rocm-libs
> 
>     2. Remove rocm
>        sudo apt autoremove rocm-dkms
> 
>     3. Remove any other available packages
>        Check and remove one by one like..
>        sudo dpkg -l | grep 
>        sudo apt remove
> 
> 
> Make sure to remove all pkgs and also /opt/rocm is clean.
> Now install rocm again freshly like suod apt install rocm-dkms --> should install all packages
> 
> way 2: You can install all missing/reuired packages one by one
> sudo apt install rocprofiler-dev roctracer-dev hip-samples hip-doc hip-base hip-rocclr llvm-amdgpu hsa-amd-aqlprofile

I have reinstalled Ubuntu and ROCM and now the folder exists

---

### 评论 #9 — rkothako (2020-11-13T11:02:21Z)

Thanks @YuriyTigiev Good to know.
You can log any new issues in future.
Thank you.

---

### 评论 #10 — YuriyTigiev (2020-11-14T05:59:14Z)

> Thanks.
> Looks like your installation did not go well. There might be problem with uninstallation of old rocm (or) issue with installation of new rocm.
> 
> Below installation steps should create rocprofiler also.
> 
>     1. sudo apt update
> 
>     2. sudo apt dist-upgrade
> 
>     3. sudo apt install libnuma-dev
> 
>     4. wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
> 
>     5. echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
> 
>     6. sudo apt update
> 
>     7. sudo apt install rocm-dkms && sudo reboot
> 
> 
> In my case, all folders are visible.
> 
> master@master:/opt/rocm$ ls
> amdgcn bin hip hsa hsa-amd-aqlprofile include lib llvm oam opencl rocm_smi rocprofiler roctracer share

Is this the provided list of command enough for install rocm library? The current list slightly different then list of command in the documentation. 

---

### 评论 #11 — rkothako (2020-11-16T06:13:13Z)

> 
> 
> > Thanks.
> > Looks like your installation did not go well. There might be problem with uninstallation of old rocm (or) issue with installation of new rocm.
> > Below installation steps should create rocprofiler also.
> > ```
> > 1. sudo apt update
> > 
> > 2. sudo apt dist-upgrade
> > 
> > 3. sudo apt install libnuma-dev
> > 
> > 4. wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
> > 
> > 5. echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
> > 
> > 6. sudo apt update
> > 
> > 7. sudo apt install rocm-dkms && sudo reboot
> > ```
> > 
> > 
> > In my case, all folders are visible.
> > master@master:/opt/rocm$ ls
> > amdgcn bin hip hsa hsa-amd-aqlprofile include lib llvm oam opencl rocm_smi rocprofiler roctracer share
> 
> Is this the provided list of command enough for install rocm library? The current list slightly different then list of command in the documentation.

I copied all commands from documentation only.
The last command (sudo apt install rocm-dkms) enables basic rocm with all compilers and runtimes.
If you wish to have some rocm libraries also on top of this, do as **sudo apt install rocm-libs rccl**

---

### 评论 #12 — YuriyTigiev (2020-11-16T06:23:18Z)

You didn't use staps 5,6 from the documentation. Are they mandatory?

```
sudo usermod -a -G video $LOGNAME
sudo usermod -a -G render $LOGNAME

echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=render' | sudo tee -a /etc/adduser.conf
```

---

### 评论 #13 — rkothako (2020-11-16T07:01:58Z)

These are needed only one time after OS is ready.

---
