# "Signal event wasn't created because limit was reached" – One CPU Core per Card Spinning at 100%, Since ROCm 2.1

> **Issue #748**
> **状态**: closed
> **创建时间**: 2019-03-20T19:47:55Z
> **更新时间**: 2024-12-12T14:59:48Z
> **关闭时间**: 2024-12-12T14:59:48Z
> **作者**: 949f45ac
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/748

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

I am running amdgpu-pro driver with ROCm as outlined here: https://github.com/949f45ac/xmrig-HIP#setup-for-high-vega-hashrate-on-linux
I am using Vega and Polaris, alone and mixed. They behave the same as far as this bug is concerned.

On version 2.1 and 2.2 I am running into a problem with two GPU miners:
- https://github.com/949f45ac/xmrig-HIP
- https://github.com/enerc/VulkanXMRMiner
- OpenCL however seems to work ok (I tested xmrig-amd)

The problem is that after a while these miners will hog one full CPU core per card they are using. At the same time, speed will stay absolutely fine, it seems like. Everything works, only that one full CPU core is spinning at 100%, for every card being used.

You can configure these miners to start multiple parallel workloads ("streams" in HIP/CUDA parlor) per card, but they will still only hog 100% per card, not per workload. (Ok, this is probably due to the fact that certain calls are only done in 1 thread per card at a time.)

I have tested all of `hipDeviceSchedule{Yield,Spin,BlockingSync}` and all have that problem.

I think the problem lies somewhere deep in hsaKmt, not in the application code. I have used the technique from https://poormansprofiler.org/ to take stack dumps of xmrig-HIP. There is a notable difference from the good (~0% CPU) state and the corrupt one:

Good:
```
Thread 3 (Thread 0x7f183b7ff700 (LWP 12168)):
#0  0x00007f1843b5b5d7 in ioctl () at ../sysdeps/unix/syscall-template.S:78
#1  0x00007f184382c0b8 in ?? () from /opt/rocm/lib/libhsakmt.so.1
#2  0x00007f1843825c8f in hsaKmtWaitOnMultipleEvents () from /opt/rocm/lib/libhsakmt.so.1
#3  0x00007f1843826249 in hsaKmtWaitOnEvent () from /opt/rocm/lib/libhsakmt.so.1
#4  0x00007f1844297d2a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#5  0x00007f1844297b2a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#6  0x00007f184428a139 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#7  0x00007f18425ae04f in waitComplete () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4815
#8  0x00007f18425adcfd in operator() () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4941
#9  _M_invoke<> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1530
#10 operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1520
#11 operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1342
#12 0x00007f18425adc92 in _M_invoke () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1856
#13 0x00007f18425adc07 in operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:2267
#14 _M_do_set () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:527
#15 0x00007f184529b827 in __pthread_once_slow (once_control=0x7f1834c902e8, init_routine=0x7f1845b09760 <__once_proxy>) at pthread_once.c:116
#16 0x00007f18425ae5cb in __gthread_once () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/x86_64-linux-gnu/c++/5.4.0/bits/gthr-default.h:699
#17 call_once<void (std::__future_base::_State_baseV2::*)(std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *), std::__future_base::_State_baseV2 *, std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/mutex:738
#18 _M_set_result () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:386
#19 _M_complete_async () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1606
#20 0x00007f1844568ddf in hc::completion_future::wait(Kalmar::enums::hcWaitMode) const () from /opt/rocm/lib/libhip_hcc.so
#21 0x00007f1844568d88 in ihipStream_t::locked_eventWaitComplete(hc::completion_future&, Kalmar::enums::hcWaitMode) () from /opt/rocm/lib/libhip_hcc.so
#22 0x00007f18445e547e in hipEventSynchronize () from /opt/rocm/lib/libhip_hcc.so
#23 0x00000000004abbc7 in CudaWorker::start() ()
#24 0x00007f18452936db in start_thread (arg=0x7f183b7ff700) at pthread_create.c:463
#25 0x00007f1843b6688f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```

Bad:
```
Thread 4 (Thread 0x7f183affe700 (LWP 12169)):                                                                                                                                                                                                
#0  0x00007f1844297d25 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1                                                                                                                                                                 
#1  0x00007f1844297b2a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1                                                                                                                                                                 
#2  0x00007f184428a139 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1                                                                                                                                                                 
#3  0x00007f18425ae04f in waitComplete () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4815                                                                                                       
#4  0x00007f18425adcfd in operator() () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4941                                                                                                         
#5  _M_invoke<> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1530                                                                                                                                      
#6  operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1520                                                                                                                                       
#7  operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1342                                                                                                                                           
#8  0x00007f18425adc92 in _M_invoke () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1856                                                                                                                  
#9  0x00007f18425adc07 in operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:2267                                                                                                                 
#10 _M_do_set () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:527                                                                                                                                             
#11 0x00007f184529b827 in __pthread_once_slow (once_control=0x7f182c2b0da8, init_routine=0x7f1845b09760 <__once_proxy>) at pthread_once.c:116                                                                                                
#12 0x00007f18425ae5cb in __gthread_once () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/x86_64-linux-gnu/c++/5.4.0/bits/gthr-default.h:699                                                                                    
#13 call_once<void (std::__future_base::_State_baseV2::*)(std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *), std::__future_base::_State_baseV2 *, std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/mutex:738                                                    
#14 _M_set_result () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:386                                                                                                                                         
#15 _M_complete_async () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1606                                                                                                                                    
#16 0x00007f184258f879 in wait () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:319                                                                                                                            
#17 wait () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:656                                                                                                                                                  
#18 wait () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:1617                                                                                                                                     
#19 0x00007f184258efb5 in copy_ext () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4076                                                                                                           
#20 0x00007f1844573cac in ihipStream_t::locked_copyAsync(void*, void const*, unsigned long, unsigned int) () from /opt/rocm/lib/libhip_hcc.so                                                                                                
#21 0x00007f1844620919 in hipMemcpyAsync () from /opt/rocm/lib/libhip_hcc.so                                                                                                                                                                 
#22 0x0000000000451932 in cryptonight_extra_cpu_final ()                                                                                                                                                                                     
#23 0x00000000004abc89 in CudaWorker::start() ()                                                                                                                                                                                             
#24 0x00007f18452936db in start_thread (arg=0x7f183affe700) at pthread_create.c:463                                                                                                                                                          
#25 0x00007f1843b6688f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95  
```

So the stack is basically the same, only the bad case is missing the four topmost entries:
```
#0  0x00007f1843b5b5d7 in ioctl () at ../sysdeps/unix/syscall-template.S:78
#1  0x00007f184382c0b8 in ?? () from /opt/rocm/lib/libhsakmt.so.1
#2  0x00007f1843825c8f in hsaKmtWaitOnMultipleEvents () from /opt/rocm/lib/libhsakmt.so.1
#3  0x00007f1843826249 in hsaKmtWaitOnEvent () from /opt/rocm/lib/libhsakmt.so.1
```

I am attaching the full stack output, in case the perpetrator is actually some other thread that I overlooked. Hope this helps!
Since file upload fails for me I created gists:
(good) https://gist.github.com/949f45ac/d5fe8958181e6657e90b2a4878e6b039
(bad) https://gist.github.com/949f45ac/613ddf969eb2527e42096fe542103b0c

---

## 评论 (12 条)

### 评论 #1 — 949f45ac (2019-03-24T19:00:18Z)

Ok, some updates on this:
- It does not actually happen with the Vulkan miner, at least not within any noteworthy timeframe. I guess I made a mistake there, or it does simply occur seldomly on that miner.
- On HIP I looked deeper into it… I have removed everything in the way of complex stream synchronization I may have been doing. I have reproduced the problem running one workload on one single Vega card, with now the only stream syncing done by `hipMemcpyAsync`. (What I removed: https://github.com/949f45ac/xmrig-HIP/commit/86a6914978e0d9e7e88980902b793ed72748e4d2) 

Here’s the traces:

Good:
```
Thread 3 (Thread 0x7fdf553ff700 (LWP 6520)):
#0  0x00007fdf588125d7 in ioctl () at ../sysdeps/unix/syscall-template.S:78
#1  0x00007fdf584e30b8 in ?? () from /opt/rocm/lib/libhsakmt.so.1
#2  0x00007fdf584dcc8f in hsaKmtWaitOnMultipleEvents () from /opt/rocm/lib/libhsakmt.so.1
#3  0x00007fdf584dd249 in hsaKmtWaitOnEvent () from /opt/rocm/lib/libhsakmt.so.1
#4  0x00007fdf58f4ed2a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#5  0x00007fdf58f4eb2a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#6  0x00007fdf58f41139 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#7  0x00007fdf5726504f in waitComplete () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4815
#8  0x00007fdf57264cfd in operator() () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4941
#9  _M_invoke<> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1530
#10 operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1520
#11 operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1342
#12 0x00007fdf57264c92 in _M_invoke () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1856
#13 0x00007fdf57264c07 in operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:2267
#14 _M_do_set () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:527
#15 0x00007fdf59f52827 in __pthread_once_slow (once_control=0x7fdf48157ff8, init_routine=0x7fdf5a7c0760 <__once_proxy>) at pthread_once.c:116
#16 0x00007fdf572655cb in __gthread_once () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/x86_64-linux-gnu/c++/5.4.0/bits/gthr-default.h:699
#17 call_once<void (std::__future_base::_State_baseV2::*)(std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *), std::__future_base::_State_baseV2 *, std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/mutex:738
#18 _M_set_result () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:386
#19 _M_complete_async () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1606
#20 0x00007fdf57246879 in wait () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:319
#21 wait () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:656
#22 wait () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:1617
#23 0x00007fdf57245fb5 in copy_ext () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4076
#24 0x00007fdf5922acac in ihipStream_t::locked_copyAsync(void*, void const*, unsigned long, unsigned int) () from /opt/rocm/hip/lib/libhip_hcc.so
#25 0x00007fdf592d7919 in hipMemcpyAsync () from /opt/rocm/hip/lib/libhip_hcc.so
#26 0x000000000044b972 in cryptonight_extra_cpu_final ()
#27 0x00000000004acf3a in CudaWorker::start (this=0x7fdf48000b20) at /home/a/code/xmrig-HIP/src/workers/CudaWorker.cpp:154
#28 0x00000000004b2b21 in Workers::start (worker=0x7fdf48000b20) at /home/a/code/xmrig-HIP/src/workers/Workers.cpp:415
#29 0x00000000004b24bc in Workers::onReady (arg=0x2199d60) at /home/a/code/xmrig-HIP/src/workers/Workers.cpp:332
#30 0x00007fdf59f4a6db in start_thread (arg=0x7fdf553ff700) at pthread_create.c:463
#31 0x00007fdf5881d88f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```

Bad:
```
Thread 3 (Thread 0x7fdf553ff700 (LWP 6520)):
#0  0x00007fdf584dd227 in hsaKmtWaitOnEvent () from /opt/rocm/lib/libhsakmt.so.1
#1  0x00007fdf58f4ed2a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007fdf58f4eb2a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#3  0x00007fdf58f41139 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#4  0x00007fdf5726504f in waitComplete () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4815
#5  0x00007fdf57264cfd in operator() () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4941
#6  _M_invoke<> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1530
#7  operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1520
#8  operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1342
#9  0x00007fdf57264c92 in _M_invoke () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1856
#10 0x00007fdf57264c07 in operator() () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:2267
#11 _M_do_set () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:527
#12 0x00007fdf59f52827 in __pthread_once_slow (once_control=0x7fdf4876f988, init_routine=0x7fdf5a7c0760 <__once_proxy>) at pthread_once.c:116
#13 0x00007fdf572655cb in __gthread_once () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/x86_64-linux-gnu/c++/5.4.0/bits/gthr-default.h:699
#14 call_once<void (std::__future_base::_State_baseV2::*)(std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *), std::__future_base::_State_baseV2 *, std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *> () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/mutex:738
#15 _M_set_result () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:386
#16 _M_complete_async () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1606
#17 0x00007fdf57246879 in wait () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:319
#18 wait () at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:656
#19 wait () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:1617
#20 0x00007fdf57245fb5 in copy_ext () at /data/jenkins_workspace/compute-rocm-rel-2.2/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:4076
#21 0x00007fdf5922acac in ihipStream_t::locked_copyAsync(void*, void const*, unsigned long, unsigned int) () from /opt/rocm/hip/lib/libhip_hcc.so
#22 0x00007fdf592d7919 in hipMemcpyAsync () from /opt/rocm/hip/lib/libhip_hcc.so
#23 0x000000000044b972 in cryptonight_extra_cpu_final ()
#24 0x00000000004acf3a in CudaWorker::start (this=0x7fdf48000b20) at /home/a/code/xmrig-HIP/src/workers/CudaWorker.cpp:154
#25 0x00000000004b2b21 in Workers::start (worker=0x7fdf48000b20) at /home/a/code/xmrig-HIP/src/workers/Workers.cpp:415
#26 0x00000000004b24bc in Workers::onReady (arg=0x2199d60) at /home/a/code/xmrig-HIP/src/workers/Workers.cpp:332
#27 0x00007fdf59f4a6db in start_thread (arg=0x7fdf553ff700) at pthread_create.c:463
#28 0x00007fdf5881d88f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```

So it seems that the jump from `hsaKmtWaitOnEvent` -> `hsaKmtWaitOnMultipleEvents` is where the CPU spins in this case.

---

### 评论 #2 — 949f45ac (2019-04-07T13:14:56Z)

### More investigation
The problem occurs reproducably after a set amount of kernel launches by the process. When it happens, `dmesg` says: `Signal event wasn't created because limit was reached`. Simply restarting the process at this point makes the problem go away, until the set amount of kernels have once more been launched.

What’s triggering it are probably not exactly kernel launches, but something related to that. (Well, signals?)
When I run a computation that includes five kernel launches, the problem occurs after 417 rounds, i.e. ~2070 launches.
A computation that has an additional kernel launch triggers the problem after ~376 rounds, i.e. ~2256 launches.
Would be more logical if the first variant had 9 of "something" per round, the second one 10 – then both are triggering the problem after ~3750 of these somethings.

Let’s have a look at `HIP_DB=api` output for one round of the first kind (triggering after ~417 runs):
```txt
<<hip-api pid:18607 tid:2.46 hipModuleLaunchKernel (0x6c33f6500, 28, 1, 1, 128, 1, 1, 0, stream:0.1, 0, 0x7f27df5fead0) @1832951739572
<<hip-api pid:18607 tid:2.46 18607 2.46 hipLaunchKernel '_Z29cryptonight_extra_gpu_prepareILb0EEviPjjjS0_S0_S0_S0_S0_S0_' gridDim:{3584,1,1} groupDim:{128,1,1} sharedMem:+0 stream:0.1 @1832951752797
  hip-api pid:18607 tid:2.46 hipModuleLaunchKernel          ret= 0 (hipSuccess)>> +147790 ns
<<hip-api pid:18607 tid:2.47 hipGetLastError () @1832951893574
  hip-api pid:18607 tid:2.47 hipGetLastError                ret= 0 (hipSuccess)>> +3507 ns
<<hip-api pid:18607 tid:2.48 hipModuleLaunchKernel (0x6c3244800, 112, 1, 1, 256, 1, 1, 0, stream:0.1, 0, 0x7f27df5fead0) @1832951921096
<<hip-api pid:18607 tid:2.48 18607 2.48 hipLaunchKernel '_Z27cryptonight_core_gpu_phase1ILN5xmrig4AlgoE0ELNS0_7VariantE9ELb0ELi8EEviPmPjS4_' gridDim:{28672,1,1} groupDim:{256,1,1} sharedMem:+0 stream:0.1 @1832951930013
  hip-api pid:18607 tid:2.48 hipModuleLaunchKernel          ret= 0 (hipSuccess)>> +96196784 ns
<<hip-api pid:18607 tid:2.49 hipGetLastError () @1833048154028
  hip-api pid:18607 tid:2.49 hipGetLastError                ret= 0 (hipSuccess)>> +4038 ns
<<hip-api pid:18607 tid:2.50 hipEventRecord (event:0x7f27d8083110, stream:0.1) @1833048180598
  hip-api pid:18607 tid:2.50 hipEventRecord                 ret= 0 (hipSuccess)>> +15470 ns
<<hip-api pid:18607 tid:2.51 hipGetLastError () @1833048202179
  hip-api pid:18607 tid:2.51 hipGetLastError                ret= 0 (hipSuccess)>> +3447 ns
<<hip-api pid:18607 tid:2.52 hipModuleLaunchKernel (0x6c335c000, 112, 1, 1, 32, 1, 1, 0, stream:0.1, 0, 0x7f27df5fea50) @1833048241484
<<hip-api pid:18607 tid:2.52 18607 2.52 hipLaunchKernel '_Z37cryptonight_core_gpu_phase2_monero_v8ILN5xmrig4AlgoE0ELNS0_7VariantE9ELb0ELi8EEviPmPjS4_S4_jS4_' gridDim:{3584,1,1} groupDim:{32,1,1} sharedMem:+0 stream:0.1 @1833048252805
  hip-api pid:18607 tid:2.52 hipModuleLaunchKernel          ret= 0 (hipSuccess)>> +937271000 ns
<<hip-api pid:18607 tid:2.53 hipGetLastError () @1833985548402
  hip-api pid:18607 tid:2.53 hipGetLastError                ret= 0 (hipSuccess)>> +4248 ns
<<hip-api pid:18607 tid:2.54 hipEventSynchronize (event:0x7f27d8083110) @1833985575464
  hip-api pid:18607 tid:2.54 hipEventSynchronize            ret= 0 (hipSuccess)>> +9057 ns
<<hip-api pid:18607 tid:2.55 hipGetLastError () @1833985590272
  hip-api pid:18607 tid:2.55 hipGetLastError                ret= 0 (hipSuccess)>> +3506 ns
<<hip-api pid:18607 tid:2.56 hipStreamWaitEvent (stream:0.1, event:0x7f27d8083110, 0) @1833985605661
  hip-api pid:18607 tid:2.56 hipStreamWaitEvent             ret= 0 (hipSuccess)>> +13786 ns
<<hip-api pid:18607 tid:2.57 hipGetLastError () @1833985624967
  hip-api pid:18607 tid:2.57 hipGetLastError                ret= 0 (hipSuccess)>> +3307 ns
<<hip-api pid:18607 tid:2.58 hipModuleLaunchKernel (0x6c32f1000, 112, 1, 1, 256, 1, 1, 0, stream:0.1, 0, 0x7f27df5feac0) @1833985660835
<<hip-api pid:18607 tid:2.58 18607 2.58 hipLaunchKernel '_Z27cryptonight_core_gpu_phase3ILN5xmrig4AlgoE0ELNS0_7VariantE9ELb0ELi8EEviPKmPjS5_' gridDim:{28672,1,1} groupDim:{256,1,1} sharedMem:+0 stream:0.1 @1833985671796
  hip-api pid:18607 tid:2.58 hipModuleLaunchKernel          ret= 0 (hipSuccess)>> +97162393 ns
<<hip-api pid:18607 tid:2.59 hipGetLastError () @1834082859497
  hip-api pid:18607 tid:2.59 hipGetLastError                ret= 0 (hipSuccess)>> +4068 ns
<<hip-api pid:18607 tid:2.60 hipMemsetAsync (0x6c2e71000, 255, 40, stream:0.1) @1834082888762
<<hip-api pid:18607 tid:2.61 hipModuleLaunchKernel (0x6c2e73300, 1, 1, 1, 256, 1, 1, 0, stream:0.1, 0, 0x7f27df5fe670) @1834082913239
<<hip-api pid:18607 tid:2.61 18607 2.61 hipLaunchKernel '_ZN12_GLOBAL__N_110hip_fill_nILj256EPjmjEEvT0_T1_T2_' gridDim:{256,1,1} groupDim:{256,1,1} sharedMem:+0 stream:0.1 @1834082923588
  hip-api pid:18607 tid:2.61 hipModuleLaunchKernel          ret= 0 (hipSuccess)>> +44815 ns
  hip-api pid:18607 tid:2.61 hipMemsetAsync                 ret= 0 (hipSuccess)>> +74391 ns
<<hip-api pid:18607 tid:2.62 hipGetLastError () @1834082968954
  hip-api pid:18607 tid:2.62 hipGetLastError                ret= 0 (hipSuccess)>> +3437 ns
<<hip-api pid:18607 tid:2.63 hipMemsetAsync (0x6c2e70000, 0, 4, stream:0.1) @1834082982710
<<hip-api pid:18607 tid:2.64 hipModuleLaunchKernel (0x6c2e73300, 1, 1, 1, 256, 1, 1, 0, stream:0.1, 0, 0x7f27df5fe670) @1834082998630
<<hip-api pid:18607 tid:2.64 18607 2.64 hipLaunchKernel '_ZN12_GLOBAL__N_110hip_fill_nILj256EPjmjEEvT0_T1_T2_' gridDim:{256,1,1} groupDim:{256,1,1} sharedMem:+0 stream:0.1 @1834083006806
  hip-api pid:18607 tid:2.64 hipModuleLaunchKernel          ret= 0 (hipSuccess)>> +34556 ns
  hip-api pid:18607 tid:2.64 hipMemsetAsync                 ret= 0 (hipSuccess)>> +54994 ns
<<hip-api pid:18607 tid:2.65 hipGetLastError () @1834083042914
  hip-api pid:18607 tid:2.65 hipGetLastError                ret= 0 (hipSuccess)>> +3337 ns
<<hip-api pid:18607 tid:2.66 hipModuleLaunchKernel (0x6c336a600, 14, 1, 1, 256, 1, 1, 0, stream:0.1, 0, 0x7f27df5feb10) @1834083074915
<<hip-api pid:18607 tid:2.66 18607 2.66 hipLaunchKernel '_Z27cryptonight_extra_gpu_finalILb0EEvimPjS0_S0_S0_' gridDim:{3584,1,1} groupDim:{256,1,1} sharedMem:+0 stream:0.1 @1834083083802
  hip-api pid:18607 tid:2.66 hipModuleLaunchKernel          ret= 0 (hipSuccess)>> +1758381 ns
<<hip-api pid:18607 tid:2.67 hipGetLastError () @1834084867721
  hip-api pid:18607 tid:2.67 hipGetLastError                ret= 0 (hipSuccess)>> +4188 ns
<<hip-api pid:18607 tid:2.68 hipMemcpyAsync (0x7f27df5fed40, 0x6c2e70000, 4, hipMemcpyDeviceToHost, stream:0.1) @1834084912486
  hip-api pid:18607 tid:2.68 hipMemcpyAsync                 ret= 0 (hipSuccess)>> +37210 ns
<<hip-api pid:18607 tid:2.69 hipGetLastError () @1834084955878
  hip-api pid:18607 tid:2.69 hipGetLastError                ret= 0 (hipSuccess)>> +3447 ns
<<hip-api pid:18607 tid:2.70 hipMemcpyAsync (0x7f27df5fed50, 0x6c2e71000, 40, hipMemcpyDeviceToHost, stream:0.1) @1834084969614
  hip-api pid:18607 tid:2.70 hipMemcpyAsync                 ret= 0 (hipSuccess)>> +20780 ns
<<hip-api pid:18607 tid:2.71 hipGetLastError () @1834084995764
  hip-api pid:18607 tid:2.71 hipGetLastError                ret= 0 (hipSuccess)>> +3356 ns
<<hip-api pid:18607 tid:2.72 hipStreamSynchronize (stream:0.1) @1834085006494
  hip-api pid:18607 tid:2.72 hipStreamSynchronize           ret= 0 (hipSuccess)>> +4308 ns
```

There’s actually two additional kernel launches via `hipFill`, making for 7 overall. Then there is two of each `hipMemsetAsync` and `hipMemcpyAsync`. Finally there is one of each `hipEventRecord`, `hipEventSynchronize` and `hipStreamWaitEvent`.

---

### 评论 #3 — 949f45ac (2019-04-15T17:58:59Z)

Issue persists on ROCm 2.3.
Please do something about this. I’ve ended up just downgrading to 2.0 for now.

---

### 评论 #4 — 949f45ac (2019-07-16T12:13:48Z)

Issue persists on ROCm 2.6. Now CPU usage even goes up to 120-190% for two workloads on a single card. Single workload still brings CPU to exactly 100% (one core spinning).

---

### 评论 #5 — smartbitcoin (2019-07-23T15:26:42Z)

Same issue found in hcc based application ( not hip or vulkan, it's just based on hcc framework ).
After long time running ,( mostly after 12 hours ),  the one of the hsa thread will dead b/c this ).

![image](https://user-images.githubusercontent.com/5984485/61723985-0defb600-ad3b-11e9-9de4-b17734e052f8.png)

and gradually , all thread will dead if hsa kernel complain the signal event create failed.

This should be a hsa fundamental implementation issue, but seems nobody from amd rocm team cares. The simple reason maybe they never meet this issue in production system as there are no serious product app they ever build, even HIP based tensorflow. 

But there are still clues as @949f45ac you mentioned,   rocm2.0 never saw this ,  so this should be a regression bug.   we can compare what's the change from 2.0 to 2.x.   This gonna be a challenge as rocm was restructure alot almost every release and now they move everything into  linux 5.3 with kfd together.  Tracing those regression issue if not done when it happens like solve it from 2.0->2.1,  it's almost impossible when we have 2.6 .

The best hope is that more and more long run app meet this bug,  but that depends rocm have the chance be a successful project and whole ecosystem go bigger.

More concern come out that rocm maybe failed as the bad quality of the implementation prevent serious app build on it.  If you try navi with linux 5.3-rc1 with vulkan or opencl,  you will feel the frustration you never met ( or exciting if you like hacking .) 


 

---

### 评论 #6 — tasso (2023-12-08T18:21:06Z)

Is the open issue still reproducible?  If not; can we please close the issue?  Thanks!

---

### 评论 #7 — tada123 (2023-12-12T11:27:24Z)

Still reproducible on `Linux hostname 6.6.6-arch1-1 #1 SMP PREEMPT_DYNAMIC Mon, 11 Dec 2023 11:48:23 +0000 x86_64 GNU/Linux`. The problem disappears, when `linux-lts` kernel is installed, but isn't there a more robust solution, than kernel downgrade workaround? I'd be interested, what is the reason of this behavior.

---

### 评论 #8 — tasso (2023-12-20T18:18:00Z)

Asking internal for help.  Thanks!

---

### 评论 #9 — akondrat-amd (2023-12-21T02:33:57Z)

@tada123 Can you provide minimal steps to reproduce the issue? ROCm version? Is it xmrig-HIP miner only? 
Please provide the build commands and workarounds(if any)

---

### 评论 #10 — tada123 (2023-12-21T15:22:19Z)

When using PyTorch:

```
import torch

... Long model training code (including Convolutions, FCN, ...)
...
...
# Now, trying to print loss:
c = t.to('cpu') # Move tensor from GPU (hangs for very long time, calls `synchronize`, but when paused in GDB and unpaused after some time, the program continues fine (without GDB, the same time is spent with 100% CPU))

```

System information:
```
>>> rocminfo
ROCk module is loaded                           =====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                  
System Endianness:       LITTLE                 
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 3 2200G with Radeon Vega Graphics
  Uuid:                    CPU-XX               
  Marketing Name:          AMD Ryzen 3 2200G with Radeon Vega Graphics
  Vendor Name:             CPU                  
  Feature:                 None specified       
  Profile:                 FULL_PROFILE         
  Float Round Mode:        NEAR                 
  Max Queue Number:        0(0x0)               
  Queue Min Size:          0(0x0)               
  Queue Max Size:          0(0x0)               
  Queue Type:              MULTI                
  Node:                    0                    
  Device Type:             CPU                  
  Cache Info:
    L1:                      32768(0x8000) KB   
  Chip ID:                 0(0x0)               
  ASIC Revision:           0(0x0)               
  Cacheline Size:          64(0x40)             
  Max Clock Freq. (MHz):   3500                 
  BDFID:                   0                    
  Internal Node ID:        0                    
  Compute Unit:            4                    
  SIMDs per CU:            0                    
  Shader Engines:          0                    
  Shader Arrs. per Eng.:   0                    
  WatchPts on Addr. Ranges:1                    
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    16305608(0xf8cdc8) KB
      Allocatable:             TRUE             
      Alloc Granule:           4KB              
      Alloc Alignment:         4KB              
      Accessible by all:       TRUE             
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16305608(0xf8cdc8) KB
      Allocatable:             TRUE             
      Alloc Granule:           4KB              
      Alloc Alignment:         4KB              
      Accessible by all:       TRUE             
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16305608(0xf8cdc8) KB
      Allocatable:             TRUE             
      Alloc Granule:           4KB              
      Alloc Alignment:         4KB              
      Accessible by all:       TRUE             
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx803               
  Uuid:                    GPU-XX               
  Marketing Name:          AMD Radeon RX 560 Series
  Vendor Name:             AMD                  
  Feature:                 KERNEL_DISPATCH      
  Profile:                 BASE_PROFILE         
  Float Round Mode:        NEAR                 
  Max Queue Number:        128(0x80)            
  Queue Min Size:          64(0x40)             
  Queue Max Size:          131072(0x20000)      
  Queue Type:              MULTI                
  Node:                    1                    
  Device Type:             GPU                  
  Cache Info:
    L1:                      16(0x10) KB        
  Chip ID:                 26607(0x67ef)        
  ASIC Revision:           1(0x1)               
  Cacheline Size:          64(0x40)             
  Max Clock Freq. (MHz):   1176                 
  BDFID:                   256                  
  Internal Node ID:        1                    
  Compute Unit:            14                   
  SIMDs per CU:            4                    
  Shader Engines:          2                    
  Shader Arrs. per Eng.:   1                    
  WatchPts on Addr. Ranges:4                    
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE                 
  Wavefront Size:          64(0x40)             
  Workgroup Max Size:      1024(0x400)          
  Workgroup Max Size per Dimension:
    x                        1024(0x400)        
    y                        1024(0x400)        
    z                        1024(0x400)        
  Max Waves Per CU:        40(0x28)             
  Max Work-item Per CU:    2560(0xa00)          
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32                   
  Packet Processor uCode:: 730                  
  SDMA engine uCode::      58                   
  IOMMU Support::          None                 
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    4194304(0x400000) KB
      Allocatable:             TRUE             
      Alloc Granule:           4KB              
      Alloc Alignment:         4KB              
      Accessible by all:       FALSE            
    Pool 2
      Segment:                 GLOBAL; FLAGS:   
      Size:                    4194304(0x400000) KB
      Allocatable:             TRUE             
      Alloc Granule:           4KB              
      Alloc Alignment:         4KB              
      Accessible by all:       FALSE            
    Pool 3
      Segment:                 GROUP            
      Size:                    64(0x40) KB      
      Allocatable:             FALSE            
      Alloc Granule:           0KB              
      Alloc Alignment:         0KB              
      Accessible by all:       FALSE            
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx803
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE 
      Default Rounding Mode:   NEAR             
      Default Rounding Mode:   NEAR             
      Fast f16:                TRUE             
      Workgroup Max Size:      1024(0x400)      
      Workgroup Max Size per Dimension:
        x                        1024(0x400)    
        y                        1024(0x400)    
        z                        1024(0x400)    
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32               
*** Done ***

>>> uname -a
Linux hostname 6.6.7-zen1-1-zen #1 ZEN SMP PREEMPT_DYNAMIC Thu, 14 Dec 2023 03:45:20 +0000 x86_64 GNU/Linux
```


---

### 评论 #11 — nartmada (2024-01-17T23:15:08Z)

Internal ticket has been created to track the investigation.  

---

### 评论 #12 — darren-amd (2024-12-06T16:23:40Z)

Hi @949f45ac,

A fix for this was deployed in ROCm 6.3. Could you please upgrade your ROCm version and let me know if the issue persists? Thanks!

---
