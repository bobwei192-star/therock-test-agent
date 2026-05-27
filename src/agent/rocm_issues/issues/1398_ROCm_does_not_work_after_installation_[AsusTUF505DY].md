# ROCm does not work after installation [AsusTUF505DY]

> **Issue #1398**
> **状态**: closed
> **创建时间**: 2021-03-01T20:37:41Z
> **更新时间**: 2021-03-02T10:25:33Z
> **关闭时间**: 2021-03-02T06:47:01Z
> **作者**: Sotwi-zz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1398

## 描述

My issue is pretty much the same as @JoseVSeb had in #1204. I'm trying to get PyTorch working for my Master, but haven't been able to. Reading I think my problem may also be related with what @Djip007 mentions in #750 but my Linux knowledge is rather basic so I don't know.

I also have an Asus TUF 505DY.
CPU: AMD Ryzen 5 3550H (With Vega/Raven GPU)
GPU: Radeon RX560X
Ubuntu: 20.04.2 LTS
Kernel: 5.6.0-1042-oem

I managed to follow the [installation guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu) but the final verification fails.

I'll attach the output of the commands I've seen used during debugging on the similar issue and if any other log is necessary I'll be glad to provide it.

Thanks in advance!

[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064316/rocminfo.txt)
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064318/clinfo.txt)
[rocm-smi.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064324/rocm-smi.txt)
[lspci-vvv.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064326/lspci-vvv.txt)
[lspci-tv.txt](https://github.com/RadeonOpenCompute/ROCm/files/6064327/lspci-tv.txt)








---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-03-02T06:45:43Z)

Thanks @Sotwi for reaching out.
I found that you are trying it on a Raven card.
We are not supporting officially Raven and looks like the driver does not load properly.

           +-18.0  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 0
           +-18.1  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 1
           +-18.2  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 2
           +-18.3  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 3
           +-18.4  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 4
           +-18.5  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 5
           +-18.6  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 6
           \-18.7  Advanced Micro Devices, Inc. [AMD] Raven/Raven2 Device 24: Function 7

---

### 评论 #2 — Sotwi-zz (2021-03-02T10:22:37Z)

Thank you for the quick answer @ROCmSupport. That's why I say it seems to
relate to what @Djip007 said on issue #750.

The Raven is part of the computer's APU. But the computer also has a
dedicate Radeon RX560X

Shouldn't it be possible to run ROCm on that one?

Thank you in advance once more!

On Tue, Mar 2, 2021, 07:45 ROCmSupport <notifications@github.com> wrote:

> Thanks @Sotwi <https://github.com/Sotwi> for reaching out.
> I found that you are trying it on a Raven card.
> We are not supporting officially Raven and hence I can not comment on this.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1398#issuecomment-788660277>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABVM4URDCYQWZFPMYM6M6R3TBSCSNANCNFSM4YNJA3FA>
> .
>


---

### 评论 #3 — ROCmSupport (2021-03-02T10:25:33Z)

Hi @Sotwi 
RX560X is also not a supported card. Check this: [https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support](url)
Thank you.


---
