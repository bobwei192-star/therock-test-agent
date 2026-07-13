# AMD Radeon RX 6800 - HIPRTC_ERROR_COMPILATION

- **Issue #:** 1889
- **State:** closed
- **Created:** 2023-01-12T14:32:46Z
- **Updated:** 2024-03-02T03:42:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1889

Hello,

I try to run a pytorch project with my RX 6800 (clinfo: gfx_1030)
/sys/module/amdgpu/version: 5.18.2.22.40

I installed ROCm 5.3 and pytorch Preview (Nightly).

But then I start the project I get after some time that errors and warnings:

```
MIOpen(HIP): Warning [SQLiteBase] Missing system database file: gfx1030_30.kdb Performance may degrade. Please follow instructions to install: https://github.com/ROCmSoftwarePlatform/MIOpen#installing-miopen-kernels-package
MIOpen(HIP): Error [Compile] 'hiprtcCompileProgram(prog.get(), c_options.size(), c_options.data())' naive_conv.cpp: HIPRTC_ERROR_COMPILATION (6)
MIOpen(HIP): Error [BuildHip] HIPRTC status = HIPRTC_ERROR_COMPILATION (6), source file: naive_conv.cpp
MIOpen(HIP): Warning [BuildHip] /tmp/comgr-112729/input/CompileSource:39:10: fatal error: 'limits' file not found
#include <limits> // std::numeric_limits
         ^~~~~~~~
1 error generated when compiling for gfx1030.
terminate called after throwing an instance of 'miopen::Exception'
  what():  /MIOpen/src/hipoc/hipoc_program.cpp:299: Code object build failed. Source: naive_conv.cpp
Aborted (core dumped)
```