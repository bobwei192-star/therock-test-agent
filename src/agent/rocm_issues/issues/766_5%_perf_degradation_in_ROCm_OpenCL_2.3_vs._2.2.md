# 5% perf degradation in ROCm OpenCL 2.3 vs. 2.2

> **Issue #766**
> **状态**: closed
> **创建时间**: 2019-04-14T14:15:53Z
> **更新时间**: 2021-05-09T20:08:42Z
> **关闭时间**: 2021-05-09T20:08:42Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/766

## 描述

Using GpuOwl https://github.com/preda/gpuowl
Ubuntu 19.04, Linux kernel 5.0.7, Radeon VII

Upon upgrade ROCm 2.2 -> 2.3, without changing anything else, there is a performance degradation of 5-6% in GpuOwl.

Upon seeing this I tried to move back to ROCm 2.2, but it seems 2.2 is missing from the archive
http://repo.radeon.com/rocm/archive/ , so I downgraded to ROCm 2.1.

For comparison I attach isa dump with "old" (ROCm 2.1) and "new" (ROCm 2.3), where new is 5% slower.

Also please provide a way to install back ROCm 2.2 (e.g. by uploading it to archive).

[new.txt](https://github.com/RadeonOpenCompute/ROCm/files/3077435/new.txt)
[old.txt](https://github.com/RadeonOpenCompute/ROCm/files/3077436/old.txt)


---

## 评论 (17 条)

### 评论 #1 — preda (2019-04-14T14:18:04Z)

If desired I can provide executions instructions for GpuOwl for repro.


---

### 评论 #2 — preda (2019-04-15T12:51:41Z)

I have a manual ROCm OpenCL build, with the manifest below, that I synced and built now and it also displays the performance degradation.
```
/rocm-opencl$ repo info
Manifest branch: master
Manifest merge branch: refs/heads/master
Manifest groups: all,-notdefault
----------------------------
Project: ROCm-OpenCL-Runtime
Mount path: /home/preda/rocm-opencl/opencl
Current revision: master
Local Branches: 2 [amd-master, master]
----------------------------
Project: OpenCL-ICD-Loader
Mount path: /home/preda/rocm-opencl/opencl/api/opencl/khronos/icd
Current revision: master
Local Branches: 0
----------------------------
Project: ROCm-OpenCL-Driver
Mount path: /home/preda/rocm-opencl/opencl/compiler/driver
Current revision: master
Local Branches: 1 [master]
----------------------------
Project: llvm
Mount path: /home/preda/rocm-opencl/opencl/compiler/llvm
Current revision: amd-common
Local Branches: 1 [amd-common]
----------------------------
Project: clang
Mount path: /home/preda/rocm-opencl/opencl/compiler/llvm/tools/clang
Current revision: amd-common
Local Branches: 1 [amd-common]
----------------------------
Project: lld
Mount path: /home/preda/rocm-opencl/opencl/compiler/llvm/tools/lld
Current revision: amd-common
Local Branches: 1 [amd-common]
----------------------------
Project: ROCm-Device-Libs
Mount path: /home/preda/rocm-opencl/opencl/library/amdgcn
Current revision: master
Local Branches: 1 [master]
----------------------------
```

---

### 评论 #3 — amd-aakash (2019-04-15T23:27:46Z)

Hi the apt,yum tar balls for ROCm 2.2 are available now under: http://repo.radeon.com/rocm/archive/
You can also access them: http://repo.radeon.com/rocm/yum/2.2/ , http://repo.radeon.com/rocm/apt/2.2/

---

### 评论 #4 — sshaik123 (2019-04-16T13:29:02Z)

Preda, 

Can you please provide the instructions on how to build.  We are seeing errors while building the master branch code.  please find the make log in the attachment.

[build,log.txt](https://github.com/RadeonOpenCompute/ROCm/files/3085061/build.log.txt)



---

### 评论 #5 — preda (2019-04-16T20:59:01Z)

@sshaik123 : I looked at the compilation errors, it seems that the compiler is not supporting c++ 17. Could you please try a more recent compiler? I know it works for sure with g++ 8 and g++ 9. What version is the compiler you used? (g++ --version)

Other than that, everything seems fine, so just use a newer compiler and it should work.

---

### 评论 #6 — preda (2019-04-17T09:23:13Z)

@sshaik123 after compilation, running is easy, e.g.:
./gpuowl -prp 84682337
And it will display timing information.
./gpuowl -h for other command line options, such as -device N to select a specific GPU.

---

### 评论 #7 — sshaik123 (2019-04-18T14:31:24Z)

@preda, Thanks . Now we are able to build using latest gcc.  we are working on verifying the drop from 2.2 to 2.3 on our setups.
I think it takes more time to run with test -prp value 84682337.  Can we use the lower value to repro the perf drop issue. Please confirm.

---

### 评论 #8 — preda (2019-04-19T14:35:08Z)

@sshaik123 You don't have to run the *whole* PRP test -- timing information is displayed for every 10K iterations, in the form "1.02 ms/sq", millis per squaring. Just keep it running for about 10 or 20 lines to be displayed (i.e. 1M or 2M iterations), which should be in the order of 1 or 2 minutes.

Also, during the test, please watch for the GPU to not thermal throttle. Normally I set the sclock manually to something lower than max, e.g. on Radeon VII I use rocm-smi --setsclk 4.

Normally the timing information should be pretty stable (very low variance) between iterations, once the GPU reaches the stable temperature.


---

### 评论 #9 — preda (2019-04-19T14:40:10Z)

@sshaik123 The "-time" option can be useful to pin down the origin of the performance difference. "-time" will display timing information per kernel. (it does have an overhead, but it gives an overall idea of where the time is spent). I'd expect the analysis to show that there is one or a pair of slow kernels.


---

### 评论 #10 — preda (2019-04-19T14:52:21Z)

> I think it takes more time to run with test -prp value 84682337. Can we use the lower value to repro the perf drop issue. Please confirm.

To answer the question: the value passed to -prp ("the exponent") must be similar (close) to the one in the example in order to use the right FFT setup, and repro (the FFT size is displayed at startup). A much lower exponent changes the FFT size, which changes the whole problem.


---

### 评论 #11 — sshaik123 (2019-04-19T15:30:54Z)

@preda, Thanks for the info. I'm able to repro the issue. on my setup I m getting a drop of ~4.5 % from 2.2 to 2.3 . we are working on investing the root cause.   

---

### 评论 #12 — sshaik123 (2019-04-25T09:24:45Z)

Update: Internal ticket has been filed . Issue has been root caused ,  we are working on the fix.

---

### 评论 #13 — preda (2019-05-06T12:14:08Z)

Has this been fixed in ROCm 2.4?

---

### 评论 #14 — valeriob01 (2019-05-08T13:26:22Z)

No, apparently the issue has not been fixed. In 2.4 performance got even worse.

The situation with ROCm is becoming unsustainable. We are forced to use version 2.2 to overcome performance regressions in more recent releases, but that is a workaround.


---

### 评论 #15 — preda (2019-06-05T12:06:24Z)

Here is some diagnosis:
In the generated ISA, for the kernel "transposeW", ROCm 2.2 generates 117 vGPRs, while ROCm 2.4 generates 129 vGPRs. This produces a significant slow-down in this kernel.

Now the bug is: if ROCm 2.2 can compile that kernel with only 117 vGPRs, why ROCm 2.4 can't do the same, and instead goes for 129 vGPRs which is such a bad number, halving the occupancy and producing an obvious slowdown.

Also..: not fixed in ROCm 2.5!

---

### 评论 #16 — preda (2019-06-05T13:28:44Z)

In a recent commit in gpuowl
https://github.com/preda/gpuowl/commit/9b66d3fe6cc041a3dd873800f74d664b03ee020f
I re-structured my code in the affected kernel to get the compiler to not jump over 128vGPRs, and thus my problem is fixed (by finding a work-around).


---

### 评论 #17 — preda (2021-05-09T20:08:42Z)

Closing as old.

---
