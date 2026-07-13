# No AMD GPUs specified

- **Issue #:** 1742
- **State:** closed
- **Created:** 2022-05-20T17:22:08Z
- **Updated:** 2024-02-02T22:43:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/1742

Hi can you please help me with this? I am remotly connected to a miner rig with 12 AMD GPUs. The OS is Ubuntu 18.04.6 LTS. 

``` 
Graphics:  Card-1: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-2: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-3: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-4: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-5: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-6: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-7: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-8: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-9: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-10: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-11: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Card-12: Advanced Micro Devices [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]
           Display Server: N/A
           drivers: amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu,amdgpu
           tty size: 212x85 Advanced Data: N/A out of X
```

As you can see all of them have amdgpu drivers installed. After following official documentation I have managed to install every single version of rocm from 3.0 to 5.1. Everytime I had the same problem:

```
 ======================= ROCm System Management Interface =======================
WARNING: No AMD GPUs specified
================================= Concise Info =================================
GPU  Temp  AvgPwr  SCLK  MCLK  Fan  Perf  PwrCap  VRAM%  GPU%
================================================================================
============================= End of ROCm SMI Log ==============================

```
No devices were recognized. I need rocm for tensorflow AI project. But have no clue why it does not work. Please help me. If any additional information is needed please tell me what to provide. 

One more piece of info that maybe important. There is/was a cuda installed on this ubuntu. 
