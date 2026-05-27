# Successfully instead ROCm v3.9.x and above, but TF-ROCm does not use GPU

> **Issue #1329**
> **状态**: closed
> **创建时间**: 2020-12-11T10:20:27Z
> **更新时间**: 2020-12-16T05:27:45Z
> **关闭时间**: 2020-12-15T12:46:26Z
> **作者**: quocdat32461997
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1329

## 描述

OS: Ubuntu 18.04.5 (5.4 kernel)
GPU: Radeon VII

After successfully installing ROCm v.3.9.x, 2 commands 
```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```
both show the same GPU.

However, after installing TF-ROCm, TF-ROCm uses CPU only (checked by monitoring /opt/rocm/bin/rocm-smi). When running TF codes, it shows that GPU is not used because it misses libMIOpen.so and other packages. 

```
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> tf.constant(1)
2020-12-11 04:07:20.679475: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
2020-12-11 04:07:20.721488: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:05:00.0 name: Vega 20     ROCm AMD GPU ISA: gfx906
coreClock: 1.801GHz coreCount: 60 deviceMemorySize: 15.98GiB deviceMemoryBandwidth: 953.67GiB/s
2020-12-11 04:07:20.724722: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-12-11 04:07:20.724926: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libMIOpen.so'; dlerror: libMIOpen.so: cannot open shared object file: No such file or directory
2020-12-11 04:07:20.725019: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'librocfft.so'; dlerror: librocfft.so: cannot open shared object file: No such file or directory
2020-12-11 04:07:20.725107: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'librocrand.so'; dlerror: librocrand.so: cannot open shared object file: No such file or directory
2020-12-11 04:07:20.725124: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1753] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2020-12-11 04:07:20.725511: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2020-12-11 04:07:20.733407: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 2593680000 Hz
2020-12-11 04:07:20.733922: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x4a2fb60 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-12-11 04:07:20.733945: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-12-11 04:07:20.735540: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-12-11 04:07:20.735561: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      
<tf.Tensor: shape=(), dtype=int32, numpy=1>
```

Hence, after installing missing packages shown in the above output (also suggested by [shawonashraf.](https://shawonashraf.github.io/rocm-tf-ubuntu/)), GPU is used.

```
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
tf.cons>>> tf.constant(1)
2020-12-11 04:09:17.198383: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
2020-12-11 04:09:17.239802: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:05:00.0 name: Vega 20     ROCm AMD GPU ISA: gfx906
coreClock: 1.801GHz coreCount: 60 deviceMemorySize: 15.98GiB deviceMemoryBandwidth: 953.67GiB/s
2020-12-11 04:09:17.243047: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-12-11 04:09:17.244565: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-12-11 04:09:17.259323: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-12-11 04:09:17.259728: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-12-11 04:09:17.259858: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-12-11 04:09:17.260304: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2020-12-11 04:09:17.268531: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 2593680000 Hz
2020-12-11 04:09:17.269112: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5918970 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-12-11 04:09:17.269150: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-12-11 04:09:17.271162: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5984340 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-12-11 04:09:17.271186: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Vega 20, AMDGPU ISA version: gfx906
2020-12-11 04:09:17.708504: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:05:00.0 name: Vega 20     ROCm AMD GPU ISA: gfx906
coreClock: 1.801GHz coreCount: 60 deviceMemorySize: 15.98GiB deviceMemoryBandwidth: 953.67GiB/s
2020-12-11 04:09:17.708622: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-12-11 04:09:17.708660: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-12-11 04:09:17.708693: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-12-11 04:09:17.708724: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-12-11 04:09:17.708818: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-12-11 04:09:17.729743: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-12-11 04:09:17.729784: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      0 
2020-12-11 04:09:17.729803: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 0:   N 
2020-12-11 04:09:17.729998: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 15385 MB memory) -> physical GPU (device: 0, name: Vega 20, pci bus id: 0000:05:00.0)
```

I wonder if this is expected. If not expected, it would be great to put all necessary packages into one place when installing ROCm with Tensorflow. 
Thanks

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2020-12-11T12:01:16Z)

Thanks @quocdat32461997 for reaching out.
TF is a python package and it can be installed via pip3 install.
TF dependent libraries and all are apt/rpm based, specific to OS platform.
So its our responsibility to make sure that all dependencies are served before using tf package.

Anyway let me gather more information on this.

---

### 评论 #2 — ROCmSupport (2020-12-15T12:46:26Z)

Hi @quocdat32461997 
I got an update from developers that: we need to make sure to serve all dependencies for tf to work.
So we need to install rocm-dkms, rocm-libs and rccl before launching tf.
Hope this helps.
Thank you.

---
