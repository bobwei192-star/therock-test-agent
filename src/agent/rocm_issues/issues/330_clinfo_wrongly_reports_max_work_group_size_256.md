# clinfo wrongly reports max work group size 256

> **Issue #330**
> **状态**: closed
> **创建时间**: 2018-02-08T11:18:12Z
> **更新时间**: 2018-02-20T21:50:52Z
> **关闭时间**: 2018-02-20T21:50:52Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/330

## 描述

ROCm 1.7, Ubuntu 17.10, Vega 64:
clinfo reports:
 Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256

In particular the "max workgroup size" does not appear to be correct as I can execute workgroups with larger sizes just fine (tried 512).

---

## 评论 (5 条)

### 评论 #1 — b-sumner (2018-02-20T14:56:29Z)

This is the result of a number of considerations including performance and misbehaving programs that do not use the reqd_work_group_size kernel attribute and do not call clGetKernelWorkGroupInfo.  By using the kernel attribute, you can indeed have a work group "volume" as high as 1024, but of course this will affect the number of registers available per work-item.

---

### 评论 #2 — jlgreathouse (2018-02-20T16:10:53Z)

Hi @preda,

(Edit: this was written in parallel with b-sumner's post, so I apologize for the needless extra information.)

This may not be communicated in the clearest way possible, but the max workgroup size being reported here is found by querying the runtime using `clGetDeviceInfo(CL_DEVICE_MAX_WORK_GROUP_SIZE)`. This is runtime-level information, which can't make any guarantees about what kind of kernel will be be asked to run.

The AMD GCN ISA allows any thread to address up to 256 4-byte vector registers; in other words, each thread can use up to 1024 bytes of VGPR space. Every thread in a workgroup must run on the same compute unit (because, for instance, they must be able to communicate through that CU's local memory/LDS). Each compute unit in our existing microarchitectures has 256 KB of registers.

With 256 KB of registers and each thread able to use up to 1 KB, we can only guarantee that a worst-case kernel can run 256 threads on a single CU. The runtime can't say anything more in the general case.


However, if you have a kernel that does *not* use all of its available register space, the GCN architecture *can* fit more wavefronts in a workgroup. In the [Vega ISA manual](https://developer.amd.com/wp-content/resources/Vega_Shader_ISA_28July2017.pdf), Section 4.3 describes how up to 16 64-wide wavefronts can be combined into a workgroup. This means that, if you limit the kernel's dynamic resource requests such that 1024 threads can fit into a single CU, the hardware *can* run the larger workgroup.

For instance, if each thread only requests 64 VGPRs, then each thread will only requests 256 bytes of VGPR space. This would allow 1024 threads to fit within a single CU. However, the runtime can only know if this is possible after the kernel has been compiled and it has laid out its VGPR allocation size.

As such, one way to request this "larger than maximum workgroup size" is to call clEnqueueNDRangeKernel() with localWorkSize set to NULL (so that the runtime does not complain about the size being larger than the maximum workgroup size), but writing/compiling the kernel using `__attribute__((reqd_work_group_size(X, Y, Z)))`, where X, Y, and Z make the total thread-count > 256. For instance, `__attribute__((reqd_work_group_size(1024, 1, 1)))`.

The reqd_work_group_size() attribute will tell the compiler that you want to avoid using too many VGPRs and thus 1024 threads from this kernel will be able to fit within a single workgroup and CU.

I'm not an expert at this, so there may be other, deeper, reasons for this decision. However, does this explanation make sense for why clinfo is reporting what it shows?

---

### 评论 #3 — preda (2018-02-20T21:19:58Z)

Firstly, thanks for the explanations, it makes sense, but I still have these observations:

As I understand, there *is* a different, "hard" workgroup-size maximum, which is 1024. No matter how small a kernel is, the hardware can't execute a workgroup with more that 1024 threads. How is this value queried or reported by clinfo?

So there are two limits:
- any kernel can be run with workgroup-size <= 256,
- some kernels can be run with workgroup-size <= 1024 (if the kernel VGPR usage allows it).
- no kernel can be run with workgroup-size > 1024.

(IMO, I'd still say that "Max work group size" is 1024)

@jlgreathouse:
https://www.khronos.org/registry/OpenCL/sdk/1.2/docs/man/xhtml/clEnqueueNDRangeKernel.html
says

The work-group size to be used for kernel can also be specified in the program source using the __attribute__ ((reqd_work_group_size(X, Y, Z))) qualifier. In this case the size of work group specified by local_work_size must match the value specified by the reqd_work_group_size __attribute__ qualifier.

Which seems to indicate that local_work_size can't be NULL when using reqd_work_group_size(), at least according to the spec.

---

### 评论 #4 — jlgreathouse (2018-02-20T21:42:14Z)

I would say that you should look at the `Max work items[]` outputs of clinfo to understand the maximum work items that the hardware limits you to. This is found by querying each of the dimensions of CL_DEVICE_MAX_WORK_ITEM_SIZES.

You're right, there are multiple limits in play, and that's why it's a bit non-clear exactly what to report for "max work group size". One of the reasons I'm writing out these explanations here is because I don't think you want all of these details dumped to the screen very time you run `clinfo`. :)

However, if we reported the maximum work group size as 1024, and then the runtime failed when you tried to enqueue a kernel with 512 threads per workgroup, I would wager we would get a torrent of complaints about the runtime being broken. My personal opinion (not any official stance of AMD) is that the current "max work group = 256" description prevents this.

As for the `reqd_work_group_size()` attribute, my previous post was overly specific to say that you *needed* to set `local_work_size` to NULL.

The current ROCm OpenCL runtime *allows* you to set `local_work_size` to NULL and it will run with the `reqd_work_group_size()` of > 256 threads. You can also set `local_work_size` to the same dimensions as your `reqd_work_group_size()` attribute and it will work. (e.g. setting `local_work_size={1024,1,1}` and `reqd_work_group_size(1024,1,1)`). If you don't set `reqd_work_group_size()`, however, requesting `local_work_size={1024,1,1}` will fail.

---

### 评论 #5 — preda (2018-02-20T21:50:52Z)

OK, thanks! I'm going to close this issue. The information contained here is useful, and may be extracted to some documentation.


---
