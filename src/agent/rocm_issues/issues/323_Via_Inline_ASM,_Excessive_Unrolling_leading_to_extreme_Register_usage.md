# Via Inline ASM, Excessive Unrolling leading to extreme Register usage 

> **Issue #323**
> **状态**: closed
> **创建时间**: 2018-02-02T13:14:42Z
> **更新时间**: 2018-10-11T23:39:54Z
> **关闭时间**: 2018-10-11T23:29:19Z
> **作者**: todxx
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/323

## 描述

I have been running into what I can best describe as register leakage (perhaps incorrect liveness tracking is a better way to describe it?) when using inline assembly in large kernels.  

The symptoms of this bug are greatly increased vgpr usage, that often overflows to the private segment, and non-functioning builds.  I have spent a fair amount of time attempting to create a simple example that produces the problem but have had no success.  I have found a reproducible example by applying a small patch to an existing public code base in this git repo https://github.com/signatumd/sgminer.

The patch: [reg_leak.txt](https://github.com/RadeonOpenCompute/ROCm/files/1689450/reg_leak.txt)

Steps to reproduce:
1. Clone above repo.
2. Compile kernel/skunk.cl targeting Vega
3. Inspect the search2 kernel and note the vgpr and private segment usage.
4. Apply attached patch by running "patch -p1 < reg_leak.txt" in root of git tree
5. Compile kernel/skunk.cl targeting Vega (this includes the modified fugue.cl file)
6. Inspect the search2 kernel and compare vgpr and private segment usage to previous build.

Without the patch, the search2 kernel uses 103 vgpr and no private segment.  With the patch, the search2 kernel uses 256 vgpr and 386 bytes of private segment.  As can easily be seen, the changes in the patch should have no effect on register allocation.  It should also be noted that, in this case, this change also causes the compiler to emit incorrect assembly that does not functionally match the source code.  In other situations I have seen the compiler generate excessive vgpr usage but the resulting build still functions correctly.

I am using rocm 1.7 and running on a Vega card.

Let me know if there's anything more I can do to help with this bug.

---

## 评论 (20 条)

### 评论 #1 — arsenm (2018-02-06T16:38:38Z)

I think the more interesting question is why are you trying to use inline asm for this? The compiler should be able to use SDWA for you.

I'm running into issues compiling this:
` error: invalid reinterpretation: sizes of 'ulong' (aka 'unsigned long') and 'unsigned long long' must match
`

The code is using "typedef unsigned long long" in various places, seemingly intending to get a typedef for a 64-bit uint. This should use the builtin type ulong for this. unsigned long long is a reserved type in OpenCL that clang thinks is 128 bits.

---

### 评论 #2 — todxx (2018-02-06T18:33:05Z)

@arsenm I must disagree.  I think the most interesting part of this bug report is the part where there is a bug in the compiler that results in it generating incorrect code without any complaints.

As for the SDWA instructions, that is great news.  Could you show me an example of how to get the compiler to generate a close to optimal set of instructions to compute the 4 lines of code changed in the patch plus the next 12 lines?  With manual assembly, I can accomplish the 16 lines of code in 16 instructions.  The best I have gotten the compiler to do is about 40 instructions for the 16 lines.  The macro these lines are in is invoked 156 times during the full computation of a fugue hash and thus takes up the majority of the time spent in this hash function.  I look forward to seeing how to achieve this performance without using inline assembly.

Regarding the compiler error: you must not be running on rocm 1.7 using the default opencl compiler.  It does not complain about the unsigned long long, or about anything for that matter.  It just silently compiles and generates incorrect code.  I agree with you that the use of unsigned long long is incorrect, but I am not the maintainer of that code base.  Using this code was the easiest way I could find to reproduce the problem (and without the assembly patch, it compiles and runs just fine).  I also do not believe it is related to the bug being targeted here, as I have run into this bug in several different, unrelated code bases that compiled and ran just fine before the addition of inline assembly.

---

### 评论 #3 — arsenm (2018-02-07T20:28:17Z)

The pass that produces this certainly needs some work to match this right now, but it should be able to handle this without inline asm. I'm not claiming it is possible to get it to produce the good code today, it just should be. The current code seems like it doesn't try very hard to do much with dst_sel.

I missed the part about this being incorrect, I thought this was an optimization issue. I'm not sure why the registers usage increases so dramatically in this case, but in general I would expect inline asm to make the register allocator do a worse job. I've managed to hit a verifier error with the inline asm so hopefully this isn't too difficult to debug

---

### 评论 #4 — arsenm (2018-02-08T02:31:11Z)

https://github.com/llvm-mirror/llvm/commit/6879e4b17a93f854187a42636d4e1153cca329fc probably fixes the wrong codegen

---

### 评论 #5 — todxx (2018-02-08T11:37:25Z)

@arsenm Firstly, thank you very much for looking into the issues I've been reporting.  It makes a big difference being able to talk to and get help directly from the devs.

I agree with you that it would be nice if the compiler generated better assembly for the code in question.  Given the magic I've seen it work in other scenarios, I'm sure you could get it to handle this case.  However, this is one of my simpler cases of inline assembly.  Others, such as using v_add3, v_xad, ds_xor*, and dpp instructions, will probably take some time to get compiler support for.  And given the delay slots for dpp and the s_waits needed for ds_*, I usually end up with relatively large sections of inline assembly that seem to trigger this problem.

Regarding your llvm change:  I do not currently have a way to test it.  I will try to get a working llvm/clang build going and verify the fix.  I don't know how far I'll make it down that path since I have not found any documentation about building gcn kernels directly with clang instead of going through libOpenCL.

Does this change address the incorrect code generation or the excessive vpgr usage, or both?  Both issues are currently show stoppers for me.

Lastly, an unrelated question, how much do you guys want us reporting bugs here?  Should I report everything I run into, or just the big show stoppers?

---

### 评论 #6 — arsenm (2018-02-08T22:05:34Z)

The register usage is a lot better and it doesn't spill anymore with the fix. It's still using more than without asm. You may have better results by putting each instruction in it's own asm statement so other instructions can be scheduled between. The asm blob as written requires more registers to be live at a time.

I'm not sure where the best place to report these sorts of bugs is. There are quite a few options.

---

### 评论 #7 — todxx (2018-02-09T10:17:20Z)

@arsenm Sounds like that fixes the problems in question.  I really wish I could try it out.

Unfortunately I'm having no luck getting a working clang/llvm toolchain built.  I'm trying to build RadeonOpenCompute/clang with RadeonOpenCompute/llvm.  I've tried the roc-1.7.x, roc-1.7.0, and amd-common branches.  All of them build, but when trying to compile opencl with them the 1.7 branches hit asserts in clang, and the amd-common branches succeeds the first clang pass, but hits errors in llvm-link.  I'm using the clang-ocl script to invoke clang and llvm when attempting to compile opencl kernels.

I could use some pointers from the devs here on how to get a working build going.  Perhaps there are additional cmake options I need to set?  I'm building on ubuntu 16.04 with gcc 5.4.0 if that helps.

Edit: I built the roc-1.7.0 branch in release mode, which disabled the asserts that were being hit.  It now compiles the opencl kernel and will generate assembly output with -S.  However, I cannot get it to output a binary.  This also happens with the builds in the rocm 1.7 repo.  It seems that it doesn't like the inline assembly.  Here is part of the output when running with -v:

```
clang version 4.0 
Target: amdgcn-amd-amdhsa-amdgizcl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
 "/opt/rocm/opencl/bin/x86_64/clang" -cc1 -triple amdgcn-amd-amdhsa-amdgizcl -emit-llvm-bc -emit-llvm-uselists -disable-free -disable-llvm-verifier -discard-value-names -main-file-name skunk.cl -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -dwarf-column-info -debugger-tuning=gdb -v -coverage-notes-file /home/todx/temp/sgminer-signatum-clean/kernel/test.o.orig.gcno -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -include /opt/rocm/opencl/include/opencl-c.h -D __AMD__=1 -D __gfx803__=1 -D __gfx803=1 -D __OPENCL_VERSION__=120 -D __IMAGE_SUPPORT__=1 -D WORKSIZE=64 -O3 -fdebug-compilation-dir /home/todx/temp/sgminer-signatum-clean/kernel -ferror-limit 19 -fmessage-length 247 -cl-std=CL1.2 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -vectorize-loops -vectorize-slp -cl-ext=+cl_khr_fp64,+cl_khr_global_int32_base_atomics,+cl_khr_global_int32_extended_atomics,+cl_khr_local_int32_base_atomics,+cl_khr_local_int32_extended_atomics,+cl_khr_int64_base_atomics,+cl_khr_int64_extended_atomics,+cl_khr_3d_image_writes,+cl_khr_byte_addressable_store,+cl_khr_gl_sharing,+cl_amd_media_ops,+cl_amd_media_ops2,+cl_khr_subgroups -mllvm -amdgpu-early-inline-all -o test.o.orig.bc -x cl skunk.cl
clang -cc1 version 4.0 based upon LLVM 4.0.0svn default target amdgcn--amdhsa
ignoring nonexistent directory "/opt/rocm/opencl/bin/lib/clang/4.0/include"
#include "..." search starts here:
#include <...> search starts here:
 /usr/local/include
 /usr/include
End of search list.
clang version 4.0 
Target: amdgcn-amd-amdhsa-amdgizcl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
 "/opt/rocm/opencl/bin/x86_64/clang" -cc1 -triple amdgcn-amd-amdhsa-amdgizcl -emit-obj -disable-free -disable-llvm-verifier -discard-value-names -main-file-name test.o.linked.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -dwarf-column-info -debugger-tuning=gdb -v -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -O3 -fdebug-compilation-dir /home/todx/temp/sgminer-signatum-clean/kernel -ferror-limit 19 -fmessage-length 247 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -mllvm -enable-si-insert-waitcnts -o /tmp/test-472d8b.o -x ir test.o.linked.bc
clang -cc1 version 4.0 based upon LLVM 4.0.0svn default target amdgcn--amdhsa
<inline asm>:1:37: error: unknown token in expression
        v_xor_b32_sdwa v25, v66, v3 dst_sel:BYTE_3 dst_unused:UNUSED_PRESERVE src0_sel:BYTE_3 src1_sel:BYTE_3
                                           ^
error: cannot compile inline asm
<inline asm>:1:37: error: not a valid operand.
        v_xor_b32_sdwa v25, v66, v3 dst_sel:BYTE_3 dst_unused:UNUSED_PRESERVE src0_sel:BYTE_3 src1_sel:BYTE_3
                                           ^
error: cannot compile inline asm
<inline asm>:2:37: error: unknown token in expression
v_xor_b32_sdwa v25, v197, v0 dst_sel:BYTE_2 dst_unused:UNUSED_PRESERVE src0_sel:BYTE_2 src1_sel:BYTE_2
                                    ^
error: cannot compile inline asm
<inline asm>:2:37: error: not a valid operand.
v_xor_b32_sdwa v25, v197, v0 dst_sel:BYTE_2 dst_unused:UNUSED_PRESERVE src0_sel:BYTE_2 src1_sel:BYTE_2
                                    ^
error: cannot compile inline asm
<inline asm>:3:38: error: unknown token in expression
v_xor_b32_sdwa v25, v247, v21 dst_sel:BYTE_1 dst_unused:UNUSED_PRESERVE src0_sel:BYTE_1 src1_sel:BYTE_1
                                     ^
error: cannot compile inline asm
<inline asm>:3:38: error: not a valid operand.
v_xor_b32_sdwa v25, v247, v21 dst_sel:BYTE_1 dst_unused:UNUSED_PRESERVE src0_sel:BYTE_1 src1_sel:BYTE_1

```



---

### 评论 #8 — arsenm (2018-02-09T16:54:49Z)

I fixed an additional assertion in clang that is also upstream in this kernel that occurred without the inline asm. 

I don't see a specified cpu target on the run line, so I'm guessing this is defaulting to a subtarget without SDWA support (although I thought the asm error in this case was better)

---

### 评论 #9 — todxx (2018-02-10T23:21:20Z)

@arsenm Thank you again for all your help with this issue.  I can finally confirm that your change fixes both incorrect code gen and the excessive vgpr usage.  I think we can call this issue closed.

Edit: Ugh, I spoke too soon.  Unfortunately I ran into the same problem in another kernel.  It seems there are other bugs that result in this same symptom.  I will try to put together a simple example that triggers the problem.

Edit2: This kernel seems to cause the symptom: [reg_leak.txt](https://github.com/RadeonOpenCompute/ROCm/files/1714046/reg_leak.txt).  It appears that the compiler is trying to cache all of the LDS stores into vgprs, even if that means spilling. A lot.


---

### 评论 #10 — gstoner (2018-03-03T18:02:51Z)

@todxx We will look at the new issue 

---

### 评论 #11 — gstoner (2018-03-05T14:43:16Z)

Looking at the code loop, it algorithm has an issue as well. 

We have a loop of 64 iterations and we have “pragma unroll” set on it.
That means the loop body will be sequentially repeated 64 times.

We also have a macro “my_round” inside the loop.
This macro contains inline assembler which requires at least 9 VGPRs on each evaluation.
Please note that all the 9 VGPRs bounded to each inline assembler clause are pre-colored in the register allocator.

In other words, the registers are considered reserved.  Which means it cannot use just 9 registers on each unrolled iteration but is forced to allocate 9x64 different registers.

---

### 评论 #12 — todxx (2018-03-06T02:27:23Z)

I am not sure how to interpret your last message.

Are you suggesting that the register allocation behaviour you have described is correct?  Or that it is the problem?  To me, it sounds like the register allocator is needlessly reserving registers used by inline assembly clauses after those clauses are no longer using said registers.  This sounds like a bug.

Your comments also seem to suggest that this problem would not happen if the loop is unrolled manually.  Are you suggesting that any loop using inline assembly must be unrolled manually in order to not use extra registers?

---

### 评论 #13 — gstoner (2018-03-06T02:43:35Z)

Your allocating 576 registers,  so the application is going to spill,  Yes unroll the look Manually.   Sorry  I was talking to Staff in Europe this morning on this.  Working reparse the comment 

---

### 评论 #14 — todxx (2018-03-06T08:37:15Z)

I am no opencl expert, so please point out where I am misunderstanding.  As I read the opencl code, it should be allocating 24 vgprs for __private variables and 2048 bytes of LDS space for __local variables.   
I do not understand why you say that the code is allocating 576 vgprs.

The assembly that is generated does not use LDS.  There are no ds_* instructions generated.  Instead it places all stores into the __local variable long_vars into vpgrs and then spills.  Effectively, it is using memory to store what was clearly labeled as __local.

After some more experimenting, it appears this problem has nothing to do with the inline assembly.  I removed the entire __asm clause and the vpgr and memory usage remained the same.

If I remove the "pragma unroll" on the loops, the compiler correctly generates assembly using 26 vpgrs, 2048 bytes of LDS, and actually uses ds_read/write instructions for the variables labeled as __local.

For the short term, I can avoid this problem by manually unrolling, or choosing not to unroll loops.  For the long term, a fix will be needed for this problem.  As it currently stands, storing data into __local variables in a fully unrolled loop results in code that spills to memory and runs significantly slower (10 to 100 times slower).

It is possible that this problem is also what is causing the extra vgpr usage and performance issues reported by @preda in #320, as his code is indexing __local variables from within a loop as well.


---

### 评论 #15 — todxx (2018-03-22T03:37:16Z)

@gstoner Any update on this issue?
Is there anything I can do to help clarify the problem or help reproduce it?

---

### 评论 #16 — arsenm (2018-03-29T19:55:43Z)

In general you can't look at the program and say that N registers will be used for this private variable. The VGPR usage looks pretty good to me as-is, 39 VGPRs, and 11 SGPRs with no scratch use so I'm not sure what you are talking about.

The use of unroll here is pretty abusive. Unrolling all of these loops is causing the code length to over 100k, greatly exceeding the instruction cache size. I would expect it to be better to use something more conservative to get it to fit in the program cache. Huge blocks also aren't great for compile time. I would expect the default unroll heuristics to do something reasonable here since the loops are pretty simple and don't have any additional control flow nested inside or anything.

You also don't need to use a macro for this. You could just use a wrapper function which will be inlined for the inline asm which could be less annoying to modify.

---

### 评论 #17 — todxx (2018-03-30T06:16:02Z)

Compiling this with rocm 1.7.1 clang/llvm results in 256 vgpr and 1808 bytes private segment usage.
What version of clang/llvm are you building with?

Regarding the abusive unrolling: It is purposely over-done on this example to get this problem to show in an exaggerated manner.  This code is just for reproducing this problem.

Regarding the macros: in a perfect world, inlined functions would be the way to go.  However, much of my code now looks like this since there were problems with bad code generation back in rocm 1.6 and before.  I believe many of the problems have been resolved at this point, but I have not gone back to refactor most of the code since it works and there's plenty of new code that needs writing.

---

### 评论 #18 — todxx (2018-04-11T12:54:28Z)

Any update here?  Were you able to reproduce the problem?

---

### 评论 #19 — gstoner (2018-06-03T15:40:14Z)

@todxx have your tried ROCm 1.8. since the fix above would have been pulled in. 

---

### 评论 #20 — jlgreathouse (2018-10-11T23:29:19Z)

Hi @todxx 
I tried your [reg_leak.txt from Feb. 10](https://github.com/RadeonOpenCompute/ROCm/files/1714046/reg_leak.txt) in ROCm 1.9.1. I built it with the following command:
```
/opt/rocm/opencl/bin/x86_64/clang -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -x cl -Xclang -finclude-default-header -I/opt/rocm/opencl/include/ -DOPENCL_VERSION=200 -cl-std=CL2.0 -O3 -target amdgcn-amd-amdhsa -mcpu=gfx900 -Xclang -mlink-bitcode-file -Xclang /opt/rocm/opencl/lib/x86_64/bitcode/opencl.amdgcn.bc -Xclang -mlink-bitcode-file -Xclang /opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_900.amdgcn.bc  -Xclang -mlink-bitcode-file -Xclang /opt/rocm/opencl/lib/x86_64/bitcode/ockl.amdgcn.bc ./reg_leak.cl -o out.so
```

The resulting `out.so` file uses 39 VGPRs and 12 SGPRs and does not appear to have any space. As such, I think this issue was fixed back in 1.8.

---
