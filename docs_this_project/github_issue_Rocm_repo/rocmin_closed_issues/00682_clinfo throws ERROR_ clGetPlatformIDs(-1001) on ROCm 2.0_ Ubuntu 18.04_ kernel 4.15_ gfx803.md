# clinfo throws ERROR: clGetPlatformIDs(-1001) on ROCm 2.0; Ubuntu 18.04; kernel 4.15; gfx803

- **Issue #:** 682
- **State:** closed
- **Created:** 2019-01-19T22:42:05Z
- **Updated:** 2019-02-08T00:47:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/682

Install proceeds without error, but when I try to test after reboot, an error occurs:
```
user@host:~$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
```

System info:
Ubuntu 18.04 (4.15.0-43-generic)
CPU: i7-5820k
GPU: gfx803 (RX480)
rocm-dkms 2.0.89

Additional info:
```
user@host:~$ dmesg | grep kfd
[    1.832810] kfd kfd: Allocated 3969056 bytes on gart
[    1.832933] kfd kfd: added device 1002:67df
```
