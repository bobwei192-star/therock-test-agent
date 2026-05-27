# ROCm profiler cannot handle application arguments with spaces

> **Issue #861**
> **状态**: closed
> **创建时间**: 2019-08-12T13:39:11Z
> **更新时间**: 2020-09-30T14:53:55Z
> **关闭时间**: 2020-09-30T14:53:55Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/861

## 描述

Both rocprof and rcprof have the following issue treating `exe -g "2 2 1"` as `exe -g 2 2 1` and cause application failure.
I make one PR and one issue but got no feedback so far.
https://github.com/ROCm-Developer-Tools/rocprofiler/pull/7
https://github.com/GPUOpen-Tools/RCP/issues/29

---

## 评论 (5 条)

### 评论 #1 — djygithub (2019-08-12T22:52:17Z)

Have you tried fully qualifying the path to the executable and parameters as shown following:

```
root@86d10faa209f:/data/RCP/bin# ./rcprof -A -o prj47-rack39.alexnet.2gpu.atp /usr/bin/python3 /root/benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --model=alexnet --forward_only=False --save_summaries_steps 10 --save_model_secs=3600 --print_training_accuracy=True --variable_update=parameter_server --local_parameter_device=cpu --num_batches=100 --num_gpus=2 --batch_size=512
Radeon Compute Profiler V5.6.0 is enabled
.
.
Done warm up
Step Img/sec total_loss top_1_accuracy top_5_accuracy
1 images/sec: 2494.9 +/- 0.0 (jitter = 0.0) 7.199 0.001 0.004
10 images/sec: 2453.4 +/- 13.5 (jitter = 41.3) 7.199 0.005 0.009
20 images/sec: 2427.6 +/- 20.6 (jitter = 48.7) 7.199 0.005 0.008
30 images/sec: 2440.3 +/- 15.0 (jitter = 45.3) 7.199 0.001 0.004
40 images/sec: 2442.1 +/- 11.7 (jitter = 48.8) 7.199 0.000 0.005
50 images/sec: 2437.9 +/- 11.2 (jitter = 41.3) 7.199 0.002 0.007
60 images/sec: 2440.9 +/- 9.6 (jitter = 43.1) 7.199 0.003 0.004
70 images/sec: 2432.9 +/- 11.6 (jitter = 48.3) 7.199 0.001 0.005
80 images/sec: 2434.7 +/- 10.3 (jitter = 48.3) 7.199 0.000 0.003
90 images/sec: 2436.3 +/- 9.3 (jitter = 46.5) 7.200 0.000 0.004
100 images/sec: 2438.5 +/- 8.7 (jitter = 48.0) 7.199 0.000 0.004
----------------------------------------------------------------
total images/sec: 2437.85
----------------------------------------------------------------
Session output path: /data/RCP/bin/prj47-rack39.alexnet.2gpu.atp
root@86d10faa209f:/data/RCP/bin#
```

---

### 评论 #2 — ye-luo (2019-08-13T18:20:34Z)

@djygithub your example doesn't contain a single argument with space inside. All the spaces are used to separate arguments.
In my example, `"2 2 1"` is taken as a whole for `-g` option. Profilers break my intention into `-g 2 2 1` all separately and only the first `2` is passed for `-g` and `exe` cannot understand the later `2 1`.

---

### 评论 #3 — djygithub (2019-08-13T18:35:25Z)

I misunderstood.  Does this work for nvprof? (I will test).  I'll also ask around.

---

### 评论 #4 — ye-luo (2019-08-13T18:57:21Z)

Yes. `nvprof` works.

---

### 评论 #5 — eshcherb (2019-12-04T20:20:29Z)

The PR https://github.com/ROCm-Developer-Tools/rocprofiler/pull/7 is merged

---
