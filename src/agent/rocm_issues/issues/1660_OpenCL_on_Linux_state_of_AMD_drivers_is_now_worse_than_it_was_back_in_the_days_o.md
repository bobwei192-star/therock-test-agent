# OpenCL on Linux: state of AMD drivers is now worse than it was back in the days of fglrx [SOLUTIONS]

> **Issue #1660**
> **状态**: closed
> **创建时间**: 2022-01-25T18:42:45Z
> **更新时间**: 2022-02-07T11:22:37Z
> **关闭时间**: 2022-02-07T10:52:22Z
> **作者**: illwieckz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1660

## 描述

OpenCL on Linux : state of AMD drivers is now worse than it was back in the days of fglrx

* The last version of AMD OpenCL PAL for GCN5 generation and later dates back from Septembre 29 of 2020. The recent versions of the proprietary AMGPU-PRO driver do not support OpenCL for GCN5 hardware.
* The last version of AMD OpenCL Orca (“legacy”) for GCN1, 2, and 3 dates back from June 21 of 2021. The last verions of the proprietary AMDGPU-PRO driver do not support OpenCL for those cards. I don't know if it's a mistake, because this driver is still provided bu does not support GCN1, 2 and 3 (and I don't have GCN4 to do tests).
* ROCm/ROCr isn't for usual users, it seems developped for specific industrial usages, it [does not support graphical applications](https://github.com/RadeonOpenCompute/ROCm/issues/1397) (AMD said it's temporary but that can last for a long time) and only supports a very small amount of hardware : a tiny selection of PCIe graphics cards and no one integrated graphics solution from AMD APUs. Currently [only three chips](https://github.com/RadeonOpenCompute/ROCm/blob/c3f91afb2688deb638c360497e35b249f8026667/README.md#hardware-and-software-support) are said to be supported by ROCm.

I tell more about the situation here:

https://rebuild.sh/post/2022-01-25-OpenCL_on_Linux_state_of_AMD_drivers_is_now_worse_than_it_was_back_in_the_days_of_fglrx/

Here I maintain a script for Ubuntu to install last working Orca, last working PAL, ROCm (if you're feeling lucky), last working Clover (if you don't need image support), and also old AMD OpenCL APP for CPU:

> https://gitlab.com/illwieckz/i-love-compute#scripts

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2022-02-07T10:52:22Z)

Looks like this is not a question/defect. Its user's point of view.
So we can not keep it open, so I am closing it now. 
Thank you.

---

### 评论 #2 — illwieckz (2022-02-07T11:16:46Z)

@ROCmSupport for a comprehensive view of defects this issue is about you may want to look at:

- https://gitlab.com/illwieckz/i-love-compute/-/issues?label_name%5B%5D=GPU%2FAMD

For a better understanding of the defect, you can [read the article](https://rebuild.sh/post/2022-01-25-OpenCL_on_Linux_state_of_AMD_drivers_is_now_worse_than_it_was_back_in_the_days_of_fglrx/) I linked before.

The defect affects ROCm but is also **at a larger level than ROCm**, defects in ROCm are just a very narrow part of a bigger problem we need to be reported at an higher level at AMD.

The defect can be worded this way: _AMD does not provide working OpenCL for its range of hardware on Linux_ (ROCm fails at it, but that's just a part of the problem), this is not an opinion, it's a report of a broken situation that includes various reported bugs (some being ROCm related).

The issue needs to be reported at an higher level at AMD.

---
