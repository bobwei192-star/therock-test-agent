# ROCM enabled CAFFE

> **Issue #86**
> **状态**: closed
> **创建时间**: 2017-02-03T19:18:08Z
> **更新时间**: 2017-05-12T08:46:33Z
> **关闭时间**: 2017-02-05T01:27:45Z
> **作者**: raxbits
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/86

## 描述

Hi AMD team, 

I have read that there is a port of Caffe using HIP language that was done last year. Is it possible to have a link to it (if it's publicly) available.

Thanks!

---

## 评论 (5 条)

### 评论 #1 — ArthurGodoy (2017-04-18T14:37:33Z)

Hi! I am searching for the same information. Does anyone have the answer?

---

### 评论 #2 — gsedej (2017-05-11T09:07:01Z)

Is it even possible to run CAFFE on ROCM today? Or is it only AMD internal version?

---

### 评论 #3 — gstoner (2017-05-11T14:15:27Z)

https://github.com/ROCmSoftwarePlatform/hipCaffe    You can run the Caffe GreenTea version on ROCm on OpenCL but I just saw they had some out of bounds references in their code, we now use guard pages to caught these errors 

---

### 评论 #4 — gsedej (2017-05-11T15:48:17Z)

Thanks for reply, I was not aware it exists. I only found 
https://github.com/BVLC/caffe/tree/opencl
and deprecated
https://github.com/amd/OpenCL-caffe

I will try this "hipCaffe" which uses Cuda conversion tomorrow. AMD should really put more effort in deep learning. In past, AMD gpus were much better at GPGPU tasks e.g. bitcoin mining.

---

### 评论 #5 — gsedej (2017-05-12T08:46:33Z)

Thanks for info about "hipCaffe"!

For those who are interested, here is my tests results (make_all.testbin) on RX 480

```

[----------] Global test environment tear-down
[==========] 2021 tests from 265 test cases ran. (747168 ms total)
[  PASSED  ] 1979 tests.
[  FAILED  ] 42 tests, listed below:
[  FAILED  ] DeconvolutionLayerTest/0.TestNDAgainst2D, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] DeconvolutionLayerTest/0.TestGradient3D, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] DeconvolutionLayerTest/1.TestNDAgainst2D, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] DeconvolutionLayerTest/1.TestGradient3D, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] DeconvolutionLayerTest/2.TestNDAgainst2D, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] DeconvolutionLayerTest/2.TestGradient3D, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] DeconvolutionLayerTest/3.TestNDAgainst2D, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] DeconvolutionLayerTest/3.TestGradient3D, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] EmbedLayerTest/0.TestGradient, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] EmbedLayerTest/0.TestGradientWithBias, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] EmbedLayerTest/1.TestGradient, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] EmbedLayerTest/1.TestGradientWithBias, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] EmbedLayerTest/2.TestGradient, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] EmbedLayerTest/2.TestGradientWithBias, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] EmbedLayerTest/3.TestGradient, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] EmbedLayerTest/3.TestGradientWithBias, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] Im2colLayerTest/0.TestGradientForceND, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] Im2colLayerTest/0.TestDilatedGradientForceND, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] Im2colLayerTest/1.TestGradientForceND, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] Im2colLayerTest/1.TestDilatedGradientForceND, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] Im2colLayerTest/2.TestGradientForceND, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] Im2colLayerTest/2.TestDilatedGradientForceND, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] Im2colLayerTest/3.TestGradientForceND, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] Im2colLayerTest/3.TestDilatedGradientForceND, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/0.TestSimple3DConvolution, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/0.TestDilated3DConvolution, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/0.TestNDAgainst2D, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/0.TestGradient3D, where TypeParam = caffe::CPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/1.TestSimple3DConvolution, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/1.TestDilated3DConvolution, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/1.TestNDAgainst2D, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/1.TestGradient3D, where TypeParam = caffe::CPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/2.TestSimple3DConvolution, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/2.TestDilated3DConvolution, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/2.TestNDAgainst2D, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/2.TestGradient3D, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] ConvolutionLayerTest/3.TestSimple3DConvolution, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/3.TestDilated3DConvolution, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/3.TestNDAgainst2D, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] ConvolutionLayerTest/3.TestGradient3D, where TypeParam = caffe::GPUDevice<double>
[  FAILED  ] NeuronLayerTest/2.TestBNLLGradient, where TypeParam = caffe::GPUDevice<float>
[  FAILED  ] NeuronLayerTest/3.TestBNLLGradient, where TypeParam = caffe::GPUDevice<double>

42 FAILED TESTS
```

---
