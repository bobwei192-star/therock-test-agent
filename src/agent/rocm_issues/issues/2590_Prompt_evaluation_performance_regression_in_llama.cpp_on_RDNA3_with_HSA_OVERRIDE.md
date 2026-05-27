# Prompt evaluation performance regression in llama.cpp on RDNA3 with HSA_OVERRIDE_GFX_VERSION=11.0.1 vs 11.0.0

> **Issue #2590**
> **状态**: closed
> **创建时间**: 2023-10-20T16:12:53Z
> **更新时间**: 2024-07-19T17:14:08Z
> **关闭时间**: 2024-07-19T17:14:08Z
> **作者**: Googulator
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2590

## 描述

We're evaluating llama.cpp with ROCm offloading on various RDNA3 GPUs (primarily RX 7800 XT and RX 7900 XT).

On initial testing, we found that a 13b model with Q6_K quantization fully offloaded to GPU (-ngl 43) showed significantly slower prompt evaluation times on the 7800 compared to the 7900, far beyond what would be expected from the relative performance difference between these 2 GPUs. On the 7800, prompt evaluation would take more than a minute on our example prompt, while it was near instantaneous (less than a second) on the 7900.

Upon further investigation, the RX 7800 shows a 3 second penalty for every 64 tokens of prompt (0-64 tokens 3 seconds, 65-128 tokens 6s, 129-192 tokens 9s, and so on) over the 7900.

Since the 7800 is recognized by ROCm as gfx1101, vs gfx1100 on the 7900, we tried setting HSA_OVERRIDE_GFX_VERSION=11.0.0, which led to massive performance improvement, with the 7800 only proportionally slower than the 7900, as expected based on the specifications. We then tested HSA_OVERRIDE_GFX_VERSION=11.0.1 (and 11.0.2) on the 7900, and saw the exact same performance issue as on the 7800.

The testing was performed on Ubuntu 22.04.3 Server, using ROCm v5.7.0, apparently the latest version available for this version of Ubuntu.
