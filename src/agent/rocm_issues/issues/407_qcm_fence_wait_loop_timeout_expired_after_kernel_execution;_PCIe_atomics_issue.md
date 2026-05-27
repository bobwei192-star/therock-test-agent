# qcm fence wait loop timeout expired after kernel execution; PCIe atomics issue?

> **Issue #407**
> **状态**: closed
> **创建时间**: 2018-05-08T20:25:26Z
> **更新时间**: 2018-05-12T13:01:11Z
> **关闭时间**: 2018-05-12T13:01:11Z
> **作者**: eqy
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/407

## 描述

I'm currently using a system with
i7 4790K
MSI Z97 Krait
Vega FE in PCI_E_2 (x16 slot--manual lists PCI_E_2 and PCI_E_5 as x16, PCI-E Gen 3 selected in UEFI/BIOS)

On rocm 1.7, Ubuntu 16.04.4, 4.4.0-119, I notice that certain kernels   repeatably produce
```
qcm fence wait loop timeout expired
Unmapping queues failed.
The cp might be in an unrecoverable state due to an unsuccessful queues preemption
qcm fence wait loop timeout expired
Unmapping queues failed.
```
at which point other, previously working kernels will also fail. Only after a reboot do other kernels starting working again.

This message is also preceded with
```
amdgpu 0000:03:00.0: VM_L2_PROTECTION_FAULT_STATUS
```
although there other kernels that produce this message do not leave the system in an unrecoverable state.

Is this a PCIe atomics issue? (e.g., in #46) It appears that out of thousands of different kernels only a few will trigger this behavior; the majority do not leave the system in an unrecoverable state.


---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-05-12T04:25:31Z)

@eqy Can you try ROCm 1.8 

---

### 评论 #2 — gstoner (2018-05-12T13:01:11Z)

@eqy with ROCm 1.7 if you put your GPU in PCI_E Gen 2 slot you would have a failure like this since PCe Gen 2 was not supported,   You can use ROCm 1.8 which remove this restriction 

---
