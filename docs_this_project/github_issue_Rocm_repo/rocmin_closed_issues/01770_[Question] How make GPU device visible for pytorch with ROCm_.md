# [Question] How make GPU device visible for pytorch with ROCm?

- **Issue #:** 1770
- **State:** closed
- **Created:** 2022-07-21T13:11:28Z
- **Updated:** 2024-03-31T14:06:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1770

I pulled docker and tried this:
```
python -c 'import torch; print(torch.cuda.is_available());'
```
and got this
```
/opt/conda/lib/python3.7/site-packages/torch/cuda/__init__.py:82: 
UserWarning: HIP initialization: Unexpected error from hipGetDeviceCount(). 
Did you run some cuda functions before calling NumHipDevices() that might have already set an error? 
Error 101: hipErrorInvalidDevice (Triggered internally at  /var/lib/jenkins/pytorch/c10/hip/HIPFunctions.cpp:110.)
  return torch._C._cuda_getDeviceCount() > 0
False
```
Although I can see I have gpu:
```
  *-display UNCLAIMED       
       description: VGA compatible controller
       product: Vega 10 [Radeon Instinct MI25 MxGPU]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 1
       bus info: pci@82fa:00:00.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pciexpress msi msix vga_controller cap_list
       configuration: latency=0
       resources: iomemory:f0-ef iomemory:f0-ef memory:fe0000000-fefffffff memory:ff0000000-ff01fffff memory:40880000-408fffff 
```

my issue is similar to #1638 
and I would like to know if there is any way I can run pytorch code on AMD GPU using azure NV4as instance.
