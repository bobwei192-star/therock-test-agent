# OpenCL alongside ROCm?

- **Issue #:** 12
- **State:** closed
- **Created:** 2016-05-18T08:14:54Z
- **Updated:** 2016-05-19T19:26:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/12

Hi - I was wondering how to have OpenCL available on a rocm enabled kernel with ubuntu 14.04.4. I followed the installation instructions in this repo and installed the opencl icd through `ocl-icd-opencl-dev` but clinfo just prints:

```
$ clinfo
I: ICD loader reports no usable platforms
```

whereas lspci correctly reports the GPU(s):

```
$ lspci -v |grep "VGA controller"
02:00.0 VGA compatible controller: NVIDIA Corporation GF119 [NVS 310] (rev a1) (prog-if 00 [VGA controller])
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca) (prog-if 00 [VGA controller])
```

but rocm-smi also chokes a bit:

```
$ sudo /opt/rocm/bin/rocm-smi -a


===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]          : Temperature: 38.0c
GPU[1]          : Unable to display temperature
============================================================================
============================================================================
GPU[0]          : GPU Clock Level: 0 (300Mhz)
GPU[0]          : GPU Memory Clock Level: 0 (500Mhz)
GPU[1]          : PowerPlay not enabled - Cannot display clocks
============================================================================
============================================================================
GPU[0]          : Fan Level: 48 (18.82)%
GPU[1]          : PowerPlay not enabled - Cannot display fan speed
============================================================================
============================================================================
GPU[0]          : Current PowerPlay Level: auto
GPU[1]          : PowerPlay not enabled - Cannot display Performance Level
============================================================================
============================================================================
GPU[0]          : Supported GPU clock frequencies on GPU0
GPU[0]          : 0: 300Mhz *
GPU[0]          : 1: 508Mhz 
GPU[0]          : 2: 717Mhz 
GPU[0]          : 3: 874Mhz 
GPU[0]          : 4: 911Mhz 
GPU[0]          : 5: 944Mhz 
GPU[0]          : 6: 974Mhz 
GPU[0]          : 7: 1000Mhz 
GPU[0]          : 
GPU[0]          : Supported GPU Memory clock frequencies on GPU0
GPU[0]          : 0: 500Mhz *
GPU[0]          : 
GPU[1]          : PowerPlay not enabled - Cannot display clocks
============================================================================
===================          End of ROCm SMI Log         ===================
```

Any hint would be appreciated.
P
