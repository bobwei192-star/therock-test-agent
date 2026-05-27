# openSUSE Tumbleweed + linux 5.0.8 small issue

> **Issue #780**
> **状态**: closed
> **创建时间**: 2019-04-23T12:22:53Z
> **更新时间**: 2023-12-18T18:55:14Z
> **关闭时间**: 2023-12-18T18:55:14Z
> **作者**: kk-1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/780

## 描述

Hello Folks,
I tried rpms of the rehl on openSUSE Tumbleweed with kernel 5.0.8 and RX 590.

There is this little issue about "pciutils-libs" dependency
opensuse has "pciutils". I ignored that and with yast installed "rocm-dkms" from yum repo.
So far no problem. 
/opt/rocm/bin/rocminfo
and
/opt/rocm/opencl/bin/x86_64/clinfo
both works

Kernel modules seems ok:
michael:/home/kemal # dmesg | grep kfd
[    5.456206] kfd kfd: Allocated 3969056 bytes on gart
[    5.456349] kfd kfd: added device 1002:67df
michael:/home/kemal # dkms status
amdgpu, 19.10-785424: added
amdgpu, 2.3-14.el7: added
 
I also compiled "hipBusBandwidth"  and executed it successfully.

In that sense, I believe making rocm rpms fully compatible with openSUSE Tumbleweed
will require very little work.
I hope you can find time to do this favor to us suse users.

Thanks for your time.
All the best...

Kemal



---

## 评论 (3 条)

### 评论 #1 — Djip007 (2019-04-25T01:39:06Z)

If i don't make mistake:
Do not install rock-dkms... kfd is include with amdgpu for last kernel (>= 4.18?) 
No dkms is neaded for kernel 5.0.x  (and kernel >= 4.18?)


---

### 评论 #2 — tasso (2023-12-12T20:07:54Z)

Is this still an issue? If not, can we please close it? Thanks!

---

### 评论 #3 — tasso (2023-12-18T18:55:12Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request. If this is still an issue, please file a new ticket and we will be more than happy to investigate it. Thanks!

---
