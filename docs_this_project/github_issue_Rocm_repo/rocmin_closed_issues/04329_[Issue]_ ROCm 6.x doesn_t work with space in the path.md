# [Issue]: ROCm 6.x doesn't work with space in the path

- **Issue #:** 4329
- **State:** closed
- **Created:** 2025-02-02T17:52:37Z
- **Updated:** 2025-07-07T14:06:04Z
- **Labels:** Under Investigation, RX 6700 XT, ROCm 6.2
- **URL:** https://github.com/ROCm/ROCm/issues/4329

### Problem Description

I'm trying to use ROCm with ComfyUI and RX 6700 XT (gfx1031) on Debian 13. It works fine when I use ROCm 5.7 (pytorch 2.3.1+rocm5.7 with HSA_OVERRIDE_GFX_VERSION=10.3.0), but I can't any newer version to work. I get this error when running ROCm 6.2 (pytorch 2.5.1+rocm6.2):

```
RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.
```

Is there any way to make it work or am I stuck with ROCm 5.7? I've also tried running Ollama and the error is a bit different there:
```
ROCm error: no kernel image is available for execution on the device
```

### Operating System

Debian 13

### CPU

-

### GPU

RX 6700 XT

### ROCm Version

ROCm 6.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_