# Rocm only use 3 CPU threads

- **Issue #:** 1229
- **State:** closed
- **Created:** 2020-09-22T16:05:03Z
- **Updated:** 2020-11-20T05:02:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/1229

![Screenshot_20200923_005414](https://user-images.githubusercontent.com/71719505/93906956-bf231f00-fd37-11ea-98b5-59932697e359.png)

OS: OpenSUSE Tumbleweed 
Rocm: 3.8.0
Python: 3.8
Tensorflow: 2.3.0
Model: MobileNetV2 
CPU: 3950X
GPU: Vega 64

as the picture showed Rocm only use 3 CPU threads. 
It will rise a warning message 

WARNING:tensorflow:Callbacks method `on_train_batch_end` is slow compared to the batch time (batch time: 0.0353s vs `on_train_batch_end` time: 1.8749s). Check your callbacks.

In this way , using CPU to train model is about 3 times faster than GPU. 
Is there any workaround to utilize more CPU threads? 

I think they are some lovely Clang compiler threads 