# [Issue]: Comfy_UI hipblasLT not supported for Radeon 7900XT and HSA_STATUS_ERROR_OUT_OF_REGISTERS error

- **Issue #:** 4437
- **State:** closed
- **Created:** 2025-03-03T16:32:35Z
- **Updated:** 2025-03-19T11:55:31Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT, ROCm 6.2.0
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4437

### Problem Description

I'm reporting this issue on behalf of the OP from [this post on discuss.pytorch.org](https://discuss.pytorch.org/t/comfy-ui-attempting-to-use-hipblaslt-on-a-unsupported-architecture/215776).
I've copied the stdout/stderr here

```
Total VRAM 20464 MB, total RAM 63432 MB
pytorch version: 2.6.0.dev20241122+rocm6.2
Set vram state to: NORMAL_VRAM
Device: cuda:0 Radeon RX 7900 XT : native
Using sub quadratic optimization for attention, if you have memory or speed issues try using: --use-split-cross-attention
[Prompt Server] web root: /home/sersys/pyproj/ComfyUI-0.3.12/web

Import times for custom nodes:
   0.0 seconds: /home/sersys/pyproj/ComfyUI-0.3.12/custom_nodes/websocket_image_save.py

Starting server

To see the GUI go to: http://127.0.0.1:8188
got prompt
model weight dtype torch.float16, manual cast: None
model_type EPS
Using split attention in VAE
Using split attention in VAE
VAE load device: cuda:0, offload device: cpu, dtype: torch.float32
CLIP/text encoder model load device: cuda:0, offload device: cpu, current: cpu, dtype: torch.float16
Requested to load SDXLClipModel
loaded completely 9.5367431640625e+25 1560.802734375 True
/home/sersys/pyproj/ComfyUI-0.3.12/comfy/ops.py:64: UserWarning: Attempting to use hipBLASLt on an unsupported architecture! Overriding blas backend to hipblas (Triggered internally at /pytorch/aten/src/ATen/Context.cpp:296.)
  return torch.nn.functional.linear(input, weight, bias)
Requested to load SDXL
loaded completely 9.5367431640625e+25 4897.0483474731445 True
  0%|                                                                | 0/20 [00:00<?, ?it/s]:0:rocdevice.cpp            :2984: 93862815501 us: [pid:318562 tid:0x7f122e5ff640] Callback: Queue 0x7f0ed8000000 aborting with error : HSA_STATUS_ERROR_OUT_OF_REGISTERS: Kernel has requested more VGPRs than are available on this agent code: 0x2d
Aborted (core dumped)
```

There are two issues here that the OP is concerned about : 

*The first is a non-fatal warning*
There appears to be a warning issued by pytorch stating that the Radeon RX 7900XT is not supported by the HIPBlasLT backend. There is no ROCm documentation that indicates this GPU is not supported by HIPBlasLT; in fact the [compatibility matrix](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-gpus) suggests it is supported. Is this an issue with Pytorch or is this GPU not actually supported in hipblaslt ?

This being said, it does appear that they are not on a [supported Linux kernel](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-operating-systems) ( 6.12.9 ); however, no errors appear to indicate specifically that this is the culprit.

*The second issue appears fatal*
During the execution of `torch.nn.functional.linear`, the code aborts with an `HSA_STATUS_ERROR_OUT_OF_REGISTERS` error. I suspect this an issue with MIOpen; perhaps it's targeting the wrong architecture and over-allocating vgpr ? My understanding is that some of these torch functions are compiled on the fly during the first execution and this is handled by MIOpen. Any guidance you can provide on further diagnosing the problem here would be great.



### Operating System

Debian GNU/Linux 12

### CPU

AMD Ryzen 9 7900X 12-Core Processor

### GPU

Radeon 7900 XT

### ROCm Version

ROCm 6.2.0

### ROCm Component

Pytorch, MIOpen

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_