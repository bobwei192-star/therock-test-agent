# Error compiling HIP application with rocprofiler.h

- **Issue #:** 936
- **State:** closed
- **Created:** 2019-11-16T14:43:02Z
- **Updated:** 2023-12-14T11:10:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/936

Hello everybody, I am a researcher at Lisbon University (Portugal) 
I am trying to get the performance counters values with the rocprofiler API, but when I compile my app I always get undefined reference to functions on the header file rocprofiler.h

`/opt/rocm/hip/bin/hipcc -I/opt/rocm/rocprofiler/include -I/opt/rocm/hsa/include/hsa -g   -c -o vectoradd_hip.o vectoradd_hip.cpp
/opt/rocm/hip/bin/hipcc -I/opt/rocm/rocprofiler/include -I/opt/rocm/hsa/include/hsa vectoradd_hip.o -o vectoradd_hip.exe
/tmp/tmp.pLmY4FXuMN/vectoradd_hip.host.o: In function `main':
/homelocal/fmendeslocal/rocm_profile_example/vectoradd_hip.cpp:121: undefined reference to `rocprofiler_open'
clang-10: error: linker command failed with exit code 1 (use -v to see invocation)`

when I use the rocprof script to profile, everything works great, but I need to use the API because I want to be able to read the performance counters in specific points of my application.

How should I compile my code in order to use the rocprofiler.h API?

Thanks

[vectoradd_hip.zip](https://github.com/RadeonOpenCompute/ROCm/files/3854286/vectoradd_hip.zip)
