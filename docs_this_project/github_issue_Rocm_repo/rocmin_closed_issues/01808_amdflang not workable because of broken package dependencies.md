# amdflang not workable because of broken package dependencies

- **Issue #:** 1808
- **State:** closed
- **Created:** 2022-09-16T15:48:05Z
- **Updated:** 2024-07-03T16:34:03Z
- **Assignees:** frepaul
- **URL:** https://github.com/ROCm/ROCm/issues/1808

when installing just the `rocm-llvm` Debian package for 5.2.3, the provided `amdflang` binary is not workable:

```console
$ amdflang -o conftest    conftest.f  -lz >&5
clang-14: error: unable to execute command: Executable "flang1" doesn't exist!
```

Because `flang1` is only provided in the (badly generic named) package `openmp-extras`:

```console
$ dpkg -S /opt/rocm-5.2.3/llvm/bin/amdflang 
rocm-llvm: /opt/rocm-5.2.3/llvm/bin/amdflang
$ dpkg -S /opt/rocm-5.2.3/llvm/bin/flang1
openmp-extras: /opt/rocm-5.2.3/llvm/bin/flang1
$ apt-cache depends openmp-extras
openmp-extras
  Depends: rocm-llvm
  Depends: rocm-device-libs
  Depends: rocm-core
```
