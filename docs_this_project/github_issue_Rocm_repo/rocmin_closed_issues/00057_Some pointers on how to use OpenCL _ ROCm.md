# Some pointers on how to use OpenCL + ROCm

- **Issue #:** 57
- **State:** closed
- **Created:** 2016-12-18T20:48:31Z
- **Updated:** 2017-01-03T19:21:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/57

I just installed the latest version of ROCm and realised that there is no GPU device recognized by the "AMD Accelerated Parallel Processing" OpenCL platform.

I'm aware that there are some changes in relation to the way to use OpenCL with the ROCm driver.

For instance, the following Makefile works perfectly and a binary 'app' is produced.

**Makefile:**
EXECUTABLE := app
CFILES := app.c
OpenCL_SDK=/opt/AMDAPPSDK-3.0
INCLUDE=-I${OpenCL_SDK}/include
LIBPATH=-L${OpenCL_SDK}/lib/x86_64
LIB=-lOpenCL -lm
all:
        gcc -O3 ${INCLUDE} ${LIBPATH} ${CFILES} ${LIB} -o ${EXECUTABLE}
clean:
        rm -f *~ app

**Portion of code from 'app.c' that initializes the OpenCL platform:**
        errcode = clGetPlatformIDs(1, &platform_id, &num_platforms);
        if(errcode == CL_SUCCESS) printf("number of platforms is %d\n",num_platforms);
        else printf("Error getting platform IDs\n");
        errcode = clGetPlatformInfo(platform_id,CL_PLATFORM_NAME, sizeof(str_temp), str_temp,NULL);
        if(errcode == CL_SUCCESS) printf("platform name is %s\n",str_temp);
        else printf("Error getting platform name\n");
        errcode = clGetPlatformInfo(platform_id, CL_PLATFORM_VERSION, sizeof(str_temp), str_temp,NULL);
        if(errcode == CL_SUCCESS) printf("platform version is %s\n",str_temp);
        else printf("Error getting platform version\n");
        errcode = clGetDeviceIDs( platform_id,  CL_DEVICE_TYPE_GPU, 1, &device_id, &num_devices);
        if(errcode == CL_SUCCESS) printf("number of devices is %d\n", num_devices);
        else printf("Error getting device IDs\n");

The call to clGetDeviceIDs() results in an error, which does not surprise me given that the "AMD Accelerated Parallel Processing" OpenCL platform only recognizes the CPU (the GPU is not listed when executing 'clinfo').

The GPU is a R9 Nano (same Fiji core as the Fury X), wich to my undertanding is supported by ROCm.

My question is, how can I compile my OpenCL apps in a machine with ROCm installed?

Thanks in advance!
