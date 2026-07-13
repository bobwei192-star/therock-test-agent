# WSL2 rocminfo Issue

- **Issue #:** 1361
- **State:** closed
- **Created:** 2021-01-16T15:21:53Z
- **Updated:** 2021-01-18T07:35:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/1361

I've tried to install rocm according to the [installation guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html), to use my RX580 GPU with TensorFlow.

When I came to step 8, I got the following error:
`/opt/rocm/bin/rocminfo`

> ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
Failed to get user name to check for video group membership
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

My WinVer: 10.0.21292.0
WLS2 - Ubuntu: 20.04

Is there any way to use my RX580 GPU with WSL2 or should I do a separate installation for Ubuntu?