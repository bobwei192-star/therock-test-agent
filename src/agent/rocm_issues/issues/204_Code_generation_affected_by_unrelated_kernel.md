# Code generation affected by unrelated kernel

> **Issue #204**
> **状态**: closed
> **创建时间**: 2017-09-13T01:33:46Z
> **更新时间**: 2019-03-12T19:09:11Z
> **关闭时间**: 2019-03-12T19:09:11Z
> **作者**: preda
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/204

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

The exact source that displays the problem can be found here:
https://github.com/preda/gpuowl/blob/master/gpuowl.cl#L338

On AMDGPU-pro 17.30, RX Vega 64, on Linux:

I have two OpenCL kernels, that invoke the same function with different arguments:
```
void carryConvolution(....) { /* skipped */ }

kernel void carryConv1K_2K(uint baseBitlen, [etc]) {
  local double lds[4 * 256];
  double2 u[4];
  carryConvolution(4, 2048, lds, u, baseBitlen, etc);
}

#ifdef ENABLE_BUG
kernel void  carryConv2K_2K(uint baseBitlen, [etc]) {
  local double lds[8 * 256];
  double2 u[8];
  carryConvolution(8, 2048, lds, u, baseBitlen, etc);
}
#endif
```
The ISA code generated for the first kernel depends on whether the second kernel (the #ifdef one) exists or not. The difference in code and perf is major, see these stats for the first kernel:

1. When the second kernel is not present:
```
		workitem_private_segment_byte_size = 0
		workgroup_group_segment_byte_size = 8192
		kernarg_segment_byte_size = 88
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 20
		workitem_vgpr_count = 83
```
2. When the second kernel is present (but not used):
```
		workitem_private_segment_byte_size = 80
		workgroup_group_segment_byte_size = 8192
		kernarg_segment_byte_size = 88
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 28
		workitem_vgpr_count = 87
```

Both variants seems to function correctly (aside from performance).

---

## 评论 (14 条)

### 评论 #1 — wdng (2017-10-31T14:32:58Z)

Hi @preda ,  Looks like https://github.com/preda/gpuowl/blob/master/gpuowl.cl#L338 doesn't point to a right kernel, it would help if you could clarify which kernel in gpuowl src codes encounters this issue? Also, it would help me for debugging if you can provide parameters for that kernel. Thanks a lot!

---

### 评论 #2 — preda (2017-10-31T21:46:32Z)

Yes, there have been edits to the code, so below I've put links to a past revisions:

This kernel:
https://github.com/preda/gpuowl/blob/8a74346839f403ee7962da6d7821c88707000132/gpuowl.cl#L336
Being affected by the #ifdef around this one:
https://github.com/preda/gpuowl/blob/8a74346839f403ee7962da6d7821c88707000132/gpuowl.cl#L344


---

### 评论 #3 — yxsamliu (2017-11-08T19:23:46Z)

Both kernels contain call of carryConvolution. The first kernel calls carryConvolution with some unused arguments and the compiler is able to optimize them out. However, the second kernel calls that function in different ways, which preventing the compiler to optimize the called function. One workaround is to separate the common functions called by the kernels as a library, and compile each kernel with the library separately. This may also create other optimization opportunities and improve performance even better.

---

### 评论 #4 — preda (2017-11-08T21:55:38Z)

I think you're missing the point -- please read the initial description carefully. I'll try to clarify:

The compilation/optimization of the first kernel, let's call it A, depends on whether the kernel B is present or not.

I'm not talking about a difference between compilation-of-A and compilation-of-B, but about a difference between A [when B is not present] with A [when B is present].

Now, the opportunities for the optimization of A are obviously unaffected by the presence or not of B. So if the compiler generates worse code for A in one case, that's a bug. The fact that the compiler generates two significantly different compilations of the same kernel (A) depending on a factor that shouldn't affect it (presence or not of B) is a bug.


---

### 评论 #5 — yxsamliu (2017-11-08T22:26:31Z)

I did not miss your point.

OpenCL uses clang/llvm for the compilation. There is an IPO pass DeadArgumentElimination which is relevant for this issue. If there is a function call where some arguments are not used, this pass will modify the callee to eliminate the unused arguments and instructions.

Before this pass, the IR for carryConv1K_2K is

define amdgpu_kernel void @carryConv1K_2K(i32 %baseBitlen, <2 x double> addrspace(1)* noalias %io, double addrspace(1)* noalias %carryShuttle, i32 addrspace(1)* noalias %ready, <2 x double> addrspace(1)* noalias %A, <2 x double> addrspace(1)* noalias %iA, <2 x double> addrspace(1)* noalias %trig1k) local_unnamed_addr #5 !kernel_arg_addr_space !21 !kernel_arg_access_qual !22 !kernel_arg_type !23 !kernel_arg_base_type !24 !kernel_arg_type_qual !25 !reqd_work_group_size !13 {
entry:
  %u = alloca [4 x <2 x double>], align 16
  %0 = bitcast [4 x <2 x double>]* %u to i8*
  call void @llvm.lifetime.start.p0i8(i64 64, i8* %0) #8
  %arraydecay = getelementptr inbounds [4 x <2 x double>], [4 x <2 x double>]* %u, i32 0, i32 0
  call fastcc void @carryConvolution.32(i32 4, i32 2048, double addrspace(3)* getelementptr inbounds ([1024 x double], [1024 x double] addrspace(3)* @carryConv1K_2K.lds, i32 0, i32 0), <2 x double>* %arraydecay, i32 %baseBitlen, <2 x double> addrspace(1)* %io, double addrspace(1)* %carryShuttle, i32 addrspace(1)* %ready, <2 x double> addrspace(1)* %A, <2 x double> addrspace(1)* %iA, <2 x double> addrspace(1)* %trig1k) #9
  call void @llvm.lifetime.end.p0i8(i64 64, i8* %0) #8
  ret void
}

After this pass, the call instruction becomes

  call fastcc void @carryConvolution.32(<2 x double>* %arraydecay, i32 %baseBitlen, <2 x double> addrspace(1)* %io, double addrspace(1)* %carryShuttle, i32 addrspace(1)* %ready, <2 x double> addrspace(1)* %A, <2 x double> addrspace(1)* %iA, <2 x double> addrspace(1)* %trig1k) #8

As you can see, the function prototype for carryConvolution.32 has changed, because this function has been modified to be faster.

When carryConv1K_2K is included, the compiler is unable to modify carryConvolution.32 as before because such modification assumes certain arguments to take constant value, e.g. constant propagate them into the callee.

However, the IR for carryConv1K_2K is

define amdgpu_kernel void @carryConv2K_2K(i32 %baseBitlen, <2 x double> addrspace(1)* noalias %io, double addrspace(1)* noalias %carryShuttle, i32 addrspace(1)* noalias %ready, <2 x double> addrspace(1)* noalias %A, <2 x double> addrspace(1)* noalias %iA, <2 x double> addrspace(1)* noalias %trig1k) local_unnamed_addr #5 !kernel_arg_addr_space !21 !kernel_arg_access_qual !22 !kernel_arg_type !23 !kernel_arg_base_type !24 !kernel_arg_type_qual !25 !reqd_work_group_size !13 {
entry:
  %u = alloca [8 x <2 x double>], align 16
  %0 = bitcast [8 x <2 x double>]* %u to i8*
  call void @llvm.lifetime.start.p0i8(i64 128, i8* %0) #10
  %arraydecay = getelementptr inbounds [8 x <2 x double>], [8 x <2 x double>]* %u, i32 0, i32 0
  call fastcc void @carryConvolution.32(i32 8, double addrspace(3)* getelementptr inbounds ([2048 x double], [2048 x double] addrspace(3)* @carryConv2K_2K.lds, i32 0, i32 0), <2 x double>* %arraydecay, i32 %baseBitlen, <2 x double> addrspace(1)* %io, double addrspace(1)* %carryShuttle, i32 addrspace(1)* %ready, <2 x double> addrspace(1)* %A, <2 x double> addrspace(1)* %iA, <2 x double> addrspace(1)* %trig1k) #8
  call void @llvm.lifetime.end.p0i8(i64 128, i8* %0) #10
  ret void
}

carryConvolution.32 is called with different arguments. LLVM pass cannot modify carryConvolution.32 as before since carryConvolution.32 is now shared between carryConv1K_2K and carryConv2K_2K.

Can the LLVM pass optimize the code as before? To do that, it has to make two versions of the callee and optimize them separately for the two call sites. IPO passes usually need to balance speed and code size. If we allow cloning of function at each call site, it may causes code explosion.

---

### 评论 #6 — wdng (2017-11-08T22:45:05Z)

One thing that I want to add here is that: all kernels appear in the *.cl file will be kept as there are even when there is a dead code (carryConv2K_2K is a dead code here from the compiler point of views). @yxsamliu mentioned that the presence of carryConv2K_2K prevents optimization for function carryConv1K_2K, which later prevents compiler to generate optimized codes since from the mid-end (LLVM IR) until ISAs, that's why you see different ISAs. In short, with the presence of carryConv2K_2K, generated carryConv1K_2K LLVM IR is not the optimized, same as the ISAs.

---

### 评论 #7 — yxsamliu (2017-11-08T22:49:03Z)

The compiler does not know carryConv2K_2K is dead code. When the program is compiled, all kernels are equally treated and kept. Because compiler does not know which kernel will be called later.

---

### 评论 #8 — preda (2017-11-09T01:53:00Z)

OK your explanation makes sense, sorry for jumping at you.

Yes there is no notion of "dead (unused) kernel", so there's no argument here about dead-code, I agree.

Now back to the point, of course the carryConvolution() should be duplicated during optimization/inlining. This is indeed the cause of the bug -- the fact that the optimization is disabled by calling with different args from different kernels.

Now, sharing code makes sense for a CPU-target compiler, where there are calls to shared blocks of code (shared functions), and this reduces binary size. But on GCN, there is no shared code between kernels -- each kernel has its own full copy of all its ISA code, let's say "fully inlined". So there's no point in avoiding duplicating the carryConvolution() (which should be duplicated in one-version-per-kernel, enabling optimization).

The only gain is compilation speed. The cost is performance of the generated code. This trade-off is not worth it!

If the compiler doesn't do it, the developer must do the duplication manually, with a lot of pain. And the compiler generates sub-optimal code by default.. That's why I say this is a problem.

Also note that the "explosion" in compilation time (but not in generated code size, which is mostly unchanged) is not exponential, it's linear in the number of kernels.

So, if more performance can be gained, at the cost of compilation time linear in the number of kernels, that's a clear gain and should be done, yes.

---

### 评论 #9 — preda (2017-11-09T02:11:53Z)

On the plus side, I think this bug can now be qualified as "Performance" instead of "Functional" based on your analysis.

---

### 评论 #10 — preda (2017-11-09T02:17:04Z)

To reiterate, carryConvolution() is duplicated in one-per-kernel anyway when generating the GCN ISA for each kernel. Only that it is duplicated late, after that optimization pass. Instead, it should be duplicated early, allowing the specialization per kernel thus optimization.

---

### 评论 #11 — preda (2017-11-09T02:31:11Z)

It's like saying: yes, you have two kernels, but if you really want to optimize them both it would take twice the optimization time for one kernel. So instead the compiler decided to do the optimization only once overall. You gain optimization time, but now neither kernel is optimized anymore.

What about triggering the behavior based on -O complier options? If I say -O2 or -O3 or -O5 (at your choice), than it means I request "optimize it as well as it's possible, I don't mind waiting".


---

### 评论 #12 — yxsamliu (2017-11-09T18:43:25Z)

Thank you for sharing your thoughts @preda. I think that makes sense. I can try to fix it by cloning function at each call site when necessary. This could be put under an option. I am not sure how well this will be received by the LLVM community, but I think it worth trying.

There may be another SROA issue revealed by this issue. The major difference of the final IR in the good and bad cases is that in the good case the temporary array u is eliminated by LLVM pass SROA. Since all kernels are inlined, it does not make sense that SROA fails to eliminate u when DeadArgumentElimination pass fails to propagate argument N=4 into the callee. I am still investigating that.

Since the investigation/fixing may take some time, if you need a quick workaround, you may consider manually cloning carryConvolution and calls different copies in two kernels.

---

### 评论 #13 — acmeman925 (2017-11-30T19:14:03Z)

@preda  Did you by any chance try the work around suggested by @yxsamliu ?

---

### 评论 #14 — preda (2017-11-30T21:33:24Z)

No I didn't. This bug is not actively affecting my code in the current form (which has been reorganized), thus I'm not investigating a workaround. 

(OTOH https://github.com/RadeonOpenCompute/ROCm/issues/241 is still alive and kicking and I don't have a workaround for that)


---
