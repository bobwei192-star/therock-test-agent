# Unable to open /dev/kfd read-write: Cannot allocate memory

- **Issue #:** 1185
- **State:** closed
- **Created:** 2020-07-27T15:19:45Z
- **Updated:** 2023-12-19T16:18:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/1185

I installed rcom on my ubuntu, then I wrote the command `rcominfo` and this happened :
`ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
akuganteng is member of render group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.`