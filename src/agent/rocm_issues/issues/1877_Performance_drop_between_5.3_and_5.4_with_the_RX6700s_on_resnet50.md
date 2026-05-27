# Performance drop between 5.3 and 5.4 with the RX6700s on resnet50

> **Issue #1877**
> **状态**: closed
> **创建时间**: 2022-12-14T16:39:07Z
> **更新时间**: 2024-02-25T04:33:31Z
> **关闭时间**: 2024-02-25T04:33:31Z
> **作者**: MatPoliquin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1877

## 描述

After installing rocm 5.4 on a fresh install of Ubuntu 22.10 I get a performance drop compared to rocm 5.3 on the same OS/hardware


Steps to reproduce:
```
pip3 install tensorflow-rocm
git clone https://github.com/tensorflow/benchmarks.git
cd benchmarks/scripts/tf_cnn_benchmarks
export HSA_OVERRIDE_GFX_VERSION=10.3.0
python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50
```
Results:

- with 5.3 : **total images/sec: 97.40**
- with 5.4 : **total images/sec: 80.03**

Specs:

- Ubuntu 22.10 - Kernel 5.19.X
- Asus g14 2022 laptop
- RX 6700s  8GB
- R7 6800HS 16GB DDR5

---

## 评论 (5 条)

### 评论 #1 — alexschroeter (2023-01-06T19:31:25Z)

I have also seen regression in performance from 5.3.3 to 5.4.0. We suspected regression in FFT because it is our main compute part but I believe resnet is not using FFT and maybe we are looking at a more general issue (we haven't found the time to investigate where the time is lost). We are running Ubuntu 22.04 LTS, Kernel 5.15.0-56, on https://www.supermicro.com/en/Aplus/system/4U/4124/AS-4124GS-TNR.cfm with two AMD EPYC 7452 32-Core Processor,

---

### 评论 #2 — nartmada (2024-02-18T04:13:22Z)

Hi @MatPoliquin and @alexschroeter, can you please try latest ROCm 6.0.2 and check if your performance issue has been resolved?  Thanks.

---

### 评论 #3 — alexschroeter (2024-02-21T16:59:30Z)

Sorry, but I don't have access to the hard- and software anymore. Maybe OP still has access to his setup.

---

### 评论 #4 — nartmada (2024-02-21T18:37:49Z)

My apologies for the lack of response and want to check if this is still an issue with latest ROCm 6.0.2.

---

### 评论 #5 — nartmada (2024-02-25T04:33:31Z)

Closing the ticket as no response from @MatPoliquin.  Please re-open if this is still an issue with latest ROCm 6.0.2.  Thanks.

---
