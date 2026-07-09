# ROCclr build issue, make failed.

- **Issue #:** 1358
- **State:** closed
- **Created:** 2021-01-12T07:14:15Z
- **Updated:** 2021-02-08T10:14:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/1358

I filed this bug here since there seems no ROCclr project on its own.
I downloaded source for 4.0.0 but ROCclr build problem.

I built and installed llvm, ROCm-Compiler-support and ROCm-device-libs ok as prereq.

But build instruction for ROCclr as follows:

### Set the environment variables

```bash
export ROCclr_DIR="$(readlink -f ROCclr)"
export OPENCL_DIR="$(readlink -f ROCm-OpenCL-Runtime)"
```

### Build ROCclr
Here is command to build ROCclr:

```bash
cd "$ROCclr_DIR"
mkdir -p build; cd build
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
make -j$(nproc)
```

It appears settings OPENCL_DIR is necessary.  So i set the env variable and make sure it is ok (below).
But "make" command after cmake resulted in following error:

oot@sriov-guest:~/ROCm/ROCclr/build# env | grep ROCclr
OPENCL_DIR=/root/ROCm/ROCclr/build/ROCm-OpenCL-Runtime
OLDPWD=/root/ROCm/ROCclr
PWD=/root/ROCm/ROCclr/build
ROCclr_DIR=/root/ROCm/ROCclr/build/ROCclr

"root@sriov-guest:~/ROCm/ROCclr/build# make
[  2%] Building CXX object device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o
In file included from /root/ROCm/ROCclr/device/rocm/roccounters.hpp:24:0,
                 from /root/ROCm/ROCclr/device/rocm/roccounters.cpp:21:
/root/ROCm/ROCclr/include/top.hpp:36:10: fatal error: CL/opencl.h: No such file or directory
 #include "CL/opencl.h"
          ^~~~~~~~~~~~~
compilation terminated.
device/rocm/CMakeFiles/oclrocm.dir/build.make:62: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o' failed
make[2]: *** [device/rocm/CMakeFiles/oclrocm.dir/roccounters.cpp.o] Error 1
CMakeFiles/Makefile2:122: recipe for target 'device/rocm/CMakeFiles/oclrocm.dir/all' failed
make[1]: *** [device/rocm/CMakeFiles/oclrocm.dir/all] Error 2
Makefile:129: recipe for target 'all' failed
make: *** [all] Error 2
"

I dont think building ROCm-OpenCL-Runtime is prereq because 1. it does not say so in the ROCclr's readme and ROCm-OpenCL-Runtime build readme specified ROCclr build is a prereq.
