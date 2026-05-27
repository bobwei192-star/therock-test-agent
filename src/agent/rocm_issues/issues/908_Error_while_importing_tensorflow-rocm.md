# Error while importing tensorflow-rocm

> **Issue #908**
> **状态**: closed
> **创建时间**: 2019-10-13T09:04:43Z
> **更新时间**: 2019-11-13T21:02:51Z
> **关闭时间**: 2019-11-13T21:02:51Z
> **作者**: limapedro
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/908

## 描述

Hi, I followed the instructions to install rocm on Ubuntu 18.04 everythings seems to work fine, running /opt/rocm/bin/rocm-smi outputs

========================ROCm System Management Interface========================
WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/gpu_busy_percent
GPU Temp AvgPwr SCLK MCLK Fan Perf PwrCap VRAM% GPU%
0 37.0c N/A 300Mhz 1200Mhz None% auto N/A N/A N/A
==============================End of ROCm SMI Log ==============================

I trying to use Vega 11 on my Ryzen 3400G, I'm aware that I cannot run HIP, but I possibly could run opencl on this APU, my first step is to import tensorflow, but I got an error, this one:

Python 3.6.8 (default, Oct 7 2019, 12:59:55)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

import tensorflow as tf
Traceback (most recent call last):
File "", line 1, in
File "/usr/local/lib/python3.6/dist-packages/tensorflow/init.py", line 28, in
from tensorflow.python import pywrap_tensorflow # pylint: disable=unused-import
File "/usr/local/lib/python3.6/dist-packages/tensorflow/python/init.py", line 47, in
import numpy as np
ModuleNotFoundError: No module named 'numpy'

Are there any guides on how to install Tensorflow for opencl?
I'll give updates with regards to this soon. meanwhile thank you guys for this project, it really is a great thing. Cheers!

---

## 评论 (3 条)

### 评论 #1 — JMadgwick (2019-10-13T09:26:58Z)

I had a look into this last year and while there are efforts to port Tensorflow to OpenCL, none of these work well and they only work with GPUs that support SYCL and SPIR. Certain AMD drivers did support this but current ROCm does not.
I don't think you will be able to use Tensorflow on that GPU. [There is a guide here](https://jonnoftw.github.io/2018/04/04/building-tensorflow-with-opencl-support-on-ubuntu-1604) that you could try to follow, but from the comments it looks like it doesn't work any more. Probably because the latest AMD drivers no longer support the OpenCL extension (SPIR) which that port requires.

Regardless in that guide the OpenCL port had very poor performance. You would be much better off **just following guides to install Tensorflow for CPU**. Vega 11 is a pretty slow GPU anyway and probably wouldn't be great for Tensorflow because of it's very poor memory (shared with CPU).

Tensorflow works just fine on a CPU, I have used it on much slower CPUs than your's with acceptable results. If you're just getting started it would be better to spend time learning Tensorflow and not wasting it trying to get a poor performing OpenCL version to work.

---

### 评论 #2 — limapedro (2019-10-13T09:35:35Z)

@JMadgwick Thanks for your answer, I will try to compile tensorflow from source to see if it better than the native installation, also I'll try to use plaidml with opencl although it may be slower.

---

### 评论 #3 — sunway513 (2019-11-13T21:02:51Z)

tensorflow-rocm only supports ROCm HIP path. 

---
