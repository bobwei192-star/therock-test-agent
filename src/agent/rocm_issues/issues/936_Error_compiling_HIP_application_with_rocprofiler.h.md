# Error compiling HIP application with rocprofiler.h

> **Issue #936**
> **状态**: closed
> **创建时间**: 2019-11-16T14:43:02Z
> **更新时间**: 2023-12-14T11:10:41Z
> **关闭时间**: 2023-12-14T11:10:41Z
> **作者**: theRTLmaker
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/936

## 描述

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


---

## 评论 (4 条)

### 评论 #1 — eshcherb (2019-11-19T03:49:15Z)

You need to link rocprofiler library.
Need to add the following linking flags: -L/opt/rocm/lib -lrocprofiler64
Also there is a test example at the GitHub: https://github.com/ROCm-Developer-Tools/rocprofiler/blob/amd-master/test/app/standalone_test.cpp
And I will update the rocprofiler README at the GitHub.



---

### 评论 #2 — theRTLmaker (2019-11-24T23:12:49Z)

Thank you! With that flag, I manage to compile the code, but I am still not able to get the performance counters. 
On the example that you point, they use the class HsaRsrcFactory. Do I need to use it? Without using it, how can I get the first argument of the function rocprofiler_open (hsa_agent_t device_id)? 

---

### 评论 #3 — eshcherb (2019-12-04T20:04:58Z)

HSA agent is a device descriptor either CPU or GPU.
You can discover HSA agents using ROCr-runtime hsa_iterate_agents API https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/master/src/inc/hsa.h#L1051
And to check type of discovered agents with hsa_agent_get_info API with attribute HSA_AGENT_INFO_DEVICE https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/master/src/inc/hsa.h#L1026
HsaRsrcFactory is a C++ API built on top of ROCr-runtime C API and you can reuse it or use as an example.
I have a HsaRsrcFactory API as a separate GitHub project: https://github.com/ROCmSoftwarePlatform/hsa-class

Full HSA specification can be found there:
http://www.hsafoundation.com/standards/
HSA Runtime Specification 1.1
HSA Programmer Reference Manual Specification 1.1
HSA Platform System Architecture Specification 1.1


---

### 评论 #4 — nartmada (2023-12-13T20:05:21Z)

Hi @theRTLmaker, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.

---
