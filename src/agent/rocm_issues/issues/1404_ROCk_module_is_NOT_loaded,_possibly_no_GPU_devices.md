# ROCk module is NOT loaded, possibly no GPU devices

> **Issue #1404**
> **状态**: closed
> **创建时间**: 2021-03-12T08:33:24Z
> **更新时间**: 2024-01-23T09:48:20Z
> **关闭时间**: 2021-05-11T03:14:14Z
> **作者**: dshm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1404

## 描述

I tried to install rocm packages in my machine，which is Ubuntu18.04.5LTS and has four 6900XT card. Why I do this is to handle the previous issue I proposed, which encountered when I try to run pytorch examples using rocm/pytorch. the link to previous issue is https://github.com/RadeonOpenCompute/ROCm/issues/1399

The steps I try this time is shown below, which follows the instructions in link https://github.com/ROCm/ROCm.github.io/blob/master/ROCmInstall.md#rocm-installation
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install rocm-dkms
sudo usermod -a -G video $LOGNAME
echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf   
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
sudo reboot
/opt/rocm/bin/rocminfo
and I get the following optputs

ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
rocm is member of video group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

I find that some links say that 6900XT is not supported by ROCm?
Could someone please help me? or give me some advice? 


---

## 评论 (15 条)

### 评论 #1 — xuhuisheng (2021-03-12T08:55:24Z)

run `dmesg | grep kfd` and `dmesg | grep amd`, see if there is warning or error message.

---

### 评论 #2 — ROCmSupport (2021-03-12T09:03:14Z)

Thanks @dshm for reaching out.
Yes Navi is not supported with ROCm right now. 
Yes, as requested in above comment, share the outputs of _dmesg | grep kfd_ and _dmesg | grep amd_ for initial understanding.
Thank you.


---

### 评论 #3 — dshm (2021-03-12T09:14:44Z)

@xuhuisheng @ROCmSupport 
dmesg | grep kfd shows nothing
dmesg | grep amd shows below
[    0.000000] Linux version 4.15.0-136-generic (buildd@lcy01-amd64-029) (gcc version 7.5.0 (Ubuntu 7.5.0-3
ubuntu1~18.04)) #140-Ubuntu SMP Thu Jan 28 05:20:47 UTC 2021 (Ubuntu 4.15.0-136.140-generic 4.15.18)

---

### 评论 #4 — xuhuisheng (2021-03-12T09:16:56Z)

I didn't use Ubuntu-18.04 for a while.
But AMD said it should use linux-5.4 kernel. Could you try to upgrade linux kernel to 5.4?

---

### 评论 #5 — ROCmSupport (2021-03-12T11:28:53Z)

Hi @dshm 
Its very old kernel. Recommend to try with 5.4 kernels.
You can install linux-5.4 , reboot and re-install rocm-dkms.

Like this:
sudo apt install linux-modules-extra-5.4.0-64-generic linux-headers-5.4.0-64-generic

---

### 评论 #6 — ROCmSupport (2021-03-12T11:30:34Z)

> 
> 
> @xuhuisheng @ROCmSupport
> dmesg | grep kfd shows nothing
> dmesg | grep amd shows below
> [ 0.000000] Linux version 4.15.0-136-generic (buildd@lcy01-amd64-029) (gcc version 7.5.0 (Ubuntu 7.5.0-3
> ubuntu1~18.04)) #140-Ubuntu SMP Thu Jan 28 05:20:47 UTC 2021 (Ubuntu 4.15.0-136.140-generic 4.15.18)

Looks like you have not installed rock-dkms, Request to install rocm kernel packages(rock-dkms, rock-dkms-firmware) or install rocm-dkms which installs everything.

---

### 评论 #7 — ROCmSupport (2021-03-17T06:07:48Z)

Hi @dshm 
Can you please follow the above comment and respond accordingly.
Thank you.

---

### 评论 #8 — btatar13 (2021-03-17T14:30:16Z)

Dear all,

I tried to install my Radeon 6800 under Ubuntu 20.04.1, however I obtained the same error. After trying to downgrade the kernel, install Ubuntu 18.04 etc. I received the same error. I wonder whether the 6000 series is supported at all? @ROCmSupport:  @dshm is using a 6900xt, is this GPU supported at all? If so, why is the Radeon 6800 not supported, or is it? I am slightly bit confused... Could someone maybe provide some advice?


---

### 评论 #9 — ROCmSupport (2021-03-18T02:54:47Z)

Hi @dshm 
Navi series of cards are currently not supported, some set of navi cards will be added into supported list in this year.
Please stay tuned for updates.
Thank you.

---

### 评论 #10 — dshm (2021-03-19T03:55:07Z)

> Hi @dshm
> Can you please follow the above comment and respond accordingly.
> Thank you.

@ROCmSupport 
Sorry for answering you late. These days I can't access github for network error. Currently I can't try 5.4 kernel because the machine is not used by me only. I will try to communicate with others who use the machine and reply you in the issue if I can use 5.4 kernel.
Thanks a lot!

---

### 评论 #11 — ROCmSupport (2021-05-07T11:16:21Z)

Hi @dshm 
Can you please share an update on this.
Or else request to close it as its open for a long time.
Thank you.

---

### 评论 #12 — ROCmSupport (2021-05-11T04:51:11Z)

Thanks @dshm for the closure of this issue Hope this issue is fixed.
Feel free to open a new issue for quick & fast resolution.
Thank you.

---

### 评论 #13 — kiwi-lilo (2021-09-08T10:43:22Z)

i have the same issue and use 6900xt too, so blogger, do you solve the question. thanks

---

### 评论 #14 — dshm (2021-12-20T03:48:35Z)

> i have the same issue and use 6900xt too, so blogger, do you solve the question. thanks

Sorry for missing this message at that time and answering so late. I didn't solve the problem.  

---

### 评论 #15 — venkat-kittu (2024-01-23T09:48:19Z)

I am also trying to install ROCm 5.6 on my ubuntu system, and I am also facing same issue when trying to run **rocminfo** command.
I followed the installation steps from below link
https://rocm.docs.amd.com/en/docs-5.6.0/deploy/linux/installer/install.html

Can you please help me where did I do wrong. 
Thanks in advance

---
