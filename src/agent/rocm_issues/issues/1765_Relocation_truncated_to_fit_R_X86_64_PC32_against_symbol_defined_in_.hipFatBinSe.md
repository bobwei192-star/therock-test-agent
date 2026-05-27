# Relocation truncated to fit: R_X86_64_PC32 against symbol defined in .hipFatBinSegment section

> **Issue #1765**
> **状态**: closed
> **创建时间**: 2022-07-05T15:37:35Z
> **更新时间**: 2023-12-19T07:51:58Z
> **关闭时间**: 2023-12-19T07:51:58Z
> **作者**: dmikushin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1765

## 描述

Debug mode compilation generates much larger code, so that the ELF segments could grow well beyond their allowed lengths. For the CPU code, mcmodel=large usually is able to cope with this issue. But somehow it does not help to fix the `.hipFatBinSegment` section problem (see below). I'm not an expert in this topic, but `.hipFatBinSegment` stands out of the other sections because it is created artificially, with an attribute on a symbol in the LLVM IR code. Could mcmodel just be skipping such user-defined sections? In fact, placing the GPU code just into the .data section should not be a big issue, if the runtime would be able to extract it from there, using some table of references?

```
/lib/../lib64/crti.o: In function `_init':
(.init+0x7): relocation truncated to fit: R_X86_64_GOTPCREL against undefined symbol `__gmon_start__'
/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbeginS.o: In function `deregister_tm_clones':
crtstuff.c:(.text+0x3): relocation truncated to fit: R_X86_64_PC32 against `.tm_clone_table'
crtstuff.c:(.text+0xb): relocation truncated to fit: R_X86_64_PC32 against symbol `__TMC_END__' defined in .hipFatBinSegment section in lib/libtorch_hip.so
crtstuff.c:(.text+0x1a): relocation truncated to fit: R_X86_64_REX_GOTPCRELX against undefined symbol `_ITM_deregisterTMCloneTable'
/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbeginS.o: In function `register_tm_clones':
crtstuff.c:(.text+0x43): relocation truncated to fit: R_X86_64_PC32 against `.tm_clone_table'
crtstuff.c:(.text+0x4a): relocation truncated to fit: R_X86_64_PC32 against symbol `__TMC_END__' defined in .hipFatBinSegment section in lib/libtorch_hip.so
crtstuff.c:(.text+0x6b): relocation truncated to fit: R_X86_64_REX_GOTPCRELX against undefined symbol `_ITM_registerTMCloneTable'
/opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbeginS.o: In function `__do_global_dtors_aux':
crtstuff.c:(.text+0x92): relocation truncated to fit: R_X86_64_PC32 against `.bss'
crtstuff.c:(.text+0x9c): relocation truncated to fit: R_X86_64_GOTPCREL against symbol `__cxa_finalize@@GLIBC_2.2.5' defined in .text section in /lib64/libc.so.6
crtstuff.c:(.text+0xaa): relocation truncated to fit: R_X86_64_PC32 against symbol `__dso_handle' defined in .data.rel.ro.local section in /opt/rh/devtoolset-7/root/usr/lib/gcc/x86_64-redhat-linux/7/crtbeginS.o
crtstuff.c:(.text+0xba): additional relocation overflows omitted from the output
lib/libtorch_hip.so: PC-relative offset overflow in PLT entry for `_ZNKSt6vectorIPN5torch3jit5fuser4cuda10TensorViewESaIS5_EEixEm'
```

---

## 评论 (3 条)

### 评论 #1 — dmikushin (2022-07-13T22:06:42Z)

The problem appears to be well-known, e.g. https://github.com/apache/incubator-mxnet/issues/17045 Perhaps, the most thoughtful comment is this one:

> To solve this, I think we can instruct the compiler to always use 64 bit relocations instead of 32 bit relocations

With `mcmodel=large`, the R_X86_64_64 relocation type should be already used by default. Therefore, the remaining errors are due to the fact that some additional object brought into the linking by the compiler (crtstuff.o?) is still using R_X86_64_PC32. This argument is supported by [this bug](https://sourceware.org/bugzilla/show_bug.cgi?id=26386):

```
I mentioned that we build gcc 8.2.0 ourselves with -mcmodel=large,
and additionally patch it to build crt{begin,end}.o with the same
option:

 # Extra flags to use when compiling crt{begin,end}.o.
-CRTSTUFF_T_CFLAGS =
+CRTSTUFF_T_CFLAGS := -mcmodel=large

In our gcc, I can compile the test program successfully
```

Customizing GCC's `crtbegin.o` should be sufficient, as it is also [used by Clang](https://flameeyes.blog/2011/08/15/compilers-rant/):

> Clang doesn’t provide its own crtbegin.o file for the C runtime prologue (while Path64 does), so it relies on the one provided by GCC, which has to be on the system somewhere.

---

### 评论 #2 — nartmada (2023-12-19T03:30:14Z)

Hi @dmikushin, please close this ticket if the issue has been resolved.  Thanks.

---

### 评论 #3 — dmikushin (2023-12-19T07:51:48Z)

Hi @nartmada , as for me the debug compilation on GPU has been simply disabled entirely, in order to reduce the .hipFatBinSegment section. Is it a resolution to never be able to debug the GPU kernels within the PyTorch? Of course not. But it is rather an issue of the software architecture. For example, Pytorch may choose to embed the source code of kernels and defer their compilation to the runtime, if they are too big to be stored in the binary.

---
