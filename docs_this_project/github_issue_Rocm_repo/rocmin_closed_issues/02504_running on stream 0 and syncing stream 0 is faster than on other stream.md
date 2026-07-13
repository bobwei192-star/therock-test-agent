# running on stream 0 and syncing stream 0 is faster than on other stream

- **Issue #:** 2504
- **State:** closed
- **Created:** 2023-09-27T18:01:42Z
- **Updated:** 2024-08-12T19:22:23Z
- **Labels:** hardware:Radeon
- **URL:** https://github.com/ROCm/ROCm/issues/2504

I tried two approaches to run a program. In the first approach, I launch all the computation and rccl kernels on stream 0, and use hipStreamSynchronize to sync with stream 0 to ensure all the kernels are completed. In the second approach, I hipStreamCreate a new stream and launch all the kernels on it. Also, I use hipStreamSynchronize to sync with the created stream in the end. It's a bit surprising to me that approach 0 is 25% faster than approach 1. Is this an expected behavior? 