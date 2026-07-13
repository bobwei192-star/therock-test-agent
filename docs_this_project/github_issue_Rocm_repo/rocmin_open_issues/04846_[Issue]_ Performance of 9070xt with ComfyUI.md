# [Issue]: Performance of 9070xt with ComfyUI

- **Issue #:** 4846
- **State:** open
- **Created:** 2025-05-30T10:17:15Z
- **Updated:** 2026-06-26T15:24:14Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4846

### Problem Description

I'm using the default ComfyUI SDXL workflow with Ubuntu 24.04 and the proprietary AMD drivers. This is also the case using Fedora 42.

Issues:
- Using the default launch settings, the generation crashes with OOM errors
- Using tweaked settings, generation passes but is very slow

Results:

Clean Ubuntu 24.04 installation
AMD proprietary drivers
Python 3.10.17
Pytorch nightly
ROCm 6.4.1

```
export TORCH_COMMAND="--pre torch torchvision torchaudio pytorch-triton-rocm --index-url https://download.pytorch.org/whl/nightly/rocm6.4"

python ./main.py
```


|Card|Model|Steps|Resolution|Time|Notes|
|-----|------|------|----------|----|------|
|6900xt|SD1.5|20|512x512|2.42s|ROCm 6.3|
|9070xt|SD1.5|20|512x512|3.76s||
|6900xt|SDXL|20|1024x1024|15.16s|ROCm 6.3|
|9070xt|SDXL|20|1024x1024|FAIL|Crashed with out of memory|
|9070xt|SDXL|20|1024x1024|30.51s|Used tiled VAE decoder to avoid OOM failure|

Results 2:

Clean Ubuntu 24.04 installation
AMD proprietary drivers
Python 3.10.17
Pytorch nightly
ROCm 6.4.1

```
export PYTORCH_TUNABLEOP_ENABLED=1\
export TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1
export TORCH_COMMAND="--pre torch torchvision torchaudio pytorch-triton-rocm --index-url https://download.pytorch.org/whl/nightly/rocm6.4"

python ./main.py --use-pytorch-cross-attention 
```

|Model|Steps|Resolution|Speed|Time|Notes|
|-|-|-|-|-|-|
|SDXL|20|1024x1024|1.49it/s|34.56s||
|SDXL|20|1024x1024|1.5it/s|27.76s|Manual tiled VAE decoder|


### Operating System

Ubuntu 24.04

### CPU

AMD 7950x

### GPU

Radeon RX 9070xt

### ROCm Version

6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

- Install Ubuntu 24.04
- Install AMD proprietary drivers with ROCm
- Install Python 3.10.17
- Clone ComfyUI
- Start ComfyUI
- Use default workflow for SDXL

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_