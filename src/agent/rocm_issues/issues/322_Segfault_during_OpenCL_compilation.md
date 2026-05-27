# Segfault during OpenCL compilation

> **Issue #322**
> **状态**: closed
> **创建时间**: 2018-02-02T12:15:01Z
> **更新时间**: 2019-01-03T20:51:39Z
> **关闭时间**: 2019-01-03T20:51:38Z
> **作者**: todxx
> **标签**: Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/322

## 标签

- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

I've been running into occasional segfaults during compilation of kernels with large amounts of inline assembly.  I managed to reproduce this in a small(ish) example while trying to reproduce a var/register leak problem that I am also observing in kernels with inline assembly.  I've attached the example that is reproducing the segfault.  Changing the macro SEGFAULT between 0 and 1 will respectively exclude or include the code that seems to be triggering the problem.

I am running on rocm 1.7 and targeting Vega.

[segfault.txt](https://github.com/RadeonOpenCompute/ROCm/files/1689245/segfault.txt)

Let me know if there is anything else I can do to help hunt down this bug.

---

## 评论 (13 条)

### 评论 #1 — todxx (2018-02-11T04:16:40Z)

Below is the backtrace printed by clang when invoked directly.  My toolchain is built from the roc-1.7.x branch.  This problem also occurs in the rocm 1.7 toolchain in the repos, but the repo versions have symbols stripped.

```
#0 0x0000000001e7847a llvm::sys::PrintStackTrace(llvm::raw_ostream&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x1e7847a)
#1 0x0000000001e7655e llvm::sys::RunSignalHandlers() (/home/todx/temp/ROCm/build/bin/clang-6.0+0x1e7655e)
#2 0x0000000001e766ac SignalHandler(int) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x1e766ac)
#3 0x00007f7815af5390 __restore_rt (/lib/x86_64-linux-gnu/libpthread.so.0+0x11390)
#4 0x000000000182c84a llvm::VirtRegAuxInfo::weightCalcHelper(llvm::LiveInterval&, llvm::SlotIndex*, llvm::SlotIndex*) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x182c84a)
#5 0x000000000182d7bd llvm::VirtRegAuxInfo::calculateSpillWeightAndHint(llvm::LiveInterval&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x182d7bd)
#6 0x000000000182d8ad llvm::calculateSpillWeightsAndHints(llvm::LiveIntervals&, llvm::MachineFunction&, llvm::VirtRegMap*, llvm::MachineLoopInfo const&, llvm::MachineBlockFrequencyInfo const&, float (*)(float, unsigned int, unsigned int)) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x182d8ad)
#7 0x00000000018a1f68 (anonymous namespace)::RAGreedy::runOnMachineFunction(llvm::MachineFunction&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x18a1f68)
#8 0x00000000016c1641 llvm::MachineFunctionPass::runOnFunction(llvm::Function&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x16c1641)
#9 0x000000000199032a llvm::FPPassManager::runOnFunction(llvm::Function&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x199032a)
#10 0x0000000001494d1e (anonymous namespace)::CGPassManager::runOnModule(llvm::Module&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x1494d1e)
#11 0x000000000198fee4 llvm::legacy::PassManagerImpl::run(llvm::Module&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x198fee4)
#12 0x0000000002038d65 clang::EmitBackendOutput(clang::DiagnosticsEngine&, clang::HeaderSearchOptions const&, clang::CodeGenOptions const&, clang::TargetOptions const&, clang::LangOptions const&, llvm::DataLayout const&, llvm::Module*, clang::BackendAction, std::unique_ptr<llvm::raw_pwrite_stream, std::default_delete<llvm::raw_pwrite_stream> >, bool) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x2038d65)
#13 0x00000000026f4c5f clang::CodeGenAction::ExecuteAction() (/home/todx/temp/ROCm/build/bin/clang-6.0+0x26f4c5f)
#14 0x00000000023cd58e clang::FrontendAction::Execute() (/home/todx/temp/ROCm/build/bin/clang-6.0+0x23cd58e)
#15 0x000000000239aa46 clang::CompilerInstance::ExecuteAction(clang::FrontendAction&) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x239aa46)
#16 0x000000000245f2d2 clang::ExecuteCompilerInvocation(clang::CompilerInstance*) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x245f2d2)
#17 0x000000000097c828 cc1_main(llvm::ArrayRef<char const*>, char const*, void*) (/home/todx/temp/ROCm/build/bin/clang-6.0+0x97c828)
#18 0x00000000008f684a main (/home/todx/temp/ROCm/build/bin/clang-6.0+0x8f684a)
#19 0x00007f7814852830 __libc_start_main /build/glibc-Cl5G7W/glibc-2.23/csu/../csu/libc-start.c:325:0
#20 0x000000000097a289 _start (/home/todx/temp/ROCm/build/bin/clang-6.0+0x97a289)
Stack dump:
0.	Program arguments: /home/todx/temp/ROCm/build/bin/clang-6.0 -cc1 -triple amdgcn-amd-amdhsa-amdgizcl -S -disable-free -disable-llvm-verifier -discard-value-names -main-file-name segfault.s.linked.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -target-cpu gfx900 -dwarf-column-info -debugger-tuning=gdb -coverage-notes-file /home/todx/temp/bugs/segfault.gcno -resource-dir /home/todx/temp/ROCm/build/lib/clang/6.0.0 -O3 -fdebug-compilation-dir /home/todx/temp/bugs -ferror-limit 19 -fmessage-length 250 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -fcolor-diagnostics -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -mllvm -enable-si-insert-waitcnts -o segfault.s -x ir segfault.s.linked.bc 
1.	Code generation
2.	Running pass 'CallGraph Pass Manager' on module 'segfault.s.linked.bc'.
3.	Running pass 'Greedy Register Allocator' on function '@sieve'
clang-6.0: error: unable to execute command: Segmentation fault
clang-6.0: error: clang frontend command failed due to signal (use -v to see invocation)
clang version 6.0.0 (https://github.com/RadeonOpenCompute/clang.git fbbf9d4f43f615514ed0defe9f81a2cbb3fcbf37) (ssh://git@github.com/RadeonOpenCompute/llvm aa423ebf5bfaca508606d157be52c5f3542aa1bf)
Target: amdgcn-amd-amdhsa-amdgizcl
Thread model: posix
InstalledDir: /home/todx/temp/ROCm/build/bin
clang-6.0: note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
clang-6.0: note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.

```

---

### 评论 #2 — gstoner (2018-03-02T23:06:01Z)

@todxx  Can you try the beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2  It support 4.13 Linux kernel 

---

### 评论 #3 — todxx (2018-03-03T20:18:22Z)

Below is the result with the 1.7.1 beta.  I'm happy to run this on a fresh build of the roc-1.7.x branch if you'd like a more detailed printout, but my guess is that it will be the same as the above trace.

```
$ /opt/rocm/bin/clang-ocl -mcpu=gfx900 -o segfault.o segfault.txt 
/opt/rocm/opencl/bin/x86_64/clang[0x24d6baa]
/opt/rocm/opencl/bin/x86_64/clang[0x24d4f0e]
/opt/rocm/opencl/bin/x86_64/clang[0x24d5060]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x11390)[0x7f0747efa390]
/opt/rocm/opencl/bin/x86_64/clang[0x1a587f5]
/opt/rocm/opencl/bin/x86_64/clang[0x1a599fd]
/opt/rocm/opencl/bin/x86_64/clang[0x1a59b1d]
/opt/rocm/opencl/bin/x86_64/clang[0x1a8f569]
/opt/rocm/opencl/bin/x86_64/clang[0x1a1ce07]
/opt/rocm/opencl/bin/x86_64/clang[0x23ca00a]
/opt/rocm/opencl/bin/x86_64/clang[0x2248f5f]
/opt/rocm/opencl/bin/x86_64/clang[0x23caa7f]
/opt/rocm/opencl/bin/x86_64/clang[0x6af068]
/opt/rocm/opencl/bin/x86_64/clang[0x5b7629]
/opt/rocm/opencl/bin/x86_64/clang[0x984e4e]
/opt/rocm/opencl/bin/x86_64/clang[0x976cbd]
/opt/rocm/opencl/bin/x86_64/clang[0x5a41ad]
/opt/rocm/opencl/bin/x86_64/clang[0x59b5b8]
/opt/rocm/opencl/bin/x86_64/clang[0x547c89]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7f0747b3f830]
/opt/rocm/opencl/bin/x86_64/clang[0x59a9e1]
Stack dump:
0.	Program arguments: /opt/rocm/opencl/bin/x86_64/clang -cc1 -triple amdgcn-amd-amdhsa-amdgizcl -emit-obj -disable-free -disable-llvm-verifier -discard-value-names -main-file-name segfault.o.linked.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -target-cpu gfx900 -dwarf-column-info -debugger-tuning=gdb -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -O3 -fdebug-compilation-dir /home/todx/temp/test_lyra2rev2 -ferror-limit 19 -fmessage-length 240 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -fcolor-diagnostics -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -mllvm -enable-si-insert-waitcnts -o /tmp/segfault-e45955.o -x ir segfault.o.linked.bc 
1.	Code generation
2.	Running pass 'CallGraph Pass Manager' on module 'segfault.o.linked.bc'.
3.	Running pass 'Greedy Register Allocator' on function '@sieve'
clang: error: unable to execute command: Segmentation fault
clang: error: clang frontend command failed due to signal (use -v to see invocation)
clang version 4.0 
Target: amdgcn-amd-amdhsa-amdgizcl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
clang: note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
clang: note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.

```

---

### 评论 #4 — b-sumner (2018-03-04T21:17:45Z)

@todxx could you comment on why you needed the inline asm in my_round?  If the compiler is not handling the C equivalent well, we'd like to hear about it.

---

### 评论 #5 — todxx (2018-03-04T23:42:34Z)

@b-sumner Most of the code I've been posting for bugs is stripped down versions of the larger codebase I'm working on.  I've been trying to generate the smallest examples I can, within reason, that trigger the symptoms I've been running into.  I do this both to try to make it easier to identify the problem, and because I'm not sure how much of my code I want to publish yet.  In this particular case, the compiler will generate better code than the above assembly since the v_mov's are redundant.  But this does not seem to be relevant to the bug in question.  Having different assembly triggers this bug just the same.

On a side note, I have a bit of a laundry list of other less-than-perfect compiler behaviours for which I've found work-arounds for, as well as new features that would be helpful to my work.  I've mostly been posting critical bugs for which I have not found work-arounds as they are the highest priority for me, and turn-around time for submitted bugs here tends to be a while (e.g. this issue was opened a month ago).

---

### 评论 #6 — gstoner (2018-03-04T23:59:46Z)

@todxx. I am sorry your seeing issue in the compiler,  We still a small team, we are working  hard looking at all the issue and closing them out.  What you find is we alway upstream fixes into the LLVM upstream.  We are starting to look at how we can run  Canary, Beta and Production for the compiler and language runtimes independent of the major driver update.  

I run the entire team I personally watch these forum and push the issue into the team we are working harder to close these issue quicker and release updates. 

G



---

### 评论 #7 — todxx (2018-03-05T00:31:42Z)

@gstoner No need to apologize.  I find the work you guys are doing to be fantastic and am extremely appreciative of the fact that you guys are working on an open source toolchain.  I also think it's awesome that you are taking public input and actually investigating the issues reported.  I like the community you are building and enjoy participating in it.

I realize you are a small team, and take this into account when filing issues.  I'm sure you guys have a lot more work on your plate than investigating issues submitted here.  This is partly why I try to only file critical issues instead of every sub-optimal behaviour I might run into.

While I may occasionally run into issues, as a whole the work you guys are doing with ROCm is making my work much easier, and I greatly appreciate it.

---

### 评论 #8 — todxx (2018-03-21T08:29:57Z)

@gstoner @b-sumner Is there any update on this issue?
Have you guys been able to reproduce it?
Is there anything I can do to help?

---

### 评论 #9 — searlmc1 (2018-03-21T14:50:47Z)

Hi,

We can reproduce it and have created 3 reduced testcases exhibiting 3 different compiler issues. Two have been fixed, the remaining causes the segfault seen in your larger testcase. The remaining problem looks like an issue in subregister renaming, where a register is not correctly renamed. A fix should be coming soon.

Sorry for the delay,

Mark

---

### 评论 #10 — todxx (2018-03-22T03:33:53Z)

@searlmc1 Thanks for the update.  I'm glad to hear you've been able to reproduce problem(s) and identify the cause.  

No worries about the delay.  I'm not trying to rush you guys.  I just wanted to check-up on the issue since it had been a little while since the last update.

Thank you for looking into this issue.

---

### 评论 #11 — searlmc1 (2018-07-09T21:13:20Z)

@todxx - the bugs have been fixed and the fixes should be available in the next ROCm release.; thanks much.

---

### 评论 #12 — jlgreathouse (2018-10-09T20:16:33Z)

For reference, this bug still exists in ROCm 1.9.x. I believe this is because our OpenCL compiler branched off before the bugfix went in. I believe the fix should make it into ROCm 2.0.

---

### 评论 #13 — jlgreathouse (2019-01-03T20:51:38Z)

Hi @todxx 

I believe this problem is fixed as of ROCm 2.0. I was able to compile your test kernel with `clang-ocl` and as part of a test harness program without causing the compiler to fail. Thanks for your patience!

---
