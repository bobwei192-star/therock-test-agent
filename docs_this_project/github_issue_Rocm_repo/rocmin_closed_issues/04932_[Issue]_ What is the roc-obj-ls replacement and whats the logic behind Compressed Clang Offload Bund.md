# [Issue]: What is the roc-obj-ls replacement and whats the logic behind Compressed Clang Offload Bundle

- **Issue #:** 4932
- **State:** closed
- **Created:** 2025-06-16T18:53:11Z
- **Updated:** 2025-12-16T16:20:49Z
- **Labels:** Under Investigation
- **Assignees:** david-salinas
- **URL:** https://github.com/ROCm/ROCm/issues/4932

### Problem Description

We need a way of extracing code-objects out of .hip_fatbin and pack them back together, so we can perform binary instrumentation on individual code-objects.
Previously, we rely on the logic implemented in rocm-obj-ls to extract the binaries and create headers that allow us to pack them back together.

With a newer version of rocm (6.3.6) we see .hip_fatbin could be of the format compressed clang offload bundle (CCOB), and the old rocm-obj-ls tool no longer works.
I tried using clang-offload-bundler it wasn't able to identify triples with --list option nor able to unbundle it.
I also tried llvm-objdump --offload-fatbin, but I maybe I didn't pass the right option, as I wasn't able to get it to dump anything.

Please let me know what is the right command/option to do so.
Link to the binary of interest is attached here.
https://mega.nz/file/UxtXmBAb#cE6IGKZ0LAveyjgi9xrPQwOuhZC5jyGXKZdRHJpfCXs

OS:
NAME="Rocky Linux"
VERSION="8.8 (Green Obsidian)"
CPU:
model name      : AMD EPYC 7402 24-Core Processor
GPU:
  Name:                    AMD EPYC 7402 24-Core Processor
  Marketing Name:          AMD EPYC 7402 24-Core Processor
  Name:                    AMD EPYC 7402 24-Core Processor
  Marketing Name:          AMD EPYC 7402 24-Core Processor
  Name:                    gfx900
  Marketing Name:          Radeon Instinct MI25
      Name:                    amdgcn-amd-amdhsa--gfx900:xnack-
      Name:                    amdgcn-amd-amdhsa--gfx9-generic:xnack-
  Name:                    gfx908
  Marketing Name:          AMD Instinct MI100
      Name:                    amdgcn-amd-amdhsa--gfx908:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-


### Operating System

Rocky Linux (RHEL 8.8)

### CPU

AMD EPYC 7402 24-Core Processor

### GPU

MI25 / MI100 / MI210

### ROCm Version

ROCm 6.3.6

### ROCm Component

llvm-project

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_