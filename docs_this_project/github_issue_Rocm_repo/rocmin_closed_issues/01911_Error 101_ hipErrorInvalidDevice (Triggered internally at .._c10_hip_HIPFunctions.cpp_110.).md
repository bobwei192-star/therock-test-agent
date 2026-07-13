# Error 101: hipErrorInvalidDevice (Triggered internally at ../c10/hip/HIPFunctions.cpp:110.)

- **Issue #:** 1911
- **State:** closed
- **Created:** 2023-02-23T15:04:43Z
- **Updated:** 2024-04-26T05:38:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/1911

```
>>> import torch
>>> torch.cuda.is_available()
/home/rocm-user/.local/lib/python3.8/site-packages/torch/cuda/__init__.py:88: UserWarning: HIP initialization: Unexpected error from hipGetDeviceCount(). Did you run some cuda functions before calling NumHipDevices() that might have already set an error? Error 101: hipErrorInvalidDevice (Triggered internally at ../c10/hip/HIPFunctions.cpp:110.)
  return torch._C._cuda_getDeviceCount() > 0
False
>>>
```

Using your docker image with the AMD RADEON RX 7900 XT.
According to your documentation, the RDNA architecture is supported.