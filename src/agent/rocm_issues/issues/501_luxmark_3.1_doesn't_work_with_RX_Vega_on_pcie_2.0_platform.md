# luxmark 3.1 doesn't work with RX Vega on pcie 2.0 platform

> **Issue #501**
> **状态**: closed
> **创建时间**: 2018-08-17T23:09:01Z
> **更新时间**: 2018-08-28T07:06:51Z
> **关闭时间**: 2018-08-19T04:47:55Z
> **作者**: nioroso-x3
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/501

## 描述

I'm testing ROCM on a 990FX+AMD FX 8320 platform. The computer has two MSI Vega 56 Airboost in the x16 slots.
Luxmark just shows a black picture as output, and hangs after the 120 second benchmark finishes.

Setting LD_LIBRARY_PROFILE to use the amdgpu-pro 18.20 OpenCL stack works fine.

I can run more tests if needed.

---

## 评论 (6 条)

### 评论 #1 — jlgreathouse (2018-08-18T03:39:41Z)

To verify, have you disabled PCIe atomics by running `export HSA_ENABLE_SDMA=0` in your bash prompt before running?

What version of ROCm is this? What OS?

In addition, could you run the following commands and attach their output? I know the list is big, but they'll hopefully help us recreate and or solve your problem, if the above recommendation does not work.

- `lsmod | grep amdgpu`
- `lsmod | grep amdkfd`
- `groups`
- `lspci | grep VGA`
- `lspci -vvv`
- `lspci -tv`
- After a reboot: `dmesg`
- `/opt/rocm/bin/rocminfo`
- `/opt/rocm/opencl/bin/x86_64/clinfo`

Thanks!

---

### 评论 #2 — nioroso-x3 (2018-08-18T18:10:17Z)

It's working now with HSA_ENABLE_SDMA=0. 
Please update the README and add that it is necesary if the platform doesn't support pcie 3.0.
I thought it was disabled automatically if the platform doesnt support atomics.

---

### 评论 #3 — jlgreathouse (2018-08-18T18:44:20Z)

Can you point to which README you were  using?  The [main ROCm README](https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md) mentions this information twice.

However,  we have a number of different installation direction pages, and I need to work on synchronizing the information on them. Thanks!

---

### 评论 #4 — nioroso-x3 (2018-08-18T19:42:21Z)

This line:

"For Vega10 Users who want to run ROCm without supporting PCIe atomic support must set HSA_ENABLE_SDMA=0"

It should be something like:
"For Vega10 Users who want to run ROCm without supporting PCIe atomic support and also users with platforms with no PCIe atomic support, set HSA_ENABLE_SDMA=0"

I thought it was an option for debugging in platforms with pcie 3.0, not something that must be manually set.

---

### 评论 #5 — jlgreathouse (2018-08-19T04:47:55Z)

Thank you for the recommendation. I have updated the main ROCm README to hopefully be more precise.

---

### 评论 #6 — rkothako (2018-08-28T07:06:51Z)

Hi @jlgreathouse @nioroso-x3 
Its no where mentioned in ROCm wiki page https://github.com/RadeonOpenCompute/ROCm/wiki about 
SDMA disable for Vega10 when we keep in PCIe2 lanes.

_Snippet:_
Supported CPUs
Starting with ROCm 1.8 we have relaxed the use of PCIe Atomics and also PCIe lane choice for Vega10/GFX9 class GPU. So now you can support CPU without PCIe Atomics and also use Gen2 x1 lanes.

---
