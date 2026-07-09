# [Issue][ROCm 6.1RC][Regression]: Offloading via `--offload-arch=native` doesn't work or falls back to CPU

- **Issue #:** 2975
- **State:** closed
- **Created:** 2024-03-25T10:33:45Z
- **Updated:** 2025-09-09T14:44:57Z
- **Labels:** Under Investigation, AMD Instinct MI250X, ROCm 6.0.0
- **URL:** https://github.com/ROCm/ROCm/issues/2975

### Problem Description

This is a simple, but quite annoying regression:

Starting with ROCm 6.1RC, one can not offload a program using the compiler flag `--offload-arch=native` anymore. 
The flag `--offload-arch=gfx90a` still works. ROCm was always quite flaky with that flag, specifically forcing to have `LIBRARY_PATH` to set up a certain way so that the respective offloading files get found (in contrast to LLVM, where it always works as expected).

Here's an easy reproducer:

```console
$ cat minimal.c
int main( void )
{

}
$ amdclang --version
AMD clang version 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.1.0 24095 dd8a9741464a2adf616a8ca3cc75494392c26db3)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-6.1.0/lib/llvm/bin
Configuration file: /opt/rocm-6.1.0/lib/llvm/bin/clang.cfg
$ amdclang -fopenmp --offload-arch=native minimal.c 
clang: error: unable to execute command: Executable "clang-linker-wrapper" doesn't exist!
clang: error: linker command failed with exit code 1 (use -v to see invocation)
$ which clang-linker-wrapper
$ find /opt/rocm -name "clang-linker-wrapper"
```

compared to ROCm 6.0.2:

```console
$ amdclang --version
AMD clang version 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.0.2 24012 af27734ed982b52a9f1be0f035ac91726fc697e4)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-6.0.2/lib/llvm/bin
Configuration file: /opt/rocm-6.0.2/lib/llvm/bin/clang.cfg
$ amdclang -fopenmp --offload-arch=native minimal.c 
$ echo $?
0
```

### Operating System

Apptainer -- Ubuntu 22.04.3 LTS on JURECA-DC Evaluation Platform

### CPU

2x AMD EPYC 7443 24-Core Processor

### GPU

4x AMD Instinct MI250X

### ROCm Version

ROCm 6.1.0 RC

### ROCm Component

llvm-project

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_