# Relocation truncated to fit: R_X86_64_PC32 against symbol defined in .hipFatBinSegment section

- **Issue #:** 1765
- **State:** closed
- **Created:** 2022-07-05T15:37:35Z
- **Updated:** 2023-12-19T07:51:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1765

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