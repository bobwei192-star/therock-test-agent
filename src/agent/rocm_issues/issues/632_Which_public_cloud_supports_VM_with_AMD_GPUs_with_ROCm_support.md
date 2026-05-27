# Which public cloud supports VM with AMD GPUs with ROCm support?

> **Issue #632**
> **状态**: closed
> **创建时间**: 2018-12-11T07:23:45Z
> **更新时间**: 2018-12-12T18:02:53Z
> **关闭时间**: 2018-12-12T09:53:10Z
> **作者**: ghostplant
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/632

## 描述

Hi,

I'd like to have a try about Tensorflow over ROCm on some cloud VMs.

---

## 评论 (4 条)

### 评论 #1 — ghostplant (2018-12-11T07:31:11Z)

I am not sure if I create a VM on some cloud with AMD GPU provided, whether it will support ROCm or just provide 3D graphic display function.

---

### 评论 #2 — briansp2020 (2018-12-11T13:05:20Z)

I don't know about VM. But if you want to try ROCm in cloud, https://gpueater.com/ has instances with VEGA FE.

---

### 评论 #3 — ghostplant (2018-12-12T09:42:13Z)

Thank you.

---

### 评论 #4 — jlgreathouse (2018-12-12T18:02:53Z)

@briansp2020 has a good answer -- [GPUEater](https://gpueater.com/) does support AMD GPUs. You may also want to look into [Genesis Cloud](https://www.genesiscloud.com/), which also supports AMD GPUs.

---
