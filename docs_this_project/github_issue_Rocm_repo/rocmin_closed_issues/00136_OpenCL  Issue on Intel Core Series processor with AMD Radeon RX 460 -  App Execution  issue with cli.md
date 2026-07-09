# OpenCL  Issue on Intel Core Series processor with AMD Radeon RX 460 -  App Execution  issue with clinfo and  luxmark 

- **Issue #:** 136
- **State:** closed
- **Created:** 2017-06-28T10:18:49Z
- **Updated:** 2018-06-03T14:57:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/136

Hi,
I am using Skylake	board with AMD Radeon ™ RX 460 Graphics and installed the rocm1.5 package after setting proxy as mentioned in https://github.com/RadeonOpenCompute/ROCm
apt-get install rocm rocm-opencl.
1. When I execute the command below, not getting any information for "clinfo"
root@bdk:/opt/rocm/opencl/bin/x86_64# ./clinfo 
<..not getting any log..>

2. Also installed "luxmark-linux64-v3.1.tar.bz2" package and executed  in skylake, But getting below error:
root@bdk:/luxmark-v3.1# ./luxmark
Profiling is not available
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
./luxmark: line 12:  3339 Aborted                 ./luxmark.bin "$@"

Could you please let me know what is the issue and how to proceed on this above issue.