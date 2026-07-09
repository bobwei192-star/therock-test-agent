# [Issue]: segfault when calling 'llvm::Target::createTargetMachine'

- **Issue #:** 2978
- **State:** closed
- **Created:** 2024-03-25T20:58:34Z
- **Updated:** 2024-10-01T20:01:56Z
- **Labels:** Under Investigation, AMD Instinct MI250X, AMD Instinct MI250, ROCm 5.6.0
- **URL:** https://github.com/ROCm/ROCm/issues/2978

### Problem Description

With ROCm 5.6.0 and later I'm getting a segfault when calling 'llvm::Target::createTargetMachine'. Earlier versions work fine.

The system:
Device name                         : AMD Instinct MI250X
GCN architecture                    : gfx910

My application uses the LLVM compiler that is bundled with the ROCm installation (/opt/rocm/llvm/). The call to 'createTargetMachine' goes like
    

```
llvm::TargetOptions options;
TargetMachine.reset(TheTarget->createTargetMachine(
                                                       "amdgcn-amd-amdhsa", // triple
                                                       "gfx90a",            // CPU
                                                       "",                  // feature str
                                                       options,
                                                       llvm::Reloc::PIC_
                                                       ));

```
This was never a problem. But since ROCm version 5.6.0 I get segfaults like:


```
  Thread 1 "t_dslashm" received signal SIGSEGV, Segmentation fault.
0x00000000008a6b81 in llvm::RegisterTargetMachine<llvm::GCNTargetMachine>::Allocator(llvm::Target const&, llvm::Triple const&, llvm::StringRef, llvm::StringRef, llvm::TargetOptions const&, std::optional<llvm::Reloc::Model>, std::optional<llvm::CodeModel::Model>, llvm::CodeGenOpt::Level, bool) ()
Missing separate debuginfos, use: zypper install krb5-debuginfo-1.19.2-150400.3.6.1.x86_64 libbrotlicommon1-debuginfo-1.0.7-3.3.1.x86_64 libbrotlidec1-debuginfo-1.0.7-3.3.1.x86_64 libcom_err2-debuginfo-1.46.4-150400.3.3.1.x86_64 libcurl4-debuginfo-8.0.1-150400.5.41.1.x86_64 libelf1-debuginfo-0.185-150400.5.3.1.x86_64 libidn2-0-debuginfo-2.2.0-3.6.1.x86_64 libjitterentropy3-debuginfo-3.4.0-150000.1.9.1.x86_64 libjson-c3-debuginfo-0.13-3.3.1.x86_64 libkeyutils1-debuginfo-1.6.3-5.6.1.x86_64 libldap-2_4-2-debuginfo-2.4.46-150200.14.17.1.x86_64 liblzma5-debuginfo-5.2.3-150000.4.7.1.x86_64 libncurses6-debuginfo-6.1-150000.5.20.1.x86_64 libnghttp2-14-debuginfo-1.40.0-150200.12.1.x86_64 libnl3-200-debuginfo-3.3.0-1.29.x86_64 libnuma1-debuginfo-2.0.14.20.g4ee5e0c-150400.1.24.x86_64 libopenssl1_1-debuginfo-1.1.1l-150400.7.60.2.x86_64 libpcre1-debuginfo-8.45-150000.20.13.1.x86_64 libpsl5-debuginfo-0.20.1-150000.3.3.1.x86_64 libselinux1-debuginfo-3.1-150400.1.69.x86_64 libssh4-debuginfo-0.9.6-150400.1.5.x86_64 libunistring2-debuginfo-0.9.10-1.1.x86_64 libxml2-2-debuginfo-2.9.14-150400.5.25.1.x86_64 libyaml-0-2-debuginfo-0.1.7-1.17.x86_64 libz1-debuginfo-1.2.11-150000.3.48.1.x86_64
(gdb) bt
#0  0x00000000008a6b81 in llvm::RegisterTargetMachine<llvm::GCNTargetMachine>::Allocator(llvm::Target const&, llvm::Triple const&, llvm::StringRef, llvm::StringRef, llvm::TargetOptions const&, std::optional<llvm::Reloc::Model>, std::optional<llvm::CodeModel::Model>, llvm::CodeGenOpt::Level, bool) ()
#1  0x0000000000578e4b in llvm::Target::createTargetMachine (this=0x48a9800 <llvm::getTheGCNTarget()::TheGCNTarget>, TT=..., CPU=..., Features=..., Options=..., RM=..., CM=..., OL=llvm::CodeGenOpt::Default, JIT=false)
    at /opt/rocm-5.6.0/llvm/include/llvm/MC/TargetRegistry.h:488
```

What am I missing?


### Operating System

Linux frontier07423 5.14.21-150400.24.46_12.0.83-cray_shasta_c

### CPU

AMD EPYC 7A53 64-Core Processor

### GPU

AMD Instinct MI250X, AMD Instinct MI250

### ROCm Version

ROCm 5.6.0

### ROCm Component

llvm-project

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_