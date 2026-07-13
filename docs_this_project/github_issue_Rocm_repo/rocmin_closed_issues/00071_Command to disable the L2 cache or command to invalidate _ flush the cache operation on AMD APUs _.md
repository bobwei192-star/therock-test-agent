# Command to disable the L2 cache or command to invalidate / flush the cache operation on AMD APUs ? 

- **Issue #:** 71
- **State:** closed
- **Created:** 2017-01-09T04:32:25Z
- **Updated:** 2017-07-02T17:19:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/71

I would like to know, when a memory is reserved in the GPU RAM, then when GPU tries to modify it, the data will be put into L2 , L1 cache before going to ALU. My question is can I flush the cache before a third party other than GPU tries to access that memory region? Is there an ISA for the same . I am trying to use AMD GPU for some research. Since ROCM is open source I want to make use of it. OpenCL also runs on top of Rocm, so will make use of the same. 