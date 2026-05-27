# rocm-smi 4.1 returns error

> **Issue #1446**
> **状态**: closed
> **创建时间**: 2021-04-09T02:37:12Z
> **更新时间**: 2021-04-12T07:32:06Z
> **关闭时间**: 2021-04-09T17:40:44Z
> **作者**: perestoronin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1446

## 描述

```
python3 /opt/rocm/bin/rocm_smi.py
Failed to get "domain" properity from properties files for kfd node 1.
rsmi_init() failed
Exception caught: rsmi_init.
ERROR:root:ROCm SMI returned 8 (the expected value is 0)
```

but rocminfo work perfect

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-04-09T05:44:39Z)

Hi @perestoronin 
Thanks for reaching out.
In my case, rocm-smi shows information properly.
Can you please share us with below information.
Asic, OS, Kernel, ROCm# version and dmesg output.

---

### 评论 #2 — perestoronin (2021-04-09T09:33:09Z)

```
Linux 5.4.110-gentoo-rt54 #1 SMP PREEMPT_RT Thu x86_64 AMD Phenom(tm) II X6 1100T
```
rocminfo  https://gist.github.com/raw/37969bd15b49c281c4d3535e9791876a
```
python /opt/rocm-4.1.0/bin/rocm_smi.py
Failed to get "domain" properity from properties files for kfd node 1.
rsmi_init() failed
Exception caught: rsmi_init.
ERROR:root:ROCm SMI returned 8 (the expected value is 0)
```
dmesg  https://gist.github.com/raw/800e51601e1aa6ccc0326abb44736890

cat /sys/class/kfd/kfd/topology/nodes/1/properties  https://gist.github.com/raw/eaa36a7bcac19abc5711ecf8cb692e0a


---

### 评论 #3 — ROCmSupport (2021-04-09T10:20:59Z)

Thanks for more information @perestoronin 
I looked at the device properties and found that "domain" property is missed and so its throwing error.

But in my case, "domain 0" and so no issue observed.
Working more to gather more information.

---

### 评论 #4 — perestoronin (2021-04-09T16:01:04Z)

I investigated, that domain introduced since kernel version 5.8.

@ROCmSupport  what versions of kernel compiance with rocm 4.1.1 ? In docs for rocm obsolete information for requerement kernel version driver amdgpu ?

---

### 评论 #5 — perestoronin (2021-04-09T17:40:40Z)

/opt/rocm/bin # python rocm_smi.py 
GPU  Temp   AvgPwr  SCLK    MCLK    Fan    Perf  PwrCap  VRAM%  GPU%  
0    39.0c  7.0W    852Mhz  167Mhz  14.9%  auto  220.0W    1%   6%    

/opt/rocm/bin # uname -a
Linux 5.10.28-gentoo-rt36 #1 SMP PREEMPT_RT x86_64 AMD Phenom(tm) II X6 1100T

Аfter update kernel from deprecated 5.4 to actual for rocm-4.1.1 kernel-5.10 issue is resolved.

---

### 评论 #6 — ROCmSupport (2021-04-12T07:32:06Z)

Thanks for upgrading kernel and closing this issue.
Thank you.

---
