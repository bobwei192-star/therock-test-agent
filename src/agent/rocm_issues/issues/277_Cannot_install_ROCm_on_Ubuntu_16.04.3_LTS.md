# Cannot install ROCm on Ubuntu 16.04.3 LTS

> **Issue #277**
> **状态**: closed
> **创建时间**: 2017-12-21T14:27:14Z
> **更新时间**: 2017-12-23T15:43:35Z
> **关闭时间**: 2017-12-23T15:43:35Z
> **作者**: bdeji
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/277

## 描述

Hello,

When trying to install ROCm with the **sudo apt-get install rocm rocm-opencl-dev** command I'm receiving the following error:

Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package rocm

Repo is added, every command was ran successfully.

A week ago this command ran just fine on another rig. What should be done?

---

## 评论 (16 条)

### 评论 #1 — boxerab (2017-12-21T14:38:21Z)

Package is now called `rocm-dkms`.  You should review the project README, as the instructions have changed.

---

### 评论 #2 — bdeji (2017-12-21T14:41:42Z)

I tried this command as well, but I don't see any increase in mining speed. How can I check if ROCm was installed properly?

---

### 评论 #3 — gstoner (2017-12-21T14:47:38Z)

Did you follow the instructions   https://rocm.github.io/ROCmInstall.html 

With move to upstreaming the KFD driver and the support of DKMS, for all Console aka headless user, you will need to add all your users to the ‘video” group by setting the Unix permissions

sudo usermod -a -G video <username>

Then reboot the system 

---

### 评论 #4 — bdeji (2017-12-21T15:57:48Z)

I tried your suggestions, but now, none of my GPU's are recognized in claymore. Does ROCm install some GPU drivers?


---

### 评论 #5 — gstoner (2017-12-21T16:37:27Z)


Are you mixing driver,  Yes ROCm 1.7  install a driver if you had AMDGPU driver on your system you have an issue.   You have to install the driver follow these instructions https://rocm.github.io/ROCmInstall.html 

---

### 评论 #6 — gstoner (2017-12-21T16:38:43Z)

You need to run this now   note rocm is now rocm-dkms.   which is why your install broke 

sudo apt-get update
sudo apt-get install rocm-dkms rocm-opencl-dev
```permisions

With move to upstreaming the KFD driver and the support of DKMS, for all Console aka headless user, you will need to add all your users to the ‘video” group by setting the Unix permissions

```shell
sudo usermod -a -G video <username>

---

### 评论 #7 — bdeji (2017-12-22T14:52:32Z)

I have tried your suggestions, but even on a clean install and after installing rocm my GPU's are not recognized.

With the original amd-gpu driver all my GPU's are showing up in Claymore.

What would you suggest to do next?

---

### 评论 #8 — bdeji (2017-12-22T18:14:21Z)

Is there any way to install ROCm 1.6? With the 1.6 version we have several rigs working just fine.

---

### 评论 #9 — CultClassik (2017-12-22T18:47:08Z)

Same issue, seems totally broken.  All of the docs are out of whack, say different things, say "we recommend doing X at this link" and it links back to itself.  What's going on with this stuff?  

---

### 评论 #10 — bdeji (2017-12-22T18:50:19Z)

I would like an option to install older versions as well. There is not much sense forcing users to the latest version when this is not working. 

I'm not saying that it is broken or something, but as you can see there are others who encounter the same issues as myself.

---

### 评论 #11 — gstoner (2017-12-22T20:05:37Z)

I am sorry you're having install issues.  We archive all releases on repo.radeon.com.  In the archive directory.

Also, the direction is consistent. But if need more straightforward direction goes to rock.github.com click on documentation tab and you see a link for install instruction.    Also, this is DKMS install which you need to make sure old components are not installed. If your working from anything other then ubuntu 16.04 it's. It is Not tested

We tested the release on large number of system

Ps, we not forcing you to upgrade you choose too.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Barni91 <notifications@github.com>
Sent: Friday, December 22, 2017 12:50:21 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] Cannot install ROCm on Ubuntu 16.04.3 LTS (#277)


I would like an option to install older versions as well. There is not much sense forcing users to the latest version when this is not working.

I'm not saying that it is broken or something, but as you can see there are others who encounter the same issues as myself.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/277#issuecomment-353655392>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuUnd3BWQYBK0Tsio2KY6ojKZcydgks5tC_ntgaJpZM4RJ5E->.


---

### 评论 #12 — bdeji (2017-12-22T20:36:52Z)

Thank you gstoner for the archive. Any steps on how to install it?

---

### 评论 #13 — gstoner (2017-12-22T21:50:56Z)

@CultClassik   To follow ROCm 1.7 follow these instruction https://rocm.github.io/ROCmInstall.html   Again we have many people who have installed it.  

The command use to be 
sudo apt-get install rocm-dkms rocm-opencl-dev
It is now this to install rocm.   Note this is DKMS,  did you check you have the development tool installed since you need this to build the kernel 

sudo apt-get install rocm-dkms rocm-opencl-dev


With move to upstreaming the KFD driver and the support of DKMS, for all Console aka headless user, you will need to add all your users to the ‘video” group by setting the Unix permissions

```shell
sudo usermod -a -G video <username>

---

### 评论 #14 — gstoner (2017-12-22T22:01:18Z)

You have to download apt_1.6.4.tar.bz2  

Then you have add the package to your package manager 
sudo dpkg -i <name of package>.deb

sudo apt

For 1.6.4 you use the old commands once the packages are added to local package manager in Ubuntu 
sudo apt-get update
sudo apt-get install rocm rocm-opencl-dev

---

### 评论 #15 — gstoner (2017-12-22T22:30:11Z)

@Barni91  What CPU are you using? 

---

### 评论 #16 — gstoner (2017-12-23T15:42:30Z)

 I now realize some people typing in <username> this was place holder for you to replace with your username  here is better command to execute to simplify this, I changed the instructions as well to this 

sudo usermod -a -G video $LOGNAME

---
