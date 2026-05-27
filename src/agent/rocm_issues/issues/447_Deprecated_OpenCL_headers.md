# Deprecated OpenCL headers?

> **Issue #447**
> **状态**: closed
> **创建时间**: 2018-06-29T22:49:44Z
> **更新时间**: 2019-06-05T01:36:00Z
> **关闭时间**: 2018-07-03T20:50:34Z
> **作者**: robinchrist
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/447

## 描述

Hi,

When using the included OpenCL headers ("/opt/rocm/opencl/include/"), the compiler generates several warnings:
```
In file included from /home/testuser/CLionProjects/horncalc/src/bem/gpu.cpp:5:
In file included from /home/testuser/CLionProjects/horncalc/include/bem/gpu.hpp:2:
/opt/rocm/opencl/include/CL/cl.hpp:4659:21: warning: 'clCreateSampler' is deprecated [-Wdeprecated-declarations]
        object_ = ::clCreateSampler(
                    ^
/opt/rocm/opencl/include/CL/cl.h:1375:56: note: 'clCreateSampler' has been explicitly marked deprecated here
                cl_int *            /* errcode_ret */) CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED;
                                                       ^
/opt/rocm/opencl/include/CL/cl_platform.h:115:74: note: expanded from macro 'CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED'
            #define CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED __attribute__((deprecated))
                                                                         ^
In file included from /home/testuser/CLionProjects/horncalc/src/bem/gpu.cpp:5:
In file included from /home/testuser/CLionProjects/horncalc/include/bem/gpu.hpp:2:
/opt/rocm/opencl/include/CL/cl.hpp:5519:25: warning: 'clCreateCommandQueue' is deprecated [-Wdeprecated-declarations]
            object_ = ::clCreateCommandQueue(
                        ^
/opt/rocm/opencl/include/CL/cl.h:1367:72: note: 'clCreateCommandQueue' has been explicitly marked deprecated here
                     cl_int *                       /* errcode_ret */) CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED;
                                                                       ^
/opt/rocm/opencl/include/CL/cl_platform.h:115:74: note: expanded from macro 'CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED'
            #define CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED __attribute__((deprecated))
                                                                         ^
In file included from /home/testuser/CLionProjects/horncalc/src/bem/gpu.cpp:5:
In file included from /home/testuser/CLionProjects/horncalc/include/bem/gpu.hpp:2:
/opt/rocm/opencl/include/CL/cl.hpp:5550:21: warning: 'clCreateCommandQueue' is deprecated [-Wdeprecated-declarations]
        object_ = ::clCreateCommandQueue(context(), devices[0](), properties, &error);
                    ^
/opt/rocm/opencl/include/CL/cl.h:1367:72: note: 'clCreateCommandQueue' has been explicitly marked deprecated here
                     cl_int *                       /* errcode_ret */) CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED;
                                                                       ^
/opt/rocm/opencl/include/CL/cl_platform.h:115:74: note: expanded from macro 'CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED'
            #define CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED __attribute__((deprecated))
                                                                         ^
In file included from /home/testuser/CLionProjects/horncalc/src/bem/gpu.cpp:5:
In file included from /home/testuser/CLionProjects/horncalc/include/bem/gpu.hpp:2:
/opt/rocm/opencl/include/CL/cl.hpp:5567:21: warning: 'clCreateCommandQueue' is deprecated [-Wdeprecated-declarations]
        object_ = ::clCreateCommandQueue(
                    ^
/opt/rocm/opencl/include/CL/cl.h:1367:72: note: 'clCreateCommandQueue' has been explicitly marked deprecated here
                     cl_int *                       /* errcode_ret */) CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED;
                                                                       ^
/opt/rocm/opencl/include/CL/cl_platform.h:115:74: note: expanded from macro 'CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED'
            #define CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED __attribute__((deprecated))
                                                                         ^
In file included from /home/testuser/CLionProjects/horncalc/src/bem/gpu.cpp:5:
In file included from /home/testuser/CLionProjects/horncalc/include/bem/gpu.hpp:2:
/opt/rocm/opencl/include/CL/cl.hpp:6371:15: warning: 'clEnqueueTask' is deprecated [-Wdeprecated-declarations]
            ::clEnqueueTask(
              ^
/opt/rocm/opencl/include/CL/cl.h:1382:46: note: 'clEnqueueTask' has been explicitly marked deprecated here
              cl_event *        /* event */) CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED;
                                             ^
/opt/rocm/opencl/include/CL/cl_platform.h:115:74: note: expanded from macro 'CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED'
            #define CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED __attribute__((deprecated))
                                                                         ^
^
6 warnings generated.
```

Is this known behaviour?

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-07-03T20:26:28Z)

Yes, the cl.hpp header, [as provided by Khronos](https://www.khronos.org/registry/OpenCL/api/2.1/cl.hpp), uses deprecated OpenCL API functions because (as shown in the comments of that file) it is designed for OpenCL 1.0, 1.1, and 1.2 systems. The use of deprecated API functions is supported, but will emit these warnings. At this time, ROCm does not fully support OpenCL 2.0 (for instance, we do not yet support device enqueue).

Nonetheless, there are two things you could do to silence these warnings:

1. You could define the following before you include cl.hpp into your program: `#define CL_USE_DEPRECATED_OPENCL_2_0_APIS`. This will silence the warnings and allow you to quietly use older, deprecated OpenCL 1.x functions beneath cl.hpp
1. You could attempt to use [cl2.hpp](https://github.khronos.org/OpenCL-CLHPP/), which is the Khronos C++ header which has been updated to support the OpenCL 2.0 APIs (most of which ROCm supports -- though at this time I cannot guarantee that this header will work for your application).

---

### 评论 #2 — crr0004 (2019-06-05T01:36:00Z)

This pops up when you search `opencl CL_EXT_SUFFIX__VERSION_1_2_DEPRECATED` so just adding a comment about 1_2 deprecation warnings. You can add `#define CL_USE_DEPRECATED_OPENCL_1_2_APIS` to silence those warnings.


---
