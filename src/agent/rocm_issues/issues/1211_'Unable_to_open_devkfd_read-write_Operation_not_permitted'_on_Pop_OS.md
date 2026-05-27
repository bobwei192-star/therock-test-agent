# 'Unable to open /dev/kfd read-write: Operation not permitted' on Pop OS

> **Issue #1211**
> **状态**: closed
> **创建时间**: 2020-09-02T00:42:50Z
> **更新时间**: 2024-07-26T00:20:57Z
> **关闭时间**: 2021-01-05T07:45:20Z
> **作者**: Maculele
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1211

## 描述

Hello,

I have installed ROCm on Pop OS, but when I attempt to ~$ rocminfo i get Unable to open /dev/kfd read-write: Operation not permitted and it states that I am a member of render group

I am running Pop!_OS 20.04 LTS

---

## 评论 (13 条)

### 评论 #1 — xuhuisheng (2020-09-02T02:40:03Z)

The device /dev/kfd need video or render group, using `ls -l /dev/kfd` to check the device group, and using `groups` to check the current login user group, if not matched, do `sudo usermod -a -G video $LOGNAME`


---

### 评论 #2 — Maculele (2020-09-02T06:01:41Z)

I am still having no luck. ls -l /dev/kfd gives this message:
> crw-rw----` 1 root render 238, 0 Sep  2 15:45 /dev/kfd

Groups says:  has my user name then   _adm sudo video render libvirt_

And just to be sure I re ran sudo usermod -a -G video $LOGNAME  but it did not help

I also noticed that when I ran '~$ sudo apt upgrade && install'  I got the following message right at the end

Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)





---

### 评论 #3 — krishoza (2020-10-21T17:45:15Z)

@xuhuisheng could this launch be failing because the owner of the file `/dev/kfd` is root and not the actual user on OS.

---

### 评论 #4 — ROCmSupport (2020-12-16T05:43:15Z)

Hi @Maculele 
Thanks for reaching out.
Recommend to uninstall ROCm completely and do a fresh and clean install of the latest ROCm 3.10.
Please share an update once done.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-01-05T07:45:20Z)

POP OS is not officially supported with ROCm.
Anyway, requesting user to try with the latest ROCm 4.0.
Thank you.

---

### 评论 #6 — MOLOjl (2021-12-23T08:28:59Z)

try this:
```shell
sudo usermod -a -G video $LOGNAME
sudo usermod -a -G render $LOGNAME
sudo reboot
```

---

### 评论 #7 — MOLOjl (2021-12-23T08:30:50Z)

@ROCmSupport 
you should mention this in your [guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#ubuntu-18-04)

---

### 评论 #8 — ROCmSupport (2021-12-23T09:13:07Z)

Hi @MOLOjl 
We have it already @ https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#setting-permissions-for-groups
Thank you.

---

### 评论 #9 — krishoza (2021-12-23T10:08:29Z)

> try this:
> 
> ```shell
> sudo usermod -a -G video $LOGNAME
> sudo usermod -a -G render $LOGNAME
> sudo reboot
> ```

@MOLOjl my user was already in the above mentioned group since this is one of prerequisites to install ROCm. 

---

### 评论 #10 — luciddream-tsin (2022-10-28T12:05:21Z)

@MOLOjl  thanks,  the reboot is very important for me!!

---

### 评论 #11 — QazCetelic (2024-02-28T09:01:20Z)

> Hi @MOLOjl We have it already @ https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#setting-permissions-for-groups Thank you.

@ROCmSupport This link gives a 404.

> > try this:
> > ```shell
> > sudo usermod -a -G video $LOGNAME
> > sudo usermod -a -G render $LOGNAME
> > sudo reboot
> > ```
> 
> @MOLOjl my user was already in the above mentioned group since this is one of prerequisites to install ROCm.

I'm getting the same error, even after adding myself to the group and rebooting.
I'm using openSUSE Tumbleweed 20240222 with kernel 6.7.5-1-default (64-bit), X11, a RX 6600 XT, and I am running it in an Ubuntu container.

Strangely, I'm not able to view the info from `rocminfo`
```
sudo rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Permission denied
user is not member of "nogroup" group, the default DRM access group. Users must be a member of the "nogroup" group or another DRM access group in order for ROCm applications to run successfully.
```

EDIT:
It seems like `/dev/kfd` isn't being passed through. The container sees a file owned by `nobody` and the group `nogroup`. The file on the host system is owned by `root` and the group `render`. I'll try again with a bind.

---

### 评论 #12 — fwdekker (2024-03-02T21:16:57Z)

@QazCetelic I had the same issue when I was using `podman` instead of `sudo docker`. I resolved the issue by moving the image to the `root` user and launching with `sudo podman`. (You can transfer the image by first exporting with `podman save -o image.tar localhost/rocm/rocm-terminal-latest`, and then importing with `sudo podman load -i image.tar`.) After that, `sudo rocminfo` worked fine. I also got `rocminfo` (without `sudo`) working by running `sudo podman` with the additional option `--group-add 107` (which corresponds to the `render` group; using `--group-add render` didn't work).

---

### 评论 #13 — jiapei100 (2024-07-26T00:17:25Z)

I got the same issue:

1. I have a `AMD Radeon RX 580 GPU`
BTW, does **ROCM** support this old AMD GPU???

```zsh
➜  ~ lspci -nnk | grep -A3 -i vga
01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] [1002:67df] (rev e7)
	Subsystem: XFX Pine Group Inc. Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] [1682:c580]
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```

3. However, the device is **NOT** even able to be detected.

```
➜  ~ sudo clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3614.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 0

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   
  clCreateContext(NULL, ...) [default]            No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  No devices found in platform

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.11
  ICD loader Profile                              OpenCL 2.1
```

4. And, `lsmod | grep kfd` replied me **NOTHING**
```zsh
➜  ~ lsmod | grep kfd
```

Can anybody please give me a hand?

My system configuration:
```zsh
➜  ~ neofetch
            .-/+oossssoo+/-.               lvision@lvision-DX4860 
        `:+ssssssssssssssssss+:`           ---------------------- 
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 20.04.6 LTS x86_64 
    .ossssssssssssssssssdMMMNysssso.       Host: MZ-B75-S 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.15.0-117-generic 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 15 hours, 30 mins 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 2038 (dpkg), 13 (snap) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: zsh 5.8 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Resolution: 1360x768 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Terminal: /dev/pts/0 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: Intel i7-3770 (8) @ 3.900GHz 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   GPU: AMD ATI Radeon RX 470/480/570/570X/580/580X/590 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Memory: 1360MiB / 32050MiB 
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/
  +sssssssssdmydMMMMMMMMddddyssssssss+                             
   /ssssssssssshdmNNNNmyNMMMMhssssss/                              
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.
```

Cheers

---
