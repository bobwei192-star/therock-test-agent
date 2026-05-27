# OpenCL ROCm 2.10 using 100% CPU *always*?

> **Issue #963**
> **状态**: closed
> **创建时间**: 2019-12-13T12:42:43Z
> **更新时间**: 2021-05-09T19:50:27Z
> **关闭时间**: 2021-05-09T19:50:26Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/963

## 描述

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


---

## 评论 (23 条)

### 评论 #1 — preda (2019-12-13T12:51:33Z)

Maybe this 100% CPU use is something intentional in ROCm 2.10 (AKA "a feature") -- is there a way to opt-out and get the old ROCm behavior?


---

### 评论 #2 — preda (2019-12-13T13:04:36Z)

How to repro: download GpuOwl (link above), compile and run with:
./gpuowl -prp 90047941
Observe 100% CPU usage by the gpuowl process.
The same on some older ROCm, observe <3% CPU usage.


---

### 评论 #3 — preda (2019-12-14T00:27:28Z)

This issues was introduced in ROCm 2.6. Verified that:
2.5 does not have it,
2.6, 2.7.2, 2.8, 2.9, 2.10 all have it.
The issue is located in the rocm-opencl package (i.e. keeping the rest of ROCm installation unchanged and changing just the version of rocm-opencl in enough to switch it on/off)


---

### 评论 #4 — preda (2019-12-14T09:22:00Z)

My motherboard is Asrock X99 Extreme4, the CPU is i7-5820K. Let me know if I can assist with other information.

---

### 评论 #5 — preda (2019-12-14T21:11:49Z)

Using "top -H" I can see which thread is busy 100%, which allows to identify the thread in gdb

```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                                                                                 
10794 preda     20   0   17.5g 331216  70164 R  99.9   0.5   1:51.39 gpuowl
```

```
(gdb) thread 15
[Switching to thread 15 (Thread 0x7fffeff7f700 (LWP 10794))]
#0  0x00007ffff73edced in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007ffff73edced in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#1  0x00007ffff73edb2a in core::InterruptSignal::WaitAcquire(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffff73dfe49 in HSA::hsa_signal_wait_scacquire(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#3  0x00007ffff7d9ae95 in ?? () from /home/preda/rocm-opencl/rocm2.10/libamdocl64.so
#4  0x00007ffff7d9d572 in ?? () from /home/preda/rocm-opencl/rocm2.10/libamdocl64.so
#5  0x00007ffff7da0484 in ?? () from /home/preda/rocm-opencl/rocm2.10/libamdocl64.so
#6  0x00007ffff7d67407 in ?? () from /home/preda/rocm-opencl/rocm2.10/libamdocl64.so
#7  0x00007ffff7d67ccd in ?? () from /home/preda/rocm-opencl/rocm2.10/libamdocl64.so
#8  0x00007ffff7ce06c6 in ?? () from /home/preda/rocm-opencl/rocm2.10/libamdocl64.so
#9  0x00007ffff7d53acf in ?? () from /home/preda/rocm-opencl/rocm2.10/libamdocl64.so
#10 0x00007ffff7861669 in start_thread (arg=<optimized out>) at pthread_create.c:479
#11 0x00007ffff7787323 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```


---

### 评论 #6 — preda (2019-12-14T21:43:28Z)

And the stack trace with debug symbols:
```
#0  0x00007ffff245cd11 in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007ffff245cd11 in core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#1  0x00007ffff245cb2a in core::InterruptSignal::WaitAcquire(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffff244ee49 in HSA::hsa_signal_wait_scacquire(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#3  0x00007ffff32e618c in roc::VirtualGPU::dispatchGenericAqlPacket<hsa_kernel_dispatch_packet_s> (this=this@entry=0x7ffb9c000b90, packet=0x7fffebf7ebf0, packet@entry=0x7fffebf7ebb0, header=<optimized out>, 
    rest=<optimized out>, blocking=<optimized out>, size=size@entry=1) at /usr/include/c++/9/new:174
#4  0x00007ffff32dfac9 in roc::VirtualGPU::dispatchAqlPacket (this=this@entry=0x7ffb9c000b90, packet=packet@entry=0x7fffebf7ebb0, header=<optimized out>, rest=<optimized out>, blocking=<optimized out>)
    at /home/preda/rocm-opencl/opencl/runtime/device/rocm/rocvirtual.cpp:457
#5  0x00007ffff32e419f in roc::VirtualGPU::submitKernelInternal (this=<optimized out>, sizes=..., kernel=..., parameters=<optimized out>, eventHandle=<optimized out>, sharedMemBytes=<optimized out>, 
    cooperativeGroups=<optimized out>) at /home/preda/rocm-opencl/opencl/runtime/platform/ndrange.hpp:124
#6  0x00007ffff32e4640 in roc::VirtualGPU::submitKernel (this=0x7ffb9c000b90, vcmd=...) at /home/preda/rocm-opencl/opencl/runtime/platform/command.hpp:794
#7  0x00007ffff32b3c3d in amd::HostQueue::loop (this=0x555555ae6cd0, virtualDevice=0x7ffb9c000b90) at /home/preda/rocm-opencl/opencl/runtime/platform/commandqueue.cpp:151
#8  0x00007ffff32b471f in amd::HostQueue::Thread::run (this=0x555555ae6d80, data=0x555555ae6cd0) at /home/preda/rocm-opencl/opencl/runtime/platform/commandqueue.hpp:145
#9  0x00007ffff320617b in amd::Thread::main (this=this@entry=0x555555ae6d80) at /home/preda/rocm-opencl/opencl/runtime/thread/thread.cpp:77
#10 0x00007ffff32b6057 in amd::Thread::entry (thread=0x555555ae6d80) at /home/preda/rocm-opencl/opencl/runtime/os/os_posix.cpp:390
#11 0x00007ffff28d6669 in start_thread (arg=<optimized out>) at pthread_create.c:479
#12 0x00007ffff27fc323 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```

---

### 评论 #7 — valeriob01 (2019-12-15T07:49:04Z)

> How to repro: download GpuOwl (link above), compile and run with:
> ./gpuowl -prp 90047941
> Observe 100% CPU usage by the gpuowl process.
> The same on some older ROCm, observe <3% CPU usage.

I can confirm. I am using ROCm 2.10 but with the old compiler from ver. 2.2 and the CPU utilization by gpuowl is 0.7%.

---

### 评论 #8 — preda (2019-12-15T10:26:59Z)

> > How to repro: download GpuOwl (link above), compile and run with:
> > ./gpuowl -prp 90047941
> > Observe 100% CPU usage by the gpuowl process.
> > The same on some older ROCm, observe <3% CPU usage.
> 
> I can confirm. I am using ROCm 2.10 but with the old compiler from ver. 2.2 and the CPU utilization by gpuowl is 0.7%.

@valeriob01 Can you try with the normal ROCm 2.10 (i.e. using libamdocl64.so from ROCm 2.10), do you see 100% of one core in that case?

---

### 评论 #9 — valeriob01 (2019-12-15T11:05:16Z)

I think we are using different systems I am on Debian 10.1, done a test with ver. 2.2 and ver 2.10, I can't see any difference, the reported gpuowl cpu utilization is between 0.7% and 3.0%.
(my cpu is Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz).

---

### 评论 #10 — valeriob01 (2019-12-15T11:27:18Z)

Only as a litmus check: what is your kernel version ?


---

### 评论 #11 — selroc (2019-12-15T12:27:04Z)

https://github.com/RadeonOpenCompute/ROCm/issues/828

---

### 评论 #12 — preda (2019-12-15T12:51:05Z)

Linux kernel 5.4.3

---

### 评论 #13 — preda (2019-12-15T12:56:34Z)

At first look it seems to be a problem in InterruptSignal::WaitRelaxed() in ROCR-Runtime. What is not clear yet is why this problem triggers on my system, but not on others..


---

### 评论 #14 — valeriob01 (2019-12-15T13:10:12Z)

> Linux kernel 5.4.3

I am on Linux kernel 4.19.67

---

### 评论 #15 — preda (2019-12-15T20:49:33Z)

 Another suspect: hsaKmtWaitOnEvent(event_, 0xFFFFFFFEu); seems to return imediately without waiting at all even when the event isn't satisfied.

I'm using the "stock kernel" without the DKMS (i.e. without the ROCm install patching the kernel). Would it be possible that a new event type was added in ROCm 2.6 that the upstream kernel doesn't know about yet (or something similar), which causes hsaKmtWaitOnEvent() to not wait (e.g. to return immediately with an error) ?

---

### 评论 #16 — 949f45ac (2019-12-16T06:38:02Z)

> Another suspect: hsaKmtWaitOnEvent

Cf. also https://github.com/RadeonOpenCompute/ROCm/issues/748 (me using HIP may explain that I’ve been seeing the problem since an earlier version)
Do you see the same "Signal event wasn't created because limit was reached" lines in dmesg maybe?

---

### 评论 #17 — preda (2019-12-16T08:10:49Z)

I confirm, I see this in dmesg for every instance of GpuOwl that I start:
Signal event wasn't created because limit was reached

---

### 评论 #18 — preda (2019-12-16T11:36:44Z)

https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/80
This seems to be the explanation: for an unknown reason ("problem 1") there is an exaustion of events (reflected in the dmesg message "Signal event wasn't created because limit was reached"), and after this point one thread starts doing busy-wait ("problem 2") taking up 100% of one core.

I'm now trying to get rid of all OpenCL events use in my app, yet this doesn't help -- the event overflow is still present. So this does not even originate from the app developer being too liberal with events, it seems to originate from internal events that are not under the control of the developer!


---

### 评论 #19 — preda (2019-12-21T00:21:31Z)

While I have implemented a workaround which allows me to use ROCm 2.10 without paying the 100% CPU cost (the workaround consists in adding a usleep(5) in the broken event wait loop that was busy-waiting before), this problem is not solved. What I don't understand is why this thread that apparently was introduced in ROCm 2.6 exists (while it was not needed before), and what are the events exactly given that my app does not explicitly create or use OpenCL events. Anyway the problem is not fixed. It seems it does not affect everybody, but when it hits the impact is severe. On my system it's 100% reproducible.


---

### 评论 #20 — b-sumner (2019-12-21T17:19:46Z)

My understanding is that there are a limited number of signals supported by the hardware, and when that is exceeded, polling is used.  Is it possible your application has a event leak or a large number of events are being used?  It's possible there is a signal leak in the OpenCL runtime as well.

---

### 评论 #21 — preda (2019-12-21T23:50:56Z)

> My understanding is that there are a limited number of signals supported by the hardware, and when that is exceeded, polling is used. Is it possible your application has a event leak or a large number of events are being used? It's possible there is a signal leak in the OpenCL runtime as well.

I checked and made sure that my app is not using any OpenCL events (when run with the default options). Thus I really can't see how it could be an event leak in the app itself. To work-around this issue I would gladly give up on using events (which I already did), unfortunately that didn't fix it. Thus the events are originating from "under the hood" somewhere.


---

### 评论 #22 — preda (2019-12-28T10:31:14Z)

I have identified the element that triggers this issue in my case:

I'm now running with an Asrock X299 Taichi motherboard. When I use 4x GPUs in the PCIe slots 1, 3, 4, 5, the problem is present, i.e.:
"Signal event wasn't created because limit was reached" is logged in dmesg *once per application instance (i.e. per GPU)*, and 100% one-thread CPU usage is observed per application instance (corresponding to all 4 GPUs).

OTOH when I use only 3x GPUs in the PCIe slots 1, 3, 5, the problem dissapears:
- the event limit-reached is not logged in dmesg at all,
- the CPU usage is under 3% per application instance, as expected

The PCIe slot 4 on this MB is special, it is the only slot that is Gen2 x1, and apparently wired differently internally (through an additional PCIe brigde?).

The other slots (1, 3, 5) are Gen3 but I configure them in BIOS to be run at Gen1 speed (in all cases); (the slot 4 is also configured to run at Gen1 speed).

So my hypothesis is:
- the fact that even one GPU is connected to this "trouble" PCIe slot (Gen2x1) changes the behavior of the driver for all the GPUs on the system (not only the GPU connected to this slot, but all of them).
- the driver suddenly starts using lots of events where it would not use them otherwise
- the kernel event limit is reached, and this hits the busy-wait loop discussed above

What is also clear is that the events do not originate from inside the application (this is what I stated before), because in the situation with only 3 GPUs no event limit is reached ever despite the same app being run.


---

### 评论 #23 — preda (2021-05-09T19:50:26Z)

Closing as old, presumably fixed in the meantime.

---
