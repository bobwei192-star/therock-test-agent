# ROCm-Opencl-runtime build is not clear.

- **Issue #:** 1072
- **State:** closed
- **Created:** 2020-04-04T09:11:25Z
- **Updated:** 2021-04-05T10:07:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/1072

The README.txt contains instruction to use cmake with several flags:
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_INCLUDES=<path-to-llvm-include> -DCMAKE_PREFIX_PATH=<path-to-amd_comgr> -DUSE_COMGR_LIBRARY=yes .

It is not clear what path to use for DLLVM_INCLUDES and DCMAKE_PREFIX_PATH as Rocm source seem to have many copies of same:
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name llvm | grep include
../../aomp/llvm-project/llvm/utils/gn/secondary/llvm/include/llvm
../../aomp/llvm-project/llvm/include/llvm
../../hcc/build/llvm-project/llvm/include/llvm
../../hcc/llvm-project/llvm/utils/gn/secondary/llvm/include/llvm
../../hcc/llvm-project/llvm/include/llvm
../../llvm_amd-stg-open/llvm/utils/gn/secondary/llvm/include/llvm
../../llvm_amd-stg-open/llvm/include/llvm
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name comgr
../../ROCm-CompilerSupport/lib/comgr
../../aomp/rocm-compilersupport/lib/comgr


Tried with same of the path but always ended with missing cmake files:
  Could not find a package configuration file provided by "amd_comgr" with
  any of the following names:
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_INCLUDES=../../hcc/build/llvm-project/llvm/include -DCMAKE_PREFIX_PATH=../../ROCm-CompilerSupport/lib/comgr -DUSE_COMGR_LIBRARY=yes ..
    amd_comgrConfig.cmake
    amd_comgr-config.cmake

Full log:

root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_INCLUDES=../../hcc/build/llvm-project/llvm/include -DCMAKE_PREFIX_PATH=../../ROCm-CompilerSupport/lib/comgr -DUSE_COMGR_LIBRARY=yes ..
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found ROCT: /opt/rocm/include
-- Found ROCR: /opt/rocm/include/hsa
CMake Error at api/opencl/amdocl/CMakeLists.txt:32 (find_package):
  Could not find a package configuration file provided by "amd_comgr" with
  any of the following names:

    amd_comgrConfig.cmake
    amd_comgr-config.cmake

  Add the installation prefix of "amd_comgr" to CMAKE_PREFIX_PATH or set
  "amd_comgr_DIR" to a directory containing one of the above files.  If
  "amd_comgr" provides a separate development package or SDK, be sure it has
  been installed.


-- Configuring incomplete, errors occurred!
See also "/root/ROCm/ROCm-OpenCL-Runtime/build/CMakeFiles/CMakeOutput.log".
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name amd_comgrConfig.cmake
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build# find ../../ -name amd_comgr-config.cmake
root@gg-desktop:~/ROCm/ROCm-OpenCL-Runtime/build#

