# pytorch support?

> **Issue #1334**
> **状态**: closed
> **创建时间**: 2020-12-12T13:16:06Z
> **更新时间**: 2020-12-14T08:34:16Z
> **关闭时间**: 2020-12-12T17:29:12Z
> **作者**: christofer-f
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/1334

## 标签

- **Question** (颜色: #cc317c)

## 描述

Hi!

I am using pytorch. 

Could you provide me with a youtube link where you successfully run GPU accelerated pytorch on RADEON hardware? 

Br,
Christofer

---

## 评论 (2 条)

### 评论 #1 — xuhuisheng (2020-12-12T14:07:32Z)

* ubuntu 20.04.1
* ROCm 3.10
* GPU RX580
* Pytorch 1.7.1

```
True
Devices:1
[_CudaDeviceProperties(name='Device 67df', major=8, minor=0, total_memory=8192MB, multi_processor_count=36)]
tensor(4., device='cuda:0', grad_fn=<SumBackward0>)

```

Sorry for no yourube video.
You could compile pytorch by yourself or use docker. there is no offically release.

* compile : https://github.com/acai66/Pytorch_ROCm_whl
* docker : https://hub.docker.com/r/rocm/pytorch


---

### 评论 #2 — christofer-f (2020-12-12T17:29:12Z)

Thx for the reply! 
I use pytorch-lightning btw. It's much better than TF   :-)

And now when Radeon GPUs are getting competitive. 
I wanted to see if this could be a viable option. 


---
