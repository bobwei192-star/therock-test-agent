# ROCk module is NOT loaded, possibly no GPU devices on Radeon RX 6700S

> **Issue #1794**
> **状态**: closed
> **创建时间**: 2022-08-21T08:51:26Z
> **更新时间**: 2024-02-16T16:38:20Z
> **关闭时间**: 2024-02-16T16:38:20Z
> **作者**: abinmahfuth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1794

## 描述

Hi all,

I have followed the steps on this page to install ROCm v5.2.3 using the installer:
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.2.3/page/How_to_Install_ROCm.html

Running` /opt/rocm-5.2.3/bin/rocminfo` I get:

`ROCk module is NOT loaded, possibly no GPU devices`

Noting I am using Ubuntu 20.4 on WSL2. 

As far as I am concerned, ROCm should support RDNA GPUs like the RX 6700s series, is that correct?

What do you think went wrong?





---

## 评论 (3 条)

### 评论 #1 — langyuxf (2022-08-26T02:31:20Z)

It seems that the amdgpu kernel mode driver is not loaded properly. 
You can try to install ROCm on bare metal Ubuntu instead of WSL2 first.
```
$ lsmod | grep amdgpu
amdgpu               8261632  0
iommu_v2               24576  1 amdgpu
gpu_sched              40960  1 amdgpu
drm_ttm_helper         16384  1 amdgpu
ttm                    73728  2 amdgpu,drm_ttm_helper
drm_display_helper    139264  1 amdgpu
drm_kms_helper        163840  4 drm_display_helper,amdgpu
i2c_algo_bit           16384  1 amdgpu
drm                   626688  7 gpu_sched,drm_kms_helper,drm_display_helper,amdgpu,drm_ttm_helper,ttm
```

---

### 评论 #2 — nartmada (2023-12-18T20:59:59Z)

Hi @abinmahfuth, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  Also please try bare metal Ubuntu.  If your issue has been resolved, please close the ticket.  Thanks.

---

### 评论 #3 — nartmada (2024-02-16T16:38:20Z)

Closing the ticket as no response from @abinmahfuth.  Please re-open the ticket if the issue still exists in latest ROCm 6.0.2.  Thanks.

---
