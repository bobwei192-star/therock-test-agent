# [Issue]: Loop unrolling leads to terrible optimization

- **Issue #:** 4202
- **State:** open
- **Created:** 2024-12-27T00:36:29Z
- **Updated:** 2025-01-02T16:24:56Z
- **Labels:** Under Investigation, Radeon VII, ROCm 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4202

### Problem Description

I have a good sized kernel with a loop that is executed just twice.    If the loop is not unrolled, 63 VGPRs are used with an occupancy of 4.  If the loop is unrolled 135 VGPRs are used for occupancy of 1.  As you can imagine, performance suffers.

Using attributes to tell ROCm to only use a specific number of registers simply leads to spilling registers and performance is even worse.

There are several optimizations that could be made by unrolling the loop, but only if ROCm does not go a bit nuts allocating VGPRs.

Source code is available at https://github.com/gwoltman/gpuowl or https://github.com/preda/gpuowl 
The offending kernel is carryFused (in src/cl/carryfused.cl) .  The offending loop is fft_WIDTH (at the end of src/cl/fftwidth.cl).

System info:

OS:
NAME="Ubuntu"
VERSION="24.04.1 LTS (Noble Numbat)"
CPU:
model name      : Intel(R) Celeron(R) CPU G3900 @ 2.80GHz
GPU:
  Name:                    Intel(R) Celeron(R) CPU G3900 @ 2.80GHz
  Marketing Name:          Intel(R) Celeron(R) CPU G3900 @ 2.80GHz
  Name:                    gfx906
  Marketing Name:          AMD Radeon VII
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
  Name:                    gfx906
  Marketing Name:          AMD Radeon VII
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-


### Operating System

Ubuntu 24.04.1

### CPU

Intel Celeron

### GPU

Radeon VII

### ROCm Version

ROCm 6.3.0

### ROCm Component

_No response_

### Steps to Reproduce

Download the git sources named above.  Run make.
Make a directory called asm.
Create a config.txt file with this line:
-device 0 -workers 1 -block 1000 -user XXX -use BIGLIT=1 -use BCAST=0 -use FAST_BARRIER -use NONTEMPORAL=1

If the save-temps bug has been fixed, this command line should generate the asm/*carryfused*.s assembly file. 

Loop left as is:
./build-release/prpll -prp 136279841 -iters 1000 -dump asm  -fft 512:15:512:2 -use UNROLL_W=0

Loop unrolled:
./build-release/prpll -prp 136279841 -iters 1000 -dump asm  -fft 512:15:512:2 -use UNROLL_W=1



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_