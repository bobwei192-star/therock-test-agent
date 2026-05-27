# Is there a way to read GPU memory usage

> **Issue #584**
> **状态**: closed
> **创建时间**: 2018-10-23T21:04:41Z
> **更新时间**: 2020-09-03T12:46:27Z
> **关闭时间**: 2019-05-09T19:02:04Z
> **作者**: hungweitseng
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/584

## 标签

- **Question** (颜色: #cc317c)

## 描述

Is there a way to read the USED GPU memory real-time or from the rcprof trace?

---

## 评论 (5 条)

### 评论 #1 — jlgreathouse (2018-10-23T22:53:59Z)

Internally, we're currently working on a patch to allow this information to be visible through rocm-smi. See [this issue](https://github.com/RadeonOpenCompute/ROC-smi/issues/42) and [this proposed patch](https://github.com/RadeonOpenCompute/ROC-smi/pull/43).

You can get this data out of the following sysfs file: `/sys/class/kfd/kfd/topology/nodes/N/mem_banks/0/used_memory` (and you can get available memory from `/sys/class/kfd/kfd/topology/nodes/N/mem_banks/0/properties` from the field `size_in_bytes`). In this case, `N` should likely be the ROCm agent ID (if you run `rocminfo` look at the Agent value and subtract 1).

---

### 评论 #2 — kentrussell (2018-10-24T13:03:06Z)

The big issue that we have is that the topology/node/N is not a direct correlation to drm/cardN or dri/N . This is being worked on (see https://github.com/RadeonOpenCompute/ROC-smi/issues/42) but for now, you can use this command to look at it in real time until we get it implemented in the SMI:
sudo cat /sys/kernel/debug/dri/0/amdgpu_vram_mm | tail -n 2

Once we close the issue linked by Joe and I, the SMI will have support for it, but for now the easiest way for the GPU is to use my command here. Joe's command works well but can be problematic if you have supported CPU nodes that KFD uses, since they don't have used_memory. It's a complicated web




---

### 评论 #3 — hungweitseng (2018-11-02T20:03:49Z)

Thanks. Will try this work-around first.

---

### 评论 #4 — kentrussell (2019-03-12T12:09:07Z)

This will be available in the 2.3 release via the SMI

---

### 评论 #5 — jlgreathouse (2019-05-09T19:02:04Z)

This has been available since ROCm 2.3 using `rocm-smi --showmeminfo vram`. I'll note that ROCm 2.3 and 2.4 reversed the "used" and "total" print-outs. The numbers are accurate, but the labels are reversed. This should be fixed in 2.5 I believe.

---
