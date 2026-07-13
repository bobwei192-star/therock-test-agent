# rocm-llvm-alt optional closed-source package compilation fails

- **Issue #:** 3492
- **State:** closed
- **Created:** 2024-08-02T18:13:47Z
- **Updated:** 2024-12-04T15:21:44Z
- **Labels:** Verified Issue, 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3492

ROCm provides an optional package – `rocm-llvm-alt` – that provides a closed-source compiler for users interested in additional closed-source CPU optimizations. This feature is not functional in the ROCm 6.2.0 release. Users who attempt to invoke the closed-source compiler will experience an LLVM consumer-producer mismatch and the compilation will fail. There is no workaround that allows use of the closed-source compiler. It is recommended to compile using the default open-source compiler, which generates high-quality AMD CPU and AMD GPU code.

The `rocm-llvm-alt` package will be removed in an upcoming release. Users relying on the functionality provided by the closed-source compiler should transition to the open-source compiler. Once the `rocm-llvm-alt` package is removed, any compilation requesting functionality provided by the closed-source compiler will result in a Clang warning: `[AMD] proprietary optimization compiler has been removed`.