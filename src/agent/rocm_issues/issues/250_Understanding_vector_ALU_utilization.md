# Understanding vector ALU utilization

> **Issue #250**
> **状态**: closed
> **创建时间**: 2017-11-12T22:09:46Z
> **更新时间**: 2018-04-10T00:32:57Z
> **关闭时间**: 2018-04-10T00:32:57Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/250

## 描述

What is the best tool to analyze VALU utilization in an OpenCL kernel ?  

In my kernel, each work item `i` performs `Ni` passes through its data buffer `Bi`.  So, two work items may diverge while each item is running through its pass, and they also may diverge when they have a different number of passes, when the work item with fewer passes is waiting for the others to finish. 

I would like to understand what factor hurts the utilization the most.  



---

## 评论 (1 条)

### 评论 #1 — preda (2017-11-15T11:08:57Z)

You could benchmark or run comparative performance analysis. The results may not be portable though (across hardware, or across compiler versions with different optimizations).


---
