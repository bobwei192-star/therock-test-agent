# [Issue]: When the AMD 7840HS GPU crashes, how do I diagnose what is going wrong?

- **Issue #:** 5180
- **State:** open
- **Created:** 2025-08-11T20:34:05Z
- **Updated:** 2026-03-04T14:50:26Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5180

### Problem Description

OS:
NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"
CPU: 
model name	: AMD Ryzen 7 7840HS w/ Radeon 780M Graphics
GPU:
  Name:                    AMD Ryzen 7 7840HS w/ Radeon 780M Graphics
  Marketing Name:          AMD Ryzen 7 7840HS w/ Radeon 780M Graphics
  Name:                    gfx1103                            
  Marketing Name:          AMD Radeon 780M                    
      Name:                    amdgcn-amd-amdhsa--gfx1103         
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   


When the AMD 7840HS GPU crashes, how do I diagnose what is going wrong?
I have a simple program that multiplies 2 matrix together using rocblas cgemm.
I can run up to 30000 x 30000 OK, but when I get to 50000 x 50000 the GPU crashes.
I have set the gtt/ttm to be 60 GBytes, and the 50000 x 50000 sits at about 58 GB when viewed on amdgpu_top.
When it crashes, the display goes blank for about 60 seconds, but then recovers and works again, without any applications exiting.
I have compiled rocm from source, probably most recent git version, with gfx1103 as the target.
I don't mind if it is officially supported or not on the gfx1103. I wish to track down the cause and fix it.
Please can you point me to some instruction on how to diagnose the problem on the GPU ?

Note rocm 6.3.1 completed the 50000 x 50000 OK.
rocm 6.3.3 failed.
rocm 6.4.1 failed.
rocm 7.rcX failed.

An example program to reproduce the problem is here:
git@github.com:jcdutton/rocm-rust.git


### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

AMD Ryzen 7 7840HS w/ Radeon 780M Graphics

### GPU

AMD Ryzen 7 7840HS w/ Radeon 780M Graphics

### ROCm Version

Latest git version. Probably version 7rc something.

### ROCm Component

rocBLAS

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_