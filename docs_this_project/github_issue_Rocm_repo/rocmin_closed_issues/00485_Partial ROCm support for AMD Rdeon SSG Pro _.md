# Partial ROCm support for AMD Rdeon SSG Pro ?

- **Issue #:** 485
- **State:** closed
- **Created:** 2018-08-01T06:55:11Z
- **Updated:** 2023-04-01T08:39:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/485

Hey guys, after several GitHub issues : 
here https://github.com/ROCmSoftwarePlatform/Tensile/issues/300 and
https://github.com/baidu-research/DeepBench/issues/105

I am under impression that, ROCm support for AMD SSD Pro is not fully operational. I also got to know that AMD SSD Pro is not one of the flagship deep learning GPUs. ROCm support should be generalised across entire range of radeon GPUs so that every faction can use it properly not just certain brands of radeon instinct GPUs. I have AMD Radeon Instinct SSD Pro and ROCm does not behave as intended with roubles giving me 1/10 of performance of MI25. I can extract 90% performance of GCN assembly level code but not from ROCm framework. 

Why it is like this ? Any specific reason to do that ?