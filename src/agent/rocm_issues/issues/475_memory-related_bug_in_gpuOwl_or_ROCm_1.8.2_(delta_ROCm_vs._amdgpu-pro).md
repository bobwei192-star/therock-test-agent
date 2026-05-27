# memory-related bug in gpuOwl or ROCm 1.8.2? (delta ROCm vs. amdgpu-pro)

> **Issue #475**
> **状态**: closed
> **创建时间**: 2018-07-27T11:40:03Z
> **更新时间**: 2018-07-30T23:54:24Z
> **关闭时间**: 2018-07-30T23:21:58Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/475

## 描述

On Ubuntu 18.04, Kernel 4.15, Rx Vega64. Running gpuOwl https://github.com/preda/gpuowl .
When moving from amdgpu-pro 18.20 to ROCm 1.8.2, a new error surfaced.
I don't know if this error is caused by ROCm codegen, or by my incorrect understanding of the OpenCL memory model.

In the gpuOwl app https://github.com/preda/gpuowl
(to repro: checkout the source from github, "make openowl", enter a single line containing "80899661" (without quotes) in worktodo.txt , run ./openowl . The app self-checks the computation and reports EE error when the error is present)

So it was running rock-solid on amdgpu-pro 18.20, but a new reproducible error appeared when running on ROCm 1.8.2.

This commit seems to improve the situation (making the error less frequent, or removing it):
https://github.com/preda/gpuowl/commit/c602af285d72fd340a5da0f7d149a2e3d06da1e2

The fix consisted in marking a global buffer "volatile". This clearly changes the codegen, and may explain that the error is fixed. The question is, is this volatile in that commit needed for code correctness? (or is it just hiding a ROCm bug?)

Maybe an engineer with understanding of the OpenCL memory model would like to take a look. The write-read to that global buffer are separated by

void bigBar() { barrier(CLK_GLOBAL_MEM_FENCE | CLK_LOCAL_MEM_FENCE); }

so I would have thought that that is enough to ensure proper memory ordering and visibility (without the volatile).

If anybody wants to look at this and repro, I can assist with building and running the app.


---

## 评论 (13 条)

### 评论 #1 — b-sumner (2018-07-27T14:38:29Z)

The OpenCL 1.2 memory model does not provide any means to ensure visibility of a global write to device scope except at kernel termination, yet this code appears to assume that work groups can communicate between each other.

OpenCL of any version also does not provide much in the way of progress guarantees between work groups.  Just because one work group can observe that another work group has reached a certain point (in a race free manner using atomic operations) does not mean that the observer has a right to expect that the other work group will continue to make progress.

The kernel should at least be using OpenCL 2.0 atomics to explicitly release/acquire the desired data at the desired scope.  But this won't fix the lack of progress guarantees that the kernel is assuming.

---

### 评论 #2 — jlgreathouse (2018-07-27T19:11:39Z)

Let me start my response by saying that @b-sumner is completely right (he knows a lot more than me about this). If you are trying to write portable, standards-compliant OpenCL code, then your kernel is broken. OpenCL 1.x does not guarantee memory consistency in global memory between work groups in the same kernel (see, for instance, the [OpenCL 1.2 specification](https://www.khronos.org/registry/OpenCL/specs/opencl-1.2.pdf), Section 3.3.1).

OpenCL 2.0, as @b-sumner mentions, allows explicit marking of requested consistency for global memory atomics. See Section 3.3.4 of the [OpenCL 2.0 specification](https://www.khronos.org/registry/OpenCL/specs/opencl-2.0.pdf), for instance. As such, to write values that you want other workgroups to see, you may want to do an atomic_store_explicit(x, y, memory_order_release); and to see the values written by another workgroup, you may want to do atomic_load_explicit(x, y, memory_order_acquire). This will at least, from a standards perspective, guarantee proper memory consistency and that the writes from one WG can be seen by reads from another.

Two examples of why your current code may fail:

1. In AMD GCN GPUs, the L1 caches are *not* coherent with one another. As such, if workgroup N is on CU 0 and workgroup N+1 is on CU 1, the following situation could happen: a) workgroup N+1 has in its L1 cache the cache line that contains `carryShuttle[N] and carryShuttle[N+1]`. b) workgroup N attempts to write to `carryShuttle[N]`. It updates its own L1 cache line and updates the L2 cache. c) workgroup N+1 tries to read `carryShuttle[N]` but it gets the _old_ value from its L1 cache because the caches are not coherent with one another.
1. Workgroup N attempts to write to `carryShuttle[wg_id]` (meaning `carryShuttle[N]`) then it tries to set a flag using atomics. Workgroup N+1 reads the flag (again using atomics, so that the load goes out to the L2 cache). It then tries to read `carryShuttle[wg_id-1]`, meaning `carryShuttle[N]`. However, the compiler sees that `carryShuttle[wg_id]` and `carryShuttle[wg_id-1]` do not overlap, and so within a single workgroup it is perfectly legal to put the read before the write. Again, the specification says that this is OK because there is no consistency guaranteed between these reads from different workgroups.

If you properly demarcate your consistency requirements using OpenCL 2.0 atomics, the compiler will not perform this reordering (because acquires won't be hauled above releases). I believe our GPUs will also set a bit in the load and store instructions to force the accesses to go to our coherent L2s, removing the coherence problem I mention above.

Beyond that, to give a bit more detail to what @b-sumner is saying about progress guarantees: your code is making even more non-standards-compliant assumptions. In particular, you are assuming that you can write into a flag with workgroup N, and have workgroup N+1 read that updated flag. As far as thje OpenCL standard is concerned, the workgroups _do not_ need to be on the GPU at the same time, and they _need not_ be scheduled in order. Per the OpenCL 2.0 specification, section 3.2.1:

> ... the kernel-instance is launched and the work-groups associated with the kernel-instance are placed into a pool of “ready to execute” work-groups. This pool is called a work-pool. The work-pool may be implemented in any manner as long as it assures that work-groups placed in the pool will eventually execute.

An example of a perfectly legal GPU execution, as per the OpenCL spec, that would break your code:

- You try to launch your kernel to a GPU that, for some reason, can only run a single workgroup at a time. Let's set aside why this may happen, but it's still a legal configuration.
- The GPU then starts off execution by launching workgroup 10. Your kernel then attempts to spin-loop on ready[9]. However, workgroup 9 is not running at this time, and cannot run until workgroup 10 finishes (because the GPU can only fit one workgroup at a time).
- Your kernel now deadlocks and your application fails.

I'm writing up all these examples of why things may fail in various manners because your code is not standards complaint first to say that I agree with @b-sumner . AMD cannot guarantee that the code you've written will always run and produce correct results. That being said, I'll try to make a post shortly that explains some of the *non-standard* ways that you could potentially write your code so that it may do what you want.

I want to emphasize that the things I will discuss *are not standard compliant* and thus may break without warning. Changes in our GPU hardware, firmware, drivers, or software may break this code because the things I will describe are not standard. It's not AMD's fault if your code breaks after doing them, and it will be your responsibility to make sure that your code continues to work in the future. Thus, the techniques I will discuss may increase your code maintenance burden. In addition, these techniques may not work on GPUs from other vendors -- and (as mentioned) may not even work on future GPUs from AMD!

---

### 评论 #3 — jlgreathouse (2018-07-27T20:11:12Z)

Again, let me start this post by saying that the things I will describe here **are not standard OpenCL**. Please do not implement anything from this post and then submit a ticket saying that AMD's OpenCL is broken when the hack code doesn't work. These techniques require a somewhat deep knowledge of AMD's hardware, and I will say that I still get this stuff wrong quite often.

I'm writing this information down because, despite all warnings like what I've given above, folks will still continue to write non-standard code in an effort to increase the performance of their kernels. As such, I may as well describe what (hopefully) goes on underneath so that it's not all black magic.

First, my post above describes how you should probably be doing your reads and writes to carryShuttle. Use the OpenCL 2.0 `atomic_store()` and `atomic_load()` operations. If you want a big hammer, just use `atomic_store()` and `atomic_load()`. If you want to try to allow for some more compiler optimizations, used `atomic_store_explicit()` and `atomic_load_explicit()` with appropriate consistency requests (as shown above). You would want to set the memory scope to e.g. `memory_scope_device`.

Using the appropriate OpenCL 2.0 atomic operations here should prevent the compiler from reordering operations that load or store to this array of shared values. In addition, by setting the appropriate scope, the compiler will generate the proper store and load instructions that will go our to our GPU's coherence point.

AMD GCN GPUs have an L1 data cache within each parallel compute unit (CU). All of the workgroups that run on the CU share that L1 cache. However, as mentioned above, the L1 caches in different CUs are not coherent with one another. As such, a write from workgroups on one CU will not back-invalidate existing data in the L1 cache of another CU.

The coherence point in a GCN GPU is the L2 cache. As such, if a workgroup on one CU writes into the L2 cache and a workgroup on a second CU reads from that L2 cache, the second workgroup will see the newly updated value.  Atomic operations are performed in the L2 on GCN GPUs, so if you use an atomic operation, you can avoid this coherence problem. Up above, I described using OpenCL 2.0 `atomic_load()` and `atomic_store()` operations. However, if (for whatever reason) you want to stick with OpenCL 1.x syntax, you could *try* to use OpenCL 1.x atomics to force the proper memory coherence. **Big reminder that this is not OpenCL standard compliant**.

For instance, your write to `carryShuttle` could be replaced with `atomic_xchg(&carryShuttle[loc], new_val)`. Your read could be replaced with e.g. `carry = atomic_or(&carryShuttle[loc], 0)`. The compiler is less likely to reorder these atomic operations with one another (though it's not *guaranteed* to not reorder them in OpenCL 1.x), and the atomic operations will go to the L2 cache of GCN, so you won't have hardware caching difficulties.

Note that these 1.x atomic operations may run slower than the 2.0 `atomic_store()` and `atomic_load()` ops, because all of the OpenCL 1.x atomics are read-modify-write operations. What if you want to do a load that goes to the L2 cache to get the latest value? Vector memory operations in AMD GCN GPUs include a bit in the instruction, "GLC" (globally coherent), which can be used to force L1 bypassing policies. For reads, setting GLC causes the read to bypass the L1 and instead read the value from the L2 cache or global memory. For writes, the GLC bit causes the write to avoid the write-combining buffers, thus avoiding any memory ordering issues where you write X and Y, but only Y is in the L2 cache while X is still sitting in the buffer.

If I remember correctly, the OpenCL 2.0 `atomic_store()` and `atomic_load()` operations set these bits on regular stores and loads, since they do not need to use atomic read-modify-write semantics. However, if you're writing code specifically for AMD GPUs on the ROCm software stack, you could also potentially directly access the GLC bit using inline assembly instructions (which are **extremely** non-standards compliant. Inline assembly statements cause all kinds of headaches for compilers, so please don't blame me when other optimization steps in your kernel don't happen if you do this. :)

However, you could do something like `__asm__ __volatile__("global_load_dword %0 %1 glc\ns_waitcnt vmcnt(0)" : "=v"(read_variable) : "v"(&carryShuffle[offset]));` Note that this is especially fragile, as different GPUs may have slightly different syntax for performing such loads. Use inline assembly at your own peril.

---

### 评论 #4 — jlgreathouse (2018-07-27T20:31:58Z)

Please allow me to once again say that the things I will describe here **are not standard OpenCL**. If I don't say this in every post, I'm sure someone will read this and then complain when their code doesn't work like they want.

@b-sumner mentioned in his post that cross-workgroup synchronization, like what you're using the `ready[]` array for, is not supported in any OpenCL version. This is true, and I gave an example of how such code could break within the confines of the OpenCL standard.

That said, on basically every GPU I've ever tried, the type barrier you're implementing should work. In particular, if you are doing *one-way synchronization*, where workgroups with lower IDs "release" workgroups with higher IDs, you are unlikely to deadlock your GPU. Basically, any spin-loops should only wait on data that will be written by a workgroup with a lower ID.

One way to do this is to start your kernel with an atomic increment of some global "virtual workgroup ID" variable, so that whatever workgroup actually starts first (no matter its ID) will have `virtual_wgid=0`, the next one will have `virtual_wgid=1`, etc. In this way, you could avoid having, e.g. only workgroup 10 sitting on the GPU as per my example above. This is done by algorithms such as [StreamScan](https://dl.acm.org/citation.cfm?id=2442539) in the literature. I believe Nvidia also does this in their [CUB library's scan algorithm](http://research.nvidia.com/sites/default/files/publications/nvr-2016-002.pdf).

Actually, if you're content to focus your non-standards-compliant implementation on AMD hardware, I believe we will guarantee that workgroups will start up in increasing order (i.e., 0, then 1, then 2, etc.). As such, you don't even need to use a "virtual" workgroup ID.

ROCm is an implementation of many parts of the HSA standard on top of AMD's discrete GPUs. And the [HSA System Architecture Specification](http://www.hsafoundation.com/standards/) (See Section 2.11 of v1.2) says that "the ... work-group with the lowest flattened work-group ID ... must be active." This doesn't necessarily say that the oldest workgroup will continue to execute instructions, but this is a pretty safe assumption on existing AMD hardware.

As such, so long as you're not spin-looping and waiting for a value from a thread with a higher workgroup-ID, then you should be able to use the kind of inter-workgroup synchronization you're showing in your app. If, however, you try to make workgroup 0 wait on the value from workgroup 1, it may be the case that it will wait forever because workgroup 1 may not be able to fit onto the device at the same time that workgroup 0 is running. This "one-way synchronization" is the limit, unless you start *carefully* balancing workgroup occupancy, which is extremely device-specific and it absolutely no way portable.

**Again, note that my discussion here is about non-standard things. Please do not take my discussion as a guarantee that anything will work now or will continue to work in the future.**

---

### 评论 #5 — preda (2018-07-27T20:53:24Z)

Thank you @jlgreathouse and @b-sumner , this was a really helpful and great answer!

Concerning the workgroup progress, I am already using the "one-way synchronization", where group N  waits only on group N-1. So as long as the workgroups are started in order and continue executing, this will work even in the extreme case of only *one* workgroup being run at a time, as you describe.

Now I'm going to switch to OpenCL 2.0 with the proper atomics, and I'll report back.


---

### 评论 #6 — preda (2018-07-28T00:05:47Z)

In this commit I switched to using OpenCL 2.0 atomics:
https://github.com/preda/gpuowl/commit/dd0f2b219275a7771aa33aff3912fa332e2fe3a6
and now the volatile on carryShuttle is not needed anymore, naturally.

I still see an infrequent (hard to repro) error, which occurs about once per 2hours. (but such an error never happened with amdgpu-pro 18.20 in weeks of runtime, that's why I mention it; the GPU is not overclocked in any way, it runs at 79C and 150W, never had memory errors before, that's why I don't suspect a hardware error).

Anyway, if you're looking for a stress-test or regression test, you could use this app. It has the advantage that it has a very strong self-check (which is always on), which allows to detect any errors (RAM or compute) that might occur. It also displays performance stats.


---

### 评论 #7 — preda (2018-07-28T00:48:04Z)

Yep I confirm, a subtle error is still present. Since changing to CL2.0, running for 3h, the error was detected 4 times.

---

### 评论 #8 — preda (2018-07-28T13:45:41Z)

OK I have an idea about what the cause may be.

When the workgroup size is 64, the ROCm compiler completely discards both
barrier() and mem_fence() in all variants. (this in both OpenCL compilation modes, 1.x and 2.x)

Now, of course when workgroup-size is 64 the thread synchronization (part of barrier()) can be discarded. BUT the question is whether the memory fence (another part of barrier()) can be discarded as well... ?

Apparently the ROCm behavior in this situation differs from both amdgpu-pro, and from the behavior when WG > 64, when it appears the mem fences are handled correctly.


---

### 评论 #9 — preda (2018-07-28T14:02:36Z)

In OpenCL 2.x mode, the expected behavior is obtained by using
work_group_barrier(CLK_GLOBAL_MEM_FENCE, memory_scope_device)
or atomic_work_item_fence(...).

And, with the proper fence use, the writes/reads to carryShuttle don't need to be atomic.


---

### 评论 #10 — preda (2018-07-29T00:34:28Z)

In this commit is what I consider the proper solution, requiring OpenCL 2.x:
https://github.com/preda/gpuowl/commit/79813d18197c058d74ad92cf174628e66b3f21d6

For OpenCL 1.x, maybe it would be nice to offer this:
barrier(CLK_GLOBAL_MEM_FENCE) should have an (implicit) scope of memory_scope_device instead of the (implicit) scope of memory_scope_work_group as it appears to have now.
While this is not required by the OpenCL 1.x standard, it may match better the expectations of developers and previous behavior.

Note that, in practice, this is probably the main use of barrier(CLK_GLOBAL_MEM_FENCE) in OpenCL 1.x, so any performance hit introduced by the "device" scope there should be fine and expected.

(the use of barrier(CLK_GLOBAL_MEM_FENCE) with an intended scope of workgroup is probably borderline or performance-challenged).

---

### 评论 #11 — jlgreathouse (2018-07-30T21:44:29Z)

Hi @preda, 

I'll note that the reason you were able to skip atomic_load() operations on the `carryShuttle` variables is because, in order to [follow the proper acquire/release semantics of our memory model](https://llvm.org/docs/AMDGPUUsage.html#memory-model), our compiler performs an L1 invalidation command after the `atomic_load_explicit(memory_order_acquire)` operation in your code. As such, any outdated values of other variables before the acquire that are in that L1 (from other wavefronts or workgroups, or from older values) will be invalidated and the next load will get the value set by the other workgroup before it set the `ready[]` flag variable with memory_order_release.

I mention this for two reasons:

1. so that anyone who finds this thread later can see why you don't necessarily need to do an atomic_load() or atomic_store() to the `carryShuffle[]` array, since [we define a series of single-threaded optimization constraints](https://llvm.org/docs/AMDGPUUsage.html#amdgpu-amdhsa-memory-model-single-thread-optimization-constraints-gfx6-gfx9-table) for these acquire/release variables. We guarantee that our compiler will not reorder the store to `carryShuttle[]` after the `atomic_store()` to `ready[]`. Similarly, we will not bring the load from `carryShuttle[]` above the `atomic_load()` from `ready[]`.
2. Because this should describe why simply having an OpenCL 1.x implementation where barrier(CLK_GLOBAL_MEM_FENCE) puts in a global memory fence may not do what you want. Unless that fence also flushed the L1 cache, or if you rewrote your code so that both the `carryShuttle[]` and `ready[]` are accessed atomically, you may get outdated values of `carryShuttle[]` when you load it. However, if we forced CLK_GLOBAL_MEM_FENCE to flush the L1 caches every time someone used it, I strongly believe we would damage the performance of numerous legacy applications.

With your code now producing correct results, is it OK to close the ticket? Thanks!

---

### 评论 #12 — preda (2018-07-30T23:21:58Z)

Yes thank you, I'll close the ticket.

> However, if we forced CLK_GLOBAL_MEM_FENCE to flush the L1 caches every time someone used it, I strongly believe we would damage the performance of numerous legacy applications.

Please consider in what situation is the legacy app likely to be using the barrier(CLK_GLOBAL_MEM_FENCE). IMO, most often the intention is similar to what is achieved in 2.x through a memory_scope_device ("flushing the L1"), vs. a memory_scope_workgroup.


---

### 评论 #13 — b-sumner (2018-07-30T23:54:24Z)

> Please consider in what situation is the legacy app likely to be using the barrier(CLK_GLOBAL_MEM_FENCE). IMO, most often the intention is similar to what is achieved in 2.x through a memory_scope_device ("flushing the L1"), vs. a memory_scope_workgroup.

That doesn't seem likely to me.  OpenCL 1.x doesn't really provide a means to reliably communicate between work groups.  The intent of that barrier is to ensure that every work item in the current work group can see global state changes made prior to it by that same work group.  It is not to make global state changes prior to the barrier by that work group visible to the entire grid.

---
