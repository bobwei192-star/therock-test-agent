# Vector copy example "Initializing the hsa runtime failed" Radeon Pro WX 7100

> **Issue #107**
> **状态**: closed
> **创建时间**: 2017-04-24T10:38:09Z
> **更新时间**: 2017-05-15T11:48:03Z
> **关闭时间**: 2017-05-15T11:48:03Z
> **作者**: vicproon
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/107

## 描述

## Problem
We've been trying to use HIP and HCC to run some ported CUDA code on Radeon Pro WX 7100.
We follow ROCm installation instructions from https://radeonopencompute.github.io/install.html

At the stage of install check (following the tutorial) we observe the following output:
1. ``Hello, world!'' example

```shell
wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cpp
wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cl
g++ -I /opt/rocm/opencl/include/ ./HelloWorld.cpp -o HelloWorld -L/opt/rocm/opencl/lib/x86_64 -lOpenCL
./HelloWorld: /usr/local/cuda/lib64/libOpenCL.so.1: no version information available (required by ./HelloWorld)
Executed program succesfully.
```

2. ``Vector copy'' example

```shell
cd /opt/rocm/hsa/sample
make
./vector_copy

Initializing the hsa runtime failed.
```

What could be our possible steps for solving this problem?

## System Specifications
OS: Ubuntu 16.04.2 64bit
Processor: Intel Core i7-4790 @ 3.60Ghz
Memory: 31,4 GiB
Graphics: Radeon Pro WX 7100
Driver Version: amdgpu-pro-17.10-401251

---

## 评论 (8 条)

### 评论 #1 — briansp2020 (2017-04-24T17:02:57Z)

I don't think amdgpu-pro driver works with ROCm.
Are you sure that you are running ROCm kernel?
What do you get when you 'uname -a'?

---

### 评论 #2 — gstoner (2017-04-25T02:50:11Z)

You can not have ROCm and amdgpu-pro-17.10-401251 running at the same-time.

Greg

On Apr 24, 2017, at 5:38 AM, Victor Proon <notifications@github.com<mailto:notifications@github.com>> wrote:

amdgpu-pro-17.10-401251



---

### 评论 #3 — vicproon (2017-04-25T05:26:12Z)

> What do you get when you 'uname -a'?
```bash
uname -a
Linux beamoflight-All-Series 4.8.0-46-generic #49~16.04.1-Ubuntu SMP Fri Mar 31 14:51:03 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```

> Are you sure that you are running ROCm kernel

> You can not have ROCm and amdgpu-pro-17.10-401251 running at the same-time.

I guess i missed some important step in the guide. Can you provide some step-by-step instructions?


---

### 评论 #4 — vicproon (2017-04-25T07:16:39Z)

Another error with the same simptoms: hip squares sample 

```shell
$ make
/opt/rocm/hip/bin/hipcc  square.hipref.cpp -o square.hip.out
$ ls
Makefile  README.md  square.cu  square.hip.out  square.hipref.cpp
$ ./square.hip.out 
### HCC STATUS_CHECK Error: HSA_STATUS_ERROR_OUT_OF_RESOURCES (0x1008) at file:/home/scchan/code/github/hcc-roc-1.4.x/hcc/lib/hsa/mcwamp_hsa.cpp line:2728
Aborted (core dumped)
```

---

### 评论 #5 — gstoner (2017-04-25T10:44:23Z)

Step One did you de-install the Radeon Pro driver from your system,  Yes or No 
You 
We can not stack the drivers which what you are doing.   ROCm Linux  Driver is a full driver which runs independent of Radeon Pro driver,  you cannot have both of them loaded at the same time.  

Now you need to de-install both driver then re-install ROCm driver then you should be good.   

---

### 评论 #6 — gstoner (2017-04-25T10:47:09Z)

I might be faster to load a new instance of Ubuntu 16.04 and then load the just the ROCm driver by following the install instructions. 

---

### 评论 #7 — jedwards-AMD (2017-04-25T13:45:28Z)

You can also install the ROCm kernel over this kernel image. The 1.4 version of the kernel will have to be made the default boot, either by selecting it at boot time or by modifying the grub config files.

---

### 评论 #8 — vicproon (2017-04-25T14:07:15Z)

@gstoner @jedwards-AMD @briansp2020
Thank you. Uninstalling rocm, amdgpu-pro, reinstalling rocm, rebooting into 1.4rocm kernel helped!

---
