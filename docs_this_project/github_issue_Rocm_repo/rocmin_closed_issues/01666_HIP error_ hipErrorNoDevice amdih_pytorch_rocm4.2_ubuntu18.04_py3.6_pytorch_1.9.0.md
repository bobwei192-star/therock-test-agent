# HIP error: hipErrorNoDevice amdih/pytorch:rocm4.2_ubuntu18.04_py3.6_pytorch_1.9.0 

- **Issue #:** 1666
- **State:** closed
- **Created:** 2022-02-07T10:38:06Z
- **Updated:** 2022-02-09T09:24:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/1666

Code produces HIP error: hipErrorNoDevice in 

```
#Training
learn.fit_one_cycle(3, lr_max=3e-5, cbs=fit_cbs)
```

while rocminfo confirms there are GPUs (not provided the details for confidentiality reason)

[fine-tuning-bart-text-summarization.txt](https://github.com/RadeonOpenCompute/ROCm/files/8014462/fine-tuning-bart-text-summarization.txt)
