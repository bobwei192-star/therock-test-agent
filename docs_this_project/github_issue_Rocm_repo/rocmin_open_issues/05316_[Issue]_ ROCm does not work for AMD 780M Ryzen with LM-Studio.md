# [Issue]: ROCm does not work for AMD 780M Ryzen with LM-Studio

- **Issue #:** 5316
- **State:** open
- **Created:** 2025-09-16T03:00:01Z
- **Updated:** 2026-06-29T12:03:39Z
- **Labels:** Under Investigation, status: assessed
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5316

### Problem Description

I keep trying to use LM Studio with Rocm drivers for 890M AMD Ryzen and have had no success, even with HSA_OVERRIDE_GFX_VERSION="11.0.2" lm-studio flag that should make it easier for the program to access rocm.

LM studio is one of the best programs if not the best program for local AI Models and it's surprising to me that it's this hard to get it to work when there is a rocm linux extension in the program. (ROCm llama.cpp (Linux)
v1.50.2 Engine Not Compatible AMD ROCm accelerated llama.cpp engine.) It keeps not detecting the hardware and other users have shared similar experiences.

Many Nvidia users do not have the same problems with using AI models locally and using the full potential of their chipsets and I wish AMD prioritized making it easier for non-developers to be able to use their products for learning about LLMs.

There is still an issue open on this topic for lm studio:
https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/426

I am not sure if this is just lm studio not implementing rocm but that extension shows.

### Operating System

Pop! OS 22.04

### CPU

Amd Ryzen 8840U

### GPU

AMD 780M Ryzen

### ROCm Version

6.4.3

### ROCm Component

_No response_

### Steps to Reproduce

Have Ryzen 8840U and 780M Ryzen GPU
Download LM studio
Install ROCm Repo
Install ROCm using AMD instructions
Run LM Studio and hope it detects ROCm
ROCm not detected and slower Vulkan process is used
AI LLM is much slower

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

rocminfo
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
...
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 8840U w/ Radeon 780M Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 8840U w/ Radeon 780M Graphics
...
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1103                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
  Vendor Name:             AMD                                


### Additional Information

_No response_