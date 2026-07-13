# [Issue]: OpenCL Crashes & Unexpected Behavior

- **Issue #:** 5678
- **State:** closed
- **Created:** 2025-11-20T00:12:33Z
- **Updated:** 2026-01-14T18:40:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/5678

### Problem Description

I am experiencing issues with OpenCL and AMD GPUs where it crashes on Linux and on Windows it does not crash but results are clearly not correct. I'm not quite sure what part is failing but it seems like maybe it is memory copies...? From what I've gathered from the crash files maybe it is switching between fine and corse grain memory types? I'm not an expert that is just from googling and trying to look for causes.

I am the developer of this software and these issues are being reported by some of my users. 

Please see the attached crash file.

Are there any steps to follow to troubleshoot this?

[crash.untitled.loris_53861_log.txt](https://github.com/user-attachments/files/23639476/crash.untitled.loris_53861_log.txt)

It does work properly on CPUs and on other GPU vendors. 

### Operating System

ALL

### CPU

ALL

### GPU

ALL

### ROCm Version

 6.4.x

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_