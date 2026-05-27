# rocminfo not recognising gpu  Radeon Pro WX 7100 on Centos 7

> **Issue #804**
> **状态**: closed
> **创建时间**: 2019-05-22T06:06:59Z
> **更新时间**: 2019-05-24T11:03:38Z
> **关闭时间**: 2019-05-24T11:03:38Z
> **作者**: brij01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/804

## 描述

$ rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/sandbox-centos/rocm-rel-2.1/rocm-2.1-96-20190201/centos/rocminfo/rocminfo.cc. Call returned 4104


[rocm@rocm ~]$ dmesg | grep kfd
[    2.558244] kfd kfd: Initialized module
[    2.562957] kfd kfd: skipped device 1002:67c4, PCI rejects atomics
[    3.359595] kfd kfd: skipped device 1002:67c4, PCI rejects atomics


[rocm@rocm ~]$ dkms status
amdgpu, 19.10-782345.el7, 3.10.0-957.el7.x86_64, x86_64: built (original_module exists)
amdgpu, 2.4-25.el7, 3.10.0-957.12.2.el7.x86_64, x86_64: installed (original_module exists)
amdgpu, 2.4-25.el7, 3.10.0-957.el7.x86_64, x86_64: installed (original_module exists)



-[0000:00]-+-00.0  Intel Corporation 5500 I/O Hub to ESI Port
             +-01.0-[01-04]----00.0-[02-04]--+-08.0-[03]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon Pro WX 7100]
             |                               |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580]
             |                               \-10.0-[04]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon Pro WX 7100]


---

## 评论 (7 条)

### 评论 #1 — brij01 (2019-05-22T06:08:01Z)

Hi
any suggestions please. 


---

### 评论 #2 — vulturm (2019-05-22T06:24:20Z)

[3.359595] kfd kfd: skipped device 1002:67c4, PCI rejects atomics

According to the docs, your card is GFX8 and needs PCI atomics.


https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md#supported-gpus--


Sent from mobile, apologies for typos.

On Wed, 22 May 2019, 09:08 brij01, <notifications@github.com> wrote:

> Hi
> any suggestions please.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/804?email_source=notifications&email_token=AAJ5S2VKDRSDPGKUUSSGDJDPWTPMFA5CNFSM4HOQ6KO2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODV575OY#issuecomment-494665403>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAJ5S2SVP56HNC6EZYY7XP3PWTPMFANCNFSM4HOQ6KOQ>
> .
>


---

### 评论 #3 — brij01 (2019-05-22T09:20:58Z)

HI
Thanks for the prompt reply. 
I now plugged in the card in a new machine with the  CPU Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz
Installed rocm-dkms and after reboot getting this error in the dmsg
rockminfo is giving same output as above 

[root@brij ~]# dmesg | grep amd
[    0.297006] amd_nb: Cannot enumerate AMD northbridges
[    9.473507] amdkcl: loading out-of-tree module taints kernel.
[    9.473632] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   10.412976] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu kernel modesetting.
[   10.895809] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu kernel modesetting.
[ 1186.784959] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu kernel modesetting.
[ 1187.467679] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu kernel modesetting.
[ 1399.048068] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu kernel modesetting.
[ 1399.776416] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu kernel modesetting.

please suggest






---

### 评论 #4 — vulturm (2019-05-22T09:40:29Z)

grep kfd still complains about rejecting atomics ?

https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md#supported-cpus
says that
"Current CPUs which support PCIe Gen3 + PCIe Atomics are:


   - AMD Ryzen CPUs;
   - The CPUs in AMD Ryzen APUs;
   - AMD Ryzen Threadripper CPUs
   - AMD EPYC CPUs;
   - Intel Xeon E7 v3 or newer CPUs;
   - Intel Xeon E5 v3 or newer CPUs;
   - Intel Xeon E3 v3 or newer CPUs;
   - Intel Core i7 v4, Core i5 v4, Core i3 v4 or newer CPUs (i.e. Haswell
   family or newer).
   - Some Ivy Bridge-E systems

"

On Wed, May 22, 2019 at 12:21 PM brij01 <notifications@github.com> wrote:

> HI
> Thanks for the prompt reply.
> I now plugged in the card in a new machine with the CPU Intel(R) Core(TM)
> i7-3770 CPU @ 3.40GHz
> Installed rocm-dkms and after reboot getting this error in the dmsg
> rockminfo is giving same output as above
>
> [root@brij ~]# dmesg | grep amd
> [ 0.297006] amd_nb: Cannot enumerate AMD northbridges
> [ 9.473507] amdkcl: loading out-of-tree module taints kernel.
> [ 9.473632] amdkcl: module verification failed: signature and/or required
> key missing - tainting kernel
> [ 10.412976] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu
> kernel modesetting.
> [ 10.895809] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu
> kernel modesetting.
> [ 1186.784959] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu
> kernel modesetting.
> [ 1187.467679] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu
> kernel modesetting.
> [ 1399.048068] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu
> kernel modesetting.
> [ 1399.776416] [drm:amdgpu_init [amdgpu]] *ERROR* VGACON disables amdgpu
> kernel modesetting.
>
> please suggest
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/804?email_source=notifications&email_token=AAJ5S2WYUWHPNC7LMEGFQM3PWUF7XA5CNFSM4HOQ6KO2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODV6OIPA#issuecomment-494724156>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAJ5S2QP6IOMUCUCDVBQ2ILPWUF7XANCNFSM4HOQ6KOQ>
> .
>


---

### 评论 #5 — brij01 (2019-05-22T09:54:55Z)

Hi, 
There is no message when I do grep kfd


---

### 评论 #6 — kentrussell (2019-05-22T15:14:43Z)

The amdgpu device isn't being initialized:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L1408

The error message shows that you have nomodeset turned on in your kernel parameters:
https://elixir.bootlin.com/linux/latest/source/drivers/video/console/vgacon.c#L114

As the warning message says, if you do that, the GPU drivers are disabled. And if the GPU (amdgpu) drivers are disabled, that means that KFD is disabled as well, thus disabling ROCm altogether.

---

### 评论 #7 — brij01 (2019-05-24T11:03:38Z)

Many Thanks.. 
I replaced the GPU in a newer machine with supported CPU and i don't see the error anymore. 


---
