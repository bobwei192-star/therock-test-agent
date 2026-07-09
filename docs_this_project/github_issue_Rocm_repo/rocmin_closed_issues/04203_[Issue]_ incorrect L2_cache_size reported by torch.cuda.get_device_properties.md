# [Issue]: incorrect L2_cache_size reported by torch.cuda.get_device_properties

- **Issue #:** 4203
- **State:** closed
- **Created:** 2024-12-27T00:54:33Z
- **Updated:** 2025-05-30T16:32:51Z
- **Labels:** Under Investigation, MI300X, ROCm 6.2.4
- **URL:** https://github.com/ROCm/ROCm/issues/4203

### Problem Description

w/ `torch-2.6` `torch.cuda.get_device_properties` reports:
```
_CudaDeviceProperties(name='AMD Instinct MI300X', major=9, minor=4, 
gcnArchName='gfx942:sramecc+:xnack-', total_memory=196592MB, multi_processor_count=304, 
uuid=66333330-6463-3464-3030-646565323262, 
L2_cache_size=4MB)
```

It currently reports an invalid `L2_cache_size`- it reports the size of a single compute die and not of the whole accelerator. It's 4MB per compute die - but there is no information of how many compute dies there are or if it's suggesting that it's per die - so this is then misleading/incorrect name of the field.

There should be 8 in the case of MI300X and the total should be then 32MB.

I first thought it was a pytorch issue, but I was told that the issue comes from ROCm.

If you're on torch slack please see this thread:

https://pytorch.slack.com/archives/C3PDTEV8E/p1735067560696929?thread_ts=1735017298.875249&cid=C3PDTEV8E


### Operating System

Ubuntu

### CPU

not sure

### GPU

MI300X

### ROCm Version

ROCm 6.2.4

### ROCm Component

HIP

### Steps to Reproduce

`torch.cuda.get_device_properties()`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

torch=2.6.0a0+gitd6a066e
hip=6.2.41133-dd7f95766