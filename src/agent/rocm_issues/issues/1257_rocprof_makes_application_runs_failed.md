# rocprof makes application runs failed

> **Issue #1257**
> **状态**: closed
> **创建时间**: 2020-10-08T23:02:45Z
> **更新时间**: 2020-12-11T07:06:52Z
> **关闭时间**: 2020-12-11T07:06:52Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1257

## 描述

Using ROCm 3.8,
Without rocprof, my application always run.
With rocprof, there is a small chance my app runs but most of the time I got two kinds of errors.
1. error(4105) "queue_event_callback(), queue error handling is not supported"
2. Thread 1 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
Need to have this random and broken behavior fixed.

Here is a backtrace from gdb `rocprof --hsa-trace gdb ./bin/check_spo_batched`
```
Thread 1 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
0x00007fff75cbad05 in rocr::HSA::hsa_signal_store_relaxed(hsa_signal_s, long) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007fff75cbad05 in rocr::HSA::hsa_signal_store_relaxed(hsa_signal_s, long) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
#1  0x00007fff748fc98e in roctracer::hsa_support::hsa_signal_store_relaxed_callback(hsa_signal_s, long) ()
   from /opt/rocm/roctracer/lib/libroctracer64.so.1
#2  0x00007fff7609d1ce in __tgt_rtl_run_target_team_region () from /opt/rocm/aomp/lib/libomptarget.rtl.hsa.so
#3  0x00007ffff6a65a9a in target(long, void*, int, void**, void**, long*, long*, int, int, int) ()
   from /opt/rocm/aomp/lib/libomptarget.so
#4  0x00007ffff6a5cecf in __tgt_target_teams () from /opt/rocm/aomp/lib/libomptarget.so
#5  0x0000000000417728 in qmcplusplus::einspline_spo_omp<double>::multi_evaluate_vgh(std::vector<qmcplusplus::SPOSet*, std::allocator<qmcplusplus::SPOSet*> > const&, std::vector<qmcplusplus::ParticleSet*, std::allocator<qmcplusplus::ParticleSet*> > const&, int) ()
#6  0x000000000040710d in main ()
```

Reproducer uses AOMP clang++:
```
git clone https://github.com/ye-luo/miniqmc.git
cd miniqmc/build
cmake -D CMAKE_CXX_COMPILER=clang++       -D ENABLE_OFFLOAD=1       -D OFFLOAD_TARGET=amdgcn-amd-amdhsa       -D OFFLOAD_ARCH=gfx906 ..
make -j
export OMP_NUM_THREADS=8
rocprof --hsa-trace ./bin/check_spo_batched
rocprof --hsa-trace ./bin/check_spo
```



---

## 评论 (9 条)

### 评论 #1 — rkothako (2020-10-09T09:39:38Z)

Hi @ye-luo 
We are able to reproduce this issue internally and filed an internal ticket to track the progress.
We will update the progress on this.

---

### 评论 #2 — ROCmSupport (2020-12-11T06:01:43Z)

Hi @ye-luo 
Fix is ready and its available 3.10.
I recommend to try with the latest ROCm 3.10.

**My output follows:**
taccuser@taccuser-SYS-4028GR-TR2:~/miniqmc/build$ PATH=$PATH:/opt/rocm/bin /opt/rocm/bin/rocprof --hsa-trace ./bin/check_spo_batched
RPL: on '201211_112810' from '/opt/rocm-3.10.0/rocprofiler' in '/home/taccuser/miniqmc/build'
RPL: profiling '"./bin/check_spo_batched"'
RPL: input file ''
RPL: output dir '/tmp/rpl_data_201211_112810_9935'
RPL: result dir '/tmp/rpl_data_201211_112810_9935/input_results_201211_112810'
ROCProfiler: input from "/tmp/rpl_data_201211_112810_9935/input.xml"
  0 metrics
  0 traces
ROCTracer (pid=9958):
    HSA-trace()
    HSA-activity-trace()
miniqmc git branch: OMP_offload
miniqmc git commit: 53f9aaa1e20d81a98bd0b04ea67fa316bb33557c

Number of orbitals/splines = 192
Tile size = 192
Number of tiles = 1
Rmax = 1.7
Iterations = 5
OpenMP threads = 8

SPO coefficients size = 98304000 bytes (93.75 MB)
Constructing 8 movers!
Complete(), Tracker::Complete bad signal value
/opt/rocm/bin/rocprof: line 271:  9958 Aborted                 (core dumped) "./bin/check_spo_batched"
START timestamp found (0ns)
File '/home/taccuser/miniqmc/build/results.csv' is generating
File '/home/taccuser/miniqmc/build/results.stats.csv' is generating
dump json 0:1
File '/home/taccuser/miniqmc/build/results.json' is generating
File '/home/taccuser/miniqmc/build/results.hsa_stats.csv' is generating
dump json 0:1
File '/home/taccuser/miniqmc/build/results.json' is generating
File '/home/taccuser/miniqmc/build/results.copy_stats.csv' is generating
File '/home/taccuser/miniqmc/build/results.json' is generating

---

### 评论 #3 — ye-luo (2020-12-11T06:19:24Z)

My issue remains. Please check with the reproducer provided in this issue. @ROCmSupport please re-open the issue.

---

### 评论 #4 — ROCmSupport (2020-12-11T06:23:53Z)

Hi @ye-luo 
You mean you are still able to reproduce the issue with the latest 3.10 also?

I am not able to reproduce, now, the error. Please check my previous comment for the log(tried the same application as yours)


---

### 评论 #5 — ye-luo (2020-12-11T06:29:21Z)

You log shows
```
Complete(), Tracker::Complete bad signal value
/opt/rocm/bin/rocprof: line 271: 9958 Aborted (core dumped) "./bin/check_spo_batched"
```
you failed. Just run the app without the rocprof to see what printout to be expected from the app.

---

### 评论 #6 — ROCmSupport (2020-12-11T06:34:37Z)

Got it.
So the previously mentioned errors are fixed and no more observed as the fix has been integrated into 3.10.
But now it turns to a different issue. Recommend to open a new ticket.
Thank you.

---

### 评论 #7 — ROCmSupport (2020-12-11T06:48:33Z)

@ye-luo 
Anyway, I am tracking the new issue also separately.
I will work with profiler team for the fix.
Thank you.


---

### 评论 #8 — ye-luo (2020-12-11T07:00:20Z)

I opened a new issue with a bit more investigation hopefully it will be helpful for hunting bugs. You may close this one.

---

### 评论 #9 — ROCmSupport (2020-12-11T07:06:52Z)

Thanks @ye-luo 

---
