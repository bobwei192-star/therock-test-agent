# FP16 Support Issue

> **Issue #289**
> **状态**: closed
> **创建时间**: 2017-12-28T02:08:38Z
> **更新时间**: 2018-01-02T06:06:22Z
> **关闭时间**: 2017-12-28T18:48:14Z
> **作者**: FullZing
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/289

## 描述

My question is whether RX580 support OpenCL FP16 computation(cl_khr_fp16)?

can anyone provide FP16 information about RX580, I cann't find accurate information about this.


---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-12-28T18:48:14Z)

RX580 support Float16 but scaler only, So no Packed instruction support.  It is GFX8 based device. 

---

### 评论 #2 — FullZing (2018-01-02T06:04:09Z)

@gstoner
Thanks for your help.  
how about RX vega? Does it support vector computation, like vload or vstore instruction? or can you tell me how to get accurate/more OpenCL information about AMD GPU. 
I found it is difficult to get these information.   
Thanks in advance. 

---
