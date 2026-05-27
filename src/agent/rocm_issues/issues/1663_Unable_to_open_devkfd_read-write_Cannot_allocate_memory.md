# Unable to open /dev/kfd read-write: Cannot allocate memory

> **Issue #1663**
> **状态**: closed
> **创建时间**: 2022-02-03T00:34:09Z
> **更新时间**: 2022-02-07T11:13:54Z
> **关闭时间**: 2022-02-04T18:55:17Z
> **作者**: JBBIntel
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1663

## 描述

I have installed rocm on Ubuntu 20.04. I tried rocminfo, and got

amdgpu:~/amd$ sudo /opt/rocm-4.5.2/bin/rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
jbberry is member of render group

Additional info;
jbberry@ortce-amdgpu:~/amd$ dkms status
amdgpu, 5.11.32-1350682, 5.4.0-97-generic, x86_64: installed

jbberry@ortce-amdgpu:~/amd$ uname -r
5.4.0-97-generic


---

## 评论 (6 条)

### 评论 #1 — JBBIntel (2022-02-03T00:45:42Z)



Works for clinfo, but 0 devices;
jbberry@ortce-amdgpu:~/amd$ sudo /opt/rocm-4.5.2/opencl/bin/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.2 AMD-APP (3361.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               0
jbberry@ortce-amdgpu:~/amd$


---

### 评论 #2 — JBBIntel (2022-02-03T01:15:07Z)

Thanks for the quick response! But I'm not sure I understand. Are you saying I need to re-install rocm, so it will select the amdgpu for the correct kernel? Or use a different version of Ubuntu? Or what? 

---

### 评论 #3 — ROCmSupport (2022-02-03T07:22:29Z)

Thanks @JBBIntel for reaching out.
I certainly understood the problem.
I recommend to try with at least 5.8/5.9 kernels and above versions.
5.4 is very old kernel and it might not work due to compatibility issues. We have not tested too. So recommend to try with the latest kernels like 5.11 and etc(atleast 5.8/5.9 are minimum requirement).

Meanwhile can you please share the below information.
1. output of dmesg command
2. GPU details of your machine.
Thank you.

---

### 评论 #4 — JBBIntel (2022-02-03T17:04:57Z)

There are no kfd messages in dmesg. The GPU is an MI100.
I am a bit puzzled by your suggestion. I initially tried to install this on Ubuntu 21.10, which uses the 5.13 kernel. However, that installation failed. I noticed that the install page says the supported Ubuntu versions are 18.04 and 20.04.  I therefore backed off to Ubuntu 20.04, which uses the 5.4 kernel. Are you suggesting I should return to 21.10? Or somehow get a different version of 20.04, with a higher kernel version? 

---

### 评论 #5 — JBBIntel (2022-02-04T18:55:17Z)

FYI, I figured out what you meant. I was able to upgrade the kernel in Ubuntu 20.04 using the instructions here;
https://wiki.ubuntu.com/Kernel/LTSEnablementStack#Server

In particular, since my machine is a server, I did this;

 sudo apt install --install-recommends linux-generic-hwe-20.04 

and then rebooted. After that, install worked fine.

---

### 评论 #6 — ROCmSupport (2022-02-07T11:13:54Z)

Hi @JBBIntel 
Recommend to install 5.8/5.9/5.11 kernel on your Ubuntu 20.04 machine and check
or
Take the latest Ubuntu 20.04.3(which is now coming with 5.13 kernels installed) and remove 5.13 kernels using sudo apt remove linux-****-5.13.0-<press tab here> (replace **** with headers, image, modules, modules-extra) and do "update-grub" and then reboot.
After the above step, your machine will have 5.13 removed and now install rocm, it works perfect.
Hope it helps.
Thank you.

---
