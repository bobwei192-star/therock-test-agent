# Why acquire fences of barrier-AND/OR packet are processed before release fences?

- **Issue #:** 5681
- **State:** closed
- **Created:** 2025-11-20T15:49:38Z
- **Updated:** 2025-12-16T17:13:56Z
- **Labels:** status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5681

https://hsafoundation.com/wp-content/uploads/2021/02/HSA-SysArch-1.2.pdf

2.9.1.1 Acquire fences
> Barrier-OR and barrier-AND packet acquire fences are processed first in the completion phase of the
packet, after the barrier condition has been met.

2.9.1.2 Release fences
> Barrier-OR and barrier-AND packet release fences are processed after the acquire fence in the completion
phase of the packet.

Processing `acquire` before `release` makes sense for kernel dispatch. For the kernel to be able to read fresh data from previous `release` operations and at the end `release` data it wrote for the following `acquire` operations. But barrier-AND/OR by itself does not do any memory operation.

Lets consider this series of packets in a single queue:

```
kernel1 -> no barrier and no fence scopes
kernel2 -> no barrier and no fence scopes
kernel3 -> no barrier and no fence scopes
barrier-AND -> barrier bit is set and both acquire and release fence scope is set to agent
kernelA -> no barrier and no fence scopes
kernelB -> no barrier and no fence scopes
kernelC -> no barrier and no fence scopes
```

Kernels `kernel1`, `kernel2` and `kernel3` are independent. They do not read any data written by any of them.
Similarly for `kernelA`, `kernelB` and `kernelC`. But kernels A, B and C need to read data written by kernels 1, 2, and 3. Kernels 1, 2 and 3 can be run in parallel then barrier-AND will wait until they are done and kernels A, B and C will wait until barrier-AND is done and then execute in parallel.

Problem may be that barrier-AND will process first `acquire` fence and then `release` fence so it seems there is no release-acquire relationship and either kernels A, B and C need to have `acquire` fence or there need to be additional barrier-AND with acquire fence after that first one like this:

```
...
barrier-AND -> barrier bit is set and release fence scope is set to agent
barrier-AND -> barrier bit is set and acquire fence scope is set to agent
...
```

So to me it seems that if barrier-AND/OR first processed `release` fence and after that `acquire` fence it would make more sense and I cannot see any use case for current behaviour. Or is my example actually correct? Or maybe it would be incorrect even if barrier-AND/OR first processed the `release` fence?

3.3.8 Packet processor fences
> A packet memory release fence makes any global segment or image data that was stored by any
unit of execution that belonged to a dispatch that has completed the active phase on any queue of
the same agent visible in all the scopes specified by the packet release fence.
> A packet memory acquire fence ensures any subsequent global segment or image loads by any unit
of execution that belongs to a dispatch that has not yet entered the active phase on any queue of the
same agent, **sees any data previously released at the scopes specified by the packet acquire fence**.

Note for example how is opencl `work_group_barrier` implemented, first `release` fence then `s_barrier` and then `acquire` fence (although that is a little different kind of "barrier"):
https://github.com/ROCm/llvm-project/blob/913ae1c1c79b6e4363bc14848d773c43503ead15/amd/device-libs/opencl/src/workgroup/wgbarrier.cl#L26-L33