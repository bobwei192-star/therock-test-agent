# [Issue]: 7900xtx Graphics Pipeline at 100% when idling with a loaded llama.cpp model

- **Issue #:** 2777
- **State:** closed
- **Created:** 2024-01-04T19:17:54Z
- **Updated:** 2024-05-17T19:21:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/2777

### Problem Description

Not a major issue, but it would be nice to find a fix for this.

When I load an LLM model into GPU's VRAM, Radeon TOP shows the Graphics Pipeline at 100% all the time. `rocm-smi` shows 100-110 watt power use. I did not observe this behavior with my rx6600 and 6700xt on the same machine. On those RDNA2 GPUs, the Graphics Pipeline goes to 0% when the GPU is idling with the model loaded and occupying the VRAM. 

Exiting koboldCPP (which uses llama.cpp backend) returns the GPU to normal and it then idles at low ~20 watts.

I'm using https://github.com/YellowRoseCx/koboldcpp-rocm with hipBLAS support and I'm using ROCm 6:

```sh

rocm6.0.0/jammy 6.0.0.60000-91~22.04 amd64
```

My system info:

```sh

$ echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
OS:
NAME="Pop!_OS"
VERSION="22.04 LTS"
```

```sh

$ echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
CPU:
model name      : AMD Ryzen 9 3950X 16-Core Processor
```

```sh

$  echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
GPU:
  Name:                    AMD Ryzen 9 3950X 16-Core Processor
  Marketing Name:          AMD Ryzen 9 3950X 16-Core Processor
  Name:                    gfx1100
  Marketing Name:          Radeon RX 7900 XTX
      Name:                    amdgcn-amd-amdhsa--gfx1100


### Operating System

Pop_OS! (based on Ubuntu 22.04 LTS)

### CPU

Ryzen 9 3950X

### GPU

AMD Radeon RX 7900 XTX

### Other

_No response_

### ROCm Version

ROCm 6.0.0

### ROCm Component

ROCm

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_