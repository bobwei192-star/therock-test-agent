# OpenCL application stuck when waiting for the completion of Radeon vii GPU buffer copy

> **Issue #802**
> **状态**: closed
> **创建时间**: 2019-05-21T01:30:33Z
> **更新时间**: 2023-12-21T14:34:08Z
> **关闭时间**: 2023-12-21T14:34:08Z
> **作者**: modernv5
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/802

## 描述


Radeon VII GPU : OpenCL application stuck when waiting for the completion of GPU buffer copy.

We ran Black-Scholes and other OpenCL tests on Radeon VII GPU of Huawei server with ROCm 2.3 (kernel 5.0). The programs were stuck on executing clEnqueueWriteBuffer or clEnqueueReadBuffer very frequently. We traced a OpenCL program and ROCm codes，the flow path of clEnqueueReadBuffer (the path depends on the amount of data, we take big size as an example )is shown as: 
clEnqueueReadBuffer -> readBuffer -> copyBuffer -> hsaCopy-> has_amd_async_copy -> DmaCopy -> SubmitLinearCopyCmmand ->PopulateQueue.

The program is stuck after submitting copy command in the function “hsacCopy”, because it waits for the finish of copy by keeping checking whether a completion signal becomes from 1 to 0 in the function“hsa_signal_wait_acquire(completion_signal_, HSA_SIGNAL_CONDITION_EQ,0,uint64_t(-1),HSA_WAIT_STATE_BLOCKED)”. According to our observation, the completion signal doesn’t change to 0, so the program is trapped in a syscall “kfd_ioctl_wait_events” of“hsaKmtWaitOnMultipleEvents”.

My questions are followed by: 
1) When the packet of the copy command is consumed by a packet process in a GPU, how the result of the packet is returned ?  which one in which way change the value of completion signal in ROCK Kernel Driver so that application is informed that the signal value minus to zero by atomic::Load(&signal_.value) in ROCR-Runtime ? 

2) What are possible reasons that the program stuck in “kfd_ioctl_wait_events” in the kernel driver? It is obvious that the event is not activated or waked up?  Even the activation failed, why does it not return to the user space when time out?

I’m so confused by these questions. 

Clinfo of OpenCL platform is shown as following:
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.0 AMD-APP.internal.dbg (2862.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 20
  Device Topology:				 PCI[ B#51, D#0, F#0 ]
  Max compute units:				 60
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1802Mhz
  Address bits:					 64
  Max memory allocation:			 14588628172
  Image support:				 No
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 17163091968
  Constant buffer size:				 14588628172
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 1703726284
  Max global variable size:			 14588628172
  Max global variable preferred total size:	 17163091968
  Max read/write image args:			 0
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0xffffb7acb568
  Name:						 gfx906+sram-ecc
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2862.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 



---

## 评论 (2 条)

### 评论 #1 — tasso (2023-12-18T18:59:37Z)

Is this issue still reproducible?  If not, can you please close it?  Thanks!

---

### 评论 #2 — tasso (2023-12-21T14:34:08Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---
