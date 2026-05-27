# [OpenMP] offload sincos crash compiler

> **Issue #1716**
> **状态**: closed
> **创建时间**: 2022-03-31T04:05:20Z
> **更新时间**: 2023-06-28T22:23:09Z
> **关闭时间**: 2023-06-28T22:23:09Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1716

## 负责人

- estewart08

## 描述

Reproducer:
https://github.com/ye-luo/openmp-target/blob/master/tests/math/sincos.cpp

This one is broken in both 5.1.0 and 5.0.0. 4.5.2 works fine.

```
$ /opt/rocm-5.1.0/llvm/bin/clang++ -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx906 -O3 -DNDEBUG sincos.cpp
LLVM ERROR: Cannot select: 0x55687c1f8d68: i32 = GlobalAddress<double addrspace(5)* @"_ZZL48sincos$ompvariant$S2$s7$Pamdgcn$S3$s9$Pmatch_anydPdS_E5__tmp"> 0
In function: __omp_offloading_10304_27a0c4e_main_l42
PLEASE submit a bug report to https://bugs.llvm.org/ and include the crash backtrace.
Stack dump:
0.	Program arguments: /opt/rocm-5.1.0/llvm/bin/llc /tmp/sincos-9140a8-gfx906-optimized-6ce7d4.bc -O3 -mtriple=amdgcn-amd-amdhsa -mcpu=gfx906 -filetype=obj --amdhsa-code-object-version=4 -o /tmp/sincos-9140a8-gfx906-765c6f.o
1.	Running pass 'CallGraph Pass Manager' on module '/tmp/sincos-9140a8-gfx906-optimized-6ce7d4.bc'.
2.	Running pass 'AMDGPU DAG->DAG Pattern Instruction Selection' on function '@__omp_offloading_10304_27a0c4e_main_l42'
 #0 0x00005568784b670f PrintStackTraceSignalHandler(void*) Signals.cpp:0:0
 #1 0x00005568784b3fed SignalHandler(int) Signals.cpp:0:0
 #2 0x00007f24ab5d93c0 __restore_rt (/lib/x86_64-linux-gnu/libpthread.so.0+0x143c0)
 #3 0x00007f24ab07803b raise /build/glibc-sMfBJT/glibc-2.31/signal/../sysdeps/unix/sysv/linux/raise.c:51:1
 #4 0x00007f24ab057859 abort /build/glibc-sMfBJT/glibc-2.31/stdlib/abort.c:81:7
 #5 0x000055687840f2b8 llvm::report_fatal_error(llvm::Twine const&, bool) (/opt/rocm-5.1.0/llvm/bin/llc+0x1c0f2b8)
 #6 0x00005568782e4e3c llvm::SelectionDAGISel::CannotYetSelect(llvm::SDNode*) (/opt/rocm-5.1.0/llvm/bin/llc+0x1ae4e3c)
 #7 0x00005568782e7f92 llvm::SelectionDAGISel::SelectCodeCommon(llvm::SDNode*, unsigned char const*, unsigned int) (/opt/rocm-5.1.0/llvm/bin/llc+0x1ae7f92)
 #8 0x00005568770535b7 AMDGPUDAGToDAGISel::Select(llvm::SDNode*) (/opt/rocm-5.1.0/llvm/bin/llc+0x8535b7)
 #9 0x00005568782e3984 llvm::SelectionDAGISel::DoInstructionSelection() (/opt/rocm-5.1.0/llvm/bin/llc+0x1ae3984)
#10 0x00005568782eb5e6 llvm::SelectionDAGISel::CodeGenAndEmitDAG() (/opt/rocm-5.1.0/llvm/bin/llc+0x1aeb5e6)
#11 0x00005568782eeebc llvm::SelectionDAGISel::SelectAllBasicBlocks(llvm::Function const&) (/opt/rocm-5.1.0/llvm/bin/llc+0x1aeeebc)
#12 0x00005568782f0ec2 llvm::SelectionDAGISel::runOnMachineFunction(llvm::MachineFunction&) (.part.886) SelectionDAGISel.cpp:0:0
#13 0x0000556877058b6a AMDGPUDAGToDAGISel::runOnMachineFunction(llvm::MachineFunction&) (/opt/rocm-5.1.0/llvm/bin/llc+0x858b6a)
#14 0x00005568778e9518 llvm::MachineFunctionPass::runOnFunction(llvm::Function&) (/opt/rocm-5.1.0/llvm/bin/llc+0x10e9518)
#15 0x0000556877d2e8d9 llvm::FPPassManager::runOnFunction(llvm::Function&) (/opt/rocm-5.1.0/llvm/bin/llc+0x152e8d9)
#16 0x00005568774dccd1 (anonymous namespace)::CGPassManager::runOnModule(llvm::Module&) CallGraphSCCPass.cpp:0:0
#17 0x0000556877d2fde7 llvm::legacy::PassManagerImpl::run(llvm::Module&) (/opt/rocm-5.1.0/llvm/bin/llc+0x152fde7)
#18 0x0000556876e11237 compileModule(char**, llvm::LLVMContext&) llc.cpp:0:0
#19 0x0000556876d884b6 main (/opt/rocm-5.1.0/llvm/bin/llc+0x5884b6)
#20 0x00007f24ab0590b3 __libc_start_main /build/glibc-sMfBJT/glibc-2.31/csu/../csu/libc-start.c:342:3
#21 0x0000556876e0968a _start (/opt/rocm-5.1.0/llvm/bin/llc+0x60968a)
clang-14: error: unable to execute command: Aborted (core dumped)
clang-14: error: amdgcn-link command failed due to signal (use -v to see invocation)
AMD clang version 14.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.1.0 22114 5cba46feb6af367b1cafaa183ec42dbfb8207b14)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-5.1.0/llvm/bin
clang-14: note: diagnostic msg: Error generating preprocessed source(s).
```

---

## 评论 (1 条)

### 评论 #1 — estewart08 (2022-04-11T14:44:46Z)

This has been already fixed, currently planned for 5.2.

---
