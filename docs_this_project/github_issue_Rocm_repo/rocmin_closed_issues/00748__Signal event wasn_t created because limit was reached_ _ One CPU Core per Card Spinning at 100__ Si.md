# "Signal event wasn't created because limit was reached" – One CPU Core per Card Spinning at 100%, Since ROCm 2.1

- **Issue #:** 748
- **State:** closed
- **Created:** 2019-03-20T19:47:55Z
- **Updated:** 2024-12-12T14:59:48Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/748

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