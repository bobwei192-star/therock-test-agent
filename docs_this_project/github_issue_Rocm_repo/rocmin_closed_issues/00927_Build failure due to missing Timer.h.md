# Build failure due to missing Timer.h

- **Issue #:** 927
- **State:** closed
- **Created:** 2019-11-02T06:33:51Z
- **Updated:** 2023-12-18T16:26:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/927

https://rocm-documentation.readthedocs.io/en/latest/Programming_Guides/Opencl-programming-guide.html has example code 3.
Build fails because it needs Timer.h which does not exist in current rocm version:

I dont expect environment issue since example 2 builds OK.

Platform Version:                              OpenCL 2.1 AMD-APP (2982.0)

EXAMPLE 3 (build fail)

root@guyen-MS-7B22:/git.co/dev-learn/amd/opencl/opencl-programming-guide# nano -w ex-code-3.c
root@guyen-MS-7B22:/git.co/dev-learn/amd/opencl/opencl-programming-guide# make ex-code-3
g++ -o ex-code-3.o -c ex-code-3.c -I/opt/rocm/opencl//include
ex-code-3.c:9:10: fatal error: Timer.h: No such file or directory
 #include "Timer.h"
          ^~~~~~~~~
compilation terminated.
Makefile:17: recipe for target 'ex-code-3' failed
make: *** [ex-code-3] Error 1

EXAMPLE 2 (build ok)

root@guyen-MS-7B22:/git.co/dev-learn/amd/opencl/opencl-programming-guide# make ex-code-2
g++ -o ex-code-2.o -c ex-code-2.c -I/opt/rocm/opencl//include
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp: In constructor ‘cl::Sampler::Sampler(const cl::Context&, cl_bool, cl_addressing_mode, cl_filter_mode, cl_int*)’:
/opt/rocm/opencl//include/CL/cl.hpp:4659:21: warning: ‘_cl_sampler* clCreateSampler(cl_context, cl_bool, cl_addressing_mode, cl_filter_mode, cl_int*)’ is deprecated [-Wdeprecated-declarations]
         object_ = ::clCreateSampler(
                     ^~~~~~~~~~~~~~~
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1371:1: note: declared here
 clCreateSampler(cl_context          /* context */,
 ^~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp:4664:19: warning: ‘_cl_sampler* clCreateSampler(cl_context, cl_bool, cl_addressing_mode, cl_filter_mode, cl_int*)’ is deprecated [-Wdeprecated-declarations]
             &error);
                   ^
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1371:1: note: declared here
 clCreateSampler(cl_context          /* context */,
 ^~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp: At global scope:
/opt/rocm/opencl//include/CL/cl.hpp:5127:28: warning: ignoring attributes on template argument ‘cl_int {aka int}’ [-Wignored-attributes]
         VECTOR_CLASS<cl_int>* binaryStatus = NULL,
                            ^
/opt/rocm/opencl//include/CL/cl.hpp: In constructor ‘cl::CommandQueue::CommandQueue(cl_command_queue_properties, cl_int*)’:
/opt/rocm/opencl//include/CL/cl.hpp:5519:25: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
             object_ = ::clCreateCommandQueue(
                         ^~~~~~~~~~~~~~~~~~~~
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp:5520:56: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
                 context(), device(), properties, &error);
                                                        ^
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp: In constructor ‘cl::CommandQueue::CommandQueue(const cl::Context&, cl_command_queue_properties, cl_int*)’:
/opt/rocm/opencl//include/CL/cl.hpp:5550:21: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
         object_ = ::clCreateCommandQueue(context(), devices[0](), properties, &error);
                     ^~~~~~~~~~~~~~~~~~~~
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp:5550:85: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
         object_ = ::clCreateCommandQueue(context(), devices[0](), properties, &error);
                                                                                     ^
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp: In constructor ‘cl::CommandQueue::CommandQueue(const cl::Context&, const cl::Device&, cl_command_queue_properties, cl_int*)’:
/opt/rocm/opencl//include/CL/cl.hpp:5567:21: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
         object_ = ::clCreateCommandQueue(
                     ^~~~~~~~~~~~~~~~~~~~
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp:5568:52: warning: ‘_cl_command_queue* clCreateCommandQueue(cl_context, cl_device_id, cl_command_queue_properties, cl_int*)’ is deprecated [-Wdeprecated-declarations]
             context(), device(), properties, &error);
                                                    ^
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1364:1: note: declared here
 clCreateCommandQueue(cl_context                     /* context */,
 ^~~~~~~~~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp: In member function ‘cl_int cl::CommandQueue::enqueueTask(const cl::Kernel&, const std::vector<cl::Event>*, cl::Event*) const’:
/opt/rocm/opencl//include/CL/cl.hpp:6371:15: warning: ‘cl_int clEnqueueTask(cl_command_queue, cl_kernel, cl_uint, _cl_event* const*, _cl_event**)’ is deprecated [-Wdeprecated-declarations]
             ::clEnqueueTask(
               ^~~~~~~~~~~~~
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1378:1: note: declared here
 clEnqueueTask(cl_command_queue  /* command_queue */,
 ^~~~~~~~~~~~~
In file included from ex-code-2.c:3:0:
/opt/rocm/opencl//include/CL/cl.hpp:6375:46: warning: ‘cl_int clEnqueueTask(cl_command_queue, cl_kernel, cl_uint, _cl_event* const*, _cl_event**)’ is deprecated [-Wdeprecated-declarations]
                 (event != NULL) ? &tmp : NULL),
                                              ^
In file included from /opt/rocm/opencl//include/CL/opencl.h:47:0,
                 from /opt/rocm/opencl//include/CL/cl.hpp:175,
                 from ex-code-2.c:3:
/opt/rocm/opencl//include/CL/cl.h:1378:1: note: declared here
 clEnqueueTask(cl_command_queue  /* command_queue */,
 ^~~~~~~~~~~~~
g++ -o ex-code-2 ex-code-2.o -lOpenCL -L/opt/rocm/opencl//lib/x86_64
root@guyen-MS-7B22:/git.co/dev-learn/amd/opencl/opencl-programming-guide#
