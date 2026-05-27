# TensorFlow error

> **Issue #1402**
> **状态**: closed
> **创建时间**: 2021-03-07T17:27:51Z
> **更新时间**: 2021-04-12T07:12:23Z
> **关闭时间**: 2021-04-12T07:12:23Z
> **作者**: kulichbulich
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1402

## 描述

Hello,
I have problem with training CNN in tensorflow-rocm-2.4.0. The error occurs randomly, sometimes after several iterations of learning CNN and sometimes it appears immediately. This error (complete error log in file **tensor-flow-rocm-error.txt**): 

_Fit:
2021-03-07 17:54:13.140698: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:116] None of the MLIR optimization passes are enabled (registered 2)
Epoch 1/200
2021-03-07 17:54:14.742459: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libMIOpen.so
2021-03-07 17:54:14.889237: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library librocblas.so
89/89 [==============================] - 141s 2s/step - loss: nan - accuracy: 0.5137 - val_loss: nan - val_accuracy: 0.6555
Epoch 2/200
30/89 [=========>....................] - ETA: 24s - loss: nan - accuracy: 0.6652Memory access fault by GPU node-1 (Agent handle: 0x5f6d730) on address 0x7fb5d8712000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)_

This is my configuration:
_Linux kulich-PC-GPU 5.4.0-66-generic #74~18.04.2-Ubuntu SMP Fri Feb 5 11:17:31 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux_
_RX Vega 64 8GB_

I try to reduce dataset size but the error still occurs. Where can be the problem?  Too complex model?

Another log file is included (**rocminfo.txt** and **dmesg.txt**)
Thank you for your work

[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6097618/dmesg.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6097619/rocminfo.txt)
[tensor-flow-rocm-error.txt](https://github.com/RadeonOpenCompute/ROCm/files/6097620/tensor-flow-rocm-error.txt)






---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2021-03-12T08:44:33Z)

Thanks @kulichbulich for reaching out.
Can you please share the exact steps(step by step) to reproduce the problem.
Thank you.

---

### 评论 #2 — aman190202 (2021-03-12T10:10:32Z)

Try filtering the dataset for any missing or invalid values. My model resulted in nan loss value whenever there was an invalid value in my dataset. 

---

### 评论 #3 — kulichbulich (2021-03-13T21:46:09Z)

Thank you All, for response.
I am creating Simple project here on [OneDriveStorage](https://1drv.ms/u/s!AhZEc7wU8vsTiDAV4iNffOHbn6ti?e=BH7ilQ) with a simple project (run: _python3 RoadTestUnet.py_).
To **aman190202** - I don't thing the problem is in dataset, because the same project was worked before update Rocm and tensorflow-cpu train network without problem, but is very slow.

---

### 评论 #4 — ROCmSupport (2021-03-17T06:10:02Z)

Hi @kulichbulich 
Can you please share the exact steps to understand the problem clearly.
Thank you

---

### 评论 #5 — kulichbulich (2021-03-17T20:55:02Z)

Please download 4files from  [OneDriveStorage](https://1drv.ms/u/s!AhZEc7wU8vsTiDAV4iNffOHbn6ti?e=BH7ilQ) to one directory and run training script _python3 RoadTestUnet.py_ . This script create model and load training file. During training error described on the top of page should appears.

---

### 评论 #6 — ROCmSupport (2021-03-19T12:44:00Z)

Thanks @kulichbulich,
Let me take a look.
But I need some more details.
Looks like you are trying it on Vega10 XT card.
Can you please share details of OS, kernel and TF docker image name and all.
Thank you.

---

### 评论 #7 — ROCmSupport (2021-03-22T10:56:41Z)

Hi @kulichbulich 
Please share the above details so that I will start working on it asap.
Thank you.

---

### 评论 #8 — kulichbulich (2021-04-10T15:30:55Z)

After update to tensorflow-rocm-2.4.1 and ROCm 4.1, problem disappeared and training is working again now.
Thank you

---

### 评论 #9 — ROCmSupport (2021-04-12T07:12:23Z)

Great to know that TF is working with ROCm 4.1 + TF2.4
Thank you

---
