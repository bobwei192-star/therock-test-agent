# CU Masking access

- **Issue #:** 1110
- **State:** closed
- **Created:** 2020-05-16T18:19:19Z
- **Updated:** 2020-09-10T16:17:11Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/1110

What is the intended way to use the CU Masking feature available in ROCM. I can see both the driver, Thunk and runtime have code for CU Masking. Yet is not clear how to use it. The calls to both the APIs in Thunk and ROCR require some sort of queue to pass to it. Its not clear how this queue is created and how to use it from something like HIP . Any userspace example that demonstrates this will be really helpful.Thanks