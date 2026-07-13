# Problem building OpenMP in LLVM.

- **Issue #:** 1822
- **State:** closed
- **Created:** 2022-10-06T06:13:40Z
- **Updated:** 2022-10-18T07:00:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1822

Dear ROCm developers,
I am trying to enable OpenMP in your fork of LLVM (I am compiling ROCm from source) but I get an error relating to the offloloading target (gfx908). Here is the error:

```
Consolidate compiler generated dependencies of target omptarget
[  4%] Building CXX object tools/archer/CMakeFiles/archer.dir/ompt-tsan.cpp.o
make[2]: *** No rule to make target 'gfx908', needed by 'libomptarget/libomptarget.so'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:1116: libomptarget/src/CMakeFiles/omptarget.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
```
and here is the full log, starting with my CMake call with CMake flags. Would you be able to help me out? I may miss some CMake flags..

```
Running command cmake  -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=/opt/rocm/rocm-5.2.3rev0/llvm -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DLIBOMPTARGET_AMDGCN_GFXLIST=gfx908 -DLLVM_OFFLOAD_ARCH=gfx908 -DDEVICELIBS_ROOT=/home/ubuntu/rocm-from-source/scripts/build/ROCm-Device-Libs -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocm-5.2.3rev0/llvm ..
-- Cannot find llvm-lit.
-- Please put llvm-lit in your PATH, set OPENMP_LLVM_LIT_EXECUTABLE to its full path, or point OPENMP_LLVM_TOOLS_DIR to its directory.
CMake Warning at cmake/OpenMPTesting.cmake:22 (message):
  The check targets will not be available!
Call Stack (most recent call first):
  cmake/OpenMPTesting.cmake:51 (find_standalone_test_dependencies)
  CMakeLists.txt:59 (include)


-- LIBOMP: Operating System     -- Linux
-- LIBOMP: Target Architecture  -- x86_64
-- LIBOMP: Build Type           -- Release
-- LIBOMP: Library Kind         -- SHARED
-- LIBOMP: Library Type         -- normal
-- LIBOMP: Fortran Modules      -- FALSE
-- LIBOMP: Build                -- 20140926
-- LIBOMP: Use Stats-gathering  -- FALSE
-- LIBOMP: Use Debugger-support -- FALSE
-- LIBOMP: Use ITT notify       -- TRUE
-- LIBOMP: Use OMPT-support     -- TRUE
-- LIBOMP: Use OMPT-optional  -- TRUE
-- LIBOMP: Use OMPD-support     -- FALSE
-- LIBOMP: Use Adaptive locks   -- TRUE
-- LIBOMP: Use quad precision   -- FALSE
-- LIBOMP: Use Hwloc library    -- FALSE
-- check-libomp does nothing.
-- check-ompt does nothing.
-- Found LLVM 14.0.0git
-- Using LLVM in: /opt/rocm/rocm-5.2.3rev0/llvm/lib/cmake/llvm
-- Could NOT find LIBOMPTARGET_DEP_CUDA_DRIVER (missing: LIBOMPTARGET_DEP_CUDA_DRIVER_LIBRARIES) 
-- Could NOT find LIBOMPTARGET_DEP_VEO (missing: LIBOMPTARGET_DEP_VEO_LIBRARIES LIBOMPTARGET_DEP_VEOSINFO_LIBRARIES LIBOMPTARGET_DEP_VEO_INCLUDE_DIRS) 
-- OMPT target enabled
 -- LLVM found at /opt/rocm/rocm-5.2.3rev0/llvm/lib/cmake/llvm
-- LIBOMPTARGET: Building offloading runtime library libomptarget.
-- LIBOMPTARGET: Not building aarch64 offloading plugin: machine not found in the system.
FOUND hsa-runtime64 at /opt/rocm/rocm-5.2.3rev0/lib/cmake/hsa-runtime64
-- LIBOMPTARGET: Building AMDGPU plugin linked against libhsa
-- LIBOMPTARGET: Not generating amdgcn test targets as amdgpu-arch is not found
-- LIBOMPTARGET: Building CUDA offloading plugin.
-- LIBOMPTARGET: Building CUDA plugin for dlopened libcuda
-- LIBOMPTARGET: Disabling tests using CUDA plugin as cuda may not be available
-- LIBOMPTARGET: Not building PPC64 offloading plugin: machine not found in the system.
-- LIBOMPTARGET: Not building PPC64le offloading plugin: machine not found in the system.
-- LIBOMPTARGET: Not building nec-aurora plugin: libveo or libveosinfo not found.
-- LIBOMPTARGET: Building x86_64 offloading plugin.
   -- Building libm bitcodes with LLVM 14.0.0git using /opt/rocm/rocm-5.2.3rev0/llvm/bin/clang
   -- Building hostrpc with LLVM 14.0.0git found with CLANG_TOOL /opt/rocm/rocm-5.2.3rev0/llvm/bin/clang
-- LIBOMPTARGET: Building the llvm-omp-device-info tool
-- LIBOMPTARGET: Getting ROCm device libs from /opt/rocm/rocm-5.2.3rev0/llvm/lib/cmake/AMDDeviceLibs
-- LIBOMPTARGET: Building AMDGCN device RTLs. Using clang: /opt/rocm/rocm-5.2.3rev0/llvm/bin/clang
-- LIBOMPTARGET: Building AMDGCN device RTL. Using clang: /opt/rocm/rocm-5.2.3rev0/llvm/bin/clang, llvm-link: /opt/rocm/rocm-5.2.3rev0/llvm/bin/llvm-link and opt: /opt/rocm/rocm-5.2.3rev0/llvm/bin/opt
-- LIBOMPTARGET: Not building NVPTX deviceRTL: Disabled by LIBOMPTARGET_BUILD_NVPTX_BCLIB
-- LIBOMPTARGET: Building DeviceRTL. Using clang: /opt/rocm/rocm-5.2.3rev0/llvm/bin/clang, llvm-link: /opt/rocm/rocm-5.2.3rev0/llvm/bin/llvm-link and opt: /opt/rocm/rocm-5.2.3rev0/llvm/bin/opt
-- LIBOMPTARGET: DeviceRTLs gfx908: Getting ROCm device libs from /opt/rocm/rocm-5.2.3rev0/llvm/lib/cmake/AMDDeviceLibs
-- check-libomptarget-x86_64-pc-linux-gnu does nothing.
-- check-libomptarget does nothing.
-- check-libarcher does nothing.
-- check-ompt-multiplex does nothing.
-- check-openmp does nothing.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ubuntu/rocm-from-source/scripts/build/llvm-project/openmp/build
Running command make -j 8 install
Consolidate compiler generated dependencies of target hostrpc_services
Consolidate compiler generated dependencies of target elf_common
Consolidate compiler generated dependencies of target prep-libomptarget-bc
[  1%] Built target libm-target-gfx908
[  1%] Built target libomp-needed-headers
[  1%] Generating hostrpc_invoke-amdgcn-gfx908.bc
[  2%] Built target hostrpc_services
[  2%] Built target omptarget-amdgcn
[  3%] Generating hostrpc-amdgcn-gfx908.o
[  4%] Built target prep-libomptarget-bc
[  4%] Built target elf_common
Consolidate compiler generated dependencies of target omptarget
[  4%] Building CXX object tools/archer/CMakeFiles/archer.dir/ompt-tsan.cpp.o
make[2]: *** No rule to make target 'gfx908', needed by 'libomptarget/libomptarget.so'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:1116: libomptarget/src/CMakeFiles/omptarget.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
Scanning dependencies of target omptarget-new-nvptx-sm_35-bc
[  4%] Building CXX object tools/archer/CMakeFiles/archer_static.dir/ompt-tsan.cpp.o
[  4%] Building CXX object runtime/src/CMakeFiles/omp.dir/kmp_alloc.cpp.o
[  4%] Building CXX object runtime/src/CMakeFiles/omp.dir/kmp_atomic.cpp.o

```