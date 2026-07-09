# Hiding/Disabling one GPU in a multiGPU system

- **Issue #:** 711
- **State:** closed
- **Created:** 2019-02-17T23:17:26Z
- **Updated:** 2019-02-19T15:27:52Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/711

Background: ubuntu 18.04, ROCm 2.1
GPUs: Vega FE*2, Radeon VII*1

Would there be a way to hide one GPU in the system?
I am trying to run some tests with the GPUs, but many of the benchmark scripts do not allow selecting a particular GPU device. Thus if I can hide the GPU from the software it will be very helpful.

With Nvidia's card, it seems like this can be done by "CUDA_VISIBLE_DEVICES" to hide a GPU from a test. Would there be a similar feature in ROCm?