# HIP_VISIBLE_DEVICES not working properly in ROCm 3.5

- **Issue #:** 1170
- **State:** closed
- **Created:** 2020-06-30T08:39:19Z
- **Updated:** 2022-10-18T23:23:35Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/1170

It seems that neither HIP_VISIBLE_DEVICES nor ROCR_VISIBLE_DEVICE is working properly anymore in ROCm 3.5 and newer. When running a program with 

```
HIP_VISIBLE_DEVICES= python training.py
```

all GPUs are used. The expected behavior is that all GPUs are hidden.

I tested this with Tensorflow version 2.2.

OS: Ubuntu 18.04.4
ROCm version: 3.5.1, using the rocm-dkms package