# Segmentation fault on gfx900 in rocm4.5.2

> **Issue #1704**
> **状态**: closed
> **创建时间**: 2022-03-16T20:33:56Z
> **更新时间**: 2022-03-19T20:28:25Z
> **关闭时间**: 2022-03-19T20:28:25Z
> **作者**: robosina
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1704

## 描述

I installed `rocm4.5.2` on my machine, and according to the `rocminfo` output, the system has detected a graphic card with the model number `gfx900`. 

```bash
Agent 3                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-021501b4400c2064               
  Marketing Name:          Radeon RX Vega                     
  Vendor Name:             AMD      
```
I attempted to compile the HIP examples, but they all crashed due to a segmentation fault or a core dump. 

```bash
$ cd HIP-Examples/

$ cd reduction/

$ make
     make: 'reduction' is up to date.

$ ./reduction 
      Usage: ./reduction num_of_elems
      using default value: 52428800
      ARRAYSIZE: 52428800
      Array size: 200 MB
      Segmentation fault (core dumped)

$ ./reduction 10
      ARRAYSIZE: 10
      Array size: 3.8147e-05 MB
      Segmentation fault (core dumped)
```

is gfx900  supported? (I noticed in the [Documentation](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#confirm-you-have-a-rocm-capable-gpu) that the gfx9 is supported so what about gfx900?)!! Does anyone have a solution to the problem?
Thanks. 

---

## 评论 (2 条)

### 评论 #1 — ex-rzr (2022-03-17T07:58:53Z)

I'd recommend you to run with `AMD_SERIALIZE_KERNEL=3 AMD_SERIALIZE_COPY=3 AMD_LOG_LEVEL=4` environment variables. It'll show you where the program crashes.

---

### 评论 #2 — robosina (2022-03-19T20:28:22Z)

@ex-rzr , Thanks, I have fixed the issue by providing architecture target of the gpu in the compilation process.

---
