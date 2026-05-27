# LLVM's __builtin_nontemporal_store() assertion failure

> **Issue #1510**
> **状态**: closed
> **创建时间**: 2021-07-03T17:16:46Z
> **更新时间**: 2024-01-24T22:40:58Z
> **关闭时间**: 2024-01-24T22:40:58Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1510

## 描述

Using ROCm 4.2.0, LLVM head build, Linux kernel 5.13.0, Radeon VII,

I tried to use  __bultin_nontemporal_store() as per https://github.com/RadeonOpenCompute/ROCm/issues/1500#issuecomment-867679552

And I hit this LLVM assert:
```
gpuowl: /home/preda/llvm-project/llvm/lib/IR/Instructions.cpp:2959: static llvm::CastInst* llvm::CastInst::Create(llvm::Instruction::CastOps, llvm::Value*, llvm::Type*, const llvm::Twine&, llvm::Instruction*): Assertion `castIsValid(op, S, Ty) && "Invalid cast!"' failed.
Aborted (core dumped)

#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007f6228ae4859 in __GI_abort () at abort.c:79
#2  0x00007f6228ae4729 in __assert_fail_base (fmt=0x7f6228c7a588 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", assertion=0x7f5e1e8de030 "castIsValid(op, S, Ty) && \"Invalid cast!\"", file=0x7f5e1e8d8230 "/home/preda/llvm-project/llvm/lib/IR/Instructions.cpp", line=2959, 
    function=<optimized out>) at assert.c:92
#3  0x00007f6228af5f36 in __GI___assert_fail (assertion=0x7f5e1e8de030 "castIsValid(op, S, Ty) && \"Invalid cast!\"", file=0x7f5e1e8d8230 "/home/preda/llvm-project/llvm/lib/IR/Instructions.cpp", line=2959, 
    function=0x7f5e1e8ddfa0 "static llvm::CastInst* llvm::CastInst::Create(llvm::Instruction::CastOps, llvm::Value*, llvm::Type*, const llvm::Twine&, llvm::Instruction*)") at assert.c:101
#4  0x00007f5e1c4c363f in llvm::CastInst::Create(llvm::Instruction::CastOps, llvm::Value*, llvm::Type*, llvm::Twine const&, llvm::Instruction*) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#5  0x00007f5e18bbb749 in clang::CodeGen::CodeGenFunction::EmitBuiltinExpr(clang::GlobalDecl, unsigned int, clang::CallExpr const*, clang::CodeGen::ReturnValueSlot) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#6  0x00007f5e1887c577 in clang::CodeGen::CodeGenFunction::EmitCallExpr(clang::CallExpr const*, clang::CodeGen::ReturnValueSlot) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#7  0x00007f5e188c8ca2 in (anonymous namespace)::ScalarExprEmitter::VisitCallExpr(clang::CallExpr const*) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#8  0x00007f5e188c6199 in (anonymous namespace)::ScalarExprEmitter::Visit(clang::Expr*) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#9  0x00007f5e188c835a in clang::CodeGen::CodeGenFunction::EmitScalarExpr(clang::Expr const*, bool) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#10 0x00007f5e1885b2c7 in clang::CodeGen::CodeGenFunction::EmitAnyExpr(clang::Expr const*, clang::CodeGen::AggValueSlot, bool) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#11 0x00007f5e1887aa8e in clang::CodeGen::CodeGenFunction::EmitIgnoredExpr(clang::Expr const*) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#12 0x00007f5e189892ea in clang::CodeGen::CodeGenFunction::EmitStmt(clang::Stmt const*, llvm::ArrayRef<clang::Attr const*>) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#13 0x00007f5e1898f68c in clang::CodeGen::CodeGenFunction::EmitCompoundStmtWithoutScope(clang::CompoundStmt const&, bool, clang::CodeGen::AggValueSlot) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#14 0x00007f5e1898faa7 in clang::CodeGen::CodeGenFunction::EmitCompoundStmt(clang::CompoundStmt const&, bool, clang::CodeGen::AggValueSlot) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#15 0x00007f5e1898fca8 in clang::CodeGen::CodeGenFunction::EmitSimpleStmt(clang::Stmt const*, llvm::ArrayRef<clang::Attr const*>) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#16 0x00007f5e1898927c in clang::CodeGen::CodeGenFunction::EmitStmt(clang::Stmt const*, llvm::ArrayRef<clang::Attr const*>) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#17 0x00007f5e1898d4de in clang::CodeGen::CodeGenFunction::EmitForStmt(clang::ForStmt const&, llvm::ArrayRef<clang::Attr const*>) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#18 0x00007f5e18989917 in clang::CodeGen::CodeGenFunction::EmitStmt(clang::Stmt const*, llvm::ArrayRef<clang::Attr const*>) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#19 0x00007f5e1898f68c in clang::CodeGen::CodeGenFunction::EmitCompoundStmtWithoutScope(clang::CompoundStmt const&, bool, clang::CodeGen::AggValueSlot) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#20 0x00007f5e189e65f1 in clang::CodeGen::CodeGenFunction::EmitFunctionBody(clang::Stmt const*) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#21 0x00007f5e189f7a5c in clang::CodeGen::CodeGenFunction::GenerateCode(clang::GlobalDecl, llvm::Function*, clang::CodeGen::CGFunctionInfo const&) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#22 0x00007f5e18a51d66 in clang::CodeGen::CodeGenModule::EmitGlobalFunctionDefinition(clang::GlobalDecl, llvm::GlobalValue*) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#23 0x00007f5e18a4d8b5 in clang::CodeGen::CodeGenModule::EmitGlobalDefinition(clang::GlobalDecl, llvm::GlobalValue*) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#24 0x00007f5e18a4dd1b in clang::CodeGen::CodeGenModule::EmitGlobal(clang::GlobalDecl) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#25 0x00007f5e18a567d2 in clang::CodeGen::CodeGenModule::EmitTopLevelDecl(clang::Decl*) [clone .part.0] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#26 0x00007f5e1876d679 in (anonymous namespace)::CodeGeneratorImpl::HandleTopLevelDecl(clang::DeclGroupRef) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#27 0x00007f5e1874b9e0 in clang::BackendConsumer::HandleTopLevelDecl(clang::DeclGroupRef) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#28 0x00007f5e1a91a324 in clang::ParseAST(clang::Sema&, bool, bool) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#29 0x00007f5e187592b8 in clang::CodeGenAction::ExecuteAction() [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#30 0x00007f5e1a6954d9 in clang::FrontendAction::Execute() () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#31 0x00007f5e1a62ae96 in clang::CompilerInstance::ExecuteAction(clang::FrontendAction&) [clone .localalias] () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#32 0x00007f5e18233900 in clang::ExecuteCompilerInvocation(clang::CompilerInstance*) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#33 0x00007f5e1777f458 in COMGR::AMDGPUCompiler::executeInProcessDriver(llvm::ArrayRef<char const*>) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#34 0x00007f5e17780b47 in COMGR::AMDGPUCompiler::processFile(char const*, char const*) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#35 0x00007f5e17780f87 in COMGR::AMDGPUCompiler::processFiles(amd_comgr_data_kind_s, char const*) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#36 0x00007f5e177826d7 in COMGR::AMDGPUCompiler::compileToBitcode(bool) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#37 0x00007f5e1779f62c in dispatchCompilerAction(amd_comgr_action_kind_s, COMGR::DataAction*, COMGR::DataSet*, COMGR::DataSet*, llvm::raw_ostream&) () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#38 0x00007f5e177a2ae1 in amd_comgr_do_action () from /opt/rocm-4.2.0/opencl/lib/../../lib/libamd_comgr.so.2
#39 0x00007f6229197979 in ?? () from /opt/rocm-4.2.0/opencl/lib/libamdocl64.so
#40 0x00007f622919e028 in ?? () from /opt/rocm-4.2.0/opencl/lib/libamdocl64.so
#41 0x00007f62291a01c4 in ?? () from /opt/rocm-4.2.0/opencl/lib/libamdocl64.so
#42 0x00007f622914717c in ?? () from /opt/rocm-4.2.0/opencl/lib/libamdocl64.so
#43 0x00007f6229115d8f in clBuildProgram () from /opt/rocm-4.2.0/opencl/lib/libamdocl64.so
#44 0x00005648d8d8b09a in build (program=0x5648dacb0080, device=0x5648dac99810, 
    args="-DEXP=107000009u -DWIDTH=1024u -DHEIGHT=4096u -DAMDGPU=1 -DDWSTEP=0xe136f69df5c18cd0ul -DDWSTEP_2=0x709b7b4efae0c668ul -DIWSTEP=0x773fc4a96b97b14ful -DIWSTEP_2=0xee7f8952d72f629eul -DNH=8u -DNONTEMPOR"...) at /usr/include/c++/10/bits/basic_string.h:2299
#45 0x00005648d8d8be5c in compile (context=context@entry=0x5648daca1bc0, device=device@entry=0x5648dac99810, 
    source=" \n// Copyright Mihai Preda and George Woltman.\n#define STR(x) XSTR(x)\n#define XSTR(x) #x\n#define OVL __attribute__((overloadable))\n#if DEBUG\n#define assert(condition) if (!(condition)) { printf(\"asser"..., extraArgs=" -save-temps=t1/4M", 
    defines=std::vector of length 11, capacity 11 = {...}) at /usr/include/c++/10/bits/char_traits.h:329
#46 0x00005648d8d83086 in (anonymous namespace)::compile (args=..., context=<optimized out>, id=<optimized out>, N=<optimized out>, E=<optimized out>, WIDTH=<optimized out>, nH=<optimized out>) at /usr/include/c++/10/bits/char_traits.h:329
#47 0x00005648d8d85eb8 in Gpu::Gpu (this=0x5648daca05c0, args=..., E=107000009, WIDTH=1024, HEIGHT=4096, nW=4, nH=8, device=0x5648dac99810, timeKernels=true, weights=...) at /usr/include/c++/10/bits/unique_ptr.h:421
#48 0x00005648d8d880b1 in Gpu::Gpu (this=0x5648daca05c0, args=..., E=107000009, W=1024, HEIGHT=4096, nW=4, nH=8, device=0x5648dac99810, timeKernels=true) at /usr/include/c++/10/ext/new_allocator.h:89
#49 0x00005648d8d88581 in std::make_unique<Gpu, Args const&, unsigned int&, unsigned int&, unsigned int&, unsigned int&, unsigned int&, _cl_device_id*, bool&> () at /usr/include/c++/10/bits/unique_ptr.h:961
#50 Gpu::make (E=107000009, args=...) at Gpu.cpp:400
#51 0x00005648d8db26ef in Task::execute (this=0x7ffe6d618830, args=...) at Task.cpp:164
#52 0x00005648d8d6f25a in main (argc=1835108400, argv=0x7ffe6d6188b0) at Worktodo.h:20
```

To repro:
- checkout gpuowl at this commit: https://github.com/preda/gpuowl/tree/b1656272cc9160fdaebf04b2719619b534f3456c (i.e. the NTT2 branch)
- compile, and run with 
```
gpuowl -prp 107000009 -time -use NO_ASM,NONTEMPORAL
```

contrast with the behavior without the nontemporal load/store, which can be observed with
```
gpuowl -prp 107000009 -time -use NO_ASM
```

---

## 评论 (6 条)

### 评论 #1 — b-sumner (2021-07-03T18:32:30Z)

@preda since it appears to be an assert, could you post a minimal plain OpenCL C source kernel source right here?  And the message printed by the assert?

---

### 评论 #2 — preda (2021-07-03T18:49:53Z)

```
gpuowl: /home/preda/llvm-project/llvm/lib/IR/Instructions.cpp:2959: static llvm::CastInst* llvm::CastInst::Create(llvm::Instruction::CastOps, llvm::Value*, llvm::Type*, const llvm::Twine&, llvm::Instruction*): Assertion `castIsValid(op, S, Ty) && "Invalid cast!"' failed.
```

```
typedef uint u32;
typedef ulong u64;

kernel void fftOut(global u64* io) {
  u32 gr = get_group_id(0);
  u32 me = get_local_id(0);
  u64 u[4];

  io += 1024u * gr;
  
  for (u32 i = 0; i < 4; ++i) {
    u[i] = io[256 * i + me];
  }
  
  for (u32 i = 0; i < 4; ++i) {
    __builtin_nontemporal_store(u[i], io + (256 * i + me));
  }
}
```


---

### 评论 #3 — preda (2021-07-03T18:55:16Z)

This triggers it too, and it doesn't get much simpler than that:
```
kernel void fftOut(global u32* io) {
  __builtin_nontemporal_store(0, io);
}
```

---

### 评论 #4 — b-sumner (2021-07-04T02:49:08Z)

Thank you very much!  This is quite a surprise.

---

### 评论 #5 — abhimeda (2024-01-02T15:51:55Z)

Is the issue still reproducible with the latest ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #6 — nartmada (2024-01-24T22:40:58Z)

Closing the issue as no response from @preda.  Please re-open if the issue still exists with the latest ROCm6.0.0.  Thanks.

---
