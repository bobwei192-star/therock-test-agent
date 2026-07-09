# Error: openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (

- **Issue #:** 1109
- **State:** closed
- **Created:** 2020-05-15T08:51:00Z
- **Updated:** 2021-06-03T09:37:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/1109


Ubuntu 20.04 . Intel i7-2600K (16Gb RAM) - Radeon RX480 6Gb  

sudo /opt/rocm/bin/rocminfo

```ROCk module is loaded
carlos is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```


strace /opt/rocm/bin/rocminfo


```
write(1, "\33[37mcarlos is member of video g"..., 41carlos is member of video group
) = 41
getpid()                                = 3136
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (No se pudo asignar memoria)
write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
) = 101
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -337, SEEK_CUR)                = -1 ESPIPE (Desplazamiento ilegal)
exit_group(4104)                        = ?
+++ exited with 8 +++
```
