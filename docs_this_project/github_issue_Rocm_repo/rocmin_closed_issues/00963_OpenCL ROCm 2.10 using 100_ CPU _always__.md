# OpenCL ROCm 2.10 using 100% CPU *always*?

- **Issue #:** 963
- **State:** closed
- **Created:** 2019-12-13T12:42:43Z
- **Updated:** 2021-05-09T19:50:27Z
- **URL:** https://github.com/ROCm/ROCm/issues/963

On Ubuntu 19.10, kernel 5.4.3, RadeonVii, ROCm 2.10,
running GpuOwl https://github.com/preda/gpuowl
I see the GpuOwl process using up 100% of one CPU thread. But with older versions of ROCm, GpuOwl was using very little CPU (around 3%). I also confirm that GpuOwl does no busy-waiting itself, and that it does not do any CPU intensive computation that would explain the observed 100%.

So the 100% CPU usage comes from ROCm, probably starting with 2.10 (I don't know whether this was present or not on 2.9).

I captured two thread profiles of the running app:
```
info threads
  Id   Target Id                                 Frame 
* 1    Thread 0x7ffff70d4140 (LWP 3903) "gpuowl" 0x00007ffff774ad45 in __GI___nanosleep (requested_time=requested_time@entry=0x7fffffffd2d0, remaining=remaining@entry=0x0)
    at ../sysdeps/unix/sysv/linux/nanosleep.c:28
  2    Thread 0x7ffff70c7700 (LWP 3907) "gpuowl" 0x00007ffff777c67b in ioctl () at ../sysdeps/unix/syscall-template.S:78
  3    Thread 0x7ffff6560700 (LWP 3908) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  4    Thread 0x7ffff5d5f700 (LWP 3909) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  5    Thread 0x7ffff555e700 (LWP 3910) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  6    Thread 0x7ffff4d5d700 (LWP 3911) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad14) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  7    Thread 0x7ffbea8ef700 (LWP 3912) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad14) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  8    Thread 0x7ffbea0ee700 (LWP 3913) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  9    Thread 0x7fffeff7f700 (LWP 3914) "gpuowl" 0x00007ffff73edd19 in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) ()
   from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
(gdb) thread 9
[Switching to thread 9 (Thread 0x7fffeff7f700 (LWP 3914))]
#0  0x00007ffff73edd19 in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007ffff73edd19 in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#1  0x00007ffff73edb2a in core::InterruptSignal::WaitAcquire(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffff73dfe49 in HSA::hsa_signal_wait_scacquire(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#3  0x00007ffff7d8ad6d in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#4  0x00007ffff7d8d501 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#5  0x00007ffff7d540bc in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#6  0x00007ffff7d54ccd in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#7  0x00007ffff7ccd6c6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#8  0x00007ffff7d40acf in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#9  0x00007ffff7861669 in start_thread (arg=<optimized out>) at pthread_create.c:479
#10 0x00007ffff7787323 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
(gdb)

----

info threads
  Id   Target Id                                 Frame 
* 1    Thread 0x7ffff70d4140 (LWP 3903) "gpuowl" 0x00007ffff774ad45 in __GI___nanosleep (requested_time=requested_time@entry=0x7fffffffd2d0, remaining=remaining@entry=0x0)
    at ../sysdeps/unix/sysv/linux/nanosleep.c:28
  2    Thread 0x7ffff70c7700 (LWP 3907) "gpuowl" 0x00007ffff777c67b in ioctl () at ../sysdeps/unix/syscall-template.S:78
  3    Thread 0x7ffff6560700 (LWP 3908) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  4    Thread 0x7ffff5d5f700 (LWP 3909) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  5    Thread 0x7ffff555e700 (LWP 3910) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  6    Thread 0x7ffff4d5d700 (LWP 3911) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad14) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  7    Thread 0x7ffbea8ef700 (LWP 3912) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad14) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  8    Thread 0x7ffbea0ee700 (LWP 3913) "gpuowl" futex_wait_cancelable (private=<optimized out>, expected=0, futex_word=0x7ffbef7fad10) at ../sysdeps/unix/sysv/linux/futex-internal.h:80
  9    Thread 0x7fffeff7f700 (LWP 3914) "gpuowl" 0x00007ffff73edc8a in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) ()
   from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
(gdb) thread 9
[Switching to thread 9 (Thread 0x7fffeff7f700 (LWP 3914))]
#0  0x00007ffff73edc8a in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007ffff73edc8a in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#1  0x00007ffff73edb2a in core::InterruptSignal::WaitAcquire(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffff73dfe49 in HSA::hsa_signal_wait_scacquire(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#3  0x00007ffff7d87e95 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#4  0x00007ffff7d8a572 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#5  0x00007ffff7d8d484 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#6  0x00007ffff7d54407 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#7  0x00007ffff7d54ccd in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#8  0x00007ffff7ccd6c6 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#9  0x00007ffff7d40acf in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
#10 0x00007ffff7861669 in start_thread (arg=<optimized out>) at pthread_create.c:479
#11 0x00007ffff7787323 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

```
I singled-in on thread-9 as my main suspect because this is the thread that I do not see when running with an old ROCm that does not show the problem, so this is what I see as a candidate for "the thread that's busy 100%"

Needless to say, if the problem I'm describing is real it's pretty severe in terms of power usage, heat, and CPU slow-down for competing apps.
