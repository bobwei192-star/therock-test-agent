# Provide matching debuginfo packages for OpenSUSE

- **Issue #:** 1795
- **State:** closed
- **Created:** 2022-08-23T04:50:07Z
- **Updated:** 2024-05-23T18:18:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/1795

Currently I have ROCm installed from `https://repo.radeon.com/rocm/zyp/latest/main/`. When I encounter a crash, the resulting stack trace (see example) is not informative because there are no matching -debuginfo or -debugsource packages.

```
Missing separate debuginfos, use: zypper install comgr-debuginfo-2.4.0.50200-sles153.65.x86_64
hsa-rocr-debuginfo-1.5.0.50200-sles153.65.x86_64
rocm-ocl-icd-debuginfo-2.0.0.50200-sles153.65.x86_64

(gdb) where
#0 0x00007fffdab9d89c in MesaGLInteropGLXExportObject (dpy=<optimized out>, out=0x7fff84ee5270, in=0x7fff84ee5250, context=0x7fffec891600) at ../src/glx/glxcmds.c:2783
#1 MesaGLInteropGLXExportObject (dpy=<optimized out>, context=0x7fffec891600, in=0x7fff84ee5250, out=0x7fff84ee5270) at ../src/glx/glxcmds.c:2769
#2 0x00007fff918ab762 in ?? () from /opt/rocm-5.2.0/lib/libamdocl64.so
#3 0x00007fff918ad002 in ?? () from /opt/rocm-5.2.0/lib/libamdocl64.so
#4 0x00007fff918ae7d6 in ?? () from /opt/rocm-5.2.0/lib/libamdocl64.so
#5 0x00007fff918a310d in ?? () from /opt/rocm-5.2.0/lib/libamdocl64.so
#6 0x00007fff91895c98 in ?? () from /opt/rocm-5.2.0/lib/libamdocl64.so
#7 0x00007fff91895ef4 in ?? () from /opt/rocm-5.2.0/lib/libamdocl64.so
#8 0x00007fff91896040 in ?? () from /opt/rocm-5.2.0/lib/libamdocl64.so
...
```

Please add the matching debuginfo and debugsource packages to the repository.