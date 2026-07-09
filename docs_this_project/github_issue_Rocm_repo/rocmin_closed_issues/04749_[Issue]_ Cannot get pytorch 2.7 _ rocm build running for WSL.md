# [Issue]: Cannot get pytorch 2.7 + rocm build running for WSL

- **Issue #:** 4749
- **State:** closed
- **Created:** 2025-05-16T14:08:18Z
- **Updated:** 2025-07-29T12:44:35Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4749

### Problem Description

Hey,
I'm working at Transformer Lab and recently took on what I thought would be a straightforward task - setting up ROCm for Windows to run some ML workloads. Two weeks and countless frustrations later, I'm reaching out to see if anyone here has successfully navigated these waters.
I initially got things working on my Linux machine with the same hardware configuration. After that to test if the integration works on WSL, I did a dualboot to Windows and opened WSL (Ubuntu 24.04). For hardware context, we have a single AMD Radeon 7900 XTX (gfx11100).

Here's what we've tried and the roadblocks we're hitting:

## WSL Integration Issues:

- Attempted to set up our API installation on bare-metal WSL
- Discovered it's impossible to set up rocm-smi on WSL due to limitations mentioned on the AMD installer page
- This makes tracking GPU usage extremely difficult since we can't properly use the pyrsmi package (which is supposed to be the ROCm equivalent to CUDA's pynvml)

## PyTorch Installation Nightmares on WSL:

- Official installation docs recommend using pre-built binaries
- Problem is, there are no pre-built binaries available yet for torch 2.7 + rocm 6.4
- Tried using the Linux wheel (torch2.7+rocm6.3) but it doesn't work on WSL - torch.cuda.is_available() can't detect anything
- Even tried the classic AMD installer trick of replacing runtime libraries, but no success with this torch2.7+rocm6.3 installation

For context, we installed ROCm 6.4, but we're trying to download ROCm 6.3 packages for PyTorch since the 6.4 wheels aren't available yet.

How do you all run ML workloads on Windows and ROCm with a current version of PyTorch?!

Really hoping to tap into the collective knowledge of this community, as the official documentation hasn't been much help with our specific use case.

Thanks in advance!

### Operating System

WSL (Ubuntu 24.04)

### CPU

AMD Ryzen 5 7600X

### GPU

1 x AMD Radeon 7900 XTX

### ROCm Version

ROCm 6.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_