# Unable to install ROCm 1.8.2 on CentOS 7.4 due to dependency on libOpenCL.so.1

- **Issue #:** 472
- **State:** closed
- **Created:** 2018-07-27T00:22:01Z
- **Updated:** 2018-08-31T00:12:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/472

Clean system with CentOS 7.4 and `kernel-headers  kernel-devel  devtoolset-7  dkms`.

```
# yum install rocm-dkms
...
---> Package rocm-dkms.x86_64 0:1.8.192-1 will be installed
...
--> Running transaction check
---> Package rocm-opencl-devel.x86_64 0:1.2.0-2018071635 will be installed
--> Processing Dependency: libOpenCL.so.1()(64bit) for package: rocm-opencl-devel-1.2.0-2018071635.x86_64
--> Finished Dependency Resolution
Error: Package: rocm-opencl-devel-1.2.0-2018071635.x86_64 (rocm)
           Requires: libOpenCL.so.1()(64bit)
```

Running `yum whatprovides libOpenCL.so.1` shows `rocm-opencl`, which I was able to install successfully, but I still cannot resolve the dependency error for `rocm-opencl-devel`.