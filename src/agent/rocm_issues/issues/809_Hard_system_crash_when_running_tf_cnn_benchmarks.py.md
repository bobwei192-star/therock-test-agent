# Hard system crash when running: tf_cnn_benchmarks.py 

> **Issue #809**
> **状态**: closed
> **创建时间**: 2019-06-03T05:22:09Z
> **更新时间**: 2019-06-14T14:55:04Z
> **关闭时间**: 2019-06-06T05:59:32Z
> **作者**: sos-michael
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/809

## 描述

So my system shuts off when I run the following command:

python3 tf_cnn_benchmarks.py --num_gpus=10 --batch_size=64 --model=resnet50 --variable_update=parameter_server --local_parameter_device=cpu

It happens during the warmup phase. I've got no logs as the crash kills the system and everything is lost when I turn back on. It's reproducible. I have rocm-smi running when it happens and the gpu aren't under a consistent load yet. They're still bouncing up and down from 20-90w and 0-100% load.

I'm on FC30 (kernel 5.1, amdgpu 3.30) with rocm 2.4 from the el7 repos. The system is an Epyc 7551p on a gigabye mz31. The GPUs are 5x Radeon Pro Duos that are power limited 100 watts per GPU from the factory.

My first thought was a power draw issues, but I'm using a single rail 1500w (thermaltake DPS) power supply and I ran a torture test without a crash, let alone a hard crash:
(1) Pegged all 32 cores / 64 thread. 
(2) Constantly read from the drive.
(3) Ran an opencl(darktable) workload on my primary (nvidia p4000) gpu.
(4) Ran an eth mining workload(not ideal, but it was a way of making sure it wasn't rocm related) on all ten cards each drawing about (according to rocm-smi) ~80w.

I'm lost as to where I should start poking.

---

## 评论 (3 条)

### 评论 #1 — sos-michael (2019-06-04T00:12:46Z)

I switched my system from uma to numa memory modes and now that benchmark fails with a missing algorithm issue, but this runs fine:

python3 tf_cnn_benchmarks.py --num_gpus=10 --batch_size=16 --model=alexnet

How could that effect anything? it would appear that an address is not being translated correctly? I don't know. I guess I'm now in the clear now, but maybe I can help track this bug down for the next user?

---

### 评论 #2 — fvdnabee (2019-06-14T08:38:05Z)

My system also experiences a system reset during the TF ResNet50 benchmark, though it depends on the benchmark settings. Using FP32 and a batch size of 64 has resulted in a reset 3 out of 4 times so far. Strangely enough the benchmark did complete correctly one time. As FP32/BS64 are the default settings in the [ROCm TF quick start guide](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-quickstart.md#tensorflows-tf_cnn_benchmarks), perhaps a note could be added warning the user of a potential reset? 

It is unclear to me if the reset is expected behaviour of TF or whether it is due to a bug in (the) rocm (TF port). I am willing to troubleshoot further, but would require guidance on how to proceed. 

Details of my system setup:
- rocm/tensorflow:rocm2.5-tf1.13-python3 docker image on an arch linux host system (5.1.8-arch1-1-ARCH kernel)
- GPU: Sapphire Technology Limited Vega 10 XL/XT [Radeon RX Vega 56/64] -> Sapphire Radeon RX Vega 56 Pulse HBM2 - 8 Gb
- Driver: amdgpu, /lib/modules/5.1.8-arch1-1-ARCH/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko.xz, srcversion:     ED0CB3420B32010EABFF1FF
- Intel(R) Core(TM) i5-4670K (stable OC at 4GHz)
- 16GiB RAM

I've attached the logs of the following benchmark runs:
FP16/BS32 (no reset): python3 ./scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --model=resnet50 --num_gpus=1 --batch_size=32 --summary_verbosity=1 --use_fp16
FP16/BS64 (no reset): python3 ./scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --model=resnet50 --num_gpus=1 --batch_size=64 --summary_verbosity=1 --use_fp16
FP32/BS64 (3/4 reset): python3 ./scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --model=resnet50 --num_gpus=1 --batch_size=64 --summary_verbosity=1 --nouse_fp16

[tf-resnet50-benchmarks.txt](https://github.com/RadeonOpenCompute/ROCm/files/3289755/tf-resnet50-benchmarks.txt)

---

### 评论 #3 — pramenku (2019-06-14T14:55:04Z)

We have tried with ROCm2.5 on below details, not seeing the reported issue as mentioned by fvdnabee
Are you observing on UB 16.04.5 ( kernel as mentioned below) . If possible, can you give a try.

Looks like you are using "5.1.8-arch1-1-ARCH kernel" higher kernel.

GPU : Radeon RX Vega 64

Intel(R) Core(TM) i7-5960X CPU @ 3.00GHz
16GiB RAM

# lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.5 LTS
Release:        16.04
Codename:       xenial

Kernel : 4.15.0-39-generic

Command : python3 ./scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --model=resnet50 --num_gpus=1 --batch_size=64 --summary_verbosity=1 --nouse_fp16

Docker : rocm/tensorflow:rocm2.5-tf1.13-python3


---
