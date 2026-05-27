# atomicMax(double) crashes

> **Issue #1441**
> **状态**: closed
> **创建时间**: 2021-04-06T02:57:15Z
> **更新时间**: 2021-04-07T12:13:45Z
> **关闭时间**: 2021-04-07T08:30:31Z
> **作者**: windstamp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1441

## 描述

Due to there is no atomicMax(double *address, const double val) api in hip, so implements it based on atomicCAS as follow:

```
__device__ __forceinline__ double AtomicDouble(double *address, const double val)
  if (*address >= val) {
    return *address;
  }

  unsigned long long int *const address_as_ull =            // NOLINT
      reinterpret_cast<unsigned long long int *>(address);  // NOLINT
  unsigned long long int old = *address_as_ull, assumed;    // NOLINT

  do {
    assumed = old;
    if (__longlong_as_double(assumed) >= val) {
      break;
    }

    old = atomicCAS(address_as_ull, assumed, __double_as_longlong(val));
  } while (assumed != old);
}
```

But it will crashes as follow:
```
:0:rocdevice.cpp            :2303: 609892899575 us: Device::callbackQueue aborting with status: 0x1016
```

It seems the AtomicDouble() is no problem, but after it will crashes.


The source code is https://github.com/PaddlePaddle/Paddle/pull/32049,

and
```
$ cd Paddle/build
$ ctest -R test_segment_ops -V
```



---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-04-06T07:07:54Z)

Thanks @windstamp for reaching out.
Request you to share the GPU name, OS, kernel version, ROCm version, outputs of /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo.
Thank you.

---

### 评论 #2 — windstamp (2021-04-07T08:30:24Z)

Add `return` does solve this problem.
```
__device__ __forceinline__ double AtomicDouble(double *address, const double val)
  if (*address >= val) {
    return *address;
  }

  unsigned long long int *const address_as_ull =            // NOLINT
      reinterpret_cast<unsigned long long int *>(address);  // NOLINT
  unsigned long long int old = *address_as_ull, assumed;    // NOLINT

  do {
    assumed = old;
    if (__longlong_as_double(assumed) >= val) {
      break;
    }

    old = atomicCAS(address_as_ull, assumed, __double_as_longlong(val));
  } while (assumed != old);

  return __longlong_as_double(old);
}
```

If no `return`，the function `AtomicDouble()` itself is no problem, but it will hang others hip runtime api, for example, `hipFree()`, the stack sush as:
```
d 0x7f029eedc700 (LWP 5949)):
#0  0x00007f02e4e92a35 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x00007f0290dde4cb in __gthread_cond_wait (__mutex=<optimized out>, __cond=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/build/build-cc-gcc-final/x86_64-conda_cos6-linux-gnu/libstdc++-v3/include/x86_64-conda_cos6-linux-gnu/bits/gthr-default.h:878
#2  std::condition_variable::wait (this=<optimized out>, __lock=...) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libstdc++-v3/src/c++11/condition_variable.cc:53
#3  0x00007f0281cdf925 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<ThreadPool::ThreadPool(unsigned long)::{lambda()#1}> > >::_M_run() () from /public/home/windstamp/working/github/windstamp/Paddle6/build_37_develop/python/paddle/fluid/core_avx.so
#4  0x00007f028758a17f in execute_native_thread_routine () from /public/home/windstamp/working/github/windstamp/Paddle6/build_37_develop/python/paddle/fluid/core_avx.so
#5  0x00007f02e4e8eea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f02e4bb79fd in clone () from /lib64/libc.so.6
Thread 5 (Thread 0x7f02bc7f7700 (LWP 5948)):
#0  0x00007f02e4bae397 in ioctl () from /lib64/libc.so.6
#1  0x00007f02d7f50078 in kmtIoctl () from /opt/rocm/lib/../lib64/libhsakmt.so.1
#2  0x00007f02d7f4a6fe in hsaKmtWaitOnMultipleEvents () from /opt/rocm/lib/../lib64/libhsakmt.so.1
#3  0x00007f02d7f4ad49 in hsaKmtWaitOnEvent () from /opt/rocm/lib/../lib64/libhsakmt.so.1
#4  0x00007f02d8b31462 in rocr::core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/lib/libhsa-runtime64.so.1
#5  0x00007f02d8b312ba in rocr::core::InterruptSignal::WaitAcquire(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/lib/libhsa-runtime64.so.1
#6  0x00007f02d8b23a99 in rocr::HSA::hsa_signal_wait_scacquire(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/lib/libhsa-runtime64.so.1
#7  0x00007f02dff34d2c in ?? () from /opt/rocm/lib/libamdhip64.so.4
#8  0x00007f02dff3679f in ?? () from /opt/rocm/lib/libamdhip64.so.4
#9  0x00007f02dff0e51a in ?? () from /opt/rocm/lib/libamdhip64.so.4
#10 0x00007f02dff0f2ed in ?? () from /opt/rocm/lib/libamdhip64.so.4
#11 0x00007f02dfdc9e96 in ?? () from /opt/rocm/lib/libamdhip64.so.4
#12 0x00007f02dff10cbf in ?? () from /opt/rocm/lib/libamdhip64.so.4
#13 0x00007f02e4e8eea5 in start_thread () from /lib64/libpthread.so.0
#14 0x00007f02e4bb79fd in clone () from /lib64/libc.so.6
Thread 4 (Thread 0x7f02bf7c6700 (LWP 5945)):
#0  0x00007f02e4b9c807 in sched_yield () from /lib64/libc.so.6
#1  0x00007f02dff01605 in ?? () from /opt/rocm/lib/libamdhip64.so.4
#2  0x00007f02dff0e448 in ?? () from /opt/rocm/lib/libamdhip64.so.4
#3  0x00007f02dff0f2ed in ?? () from /opt/rocm/lib/libamdhip64.so.4
#4  0x00007f02dfdc9e96 in ?? () from /opt/rocm/lib/libamdhip64.so.4
#5  0x00007f02dff10cbf in ?? () from /opt/rocm/lib/libamdhip64.so.4
#6  0x00007f02e4e8eea5 in start_thread () from /lib64/libpthread.so.0
#7  0x00007f02e4bb79fd in clone () from /lib64/libc.so.6
Thread 3 (Thread 0x7f029c6db700 (LWP 5915)):
#0  0x00007f02e4bae397 in ioctl () from /lib64/libc.so.6
#1  0x00007f02d7f50078 in kmtIoctl () from /opt/rocm/lib/../lib64/libhsakmt.so.1
#2  0x00007f02d7f4a6fe in hsaKmtWaitOnMultipleEvents () from /opt/rocm/lib/../lib64/libhsakmt.so.1
#3  0x00007f02d8b463e5 in rocr::core::Signal::WaitAny(unsigned int, hsa_signal_s const*, hsa_signal_condition_t const*, long const*, unsigned long, hsa_wait_state_t, long*) () from /opt/rocm/lib/libhsa-runtime64.so.1
#4  0x00007f02d8b2de9e in rocr::AMD::hsa_amd_signal_wait_any(unsigned int, hsa_signal_s*, hsa_signal_condition_t*, long*, unsigned long, hsa_wait_state_t, long*) () from /opt/rocm/lib/libhsa-runtime64.so.1
#5  0x00007f02d8b3f670 in rocr::core::Runtime::AsyncEventsLoop(void*) () from /opt/rocm/lib/libhsa-runtime64.so.1
#6  0x00007f02d8af06c7 in rocr::os::ThreadTrampoline(void*) () from /opt/rocm/lib/libhsa-runtime64.so.1
#7  0x00007f02e4e8eea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00007f02e4bb79fd in clone () from /lib64/libc.so.6
Thread 2 (Thread 0x7f029beda700 (LWP 5911)):
#0  0x00007f02e4b7e8ed in nanosleep () from /lib64/libc.so.6
#1  0x00007f02e4baf1c4 in usleep () from /lib64/libc.so.6

...
Thread 1 (Thread 0x7f02e52b4740 (LWP 5853)):
#0  0x00007f02e4b9c807 in sched_yield () from /lib64/libc.so.6
#1  0x00007f02dff01605 in ?? () from /opt/rocm/lib/libamdhip64.so.4
#2  0x00007f02dff0ea20 in ?? () from /opt/rocm/lib/libamdhip64.so.4
#3  0x00007f02dfe34b4a in ?? () from /opt/rocm/lib/libamdhip64.so.4
#4  0x00007f02dfe385af in hipFree () from /opt/rocm/lib/libamdhip64.so.4

...
```






---

### 评论 #3 — ROCmSupport (2021-04-07T12:13:45Z)

Thanks for the update @windstamp 
Thank you much.

---
