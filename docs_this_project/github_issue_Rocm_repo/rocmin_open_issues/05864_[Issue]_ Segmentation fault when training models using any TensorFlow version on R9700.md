# [Issue]: Segmentation fault when training models using any TensorFlow version on R9700

- **Issue #:** 5864
- **State:** open
- **Created:** 2026-01-17T02:46:04Z
- **Updated:** 2026-03-18T12:48:06Z
- **Labels:** status: assessed
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5864

### Problem Description

I consistently get a segmentation error when training TensorFlow models on an AMD Radeon AI PRO R9700 under Linux. This may be related to issue #5718, but I additionally get a segmentation fault with both TensorFlow versions 2.19.1 and 2.18.1. This occurs on bare metal in addition to under Docker. I have also attempted a fresh install of Ubuntu Server 24.04 and ROCm 7.1.1 with the same result. ROCm 6.4.3 was also tried. I have not yet found a combination that avoids this issue.



### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

AMD Ryzen Threadripper 3960X

### GPU

AMD Radeon AI PRO R9700

### ROCm Version

ROCm 7.1.1

### ROCm Component

HIP

### Steps to Reproduce

This issue can be reproduced simply by running the MNIST example posted at https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html and increasing the number of epochs to 100. The failure point happens within the same epoch for a given session. This happens for other models as well.

```
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
predictions = model(x_train[:1]).numpy()
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100)
model.evaluate(x_test,  y_test, verbose=2)
```

When running with gdb, the seg fault originates from libamdhip64.so.7. The full stack trace and logs are in the additional information section.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module version 6.16.6 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.14
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen Threadripper 3960X 24-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper 3960X 24-Core Processor
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
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            48                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    49155112(0x2ee0c28) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    49155112(0x2ee0c28) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    49155112(0x2ee0c28) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    49155112(0x2ee0c28) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-11ac8a4bc02c5165               
  Marketing Name:          AMD Radeon AI PRO R9700            
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
    L1:                      32(0x20) KB                        
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30033(0x7551)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2350                               
  BDFID:                   8960                               
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 108                                
  SDMA engine uCode::      662                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    31309824(0x1ddc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1201         
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*** Done *** 
```

### Additional Information

**gdb stack trace:**
```
Thread 149 "python3" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffbc27fc6c0 (LWP 18258)]
0x00007ffff1e5136f in ?? () from /opt/rocm/lib/libamdhip64.so.7
(gdb) bt
#0  0x00007ffff1e5136f in ?? () from /opt/rocm/lib/libamdhip64.so.7
#1  0x00007ffff1e51f64 in ?? () from /opt/rocm/lib/libamdhip64.so.7
#2  0x00007ffff1ad2734 in ?? () from /opt/rocm/lib/libamdhip64.so.7
#3  0x00007ffff1ad06a2 in ?? () from /opt/rocm/lib/libamdhip64.so.7
#4  0x00007ffff1b0c5cd in ?? () from /opt/rocm/lib/libamdhip64.so.7
#5  0x00007ffff600d27b in stream_executor::gpu::RocmCommandBuffer::UpdateKernelNode(stream_executor::gpu::GpuCommandBuffer::GraphNodeHandleOpaque*, stream_executor::ThreadDim const&, stream_executor::BlockDim const&, stream_executor::Kernel const&, stream_executor::KernelArgsPackedArrayBase const&)
    () from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#6  0x00007ffff6012f26 in stream_executor::gpu::GpuCommandBuffer::LaunchWithPackedArgs(tsl::gtl::IntType<stream_executor::CommandBuffer::ExecutionScopeId_tag_, unsigned long>, stream_executor::ThreadDim const&, stream_executor::BlockDim const&, stream_executor::Kernel const&, stream_executor::KernelArgsPackedArrayBase const&) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#7  0x00007ffff60131b1 in stream_executor::gpu::GpuCommandBuffer::Launch(tsl::gtl::IntType<stream_executor::CommandBuffer::ExecutionScopeId_tag_, unsigned long>, stream_executor::ThreadDim const&, stream_executor::BlockDim const&, stream_executor::Kernel const&, stream_executor::KernelArgs const&)
    () from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#8  0x00007fffd273e5a2 in xla::gpu::LaunchCmd::Record(xla::gpu::Thunk::ExecuteParams const&, xla::gpu::CommandBufferCmd::RecordParams const&, stream_executor::CommandBuffer*) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#9  0x00007fffd273b656 in xla::gpu::CommandBufferCmdSequence::Record(xla::gpu::Thunk::ExecuteParams const&, xla::gpu::CommandBufferCmd::RecordParams const&, stream_executor::CommandBuffer*, xla::gpu::CommandBufferCmdSequence::RecordMode) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#10 0x00007fffd27381ff in xla::gpu::CommandBufferThunk::ExecuteOnStream(xla::gpu::Thunk::ExecuteParams const&) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#11 0x00007fffd38c479c in xla::gpu::SequentialThunk::ExecuteOnStream(xla::gpu::Thunk::ExecuteParams const&) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#12 0x00007fffd38becb4 in xla::gpu::(anonymous namespace)::ExecuteThunks(xla::DebugOptions const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, xla::gpu::SequentialThunk&, xla::gpu::Thunk::ExecutableSource, xla::ServiceExecutableRunOptions const*, xla::gpu::BufferAllocations const&, bool, absl::lts_20230802::flat_hash_set<tsl::gtl::IntType<xla::gpu::ExecutionStreamId_tag_, unsigned long>, absl::lts_20230802::hash_internal::Hash<tsl::gtl::IntType<xla::gpu::ExecutionStreamId_tag_, unsigned long> >, std::equal_to<tsl::gtl::IntType<xla::gpu::ExecutionStreamId_tag_, unsigned long> >, std::allocator<tsl::gtl::IntType<xla::gpu::ExecutionStreamId_tag_, unsigned long> > > const&) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#13 0x00007fffd38bbd12 in xla::gpu::GpuExecutable::ExecuteAsyncOnStreamImpl(xla::ServiceExecutableRunOptions const*, std::variant<absl::lts_20230802::Span<xla::ShapedBuffer const* const>, absl::lts_20230802::Span<xla::ExecutionInput> >) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#14 0x00007fffd38ba70d in xla::gpu::GpuExecutable::ExecuteAsyncOnStream(xla::ServiceExecutableRunOptions const*, std::vector<xla::ExecutionInput, std::allocator<xla::ExecutionInput> >) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
--Type <RET> for more, q to quit, c to continue without paging--c
#15 0x00007fffdda784df in xla::Executable::ExecuteAsyncOnStreamWrapper(xla::ServiceExecutableRunOptions const*, std::vector<xla::ExecutionInput, std::allocator<xla::ExecutionInput> >) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#16 0x00007fffd455e8d9 in xla::LocalExecutable::RunAsync(absl::lts_20230802::Span<xla::Shape const* const>, std::vector<xla::ExecutionInput, std::allocator<xla::ExecutionInput> >, xla::ExecutableRunOptions) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#17 0x00007fffd455f01e in xla::LocalExecutable::RunAsync(std::vector<xla::ExecutionInput, std::allocator<xla::ExecutionInput> >, xla::ExecutableRunOptions) () from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#18 0x00007fffd3b49262 in tensorflow::(anonymous namespace)::RunExecutable(tensorflow::XlaPlatformInfo const&, tensorflow::XlaComputationLaunchContext const&, std::vector<xla::ExecutionInput, std::allocator<xla::ExecutionInput> >, xla::ExecutableRunOptions, xla::LocalExecutable*, tensorflow::OpKernelContext*, stream_executor::DeviceMemoryAllocator*) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#19 0x00007fffd3b54216 in std::_Function_handler<void (), tensorflow::XlaLocalLaunchBase::ComputeAsync(tensorflow::OpKernelContext*, std::function<void ()>)::$_1>::_M_invoke(std::_Any_data const&) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#20 0x00007fffd3b428b0 in tensorflow::XlaLocalLaunchBase::ComputeAsync(tensorflow::OpKernelContext*, std::function<void ()>) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_cc.so.2
#21 0x00007ffff504099b in tensorflow::BaseGPUDevice::ComputeAsync(tensorflow::AsyncOpKernel*, tensorflow::OpKernelContext*, std::function<void ()>)
    () from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#22 0x00007ffff514610b in tensorflow::(anonymous namespace)::ExecutorState<tensorflow::PropagatorState>::Process(tensorflow::PropagatorState::TaggedNode const&, long) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#23 0x00007ffff604b045 in Eigen::ThreadPoolTempl<tsl::thread::EigenEnvironment>::WorkerLoop(int) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#24 0x00007ffff604a211 in void std::__invoke_impl<void, tsl::thread::EigenEnvironment::CreateThread(std::function<void ()>)::{lambda()#1}&>(std::__invoke_other, tsl::thread::EigenEnvironment::CreateThread(std::function<void ()>)::{lambda()#1}&) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#25 0x00007ffff54d4cfa in tsl::(anonymous namespace)::PThread::ThreadFn(void*) ()
   from /home/loheac/Projects/complex/venv/lib/python3.12/site-packages/tensorflow/python/platform/../../libtensorflow_framework.so.2
#26 0x00007ffff7c9caa4 in start_thread (arg=<optimized out>) at ./nptl/pthread_create.c:447
#27 0x00007ffff7d29c6c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78
```

**Log emitted by ROCm with AMD_LOG_LEVEL=4 at the failure point:**
```
GB1_GRPM1_GRVW1_GSU1_GSUASB_GLS0_ISA000_IU1_K1_KLS_LBSPPA0_LBSPPB0_LPA0_LPB0_LDL1_LRVW1_LWPMn1_LDW0_FMA_MIAV0_MDA2_MO40_MMFSC_MKFGSU256_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR1_PLR1_PKA0_SIA1_SLW1_SS0_SU32_SUM0_SUS256_SCIUI1_SPO0_SRVW0_SSO0_SVW2_SNLL0_TSGRA0_TSGRB0_TT2_2_TLDS0_UMLDSA0_UMLDSB0_U64SL1_USFGRO0_VAW1_VS1_VW1_VWB1_VFLRP0_WSGRA0_WSGRB0_WS64_WG16_16_1_WGM8
:3:hip_graph.cpp            :1913: 32130193118 us: [pid:39416 tid: 0x71a40bfff6c0]  hipGraphExecKernelNodeSetParams ( 0x7198ca566060, 0x7198d6903100, 0x71a40bffa708 ) 
:4:rocvirtual.cpp           :792 : 32130193132 us: [pid:39416 tid: 0x71a40bfff6c0] Arg0:   = ptr:0x719bff2a0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193141 us: [pid:39416 tid: 0x71a40bfff6c0] Arg1:   = ptr:0x719bfd2a0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193150 us: [pid:39416 tid: 0x71a40bfff6c0] Arg2:   = ptr:0x719bfb18fa00 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193159 us: [pid:39416 tid: 0x71a40bfff6c0] Arg3:   = ptr:0x719c00cf4400 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193169 us: [pid:39416 tid: 0x71a40bfff6c0] Arg4:   = ptr:0x719bfe2a0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:3:rocvirtual.cpp           :3503: 32130193178 us: [pid:39416 tid: 0x71a40bfff6c0] ShaderName : input_reduce_select_fusion_3
:3:hip_graph.cpp            :1931: 32130193186 us: [pid:39416 tid: 0x71a40bfff6c0] hipGraphExecKernelNodeSetParams: Returned hipSuccess : 
:3:hip_graph.cpp            :1913: 32130193197 us: [pid:39416 tid: 0x71a40bfff6c0]  hipGraphExecKernelNodeSetParams ( 0x7198ca566060, 0x71a3c3b83540, 0x71a40bffa708 ) 
:4:rocvirtual.cpp           :792 : 32130193211 us: [pid:39416 tid: 0x71a40bfff6c0] Arg0:   = ptr:0x719bfaf88f00 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193220 us: [pid:39416 tid: 0x71a40bfff6c0] Arg1:   = ptr:0x719bffaa0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:3:rocvirtual.cpp           :3503: 32130193229 us: [pid:39416 tid: 0x71a40bfff6c0] ShaderName : loop_complex_fusion_5
:3:hip_graph.cpp            :1931: 32130193237 us: [pid:39416 tid: 0x71a40bfff6c0] hipGraphExecKernelNodeSetParams: Returned hipSuccess : 
:3:hip_graph.cpp            :1982: 32130193247 us: [pid:39416 tid: 0x71a40bfff6c0]  hipGraphExecChildGraphNodeSetParams ( 0x7198ca566060, 0x71a3c2da2470, 0x7198c974d900 ) 
:4:rocvirtual.cpp           :792 : 32130193262 us: [pid:39416 tid: 0x71a40bfff6c0] Arg0:   = ptr:0x719bff2a0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193272 us: [pid:39416 tid: 0x71a40bfff6c0] Arg1:   = ptr:0x719bff2a0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193283 us: [pid:39416 tid: 0x71a40bfff6c0] Arg2:   = ptr:0x719bffaa0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :792 : 32130193292 us: [pid:39416 tid: 0x71a40bfff6c0] Arg3:   = ptr:0x719bfe2a0400 obj:[0x719bfaa00000-0x71a3bfe00000]
:4:rocvirtual.cpp           :882 : 32130193301 us: [pid:39416 tid: 0x71a40bfff6c0] Arg4:   = val:0x3f800000 (size:0x8)
:4:rocvirtual.cpp           :882 : 32130193308 us: [pid:39416 tid: 0x71a40bfff6c0] Arg5:   = val:0x0 (size:0x8)
:4:rocvirtual.cpp           :882 : 32130193314 us: [pid:39416 tid: 0x71a40bfff6c0] Arg6:   = val:0x200 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193321 us: [pid:39416 tid: 0x71a40bfff6c0] Arg7:   = val:0x0 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193328 us: [pid:39416 tid: 0x71a40bfff6c0] Arg8:   = val:0x200 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193335 us: [pid:39416 tid: 0x71a40bfff6c0] Arg9:   = val:0x0 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193342 us: [pid:39416 tid: 0x71a40bfff6c0] Arg10:   = val:0x200 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193349 us: [pid:39416 tid: 0x71a40bfff6c0] Arg11:   = val:0x0 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193355 us: [pid:39416 tid: 0x71a40bfff6c0] Arg12:   = val:0x200 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193362 us: [pid:39416 tid: 0x71a40bfff6c0] Arg13:   = val:0x0 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193369 us: [pid:39416 tid: 0x71a40bfff6c0] Arg14:   = val:0x200 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193376 us: [pid:39416 tid: 0x71a40bfff6c0] Arg15:   = val:0x400 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193382 us: [pid:39416 tid: 0x71a40bfff6c0] Arg16:   = val:0x1 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193389 us: [pid:39416 tid: 0x71a40bfff6c0] Arg17:   = val:0x200 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193396 us: [pid:39416 tid: 0x71a40bfff6c0] Arg18:   = val:0xf (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193403 us: [pid:39416 tid: 0x71a40bfff6c0] Arg19:   = val:0x10 (size:0x4)
:4:rocvirtual.cpp           :882 : 32130193410 us: [pid:39416 tid: 0x71a40bfff6c0] Arg20:   = val:0x20 (size:0x4)
:3:rocvirtual.cpp           :3503: 32130193416 us: [pid:39416 tid: 0x71a40bfff6c0] ShaderName : Cijk_Alik_Bljk_CB_MT32x32x8_SN_1LDSB0_APM1_ABV0_ACED0_AF0EM1_AF1EM1_AMAS0_ASE_ASGT_ASLT_ASM_ASAE01_ASCE01_ASEM1_AAC0_BL0_BS1_CLR0_DTLA0_DTLB0_DTVA0_DTVB0_DVO0_ETSP_EPS0_ELFLR0_EMLL0_FSSC10_FL0_GLVWA1_GLVWB1_GRCGA1_GRCGB1_GRPM1_GRVW1_GSU1_GSUASB_GLS0_ISA000_IU1_K1_KLS_LBSPPA0_LBSPPB0_LPA0_LPB0_LDL1_LRVW1_LWPMn1_LDW0_FMA_MIAV0_MDA2_MO40_MMFSC_MKFGSU256_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR1_PLR1_PKA0_SIA1_SLW1_SS0_SU32_SUM0_SUS256_SCIUI1_SPO0_SRVW0_SSO0_SVW2_SNLL0_TSGRA0_TSGRB0_TT2_2_TLDS0_UMLDSA0_UMLDSB0_U64SL1_USFGRO0_VAW1_VS1_VW1_VWB1_VFLRP0_WSGRA0_WSGRB0_WS64_WG16_16_1_WGM8
:4:rocdevice.cpp            :2186: 32130196219 us: [pid:39416 tid: 0x71a40bfff6c0] Allocate hsa device memory (nil), size 0x29b00, hsa_mem_flags 0x4h
:1:rocdevice.cpp            :2190: 32130196231 us: [pid:39416 tid: 0x71a40bfff6c0] Fail allocation local memory
Segmentation fault (core dumped)
```