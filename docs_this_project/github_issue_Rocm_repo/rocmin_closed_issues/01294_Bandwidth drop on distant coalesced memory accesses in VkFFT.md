# Bandwidth drop on distant coalesced memory accesses in VkFFT

- **Issue #:** 1294
- **State:** closed
- **Created:** 2020-11-17T06:11:46Z
- **Updated:** 2021-01-18T13:56:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1294

Hello! I am trying to optimize my Vulkan FFT library (https://github.com/dtolm/VkFFT) for AMD Radeon VII GPU and I am hitting what I think are TLB misses on big seqences (starts at 4MB, before that bandwidth scales almost linearly with size of memory uploaded). This happens when I try to do distant, but coalesced memory accesses, i.e. data are still grouped in 32b-128b transactions but target addresses with > 2^18 bytes between them. As can be seen on the attached graph, (VkFFT Radeon VII with reshuffle, brown line) effective bandwidth drops drastically. If I replace one of such distant accesses with a linear one (VkFFT Radeon VII no 4-step reshuffle, green line) it is possible to recover some of the bandwidth.
The same algorithm on Nvidia 1660Ti (Turing, 288GB/s theoretical bandwidth, L2 TLB covering 8GB of memory) has no such problem on the whole range and bandwidth stays linear. 
Can you help me understand the TLB structure of Vega architecture? Is there a way to access multidimensional data from large buffers more effectively? 
![benchmark](https://user-images.githubusercontent.com/42055491/99352899-c3853780-28a3-11eb-99bf-44504befa804.png)
