# yum install rocm fails (CentOS 7.3)

- **Issue #:** 94
- **State:** closed
- **Created:** 2017-03-06T14:35:43Z
- **Updated:** 2017-03-07T15:52:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/94

After adding the ROCm repo on CentOS 7.3, running `yum install rocm` fails with the following error:

    Error: Package: llvm-amdgpu-3.9.dev-1.x86_64 (remote)
               Requires: libclang.so.40()(64bit)

Is there some dependency missing here?
