# [Issue]: Freeze with 100% usage

- **Issue #:** 2715
- **State:** closed
- **Created:** 2023-12-14T20:53:12Z
- **Updated:** 2024-05-26T03:15:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/2715

### Problem Description

When trying to move a buffer to GPU, the code freezes with 100% CPU usage in hsa library (probably an infinite loop).
I use ArchLinux and the problem disappears, when using `linux-lts` (older) kernel.
When debugging with GDB, i get following info (when i interrupt the program in the 100% usage state):

```
(gdb) r
Starting program: /usr/bin/python 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
Python 3.11.6 (main, Nov 14 2023, 09:36:21) [GCC 13.2.1 20230801] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> t = torch.tensor([0.1, 0.5])
>>> c = t.to('cuda')
[New Thread 0x7ffeb02296c0 (LWP 11107)]
[New Thread 0x7ffeafa286c0 (LWP 11108)]
[Thread 0x7ffeafa286c0 (LWP 11108) exited]
^C
Thread 1 "python" received signal SIGINT, Interrupt.
0x00007fff4e6501d1 in rocr::core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libhsa-runtime64.so
(gdb) bt
#0  0x00007fff4e6501d1 in rocr::core::InterruptSignal::WaitRelaxed(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libhsa-runtime64.so
#1  0x00007fff4e65006a in rocr::core::InterruptSignal::WaitAcquire(hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libhsa-runtime64.so
#2  0x00007fff4e643d49 in rocr::HSA::hsa_signal_wait_scacquire(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libhsa-runtime64.so
#3  0x00007fff88c0ad45 in roctracer::hsa_support::detail::hsa_signal_wait_scacquire_callback(hsa_signal_s, hsa_signal_condition_t, long, unsigned long, hsa_wait_state_t) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libroctracer64.so
#4  0x00007fffa66a8b83 in bool roc::WaitForSignal<false>(hsa_signal_s, bool, bool) () from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#5  0x00007fffa669fd68 in roc::VirtualGPU::HwQueueTracker::CpuWaitForSignal(roc::ProfilingSignal*) () from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#6  0x00007fffa66ce13d in roc::DmaBlitManager::hsaCopyStaged(unsigned char const*, unsigned char*, unsigned long, unsigned char*, bool) const ()
   from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#7  0x00007fffa66cffc7 in roc::DmaBlitManager::writeBuffer(void const*, device::Memory&, amd::Coord3D const&, amd::Coord3D const&, bool, amd::CopyMetadata) const ()
   from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#8  0x00007fffa66d026b in roc::KernelBlitManager::writeBuffer(void const*, device::Memory&, amd::Coord3D const&, amd::Coord3D const&, bool, amd::CopyMetadata) const ()
   from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#9  0x00007fffa66a0c79 in roc::VirtualGPU::submitWriteMemory(amd::WriteMemoryCommand&) () from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#10 0x00007fffa667761a in amd::Command::enqueue() () from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#11 0x00007fffa65239a0 in ihipMemcpy(void*, void const*, unsigned long, hipMemcpyKind, hip::Stream&, bool, bool) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#12 0x00007fffa65684c0 in hipMemcpyWithStream () from /usr/lib/python3.11/site-packages/torch/lib/libamdhip64.so
#13 0x00007fffa863c97a in at::native::copy_kernel_cuda(at::TensorIterator&, bool) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_hip.so
#14 0x00007fffdecb43bf in at::native::copy_impl(at::Tensor&, at::Tensor const&, bool) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#15 0x00007fffdecb56f2 in at::native::copy_(at::Tensor&, at::Tensor const&, bool) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#16 0x00007fffdf98ea1f in at::_ops::copy_::call(at::Tensor&, at::Tensor const&, bool) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#17 0x00007fffdef843c5 in at::native::_to_copy(at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#18 0x00007fffdfd2069b in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::WrapFunctionIntoFunctor_<c10::CompileTimeFunctionPointer<at::Tensor (at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>), &at::(anonymous namespace)::(anonymous namespace)::wrapper_CompositeExplicitAutograd___to_copy>, at::Tensor, c10::guts::typelist::typelist<at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat> > >, at::Tensor (at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>)>::call(c10::OperatorKernel*, c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#19 0x00007fffdf489fb5 in at::_ops::_to_copy::redispatch(c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#20 0x00007fffdfb4fd03 in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::WrapFunctionIntoFunctor_<c10::CompileTimeFunctionPointer<at::Tensor (at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>), &at::(anonymous namespace)::_to_copy>, at::Tensor, c10::guts::typelist::typelist<at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat> > >, at::Tensor (at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>)>::call(c10::OperatorKernel*, c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#21 0x00007fffdf489fb5 in at::_ops::_to_copy::redispatch(c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#22 0x00007fffe121d94f in torch::autograd::VariableType::(anonymous namespace)::_to_copy(c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#23 0x00007fffe121defe in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::WrapFunctionIntoFunctor_<c10::CompileTimeFunctionPointer<at::Tensor (c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>), &torch::autograd::VariableType::(anonymous namespace)::_to_copy>, at::Tensor, c10::guts::typelist::typelist<c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat> > >, at::Tensor (c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>)>::call(c10::OperatorKernel*, c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#24 0x00007fffdf5114de in at::_ops::_to_copy::call(at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#25 0x00007fffdef7bd1b in at::native::to(at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#26 0x00007fffdfef8a41 in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::WrapFunctionIntoFunctor_<c10::CompileTimeFunctionPointer<at::Tensor (at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, bool, c10::optional<c10::MemoryFormat>), &at::(anonymous namespace)::(anonymous namespace)::wrapper_CompositeImplicitAutograd_dtype_layout_to>, at::Tensor, c10::guts::typelist::typelist<at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, bool, c10::optional<c10::MemoryFormat> > >, at::Tensor (at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, bool, c10::optional<c10::MemoryFormat>)>::call(c10::OperatorKernel*, c10::DispatchKeySet, at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, bool, c10::optional<c10::MemoryFormat>) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#27 0x00007fffdf6a6183 in at::_ops::to_dtype_layout::call(at::Tensor const&, c10::optional<c10::ScalarType>, c10::optional<c10::Layout>, c10::optional<c10::Device>, c10::optional<bool>, bool, bool, c10::optional<c10::MemoryFormat>) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so
#28 0x00007ffff56a2308 in torch::autograd::dispatch_to(at::Tensor const&, c10::Device, bool, bool, c10::optional<c10::MemoryFormat>) ()
   from /usr/lib/python3.11/site-packages/torch/lib/libtorch_python.so
#29 0x00007ffff56ff0d4 in torch::autograd::THPVariable_to(_object*, _object*, _object*) () from /usr/lib/python3.11/site-packages/torch/lib/libtorch_python.so
#30 0x00007ffff7a058a5 in ?? () from /usr/lib/libpython3.11.so.1.0
#31 0x00007ffff79f2987 in PyObject_Vectorcall () from /usr/lib/libpython3.11.so.1.0
#32 0x00007ffff79e4c23 in _PyEval_EvalFrameDefault () from /usr/lib/libpython3.11.so.1.0
#33 0x00007ffff7a9c484 in ?? () from /usr/lib/libpython3.11.so.1.0
#34 0x00007ffff7a9be6c in PyEval_EvalCode () from /usr/lib/libpython3.11.so.1.0
#35 0x00007ffff7ab9fc3 in ?? () from /usr/lib/libpython3.11.so.1.0
#36 0x00007ffff7ab63ea in ?? () from /usr/lib/libpython3.11.so.1.0
#37 0x00007ffff79be02a in ?? () from /usr/lib/libpython3.11.so.1.0
#38 0x00007ffff79be2f2 in _PyRun_InteractiveLoopObject () from /usr/lib/libpython3.11.so.1.0
#39 0x00007ffff793556b in ?? () from /usr/lib/libpython3.11.so.1.0
#40 0x00007ffff79be417 in PyRun_AnyFileExFlags () from /usr/lib/libpython3.11.so.1.0
#41 0x00007ffff792fc28 in ?? () from /usr/lib/libpython3.11.so.1.0
#42 0x00007ffff7a8e79b in Py_BytesMain () from /usr/lib/libpython3.11.so.1.0
#43 0x00007ffff7645cd0 in ?? () from /usr/lib/libc.so.6
#44 0x00007ffff7645d8a in __libc_start_main () from /usr/lib/libc.so.6
#45 0x0000555555555045 in _start ()
(gdb) 
```

Also, i see difference of `rocminfo` outputs on those two kernels (on the same computer). Looks like this (compared with `diff`):

```
11c11
< DMAbuf Support:          YES
---
> DMAbuf Support:          NO
49c49
<       Size:                    16305612(0xf8cdcc) KB              
---
>       Size:                    16306580(0xf8d194) KB              
56c56
<       Size:                    16305612(0xf8cdcc) KB              
---
>       Size:                    16306580(0xf8d194) KB              
63c63
<       Size:                    16305612(0xf8cdcc) KB              
---
>       Size:                    16306580(0xf8d194) KB     
```

Is there any known fix, or is that a bug?

### Operating System

ArchLinux amd64

### CPU

AMD Ryzen 3 2200G with Radeon Vega Graphics

### GPU

gfx803

### ROCm Version

5.7.0

### ROCm Component

_No response_

### Steps to Reproduce

Copy buffer GPU (using PyTorch library)

```python
import torch
t = torch.tensor([0.1, 0.3])
print("cuda")
c = t.cuda() #This line freezes whole process ()
# OR
c = t.to(torch.device('cuda:0'))
# OR
c = t.to('cuda:0')
```

### Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
=====================    
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
      Size:                    16305612(0xf8cdcc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16305612(0xf8cdcc) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16305612(0xf8cdcc) KB              
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

Update:
Also on the working LTS kernel, there is still problem with 100% CPU usage (,,only´´ for about 10 seconds, when moving to/from GPU after some chain of mathematical operations). That looks like a problem of sync implementation (using while loop (also without sleep function) eating CPU, instead of some `poll`/`epoll` syscall)