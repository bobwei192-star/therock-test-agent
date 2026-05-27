# Unable to open /dev/kfd read-write: Cannot allocate memory

> **Issue #1148**
> **状态**: closed
> **创建时间**: 2020-06-15T08:17:26Z
> **更新时间**: 2024-01-27T20:12:07Z
> **关闭时间**: 2020-12-18T03:45:26Z
> **作者**: TolyProg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1148

## 描述

My OS is Arch Linux.
My PC is Xeon E5-2689, 32GB of RAM and RX570 8GB.

> $ sudo rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
tolyprog is member of render group
hsa api call failure at: /home/tolyprog/.cache/yay/rocminfo/src/rocminfo-rocm-3.5.0/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

---

## 评论 (15 条)

### 评论 #1 — kjuanman (2020-07-04T19:06:56Z)

same issue, I confirm:
$ sudo rocminfo 
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
juan is member of render group
hsa api call failure at: /home/juan/.cache/pacaur/rocminfo/src/rocminfo-rocm-3.5.0/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

My OS is Manjaro, archlinux based
$ lsb_release -a
LSB Version:    n/a
Distributor ID: ManjaroLinux
Description:    Manjaro Linux
Release:        20.0.3
Codename:       Lysia

---

### 评论 #2 — geocarvalho (2020-08-02T21:45:45Z)

Same issue on my ubuntu 20.04

```
$ rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
george is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
```

---

### 评论 #3 — xuhuisheng (2020-08-03T01:59:54Z)

`dmesg|grep kfd`
check whether kdf reject because not supporting PCIe Atomics

---

### 评论 #4 — RedScientistOne (2020-08-03T03:15:48Z)

rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
red is member of video group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.


> `dmesg|grep kfd`
> check whether kdf reject because not supporting PCIe Atomics

dmesg|grep kfd
[   16.149772] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[   16.151683] kfd kfd: amdgpu: error getting iommu info. is the iommu enabled?
[   16.151688] kfd kfd: amdgpu: Error initializing iommuv2
[   16.151775] kfd kfd: amdgpu: device 1002:130d NOT added due to errors
[   16.699618] kfd kfd: amdgpu: HAINAN  not supported in kfd

This is my information look like.
My System is Ubuntu 18.04 LTS, with laptop A10-7400p radeon R6 and R5 M250 GPU with 6GB of RAMs and 1 TB of HDD



---

### 评论 #5 — xuhuisheng (2020-08-03T03:32:58Z)

kfd not successful added GPU. but donot know what the HAINAN means.
```
[ 16.151683] kfd kfd: amdgpu: error getting iommu info. is the iommu enabled?
[ 16.151688] kfd kfd: amdgpu: Error initializing iommuv2
[ 16.151775] kfd kfd: amdgpu: device 1002:130d NOT added due to errors
[ 16.699618] kfd kfd: amdgpu: HAINAN not supported in kfd
```

---

### 评论 #6 — geocarvalho (2020-08-04T11:15:14Z)

```
$ dmesg | grep kfd
[    4.528825] kfd kfd: amdgpu: TOPAZ  not supported in kfd
```

---

### 评论 #7 — xuhuisheng (2020-08-04T11:52:55Z)

```
$ dmesg|grep kfd
[    5.143681] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    5.148990] kfd kfd: amdgpu: added device 1002:67df
```

---

### 评论 #8 — piodag (2020-09-24T07:15:55Z)

> ```
> $ dmesg|grep kfd
> [    5.143681] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
> [    5.148990] kfd kfd: amdgpu: added device 1002:67df
> ```

For me

root@lonovo:/home/gfwp# dmesg | grep kfd
[    1.884198] kfd kfd: Allocated 3969056 bytes on gart
[    1.885377] kfd kfd: added device 1002:15d8


On up to date Debian Bullseye and rocm 3.80

---

### 评论 #9 — Mhowser (2020-12-17T23:33:21Z)

```
dmesg | grep kfd
[    2.803287] kfd kfd: skipped device 1002:67df, PCI rejects atomics
```
Anything I can do about this?

---

### 评论 #10 — xuhuisheng (2020-12-17T23:56:21Z)

@Mhowser 
gfx803 cannot run without PCIe atomics. please refer here https://github.com/radeonopencompute/ROCm#supported-cpus


---

### 评论 #11 — Mhowser (2020-12-18T00:15:59Z)

I have the AMD Athlon x4 880k CPU and the AMD RX580 GPU, so due to my CPU not having PCIe 3.0 capability I cannot use ROCm, correct?

---

### 评论 #12 — xuhuisheng (2020-12-18T00:21:32Z)

Cannot run ROCm with RX580 without PCIe atomics.
Can use Vega64, Radeon VII, they don't need PCIe atomics. 

---

### 评论 #13 — ROCmSupport (2020-12-18T03:43:58Z)

Yes @Mhowser 
gfx8 needs PCIe atomics support.
gfx9 devices does not require PCIe atomics. 
As complete support of ROCm works with gfx9 devices like Vega64, MI50(Vega 20), Radeon 7, recommend to use this type of card only.
Thank you.

---

### 评论 #14 — ROCmSupport (2020-12-18T03:45:26Z)

Hi All,
Hainan and Topaz are very old cards having GFX IP of 7 and below, which are not supported with ROCm.
Thank you.

---

### 评论 #15 — eugene-bright (2024-01-27T20:12:07Z)

Now you can use `rusticl` mesa backend. `RUSTICL_ENABLE=radeonsi` env variable is still required.

---
