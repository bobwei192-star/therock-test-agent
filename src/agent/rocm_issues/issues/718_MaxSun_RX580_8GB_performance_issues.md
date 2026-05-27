# MaxSun RX580 8GB performance issues

> **Issue #718**
> **状态**: closed
> **创建时间**: 2019-02-26T14:20:55Z
> **更新时间**: 2019-03-08T16:05:02Z
> **关闭时间**: 2019-03-08T16:05:02Z
> **作者**: MatPoliquin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/718

## 描述

I installed ROCm and tensorflow using the aieater script:
[aieater](https://github.com/aieater/rocm_tensorflow_info)

I get expected performance on standard benchmarks:
Cifar10 peak        ~8500 examples/sec  
Alexnet forward    0.051s/batch 
Alexnet backward  0.190s/batch

However for OpenAI baselines PPO2 implementation I get half the performance of a p106-100 on the same computer

command used from baselines:
[OpenAI baselines](https://github.com/openai/baselines)
```
python3 -m baselines.run --alg=ppo2 --env=PongNoFrameskip-v4 --num_timesteps=2e7
```
I haven't have the time to profile yet, I wounder if someone else ran into same performance issues


System:
Ubuntu 18.10
Asus x99-e ws motherboard
Xeon e5 2667 v3
32GB DDR4 2400mhz

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-03-08T16:05:02Z)

I recommend that you taking this issue to [our TensorFlow issue tracker](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues).

---
