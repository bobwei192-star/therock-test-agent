# Please confirm ROCm works on Ubuntu 18.10

> **Issue #588**
> **状态**: closed
> **创建时间**: 2018-10-27T04:28:03Z
> **更新时间**: 2019-12-26T18:16:01Z
> **关闭时间**: 2018-11-15T15:48:40Z
> **作者**: preda
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/588

## 标签

- **Question** (颜色: #cc317c)

## 描述

Does ROCm work on Ubuntu 18.10, which was released on October 18
https://wiki.ubuntu.com/CosmicCuttlefish/ReleaseSchedule


---

## 评论 (8 条)

### 评论 #1 — 949f45ac (2018-10-27T05:34:22Z)

I ran it on 18.10 beta (downloaded 2018-10-05) and it worked fine. Installed without dkms. Don’t forget to add the kfd rule. `echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules`

There hasn’t yet been an amdgpu-pro release for 18.10, however. Just in case you want that too.

---

### 评论 #2 — jlgreathouse (2018-10-27T17:02:03Z)

I can confirm what @949f45ac says. I've run ROCm 1.9.1 user-land code on top of the default Ubuntu 18.10 kernel and haven't run into any major problems.

That said, Ubuntu 18.10 is not an [officially supported platform](https://github.com/RadeonOpenCompute/ROCm#supported-operating-systems---new-operating-systems-available), so we have not rigorously tested all layers of the ROCm stack against it. It _should_ work as far as we know, but it does not go through the same level of pre-released testing as our officially supported distros.

---

### 评论 #3 — shimmervoid (2018-10-27T17:05:53Z)

Installing and using GCC 7.3 over the default 8.2 may help with any compiler issues. 

---

### 评论 #4 — preda (2018-11-06T23:00:04Z)

Thanks, I confirm I can use ROCm 1.9.1 OpenCL correctly on Ubuntu 18.10 with the default Linux kernel 4.18.0.

As a side note, it would be nice to mention somewhere on ROCm install instructions the udev setup that is needed when installing without dkms:

echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules


---

### 评论 #5 — jlgreathouse (2018-11-07T01:12:17Z)

I believe [we do mention that](https://github.com/RadeonOpenCompute/ROCm#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels) specifically when discussing using upstream kernels with ROCm.

---

### 评论 #6 — preda (2018-11-07T07:46:18Z)

@jlgreathouse: yes, indeed that is documented, my bad.

---

### 评论 #7 — arigit (2018-11-25T18:53:36Z)

Just to add for the record - on ubuntu 18.10, ROCM-based OpenCL acceleration for darktable works flawlessly (and a tad faster than with the legacy amdgpu-pro drivers). 
The only package required is rocm-opencl; that, the udev rule above and adding the user to the 'video' group. Thanks @amd folks for making it simple

---

### 评论 #8 — alejandromunozes (2019-12-26T18:16:01Z)

> I believe [we do mention that](https://github.com/RadeonOpenCompute/ROCm#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels) specifically when discussing using upstream kernels with ROCm.

The command you mention there is wrong because the character | is missing. The correct one is:

`echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules`

So please, fix it. 


---
