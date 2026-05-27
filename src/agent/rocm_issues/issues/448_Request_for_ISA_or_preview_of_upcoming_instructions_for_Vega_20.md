# Request for ISA or preview of upcoming instructions for Vega 20

> **Issue #448**
> **状态**: closed
> **创建时间**: 2018-07-02T13:49:17Z
> **更新时间**: 2019-12-12T21:02:01Z
> **关闭时间**: 2018-07-07T15:05:45Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/448

## 描述

In particular I'm interested in fp64 advancements, and math function support but I'd like to know what other new instructions might be arriving.  For example, with vega10 we had cross-lane operations (maybe this was just when rocm made it available, and thereabouts of fiji had?) and fp16 vectorized types.

---

## 评论 (3 条)

### 评论 #1 — gstoner (2018-07-07T15:05:45Z)

Nevion,  you know this we can not pre-release information like this. 

---

### 评论 #2 — nevion (2018-07-11T20:56:45Z)

@gstoner I look here: 
https://reviews.llvm.org/search/query/SOt5labuz5hE/#R
http://llvm.org/svn/llvm-project/cfe/trunk/include/clang/Basic/BuiltinsAMDGPU.def

I don't really see a whole lot of new stuff/intrinsics which leads me to believe not all that much is in the works unless you guys are keeping it internal only.

Is there anything marketing et al can clear that is otherwise boring details on upcoming operation types?  Cross-lane operations kind of fit that, for instance.  Even hardware support for fmad/fdiv at double precision would be a great advancement.  If not inline to this topic, maybe you guys can organize and talk about it more properly at gpuopen.com?

---

### 评论 #3 — jlgreathouse (2019-12-12T21:02:01Z)

We have released the new ISA guide for the Vega 20 GPUs: https://gpuopen.com/wp-content/uploads/2019/11/Vega_7nm_Shader_ISA_26November2019.pdf

---
