#  tensorflow-rocm-enhanced installed, but training uses CPU only

- **Issue #:** 1217
- **State:** closed
- **Created:** 2020-09-13T02:52:50Z
- **Updated:** 2020-12-16T05:32:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/1217

**System information**
- OS Platform and Distribution (e.g., Linux Ubuntu 16.04): Ubuntu 20.04.1 LTS
- TensorFlow installed from (source or binary): binary
- TensorFlow version (use command below): v2.3.0-rc1-2368-gc1ffa3658f 2.3.0
- Python version: 3.7.9
- GPU model and memory: Rx 580

The GPU does not get used at all. For example, with ai-benchmark 0.1.2, which can be installed with: `pip install ai-benchmark`

```
from ai_benchmark import AIBenchmark
benchmark = AIBenchmark(use_CPU=False, verbose_level=1)
results = benchmark.run()
```

GPU load 0% during the whole process

```
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr   SCLK     MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
0    35.0c  51.191W  1300Mhz  300Mhz  16.86%  auto  152.0W    6%   0%    
================================================================================
==============================End of ROCm SMI Log ==============================
```