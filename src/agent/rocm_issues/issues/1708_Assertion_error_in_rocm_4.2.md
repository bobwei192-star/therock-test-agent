# Assertion error in rocm 4.2

> **Issue #1708**
> **状态**: closed
> **创建时间**: 2022-03-18T00:41:07Z
> **更新时间**: 2024-01-25T14:51:29Z
> **关闭时间**: 2024-01-25T14:51:29Z
> **作者**: cosigh
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1708

## 描述


When I use rocm4.2 compiled from source to compile vision

clang-12: /home/llvm-project-roc-4.2.x/llvm/include/llvm/IR/InstrTypes.h:1431: void llvm::CallBase::setCalledFunction(llvm::FunctionType*, llvm::Value*): Assertion `getType() == FTy->getReturnType()' failed.
PLEASE submit a bug report to https://bugs.llvm.org/ and include the crash backtrace, preprocessed source, and associated run script.
Stack dump:
0.	Program arguments: /opt/rocm-4.2.0/llvm/bin/clang-12 -cc1 -mllvm --amdhsa-code-object-version=4 -triple amdgcn-amd-amdhsa -aux-triple x86_64-unknown-linux-gnu -emit-obj --mrelax-relocations -disable-free -main-file-name interpolate_aa_kernels.hip -mrelocation-model pic -pic-level 2 -fhalf-no-semantic-interposition -mframe-pointer=none -fno-rounding-math -aux-target-cpu x86-64 -fcuda-is-device -mllvm -amdgpu-internalize-symbols -fcuda-allow-variadic-functions -fvisibility hidden -fapply-global-visibility-to-externs -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/hip.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/ocml.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/ockl.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/oclc_daz_opt_off.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/oclc_unsafe_math_off.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/oclc_finite_only_off.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/oclc_correctly_rounded_sqrt_on.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/oclc_wavefrontsize64_on.bc -mlink-builtin-bitcode /opt/rocm/amdgcn/bitcode/oclc_isa_version_908.bc -target-cpu gfx908 -fno-split-dwarf-inlining -debugger-tuning=gdb -resource-dir /opt/rocm-4.2.0/llvm/lib/clang/12.0.0 -internal-isystem /opt/rocm-4.2.0/llvm/lib/clang/12.0.0/include/cuda_wrappers -internal-isystem /opt/rocm/include -include __clang_hip_runtime_wrapper.h -isystem/opt/rocm-4.2.0/llvm/lib/clang/12.0.0/include/.. -isystem /opt/rocm/hsa/include -isystem /opt/rocm-4.2.0/hip/include -D WITH_HIP -I /home/vision/torchvision/csrc -I /usr/local/lib/python3.8/dist-packages/torch/include -I /usr/local/lib/python3.8/dist-packages/torch/include/torch/csrc/api/include -I /usr/local/lib/python3.8/dist-packages/torch/include/TH -I /usr/local/lib/python3.8/dist-packages/torch/include/THC -I /usr/local/lib/python3.8/dist-packages/torch/include/THH -I /opt/rocm/include -I /opt/rocm/miopen/include -I /usr/include/python3.8 -D __HIP_PLATFORM_HCC__=1 -D USE_ROCM=1 -D CUDA_HAS_FP16=1 -D __HIP_NO_HALF_OPERATORS__=1 -D __HIP_NO_HALF_CONVERSIONS__=1 -D TORCH_API_INCLUDE_EXTENSION_H -D PYBIND11_COMPILER_TYPE=\"_gcc\" -D PYBIND11_STDLIB=\"_libstdcpp\" -D PYBIND11_BUILD_ABI=\"_cxxabi1013\" -D TORCH_EXTENSION_NAME=_C -D _GLIBCXX_USE_CXX11_ABI=1 -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9 -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9 -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9 -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/backward -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9 -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9 -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/x86_64-linux-gnu/c++/9 -internal-isystem /usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/backward -internal-isystem /usr/local/include -internal-isystem /opt/rocm-4.2.0/llvm/lib/clang/12.0.0/include -internal-externc-isystem /usr/include/x86_64-linux-gnu -internal-externc-isystem /include -internal-externc-isystem /usr/include -internal-isystem /usr/local/include -internal-isystem /opt/rocm-4.2.0/llvm/lib/clang/12.0.0/include -internal-externc-isystem /usr/include/x86_64-linux-gnu -internal-externc-isystem /include -internal-externc-isystem /usr/include -O3 -std=c++14 -fdeprecated-macro -fno-autolink -fdebug-compilation-dir /home/vision -ferror-limit19 -fhip-new-launch-api -fgnuc-version=4.2.1 -fcxx-exceptions -fexceptions -fcolor-diagnostics -vectorize-loops -vectorize-slp -mllvm -amdgpu-early-inline-all=true -mllvm -amdgpu-function-calls=false -fcuda-allow-variadic-functions -munsafe-fp-atomics -faddrsig -o /tmp/interpolate_aa_kernels-gfx908-30acf8.o -x hip /home/vision/torchvision/csrc/ops/hip/interpolate_aa_kernels.hip
1.	<eof> parser at end of file
2.	Per-module optimization passes
3.	Running pass 'Late propagate attributes from kernels to functions' on module '/home/vision/torchvision/csrc/ops/hip/interpolate_aa_kernels.hip'.
 #0 0x0000558a0fe0f8e1 llvm::sys::PrintStackTrace(llvm::raw_ostream&, int) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x24998e1)
 #1 0x0000558a0fe0d4a4 llvm::sys::RunSignalHandlers() (/opt/rocm-4.2.0/llvm/bin/clang-12+0x24974a4)
 #2 0x0000558a0fe0d61b SignalHandler(int) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x249761b)
 #3 0x00007fe87a28a3c0 __restore_rt (/lib/x86_64-linux-gnu/libpthread.so.0+0x143c0)
 #4 0x00007fe879d2703b raise /build/glibc-sMfBJT/glibc-2.31/signal/../sysdeps/unix/sysv/linux/raise.c:51:1
 #5 0x00007fe879d06859 abort /build/glibc-sMfBJT/glibc-2.31/stdlib/abort.c:81:7
 #6 0x00007fe879d06729 get_sysdep_segment_value /build/glibc-sMfBJT/glibc-2.31/intl/loadmsgcat.c:509:8
 #7 0x00007fe879d06729 _nl_load_domain /build/glibc-sMfBJT/glibc-2.31/intl/loadmsgcat.c:970:34
 #8 0x00007fe879d18006 (/lib/x86_64-linux-gnu/libc.so.6+0x34006)
 #9 0x0000558a0e8ddc37 (anonymous namespace)::AMDGPUPropagateAttributes::process() (/opt/rocm-4.2.0/llvm/bin/clang-12+0xf67c37)
#10 0x0000558a0e8ddec5 (anonymous namespace)::AMDGPUPropagateAttributesLate::runOnModule(llvm::Module&) (/opt/rocm-4.2.0/llvm/bin/clang-12+0xf67ec5)
#11 0x0000558a0f57032c llvm::legacy::PassManagerImpl::run(llvm::Module&) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x1bfa32c)
#12 0x0000558a1010de09 (anonymous namespace)::EmitAssemblyHelper::EmitAssembly(clang::BackendAction, std::unique_ptr<llvm::raw_pwrite_stream, std::default_delete<llvm::raw_pwrite_stream> >) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x2797e09)
#13 0x0000558a1010fc08 clang::EmitBackendOutput(clang::DiagnosticsEngine&, clang::HeaderSearchOptions const&, clang::CodeGenOptions const&, clang::TargetOptions const&, clang::LangOptions const&, llvm::DataLayout const&, llvm::Module*,clang::BackendAction, std::unique_ptr<llvm::raw_pwrite_stream, std::default_delete<llvm::raw_pwrite_stream> >) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x2799c08)
#14 0x0000558a10edaa79 clang::BackendConsumer::HandleTranslationUnit(clang::ASTContext&) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x3564a79)
#15 0x0000558a11bd67a9 clang::ParseAST(clang::Sema&, bool, bool) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x42607a9)
#16 0x0000558a10ed9758 clang::CodeGenAction::ExecuteAction() (/opt/rocm-4.2.0/llvm/bin/clang-12+0x3563758)
#17 0x0000558a107cbfa9 clang::FrontendAction::Execute() (/opt/rocm-4.2.0/llvm/bin/clang-12+0x2e55fa9)
#18 0x0000558a107689de clang::CompilerInstance::ExecuteAction(clang::FrontendAction&) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x2df29de)
#19 0x0000558a108a1050 clang::ExecuteCompilerInvocation(clang::CompilerInstance*) (/opt/rocm-4.2.0/llvm/bin/clang-12+0x2f2b050)
#20 0x0000558a0e5e6f70 cc1_main(llvm::ArrayRef<char const*>, char const*, void*) (/opt/rocm-4.2.0/llvm/bin/clang-12+0xc70f70)
#21 0x0000558a0e5e1da8 ExecuteCC1Tool(llvm::SmallVectorImpl<char const*>&) (/opt/rocm-4.2.0/llvm/bin/clang-12+0xc6bda8)
#22 0x0000558a0e55924e main (/opt/rocm-4.2.0/llvm/bin/clang-12+0xbe324e)
#23 0x00007fe879d080b3 __libc_start_main /build/glibc-sMfBJT/glibc-2.31/csu/../csu/libc-start.c:342:3
#24 0x0000558a0e5e18fe _start (/opt/rocm-4.2.0/llvm/bin/clang-12+0xc6b8fe)
clang-12: error: unable to execute command: Aborted (core dumped)
clang-12: error: clang frontend command failed due to signal (use -v to see invocation)
clang version 12.0.0
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
clang-12: note: diagnostic msg: Error generating preprocessed source(s).
error: command '/opt/rocm/bin/hipcc' failed with exit status 254


---

## 评论 (4 条)

### 评论 #1 — cosigh (2022-03-23T03:11:32Z)

Is there something wrong with my compile parameters?
llvm ：
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/rocm/llvm -DLLVM_ENABLE_ASSERTIONS=1 -DLLVM_TARGETS_TO_BUILD="AMDGPU;X86" -DLLVM_ENABLE_PROJECTS="compiler-rt;lld;clang"    -DCPACK_PACKAGING_INSTALL_PREFIX=$ROCM_INSTALL_DIR/llvm/ -DCPACK_GENERATOR=DEB  -DCPACK_DEBIAN_PACKAGE_MAINTAINER=amd  -DCPACK_PACKAGE_NAME=llvm-amdgpu  ../llvm

I replace the source compiled llvm with the binary installation and no error will be reported.
gdb debugging：
getType（）
at ~/llvm/include/llvm/IR/Value.h:246
 Type *getType() const{ return Vty; }   
{Context = ... , ID = llvm::Type::VoidTyID,.....}

 FTy->getReturnType()
Type *getReturnType() const { return ContainedTys[0]; }
{Context = ... , ID = llvm::Type::DoubleTyID,.....}





---

### 评论 #2 — milliar2020 (2022-07-07T07:40:59Z)

@cosigh you can try build llvm with these compile parameters:
```
cmake -DCMAKE_BUILD_TYPE=Release \
-DCMAKE_INSTALL_PREFIX=/opt/rocm/llvm \
-DLLVM_TARGETS_TO_BUILD="AMDGPU;X86" \
-DLLVM_ENABLE_PROJECTS="compiler-rt;lld;clang" \
-DCPACK_PACKAGING_INSTALL_PREFIX=$ROCM_INSTALL_DIR/llvm/ \
-DCPACK_GENERATOR=DEB \
-DCPACK_DEBIAN_PACKAGE_MAINTAINER=amd \
-DCPACK_PACKAGE_NAME=llvm-amdgpu \
../llvm
```
It seems there is some thing wrong when compile pytorch vision with LLVM_ENABLE_ASSERTIONS option enable.

---

### 评论 #3 — abhimeda (2024-01-25T03:27:18Z)

@cosigh Hi, is your issue resolved in the latest ROCm? If so can we close this ticket?

---

### 评论 #4 — cosigh (2024-01-25T14:51:24Z)

yes ，you can  close this ticket

---
