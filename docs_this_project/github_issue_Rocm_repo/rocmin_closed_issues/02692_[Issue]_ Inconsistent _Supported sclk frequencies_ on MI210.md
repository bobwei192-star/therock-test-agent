# [Issue]: Inconsistent *Supported sclk frequencies* on MI210

- **Issue #:** 2692
- **State:** closed
- **Created:** 2023-12-06T14:59:51Z
- **Updated:** 2024-09-05T16:16:03Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/2692

### Problem Description

I am observing a strange issue regarding clock frequency settings on MI210: I see different *supported sclk frequencies* depending on whether the *performance level* is set to auto (e.g., reseting the settings with `rocm_smi -r`) or manual (setting a particular frequency manually with rocm-smi --setclock sclk 0/1/2).

I see the following supported sclk frequencies after running `rocm-smi --setclock sclk 0`: level0: 500Mhz, level1: 1700Mhz
I see the following supported sclk frequencies after running `rocm_smi -r`: level0: 500Mhz, level1: 800Mhz, level2: 1700Mhz

This means that the levels are inconsistent in different modes (e.g., auto/manual) and therefore I cannot set the frequency to 800Mhz using --setclock flag, and I can only set it to 800Mhz when using -r flag!

I don't see a similar issue on MI100 with an older version of the rocm stack (5.4.3) and driver (5.16.9.22.20).



### Operating System

SLES 15-SP5

### CPU

AMD EPYC 7773X 64-Core Processor

### GPU

MI210

### ROCm Version

5.7.1

### ROCm Component

Driver version: 6.2.4

### Steps to Reproduce

rocm-smi --setclock sclk 0
rocm-smi -s
rocm-smi -r
rocm-smi -s
rocm-smi --setclock sclk 1
rocm-smi -s
rocm-smi -r
rocm-smi -s
rocm-smi --setclock sclk 2
rocm-smi -s
rocm-smi -r
rocm-smi -s


### Output of /opt/rocm/bin/rocminfo --support


[support.txt](https://github.com/RadeonOpenCompute/ROCm/files/13587454/support.txt)



