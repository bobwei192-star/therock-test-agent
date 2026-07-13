# Missing ISO_Fortran_binding.h

- **Issue #:** 3867
- **State:** closed
- **Created:** 2024-10-05T15:03:09Z
- **Updated:** 2024-10-08T21:51:48Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3867

The `ISO_Fortran_binding.h` which is part of `flang`/`amdflang` is not part of the ROCm installation. It doesn't show up in any ROCm rpms. LLVM has the necessary install rule:
https://github.com/llvm/llvm-project/blob/main/flang/CMakeLists.txt#L543-L547
and apparently so does the ROCm/llvm-project:
https://github.com/ROCm/llvm-project/blob/rocm-6.2.2/flang/CMakeLists.txt#L508-L512
So it might just be a packaging error.