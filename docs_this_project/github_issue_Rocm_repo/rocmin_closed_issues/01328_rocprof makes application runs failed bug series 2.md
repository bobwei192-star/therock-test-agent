# rocprof makes application runs failed bug series 2

- **Issue #:** 1328
- **State:** closed
- **Created:** 2020-12-11T06:57:50Z
- **Updated:** 2021-12-15T06:01:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1328

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
