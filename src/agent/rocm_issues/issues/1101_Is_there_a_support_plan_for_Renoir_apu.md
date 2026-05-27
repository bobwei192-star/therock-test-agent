# Is there a support plan for Renoir apu ?

> **Issue #1101**
> **状态**: closed
> **创建时间**: 2020-05-08T08:20:29Z
> **更新时间**: 2020-12-16T05:23:24Z
> **关闭时间**: 2020-12-15T10:08:53Z
> **作者**: changephilip
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1101

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Hello,
AMD has announced that more than 135 laptops with Renoir will come in 2020.
Some benchmarks of 4800u/4800H have shown Renoir's high performance.

This month(May,2020), a lot of laptops(Asus,Acer,HP,Lenovo and so on) released worldwide. 

On Raven Ridge ,ROCm only has limited support such as openCL.
Will ROCm support more features for Renoir APUs?



---

## 评论 (8 条)

### 评论 #1 — btspce (2020-05-08T12:14:05Z)

Im also interested in any info regarding this from AMD. Our company don't want to buy Intel/nvidia based laptops and the opencl performance from these apus is beginning to get "good enough". Unfortunately we hit multiple problems with AMD's OpenCL stacks such as  getting 33% of the performance on rocm 3.3 compared to the extracted opencl from amdgpu-pro. But OpenCL from amdgpu-pro breaks mesa OpenGL (please fix this) so we cant use that with OpenGL based apps like Davinci Resolve. ROCm works but downclocks all cores on Raven Ridge 2700u to 399MHz when starting an opencl enabled app which makes the computer unusable. I suspect the low rocm performance on raven ridge is due to these clocking issues of the gpu.

Here is a few of the issues talked about above so far without progress or answer..
https://github.com/RadeonOpenCompute/ROCm/issues/1089
https://github.com/RadeonOpenCompute/ROCm/issues/981
https://github.com/RadeonOpenCompute/ROCm/issues/976


---

### 评论 #2 — ye-luo (2020-05-11T22:27:54Z)

Just installed rocm3.3 on ubuntu 20.04 with 4700u.
```
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
This issue may not be directly Renoir related. Hopefully the situation will improve.

---

### 评论 #3 — ye-luo (2020-05-18T21:42:45Z)

Adding user to the render group. I can get rocminfo and rocm-smi working.
```
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Renoir                             
  Vendor Name:             AMD                       
...
```

---

### 评论 #4 — changephilip (2020-05-19T01:19:36Z)

> 
> 
> Adding user to the render group. I can get rocminfo and rocm-smi working.
> 
> ```
> *******                  
> Agent 2                  
> *******                  
>   Name:                    gfx900                             
>   Marketing Name:          Renoir                             
>   Vendor Name:             AMD                       
> ...
> ```

That 's great!
I will try it as soon as I receive my new ryzen laptop.

---

### 评论 #5 — ye-luo (2020-05-19T02:57:43Z)

@changephilip could barely run something. I will wait rocm 3.5 to see if the situation could improve.

---

### 评论 #6 — alexanderkjeldaas (2020-07-03T13:11:58Z)

Have you tried https://bruhnspace.com/en/bruhnspace-rocm-for-amd-apus/ ?


---

### 评论 #7 — a-repko (2020-10-15T14:16:47Z)

I recently tried hard to run OpenCL on AMD Ryzen 7 PRO 4750G with Gentoo Linux, and I was not successful with ROCm (tried various versions, such as 3.5.1, 3.7, 3.8, with kernels 5.8.14 and 5.9; see also #1219). For example, there are GPU resets with `clinfo`, which moreover leaves 99% GPU utilization. When trying some OpenCL program, system usually freezes. Nevertheless, it appears (#883) that it is possible to run ROCm 3.7 with bundled ROCk kernel driver on Ubuntu; I haven't tried it.

What finally enabled me to run OpenCL flawlessly, are the closed-source libraries from amdgpu-pro, which can be neatly installed by this script (after removing the ROCm stack from the system):
https://gist.github.com/kytulendu/3351b5d0b4f947e19df36b1ea3c95cbe
It just copies some libraries into `/opt/amdgpu`, `/opt/amdgpu-pro` and `/etc/OpenCL/vendors`, and puts some file into `/etc/ld.so.conf.d` to notify the system about the new libraries.

When I compare the performance of OpenCL on Raven Ridge (ROCm 3.1) and Renoir (amdgpu-pro 20.30), then Renoir is about 8% faster, which can be perhaps attributed to a newer architecture. It's a pity that the frequency of iGPU can be chosen (obviously by rocm-smi or /sys interface) only between 700 MHz and 2100 MHz (besides 200 MHz). The latter one can be run sustainably at full load, consuming around 40 W, while having ca. 50% energy efficiency of the 700 MHz mode.

In case somebody is interested, I'm attaching `clinfo` outputs for APU Renoir on linux kernel 5.8.14 (kernel 5.9 gives wrong number of 28 CU instead of 8 CU), and also APU Raven Ridge on linux kernel 4.19 with ROCm 3.1 (this gives 11 CU instead of correct 10 CU, but it doesn't seem to matter)
[clinfo_ROCm_380.txt](https://github.com/RadeonOpenCompute/ROCm/files/5385269/clinfo_ROCm_380.txt)
[clinfo_amdgpu_pro.txt](https://github.com/RadeonOpenCompute/ROCm/files/5385272/clinfo_amdgpu_pro.txt)
[clinfo_RavenRidge_ROCm_310.txt](https://github.com/RadeonOpenCompute/ROCm/files/5385274/clinfo_RavenRidge_ROCm_310.txt)


---

### 评论 #8 — ROCmSupport (2020-12-15T10:08:53Z)

Hi @changephilip 
**We are not officially supporting Renior APU for now.**
But it might still work. I have seen many posts that people are using Renior with ROCm and its working perfect too.

---
