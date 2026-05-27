# Segmentation Fault while running tensorflow on RX580

> **Issue #1165**
> **状态**: closed
> **创建时间**: 2020-06-24T19:12:45Z
> **更新时间**: 2020-06-26T21:33:57Z
> **关闭时间**: 2020-06-25T11:21:10Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1165

## 描述

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

---

## 评论 (3 条)

### 评论 #1 — rat9615 (2020-06-26T20:54:51Z)

Hey, did you find a solution to this? It so happens that I am facing the same problem.

---

### 评论 #2 — ghost (2020-06-26T21:02:41Z)

Fixed with these commands:
```​
echo 'export LD_LIBRARY_PATH=/opt/rocm/lib:$LD_LIBRARY_PATH' >> $HOME/.bashrc 
source $HOME/.bashrc
sudo reboot
```

---

### 评论 #3 — rat9615 (2020-06-26T21:33:57Z)

Worked perfectly.

---
