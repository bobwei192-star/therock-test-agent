# Bandwidth drop on distant coalesced memory accesses in VkFFT

> **Issue #1294**
> **状态**: closed
> **创建时间**: 2020-11-17T06:11:46Z
> **更新时间**: 2021-01-18T13:56:39Z
> **关闭时间**: 2021-01-18T13:56:39Z
> **作者**: DTolm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1294

## 描述

Hello! I am trying to optimize my Vulkan FFT library (https://github.com/dtolm/VkFFT) for AMD Radeon VII GPU and I am hitting what I think are TLB misses on big seqences (starts at 4MB, before that bandwidth scales almost linearly with size of memory uploaded). This happens when I try to do distant, but coalesced memory accesses, i.e. data are still grouped in 32b-128b transactions but target addresses with > 2^18 bytes between them. As can be seen on the attached graph, (VkFFT Radeon VII with reshuffle, brown line) effective bandwidth drops drastically. If I replace one of such distant accesses with a linear one (VkFFT Radeon VII no 4-step reshuffle, green line) it is possible to recover some of the bandwidth.
The same algorithm on Nvidia 1660Ti (Turing, 288GB/s theoretical bandwidth, L2 TLB covering 8GB of memory) has no such problem on the whole range and bandwidth stays linear. 
Can you help me understand the TLB structure of Vega architecture? Is there a way to access multidimensional data from large buffers more effectively? 
![benchmark](https://user-images.githubusercontent.com/42055491/99352899-c3853780-28a3-11eb-99bf-44504befa804.png)


---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2020-11-17T13:24:45Z)

@DTolm ,
  
   Thank you for reaching out. 
   Request you to kindly furnish the logs for the following commands :   

    1) /opt/rocm/bin/rocminfo
    2) /opt/rocm/bin/rocm-bandwidth-test
    3) /opt/rocm/bin/rocm-bandwidth-test -t 
    4) /opt/rocm/bin/rocm-smi

    These shall help us understand your problem / config better.

Thanks 

---

### 评论 #2 — DTolm (2020-11-17T15:56:40Z)

Here:
[rocm-smi.txt](https://github.com/RadeonOpenCompute/ROCm/files/5554598/rocm-smi.txt)
[rocm-bandwidth-test-t.txt](https://github.com/RadeonOpenCompute/ROCm/files/5554599/rocm-bandwidth-test-t.txt)
[rocm-bandwidth-test.txt](https://github.com/RadeonOpenCompute/ROCm/files/5554600/rocm-bandwidth-test.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5554602/rocminfo.txt)


---

### 评论 #3 — DTolm (2020-11-26T16:26:43Z)

Hello. The issue is also present in 6800XT. However, I managed to solve it by splitting bounded buffer in a big amount of 16KB logical memory buffers and using logical addressing in the shader. This resulted in up to 5x performance increase for sequences taking ~1GB. Also, this somehow led to better L3 cache reuse on Radeon 6800XT (way more performance improvement than expected), but as I don't own the card and ask others to run code, I am not able to do more tests than I want to. Hope this information can be helpful and if you would like to discuss this in more detail, feel free to contact me. Otherwise, you can close this issue.
![vkfft_benchmark_single_new](https://user-images.githubusercontent.com/42055491/100374311-59d7fc80-300c-11eb-8d98-ed8d9d85194f.png)
![vkfft_benchmark_3d_new](https://user-images.githubusercontent.com/42055491/100374316-5d6b8380-300c-11eb-9484-5c5c53dbe43d.png)



---

### 评论 #4 — ROCmSupport (2021-01-18T13:56:39Z)

@DTolm,

   Thank you for the information. We shall check the same. 
   Closing this ticket for now.

---
