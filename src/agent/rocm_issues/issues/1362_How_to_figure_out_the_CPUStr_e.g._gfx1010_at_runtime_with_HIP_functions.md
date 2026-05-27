# How to figure out the CPUStr e.g. "gfx1010" at runtime with HIP functions?

> **Issue #1362**
> **状态**: closed
> **创建时间**: 2021-01-20T05:15:03Z
> **更新时间**: 2021-01-20T15:59:56Z
> **关闭时间**: 2021-01-20T15:59:56Z
> **作者**: fwinter
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/1362

## 标签

- **Question** (颜色: #cc317c)

## 描述

My application uses LLVM's AMDGPU backend to generate GPU kernels at runtime. In order to instantiate the correct TargetMachine I'd need to have the "CPUString" like "gfx908", "gfx1010", etc.

The HIP functions hipDeviceComputeCapability and hipDeviceGetName get me close but not really there without some educated guessing. Compute capability is returned as major=10, minor=1. How do I arrive from that to the correct CPU string "gfx1010"? It can't be "gfx${major}${minor}0" since that wouldn't work for "gfx908". This needs to work for any card.

If this is currently not possible can I suggest adding those features?


---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-01-20T09:42:36Z)

@fwinter ,
You may check the [HIP programming interface](https://github.com/RadeonOpenCompute/ROCm/blob/master/HIP-API_Guide_v4.0.pdf) for specific HIP API

You may also get the same information using any shell. For eg :
      `/opt/rocm/bin/rocminfo | less | grep gfx`
  Which shall give you the output like following 
   
```
  Name:                    gfx900
      Name:                    amdgcn-amd-amdhsa--gfx900:xnack-

```  

This can be encapsulated in any string & pass to your host code which you are using to write the kernel.

Hope this helps.  

Let us know, if this does not solves the problem, I shall check more.

---

### 评论 #2 — ROCmSupport (2021-01-20T15:58:57Z)

@fwinter ,

  you can use API :  `hipGetDeviceProperties`

```
     hipGetDeviceProperties(&props, deviceId);
    std::cout<<"gcnArchName: "<<props.gcnArchName<<std::endl;
```

gives me desired output 

`gcnArchName: gfx906`

Hope this solves your query 

---
