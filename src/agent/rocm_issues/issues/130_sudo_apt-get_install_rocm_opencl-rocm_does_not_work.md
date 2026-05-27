# sudo apt-get install rocm opencl-rocm does not work

> **Issue #130**
> **状态**: closed
> **创建时间**: 2017-06-16T09:38:11Z
> **更新时间**: 2017-07-01T21:46:36Z
> **关闭时间**: 2017-07-01T21:46:36Z
> **作者**: zhaojunfan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/130

## 描述

Linux 16.04.02, AMD W9100 graphic card.
I follow the readme.md in ROCm project, on branch roc-1.5.0 .
I try to install opencl, but failed.
1. wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
2. sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
3. sudo apt-get update
4. sudo apt-get install rocm opencl-rocm
5. sudo apt-get install rocm opencl-rocm-dev

both 4 and 5 failed, can get the package.
I want to know why?

---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-06-16T10:19:47Z)

You only need to do 4 or 5


Greg
On Jun 16, 2017, at 4:38 AM, zhaojunfan <notifications@github.com<mailto:notifications@github.com>> wrote:


Linux 16.04.02, AMD W9100 graphic card.
I follow the readme.md in ROCm project, on branch roc-1.5.0 .
I try to install opencl, but failed.

  1.  wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
  2.  sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
  3.  sudo apt-get update
  4.  sudo apt-get install rocm opencl-rocm
  5.  sudo apt-get install rocm opencl-rocm-dev

both 4 and 5 failed, can get the package.
I want to know why?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/130>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQPiA7x3ZqNhl2J5AH9lCwVHhbJ6ks5sEk0EgaJpZM4N8PnQ>.



---

### 评论 #2 — zhaojunfan (2017-06-19T01:22:53Z)

I did step 4, get the output like this:
mcw@mcw-All-Series-Invalid-entry-length-16-Fixed-up-to-11:~/fzj$ sudo apt-get install rocm opencl-rocm
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package opencl-rocm

I did step 5, get the output like this;
mcw@mcw-All-Series-Invalid-entry-length-16-Fixed-up-to-11:~/fzj$ sudo apt-get install rocm opencl-rocm-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package opencl-rocm-dev





---

### 评论 #3 — briansp2020 (2017-06-19T02:02:40Z)

Proper command is
sudo apt-get install **rocm-opencl-dev**

---

### 评论 #4 — gstoner (2017-07-01T21:46:36Z)

ROCm 1.6 is out now also we built new set of getting started instructions https://github.com/ROCm/ROCm.github.io/blob/master/ROCmInstall.md 

---
