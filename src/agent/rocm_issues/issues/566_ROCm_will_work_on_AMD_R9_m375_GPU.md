# ROCm will work on AMD R9 m375 GPU?

> **Issue #566**
> **状态**: closed
> **创建时间**: 2018-10-01T18:03:50Z
> **更新时间**: 2018-10-02T02:07:24Z
> **关闭时间**: 2018-10-02T02:07:17Z
> **作者**: mowagih96
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/566

## 描述

As the title says I want to know whether the tool will work or not as I need to download linux for it and bunch of other stuff that should be soon or find another alternative because my time limitation.
And yes I checked the supported GPUs page but I couldn't find it there neither in the supported nor in the not supported section

---

## 评论 (3 条)

### 评论 #1 — briansp2020 (2018-10-01T18:10:06Z)

R9 m375 is old and is not supported in ROCm. ROCm supports Polaris and newer which means Radeon RX or Vega.
See https://github.com/RadeonOpenCompute/ROCm#supported-gpus

---

### 评论 #2 — mowagih96 (2018-10-01T18:15:02Z)

@briansp2020 Thanks for your reply. Ok do you know any other alternative to HIP? as I need it to execute and run CUDA code on my GPU, gpuocelot will do the trick or do you know others? and yea I can't afford buying a new laptop for the sake of executing CUDA code.



---

### 评论 #3 — jlgreathouse (2018-10-02T02:07:17Z)

@briansp2020 is correct. The R9 M375 is neither supported nor enabled in ROCm. This is a "GCN 1.0" GPU (also known as Southern Islands, of gfx6). gfx6 GPUs are not supported in ROCm, as described [on our more detailed hardware requirements page](https://rocm.github.io/hardware.html). If you need this GPU to run OpenCL, you could try the amdgpu-pro drivers.

I can't give you any official recommendations for how to run CUDA applications on this device. You could try academic translation frameworks, such as [SnuCL-Tr](http://snucl.snu.ac.kr/snucl-tr.html), [CU2CL](http://chrec.cs.vt.edu/cu2cl/), or [Swan](https://github.com/Acellera/swan). I can't guarantee that any of these applications will do what you want, and AMD does not offer support for these applications.

---
