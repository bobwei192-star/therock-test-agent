# Document device recommendation

> **Issue #1351**
> **状态**: closed
> **创建时间**: 2020-12-30T08:55:51Z
> **更新时间**: 2024-01-24T15:41:58Z
> **关闭时间**: 2024-01-24T15:41:57Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1351

## 描述

The documentation currently states that there are "supported" and "not officially supported" GPUs for ROCm:

<https://github.com/RadeonOpenCompute/ROCm#supported-gpus>

As recently stated, there are a set of devices which are recommended for use with ROCm:

> As complete support of ROCm works with gfx9 devices like Vega64, MI50(Vega 20), Radeon 7, recommend to use this type of card only.

_Originally posted by @ROCmSupport in https://github.com/RadeonOpenCompute/ROCm/issues/1148#issuecomment-747849233_

I suggest using this wording in the documentation, as it more closely conveys the distinction between such hardware, that might work ("supported") and such hardware, that should to work ("recommended").

---

## 评论 (12 条)

### 评论 #1 — ROCmSupport (2021-01-04T06:14:29Z)

Thanks @Bengt for reaching us.
Will reach Documentation team and marketing team for changes as you suggested.
Thank you.

---

### 评论 #2 — torehl (2021-01-13T14:55:14Z)

Maybe you could add it to rocm-smi. Poor reporting, e.g. for Instinct Mi100 

```
torel@n004:~$ /opt/rocm-4.0.0/bin/rocm-smi --showproductname
======================= ROCm System Management Interface =======================
================================= Product Info =================================
GPU[0]		: Card series: 		0x738c
GPU[0]		: Card model: 		0xc34
GPU[0]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]		: Card SKU: 		D34314
================================================================================
============================= End of ROCm SMI Log ==============================
```

while on Radeon Pro VII

```
torel@n003:~$  /opt/rocm-4.0.0/bin/rocm-smi --showproductname
======================= ROCm System Management Interface =======================
================================= Product Info =================================
GPU[0]		: Card series: 		Vega 20
GPU[0]		: Card model: 		0x81e
GPU[0]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]		: Card SKU: 		D16406
================================================================================
============================= End of ROCm SMI Log =============================
```

Maybe you could add here and to clinfo -v

---

### 评论 #3 — Bengt (2021-01-13T15:06:28Z)

@ROCmSupport I did the legwork and made it a pull request: <https://github.com/RadeonOpenCompute/ROCm/pull/1352>

---

### 评论 #4 — Bengt (2021-01-13T15:08:35Z)

@torehl I am no sure I get what you are suggesting. Do you want to see the marketing product name in the command line tools' output?

---

### 评论 #5 — kentrussell (2021-01-18T21:03:04Z)

Regarding the product information, we have an internal change coming to 4.1 or 4.2 to expose the proper Product Name for MI100 and other server cards. The issue is that we're currently using pci.ids and that's notoriously slow to update. For server cards, we'll be using the product information from the card itself, so we can get a bit more clarity for server cards. Unfortunately for consumer cards (like Radeon VII), we'll be stuck with whatever pci.ids has for us. Or we can try to integrate libdrm into the thunk and try to refer to that to get the information too.

---

### 评论 #6 — Bengt (2021-01-18T21:55:46Z)

There are two use cases to distinguish, here:

- As a user like me, who is in the market for a (new) GPU, I want to know which GPU to buy (next) for best ROCm support. For that use case, one needs to get the marketing names of recommended GPUs from the documentation.
- As a user like @torehl, who already has a card, I want to know if it is supported by ROCm. For that use case, one needs a mention of the "card model"/"PCI-ID" in the documentation.

Note that the card SKU does not help at all. Currently, this is the only mention of "D34314" and "D16406" [*dramatic pause*] on the web:

<https://www.google.com/search?q=%22D16406%22+Radeon+OR+AMD>
<https://www.google.com/search?q=%22D34314%22+Radeon+OR+AMD>

So would the best solution to these problems be naming both the marketing and PCI-IDs in the documentation?

For my cards, ROCm-SMI displays the correct code name ("Vega 10 XL/XT"), marketing name ("Radeon RX Vega 56/64") and also a card SKU ("D05005"):

```
$ /opt/rocm-4.0.0/bin/rocm-smi --device 0 --showproductname

======================= ROCm System Management Interface =======================
================================= Product Info =================================
GPU[0]		: Card series: 		Vega 10 XL/XT [Radeon RX Vega 56/64]
GPU[0]		: Card model: 		RX Vega64
GPU[0]		: Card vendor: 		Advanced Micro Devices, Inc. [AMD/ATI]
GPU[0]		: Card SKU: 		D05005
================================================================================
============================= End of ROCm SMI Log ==============================
```

The card SKU can be googled with some sensible results like it's VBIOS entry at TechPowerUp:

<https://www.google.com/search?q=D05005+radeon+OR+AMD>

---

### 评论 #7 — ROCmSupport (2021-02-04T06:06:20Z)

> 
> 
> @ROCmSupport I did the legwork and made it a pull request: #1352

Thanks @Bengt 
Please modify the PR as suggested and update asap.

---

### 评论 #8 — Bengt (2021-02-04T06:17:19Z)

You are welcome, @ROCmSupport
I modified the PR as suggested.

---

### 评论 #9 — ROCmSupport (2021-02-04T07:13:34Z)

Thanks @Bengt 
Let me talk to Documentation team for merging this PR.

---

### 评论 #10 — Bengt (2021-02-04T09:21:24Z)

Thanks for carrying my changes further though the process.

---

### 评论 #11 — nartmada (2024-01-18T03:55:22Z)

Hi @Bengt, do you still need this ticket to be opened?  Please close it if the work has been completed.  Thanks.

---

### 评论 #12 — nartmada (2024-01-24T15:41:57Z)

Closing this ticket for now as no updates after PR https://github.com/ROCm/ROCm/pull/1352 has been closed.  

---
