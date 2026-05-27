# Memory access fault by GPU node-1 when training a model.

> **Issue #1574**
> **状态**: closed
> **创建时间**: 2021-09-18T21:03:32Z
> **更新时间**: 2021-09-23T10:05:58Z
> **关闭时间**: 2021-09-23T10:05:58Z
> **作者**: tichondrius2215
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1574

## 描述

I had a working installation of both ROCm and tensorflow-rocm running smoothly on my Ubuntu 20.04. Until recently it developed this error `Memory access fault by GPU node-1 (Agent handle: 0x55f6dc9adc10) on address 0x3f7b9000. Reason: Page not present or supervisor privilege` while training a resnet model on my data. 
Surprisingly I get this error only when trying to train a model on my data with rocm and tensorflow-rocm. I know this issue has been already reported here [https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/302](url) and the solution mentions downgrading rocm-opencl version but the provided versions in the thread appears quite old to install with 3.5.1. 

I also have a slight confusion here. When I run tensorflow benchmarks with `python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50 --variable_update=parameter_server ` everything works as expected without any error.

**Details:**
ROCm Version = 3.5.1
Tensorflow-rocm version = 2.2.0
Ubuntu: 20.04 with kernel = 5.4.0-42-generic
CPU: Intel(R) Core(TM) i5-6400 CPU @ 2.70GHz
GPU: RX-580 (gfx803)

The only recent change made in system is installing `ocl-icd-opencl-dev`. 

**My question is, can `ocl-icd-opencl-dev` create conflict with rocm-opencl?** 

Following is the output of error.

`021-09-19 00:49:18.386647: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2021-09-19 00:49:18.946959: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.34GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2021-09-19 00:49:19.141229: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2021-09-19 00:49:19.142295: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2021-09-19 00:49:19.385058: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2021-09-19 00:49:19.386320: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2021-09-19 00:49:19.386452: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-09-19 00:49:19.386702: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
2021-09-19 00:49:19.390853: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 2699905000 Hz
2021-09-19 00:49:19.391001: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x557ed083ac00 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2021-09-19 00:49:19.391017: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2021-09-19 00:49:19.391192: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.34GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2021-09-19 00:49:19.391235: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2021-09-19 00:49:19.391282: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2021-09-19 00:49:19.391326: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2021-09-19 00:49:19.391369: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2021-09-19 00:49:19.391485: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-09-19 00:49:19.391543: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-09-19 00:49:19.391552: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2021-09-19 00:49:19.391558: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2021-09-19 00:49:19.391699: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7399 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], pci bus id: 0000:01:00.0)
2021-09-19 00:49:19.702994: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x557ed05c2c50 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2021-09-19 00:49:19.703026: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], AMDGPU ISA version: gfx803
Epoch 1/100
2021-09-19 00:49:22.985901: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2021-09-19 00:49:23.034224: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
Memory access fault by GPU node-1 (Agent handle: 0x557ed0947610) on address 0x3f43b000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)`


This is the output of benchmark test.

`2021-09-19 00:55:33.989875: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7399 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], pci bus id: 0000:01:00.0)
TensorFlow:  2.2
Model:       resnet50
Dataset:     imagenet (synthetic)
Mode:        training
SingleSess:  False
Batch size:  32 global
             32 per device
Num batches: 100
Num epochs:  0.00
Devices:     ['/gpu:0']
NUMA bind:   False
Data format: NCHW
Optimizer:   sgd
Variables:   parameter_server
==========
Generating training model
WARNING:tensorflow:From /home/user/github/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:131: conv2d (from tensorflow.python.layers.convolutional) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.keras.layers.Conv2D` instead.
W0919 00:55:34.314103 140042160953152 deprecation.py:317] From /home/user/github/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:131: conv2d (from tensorflow.python.layers.convolutional) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.keras.layers.Conv2D` instead.
WARNING:tensorflow:From /home/user/environments/rocm_tf/rocm_tf/lib/python3.8/site-packages/tensorflow/python/layers/convolutional.py:424: Layer.apply (from tensorflow.python.keras.engine.base_layer_v1) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.__call__` method instead.
W0919 00:55:34.318003 140042160953152 deprecation.py:317] From /home/user/environments/rocm_tf/rocm_tf/lib/python3.8/site-packages/tensorflow/python/layers/convolutional.py:424: Layer.apply (from tensorflow.python.keras.engine.base_layer_v1) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.__call__` method instead.
WARNING:tensorflow:From /home/user/github/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:262: max_pooling2d (from tensorflow.python.layers.pooling) is deprecated and will be removed in a future version.
Instructions for updating:
Use keras.layers.MaxPooling2D instead.
W0919 00:55:34.343493 140042160953152 deprecation.py:317] From /home/user/github/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:262: max_pooling2d (from tensorflow.python.layers.pooling) is deprecated and will be removed in a future version.
Instructions for updating:
Use keras.layers.MaxPooling2D instead.
Initializing graph
WARNING:tensorflow:From /home/user/github/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2252: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
W0919 00:55:36.338399 140042160953152 deprecation.py:317] From /home/user/github/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2252: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
2021-09-19 00:55:36.602834: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.34GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2021-09-19 00:55:36.602893: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2021-09-19 00:55:36.602907: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2021-09-19 00:55:36.602934: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2021-09-19 00:55:36.602959: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2021-09-19 00:55:36.603034: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2021-09-19 00:55:36.603062: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2021-09-19 00:55:36.603083: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2021-09-19 00:55:36.603088: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2021-09-19 00:55:36.603198: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7399 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], pci bus id: 0000:01:00.0)
INFO:tensorflow:Running local_init_op.
I0919 00:55:37.123021 140042160953152 session_manager.py:505] Running local_init_op.
INFO:tensorflow:Done running local_init_op.
I0919 00:55:37.179463 140042160953152 session_manager.py:508] Done running local_init_op.
Running warm up
2021-09-19 00:55:38.150849: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2021-09-19 00:55:38.288852: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
Done warm up
Step	Img/sec	total_loss
1	images/sec: 43.6 +/- 0.0 (jitter = 0.0)	7.731
10	images/sec: 43.9 +/- 0.0 (jitter = 0.1)	8.061
20	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	7.813
30	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	7.971
40	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	7.561
50	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	7.535
60	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	7.811
70	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	7.766
80	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	7.808
90	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	8.031
100	images/sec: 44.0 +/- 0.0 (jitter = 0.1)	8.003
----------------------------------------------------------------
total images/sec: 43.98
----------------------------------------------------------------`



---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-09-23T10:05:58Z)

Thanks @tichondrius2215 for reaching out.
I certainly understood the problem.
But I can not comment on this issue as ROCm currently does not support ELLESMERE(gfx803) devices. Request you to check for supported hardware @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support
Request you try on supported hardware.
Thank you.

---
