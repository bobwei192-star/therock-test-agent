# Why Create 3 compute queues and 2 SDMA queues in  calculation program?

> **Issue #911**
> **状态**: closed
> **创建时间**: 2019-10-17T07:40:27Z
> **更新时间**: 2023-08-07T16:11:11Z
> **关闭时间**: 2023-08-07T16:08:53Z
> **作者**: yaxroger
> **标签**: Question, Informational
> **URL**: https://github.com/ROCm/ROCm/issues/911

## 标签

- **Question** (颜色: #cc317c)
- **Informational** (颜色: #c5def5)

## 描述

1.  I wrote a simple opencl calculation program, input two arrays (a, b), perform "a + b = c" calculation, when it actually run, I found that it will generate 3 calculation queues, but there are not any AQL packages in the second compute queue, because these queues actually correspond to hardware resources. If not necessary, i think it will waste hardware resources. Is there any consideration for this design?

2. The above opencl calculation program will generate two SDMA queues, one copy from the host to the device, and one from the device to the host. From my actual operation, there is no difference between the two queues. Can I use a queue? Because my usage scenario is relatively simple, what are the considerations for using two queues or what application scenarios?

Thank you 

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2023-08-07T16:08:53Z)

Hi @yaxroger -- I'm sorry for the long delay in responding to this ticket. The underling reason behind the creation of this number of queues is because different layers of our software stack each create some queues independently of other layers. For example, in a simple OpenCL application, our [ROCclr](https://github.com/ROCm-Developer-Tools/clr/tree/rocm-5.6.0/rocclr) runtime layer will create an HSA queue for the cl_command_queue that you are enqueueing kernels to. If you create more cl_command_queue structures, ROCclr may create more underling HSA queues, up to the limit set by the environment variable [GPU_MAX_HW_QUEUES](https://github.com/ROCm-Developer-Tools/clr/blob/rocm-5.6.0/rocclr/utils/flags.hpp#L202). After reaching that number of HSA queues, the ROCclr runtime will start mapping new cl_command_queue structures to previously existing HSA queues. We do not guarantee an architecture for that mapping; in other words, we reserve the right to change that mapping at any time.

The other two queues you are observing likely come from the [ROCr runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime/tree/rocm-5.6.0). The ROCr runtime [creates up to two HSA queues per device for its own internal usage](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L701). [One is used for host->device "blit kernel" transfers](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L719), while the other us a "utility" queue that is used for [device->host "blit kernels"](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L721), [local-device-to-local-device copies](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L713), sending in packets that [invalidate instruction caches when new code objects are loaded](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L1728), and [peer-to-peer device transfer "blit kernels"](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L724).

Now, you may note that instead of using "blit" copy kernels, we could instead use the SDMA engines (a.k.a. the copy engines, or hardware engines specifically built for copying data from one location to another). A first thing to note is that these engines are not designed to do copies from local GPU memory (e.g., HBM, GDDR) to local GPU memory -- they will not achieve the kind of bandwidth that a blit/copy kernel will achieve. So the local-local copies will fall through to blit kernels.

Similarly, [some of our hardware will not be able to use SDMA engines due to hardware issues](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L669). We have [an environment variable](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/util/flag.h#L86) that allows you to disable the usage of SDMA engines.

In addition, our SDMA engines can only have a limited number of simultaneous queues (some only have 2 queues, others have 8). When we are out of SDMA queues, [our driver can NAK the request](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_blit_sdma.cpp#L184) of an application to create a new SDMA queue. If the [runtime does not receive an SDMA queue when it asks for one](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_gpu_agent.cpp#L685), it will fall back to blit kernels.

All of this taken together means that we may end up with even very simple applications using 3 HSA queues and 2 SDMA queues:

1. HSA queue from ROCr for host->device copy kernels
2. HSA queue from ROCr for device->host copy kernels and other utility functions like cache flushing and device->device copy kernels
3. HSA queue from ROCclr for your application-level command queues
4. SDMA queue from ROCr for host->device copies
5. SDMA queue from ROCr for device->host copies

These queues should generally be created lazily, meaning we only create the queue when we're about to use it. That may not have been the case when you asked this question in 2019 (I don't remember).

We currently use two separate queues for copies (one for H->D and one for D->H) so that we can overlap transfers in both directions. If we put both transfers in the queue at the same time, we would serialize such execution. Generally, this would limit the ability of programmers to do triple buffering (e.g., copying result0 to host while calculating result1 and copying input2 to the device, all in parallel). As such, we currently don't allow a way to limit the number of ROCr-internal queues except for disabling SDMA usage through the environment variable `HSA_ENABLE_SDMA=0`. ROCclr allows limiting the number of HSA queues it attempts to use through the `GPU_MAX_HW_QUEUES` environment variable; this variable is currently set to 4 by default.

---
