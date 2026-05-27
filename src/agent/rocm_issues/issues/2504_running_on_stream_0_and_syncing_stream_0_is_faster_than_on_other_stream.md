# running on stream 0 and syncing stream 0 is faster than on other stream

> **Issue #2504**
> **状态**: closed
> **创建时间**: 2023-09-27T18:01:42Z
> **更新时间**: 2024-08-12T19:22:23Z
> **关闭时间**: 2024-08-12T19:22:23Z
> **作者**: jinhongyii
> **标签**: hardware:Radeon
> **URL**: https://github.com/ROCm/ROCm/issues/2504

## 标签

- **hardware:Radeon** (颜色: #2B113F)

## 描述

I tried two approaches to run a program. In the first approach, I launch all the computation and rccl kernels on stream 0, and use hipStreamSynchronize to sync with stream 0 to ensure all the kernels are completed. In the second approach, I hipStreamCreate a new stream and launch all the kernels on it. Also, I use hipStreamSynchronize to sync with the created stream in the end. It's a bit surprising to me that approach 0 is 25% faster than approach 1. Is this an expected behavior? 
