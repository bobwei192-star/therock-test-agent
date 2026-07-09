# [Issue]: HIP programs hang inside amdhip64.dll after main

- **Issue #:** 3418
- **State:** closed
- **Created:** 2024-07-12T21:33:35Z
- **Updated:** 2024-10-05T19:50:49Z
- **Labels:** Under Investigation, AMD Instinct MI300X, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3418

### Problem Description

Using the recently released HIP SDK for Windows 6.1.2 with Visual Studio 2022 17.10.4 and latest Radeon Software 24.6.1, compiling the simplest of SAXPY programs (my own, but also AMD's ROCm-examples one), when the program is compiled in Debug mode (both using the VS Extension and MSBuild or using CMake+Ninja), the program after leaving main hangs inside amdhip64.dll. Everything works as expected when compiled in Release mode.

![kép](https://github.com/user-attachments/assets/eea8e6ca-064e-4fe9-8a9f-3533ff59e2ae)

### Operating System

Windows 11 Pro (10.0.22631)

### CPU

AMD Ryzen 9 7945HX with Radeon Graphics

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.1.0

### ROCm Component

HIP

### Steps to Reproduce

1. Clone https://github.com/ROCm/rocm-examples/blob/develop/HIP-Basic/saxpy/main.hip
2. Build in Debug mode
3. Run
4. Profit

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Not really MI300X, but I can't select AMD Radeon(TM) 610M from the HW drop-down. I know this device isn't strictly speaking supported, but the issue doesn't seem to be related to the device itself. (I wouldn't want to go into the perception of the sparsity of the support matrix.)