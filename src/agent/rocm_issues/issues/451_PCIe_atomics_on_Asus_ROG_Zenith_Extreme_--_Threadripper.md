# PCIe atomics on Asus ROG Zenith Extreme -- Threadripper

> **Issue #451**
> **状态**: closed
> **创建时间**: 2018-07-07T02:12:37Z
> **更新时间**: 2018-10-09T14:06:26Z
> **关闭时间**: 2018-09-19T15:25:10Z
> **作者**: chromakey-io
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/451

## 描述

Hi again.

I can't seem to get PCIe atomics to tell me they are working on my new threadripper setup.  Here's the output from rocm/opecl/bin/clinfo

    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0

It isn't throwing any errors with kfd like it did the older drivers, but I'm thinking maybe that's because a change in the drivers?

Aaany-who.  I think I've gone through the motherboard's options with a fine tooth comb at this point and am not sure what else I can do ... so here I am :)  SVM, IOMMU, IOMMU-IVRS, PCIe-ARI enabled ...

Currently downloading tek's rocm-rippa 2 thing ... to see if I've somehow missed a kernel parameter or am missing some special sauce.


Other than that the drivers load and work just fine.  Though I'm seeing pretty much identical performance numbers (ethereum) as I did on my previous setup which was using 4x slots.... which I'm guessing is the atomics failing to do their magic.

---

## 评论 (24 条)

### 评论 #1 — gstoner (2018-07-07T15:03:18Z)

We run Threadripper internally.    Stock ROCm should run if you put a single GPU in x16 lane, Then  add in GPU 1 at time one you confrmed a working solution.   


The x4 lane could be PCIe Gen2 off a southbridge  which means it not not support PCIe Atomics 

.      

---

### 评论 #2 — robinchrist (2018-07-08T04:40:36Z)

I can confirm, that PCIe Atomics are not shown to be working by clinfo:
```
  SVM capabilities:                              
    Coarse grain buffer:                         Yes
    Fine grain Xbuffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No

```

Threadripper 1950X + ROG Zenith Extreme
VEGA FE placed in PCIE x16 Slot (Slot No. 3)

---

### 评论 #3 — chromakey-io (2018-07-08T05:23:47Z)

Yeah I'm realizing now this was a red-herring ... and things were actually working just fine.

Running the rocm-rippa thing now and see that he's been getting the higher ethereum numbers with the AMDGPU-Pro/RoCM stack rather than just the pure RoCM stack.  So that was a second bad way for me to be sanity testing that everything was in working order ... heh.

I also went back to 1.7.2 which I know throws a kernel error on boot if atomics are not working ... and didn't see the error there either.  So I'm pretty confident everything is working fine except for the clinfo reporting on Atomics...

---

### 评论 #4 — gstoner (2018-07-08T13:20:09Z)

@robinchrist The Atomic you see in CLinfo have nothing to do with PCIe Atomics - the really are Atomic Completors 

Here what they. are:; 
3 new PCIe transactions, each of which carries out a specific Atomic Operation (“AtomicOp”) on a target location in Memory Space. The 3 AtomicOps are FetchAdd (Fetch and Add), Swap (Unconditional Swap), and CAS (Compare and Swap). FetchAdd and Swap support operand sizes of 32 and 64 bits. CAS supports operand sizes of 32, 64, and 128 bits.

Endpoints and Root Ports may serve as Requesters for AtomicOps. PCIe Functions with Memory Space BARs as well as all Root Ports may serve as Completers for AtomicOp Requests. Routing elements (Switches, as well as Root Complexes supporting peer-to-peer access between Root Ports) require modification in order to route AtomicOp Requests. AtomicOps are architected for device-to-host, device- to-device, and host-to-device transactions.



---

### 评论 #5 — gstoner (2018-07-08T13:21:58Z)

OpenCL has Atomic fuction support part of the spec again independent of PCIe Atomics 

https://www.khronos.org/registry/OpenCL/sdk/1.2/docs/man/xhtml/atomicFunctions.html

Description
These functions provide atomic operations on 32-bit signed, unsigned integers and single precision floating-point to locations in __global or __local memory. Only the atomic_xchg operation is supported for single precision floating-point data type.

The atomic built-in functions that use the atom_ prefix and are described in the OpenCL Extension Specification and are enabled by: cl_khr_global_int32_base_atomics, cl_khr_global_int32_extended_atomics, cl_khr_local_int32_base_atomics, and cl_khr_local_int32_extended_atomics in sections 9.5 and 9.6 of the OpenCL 1.0 specification are also supported. .

The 64-bit transactions are atomic for the device executing these atomic functions. There is no guarantee of atomicity if the atomic operations to the same memory location are being performed by kernels executing on multiple devices.



---

### 评论 #6 — robinchrist (2018-07-08T13:29:36Z)

Hmm,
clinfo refers to `CL_DEVICE_SVM_ATOMICS` for the atomic information, the doc (from OpenCL 2.0!) says
`CL_DEVICE_SVM_ATOMICS – Support for the OpenCL 2.0 atomic operations that provide memory consistency across the host and all OpenCL devices supporting fine-grain SVM allocations.`

Arent't the SVM_ATOMICs (which guarantee `consistency across the host and all OpenCL devices supporting fine-grain SVM allocations`) related to the PCIe atomics?

---

### 评论 #7 — gstoner (2018-07-08T15:28:07Z)

Remember there are three types of SVM in OpenCL   You see Cross Device Atomics is optional in OpenCL spec.   It Cross Device Atomics which PCIe Atomic aka Atomic Completor help, since alow GPU to do atomic operatoration CPU memory directly with out CPU intervention.     We still can do Atomic operations on the GPU without PCIe atomics 

Note all the miner are asking us to remove PCIe Atomic supprt so they can us low end CPU with PCIeGen 2 and low end PCIe switches. 

Right now ROCr support Fine-Grained Buffer SVM with dGPU, you need APU or Gen8 Intel GPU/CPU to support Fine Grained System SVM. 

- Coarse-Grained buffer SVM: Sharing occurs at the granularity of regions of OpenCL buffer memory objects. Cross-device atomics are not supported.
- Fine-Grained buffer SVM: Sharing occurs at the granularity of individual loads and stores within OpenCL buffer memory objects. Cross-device atomics are optional.
- Fine-Grained system SVM: Sharing occurs at the granularity of individual loads/stores occurring anywherewithin the host memory. Cross-device atomics are optional.

---

### 评论 #8 — chromakey-io (2018-07-09T10:03:57Z)

>Note all the miner are asking us to remove PCIe Atomic supprt so they can us low end CPU with PCIeGen 2 and low end PCIe switches.

Isn't this kind of silly though?  My understanding was the very reason these drivers were more performant was due to the use of these new features.

If anyone is curious though I did manage to get about a 10% boost with the RoCM stack.  What's odd is that without BIOS modifications the amdgpu-pro stack seems to have about a 10% advantage (tested with the "rocm-ripp v2" setup).  So 18mh/s on an RX570-4g with RoCM stock bios vs. 21mh/s amdgpu-pro.

Where-as with BIOS mods I'm seeing 28mh/s with RoCM and 24-26mh/s with amdgpu-pro.  A nice little bump for sure, though not quite the 30-40mh/s tekcomm managed, but maybe he's referring to 2 cards? lol

I'm guessing the amdgpu-pro stack has some differences in power management and that jazz, which would explain the differences in stock-BIOS performance?

Any-way, now it's time to actually start learning how to use this machine with tensorflow so I can start harvesting facebook data and swaying election results... joking ... actually hoping to work on some fin-tech stuff ... we'll see :)

---

### 评论 #9 — e-c-d (2018-09-07T08:46:39Z)

@kevin 

I'd like to offer a dissenting opinion. I have a RX580, and three desktops none of which supports PCIe atomics. To get a version of OpenCL higher than 1.1 (as provided by Mesa), I have the following options:

- Use the closed-source AMDGPU-PRO driver. (Bad, and from what I understand, deprecated.)
- Spend four digits on a brand new computer.
- Spend three or four digits on a replacement graphics card.

I'm still unclear as to how the PCIe atomics are used (yes, even after reading `More-about-how-ROCm-uses-PCIe-Atomics.rst`) so the following may be completely ignorant/wrong. If PCIe atomics are not available, isn't it possible to fall back on relying on the CPU for synchronization purposes, at some cost in latency/speed?

I'm not trying to mine cryptocurrency, I just want to experiment with accelerating scientific/numerical computation. Being able to use the hardware I have, even inefficiently, is *highly preferable* to not being able to use it at all.


---

### 评论 #10 — chromakey-io (2018-09-19T10:04:41Z)

@e-c-d ...

have you _tried_ to use the RoCM drivers?  If you have a 8 or 16x Gen3 slot I'd at least give it a shot.

>Use the closed-source AMDGPU-PRO driver. (Bad, and from what I understand, deprecated.)

The pro stack is still the officially supported driver stack from AMD.  They literally *just* published new drivers in August ... so it is still _fully_ supported ... and offers support for Vulkan and all that fancy stuff.

>Spend four digits on a brand new computer.

A used celeron CPU and motherboard shouldn't set you back more than $100.

If you want the bleeding edge drivers that aren't even officially supported by Linux or AMD yet though ... you can't really _expect_ your 10 year old hardware to work.  Really even if it was the official driver stack (and not one targeting the professional/corporate/science sectors) you have to expect that at some point your hardware will be deprecated.

If you have a career in analytics or maths/science it won't be the last time you spend money to keep up with changing software and technology ... and I doubt it's the first.

---

### 评论 #11 — jlgreathouse (2018-09-19T14:56:24Z)

Hi @kevin -- just a note that I've slightly edited your post to remove some language that we would prefer not be used on this public form. In addition, I should note that ROCm is an official AMD software platform and we do work with the upstream Linux kernels as of ROCm 1.9 and Linux 4.17. :) That said, this official support statement does come with caveats on the hardware we will enable in ROCm, as detailed in [our documentation](https://github.com/RadeonOpenCompute/ROCm#hardware-support).

Finally, to be fair to @e-c-d -- it's possible to go out right now and buy CPUs that don't support PCIe atomics (for instance, AMD's Kaveri/Godavari and Carrizo/Bristol APUs). I'll reiterate that we support _some_ but not _all_ ROCm-enabled GPUs on these platforms. But we definitely understand how it can be disappointing that a relatively new CPU purchase does not work with your GPU of choice on the ROCm software stack. That's one of the reason why we worked to enable an optional mode for gfx9 GPUs so that they can work without PCIe atomics.

---

### 评论 #12 — jlgreathouse (2018-09-19T14:57:10Z)

To give a slightly more in-depth answer to @e-c-d about why we require PCIe atomics on some platforms: this is a side effect of one of the very basic technologies at the root of ROCm -- user-level enqueue of work to the GPU (and user-level memory messaging between the CPU and GPU). Traditional accelerator models require applications to go to the kernel driver every time they want to send a command to the GPU. So if you wanted to launch a computational kernel, or if you wanted to start a data transfer between the host and the device, you would have to send that request to the kernel driver, and that driver would then send a request to the device through mechanisms like memory-mapped I/O writes.

With [user-level enqueue of work](https://www.slideshare.net/hsafoundation/hsa-queuing-hot-chips-2013), you can avoid a lot of the "user->kernel->user" mode transitions. This allows you to submit work to the GPU faster, which can especially help reduce the latency for small pieces of work. Originally, HSA was supported on AMD devices that shared a physical memory system between the CPU and the GPU. So writing into that queue by one device, and reading from that queue on another device, could be done with atomic operations in the memory controller.

However, when we transitioned to ROCm, we wanted to get this benefit of HSA while working with discrete GPUs which sit on the other side of a PCIe bus. As such, we needed some way for the CPU and GPU to synchronize when they are working on these user-level queues that sit in CPU memory. Otherwise, you might end up with (for example) the CPU writing data into a queue while the GPU is also trying to write data into that queue (for things like [HSA signals](http://www.hsafoundation.com/html/Content/Runtime/Topics/01_Intro/signals_and_packet_launch.htm)). As such, we added the requirement that the CPU and GPU access these queues using PCIe atomics. In this way, we could prevent the two devices from breaking HSA queues and you could get the performance benefit of user-level queues on discrete GPUs.

However, based on feedback from the community, we saw that many users wanted to run ROCm on hardware that doesn't fully support PCIe atomics. For example, crypto miners may want to install many GPUs in a single box using cheaper PCIe switches to increase physical density. Others, like @e-c-d, want to use existing computers to try out cool ROCm technologies like our support for TensorFlow.

As such, we worked with our hardware and firmware teams to come up with a solution that allows us to still work with user-level queues while avoiding PCIe atomics. Doing this adds extra overhead to accessing these queues; I can't go into the details of how this is done, but it trades off _some_ of the performance benefits of user-level queues to enable these devices to run on systems that do not support PCIe atomics. We detect whether your system supports atomics or not and enable this mode if it does not.

Performing these changes took quite a bit of internal development effort. And as such, we have only been able to add such features to a subset of our supported GPUs --  in particular, gfx9 (with early development work done to bring up experimental support for "Hawaii" GPUs). I cannot guarantee that we will be able to get this capability working on gfx8 GPUs, so for now those devices still require PCIe atomics to work within the ROCm software stack.

I hope this helps give some context to these requirements, why they exist, and what we are doing.

---

### 评论 #13 — jlgreathouse (2018-09-19T15:25:10Z)

Finally, as of ROCm 1.9 anyway, I know that the amdkfd automatically tests for PCIe atomics. On devices that support PCIe atomics, it will use them. If your devices supports operation without PCIe atomics, it should avoid using them. If your device requires PCIe atomics but your platform does not support them, it will not enable that device.

We also have directed tests for this in the in-development [ROCm Validation Suite](https://github.com/ROCm-Developer-Tools/ROCmValidationSuite).

Note that, as @gstoner mentioned, all of this is orthogonal to OpenCL fine-grained SVM atomics. This is a separate, optional part of OpenCL shared virtual memory that allows multiple devices that are sharing an SVM region to use atomics. This may require PCIe atomics if you wanted to implement it on discrete GPUs -- I've never built such a system so I couldn't tell you for sure.

At this time, I don't believe our OpenCL runtime supports fine-grained SVM atomics, even on systems that have PCIe atomics.

It sounds like the underlying issues brought up the OP have been solved, answered, or bypassed, so I'm going to go ahead and close this issue. :)

---

### 评论 #14 — e-c-d (2018-09-20T01:18:36Z)

First, I want to thank you for replying to me in such detail. I understand that my request is *not* actually within the scope of this project, and you wouldn't be wrong to stop answering me whenever. So thank you.

> Traditional accelerator models require applications to go to the kernel driver every time they want to send a command to the GPU. So if you wanted to launch a computational kernel, or if you wanted to start a data transfer between the host and the device, you would have to send that request to the kernel driver, and that driver would then send a request to the device through mechanisms like memory-mapped I/O writes.

How does the kernel avoid synchronization issues then? If it is writing to a queue on the dGPU that is also being accessed/written-to by the dGPU, that could very well cause problems. Is the kernel driver writing to some MMIO addresses that userspace doesn't/shouldn't have access to for security reasons?

> With user-level enqueue of work, you can avoid a lot of the "user->kernel->user" mode transitions. This allows you to submit work to the GPU faster, which can especially help reduce the latency for small pieces of work. Originally, HSA was supported on AMD devices that shared a physical memory system between the CPU and the GPU. So writing into that queue by one device, and reading from that queue on another device, could be done with atomic operations in the memory controller.

That makes sense in the HSA view that the GPU is a sort of big SIMD coprocessor that the CPU can call upon for every little thing it needs done. My use case is different (and maybe not within your project's goals) in that the tasks are typically very large, and the task submission overhead (context switch) is negligible compared to the task itself. I wouldn't call upon the GPU to multiply two 4x4 matrices :).

> However, when we transitioned to ROCm, we wanted to get this benefit of HSA while working with discrete GPUs which sit on the other side of a PCIe bus. As such, we needed some way for the CPU and GPU to synchronize when they are working on these user-level queues that sit in CPU memory. Otherwise, you might end up with (for example) the CPU writing data into a queue while the GPU is also trying to write data into that queue (for things like HSA signals).

It must be possible to somehow achieve synchronization between CPU and GPU without GPU-initiated atomic ops, otherwise the traditional accelerator models you referenced above wouldn't work. Something must therefore be different in the ROCm model you described. Is the difference that the command queue sits in CPU memory instead of GPU memory (as it is normally the case in the 'traditional model')? If I understand correctly from reading related documentation, there's an asymmetry in that PCIe devices may have trouble with atomic ops (e.g. pre-PCIe 3), but the CPU can *always* initiate atomic operations.

> The pro stack is still the officially supported driver stack from AMD. They literally just published new drivers in August ... so it is still fully supported ... and offers support for Vulkan and all that fancy stuff.

Sorry, I'm one of those people who refuse to run closed source software. AMDGPU-PRO is not an option for me. :(

Are there any plans to enable OpenCL >1.1 on platforms not supporting ROCm? The Mesa Clover stack is getting quite outdated. I see that someone has hacked Clover [to use the proprietary AMDGPU-PRO shader compiler](https://github.com/matszpk/mesa3d-comp-bridge), would it be possible to do a similar thing but instead use ROCm's compiler?

---

### 评论 #15 — jlgreathouse (2018-09-20T02:22:31Z)

Hi @e-c-d 

> How does the kernel avoid synchronization issues then? If it is writing to a queue on the dGPU that is also being accessed/written-to by the dGPU, that could very well cause problems. Is the kernel driver writing to some MMIO addresses that userspace doesn't/shouldn't have access to for security reasons?

Let me start by saying that you're pretty quickly running up against the edges of my expertise how work was traditionally shipped to GPUs. I've spent my time in the GPU world mostly working in the HSA/ROCm stack. I haven't written any classic graphics drivers or work that piggybacks on those classic drivers. :)

That said, [this series of blog posts](https://mynameismjp.wordpress.com/2018/03/06/breaking-down-barriers-part-1-whats-a-barrier/) may prove educational towards how classic graphics stacks interact with the GPU. You're going through a kernel driver to launch GPU work; that kernel driver can ensure synchronization with all other CPU cores, and yes, the reads and writes to the GPU can use MMIO writes that are in regions not accessible by user-space. This prevents users from sending work to the device at bad times, preventing a lot of random hardware lockups. 

A common way to set up work to be queued to the GPU might be to set up a new buffer in memory, fill it with commands for the GPU, then point the GPU's command processor to that buffer. The GPU then owns that command buffer until it's done with the work, so it knows no one else will access it. Thus the writes can be done while the CPU "owns the lock" and the reads can be done one the GPU "owns the lock".

On the other hand, in the HSA world, any HSA agent in the system (including the GPU) can write work into a command buffer at any time. In addition, work can come with signal dependencies -- e.g. "don't start kernel C until kernel B on GPU0 and kernel C on GPU1 have completed". In this example, GPUs 0 and 1 would both write their completion signals and could therefore be modifying data in multiple other queues while other devices are trying to read them.

It's really a lot more complicated than this, internally. But suffice it to say, user-level queues, HSA signal dependency tracking, and synchronization between compute units, SDMA engines, etc. ends up relying pretty heavily on PCIe atomics in our software stack since the internal state of queues can be much more dynamic than "write once on the CPU, read on the GPU till it's drained".

Going into all of the details of how this works would, unfortunately, require both a tremendous amount of time, and would describe a lot of information about our on-chip firmware. The company would be severely unhappy if I were to do that. :)


> That makes sense in the HSA view that the GPU is a sort of big SIMD coprocessor that the CPU can call upon for every little thing it needs done. My use case is different (and maybe not within your project's goals) in that the tasks are typically very large, and the task submission overhead (context switch) is negligible compared to the task itself. I wouldn't call upon the GPU to multiply two 4x4 matrices :).

We have found that this is still useful even in "big jobs on big GPUs". Our MIOpen team makes heavy use of both large and small kernels as they port machine learning frameworks for our hardware. For instance, you may have a large amount of data on the GPU. Yes, you'll throw some giant convolution kernels onto the device. As part of the training loop, you'll have many steps with a bunch of small 1x1 convolution kernels that run very quickly. Even if those small/fast kernels don't take full advantage of the GPU, it's faster to run them on the GPU than to copy a bunch of data back to the host just to do the computation there.

I'm sure you've seen similar cases in HPC (I know I have). And if those small kernels can be enqueued more rapidly, you can help make them more efficient.

> Are there any plans to enable OpenCL >1.1 on platforms not supporting ROCm? The Mesa Clover stack is getting quite outdated. I see that someone has hacked Clover [to use the proprietary AMDGPU-PRO shader compiler](https://github.com/matszpk/mesa3d-comp-bridge), would it be possible to do a similar thing but instead use ROCm's compiler?

I can't speak towards any other plans AMD has for other software stacks. However, at this time our primary development efforts in compare are the open source ROCm stack and the semi-closed amdgpu-pro stack (which still runs on top of the open amdgpu driver).

---

### 评论 #16 — e-c-d (2018-09-20T10:16:18Z)

Thanks for replying to my annoying messages!

> On the other hand, in the HSA world, any HSA agent in the system (including the GPU) can write work into a command buffer at any time. In addition, work can come with signal dependencies -- e.g. "don't start kernel C until kernel B on GPU0 and kernel C on GPU1 have completed". In this example, GPUs 0 and 1 would both write their completion signals and could therefore be modifying data in multiple other queues while other devices are trying to read them.

There are no synchronization issues for HSA agents that submit to their own queues, but only when they write to *other* agents' queues. In that case, the CPU could be used as a synchronization arbitrator. For example, let's say GPU0 wants to write to a queue on GPU1 (or possibly the CPU itself, but let's use GPU1 for sake of the example). GPU0 adds the packet it wants to send to its outgoing queue (along with an ID for its destination), then raises an interrupt to get the kernel's attention. The kernel driver copies the packet from GPU0's outgoing queue to one of GPU1's incoming queues, then writes to some MMIO to tell GPU1 to check that incoming queue. All messages thus go through the kernel; this adds extra latency and inefficiency, but could nonetheless serve as a generic fallback for non-PCIe-atomics systems. And even with that latency and inefficiency, I think it would still be faster to use the GPU to accelerate computation than not to use it at all.

> It's really a lot more complicated than this, internally. But suffice it to say, user-level queues, HSA signal dependency tracking, and synchronization between compute units, SDMA engines, etc. ends up relying pretty heavily on PCIe atomics in our software stack since the internal state of queues can be much more dynamic than "write once on the CPU, read on the GPU till it's drained".

Of course, I'm just making things up, and what I described may be extremely difficult to accomplish given your current code. Also not really within the scope of the project. But still I think a lot of (financially-challenged) people would find great value in such a feature.

> Yes, you'll throw some giant convolution kernels onto the device. As part of the training loop, you'll have many steps with a bunch of small 1x1 convolution kernels that run very quickly. Even if those small/fast kernels don't take full advantage of the GPU, it's faster to run them on the GPU than to copy a bunch of data back to the host just to do the computation there.

That's a good point! But if you use a single OpenCL command queue (without the out-of-order flag, so that each work item must finish before the next one begins), wouldn't it be possible to queue up all of those small 1x1 convolution kernels at once (and do just 1 context switch instead of 1 context switch per work item)?

> and the semi-closed amdgpu-pro stack (which still runs on top of the open amdgpu driver).

Are there plans on opening up the OpenCL part (so, the compiler) of the semi-closed amdgpu-pro stack? Given the mesa3d-comp-bridge project, it seems that that's the only component needed.


---

### 评论 #17 — jlgreathouse (2018-09-20T14:18:31Z)

Hi @e-c-d 

Let me try to head off a potentially long and iterative discussion here by saying that the things I am describing in my posts are examples of _some_ of the reasons this is hard. They are not fully inclusive of all of the difficulties with removing PCIe atomics from our requirements. I want to be clear on this point, because at some point in the future someone will wander into this thread and, based on a very literal reading of the posts so far, incorrectly think "This single example issue described sounds easy to fix. Why does AMD not do this already? They are the worst and so lazy". :)

I am obviously not going to describe every difficulty in enough detail like this such that you will solve the issues entirely. To begin with, even architecting the actual solution would involve information about our on-chip firmware-based controllers that we do not share with the public.

That said:
> There are no synchronization issues for HSA agents that submit to their own queues, but only when they write to _other_ agents' queues.

This is not true. [HSA Signals](http://www.hsafoundation.com/html/Content/SysArch/Topics/02_Details/req_signaling_and_synchronization.htm) make this more complex thank you think. HSA agents are required to have a set of atomic operations that can be used to modify the value in the signals (unlike traditional Unix signals, these are not simple binaries).

As _non-inclusive_ examples that I just came up with off the top of my head: you could have the command processor of a GPU waiting for a signal to be met, but the [compute units on the device update the values in those signals](https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/43#issuecomment-423043229). The compute command processor may want to update the signal that a DMA engine is waiting on (or vice versa); both may be on the GPU, but they're potentially different parallel units of hardware. While these examples may or may not be a problem in our GPUs, I hope that this illustrates some reasons why HSA queues and signaling is a relatively intricate topic that requires quite a bit of work in the hardware, firmware, and drivers to get right.

> In that case, the CPU could be used as a synchronization arbitrator. For example, let's say GPU0 wants to write to a queue on GPU1 (or possibly the CPU itself, but let's use GPU1 for sake of the example). GPU0 adds the packet it wants to send to its outgoing queue (along with an ID for its destination), then raises an interrupt to get the kernel's attention. The kernel driver copies the packet from GPU0's outgoing queue to one of GPU1's incoming queues, then writes to some MMIO to tell GPU1 to check that incoming queue. All messages thus go through the kernel; this adds extra latency and inefficiency, but could nonetheless serve as a generic fallback for non-PCIe-atomics systems. And even with that latency and inefficiency, I think it would still be faster to use the GPU to accelerate computation than not to use it at all.

I'll admit that I'm not going to spend a whole lot of time debugging a hypothetical situation. :) Let's imagine that this solution works (though I don't believe it covers all of the cases we require in the real world). You've now signed the driver development team up to basically re-implement the current user-level code that we handle in things like [ROCr](https://github.com/RadeonOpenCompute/ROCR-Runtime) as well as new mechanisms for juggling synchronization between multiple hardware units.

In addition, what used to be a "simple" update into a memory location for the firmware suddenly becomes a complicated dance that also involves the driver and synchronization with various user-level libraries. Maybe it's possible (again, I'm not going to spend a lot of time figuring it out for this particular made-up example). If we imagine that it is, I would posit that it would require a not-insignificant amount of development effort across multiple teams, it would require a great deal of validation effort, and we now need to maintain this entirely separate code-path for non-atomic (legacy) hardware. These are precisely the kinds of things that I brought up earlier as examples of why we have not currently built a "non-atomics" path for gfx8.

And to hopefully head off another question such as "why don't you just avoid all the user-level stuff entirely, ignore HSA queues, don't use HSA signals, don't bother with AQL packets?" -- AMD has a path that does this. amdgpu-pro. :)

> That's a good point! But if you use a single OpenCL command queue (without the out-of-order flag, so that each work item must finish before the next one begins), wouldn't it be possible to queue up all of those small 1x1 convolution kernels at once (and do just 1 context switch instead of 1 context switch per work item)?

Yes, if possible GPU developers *should* try to asynchronously enqueue work to the device while other work is going on. However, the ability to asynchronously enqueue work while a previous kernel is in flight is obviously dependent on the algorithm itself. It's also potentially dependent on the _data_, not just the algorithm. A few examples off the top of my head:
- How many iterations of a breadth-first search of a graph should you asynchronously enqueue? The number of iterations and the amount of work per iteration [directly depends on the graph](http://www.computermachines.org/joe/publications/pdfs/asbd2014_power.pdf)
- Sparse linear algebra algorithms can have highly variable amount of work per kernel invocation, and they are often used in iterative methods. How many iterations does it take for these methods to converge? How many kernels should you enqueue?

> Are there plans on opening up the OpenCL part (so, the compiler) of the semi-closed amdgpu-pro stack? Given the mesa3d-comp-bridge project, it seems that that's the only component needed.

The majority of our [OpenCL runtime](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime) is shared between open and closed source releases. I've honestly never looked through the code in enough depth to tell you the differences between what we use in ROCm and what would run on top of amdgpu-pro. Not that I could tell you exactly what the internals of the latter look like in any case.

---

### 评论 #18 — e-c-d (2018-09-21T06:17:56Z)

Hi @jlgreathouse 

Thanks for explaining everything, and good call preemptively answering the literal-minded reader.

I didn't realize HSA provides such rich signaling primitives. I have to say all of this is very exciting, although maybe not enough to drop half a salary on a Vega or a new motherboard+CPU; maybe in a year or two after prices go down a bit, although given the cryptocurrency mining frenzy, who knows. I'll try scavenging around the local second-hand market, maybe someone's getting rid of a recent desktop that happens to have a PCIe3+atomics slot.

> And to hopefully head off another question such as "why don't you just avoid all the user-level stuff entirely, ignore HSA queues, don't use HSA signals, don't bother with AQL packets?" -- AMD has a path that does this. amdgpu-pro. :)

That would indeed work for me (since I don't mind the extra inefficiency, at least for now). But amdgpu-pro is, sadly, still closed source.

> > Are there plans on opening up the OpenCL part (so, the compiler) of the semi-closed amdgpu-pro stack? Given the mesa3d-comp-bridge project, it seems that that's the only component needed.

> The majority of our OpenCL runtime is shared between open and closed source releases.

Well, that's *extremely* encouraging. Should I try to take this up with the amdgpu-pro people and plead my case for opening up whatever is left of the OpenCL runtime part? (Or could you please do so on my behalf, since you actually work there?) Since Clover is quite outdated, and ROCm doesn't quite work for everyone, it would be very nice to have a(n open source) fallback OpenCL solution to replace Clover. I can also try comparing the OpenCL runtime binaries provided by ROCm and amdgpu-pro, although that would likely be pointless (aside from putting a number to the claim "only x% of the stack is still closed source, we're so close!").

(I bet you regret giving me false hope now.)


---

### 评论 #19 — briansp2020 (2018-09-21T13:11:26Z)

> although maybe not enough to drop half a salary on a Vega or a new motherboard+CPU;

I just picked up a (supposedly new) Vega FE from eBay for less than $500 (https://www.ebay.com/itm/AMD-Radeon-Vega-Frontier-Edition-GPU-Mining-New-16GB/372435649677?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2060353.m2749.l2649). You can also buy new Vega 56 from e-tailers for a bit more than $400 (https://www.bestbuy.com/site/xfx-amd-radeon-rx-vega-56-8gb-hbm2-pci-express-3-0-graphics-card/6183041.p?skuId=6183041&ref=199&loc=AKGBlS8SPlM&acampID=1&siteID=AKGBlS8SPlM-3KAszmaTeJZnWVcibkCV5A).

Mining seems to be dead for now and AMD's next gen card doesn't look like it will be affordable for some time after it is released. So, if you want to experiment with AMD's ROCm software stack, this looks like a good time to pick up Vega graphics card.

BTW, does AMD plan to release Vega FE like card based on 7nm Vega? Do you plan to call it Vega Fe? :)


---

### 评论 #20 — briansp2020 (2018-09-21T13:15:59Z)

Newegg has cheaper Vega 56 at $380 after rebate (https://www.newegg.com/Product/Product.aspx?Item=N82E16814131740&ignorebbr=1&nm_mc=AFC-C8Junction&cm_mmc=AFC-C8Junction-VigLink-_-na-_-na-_-na&cm_sp=&AID=10446076&PID=6163686&SID=jmc11mcujj011rh100053).

---

### 评论 #21 — jlgreathouse (2018-09-21T16:39:11Z)

Hi @e-c-d 

I honestly can't give you any information or recommendations with respect to our closed-source components. I do not work on those teams, and they have thought through their business concerns in a lot more depth than I have -- and I couldn't publicly describe their internal business considerations even if I did know them.

I'll say that we put a lot of work into getting the OpenCL runtime open for the ROCm software stack, and this involved re-implementing the part of the runtime that talks to our drivers (because the ROCm/HSA "drivers" work very differently than other stacks, as discussed in this thread). Any parts that interfaces with non-ROCm drivers has not gone through such processes. For example: our internal codebase obviously hooks into our closed-source Windows drivers so that OpenCL works on Windows. I would guess that this isn't going to be open sourced no matter what, and that could potentially make it hard to open the parts of our code-base that talk to our closed-source Linux driver components.

I would sincerely appreciate it if you were to not associate our conversations with any requests you might make. "Hey, @jlgreathouse told me $foo, so you should open source your software!" is likely to correspond to "jlgreathouse answering issues is causing more work for other teams." and would lead me to stop responding to ROCm questions in this relatively open and candid manner. I appreciate interacting with and getting feedback from our users, and hopefully my posts give some insight into our team's decisions. That said, it's a problem as soon as those discussions start causing problems for *other* teams.

---

### 评论 #22 — e-c-d (2018-09-22T06:12:15Z)

@briansp2020

I'm in Canada. The Vega 56 you linked on newegg is 480 USD here. The absolute cheapest right now is 460 USD. I've found a second hand Vega 56 at 380 USD with 27 remaining months of warranty, and I'll sell my RX 580 once I receive that.

That said, just because I've 'fixed' my problem doesn't mean I'm any less interested in seeing better open source OpenCL support for non-ROCm hardware!

@jlgreathouse

> Any parts that interfaces with non-ROCm drivers has not gone through such processes. For example: our internal codebase obviously hooks into our closed-source Windows drivers so that OpenCL works on Windows. I would guess that this isn't going to be open sourced no matter what, and that could potentially make it hard to open the parts of our code-base that talk to our closed-source Linux driver components.

Well, it depends where those parts are. It seems that the OpenCL runtime inside amdgpu-pro can *already* run on top of the open source amdgpu driver (because some people do exactly that!). It looks like llvm trunk already has target triples for amdhsa/ROCm, amdpal, *and mesa3d*, so at the very least it may be possible to update the C compiler and codegen in Clover without huge amounts of work. OpenCL >1.1 provides a lot of extra memory management/synchronization, which may require some work (to replace the beautiful HSA calls with awful slowpaths).

> I would sincerely appreciate it if you were to not associate our conversations with any requests you might make.

Of course! I would hate to cause you any trouble, especially when you've been so delightfully helpful!

---

### 评论 #23 — chromakey-io (2018-10-09T07:25:29Z)

sorry for the course language.  I grew up in NJ ... and sometimes it's hard not to chanel Torvalds in tech discussions ... I try my best not to but it often seeps through despite my best efforts.


Aaanny-who.  I really had a very cursory understanding of the underpinnings of the RoCM stack before this thread and just wanted to thank you guys for enlightening me of all the nitty gritty underpinnings and how all this magical stuff comes to together.

Thanks ... sincerely.

---

### 评论 #24 — jlgreathouse (2018-10-09T14:06:26Z)

No worries, I just wanted to note why I edited a few words in your post. Hopefully the explanations are helpful. I write these posts so that folks can learn more about our open software and hardware stack. I'm excited about it -- hopefully I can get others excited about it too. :)

---
