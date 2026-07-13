# amdgpu XXXX:XX:XX.X: kfd not supported on this ASIC (RX 550, ROCm 1.9, Linux 4.19, amdgpu)

- **Issue #:** 539
- **State:** closed
- **Created:** 2018-09-16T13:35:51Z
- **Updated:** 2019-01-08T15:45:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/539

First of all thanks for releasing a ROCm version compatible with mainline kfd. Now I can finally use my Vega64 with newer kernels.

However, my problem occurs when I try to use my RX ~~560~~ 550 as an OpenCL device.  
Apparently mainline kernels do not have kfd support for these cards (yet?).

Is there a workaround for using a RX ~~560~~ 550 with ROCm?

My system details:  
Ubuntu 18.04  
Kernel 4.19-rc3
ROCm 1.9.211
Using `amdgpu` as driver

```
$ dmesg | grep -i kfd
[    1.549222] kfd kfd: Initialized module
[    1.549574] amdgpu XXXX:XX:XX.X: kfd not supported on this ASIC
```
```
$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104
```
```
$ /opt/rocm/opencl/bin/x86_64/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)
```