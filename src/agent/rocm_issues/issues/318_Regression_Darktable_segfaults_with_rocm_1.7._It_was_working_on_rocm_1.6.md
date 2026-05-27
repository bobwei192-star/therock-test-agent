# Regression: Darktable segfaults with rocm 1.7. It was working on rocm 1.6.

> **Issue #318**
> **状态**: closed
> **创建时间**: 2018-01-30T17:41:09Z
> **更新时间**: 2018-03-11T15:42:51Z
> **关闭时间**: 2018-03-11T15:42:51Z
> **作者**: simonwaid
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/318

## 描述

Steps to reproduce on Ubuntu 17.10, with rocm 1.7:

1. Make sure you have the rocm ppa in your repository.
2. Uninstall rocm and restore the firmware for amdgpu (work-around for another bug)
`apt remove rocm-dkms rocm-opencl`
`apt autoremove`
`apt install --reinstall linux-firmware`
`reboot`
3. Install darktable and verify that it works:
`apt install darktable`
`darktable`
4. Install rocm afresh
`apt install rocm-dkms rocm-opencl`
`reboot`
5. Start darktable and watch it segfault.
`darktable`
6. If it does not segfault: Go to settings and ensure that OpenCl is available and enabled, then restart darktable.


---

## 评论 (6 条)

### 评论 #1 — jamilbk (2018-01-30T17:44:15Z)

I can confirm this happens with ROCm 1.7 on Ubuntu 16.04 with the 4.13 kernel. All other OpenCL programs run fine.

Threadripper 1950x
Quad Vega FE
Darktable 1.4

[Here's a backtrace](https://github.com/RadeonOpenCompute/ROCm/files/1678770/darktable_bt_BTC5DZ.txt)


---

### 评论 #2 — simonwaid (2018-02-03T19:31:36Z)

Is there any way to downgrade to rocm 1.6?

This bug is a showstopper for me!

---

### 评论 #3 — gstoner (2018-02-03T19:49:17Z)

You know you can run Older OpenCL on 1.7 you do not have to swap out the whole foundation.    I ask our SQE group to see if Darktable is having an issue with the new 1.71 release we are working on  I let you know if we see anything  

PS you can downgade via the archive by up packing the tar for 1.6.4 and installing from local repo. 

---

### 评论 #4 — gstoner (2018-02-03T19:51:18Z)

One thing we need to check if Darktable is has a kernel that is doing out of bound memory reference, since,  we use guard pages that will fault the app upon an out of bounds memory reference. 

---

### 评论 #5 — simonwaid (2018-02-03T21:00:47Z)

Thank you gstoner! My Darktable is back!

For those who come across this thread. Here is how you get Darktable back to work:

Install rocm-dkms:
`apt install rocm-dkms`

From this site: [http://repo.radeon.com/rocm/archive/](http://repo.radeon.com/rocm/archive/)
download and extract apt_1.6.4.tar.bz2  

Now got to the directory apt_1.6.4/pool/main/r/rocm-opencl and install rocm-opencl_1.2.0-1464666_amd64.deb.

`dpkg -i rocm-opencl_1.2.0-1464666_amd64.deb`

Start Darktable and enjoy the speed of OpenCl!

---

### 评论 #6 — simonwaid (2018-03-11T15:42:49Z)

This issue is solved since rocm opencl 1.2.0-2018030103

---
