# [Issue]: RX 9070 / gfx1201: massive prefill slowdown unless ROCBLAS_USE_HIPBLASLT=0 is set

- **Issue #:** 6203
- **State:** closed
- **Created:** 2026-05-07T07:58:49Z
- **Updated:** 2026-06-11T15:17:56Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6203

### Problem Description

I have Radeon R9700. I noticed in ollama logs:

rocblaslt error: Cannot read "TensileLibrary_lazy_gfx1201.dat": No such file or directory
rocblaslt error: Could not load "TensileLibrary_lazy_gfx1201.dat"

as I run ollama in podman container, I mounted the 7.2.3 libraries from the host in the quadlet:

Volume=/opt/rocm-7.2.3/lib/hipblaslt/library:/lib/ollama/rocm/hipblaslt/library:ro
Environment=HIPBLASLT_TENSILE_LIBPATH=/lib/ollama/rocm/hipblaslt/library

then the error in the podman/ollama logs was gone. 

However, I got a MASSIVE hit to performance. A medium-sized prompt run against qwen3.6 took 4 minutes to complete. Mostly spent in cold pre-filling.

when i eventually commented out these 7.2.3 libraries and instead added:
Environment=ROCBLAS_USE_HIPBLASLT=0

the performace was back to normal, the same prompt took like 20 secs to execute.

Took me a whole day of scratching my head (and help from Opus) to figure it out... :)



### Operating System

Debian 13 Trixie

### CPU

AMD Ryzen 7 9700X 

### GPU

 AMD Radeon AI PRO R9700 

### ROCm Version

ROCM 7.2.3

### ROCm Component

_No response_

### Steps to Reproduce

create an ollama podman container and provide the host ROCm 7.2.3 libraries to it:

# Provide the missing hipBLASLt kernel directory from the host
Volume=/opt/rocm-7.2.3/lib/hipblaslt/library:/lib/ollama/rocm/hipblaslt/library:ro
Environment=HIPBLASLT_TENSILE_LIBPATH=/lib/ollama/rocm/hipblaslt/library

then run a medium sized prompt (50k long) against it:

time curl http://localhost:11434/api/chat -d @prompt_file.json
real    4m12.321s

when the quadlet config for ollama is changed to:
#Volume=/opt/rocm-7.2.3/lib/hipblaslt/library:/lib/ollama/rocm/hipblaslt/library:ro
#Environment=HIPBLASLT_TENSILE_LIBPATH=/lib/ollama/rocm/hipblaslt/library
Environment=ROCBLAS_USE_HIPBLASLT=0

the same prompt runs much faster:
time curl http://localhost:11434/api/chat -d @prompt_file.json
real    0m29.903s



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_