# RX 6700s performance test - low memory clock speed

> **Issue #1803**
> **状态**: closed
> **创建时间**: 2022-09-02T15:39:54Z
> **更新时间**: 2023-12-19T06:37:12Z
> **关闭时间**: 2023-12-19T06:37:12Z
> **作者**: MatPoliquin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1803

## 描述

Specs:

- AMD RX 6700s
- AMD 6800HS 8C/16T
- 2x 8GB DDR5 @4800Mhz
- OpenSuse Tumbleweed - Kernel: 5.19.2-1-default
- EDIT: same problem with Ubuntu 22.04 as well
- Tensorflow 2.9.2

The performance of the RX 6700s seems to be a bit low for the specs. When I check rocm-smi (see pic below) The memory clock is capped at 875Mhz when the real maximum should be twice as much (as reported by GPU-Z and official specs). When I display the list of available frequencies with rocm-smi the maximum is 875Mhz as well even if I set the performance mode to high

![rocm-smi](https://user-images.githubusercontent.com/7024551/188184293-39884dbe-cd10-4db7-9b0d-49b9a5ff6e9b.png)

Steps to reproduce:

```
pip3 install tensorflow-rocm
git clone https://github.com/tensorflow/benchmarks.git
cd benchmarks/scripts/tf_cnn_benchmarks
```

```
python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50
```

Result:

```
Step	Img/sec	total_loss
1	images/sec: 99.3 +/- 0.0 (jitter = 0.0)	7.765
10	images/sec: 99.5 +/- 0.1 (jitter = 0.2)	8.049
20	images/sec: 99.3 +/- 0.1 (jitter = 0.3)	7.808
30	images/sec: 98.8 +/- 0.2 (jitter = 0.6)	7.976
40	images/sec: 98.4 +/- 0.2 (jitter = 1.2)	7.591
50	images/sec: 98.1 +/- 0.2 (jitter = 1.1)	7.549
60	images/sec: 97.9 +/- 0.2 (jitter = 1.0)	7.819
70	images/sec: 97.7 +/- 0.1 (jitter = 0.7)	7.819
80	images/sec: 97.6 +/- 0.1 (jitter = 0.5)	7.848
90	images/sec: 97.5 +/- 0.1 (jitter = 0.5)	8.026
100	images/sec: 97.4 +/- 0.1 (jitter = 0.5)	8.030
----------------------------------------------------------------
total images/sec: 97.40
----------------------------------------------------------------
```

You can see the performance is lower, as expected with a 875Mhz memory clock speed

Anybody else have this issue?

---

## 评论 (1 条)

### 评论 #1 — nartmada (2023-12-18T19:32:58Z)

Hi @MatPoliquin, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.


---
