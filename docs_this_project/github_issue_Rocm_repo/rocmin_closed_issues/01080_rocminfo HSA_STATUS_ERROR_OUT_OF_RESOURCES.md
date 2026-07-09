# rocminfo HSA_STATUS_ERROR_OUT_OF_RESOURCES

- **Issue #:** 1080
- **State:** closed
- **Created:** 2020-04-12T00:56:03Z
- **Updated:** 2021-03-17T07:45:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1080

Ubuntu 19.10
Kernel 5.3.0-46-generic
rocm-dkms 3.3.0-19
RX 580
E5 2680v2

When I run **rocminfo**, I get this error
ROCk module is loaded
xeon is member of video group
`hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
`


But if I run it as **root**, it works as intended
`sudo /opt/rocm/bin/rocminfo`

This problem started with the latest rocm

EDIT:
I got it to work by installing rocm 3.1 first and then upgrading to 3.3