#  tensorflow-rocm-enhanced installed, but training uses CPU only

> **Issue #1217**
> **状态**: closed
> **创建时间**: 2020-09-13T02:52:50Z
> **更新时间**: 2020-12-16T05:32:52Z
> **关闭时间**: 2020-12-16T04:12:40Z
> **作者**: ffleader1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1217

## 描述

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

---

## 评论 (10 条)

### 评论 #1 — xuhuisheng (2020-09-13T09:43:12Z)

I had met errors on tf, when tf met loading so error, then it fail to cpu. please check the output if there is any error or warning logs.

---

### 评论 #2 — ffleader1 (2020-09-13T12:00:55Z)

> I had met errors on tf, when tf met loading so error, then it fail to cpu. please check the output if there is any error or warning logs.

That sounds reasonable, but where can I find the loading logs? I mean all the imports are fine, no err so I am not sure where to look.

---

### 评论 #3 — baryluk (2020-09-25T17:31:01Z)

I got it working with `tensorflow-rocm`.  I am on AMD Fury X (FIJI, GFX8), 4GB VRAM.

Not sure what is `tensorflow-rocm-enhanced`, as the pypi page doesn't provide much info about it.

Most of the benchmarks in the AIBenchmark are rather short, so it might be hard to see the GPU high often. In my expirience a majority of time is spend in the host waiting for clang and linker to finish building GPU kernels, then they execute in a second or two, but VRAM is usually pretty high (close to 100%). In fact one of the benchmarks in the AIBenchmark loads my system so high that xorg and amdgpu driver crashes.

Could you provide the output of the `benchmark.run()` ?

Before my run crashes I got:

```
root@debian:~# LD_LIBRARY_PATH=/opt/rocm-3.8.0/lib ROCM_PATH=/opt/rocm-3.8.0 python3
Python 3.8.5 (default, Aug  2 2020, 15:09:07) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from ai_benchmark import AIBenchmark
>>> benchmark = AIBenchmark(use_CPU=False, verbose_level=1)

>>   AI-Benchmark-v.0.1.2   
>>   Let the AI Games begin..

>>> results = benchmark.run()
*  TF Version: 2.3.1
*  Platform: Linux-5.7.0-1-amd64-x86_64-with-glibc2.29
*  CPU: N/A
*  CPU RAM: 126 GB
*  GPU/0: Fiji [Radeon R9 FURY / NANO Series]
*  GPU RAM: 3.7 GB
*  CUDA Version: N/A
*  CUDA Build: N/A

The benchmark is running...
The tests might take up to 20 minutes
Please don't interrupt the script

1/19. MobileNet-V2

1.1 - inference | batch=50, size=224x224: 60.8 ± 2.8 ms
1.2 - training  | batch=50, size=224x224: 7848 ± 70 ms

2/19. Inception-V3

2.1 - inference | batch=20, size=346x346: 120 ± 4 ms
2.2 - training  | batch=20, size=346x346: 240474.0 ± 0.0 ms

3/19. Inception-V4

3.1 - inference | batch=10, size=346x346: 145 ± 1 ms
3.2 - training  | batch=10, size=346x346: 180127.0 ± 0.0 ms

4/19. Inception-ResNet-V2

4.1 - inference | batch=10, size=346x346: 186 ± 13 ms
4.2 - training  | batch=8, size=346x346: 289089.0 ± 0.0 ms

5/19. ResNet-V2-50

5.1 - inference | batch=10, size=346x346: 75.0 ± 0.0 ms
5.2 - training  | batch=10, size=346x346: 131282.0 ± 0.0 ms

6/19. ResNet-V2-152

6.1 - inference | batch=10, size=256x256: 115681.0 ± 0.0 ms
6.2 - training  | batch=10, size=256x256: 246965.0 ± 0.0 ms

7/19. VGG-16

7.1 - inference | batch=20, size=224x224: 406 ± 189 ms
7.2 - training  | batch=2, size=224x224: 958 ± 509 ms

8/19. SRCNN 9-5-5

8.1 - inference | batch=10, size=512x512: 82.4 ± 4.5 ms
8.2 - inference | batch=1, size=1536x1536: 71.6 ± 1.0 ms
2020-09-25 17:58:05.969077: F tensorflow/stream_executor/rocm/rocm_dnn.cc:3527] Failed to allocate scratch memory - Failed to allocate the requested memory size (1677721600).
	You can set the env var TF_CUDNN_WORKSPACE_LIMIT_IN_MB to a larger number (e.g. 8192) to increase the max memory limit.
	Increasing the max memory limit might help resolve this error
Aborted


```

Some of the kernels take minutes to build by clang, on my fast CPU.

Some benchmarks are super slow because this GPU only has 3.7GB of main VRAM, but many tests require 4GB or a bit more.


EDIT: I installed `tensorflow-rocm-enhanced` and it is faster:

```
>>> results = benchmark.run()
*  TF Version: 2.3.1
*  Platform: Linux-5.7.0-1-amd64-x86_64-with-glibc2.29
*  CPU: N/A
*  CPU RAM: 126 GB
*  GPU/0: Fiji [Radeon R9 FURY / NANO Series]
*  GPU RAM: 3.7 GB
*  CUDA Version: N/A
*  CUDA Build: N/A

The benchmark is running...
The tests might take up to 20 minutes
Please don't interrupt the script

1/19. MobileNet-V2

1.1 - inference | batch=50, size=224x224: 62.2 ± 5.2 ms
1.2 - training  | batch=50, size=224x224: 8628 ± 53 ms

2/19. Inception-V3

2.1 - inference | batch=20, size=346x346: 116 ± 4 ms
2.2 - training  | batch=20, size=346x346: 2272 ± 12 ms

3/19. Inception-V4

3.1 - inference | batch=10, size=346x346: 141.6 ± 0.5 ms
3.2 - training  | batch=10, size=346x346: 1809 ± 300 ms

4/19. Inception-ResNet-V2

4.1 - inference | batch=10, size=346x346: 155.7 ± 0.8 ms
4.2 - training  | batch=8, size=346x346: 1153 ± 7 ms

5/19. ResNet-V2-50

5.1 - inference | batch=10, size=346x346: 75.3 ± 0.5 ms
5.2 - training  | batch=10, size=346x346: 245.2 ± 0.4 ms

6/19. ResNet-V2-152

6.1 - inference | batch=10, size=256x256: 109.3 ± 0.6 ms
6.2 - training  | batch=10, size=256x256: 393 ± 2 ms

7/19. VGG-16

7.1 - inference | batch=20, size=224x224: 360 ± 7 ms
7.2 - training  | batch=2, size=224x224: 795 ± 295 ms

8/19. SRCNN 9-5-5

8.1 - inference | batch=10, size=512x512: 86.4 ± 9.0 ms
8.2 - inference | batch=1, size=1536x1536: 75.8 ± 3.6 ms
2020-09-25 18:06:22.784247: F tensorflow/stream_executor/rocm/rocm_dnn.cc:3527] Failed to allocate scratch memory - Failed to allocate the requested memory size (1677721600).
	You can set the env var TF_CUDNN_WORKSPACE_LIMIT_IN_MB to a larger number (e.g. 8192) to increase the max memory limit.
	Increasing the max memory limit might help resolve this error
Aborted

```

There is still a lot of PCIe bus traffic when doing training due to the training data set size.

Also second run was faster because all the GPU kernels were already cached (`/root/.cache/miopen`).


---

### 评论 #4 — ffleader1 (2020-09-25T22:54:47Z)

Sorry. As soon as I know Tensorflow-DirectML was released one or two week ago, I just wiped that Ubuntu partition from my PC and use Windows for training. I know the speed is basically 1/5 Rocm, but after spending 2 days of pulling my hair out while installing/uninstalling the various version of Ubuntu and Rocm, but still come up short, I decided to go with a solution that "just work". This is just my hobby so I do not mind much.

Anyway, about this problem, as you can see, in your code
```
*  TF Version: 2.3.1
*  Platform: Linux-5.7.0-1-amd64-x86_64-with-glibc2.29
*  CPU: N/A
*  CPU RAM: 126 GB
*  GPU/0: Fiji [Radeon R9 FURY / NANO Series]
*  GPU RAM: 3.7 GB
*  CUDA Version: N/A
*  CUDA Build: N/A
````

You have the GPU line, but I don't. Mine stopped basically at CPU RAM. That's why I am 99% positive that the rocm install process messed up some point and failed to detect my GPU. Running this benchmark on Windows on tensorflow-DirectML does indeed show the GPU.

---

### 评论 #5 — baryluk (2020-09-25T23:33:18Z)

@ffleader1 Thanks for extra info.

Just for completeness, what CPU and motherboard are you using?

It is good to inspect for example what `/opt/rocm-3.8.0/bin/rocminfo` says, i.e. if it detects everything correctly.


---

### 评论 #6 — ffleader1 (2020-09-26T01:58:34Z)

@baryluk Oh. A R5 3600X with a MSI MPG X570 Gaming plus

---

### 评论 #7 — baryluk (2020-09-26T20:41:37Z)

@ffleader1 Thanks. That should work then. I guess something with installation process was wrong probably.

---

### 评论 #8 — ROCmSupport (2020-12-15T13:01:37Z)

Hi @ffleader1 
Can you please try with ROCm 3.10 on the same machine and update.
Request to close this issue, if it works in 3.10.
Thank you.

---

### 评论 #9 — ffleader1 (2020-12-15T15:48:25Z)

> Hi @ffleader1
> Can you please try with ROCm 3.10 on the same machine and update.
> Request to close this issue, if it works in 3.10.
> Thank you.

I did format the OS out of my disks partition so I no longer keep it. This is probably just a single problem on my end, so please close it. Thank you.

---

### 评论 #10 — ROCmSupport (2020-12-16T04:12:40Z)

Thanks @ffleader1 for the update.
Closing it now.
Thank you.

---
