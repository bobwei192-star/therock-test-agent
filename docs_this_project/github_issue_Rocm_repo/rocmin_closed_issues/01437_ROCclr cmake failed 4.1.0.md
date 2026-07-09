# ROCclr cmake failed 4.1.0

- **Issue #:** 1437
- **State:** closed
- **Created:** 2021-04-02T02:44:39Z
- **Updated:** 2021-05-07T12:10:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/1437

I have built rocm-dkms，HIP-Clang and ROCm device library successfully, howerver, when I build ROCclr as follows：

git clone https://github.com/ROCm-Developer-Tools/ROCclr.git
git clone -b master-next https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git
export ROCclr_DIR="$(readlink -f ROCclr)"
export OPENCL_DIR="$(readlink -f ROCm-OpenCL-Runtime)"
cd "$ROCclr_DIR"
mkdir -p build; cd build
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
make -j$(nproc)

When I cmake rocclr, I encountered the following error：

# cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..

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
CMake Error at CMakeLists.txt:46 (find_package):
  Could not find a package configuration file provided by "amd_comgr" with
  any of the following names:

    amd_comgrConfig.cmake
    amd_comgr-config.cmake

  Add the installation prefix of "amd_comgr" to CMAKE_PREFIX_PATH or set
  "amd_comgr_DIR" to a directory containing one of the above files.  If
  "amd_comgr" provides a separate development package or SDK, be sure it has
  been installed.


-- Configuring incomplete, errors occurred!
See also "/usr/local/ROCclr/build/CMakeFiles/CMakeOutput.log".

May I ask why？Thank you.
