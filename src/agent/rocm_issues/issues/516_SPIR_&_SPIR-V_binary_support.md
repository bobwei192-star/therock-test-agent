# SPIR & SPIR-V binary support

> **Issue #516**
> **状态**: closed
> **创建时间**: 2018-08-28T08:55:01Z
> **更新时间**: 2018-09-08T17:51:55Z
> **关闭时间**: 2018-08-30T03:41:28Z
> **作者**: MathiasMagnus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/516

## 描述

### Context
Our group is a happy user of Codeplays ComputeCpp, a fully conformant SYCL 1.2.1 implementation. With Intels rock solid OpenCL infrastructure(s, they too have many to chose from but all are SPIR enabled), it's a shame how AMD seems to have put OpenCL to the side. ([CPU support being discontinued on Windows](https://community.amd.com/message/2875387#2875387), [AMD APP SDK removed from developer.amd.com](https://community.amd.com/message/2847320#2847320), fragmentation of AMDs driver stacks…) When finally AMD and Intel had something to rival CUDA in a portable manner, AMD loses interest in supporting OpenCL, the underlying infrastructure. Luckily Codeplay goes around by adding non-conform additions to ComputeCpp, which is able to emit not just SPIR and SPIR-V, but also PTX and AMDGCN ISA. I understand that they need to do this for Nvidia who sabotages OpenCL to their dying breath, but I was expecting better of AMD.

The Wigner GPU Lab is dedicated to promote SYCL and grow its ecosystem ([BLAS](https://github.com/codeplaysoftware/sycl-blas), [ML](https://github.com/codeplaysoftware/SYCL-ML), [DNN](https://github.com/codeplaysoftware/SYCL-DNN) done by Codeplay, initial [PRNG](https://github.com/Wigner-GPU-Lab/SYCL-PRNG) by us, FFT planned if someone does not beat us to it, SPARSE up for grabs).

I would like to ask for AMD to pay a little more attention to OpenCL in general. I feel it is the best thing to do before GPGPU makes it into ISO C++, and even after that via vendor extensions of OpenCL & SYCL. IMHO the effort put into HCC would have been better put into upstream SYCL support for Clang which would have enabled a far wider audience of developers to write libraries that support AMD HW (NOT JUST GPUs!).

### Sad example
TF 1.8 supporting ROCm enabled GPUs via rocPRIM is nice, but given the limited resources AMD can put into domain library support, I feel the common denominator should be put first. Not putting enough effort into OpenCL/triSYCL/ComputeCpp support for TF is the reason why anyone coming to take a look at the installation instructions for both [Linux](https://www.tensorflow.org/install/install_linux) & [Windows](https://www.tensorflow.org/install/install_windows) are greeted by

> **TensorFlow with GPU support.** TensorFlow programs typically run significantly faster on a GPU than on a CPU. Therefore, if your system has a NVIDIA® GPU meeting the prerequisites shown below and you need to run performance-critical applications, you should ultimately install this version.

The message is simple: `GPU == CUDA` Intel CPUs and IGPs being ubiquitous in both consumer and workstations and having prime-time OpenCL support, it's a miracle how AMD who initially was all in for OpenCL cannot make it to the "front-page" together with Intel. And TF is a Google project! Google is fed up with NVCC! They "single-handedly" added CUDA support for Clang to get rid of closed-source Nvidia components. If only that effort were put into SYCL...

### Summa summarum
Please add support for SPIR & SPIR-V binaries in ROCm (and all other) AMD runtime stacks.

---

## 评论 (3 条)

### 评论 #1 — zpodlovics (2018-08-28T09:27:42Z)

FYI: https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/57

I am afraid if you want predictable multi-vendor hw support, you have to build your own compiler group.

---

### 评论 #2 — gstoner (2018-08-30T03:41:28Z)

@MathiasMagnus 

OpenCL 1.2 works on Windows, AMDGPUpro, and ROCm which matches NVIDIA and Mac OSX over the past 2 years.   APPS SDK is not needed on Linux stack to enable OpenCL the header are there already.   

You can blame AMD Embedded team for blowing away the AMD APPS SDK. You notice it just CPU Tools.  You find them here https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/releases 

We are investing in OpenCL just not in the area your would like with components that are not really part of the core standard of OpenCL,  SPIR 1.2 was Optional, was to be quickly superceded by SPIR 2.0 ,  we moved on have been working on SPIR-V and OpenCL 2.1 for stack, waiting for SPIR_V to mature.  

Your knowledge of the investment to get Tensorflow to run fast is limited.  It is a lot more then rocPRIM.  You might want to look at MIOpen, rocBLAS, rocFFT, rocSOLVER, rocRAND,  EIGEN port ( which is upstream).  We have a lot more libraries coming. HIP is now a standard part of CLANG and LLVM.     Also SCYL port was a very limited port on what was needed to really get Tensorflow running competitively with NVIDIA.   One more thing XLA is now taking over how you program operator in Tensorflow.  SYCL does not solve that issue, we have to build that compiler. 

Right now Google is very happy with AMD and the work we are doing to truly clean up Tensorflow to get it to support more then CUDA GPU.    Everything we do we bringing to Windows.  Step one is getting a platform in place that truly competitive with CUDA. 


I hear you that you believe SYCL would have been better investment then HCC.  But it  was the foundation for a lot of what when into the SYCL spec.    The original triSCYLE was built from the Source Tree of our C++ AMP research compiler for HSA. Doing Single Source was not part of the original spec.   I know Ronan work in the same team as me  He also rewrote much of the original SYCL spec 

Honestly, the best if really want this is nice and not bash the team.  But thank you for your opinion we take it under advisement 

One thing the team is growing fast. 

---

### 评论 #3 — gstoner (2018-09-08T17:51:55Z)

@MathiasMagnus  Looks like some solving the Sycl issue https://github.com/illuhad/hipSYCL for you..  This great to see also show the power of opensource software.   This give you NVIDIA and ROCm backends, still work in progress but great start. 

---
