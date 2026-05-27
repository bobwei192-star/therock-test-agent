# memory bandwidth of HBM1 drops with more than 2GB to consume

> **Issue #102**
> **状态**: closed
> **创建时间**: 2017-03-28T21:18:49Z
> **更新时间**: 2018-06-03T14:46:37Z
> **关闭时间**: 2018-06-03T14:46:37Z
> **作者**: psteinb
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/102

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

Hi, I ran a series of GPU-stream instances on a R9 Fiji Nano with rocm 1.4 on a E5 haswell box. I looked at the OpenCL and HIP implementations available in [GPU-Stream 3.1](https://github.com/UoB-HPC/GPU-STREAM). 

I am wondering why the bandwidth drops off by 2x after a total of 2GB of data is consumed on the device. I attached the plot here.

![gpu_stream_add_bandwidth_rocm](https://cloud.githubusercontent.com/assets/1465603/24427876/c69581e6-140c-11e7-903f-4e8a88110e62.png)


---

## 评论 (22 条)

### 评论 #1 — pszi1ard (2017-05-02T18:24:41Z)

TLB misses?

---

### 评论 #2 — gstoner (2017-05-02T18:27:27Z)

Can you re-run with ROCm 1.5 and new OpenCL stack?  https://github.com/RadeonOpenCompute/ROCm

---

### 评论 #3 — psteinb (2017-05-03T06:22:23Z)

> TLB misses? 

could be, but how do I check?

> rocm 1.5?

will do, after I [updated to xenial](https://github.com/RadeonOpenCompute/ROCm/issues/109). :/

---

### 评论 #4 — pszi1ard (2017-05-03T11:40:01Z)

Actually, you're reading contiguous memory, so TLB is likely not an issue.

BTW, I could install ROCm 1.5 on Ubuntu 14.04 (the docs only claim that it "has been tested" only on 16.04). 

---

### 评论 #5 — gstoner (2017-05-03T12:42:07Z)

I was looking at the text the opencl was not using the right string on the install instructions it should be sudo apt-get install rocm-opencl-dev

---

### 评论 #6 — gstoner (2017-05-03T12:56:25Z)

When you run hcc you will need to update gcc g++

Get Outlook for iOS<https://aka.ms/o0ukef>



On Wed, May 3, 2017 at 6:40 AM -0500, "Szilárd Páll" <notifications@github.com<mailto:notifications@github.com>> wrote:


Actually, you're reading contiguous memory, so TLB is likely not an issue.

BTW, I could install ROCm 1.5 on Ubuntu 14.04 (the docs only claim that it "has been tested" only on 16.04).

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/102#issuecomment-298887528>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuX6o7rLdcitY0AGwI8CwZ_IOT8mJks5r2GeSgaJpZM4MsNTa>.


---

### 评论 #7 — psteinb (2017-05-04T11:16:49Z)

just checked with rocm 1.5 and got the following (apologies for the unpolished plot):

![add_bandwidth_versus_rocm_version](https://cloud.githubusercontent.com/assets/1465603/25701185/878b7a60-30cb-11e7-9eb8-9495c15c1569.png)

I see a regession there from 1.4 to 1.5. if you want to see other kernels, just let me know. the results are from [this branch for hc support](https://github.com/psteinb/GPU-STREAM/tree/rocm_hc_support) and [this branch for opencl support](https://github.com/psteinb/GPU-STREAM/tree/rocm_opencl_support). but the problem of this issue is still there.

---

### 评论 #8 — gstoner (2017-05-04T11:20:09Z)

Yes, can you send me kernel via my AMD email, Linux driver team upgraded the Linux kernel.  We need to retune the memory kernel api's 

---

### 评论 #9 — psteinb (2017-05-04T11:21:56Z)

will do! thanks.


---

### 评论 #10 — gstoner (2017-07-02T17:36:42Z)

Can you test 1.6,  and send me the data.     It out now.   We still working through some changes in the base Linux driver outside the ROCm memory management stack that happen to go to Linux Kernel  4.9.  

---

### 评论 #11 — gstoner (2017-07-25T19:49:05Z)

It was TLB issue on GFX8 devices,  1.6.1 is addressing this issue. It was a fix in the thunk layer.   Big jump in memory performance on FIJI.    Working 2 MB TLB on Vega10 next 

---

### 评论 #12 — psteinb (2017-07-25T20:00:23Z)

Awesome news, @gstoner. I checked with 1.6-77 but no difference. Can't wait to try 1.6.1! Congratulations to your team for fixing this. Can't wait to see Vega FE in Action.



---

### 评论 #13 — gstoner (2017-07-25T20:15:25Z)

@psteinb You need to send me your script for graphing the data.    Also you should check this out as tool https://github.com/patflick/miopen-benchmark/blob/master/gputop.cpp for pulling CU & Mem Frequency, Temp and Fan Speed.    We are now working on C API as well for ROCm-SMI. 

---

### 评论 #14 — psteinb (2017-07-26T07:31:08Z)

would love to provide you the plotting markdown, but it relies on 
Babelstream csv input - which I in turn create with some sed/awk magic. 
I think I have time to push a PR to babelstream to create csv output. 
Once that is done/merged, I provide you the R markdown to produce the 
plots - I think it's more clean that way.

Regarding the gputop.cpp that you shared. It would be nice if 
`Device::get_devices` would be ported to the `hc` namespace. Stuff like 
this can be extremely handy in certain situations. But I agree, putting 
it into ROCM-SMI has priority.




---

### 评论 #15 — psteinb (2017-07-26T12:57:58Z)

1.6-115 looks much better for the add kernel:

![image](https://user-images.githubusercontent.com/1465603/28621828-8a4e75bc-7212-11e7-904f-709ce31ec1cc.png)

strange enough the copy kernel still exposes some difference between opencl, hip and hc:

![image](https://user-images.githubusercontent.com/1465603/28621862-a7ca3554-7212-11e7-8f40-e7981a44de59.png)

the dip at 2GB is still there. All in all, good job to the team. the time progression visible here is amazing and on top ... it's open source!

---

### 评论 #16 — aditya4d (2017-07-31T01:39:06Z)

Can you try a simple `A += k * A` ? This shows loading from A and storing to A. Also, can you share the code in a easily reproducible repo? (I want to use it for my experiments too).

---

### 评论 #17 — psteinb (2017-07-31T08:33:18Z)

Dear Aditya,

can you elaborate what you mean by `A += k * A`. I am guessing that you 
are referring to `A[i] += k * A[i]`, so that k is a scalar and A is a 1D 
array. I am not sure how that would differ from a copy kernel as in 
`b[i] = a[i]`, except the 2 FP ops or 1 FMA in there.

right now, the guys from Bristol haven't made any move on my HC PR to 
babelstream. So for now, you have to live with:

```
$ git clone git@github.com:psteinb/GPU-STREAM.git babelstream
$ cd babelstream
$ git checkout rocm_hc_support
$ make -f HC.make
$ ./hc-stream --list
BabelStream
Version: 3.2
Implementation: HC

Devices:
0: CPU Device
1: AMD HSA Agent gfx8032
$ ./hc-stream --device 1
BabelStream
Version: 3.2
Implementation: HC
Running kernels 100 times
Precision: double
Array size: 268.4 MB (=0.3 GB)
Total size: 805.3 MB (=0.8 GB)
Using HC device AMD HSA Agent gfx8032
Function    MBytes/sec  Min (sec)   Max         Average
Copy        375960.286  0.00143     0.00154     0.00148
Mul         383903.436  0.00140     0.00152     0.00147
Add         405419.769  0.00199     0.00206     0.00202
Triad       407362.910  0.00198     0.00206     0.00202
Dot         329400.789  0.00163     0.00178     0.00169
```


---

### 评论 #18 — mgjaggers (2017-10-04T22:10:34Z)

@psteinb Does this simply affect large arrays of data or the amount of data moved?  For example, in your "ADD" algorithm, we use 6 variables instead of 3.  Say it's A, B, C, and X, Y, Z respectively. Now, once the A, B, and C arrays start to approach 2GB, we start transition to using the X, Y, and Z arrays instead.  Does what I'm explaining make sense?


---

### 评论 #19 — aaronenyeshi (2017-11-09T20:39:54Z)

This issue should be fixed with HIP. Now HIP achieves the same performance as OpenCL. HCC however cannot be fixed due to inherent limitations of C++ AMP API design.

---

### 评论 #20 — psteinb (2017-11-09T21:34:03Z)

any more news on this? what do you mean by the inherent C++ AMP API design?


---

### 评论 #21 — aaronenyeshi (2017-11-09T22:47:33Z)

Sorry, I meant to say that we have done everything we could on the compiler side for HIP and HCC. HIP is fixed, but HCC still sees this. There is an internal issue opened for the HCC performance drop assigned to run-time team.
Here are my findings:
**Issue:**
HCC has much lower memory bandwidth than OpenCL on ROCm/LC. There is a strange 25% perf boost that occurs in OpenCL and sometimes in HCC (copy or mul only kernel). (400 boosts to 307 microsec) HIP gains the boost after recent global id fix. This makes OCL and HIP faster than HCC.
**Details: Please ignore orange line (hip was fixed)**
In the COPY graph below, please notice the YELLOW line. HCC is able to achieve just as much performance for Memory Bandwidth as OpenCL, if I comment out the other tests (MUL, ADD, TRIAD, and DOT). HCC is able to achieve a large speed-up of 25% if I ran COPY kernel alone, and please check the detailed profiling durations of COPY kernel in the table at the bottom.
![image](https://user-images.githubusercontent.com/17602366/32633244-c46121ae-c574-11e7-9676-20dbd3259183.png)
Similarly in the MUL graph below, please notice the YELLOW line. HCC is able to achieve better Memory BW performance than OCL. This yellow line occurs after I comment out COPY, ADD, TRIAD, and DOT tests. Therefore, I suspect that there is an optimization that occurs for HCC only when the kernel is ran alone. Please see the profiling details below.
![image](https://user-images.githubusercontent.com/17602366/32633251-c90fff22-c574-11e7-9a2c-450aac81cb63.png)
I profiled the different languages (for COPY kernel) under different conditions. In the table below, HCC, HIP and OCL were tested under two conditions. 1) First was to include all test cases (COPY, MUL, ADD, TRIAD, DOT), and 2) second row includes only COPY test case.

OpenCL will eventually achieve this 25% perf boost in kernel time. For HCC, the 25% perf boost only occurs when you run the COPY kernel alone (or MUL kernel alone). 

**Profiling information collected:**
Using CopyXL profiler, these are copy kernel durations (in microseconds)

HCC: | all tests included: |   |   |   |   |   |   |   |  
-- | -- | -- | -- | -- | -- | -- | -- | -- | --
  | 413 | 407 | 414 | 408 | 409 | 414 | 410 | 406 | 415 | 416
  | copy-only test: |   |   |   |   |   |   |   |  
  | 408 | 424 | 410 | 411 | 406 | 409 | 408 | **307** | **307** | **309**
  |   |   |   |   |   |   |   |   |   |  
OpenCL: | all tests included: |   |   |   |   |   |   |   |  
  | 409 | 401 | **306** | **306** | **306** | **306** | **306** | **306** | **306** | **307**
  | copy-only test: |   |   |   |   |   |   |   |  
  | 399 | 400 | 402 | 399 | **306** | **307** | **307** | **307** | **305** | **306**
  |   |   |   |   |   |   |   |   |   |  
HIP: | all tests included: |   |   |   |   |   |   |   |  
  | 451 | 434 | 403 | 403 | 403 | 403 | 402 | 402 | 403 | 403
  | copy-only test: |   |   |   |   |   |   |   |  
  | 454 | 440 | 443 | 441 | 444 | 440 | 440 | 438 | 433 | 402

**What we've done:**

- Set clocks on high: “/opt/rocm/bin/rocm-smi --setsclk 7”. 
- The memory is allocated once at start of benchmark and re-used. (HIP_DB=1)
- This is same code launched for each iteration.  We see same behavior for OpenCL kernels and HCC kernels.
- Examined performance counters and see ~same for each iteration.

**To Reproduce 25% perf boost in OCL:**
Checkout HCC/OCL branch link above.
Depending on the language, use these commands:
HCC:
make -f HC.make
./hc-stream --device 1 --float --arraysize 16777216 --numtimes 10
OCL: 
make -f OpenCL.make COMPILER=HCC
./ocl-stream --device 1 --float --arraysize 16777216 --numtimes 10
 
**Expected Result:**
OpenCL and HCC should have about the same performance. Both reached 307 consistently for kernel time. And memory bandwidth over 400,000MBytes/sec for Copy and Mul.

****There is a ticket opened internally for investigation into HCC run-time issues seen above.****

---

### 评论 #22 — aaronenyeshi (2017-11-09T22:52:54Z)

Here are more recent graphs:
![image](https://user-images.githubusercontent.com/17602366/32633758-c721f862-c576-11e7-9c1d-403f275d05dd.png)
![image](https://user-images.githubusercontent.com/17602366/32633759-c920ea9c-c576-11e7-9ba1-679f3677c9d8.png)



---
