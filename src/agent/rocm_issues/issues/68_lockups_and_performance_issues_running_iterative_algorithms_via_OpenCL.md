# lockups and performance issues running iterative algorithms via OpenCL

> **Issue #68**
> **状态**: closed
> **创建时间**: 2017-01-03T19:06:49Z
> **更新时间**: 2017-01-16T02:49:37Z
> **关闭时间**: 2017-01-16T02:49:37Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/68

## 描述

First - I've not validated output - I suspect invalid data - but I have been using arrayfire benchmarks to track performance of OpenCL on  ROCm and AMDGPU Pro (and OpenCL/CUDA, on NVidia boxen).

Please give this program a try (after installing arrayfire).
https://github.com/nevion/arrayfire-benchmark

You will note that Cholesky_f32/ Cholesky_f64 can soft lock or hardlock the machine (ROCm= softlock, AMDGPU-Pro=hardlock)

You will also note atrocious performance on sorting benchmarks.  The 2 could be related as these are data-driven iterative algorithms and possibly the only such in the benchmarks available.  The remainder of the benchmarks run seemingly run at acceptable (not necessarily performant) rates on the AMD stacks.  They all run acceptably on NVidia's OpenCL runtime.

You can list benchmarks with the -l argument.  All benchmarks function on CUDA's OpenCL

---

## 评论 (11 条)

### 评论 #1 — parallelo (2017-01-03T21:10:38Z)

Could you provide the process you use for building/installing Arrayfire?  (e.g. cmake command, etc)  That'll help streamline the troubleshooting process.  Thanks!

---

### 评论 #2 — nevion (2017-01-03T22:20:15Z)

I usually just install the prebuilt arrayfire here: https://arrayfire.com/download-splash/?redirect_to=/download

The included script updateLibraries.sh (not from me and not really used by me either) should work too.

I usually install to /opt/arrayfire-3 in which case cmake arguments, from the build directory would be:
cmake -DArrayFire_DIR=${AF_DIR}/share/ArrayFire/cmake ..

You will get 1-3 binaries in the bin folder depending on the platform availability - CPU, OpenCL, and CUDA .

---

### 评论 #3 — parallelo (2017-01-03T22:38:09Z)

If you are using prebuilt Arrayfire, then you should probably talk with the Arrayfire folks for further support.  They do not appear to be using ROCm-OpenCL for their "pre-configured" installation -- probably using the AMD APP SDK implementation instead.  

This dependency is mentioned on the Arrayfire page (https://github.com/arrayfire/arrayfire/wiki/Build-Instructions-for-Linux#opencl-build-dependencies):  

> OpenCL backend dependencies
> 
> Required:
> 
> Boost (>= 1.48. Latest recommended)
> An OpenCL SDK which may be one of the following
> -   AMD APP SDK
> -   ...


---

### 评论 #4 — nevion (2017-01-03T22:50:08Z)

Doesn't matter - shouldn't at least and I'll take care of it there if it does.  I've surveyed (and read) most of the code and you can't tell me an open source codebase like it won't work against ROCm's runtime.

It is a bug no matter what that it can crash the computer - right?

Performance isn't looking good either (I know it's a technical preview for now but it won't be forever).  I did want to mention occasionally you see good performance on a given test (like beats NVidia performance).

I'm not looking for support of arrayfire I'm trying to improve ROCm.

FYI most of how they do is the same way of doing things is in Boost.Compute too and you've got problems if you're going to pull the same stance there too.

---

### 评论 #5 — parallelo (2017-01-03T23:19:11Z)

Please check if the ROCm-OpenCL libraries are being used by the pre-built Arrayfire installation.  Those libs are located here by default:  /opt/rocm/opencl/lib/x86_64

---

### 评论 #6 — nevion (2017-01-03T23:22:36Z)

I've verified, they definitely are.  I have set LD_LIBRARY_PATH and verified with ldd.

Can you duplicate the fault via compiling and running instead of searching for blame/troubleshooting?  It should only take you about 20 minutes.

You can constrain to the benchmarks I've mentioned with the --benchmark=Cholesky_f32 - for instance.  There's also Sort_f32_ASCENDING (among other variants).

---

### 评论 #7 — nevion (2017-01-04T03:24:52Z)

@parallelo  also make sure you look at your dmesg after running against ROCm-OpenCL and the softlock I'm expecting.  You should see a variety of memory related faults (not your standard kernel oops format, probably from the newer KFD or ROCm specific things).  I'll post a few on my end just in case, but just be aware of it anyhow.

---

### 评论 #8 — gstoner (2017-01-04T03:28:17Z)

I am talking to the lead developer for OpenCL on ROCm so that he can look at this.  We are still tuning the compiler and runtime for OpenCL on ROCm for performance.   I am looking for Functionality issues on this first release. 

 but thanks you for the input. 

---

### 评论 #9 — nevion (2017-01-05T07:12:13Z)

Here's some output from
```
LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64/ ./benchmark_opencl -b Cholesky_f32
[  CELERO  ]
-----------------------------------------------------------------------------------------------------------------------------------------------
     Group      |   Experiment    |   Prob. Space   |     Samples     |   Iterations    |    Baseline     |  us/Iteration   | Iterations/sec  | 
-----------------------------------------------------------------------------------------------------------------------------------------------
LAPACK_Cholesky | Baseline        | Null            |              10 |              10 |         1.00000 |         1.00000 |      1000000.00 | 
LAPACK_Cholesky | Baseline        |            1024 |              10 |              10 |         1.00000 |         0.90000 |      1111111.11 | 
LAPACK_Cholesky | Baseline        |            4096 |              10 |              10 |         1.00000 |         0.80000 |      1250000.00 | 
LAPACK_Cholesky | Baseline        |           16384 |              10 |              10 |         1.00000 |         0.90000 |      1111111.11 | 
LAPACK_Cholesky | Baseline        |           65536 |              10 |              10 |         1.00000 |         0.80000 |      1250000.00 | 
LAPACK_Cholesky | Baseline        |          262144 |              10 |              10 |         1.00000 |         0.60000 |      1666666.67 | 
LAPACK_Cholesky | Baseline        |         1048576 |              10 |              10 |         1.00000 |         0.60000 |      1666666.67 | 
LAPACK_Cholesky | Baseline        |         4194304 |              10 |              10 |         1.00000 |         1.00000 |      1000000.00 | 
LAPACK_Cholesky | Cholesky_f32    |            1024 |              10 |              10 |      6103.88889 |      5493.50000 |          182.03 | 
LAPACK_Cholesky | Cholesky_f32    |            4096 |              10 |              10 |     11803.12500 |      9442.50000 |          105.90 | 
LAPACK_Cholesky | Cholesky_f32    |           16384 |              10 |              10 |     20886.88889 |     18798.20000 |           53.20 |
```

It doesn't immediately hardlock like AMDGPU-Pro's runtime and the program remains cancelable and didn't hang on repeated runs (this defies previous experiences).  Here's dmesg output:
```
[112679.546533] VM fault (0x02, vmid 8) at page 35826333, read from 'TC2' (0x54433200) (
[112679.546537] amdgpu 0000:03:00.0: GPU fault detected: 147 0x06d80402
[112679.547412] amdgpu 0000:03:00.0:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x0222AABE
[112679.548290] amdgpu 0000:03:00.0:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10188002
[112679.549171] VM fault (0x02, vmid 8) at page 35826366, read from 'TC4' (0x54433400) (
[112679.549176] amdgpu 0000:03:00.0: GPU fault detected: 147 0x07f80402
[112679.550050] amdgpu 0000:03:00.0:   VM_CONTEXT1_PROTECTION_FAULT_ADDR   0x0222AADF
[112679.550928] amdgpu 0000:03:00.0:   VM_CONTEXT1_PROTECTION_FAULT_STATUS 0x10044002
```

This time I was not able to reproduce soft-lockups, I believe I've seen them previously but, well this has left me a bit confused.

FYI AMDGPU-Pro will hardlock immediately upon the first Cholesky problemsize's benchmark - and I reproduced that a few times.

---

### 评论 #10 — nevion (2017-01-15T10:56:41Z)

I wanted to provide an update - apparently LD_PRELOADing libOpenCL.so was not enough as the ICD loader got confused by the same named libraries and ended up using libamdocl64.so from amdgpu-pro rather than rocm's.  To address this, I've completely removed amdgpu pro from the system.  I caught it loading the symbol under gdb while debugging other issues.  To reduce user error, can we make sure the 2 can coexist installation wise on the same system - even if the run times don't?  Or have some way of dealing with this ICD situation.  I believe simply pulling in amdgpu pro drivers (without explicitly asking for opencl) will bring about this confusing situation.

---

### 评论 #11 — nevion (2017-01-16T02:49:36Z)

Ok other than the compiler error I reported as #77 and native_exp not working on double, I was able to run everything.  Performance on the cholesky benchmarks still is quite bad, but it caused no output in dmesg this time.  I've not had time to compare sorting performance.  So I still want to urge some investigation on performance but I'm closing this issue out for now.

---
