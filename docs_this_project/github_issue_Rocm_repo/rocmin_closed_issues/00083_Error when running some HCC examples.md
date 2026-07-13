# Error when running some HCC examples

- **Issue #:** 83
- **State:** closed
- **Created:** 2017-01-30T03:47:14Z
- **Updated:** 2017-07-02T17:22:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/83

I was running some example code from the repo of HCC-Example-Applications. Besides the problem that some of the applications do not compile, the MD example generates a segment fault. I tried to use GDB to figure out where the error is 
```
Thread 1 "MD" received signal SIGSEGV, Segmentation fault.
0x00007ffff64e04af in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
(gdb) bt
#0  0x00007ffff64e04af in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#1  0x00007ffff64df9ba in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffff675f023 in HSADispatch::waitComplete() () from /opt/rocm/hcc-lc/lib/libmcwamp_hsa.so
#3  0x00007ffff6761690 in std::__1::__deferred_assoc_state<void, std::__1::__async_func<HSADispatch::dispatchKernelAsync(Kalmar::HSAQueue*, void const*, int, bool)::{lambda()#1}> >::__execute() () from /opt/rocm/hcc-lc/lib/libmcwamp_hsa.so
#4  0x00007ffff7b62484 in std::__1::__assoc_sub_state::wait() () from /usr/lib/x86_64-linux-gnu/libc++.so.1
#5  0x00007ffff67571ec in Kalmar::HSAQueue::wait(Kalmar::enums::hcWaitMode) () from /opt/rocm/hcc-lc/lib/libmcwamp_hsa.so
#6  0x000000000042965a in hc::accelerator_view::wait(Kalmar::enums::hcWaitMode) ()
#7  0x000000000041820b in MD<float>::run(std::__1::vector<hc::short_vector::float_4, std::__1::allocator<hc::short_vector::float_4> >&) ()
#8  0x0000000000414561 in main ()
```
My own C++ HC programs suffer from the same problem. It was running well before upgrading to ROCm 1.4. I suspect it is related to wating for the completion_future object. 