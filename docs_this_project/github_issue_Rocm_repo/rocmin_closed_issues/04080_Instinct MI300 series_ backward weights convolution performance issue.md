# Instinct MI300 series: backward weights convolution performance issue

- **Issue #:** 4080
- **State:** closed
- **Created:** 2024-12-03T22:19:26Z
- **Updated:** 2024-12-20T23:07:21Z
- **Labels:** Verified Issue, AMD Instinct MI300X, AMD Instinct MI300A, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4080

A performance issue affects certain tensor shapes during backward weights convolution when using FP16 or FP32 data types on Instinct MI300 series accelerators. This issue will be addressed in a future ROCm release.

To mitigate the issue during model training, set the following environment variables:
```shell
export MIOPEN_FIND_MODE=3
export MIOPEN_FIND_ENFORCE=3
```

These settings enable auto-tuning on the first occurrence of a new tensor shape. The tuning results are stored in the user database, eliminating the need for repeated tuning when the same shape is encountered in subsequent runs. See the [MIOpen](https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/workload.html#miopen) section in the workload optimization guide to learn more about MIOpen’s auto-tuning capabilities.