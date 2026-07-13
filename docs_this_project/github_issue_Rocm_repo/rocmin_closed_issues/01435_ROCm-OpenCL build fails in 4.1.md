# ROCm-OpenCL build fails in 4.1

- **Issue #:** 1435
- **State:** closed
- **Created:** 2021-03-31T04:32:25Z
- **Updated:** 2021-04-07T06:40:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/1435

**used to build in previous version but appears to have broken in 4.1:


root@guest:~/ROCm/ROCm-OpenCL-Runtime# nano -w README.md
root@guest:~/ROCm/ROCm-OpenCL-Runtime# cd build
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# make
[  9%] Built target OpenCL
[ 12%] Built target IcdLog
[ 21%] Built target OpenCLDriverStub
Scanning dependencies of target icd_loader_test
[ 25%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_kernel.c.o
[ 28%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/main.c.o
[ 28%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_platforms.c.o
[ 31%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/icd_test_match.c.o
[ 31%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_program_objects.c.o
[ 34%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_sampler_objects.c.o
[ 34%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_buffer_object.c.o
[ 37%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_cl_runtime.c.o
[ 37%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/callbacks.c.o
[ 40%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_create_calls.c.o
[ 40%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_clgl.c.o
[ 43%] Building C object khronos/icd/test/loader_test/CMakeFiles/icd_loader_test.dir/test_image_objects.c.o
[ 43%] Linking C executable icd_loader_test
[ 43%] Built target icd_loader_test
[ 43%] Building CXX object amdocl/CMakeFiles/amdocl64.dir/cl_memobj.cpp.o
In file included from /root/ROCm/ROCm-OpenCL-Runtime/amdocl/cl_memobj.cpp:21:0:
/root/ROCm/ROCm-OpenCL-Runtime/amdocl/cl_common.hpp:31:10: fatal error: top.hpp: No such file or directory
 #include "top.hpp"
          ^~~~~~~~~
compilation terminated.
amdocl/CMakeFiles/amdocl64.dir/build.make:62: recipe for target 'amdocl/CMakeFiles/amdocl64.dir/cl_memobj.cpp.o' failed
make[2]: *** [amdocl/CMakeFiles/amdocl64.dir/cl_memobj.cpp.o] Error 1
CMakeFiles/Makefile2:1453: recipe for target 'amdocl/CMakeFiles/amdocl64.dir/all' failed
make[1]: *** [amdocl/CMakeFiles/amdocl64.dir/all] Error 2
Makefile:129: recipe for target 'all' failed
make: *** [all] Error 2
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# git remote -v
roc-github      http://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime (fetch)
roc-github      http://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime (push)
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# git branch
* (no branch)
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build# git branch -r
  m/roc-4.1.x -> rocm-4.1.0
root@guest:~/ROCm/ROCm-OpenCL-Runtime/build#**
