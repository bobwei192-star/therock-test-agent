# just a suggestion about apu

> **Issue #635**
> **状态**: closed
> **创建时间**: 2018-12-18T04:20:01Z
> **更新时间**: 2021-01-07T10:47:52Z
> **关闭时间**: 2021-01-07T10:47:51Z
> **作者**: halalia
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/635

## 描述

leaving raven-ridge apus'  integrated gpus unsupported seems a pity

it could be a nice platform to deploy deep models on apu computers to run the tasks as "evaluate" the models

the compute power of apus' igp is at a unsuited\unmatched level, too strong for office task,  but weak for professional application. Evaluating,(not training) deep learning model might be ok, and i guess this idea is similar to the first apus some 8 years ago 

---

## 评论 (6 条)

### 评论 #1 — nevion (2018-12-18T05:35:59Z)

aww shucks.  I got a thinkpad a485 coming and rocm played a role in that decision as well as some decent opencl support.  I didn't know that raven ridge was in this mostly unsupported state until now.

Support ROCm everywhere, not just the data center, amd.  Us GPU developers have to develop our code somewhere, and if you don't have it on the commodity stuff it doesn't pick up steam on the FOSS side of things. Here I was hoping to add opencl image processing to various astronomy softwares and this just threw a wrench in it.

---

### 评论 #2 — emerth (2018-12-18T18:28:43Z)

For developers who cannot afford to buy professional AMD GPU cards, APUs would be a fantastic option, if ROCm supported them. As well the power consumption is a lot lower for a 2400G than an RX Vega 64. 

It would be great if the APUs were supported.

---

### 评论 #3 — 3D-360 (2018-12-21T20:25:18Z)

I like AMD's APU architecture because of the shared memory between the CPU & GPU.  In 2014 my team used OpenCL & shared memory on a Kaveri APU  to outperform a much bigger discrete Nvidia card running CUDA.   I *REALLY* want to use AMD APUs in an autonomous system, and I am assuming that APUs like Raven Ridge will soon have full support of ROCm (not just OpenCL).  

Nvidia has proven than small Jetson boards can do useful work in autonomous systems.  Is it realistic to expect that HCC/ROCm will work on APUs like Raven Ridge in the first half of 2019, or should I bail on AMD APUs and go back to Nvidia/Jetson?

---

### 评论 #4 — luyatshimbalanga (2018-12-29T21:08:24Z)

@3D-360 See [this comment](https://github.com/RadeonOpenCompute/ROCm/issues/608#issuecomment-450519762). More works to be done but at least Raven Ridge is supported.

---

### 评论 #5 — chophshiy (2019-04-27T22:16:47Z)

@nevion 
I'm in the same boat here.  Have you had any luck getting things working since then?


---

### 评论 #6 — ROCmSupport (2021-01-07T10:47:51Z)

Hi @halalia 
We are not supporting right now. Please stay tuned for the future updates.
Thank you.

---
