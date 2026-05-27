# rocprof makes application runs failed bug series 2

> **Issue #1328**
> **状态**: closed
> **创建时间**: 2020-12-11T06:57:50Z
> **更新时间**: 2021-12-15T06:01:17Z
> **关闭时间**: 2021-12-15T00:57:15Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1328

## 描述

A follow up of #1257
Using ROCm 3.10,
Without rocprof, my application always run.
With rocprof, application crashes.

build the app with AOMP shipped by 3.10. 
AOMP_11.9-1 clang version 11.0.0 (/src/external/rocm-aomp/amd-llvm-project/clang 5cfd278ccb98e85bc8c193bc9d8fe40233c5e2be)

Here is a backtrace from gdb `rocprof --hsa-trace gdb ./bin/check_spo_batched`
```
Thread 1 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
0x0000000000500c00 in ?? ()
(gdb) bt
#0  0x0000000000500c00 in ?? ()
#1  0x00007fffb5cb8da8 in rocr::HSA::hsa_signal_store_screlease(hsa_signal_s, long) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffeb4712e6e in roctracer::hsa_support::hsa_signal_store_screlease_callback(hsa_signal_s, long) ()
   from /opt/rocm-3.10.0/roctracer/tool/../lib/libroctracer64.so.1
#3  0x00007fffb6088360 in core::Runtime::Memcpy(hsa_signal_s, void*, void const*, unsigned long) ()
   from /opt/rocm/aomp/lib/libomptarget.rtl.hsa.so
#4  0x00007fffb609d0a8 in __tgt_rtl_data_submit_async () from /opt/rocm/aomp/lib/libomptarget.rtl.hsa.so
#5  0x00007ffff6a671dd in target_data_begin(DeviceTy&, int, void**, void**, long*, long*, __tgt_async_info*) ()
   from /opt/rocm/aomp/lib/libomptarget.so
#6  0x00007ffff6a677e2 in target(long, void*, int, void**, void**, long*, long*, int, int, int) ()
   from /opt/rocm/aomp/lib/libomptarget.so
#7  0x00007ffff6a5ec79 in __tgt_target () from /opt/rocm/aomp/lib/libomptarget.so
#8  0x000000000041397b in qmcplusplus::einspline_spo_omp<double>::einspline_spo_omp(qmcplusplus::einspline_spo_omp<double> const&, int, int) ()
#9  0x0000000000408264 in omp_outlined. ()
#10 0x00007ffff6d1a813 in __kmp_invoke_microtask () from /opt/rocm/aomp/lib/libomp.so
#11 0x00007ffff6cacca5 in __kmp_invoke_task_func () from /opt/rocm/aomp/lib/libomp.so
#12 0x00007ffff6cb13de in __kmp_fork_call () from /opt/rocm/aomp/lib/libomp.so
#13 0x00007ffff6c9da79 in __kmpc_fork_call () from /opt/rocm/aomp/lib/libomp.so
#14 0x0000000000406eb5 in main ()
```

second run
```
Thread 2 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffb59e5700 (LWP 24526)]
0x00007fffb5cb89df in rocr::HSA::hsa_signal_load_relaxed(hsa_signal_s) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007fffb5cb89df in rocr::HSA::hsa_signal_load_relaxed(hsa_signal_s) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
#1  0x00007ffeb4712b51 in roctracer::hsa_support::hsa_signal_load_relaxed_callback(hsa_signal_s) ()
   from /opt/rocm-3.10.0/roctracer/tool/../lib/libroctracer64.so.1
#2  0x00007ffeb474284a in proxy::Tracker::Complete(long, roctracer::trace_entry_t*) ()
   from /opt/rocm-3.10.0/roctracer/tool/../lib/libroctracer64.so.1
#3  0x00007ffeb4742dc7 in proxy::Tracker::Handler(long, void*) ()
   from /opt/rocm-3.10.0/roctracer/tool/../lib/libroctracer64.so.1
#4  0x00007fffb5cd59eb in rocr::core::Runtime::AsyncEventsLoop(void*) ()
   from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
#5  0x00007fffb5c83367 in rocr::os::ThreadTrampoline(void*) () from /opt/rocm/aomp/lib/../../hsa/lib/libhsa-runtime64.so.1
#6  0x00007ffff6a22609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#7  0x00007ffff6949293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

```

Using AOMP
AOMP_STANDALONE_11.11-2 clang version 11.0.0 (https://github.com/ROCm-Developer-Tools/amd-llvm-project de58da8db4581dd8f17a613a33c0f916b56be788)
```
Thread 9 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffd2d833a00 (LWP 25473)]
0x0000000000000000 in ?? ()
(gdb) bt
#0  0x0000000000000000 in ?? ()
#1  0x00007fffadd7f479 in ?? () from /usr/lib/aomp/lib/libhsa-runtime64.so.1
#2  0x00007fffac9f7c35 in roctracer::hsa_support::hsa_signal_wait_scacquire_callback(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm-3.10.0/roctracer/tool/../lib/libroctracer64.so.1
#3  0x00007fffae0273da in __tgt_rtl_run_target_team_region () from /usr/lib/aomp/lib/libomptarget.rtl.amdgpu.so
#4  0x00007fffae027ee0 in __tgt_rtl_run_target_region_async () from /usr/lib/aomp/lib/libomptarget.rtl.amdgpu.so
#5  0x00007ffff6a675c3 in ?? () from /usr/lib/aomp/lib/libomptarget.so
#6  0x00007ffff6a5dfb9 in __tgt_target () from /usr/lib/aomp/lib/libomptarget.so
#7  0x000000000041397b in qmcplusplus::einspline_spo_omp<double>::einspline_spo_omp(qmcplusplus::einspline_spo_omp<double> const&, int, int) ()
#8  0x0000000000408264 in omp_outlined. ()
#9  0x00007ffff6d1a793 in __kmp_invoke_microtask () from /usr/lib/aomp/lib/libomp.so
#10 0x00007ffff6cacc25 in ?? () from /usr/lib/aomp/lib/libomp.so
#11 0x00007ffff6cabd41 in ?? () from /usr/lib/aomp/lib/libomp.so
#12 0x00007ffff6d03dc2 in ?? () from /usr/lib/aomp/lib/libomp.so
#13 0x00007ffff6a21609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#14 0x00007ffff6948293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```
run 2
```
Thread 8 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffd2e035980 (LWP 25551)]
0x0000000000000000 in ?? ()
(gdb) bt
#0  0x0000000000000000 in ?? ()
#1  0x00007fffadd7f088 in ?? () from /usr/lib/aomp/lib/libhsa-runtime64.so.1
#2  0x00007fffac9eed5e in roctracer::hsa_support::hsa_signal_store_relaxed_callback(hsa_signal_s, long) ()
   from /opt/rocm-3.10.0/roctracer/tool/../lib/libroctracer64.so.1
#3  0x00007fffae027369 in __tgt_rtl_run_target_team_region () from /usr/lib/aomp/lib/libomptarget.rtl.amdgpu.so
#4  0x00007fffae027ee0 in __tgt_rtl_run_target_region_async () from /usr/lib/aomp/lib/libomptarget.rtl.amdgpu.so
#5  0x00007ffff6a675c3 in ?? () from /usr/lib/aomp/lib/libomptarget.so
#6  0x00007ffff6a5dfb9 in __tgt_target () from /usr/lib/aomp/lib/libomptarget.so
#7  0x000000000041397b in qmcplusplus::einspline_spo_omp<double>::einspline_spo_omp(qmcplusplus::einspline_spo_omp<double> const&, int, int) ()
#8  0x0000000000408264 in omp_outlined. ()
#9  0x00007ffff6d1a793 in __kmp_invoke_microtask () from /usr/lib/aomp/lib/libomp.so
#10 0x00007ffff6cacc25 in ?? () from /usr/lib/aomp/lib/libomp.so
#11 0x00007ffff6cabd41 in ?? () from /usr/lib/aomp/lib/libomp.so
#12 0x00007ffff6d03dc2 in ?? () from /usr/lib/aomp/lib/libomp.so
#13 0x00007ffff6a21609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#14 0x00007ffff6948293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```
run 3
```
Thread 3 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffadadf700 (LWP 26064)]
0x0000000000000000 in ?? ()
(gdb) bt
#0  0x0000000000000000 in ?? ()
#1  0x00007fffadd7f1c8 in ?? () from /usr/lib/aomp/lib/libhsa-runtime64.so.1
#2  0x00007fffad0b07b5 in ?? () from /opt/rocm-3.10.0/rocprofiler/lib/librocprofiler64.so
#3  0x00007fffad0b0b3d in ?? () from /opt/rocm-3.10.0/rocprofiler/lib/librocprofiler64.so
#4  0x00007fffadd9bd4b in ?? () from /usr/lib/aomp/lib/libhsa-runtime64.so.1
#5  0x00007fffadd49787 in ?? () from /usr/lib/aomp/lib/libhsa-runtime64.so.1
#6  0x00007ffff6a21609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#7  0x00007ffff6948293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```
run 4
```
error(4105) "queue_event_callback(), queue error handling is not supported"

Thread 7 "check_spo_batch" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffd2e837900 (LWP 26445)]
0x0000000000000000 in ?? ()
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

## 评论 (43 条)

### 评论 #1 — ROCmSupport (2020-12-11T07:10:37Z)

Thanks @ye-luo 
We are tracking this issue internally and working with dev.
Will share an update soon.
Thank you.

---

### 评论 #2 — ye-luo (2021-04-09T18:13:36Z)

Ping. Still broken in 4.1.

---

### 评论 #3 — ROCmSupport (2021-04-12T07:29:21Z)

Hi @ye-luo, yes, its broken in 4.1 too, which we know.
I just informed developer for the status on this. Let me share an update once I get any.
Thank you.

---

### 评论 #4 — ye-luo (2021-08-18T03:07:43Z)

remains broken in 4.3

---

### 评论 #5 — ROCmSupport (2021-08-19T13:02:49Z)

Hi @ye-luo 
Thanks for the update. I have increased the priority and it will be hopefully fixed in next public release.
Thank you.

---

### 评论 #6 — ye-luo (2021-10-30T00:43:33Z)

Still broken in 4.5.

---

### 评论 #7 — ronlieb (2021-11-03T19:56:03Z)

Hi Ye, we recently fixed an issue in the libomptarget where we released a packet a bit too early:
[libomptarget] [amdgpu] After a kernel dispatch packet is published, its contents must not be accessed.


can you try on ROCm 4.5 with the AOMP 14.0 you built yesterday ?

---

### 评论 #8 — ye-luo (2021-11-03T20:11:27Z)

My AOMP build
```
$ clang++ -v
AOMP_STANDALONE_14.0-0 clang version 14.0.0 (https://github.com/radeonopencompute/llvm-project 11d5fa11d52cc4beca16e57b9a16a56947e58635)
```
And using rocprof from ROCm 4.5, both
```
rocprof --hsa-trace ./bin/check_spo_batched
```
and
```
rocprof --stats ./bin/check_spo_batched
```
crash. The crashes happen at the beginning of the run.

---

### 评论 #9 — dhruvachak (2021-11-04T02:01:16Z)

@ye-luo Do you have a stack trace for the latest crash?


---

### 评论 #10 — ye-luo (2021-11-04T02:31:53Z)

With `--hsa-trace`
```
/opt/rocm/bin/rocprof --hsa-trace gdb ./bin/check_spo_batched
RPL: on '211103_212535' from '/opt/rocm-4.5.0/rocprofiler' in '/home/yeluo/opt/miniqmc/build_r7_rocmbuild_offload'
...
Starting program: /home/yeluo/opt/miniqmc/build_r7_rocmbuild_offload/bin/check_spo_batched 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffee50c6700 (LWP 3664285)]
[New Thread 0x7ffee3e57700 (LWP 3664286)]
ompt_pre_init(): tool_setting = 1
ompt_pre_init(): ompt_enabled = 0
ROCProfiler: input from "/tmp/rpl_data_211103_212535_3664250/input.xml"
  0 metrics
ROCTracer (pid=3664276): 
    HSA-trace()
    HSA-activity-trace()

Thread 1 "check_spo_batch" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff6a64859 in __GI_abort () at abort.c:79
#2  0x00007ffee2fe3743 in HsaRsrcFactory::HsaRsrcFactory(bool) () from /opt/rocm-4.5.0/roctracer/tool/libtracer_tool.so
#3  0x00007ffee2fcd747 in OnLoad () from /opt/rocm-4.5.0/roctracer/tool/libtracer_tool.so
#4  0x00007ffee3f38ddf in rocr::core::Runtime::LoadTools() () from /home/yeluo/rocm/aomp/lib-debug/../lib/libhsa-runtime64.so.1
#5  0x00007ffee3f398f0 in rocr::core::Runtime::Load() () from /home/yeluo/rocm/aomp/lib-debug/../lib/libhsa-runtime64.so.1
#6  0x00007ffee3f399fc in rocr::core::Runtime::Acquire() () from /home/yeluo/rocm/aomp/lib-debug/../lib/libhsa-runtime64.so.1
#7  0x00007ffee3f18ade in rocr::HSA::hsa_init() () from /home/yeluo/rocm/aomp/lib-debug/../lib/libhsa-runtime64.so.1
#8  0x00007ffee43428e9 in HSALifetime::HSALifetime (this=0x7ffee48c1230 <DeviceInfo>) at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/plugins/amdgpu/src/rtl.cpp:359
#9  0x00007ffee43401e9 in RTLDeviceInfoTy::RTLDeviceInfoTy (this=0x7ffee48c1230 <DeviceInfo>) at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/plugins/amdgpu/src/rtl.cpp:722
#10 0x00007ffee4340100 in __cxx_global_var_init.4(void) () at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/plugins/amdgpu/src/rtl.cpp:875
#11 0x00007ffee4340133 in _GLOBAL__sub_I_rtl.cpp () at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/plugins/amdgpu/src/trace.h:114
#12 0x00007ffff7fe0c4a in call_init (l=<optimized out>, argc=argc@entry=1, argv=argv@entry=0x7fffffffc538, env=env@entry=0x7fffffffc548) at dl-init.c:72
#13 0x00007ffff7fe0d51 in call_init (env=0x7fffffffc548, argv=0x7fffffffc538, argc=1, l=<optimized out>) at dl-init.c:30
#14 _dl_init (main_map=0x334680, argc=1, argv=0x7fffffffc538, env=0x7fffffffc548) at dl-init.c:119
#15 0x00007ffff6ba2915 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:182
#16 0x00007ffff7fe520f in dl_open_worker (a=a@entry=0x7fffffffbdb0) at dl-open.c:758
#17 0x00007ffff6ba28b8 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:208
#18 0x00007ffff7fe474a in _dl_open (file=0x30c610 "/home/yeluo/rocm/aomp/lib-debug/libomptarget.rtl.amdgpu.so", mode=-2147483646, caller_dlopen=<optimized out>, nsid=-2, argc=1, argv=0x7fffffffc538, 
    env=0x7fffffffc548) at dl-open.c:837
#19 0x00007ffff714334c in dlopen_doit (a=a@entry=0x7fffffffbfd0) at dlopen.c:66
#20 0x00007ffff6ba28b8 in __GI__dl_catch_exception (exception=exception@entry=0x7fffffffbf70, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:208
#21 0x00007ffff6ba2983 in __GI__dl_catch_error (objname=0x2faa40, errstring=0x2faa48, mallocedp=0x2faa38, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:227
#22 0x00007ffff7143b59 in _dlerror_run (operate=operate@entry=0x7ffff71432f0 <dlopen_doit>, args=args@entry=0x7fffffffbfd0) at dlerror.c:170
#23 0x00007ffff71433da in __dlopen (file=<optimized out>, mode=<optimized out>) at dlopen.c:87
#24 0x00007ffff6ceaa11 in RTLsTy::LoadRTLs (this=0x2f9880) at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/src/rtl.cpp:151
#25 0x00007ffff6ce8e7e in std::__invoke_impl<void, void (RTLsTy::*)(), RTLsTy*> (__f=@0x7fffffffc3d0: (void (RTLsTy::*)(struct RTLsTy * const)) 0x7ffff6cea540 <RTLsTy::LoadRTLs()>, 
    __t=@0x7fffffffc3c8: 0x2f9880) at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/invoke.h:73
#26 0x00007ffff6ce8de2 in std::__invoke<void (RTLsTy::*)(), RTLsTy*> (__fn=@0x7fffffffc3d0: (void (RTLsTy::*)(struct RTLsTy * const)) 0x7ffff6cea540 <RTLsTy::LoadRTLs()>, __args=@0x7fffffffc3c8: 0x2f9880)
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/invoke.h:95
#27 0x00007ffff6ce8d9c in std::call_once<void (RTLsTy::*)(), RTLsTy*>(std::once_flag&, void (RTLsTy::*&&)(), RTLsTy*&&)::{lambda()#1}::operator()() const (this=0x7fffffffc368)
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:671
#28 0x00007ffff6ce8d54 in std::call_once<void (RTLsTy::*)(), RTLsTy*>(std::once_flag&, void (RTLsTy::*&&)(), RTLsTy*&&)::{lambda()#2}::operator()() const (this=0x7ffff713b758)
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:676
#29 0x00007ffff6ce8d29 in std::call_once<void (RTLsTy::*)(), RTLsTy*>(std::once_flag&, void (RTLsTy::*&&)(), RTLsTy*&&)::{lambda()#2}::__invoke() ()
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:676
#30 0x00007ffff6c434df in __pthread_once_slow (once_control=0x2f98bc, init_routine=0x7ffff7035c20 <__once_proxy>) at pthread_once.c:116
#31 0x00007ffff6ce881b in __gthread_once (__once=0x2f98bc, __func=0x7ffff7035c20 <__once_proxy>) at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9/bits/gthr-default.h:700
#32 0x00007ffff6ce895c in std::call_once<void (RTLsTy::*)(), RTLsTy*> (__once=..., __f=@0x7fffffffc3d0: (void (RTLsTy::*)(struct RTLsTy * const)) 0x7ffff6cea540 <RTLsTy::LoadRTLs()>, 
    __args=@0x7fffffffc3c8: 0x2f9880) at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:683
#33 0x00007ffff6ce48d9 in __tgt_register_lib (desc=0x245230 <omp_offloading.descriptor>) at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/src/interface.cpp:36
#34 0x00000000002b33bd in __libc_csu_init ()
#35 0x00007ffff6a66040 in __libc_start_main (main=0x257020 <main>, argc=1, argv=0x7fffffffc538, init=0x2b3370 <__libc_csu_init>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffc528)
    at ../csu/libc-start.c:264
#36 0x000000000025655e in _start ()
```
with `--stats` or nothing
```
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff6a64859 in __GI_abort () at abort.c:79
#2  0x00007ffee3446474 in ?? () from /opt/rocm-4.5.0/rocprofiler/lib/librocprofiler64.so
#3  0x00007ffee34240e0 in ?? () from /opt/rocm-4.5.0/rocprofiler/lib/librocprofiler64.so
#4  0x00007ffee3428e95 in ?? () from /opt/rocm-4.5.0/rocprofiler/lib/librocprofiler64.so
#5  0x00007ffee343d687 in ?? () from /opt/rocm-4.5.0/rocprofiler/lib/librocprofiler64.so
#6  0x00007ffee34433ed in ?? () from /opt/rocm-4.5.0/rocprofiler/lib/librocprofiler64.so
#7  0x00007ffee4340c1b in RTLDeviceInfoTy::RTLDeviceInfoTy (this=0x7ffee48c1230 <DeviceInfo>) at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/plugins/amdgpu/src/rtl.cpp:815
#8  0x00007ffee4340100 in __cxx_global_var_init.4(void) () at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/plugins/amdgpu/src/rtl.cpp:875
#9  0x00007ffee4340133 in _GLOBAL__sub_I_rtl.cpp () at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/plugins/amdgpu/src/trace.h:114
#10 0x00007ffff7fe0c4a in call_init (l=<optimized out>, argc=argc@entry=1, argv=argv@entry=0x7fffffffc588, env=env@entry=0x7fffffffc598) at dl-init.c:72
#11 0x00007ffff7fe0d51 in call_init (env=0x7fffffffc598, argv=0x7fffffffc588, argc=1, l=<optimized out>) at dl-init.c:30
#12 _dl_init (main_map=0x334670, argc=1, argv=0x7fffffffc588, env=0x7fffffffc598) at dl-init.c:119
#13 0x00007ffff6ba2915 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:182
#14 0x00007ffff7fe520f in dl_open_worker (a=a@entry=0x7fffffffbe00) at dl-open.c:758
#15 0x00007ffff6ba28b8 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:208
#16 0x00007ffff7fe474a in _dl_open (file=0x30c620 "/home/yeluo/rocm/aomp/lib-debug/libomptarget.rtl.amdgpu.so", mode=-2147483646, caller_dlopen=<optimized out>, nsid=-2, argc=1, argv=0x7fffffffc588, 
    env=0x7fffffffc598) at dl-open.c:837
#17 0x00007ffff714334c in dlopen_doit (a=a@entry=0x7fffffffc020) at dlopen.c:66
#18 0x00007ffff6ba28b8 in __GI__dl_catch_exception (exception=exception@entry=0x7fffffffbfc0, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:208
#19 0x00007ffff6ba2983 in __GI__dl_catch_error (objname=0x2faa40, errstring=0x2faa48, mallocedp=0x2faa38, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:227
#20 0x00007ffff7143b59 in _dlerror_run (operate=operate@entry=0x7ffff71432f0 <dlopen_doit>, args=args@entry=0x7fffffffc020) at dlerror.c:170
#21 0x00007ffff71433da in __dlopen (file=<optimized out>, mode=<optimized out>) at dlopen.c:87
#22 0x00007ffff6ceaa11 in RTLsTy::LoadRTLs (this=0x2f9880) at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/src/rtl.cpp:151
#23 0x00007ffff6ce8e7e in std::__invoke_impl<void, void (RTLsTy::*)(), RTLsTy*> (__f=@0x7fffffffc420: (void (RTLsTy::*)(struct RTLsTy * const)) 0x7ffff6cea540 <RTLsTy::LoadRTLs()>, 
    __t=@0x7fffffffc418: 0x2f9880) at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/invoke.h:73
#24 0x00007ffff6ce8de2 in std::__invoke<void (RTLsTy::*)(), RTLsTy*> (__fn=@0x7fffffffc420: (void (RTLsTy::*)(struct RTLsTy * const)) 0x7ffff6cea540 <RTLsTy::LoadRTLs()>, __args=@0x7fffffffc418: 0x2f9880)
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/invoke.h:95
#25 0x00007ffff6ce8d9c in std::call_once<void (RTLsTy::*)(), RTLsTy*>(std::once_flag&, void (RTLsTy::*&&)(), RTLsTy*&&)::{lambda()#1}::operator()() const (this=0x7fffffffc3b8)
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:671
#26 0x00007ffff6ce8d54 in std::call_once<void (RTLsTy::*)(), RTLsTy*>(std::once_flag&, void (RTLsTy::*&&)(), RTLsTy*&&)::{lambda()#2}::operator()() const (this=0x7ffff713b758)
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:676
#27 0x00007ffff6ce8d29 in std::call_once<void (RTLsTy::*)(), RTLsTy*>(std::once_flag&, void (RTLsTy::*&&)(), RTLsTy*&&)::{lambda()#2}::__invoke() ()
    at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:676
#28 0x00007ffff6c434df in __pthread_once_slow (once_control=0x2f98bc, init_routine=0x7ffff7035c20 <__once_proxy>) at pthread_once.c:116
#29 0x00007ffff6ce881b in __gthread_once (__once=0x2f98bc, __func=0x7ffff7035c20 <__once_proxy>) at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9/bits/gthr-default.h:700
#30 0x00007ffff6ce895c in std::call_once<void (RTLsTy::*)(), RTLsTy*> (__once=..., __f=@0x7fffffffc420: (void (RTLsTy::*)(struct RTLsTy * const)) 0x7ffff6cea540 <RTLsTy::LoadRTLs()>, 
    __args=@0x7fffffffc418: 0x2f9880) at /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/mutex:683
#31 0x00007ffff6ce48d9 in __tgt_register_lib (desc=0x245230 <omp_offloading.descriptor>) at /home/yeluo/git/aomp14.0/llvm-project/openmp/libomptarget/src/interface.cpp:36
#32 0x00000000002b33bd in __libc_csu_init ()
#33 0x00007ffff6a66040 in __libc_start_main (main=0x257020 <main>, argc=1, argv=0x7fffffffc588, init=0x2b3370 <__libc_csu_init>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffc578)
    at ../csu/libc-start.c:264
#34 0x000000000025655e in _start ()
```

---

### 评论 #11 — dhruvachak (2021-11-05T01:22:45Z)

@ye-luo An issue was just fixed. 
https://github.com/RadeonOpenCompute/llvm-project/commit/c974d826ca4596739c47b8d2a1520c35affc5ead

Can you please update llvm-project in AOMP14 so that you have the above commit and then rebuild and try again? Also, please use rocprof built by AOMP14, not the one from ROCm4.5. 

---

### 评论 #12 — ye-luo (2021-11-05T02:54:11Z)

fresh built compiler and rocprof still don't work
```
yeluo@epyc-server:~/git/aomp14.0$ aomp/bin/clone_aomp.sh list
MANIFEST FILE: /home/yeluo/git/aomp14.0/aomp/bin/../manifests/aomp_14.0.xml
  repo src       branch                 path                 repo name    last hash    updated           commitor         for author
  --------       ------                 ----                 ---------    ---------    -------           --------         ----------
       roc amd-stg-open         llvm-project              llvm-project c974d826ca45 2021-11-04      Ron Lieberman       Greg Rodgers         
       roc amd-stg-open rocm-compilersupport      ROCm-CompilerSupport ef72f4edb3dd 2021-10-12      Jeremy Newton      Jeremy Newton         
       roc amd-stg-open     rocm-device-libs          ROCm-Device-Libs 2011841dfe9e 2021-11-03      Ron Lieberman        gregrodgers         
  roctools     aomp-dev                flang                     flang 4f1282c59a76 2021-09-22             GitHub            ronlieb         
  roctools     aomp-dev          aomp-extras               aomp-extras aefc0d6c7434 2021-10-18      Ron Lieberman      Ron Lieberman         
  roctools     aomp-dev                 aomp                      aomp f4c110ac8ad4 2021-11-04 Dhruva Chakrabarti Dhruva Chakrabarti         
  roctools   rocm-4.5.x          rocprofiler               rocprofiler e140f47f3609 2021-10-08 Gerrit Code Review      Zhongyu Zhang         
  roctools   rocm-4.5.x            roctracer                 roctracer d8ecefda4efd 2021-10-09      Ammar Elwazir      Ammar ELWazir         
  roctools   rocm-4.5.x            ROCdbgapi                 ROCdbgapi 1040f1521831 2021-09-26 Laurent Morichetti Laurent Morichetti         
  roctools   rocm-4.5.x               ROCgdb                    ROCgdb a1f2a479f060 2021-09-24 Laurent Morichetti       Simon Marchi         
  roctools   rocm-4.5.x               hipamd                    hipamd bedc5f614221 2021-10-04  Pruthvi Madugundu            Sourabh         
  roctools   rocm-4.5.x                  hip                       hip 3413a164f458 2021-10-11      Maneesh Gupta      Maneesh Gupta         
  roctools   rocm-4.5.x               ROCclr                    ROCclr aba55f5c2775 2021-10-07      Zhongyu Zhang   German Andryeyev         
       roc   rocm-4.5.x  ROCm-OpenCL-Runtime       ROCm-OpenCL-Runtime bf77cab71234 2021-09-27        Freddy Paul        Freddy Paul         
       roc    roc-4.5.x             rocminfo                  rocminfo 1452f8fa24b2 2021-07-19      Icarus Sparry      Icarus Sparry         
       roc rocm-rel-4.5           rocm-cmake                rocm-cmake 8d82398d269d 2021-09-14            Jenkins            Jenkins         
       roc   rocm-4.5.x         rocr-runtime              ROCR-Runtime f32dfa887d02 2021-10-27         Sean Keely         Sean Keely         
       roc    roc-4.5.x roct-thunk-interface      ROCT-Thunk-Interface 5b152ed0f043 2021-09-30         Sean Keely         Sean Keely         
```

---

### 评论 #13 — dhruvachak (2021-11-05T03:52:00Z)

@ye-luo Thanks for checking. Is there a way we can get a reproducer?

---

### 评论 #14 — ye-luo (2021-11-05T03:56:51Z)

@dhruvachak Search above "Reproducer uses AOMP clang++" ;)
You will need a LAPACK library but any LAPACK will work and it is not called by the check_spo_batched executable.
Thank you for trying it out on your side.

---

### 评论 #15 — dhruvachak (2021-11-05T18:29:11Z)

@ye-luo Thanks, I did not see the reproducer earlier. 

After installing LAPACK, I was able to build/run miniqmc successfully using AOMP14. For me, rocprof --stats and --hsa-trace both work as well on both check_spo and check_spo_batched. Don't know why it is not working for you. I have an older ROCm but that should not matter. 

Can you please verify whether "rocprof --hsa-trace" works for you on a smoke test? Try 
$ cd $AOMP_REPOS/aomp/test/smoke/vmulsum
$ make run
$ rocprof --hsa-trace ./vmulsum

If that does not work, I suggest removing $AOMP_REPOS/build, the install directory pointed to by $AOMP, and then rebuild all of AOMP by using build_aomp.sh and try again. 

Also, please ensure you are picking up the compiler and rocprof from AOMP14 and not from ROCm. 

Thanks.


---

### 评论 #16 — ye-luo (2021-11-05T23:28:32Z)

Unfortunately. I had no progress. I tried removing the whole /opt/rocm (not the dkms), remove build, remove installation. I still got the above error. My OS is ubuntu 20.04. Since you succeeded to run, could you post the `--stats` csv output, so we can verify that GPU offload is happening as intended.

---

### 评论 #17 — dhruvachak (2021-11-05T23:41:39Z)

I am attaching the --stats output of check_spo_batched.
[spo_batched.csv](https://github.com/RadeonOpenCompute/ROCm/files/7489329/spo_batched.csv)


---

### 评论 #18 — dhruvachak (2021-11-05T23:43:39Z)

@ye-luo No need to remove the ROCm installation. You should be able to use the AOMP14 build/install. 

My OS is Ubuntu 20.04 as well. Can you please post how you are building AOMP14?

---

### 评论 #19 — ye-luo (2021-11-05T23:44:17Z)

> I am attaching the --stats output of check_spo_batched. [spo_batched.csv](https://github.com/RadeonOpenCompute/ROCm/files/7489329/spo_batched.csv)

This all look good.

---

### 评论 #20 — ye-luo (2021-11-05T23:48:07Z)

I just follow. https://github.com/ROCm-Developer-Tools/aomp/blob/aomp-dev/docs/SOURCEINSTALL.md#clone-and-build-aomp no modification. My run will fail at rocgdb due to missing dependencies. Then I just run
```
./aomp/bin/build_aomp.sh continue roctracer
```
roctracer is the package after rocgdb
```
COMPONENTS:rocm-cmake roct rocr project libdevice openmp extras comgr rocminfo pgmath flang flang_runtime hipamd  rocdbgapi rocgdb roctracer rocprofiler
```

---

### 评论 #21 — ronlieb (2021-11-05T23:52:09Z)

[AMD Official Use Only]

Is your gdb build failing on GMP ?

If so,  I noticed a new dependency recently came in on gdb build
sudo apt-get install libgmp-dev

From: Ye Luo ***@***.***>
Sent: Friday, November 5, 2021 7:48 PM
To: RadeonOpenCompute/ROCm ***@***.***>
Cc: Lieberman, Ron ***@***.***>; Comment ***@***.***>
Subject: Re: [RadeonOpenCompute/ROCm] rocprof makes application runs failed bug series 2 (#1328)

[CAUTION: External Email]

I just follow. https://github.com/ROCm-Developer-Tools/aomp/blob/aomp-dev/docs/SOURCEINSTALL.md#clone-and-build-aomp<https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2FROCm-Developer-Tools%2Faomp%2Fblob%2Faomp-dev%2Fdocs%2FSOURCEINSTALL.md%23clone-and-build-aomp&data=04%7C01%7Cron.lieberman%40amd.com%7C924d70f8891d460d363008d9a0b6be04%7C3dd8961fe4884e608e11a82d994e183d%7C0%7C0%7C637717529017396487%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=HWDkwUAw3lIhPmULo%2Bb5kPmNx2Y0IEpg9DnFxqU%2FdIs%3D&reserved=0> no modification. My run will fail at rocgdb due to missing dependencies. Then I just run

./aomp/bin/build_aomp.sh continue roctracer

roctracer is the package after rocgdb

-
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2FRadeonOpenCompute%2FROCm%2Fissues%2F1328%23issuecomment-962282515&data=04%7C01%7Cron.lieberman%40amd.com%7C924d70f8891d460d363008d9a0b6be04%7C3dd8961fe4884e608e11a82d994e183d%7C0%7C0%7C637717529017406483%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=v%2FYln17L9NTB8XqifgcSt2AYObuBjcoSS26fT0hhVA0%3D&reserved=0>, or unsubscribe<https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fnotifications%2Funsubscribe-auth%2FAD3EYZYPTW2BNPT2R3UAIQDUKR3NDANCNFSM4UWE7JOQ&data=04%7C01%7Cron.lieberman%40amd.com%7C924d70f8891d460d363008d9a0b6be04%7C3dd8961fe4884e608e11a82d994e183d%7C0%7C0%7C637717529017406483%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=3nuxfkGgoEIBbrqnhar25L2P1qG2Cmm0khm%2BANjpl%2Fs%3D&reserved=0>.
Triage notifications on the go with GitHub Mobile for iOS<https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fapps.apple.com%2Fapp%2Fapple-store%2Fid1477376905%3Fct%3Dnotification-email%26mt%3D8%26pt%3D524675&data=04%7C01%7Cron.lieberman%40amd.com%7C924d70f8891d460d363008d9a0b6be04%7C3dd8961fe4884e608e11a82d994e183d%7C0%7C0%7C637717529017416478%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=0dWrfmEggJV%2FXo2kYArJ2XOkN7U7qb4a0Vvbpi%2BGqOM%3D&reserved=0> or Android<https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.github.android%26referrer%3Dutm_campaign%253Dnotification-email%2526utm_medium%253Demail%2526utm_source%253Dgithub&data=04%7C01%7Cron.lieberman%40amd.com%7C924d70f8891d460d363008d9a0b6be04%7C3dd8961fe4884e608e11a82d994e183d%7C0%7C0%7C637717529017416478%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=ghFS05Ikg8SPUDehSuFXsRmZLD3ynmG0Fmr8zmfmswU%3D&reserved=0>.


---

### 评论 #22 — dhruvachak (2021-11-05T23:52:59Z)

Yes, that sounds right, same as what I did. After updating your llvm-project repo yesterday, did you remove the build directory from $AOMP_REPOS and the install directory $AOMP and re-build using build_aomp.sh?

This cleanup step is usually not required unless something unexpected is happening. 

---

### 评论 #23 — ye-luo (2021-11-06T00:07:41Z)

@ronlieb I have libgmp-dev installed. So it is something else causing rocgdb build issue unfortunately.
@dhruvachak I tried removing the whole build folder, "~/rocm" installation folder. I even tried deleting the git/aomp14.0 source repo folder to start fresh. They still didn't work. So to prevent being affected by `/opt/rocm`, I also make sure it is removed. Still doesn't help. It will be nice if you try a node other than your workstation. Maybe try the nightly build from your test farm?

---

### 评论 #24 — dhruvachak (2021-11-06T00:19:45Z)

@ye-luo Ok, will try and let you know.

---

### 评论 #25 — dhruvachak (2021-11-06T02:05:31Z)

@ye-luo I tried a different machine with Ubuntu 20.04 and ROCm 4.5 installed. I freshly cloned/built AOMP14.0 and cloned/built miniqmc. I can run "rocprof --stats/--hsa-trace" on both check_spo and check_spo_batched without any problems. The CSV and JSON files look good.

Is it possible for you to try a different machine?

---

### 评论 #26 — dhruvachak (2021-11-06T02:09:22Z)

@ye-luo Does rocprof work for you on a smoke test like I suggested earlier?

---

### 评论 #27 — ye-luo (2021-11-06T03:16:03Z)

> @ye-luo Does rocprof work for you on a smoke test like I suggested earlier?

I did try since vmulsum is even simpler to reproduce. Same failure unfortunately.

---

### 评论 #28 — ye-luo (2021-11-06T03:17:51Z)

> @ye-luo I tried a different machine with Ubuntu 20.04 and ROCm 4.5 installed. I freshly cloned/built AOMP14.0 and cloned/built miniqmc. I can run "rocprof --stats/--hsa-trace" on both check_spo and check_spo_batched without any problems. The CSV and JSON files look good.
> 
> Is it possible for you to try a different machine?

Thank you so much. I will try on another machine as soon as I can.

---

### 评论 #29 — ye-luo (2021-11-06T14:57:44Z)

I still got the same failure on another machine as above.

---

### 评论 #30 — dhruvachak (2021-11-07T04:28:40Z)

@ye-luo Can you please share the stack traces again? Your previous ones had rocm4.5 in them. 

---

### 评论 #31 — ye-luo (2021-11-08T02:58:27Z)

```
$ rocprof gdb ./vmulsum

(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7b5f859 in __GI_abort () at abort.c:79
#2  0x00007fffe4559a27 in ?? () from /home/yeluo/rocm/aomp_14.0-0/rocprofiler/lib/librocprofiler64.so
#3  0x00007fffe452da97 in ?? () from /home/yeluo/rocm/aomp_14.0-0/rocprofiler/lib/librocprofiler64.so
#4  0x00007fffe45454a8 in ?? () from /home/yeluo/rocm/aomp_14.0-0/rocprofiler/lib/librocprofiler64.so
#5  0x00007fffe4556bf1 in ?? () from /home/yeluo/rocm/aomp_14.0-0/rocprofiler/lib/librocprofiler64.so
#6  0x00007fffe51e6d3d in RTLDeviceInfoTy::RTLDeviceInfoTy() () from /home/yeluo/rocm/aomp/lib/libomptarget.rtl.amdgpu.so
#7  0x00007fffe51eca16 in _GLOBAL__sub_I_rtl.cpp () from /home/yeluo/rocm/aomp/lib/libomptarget.rtl.amdgpu.so
#8  0x00007ffff7fe0c4a in call_init (l=<optimized out>, argc=argc@entry=1, argv=argv@entry=0x7fffffffc588, 
    env=env@entry=0x7fffffffc598) at dl-init.c:72
#9  0x00007ffff7fe0d51 in call_init (env=0x7fffffffc598, argv=0x7fffffffc588, argc=1, l=<optimized out>) at dl-init.c:30
#10 _dl_init (main_map=0x280b80, argc=1, argv=0x7fffffffc588, env=0x7fffffffc598) at dl-init.c:119
#11 0x00007ffff7c9d915 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>)
    at dl-error-skeleton.c:182
#12 0x00007ffff7fe520f in dl_open_worker (a=a@entry=0x7fffffffc000) at dl-open.c:758
#13 0x00007ffff7c9d8b8 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>)
    at dl-error-skeleton.c:208
#14 0x00007ffff7fe474a in _dl_open (file=0x24dd20 "/home/yeluo/rocm/aomp/lib/libomptarget.rtl.amdgpu.so", mode=-2147483646, 
    caller_dlopen=<optimized out>, nsid=-2, argc=1, argv=0x7fffffffc588, env=0x7fffffffc598) at dl-open.c:837
#15 0x00007ffff7b2834c in dlopen_doit (a=a@entry=0x7fffffffc220) at dlopen.c:66
#16 0x00007ffff7c9d8b8 in __GI__dl_catch_exception (exception=exception@entry=0x7fffffffc1c0, operate=<optimized out>, 
    args=<optimized out>) at dl-error-skeleton.c:208
#17 0x00007ffff7c9d983 in __GI__dl_catch_error (objname=0x24dd00, errstring=0x24dd08, mallocedp=0x24dcf8, operate=<optimized out>, 
    args=<optimized out>) at dl-error-skeleton.c:227
#18 0x00007ffff7b28b59 in _dlerror_run (operate=operate@entry=0x7ffff7b282f0 <dlopen_doit>, args=args@entry=0x7fffffffc220)
    at dlerror.c:170
#19 0x00007ffff7b283da in __dlopen (file=<optimized out>, mode=<optimized out>) at dlopen.c:87
#20 0x00007ffff7ddaef8 in RTLsTy::LoadRTLs() () from /home/yeluo/rocm/aomp/lib/libomptarget.so
#21 0x00007ffff7d3e4df in __pthread_once_slow (once_control=0x24db8c, init_routine=0x7fffee93cc20 <__once_proxy>)
    at pthread_once.c:116
#22 0x00007ffff7dd556d in __tgt_register_lib () from /home/yeluo/rocm/aomp/lib/libomptarget.so
#23 0x000000000020b38d in __libc_csu_init ()
#24 0x00007ffff7b61040 in __libc_start_main (main=0x20aac0 <main>, argc=1, argv=0x7fffffffc588, init=0x20b340 <__libc_csu_init>, 
    fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffc578) at ../csu/libc-start.c:264
#25 0x000000000020a9fe in _start ()


---

### 评论 #32 — dhruvachak (2021-11-09T00:55:20Z)

@ye-luo Update: Though I am still not able to reproduce the failure, some of my colleagues are. While we are still investigating the root cause, we found that setting LD_LIBRARY_PATH to the ROCm4.5 lib works. 

Can you check with this workaround?
% LD_LIBRARY_PATH=/opt/rocm-4.5.0/lib rocprof --stats ./vmulsum

Please make sure the application is built with AOMP14. The rocprof script can be either from the ROCm installation or from AOMP14. 

Thanks.

---

### 评论 #33 — ye-luo (2021-11-09T01:50:48Z)

I finally got it working. The last missing piece is libhsa-amd-aqlprofile64.so which is from hsa-amd-aqlprofile package I didn't install.
With AOMP14 and hsa-amd-aqlprofile, profiling works for me now!!!

Here is my thoughts.
1. AOMP probably needs to include hsa-amd-aqlprofile to make it self-contained.
2. librocprofiler64.so is missing error handling when libhsa-amd-aqlprofile64.so is not found
3. ROCm release needs to add hsa-amd-aqlprofile as a dependency of rocprof

---

### 评论 #34 — ye-luo (2021-11-09T01:55:50Z)

Indeed found another user bug report https://github.com/ROCm-Developer-Tools/rocprofiler/issues/49
```
$ LD_DEBUG=libs rocprof --hsa-trace vmulsum 2&>1 > log.txt
```
directly indicates missing libhsa-amd-aqlprofile64.so

---

### 评论 #35 — ye-luo (2021-11-09T02:26:12Z)

@dhruvachak Is your fix to the OpenMP offload plugin also needed in LLVM upstream? If yes, could you submit a patch?

---

### 评论 #36 — dhruvachak (2021-11-09T03:44:25Z)

> I finally got it working. The last missing piece is libhsa-amd-aqlprofile64.so which is from hsa-amd-aqlprofile package I didn't install. With AOMP14 and hsa-amd-aqlprofile, profiling works for me now!!!
> 
> Here is my thoughts.
> 
> 1. AOMP probably needs to include hsa-amd-aqlprofile to make it self-contained.
> 2. librocprofiler64.so is missing error handling when libhsa-amd-aqlprofile64.so is not found
> 3. ROCm release needs to add hsa-amd-aqlprofile as a dependency of rocprof

Thanks for the update.

---

### 评论 #37 — dhruvachak (2021-11-09T03:45:38Z)

> @dhruvachak Is your fix to the OpenMP offload plugin also needed in LLVM upstream? If yes, could you submit a patch?

@ye-luo Are you referring to 
[libomptarget] [amdgpu] After a kernel dispatch packet is published, its contents must not be accessed.

The above fix has been pushed to trunk already.

---

### 评论 #38 — ye-luo (2021-11-09T04:54:57Z)

@dhruvachak I was thinking of https://github.com/RadeonOpenCompute/llvm-project/commit/c974d826ca4596739c47b8d2a1520c35affc5ead but it seems is not the part of upstream. So never mind.

---

### 评论 #39 — ROCmSupport (2021-11-10T10:21:08Z)

Hi @ye-luo and all,
Looks like I have seen some positive updates in the latest/recent comments. Can we close this issue now?
Please share your thoughts. Thank you.

---

### 评论 #40 — ye-luo (2021-11-10T14:14:18Z)

I make the following request earlier 
>     1. AOMP probably needs to include hsa-amd-aqlprofile to make it self-contained.
I just realize that hsa-amd-aqlprofile seems closed-source. So it may not be easily incorporated in AOMP. So I will leave AOMP team to sort out a reasonable solution.

>     2. librocprofiler64.so is missing error handling when libhsa-amd-aqlprofile64.so is not found
This bug needs a fix in high priority. Users constantly hit this issue as reported in several repos (rocporf/AOMP/ROCm). So needs actions from rocprof developers.

>     3. ROCm release needs to add hsa-amd-aqlprofile as a dependency of rocprof
This also needs to be addressed by the packaging team. rocprofiler-dev and rocprofiler-dev4.5.0 need the additional dependency to hsa-amd-aqlprofile and hsa-amd-aqlprofile4.5.0

@ROCmSupport could you confirm with rocprof team and the packaging team that they are aware of point 2 and 3 and they will be taken care of in the upcoming releases? I guess 3 should be no challenge for ROCm 5.0 but rocprof change maybe depends on the 5.0 release cycle but preferably ASAP. 

About closing this issue, I would prefer leaving this issue open till point 2 and 3 being fixed by one ROCm release. Otherwise, it gives false feeling that the issue has been addressed as a "closed" status indicates.

---

### 评论 #41 — ROCmSupport (2021-11-15T08:54:38Z)

Thanks @ye-luo 
Good news, fix will be part of 4.5.x. Stay tuned.
Thank you.

---

### 评论 #42 — ye-luo (2021-12-15T00:57:15Z)

Fixed by 4.5.2 release.

---

### 评论 #43 — ROCmSupport (2021-12-15T05:57:04Z)

Thanks @ye-luo for the closure.
Feel free to file a new issues, if any, for quick resolutions. Thank you.

---
