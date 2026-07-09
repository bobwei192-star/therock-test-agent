# [Issue]: HIPCC not executing, fails with path error

- **Issue #:** 3680
- **State:** closed
- **Created:** 2024-09-04T22:15:03Z
- **Updated:** 2025-02-10T20:13:42Z
- **Labels:** Under Investigation, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3680

### Problem Description

I am trying to compile some of the HIP samples on my computer, I downloaded and installed the HIP SDK and everything seemed fine, I had to install perl, as mentioned in #2713, but then I tried to compile the vector add samples, and I get this output: 
```
PS C:\Users\suyda\dev\school\research\GPU Frameworks Project\ROCm\HIP-Examples\vectorAdd> hipcc .\vectoradd_hip.cpp -o .\vectoradd_hip.exe
'C:\Program' is not recognized as an internal or external command,
operable program or batch file.

failed to execute:C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\bin/nvcc  -Wno-deprecated-gpu-targets  -isystem C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3/include -isystem "include" -x cu  -Wno-deprecated-gpu-targets -lcuda -lcudart -LC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3/lib64  .\vectoradd_hip.cpp -o ".\vectoradd_hip.exe"
PS C:\Users\suyda\dev\school\research\GPU Frameworks Project\ROCm\HIP-Examples\vectorAdd>
```

Not sure what to do. 

### Operating System

Windows 11

### CPU

AMD Ryzen 7 7600X

### GPU

AMD Instinct MI250

### ROCm Version

ROCm 6.1.0

### ROCm Component

HIPCC

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

I don't actually have an MI250, it is making me pick a gpu anyway to report the issue. 