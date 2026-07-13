# [Issue]: Error -22

- **Issue #:** 4533
- **State:** closed
- **Created:** 2025-03-26T14:32:41Z
- **Updated:** 2025-03-27T15:09:24Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4533

### Problem Description

I am running ubuntu 24.04 lts 
OS:
NAME="Ubuntu"
VERSION="24.04.2 LTS (Noble Numbat)"
With AMD cpu 
CPU: 
model name	: AMD EPYC 7313 16-Core Processor

rocm driver installed  but gpus are not seen by the os always the same error 


dmesg  | grep e3:00.0
[    6.581503] pci 0000:e3:00.0: [1002:738c] type 00 class 0x038000 PCIe Legacy Endpoint
[    6.581541] pci 0000:e3:00.0: BAR 0 [mem 0x4f800000000-0x4ffffffffff 64bit pref]
[    6.581566] pci 0000:e3:00.0: BAR 2 [mem 0x50000000000-0x500001fffff 64bit pref]
[    6.581582] pci 0000:e3:00.0: BAR 4 [io  0xf000-0xf0ff]
[    6.581598] pci 0000:e3:00.0: BAR 5 [mem 0xc2200000-0xc227ffff]
[    6.581613] pci 0000:e3:00.0: ROM [mem 0xc2280000-0xc229ffff pref]
[    6.581808] pci 0000:e3:00.0: PME# supported from D1 D2 D3hot D3cold
[    6.687727] pci 0000:e3:00.0: Adding to iommu group 89
[   51.820381] amdgpu 0000:e3:00.0: enabling device (0000 -> 0003)
[   51.829903] amdgpu 0000:e3:00.0: amdgpu: Fetched VBIOS from platform
[   51.831796] amdgpu 0000:e3:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[   71.836015] amdgpu 0000:e3:00.0: amdgpu: gpu post error!
[   71.836341] amdgpu 0000:e3:00.0: amdgpu: Fatal error during GPU init
[   71.853942] amdgpu 0000:e3:00.0: amdgpu: amdgpu: finishing device.
[   71.871281] amdgpu: probe of 0000:e3:00.0 failed with error -22

    WARNING: No AMD GPUs specified
    ===================================== ROCm System Management Interface       =====================================
    =============================================== Concise Info  ===============================================
    Device  Node  IDs           Temp    Power  Partitions          SCLK  MCLK  Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,  GUID)  (Edge)  (Avg)  (Mem, Compute, ID)                                                  
         ============================================================================================. ================
                    ============================================================================================================
      =========================================== End of ROCm SMI Log  ============================================

installed packages 

```
dpkg -l | grep rocm
ii  rocm                                 6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) software stack meta package
ii  rocm-cmake                           0.14.0.60303-74~24.04                   amd64        rocm-cmake built using CMake
ii  rocm-core                            6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-dbgapi                          0.77.0.60303-74~24.04                   amd64        Library to provide AMD GPU debugger API
ii  rocm-debug-agent                     2.0.3.60303-74~24.04                    amd64        Radeon Open Compute Debug Agent (ROCdebug-agent)
ii  rocm-dev                             6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-developer-tools                 6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                     1.0.0.60303-74~24.04                    amd64        Radeon Open Compute - device libraries
ii  rocm-gdb                             15.2.60303-74~24.04                     amd64        ROCgdb
ii  rocm-hip-libraries                   6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime                     6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-runtime-dev                 6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-hip-sdk                         6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-language-runtime                6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-llvm                            18.0.0.25012.60303-74~24.04             amd64        ROCm core compiler
ii  rocm-ml-libraries                    6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-ml-sdk                          6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl                          2.0.0.60303-74~24.04                    amd64        clr built using CMake
ii  rocm-opencl-dev                      2.0.0.60303-74~24.04                    amd64        clr built using CMake
ii  rocm-opencl-runtime                  6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-opencl-sdk                      6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-openmp-sdk                      6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) OpenMP Software development Kit.
ii  rocm-smi-lib                         7.4.0.60303-74~24.04                    amd64        AMD System Management libraries
ii  rocm-utils                           6.3.3.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                             1.0.0.60303-74~24.04                    amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool

```


### Operating System

Ubuntu 24.04 LTS

### CPU

AMD EPYC 7313 

### GPU

AMD MI100 Instinct

### ROCm Version

rocm 6.3.3

### ROCm Component

_No response_

### Steps to Reproduce

clean ubuntu install than follow install instructions from https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/amdgpu-installer/amdgpu-installer-ubuntu.html

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_