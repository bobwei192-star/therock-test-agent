# Deprecated OpenCL headers?

- **Issue #:** 447
- **State:** closed
- **Created:** 2018-06-29T22:49:44Z
- **Updated:** 2019-06-05T01:36:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/447

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