# [Feature]:  request __shfl_xor_sync  in rocm

- **Issue #:** 3917
- **State:** closed
- **Created:** 2024-10-18T02:21:09Z
- **Updated:** 2025-05-04T14:11:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/3917



hi, rocm expert, 
 during our recent project, we need a same function as cuda, __shfl_xor_sync().

however looks recent [rocm 6.2.2](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/tables/CUDA_Device_API_supported_by_HIP.html) has not supported yet:

|   |     |    |    | 
|---|---|---|---|
__shfl_xor | 9.0 |      __shfl_xor | 1.6.0 | 
__shfl_xor_sync |   |   |   |  


is there other primitives as quick replacement ? 

Thanks
David 



### Operating System

_No response_

### GPU

mi300

### ROCm Component

6.2.2