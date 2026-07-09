# System freezes when using ROCm 3.7.0 with gfx1010 and making OpenCL allocate memory.

- **Issue #:** 1215
- **State:** closed
- **Created:** 2020-09-10T12:21:19Z
- **Updated:** 2020-12-16T05:50:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1215

I heard that OpenCL runs on RX 5700 XT with ROCm 3.7.0 and tried to test it.
If someone is actively trying to make it work with Navi then this might be helpful.

Using CL_MEM_COPY_HOST_PTR with clCreateBuffer freezes the system. Using CL_MEM_USE_HOST_PTR works fine.
Creating a buffer with nullptr as host ptr and then using clEnqueueMapBuffer freezes the system, but not if I create the buffer with CL_MEM_USE_HOST_PTR.

I'm using the 5.5.19-050519-generic kernel on Linux Mint 19.2.

My test code:

    #include <CL/cl.h>

    #include <algorithm>
    #include <cstring>
    #include <iostream>

    int main()
    {
	    cl_platform_id p[10];
	    cl_uint num = 0;
	    cl_int res = clGetPlatformIDs(10, p, &num);
        if (res != CL_SUCCESS)
            return -1;

        for (uint i = 0; i < num; ++i) {
            cl_platform_id plat = p[i];
            char buf[100];
            size_t size = 0;
            res = clGetPlatformInfo(plat, CL_PLATFORM_NAME, 100, buf, &size);
            buf[std::min<size_t>(size + 1, 99)] = '\0';

            if (res == CL_SUCCESS)
                std::cout << buf << std::endl;
        }

        if (num == 0)
            return -1;

        cl_device_id devs[10];
        res = clGetDeviceIDs(p[0], CL_DEVICE_TYPE_DEFAULT, 10, devs, &num);
        if (res != CL_SUCCESS)
            return -1;

        for (uint i = 0; i < num; ++i) {
            cl_device_id d = devs[i];
            char buf[100];
            size_t size = 0;
            res = clGetDeviceInfo(d, CL_DEVICE_NAME, 100, buf, &size);
            buf[std::min<size_t>(size + 1, 99)] = '\0';

            if (res == CL_SUCCESS)
                std::cout << buf << std::endl;
        }

        if (num == 0)
            return -1;

        cl_context c = clCreateContext(nullptr, 1, devs, nullptr, nullptr, &res);
        if (res != CL_SUCCESS)
            return -1;

        cl_command_queue cq = clCreateCommandQueue(c, *devs, 0, &res);
        if (res != CL_SUCCESS)
            return -1;

        const char* program = R"SRC(
        kernel void func(global const int* i1, global const int* i2, global int* i3) {
            size_t idx = get_global_id(0);
            i3[idx] = i1[idx] + i2[idx];
        }
        )SRC";

        size_t len = std::strlen(program);
        cl_program prog = clCreateProgramWithSource(c, 1, &program, &len, &res);
        if (res != CL_SUCCESS)
            return -1;

        res = clBuildProgram(prog, 1, devs, nullptr, nullptr, nullptr);
        if (res != CL_SUCCESS)
            return -1;

        cl_kernel k = clCreateKernel(prog, "func", &res);
        if (res != CL_SUCCESS)
            return -1;

        cl_int i1s[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        cl_int i2s[] = {11, 22, 33, 44, 55, 66, 77, 88, 99, 110};
        //CL_MEM_COPY_HOST_PTR freezes system
        cl_mem b1 = clCreateBuffer(c, CL_MEM_READ_ONLY | CL_MEM_USE_HOST_PTR, 10*sizeof(cl_int), i1s, &res);
        if (res != CL_SUCCESS)
            return -1;

        //CL_MEM_COPY_HOST_PTR freezes system
        cl_mem b2 = clCreateBuffer(c, CL_MEM_READ_ONLY | CL_MEM_USE_HOST_PTR, 10*sizeof(cl_int), i2s, &res);
        if (res != CL_SUCCESS)
            return -1;

        cl_int i3[10] = {};
        //nullptr and not CL_MEM_USE_HOST_PTR instead of i3 freezes system when calling clEnqueueMapBuffer later.
        cl_mem b3 = clCreateBuffer(c, CL_MEM_WRITE_ONLY | CL_MEM_HOST_READ_ONLY | CL_MEM_USE_HOST_PTR, 10*sizeof(cl_int), i3, &res);
        if (res != CL_SUCCESS)
            return -1;

        res = clSetKernelArg(k, 0, sizeof(b1), &b1);
        if (res != CL_SUCCESS)
            return -1;

        res = clSetKernelArg(k, 1, sizeof(b2), &b2);
        if (res != CL_SUCCESS)
            return -1;

        res = clSetKernelArg(k, 2, sizeof(b3), &b3);
        if (res != CL_SUCCESS)
            return -1;

        size_t size = 10;
        res = clEnqueueNDRangeKernel(cq, k, 1, nullptr, &size, nullptr, 0, nullptr, nullptr);
        if (res != CL_SUCCESS)
            return -1;

        res = clFinish(cq);
        if (res != CL_SUCCESS)
            return -1;

        //this freezes if b3 was not created using CL_MEM_USE_HOST_PTR
        void* ptr = clEnqueueMapBuffer(cq, b3, CL_TRUE, CL_MAP_READ, 0, 10*sizeof(cl_int), 0, nullptr, nullptr, &res);
        if (res != CL_SUCCESS)
            return -1;

        int* int_ptr = reinterpret_cast<int*>(ptr);
        for (int i = 0; i < 10; ++i)
            std::cout << int_ptr[i] << " ";
        std::cout << std::endl;

    }


Output from clinfo

    dlerror: /opt/rocm-3.3.0/opencl/lib/x86_64/libamdocl64.so: cannot open shared object file: No such file or directory
    dlerror: libMesaOpenCL.so.1: cannot open shared object file: No such file or directory
    Number of platforms                               1
      Platform Name                                   AMD Accelerated Parallel Processing
      Platform Vendor                                 Advanced Micro Devices, Inc.
      Platform Version                                OpenCL 2.0 AMD-APP (3182.0)
      Platform Profile                                FULL_PROFILE
      Platform Extensions                             cl_khr_icd cl_amd_event_callback 
      Platform Extensions function suffix             AMD

      Platform Name                                   AMD Accelerated Parallel Processing
    Number of devices                                 1
      Device Name                                     gfx1010
      Device Vendor                                   Advanced Micro Devices, Inc.
      Device Vendor ID                                0x1002
      Device Version                                  OpenCL 2.0 
      Driver Version                                  3182.0 (HSA1.1,LC)
      Device OpenCL C Version                         OpenCL C 2.0 
      Device Type                                     GPU
      Device Board Name (AMD)                         Device 731f
      Device Topology (AMD)                           PCI-E, 09:00.0
      Device Profile                                  FULL_PROFILE
      Device Available                                Yes
      Compiler Available                              Yes
      Linker Available                                Yes
      Max compute units                               20
      SIMD per compute unit (AMD)                     4
      SIMD width (AMD)                                32
      SIMD instruction width (AMD)                    1
      Max clock frequency                             100MHz
      Graphics IP (AMD)                               10.10
      Device Partition                                (core)
        Max number of sub-devices                     20
        Supported partition types                     None
      Max work item dimensions                        3
      Max work item sizes                             1024x1024x1024
      Max work group size                             256
      Preferred work group size (AMD)                 256
      Max work group size (AMD)                       1024
      Preferred work group size multiple              32
      Wavefront width (AMD)                           32
      Preferred / native vector sizes                 
        char                                                 4 / 4       
        short                                                2 / 2       
        int                                                  1 / 1       
        long                                                 1 / 1       
        half                                                 1 / 1        (cl_khr_fp16)
        float                                                1 / 1       
        double                                               1 / 1        (cl_khr_fp64)
      Half-precision Floating-point support           (cl_khr_fp16)
        Denormals                                     No
        Infinity and NANs                             No
        Round to nearest                              No
        Round to zero                                 No
        Round to infinity                             No
        IEEE754-2008 fused multiply-add               No
        Support is emulated in software               No
      Single-precision Floating-point support         (core)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
        Correctly-rounded divide and sqrt operations  Yes
      Double-precision Floating-point support         (cl_khr_fp64)
        Denormals                                     Yes
        Infinity and NANs                             Yes
        Round to nearest                              Yes
        Round to zero                                 Yes
        Round to infinity                             Yes
        IEEE754-2008 fused multiply-add               Yes
        Support is emulated in software               No
      Address bits                                    64, Little-Endian
      Global memory size                              8573157376 (7.984GiB)
      Global free memory (AMD)                        8372224 (7.984GiB)
      Global memory channels (AMD)                    8
      Global memory banks per channel (AMD)           4
      Global memory bank width (AMD)                  256 bytes
      Error Correction support                        No
      Max memory allocation                           7287183769 (6.787GiB)
      Unified memory for Host and Device              No
      Shared Virtual Memory (SVM) capabilities        (core)
        Coarse-grained buffer sharing                 Yes
        Fine-grained buffer sharing                   Yes
        Fine-grained system sharing                   No
        Atomics                                       No
      Minimum alignment for any data type             128 bytes
      Alignment of base address                       1024 bits (128 bytes)
      Preferred alignment for atomics                 
        SVM                                           0 bytes
        Global                                        0 bytes
        Local                                         0 bytes
      Max size for global variable                    7287183769 (6.787GiB)
      Preferred total size of global vars             8573157376 (7.984GiB)
      Global Memory cache type                        Read/Write
      Global Memory cache size                        16384 (16KiB)
      Global Memory cache line size                   64 bytes
      Image support                                   Yes
        Max number of samplers per kernel             29471
        Max size for 1D images from buffer            65536 pixels
        Max 1D or 2D image array size                 2048 images
        Base address alignment for 2D image buffers   256 bytes
        Pitch alignment for 2D image buffers          256 pixels
        Max 2D image size                             16384x16384 pixels
        Max 3D image size                             2048x2048x2048 pixels
        Max number of read image args                 128
        Max number of write image args                8
        Max number of read/write image args           64
      Max number of pipe args                         16
      Max active pipe reservations                    16
      Max pipe packet size                            2992216473 (2.787GiB)
      Local memory type                               Local
      Local memory size                               65536 (64KiB)
      Local memory syze per CU (AMD)                  65536 (64KiB)
      Local memory banks (AMD)                        32
      Max number of constant args                     8
      Max constant buffer size                        7287183769 (6.787GiB)
      Preferred constant buffer size (AMD)            16384 (16KiB)
      Max size of kernel argument                     1024
      Queue properties (on host)                      
        Out-of-order execution                        No
        Profiling                                     Yes
      Queue properties (on device)                    
        Out-of-order execution                        Yes
        Profiling                                     Yes
        Preferred size                                262144 (256KiB)
        Max size                                      8388608 (8MiB)
      Max queues on device                            1
      Max events on device                            1024
      Prefer user sync for interop                    Yes
      Number of P2P devices (AMD)                     0
      P2P devices (AMD)                               <printDeviceInfo:144: get number of CL_DEVICE_P2P_DEVICES_AMD : error -30>
      Profiling timer resolution                      1ns
      Profiling timer offset since Epoch (AMD)        0ns (Thu Jan  1 01:00:00 1970)
      Execution capabilities                          
        Run OpenCL kernels                            Yes
        Run native kernels                            No
        Thread trace supported (AMD)                  No
        Number of async queues (AMD)                  8
        Max real-time compute queues (AMD)            8
        Max real-time compute units (AMD)             20
      printf() buffer size                            4194304 (4MiB)
      Built-in kernels                                
      Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

    NULL platform behavior
      clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
      clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
      clCreateContext(NULL, ...) [default]            No platform
      clCreateContext(NULL, ...) [other]              Success [AMD]
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1010
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1010
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
      clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
        Platform Name                                 AMD Accelerated Parallel Processing
        Device Name                                   gfx1010
