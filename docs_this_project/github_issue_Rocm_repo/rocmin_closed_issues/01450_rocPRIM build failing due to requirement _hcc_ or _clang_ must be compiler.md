# rocPRIM build failing due to requirement 'hcc' or 'clang' must be compiler

- **Issue #:** 1450
- **State:** closed
- **Created:** 2021-04-10T08:37:49Z
- **Updated:** 2021-04-16T10:41:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1450

=~=~=~=~=~=~=~=~=~=~=~= MobaXterm log 2021.04.09 22:46:10 =~=~=~=~=~=~=~=~=~=~=~=
na[CXX=hipcc] cmake -DBUILD_BENCHMARK=ON ../.CXX=hipcc;..
root@guest:~/ROCm-4.1/rocPRIM# ehich       which hipcc
/usr/bin/hipcc
root@guest:~/ROCm-4.1/rocPRIM# which hipccCXX=`which hipcc`
root@guest:~/ROCm-4.1/rocPRIM# [CXX=hipcc] cmake -DBUILD_BENCHMARK=ON ../.Xccm
CMake Error: The source directory "/root/ROCm-4.1" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
root@guest:~/ROCm-4.1/rocPRIM# cd build
root@guest:~/ROCm-4.1/rocPRIM/build# rm -rf ./*
root@guest:~/ROCm-4.1/rocPRIM/build# rm -rf ./*cd buildmake -DBUILD_BENCHMARK=ON ../.
-- The CXX compiler identification is GNU 7.5.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Setting build type to 'Release' as none was specified.
CMake Error at cmake/VerifyCompiler.cmake:24 (find_package):
  Could not find a package configuration file provided by "hip" with any of
  the following names:

    hipConfig.cmake
    hip-config.cmake

  Add the installation prefix of "hip" to CMAKE_PREFIX_PATH or set "hip_DIR"
  to a directory containing one of the above files.  If "hip" provides a
  separate development package or SDK, be sure it has been installed.
Call Stack (most recent call first):
  CMakeLists.txt:67 (include)


-- Configuring incomplete, errors occurred!
See also "/root/ROCm-4.1/rocPRIM/build/CMakeFiles/CMakeOutput.log".
root@guest:~/ROCm-4.1/rocPRIM/build# find /opt -name hipConfig.cmake
root@guest:~/ROCm-4.1/rocPRIM/build# find ~/ROCm-4.1/ -name hipConfig.cmake
root@guest:~/ROCm-4.1/rocPRIM/build# find /opt -name HIP
root@guest:~/ROCm-4.1/rocPRIM/build# find /opt -name HIP   hip
/opt/rocm-4.1.0/include/hip
/opt/rocm-4.1.0/hip
/opt/rocm-4.1.0/hip/include/hip
/opt/rocm-4.1.0/hip/lib/cmake/hip
/opt/rocm-4.1.0/lib/cmake/hip
/opt/rocm/hip
root@guest:~/ROCm-4.1/rocPRIM/build# 