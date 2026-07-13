# Segmentation Fault while running tensorflow on RX580

- **Issue #:** 1165
- **State:** closed
- **Created:** 2020-06-24T19:12:45Z
- **Updated:** 2020-06-26T21:33:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/1165

**System**
Os : Ubuntu 20.04 LTS
GPU : Rx580
Tensorflow version : v2.2.0
Rocm version: 3.5.1

**The problem**
Whenever i try to utilise the GPU with tensorflow it pops up with segmentation fault (core dumped)

**Logs**
```020-06-24 19:13:58.587688: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108] 0
2020-06-24 19:13:58.587693: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0: N
2020-06-24 19:13:58.587837: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7399 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X], pci bus id: 0000:01:00.0)
Segmentation fault (core dumped)
```