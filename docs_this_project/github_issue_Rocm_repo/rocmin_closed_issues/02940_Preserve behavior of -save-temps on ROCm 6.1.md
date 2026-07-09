# Preserve behavior of -save-temps on ROCm 6.1

- **Issue #:** 2940
- **State:** closed
- **Created:** 2024-03-03T19:25:43Z
- **Updated:** 2025-04-30T14:29:59Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon Pro VII, AMD Radeon VII
- **URL:** https://github.com/ROCm/ROCm/issues/2940

### Problem Description

On Ubuntu 22.04 w. linux kernel 6.7.5, Radeon Pro VII.
The behavior of the OpenCL compilation flag -save-temps seems altered on ROCm 6.1 vs. all previous ROCm versions.

The expected behavior: with -save-temps=folder/
the "temps" (.s, .so, .i etc) are written to that folder.

New observed behavior in 6.1: the value of the -save-temps=something is ignored, and some temps are written to the current folder, seemingly with overwriting names (when compiling multiple OpenCL programs in sequence).

Please restore the normal behavior of -save-temps in ROCm 6.1.

-save-temps is an important debug tool that has been around for decades with the AMD OpenCL stacks.

Caveat: ROCm 6.1 has not been released yet ATM.


### Operating System

Ubuntu 22.04

### CPU

not relevant

### GPU

AMD Radeon Pro VII, AMD Radeon VII

### ROCm Version

ROCm 6.0.0

### ROCm Component

clang-ocl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_