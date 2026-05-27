# ROCk module is NOT loaded, possibly no GPU devices

> **Issue #1506**
> **状态**: closed
> **创建时间**: 2021-06-25T18:47:40Z
> **更新时间**: 2021-07-27T12:06:50Z
> **关闭时间**: 2021-07-27T12:06:50Z
> **作者**: psairam369
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1506

## 描述

I have tried to install ROCm in my pc which has AMD Radeon (TM)RX Vega 10 Graphics as my GPU using steps provided in
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu website 
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install rocm-dkms
groups
sudo usermod -a -G video $LOGNAME
echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf
reboot
when i excute these command 
/opt/rocm/bin/rocminfo
I am getting 
ROCk module is NOT loaded, possibly no GPU devices
and when I excute 
/opt/rocm/opencl/bin/x86_64/clinf command
i am getting error    as
 bash: /opt/rocm/opencl/bin/x86_64/clinfo: No such file or directory
but facing these errors can you people please help me with these error.


---

## 评论 (9 条)

### 评论 #1 — Rmalavally (2021-06-25T19:53:29Z)

Thank you for reaching out. Please check the FAQ on ROCm installation at the following location, and let us know if you are unable to resolve the issue.

https://community.amd.com/t5/knowledge-base/frequently-asked-questions-about-rocm-installation/ta-p/475760

---

### 评论 #2 — ROCmSupport (2021-06-28T02:32:33Z)

Hi @psairam369 
Can you please help us with the system's environment, to help you better, like OS version, ROCm version, GPU(I got that its Vega10) and share the output of dmesg also.
Thank you.

---

### 评论 #3 — psairam369 (2021-06-28T14:13:04Z)

I am using Ubuntu 20.04 and I am facing these error
![Screenshot from 2021-06-28 19-41-10](https://user-images.githubusercontent.com/70476269/123651228-ed92d500-d848-11eb-83cb-206d5e49b593.png)


---

### 评论 #4 — ROCmSupport (2021-06-29T04:30:50Z)

Hi @psairam369 
Found that installation did not go well and so /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo executables are missed.
Can you please share the content of /opt

And also, as I asked in the previous comment, help me with the system's environment, to help you better, like **OS version, ROCm version, GPU**(I got that its Vega10) and **share the output of dmesg also**.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-07-01T12:54:46Z)

Hi @psairam369 
Can you please follow as suggested in the previous comment and help us with information, so that we will provide faster resolution.
Thank you.

---

### 评论 #6 — psairam369 (2021-07-01T14:53:14Z)

![Screenshot from 2021-07-01 20-20-48](https://user-images.githubusercontent.com/70476269/124144860-f6361600-daa9-11eb-8ee9-f4c871ca2a5c.png)


---

### 评论 #7 — sanjtrip (2021-07-01T15:21:54Z)

ROCM-TechSupport-Log script can be used to collect system info. It's at : https://github.com/amddcgpuce/rocmtechsupport

---

### 评论 #8 — ROCmSupport (2021-07-06T07:26:10Z)

Hi @psairam369 
Can you please share output of dmesg.
Looks like GPU is not detected or ROCm installation did not go well.

---

### 评论 #9 — ROCmSupport (2021-07-27T12:06:50Z)

Looks like no response from user for 3 weeks. I am closing this by considering that issue is fixed.
Request @psairam369 to file a new issues, if any, for faster resolutions.
Thank you.

---
