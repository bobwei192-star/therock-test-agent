# Support Ubuntu 18.04.5

> **Issue #1187**
> **状态**: closed
> **创建时间**: 2020-08-02T18:44:11Z
> **更新时间**: 2020-12-01T17:28:20Z
> **关闭时间**: 2020-12-01T17:28:19Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1187

## 描述

ROCm should support Ubuntu 18.04.5 since it is the next point release of this long-term support (LTS) version of this Linux distribution, following the currently-supported 18.04.4. The point release of Ubuntu 18.04.5 is set to be released on August 13th, so now is a good time to start testing with that version, before it gets released:

https://wiki.ubuntu.com/BionicBeaver/ReleaseSchedule

---

## 评论 (2 条)

### 评论 #1 — xuhuisheng (2020-08-03T01:57:22Z)

2020-08-03
I found my ubuntu-18.04.4 already using linux-5.4.0-42, And rocm seems run ok.
```
# hostnamectl
   Static hostname: x-MS-7816
         Icon name: computer-desktop
           Chassis: desktop
        Machine ID: 885ec2c7c1974347b0e372349a9b92f5
           Boot ID: b11888222673424eae46e414a2df8826
  Operating System: Ubuntu 18.04.4 LTS
            Kernel: Linux 5.4.0-42-generic
      Architecture: x86-64
```

```
$ python test.py 
2020-08-03 09:56:12.686197: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-08-03 09:56:13.377395: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:02:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.34GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-08-03 09:56:13.604802: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-08-03 09:56:13.606448: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-08-03 09:56:13.901224: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-08-03 09:56:13.902955: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-08-03 09:56:13.903170: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-08-03 09:56:13.903819: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
2020-08-03 09:56:13.928568: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 2394170000 Hz
2020-08-03 09:56:13.929708: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x563409d498a0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-08-03 09:56:13.929736: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-08-03 09:56:13.931722: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x56340e1a6d90 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-08-03 09:56:13.931755: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Ellesmere [Radeon RX 470/480/570/570X/580/580X], AMDGPU ISA version: gfx803
2020-08-03 09:56:13.931952: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:02:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.34GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-08-03 09:56:13.932016: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-08-03 09:56:13.932040: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-08-03 09:56:13.932061: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-08-03 09:56:13.932082: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-08-03 09:56:13.932235: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-08-03 09:56:13.932266: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-08-03 09:56:13.932280: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2020-08-03 09:56:13.932290: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2020-08-03 09:56:13.932513: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7399 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X], pci bus id: 0000:02:00.0)
Epoch 1/5
2020-08-03 09:56:15.443621: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
1875/1875 [==============================] - 5s 2ms/step - loss: 0.2977 - accuracy: 0.9131
Epoch 2/5
1875/1875 [==============================] - 5s 2ms/step - loss: 0.1419 - accuracy: 0.9580
Epoch 3/5
1875/1875 [==============================] - 5s 2ms/step - loss: 0.1074 - accuracy: 0.9678
Epoch 4/5
1875/1875 [==============================] - 5s 3ms/step - loss: 0.0882 - accuracy: 0.9727
Epoch 5/5
1875/1875 [==============================] - 5s 3ms/step - loss: 0.0755 - accuracy: 0.9762
313/313 - 1s - loss: 0.0803 - accuracy: 0.9756

```


---

### 评论 #2 — jlgreathouse (2020-12-01T17:28:19Z)

This should work on current ROCm versions. Thanks!

---
