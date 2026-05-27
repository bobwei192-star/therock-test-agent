# Kernel `4.4.0-kfd-compute-rocm-rel-1.2-31` doesn't have ZFS modules.

> **Issue #34**
> **状态**: closed
> **创建时间**: 2016-09-27T10:59:45Z
> **更新时间**: 2017-07-02T17:14:48Z
> **关闭时间**: 2017-07-02T17:14:48Z
> **作者**: almson
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/34

## 描述

Please build your Ubuntu kernels from Ubuntu kernel sources using Ubuntu configs to be compatible with Ubuntu.


---

## 评论 (8 条)

### 评论 #1 — gstoner (2016-09-27T11:44:23Z)

With ROCm 1.3 we moving to Loadable Modules for KFD,  So you use standard linux kernel.

On Sep 27, 2016, at 5:59 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:

Please build your Ubuntu kernels from Ubuntu kernel sources using Ubuntu configs to be compatible with Ubuntu.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/34, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuQSU1AVbnq0OQaxyz-M3usZ3ZZN7ks5quPchgaJpZM4KHh5G.


---

### 评论 #2 — almson (2016-09-27T13:18:25Z)

That's very good. In the meantime, I wrote up some instructions for porting the Ubuntu patches to your kernel. (Tested on Ubuntu 16.04.)

### Install prerequisites

```
sudo apt-get build-dep linux
```

### Get sources

```
git clone git://kernel.ubuntu.com/ubuntu/linux.git linux-kernel
git clone --reference linux-kernel https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver.git linux-kernel-roc
git clone --reference linux-kernel git://kernel.ubuntu.com/ubuntu/ubuntu-xenial.git ubuntu-kernel-xenial
```

### Push the ROC branch into the Ubuntu tree

```
cd linux-kernel-roc
git checkout roc-1.2.0
git branch roc
git remote add ubuntu-kernel-xenial ../ubuntu-kernel-xenial
git push ubuntu-kernel-xenial roc
```

### Rebase ROC onto the last Ubuntu kernel commit that supports it.

```
cd ../ubuntu-kernel-xenial
git checkout Ubuntu-4.4.0-0.10
git rebase roc
```

(Ubuntu-4.4.0-0.10 uses the same base, namely 4.4.0, as the ROC 1.2 kernel. It may be possible/advisable to use a more recent base.)

### Fix the config

Here I was a little unsure, because the roc .config doesn't set most of these either. (Note that if you're doing this to a more recent version of the Ubuntu kernel, chances are the broken config entries will be different. Proceed to the `updateconfigs` step and see what, if anything, it wants from you.)

Edit `debian.master/config/config.common.ubuntu`, and append

```
CONFIG_DRM_AMDGPU_GART_DEBUGFS=n
CONFIG_DRM_AMD_POWERPLAY=y
CONFIG_DRM_AMD_ACP=n
CONFIG_DRM_AMD_DAL=n
CONFIG_SND_SOC_AMD_ACP=n
```

### Compile

```
fakeroot debian/rules clean
debian/rules updateconfigs
env AUTOBUILD=1 fakeroot debian/rules binary
```

### Install

(Pick which packages to install based on your needs.)

```
cd ..
sudo dpkg -i linux-headers-4.4.0-0_4.4.0-0.10_all.deb linux-tools-4.4.0-0_4.4.0-0.10_amd64.deb  linux-headers-4.4.0-0-lowlatency_4.4.0-0.10_amd64.deb linux-image-4.4.0-0-lowlatency_4.4.0-0.10_amd64.deb linux-tools-4.4.0-0-lowlatency_4.4.0-0.10_amd64.deb
```


---

### 评论 #3 — almson (2016-11-27T17:00:55Z)

ROCm 1.3 still doesn't have zfs modules or Ubuntu patches. Nor does it use a standard kernel with dkms as promised.

---

### 评论 #4 — gstoner (2016-11-27T18:50:30Z)


On Nov 27, 2016, at 11:00 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:


ROCm 1.3 still doesn't have zfs modules or Ubuntu patches. Nor does it use a standard kernel with dkms as promised.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/34#issuecomment-263133474>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYvS4fngi4BzcytIfC9ERlx2yNtbks5rCbdIgaJpZM4KHh5G>.



---

### 评论 #5 — gstoner (2016-11-27T18:51:53Z)

We never promised ZFS support,  But I let the lead on DKMS talk you through what is there what is not.  We have been working on it base DKMS support is already there. 

---

### 评论 #6 — almson (2016-11-28T10:23:59Z)

Thank you, looking forward to it. The trick with rebasing the Ubuntu tree onto the ROCm tree isn't working, so a DKMS solution would be great.

---

### 评论 #7 — almson (2016-11-28T12:09:31Z)

Is ROCm 1.3 compatible with any vanilla 4.8 kernel? When do you foresee standard Linux supporting ROCm?

---

### 评论 #8 — almson (2016-12-05T10:41:39Z)

@gstoner Any update on how I can compile a module for the Ubuntu kernel?

---
