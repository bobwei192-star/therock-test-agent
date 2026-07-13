# fatal error: 'limits' file not found

- **Issue #:** 2054
- **State:** closed
- **Created:** 2023-04-16T00:23:08Z
- **Updated:** 2023-04-16T00:40:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/2054

When trying to run a PyTorch application on ROCm 5.4, I get this error:

```
MIOpen(HIP): Error [Compile] 'hiprtcCompileProgram(prog.get(), c_options.size(), c_options.data())' naive_conv.cpp: HIPRTC_ERROR_COMPILATION (6)
MIOpen(HIP): Error [BuildHip] HIPRTC status = HIPRTC_ERROR_COMPILATION (6), source file: naive_conv.cpp
MIOpen(HIP): Warning [BuildHip] /tmp/comgr-ededb1/input/naive_conv.cpp:39:10: fatal error: 'limits' file not found
#include <limits> // std::numeric_limits
         ^~~~~~~~
1 error generated when compiling for gfx900.
terminate called after throwing an instance of 'miopen::Exception'
  what():  /long_pathname_so_that_rpms_can_package_the_debug_info/data/driver/MLOpen/src/hipoc/hipoc_program.cpp:304: Code object build failed. Source: naive_conv.cpp
```