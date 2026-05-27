# PCI-E Splitter Support?

> **Issue #450**
> **状态**: closed
> **创建时间**: 2018-07-05T15:07:50Z
> **更新时间**: 2018-07-07T15:57:29Z
> **关闭时间**: 2018-07-07T15:05:01Z
> **作者**: TheKnightCoder
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/450

## 描述

Hi, 
I am in the process of switching from windows to Ubuntu linux. The problem I am having is that the ROCm drivers do not work with my 4 in 1 PCI-E splitter. This worked fine with Windows. Is this a known issue? Is there any way to resolve this?

---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-07-07T15:05:01Z)

ROCm support PCIe Switches.   It dependent on you  which GPU you are running.  If you running Polaris cards you need PCIe Gen3 base PCIe switch since they need PCIe Atomic support.   Not windows driver does not use PCIe Atomics 

---

### 评论 #2 — TheKnightCoder (2018-07-07T15:57:28Z)

@gstoner hmm it was for Vega 56 in a PCIe 3 slot. I have changed my motherboard now without splitter

---
