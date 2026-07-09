# Enabling xla on tensorflow-rocm with Rocm 5.2.3?

- **Issue #:** 1796
- **State:** closed
- **Created:** 2022-08-23T18:19:27Z
- **Updated:** 2023-12-19T01:55:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1796

I have a gfx1030 card l, Rocm 5.2.3 and currently running into xla issues with tensorflow.
My GPU can do pytorch model fine, can do tensorflow fine, without xla. With xla however, I got this error: ````bitcode module not found at ./opencl.bc````

Am I missing something during the install process (because I installed with ````rocm```` usecase).

How to get my device running tensorflow training with xla?
Thank you 