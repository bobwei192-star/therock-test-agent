# Some pointers on how to use OpenCL + ROCm

> **Issue #57**
> **状态**: closed
> **创建时间**: 2016-12-18T20:48:31Z
> **更新时间**: 2017-01-03T19:21:22Z
> **关闭时间**: 2017-01-03T19:14:15Z
> **作者**: rjfnobre
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/57

## 描述

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


---

## 评论 (15 条)

### 评论 #1 — boxerab (2016-12-19T04:02:19Z)

I have the same question.

---

### 评论 #2 — jedwards-AMD (2016-12-19T15:06:21Z)

This seems like a configuration or platform issue. Can you run a different type of sample, like a HIP or the vector_copy sample provided with the HSA runtime? Please provided the output of 'dmidecode' and 'uname -a'.

---

### 评论 #3 — boxerab (2016-12-19T18:46:19Z)

Should I expect the AMD APP SDK samples to run with ROCm platform ? 

---

### 评论 #4 — jedwards-AMD (2016-12-19T18:51:14Z)

Support is currently limited. Images are not supported by the LC compiler, so any sample that requires image support will fail. This is also a developer preview, so other samples requiring special functionality may also encounter issues. The 'clinfo' command should work, and should identify your dGPU, however.

---

### 评论 #5 — rjfnobre (2016-12-19T20:51:08Z)

**uname -a**
Linux workstation 4.6.0-kfd-compute-rocm-rel-1.4-16 #1 SMP Tue Dec 13 13:14:21 EST 2016 x86_64 x86_64 x86_64 GNU/Linux

**dmidecode**
https://gist.github.com/rjfnobre/4e82c68f22bf6eb58557adc55dcfaee9

**/opt/rocm/hsa/sample/vector_copy**
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Segmentation fault (core dumped)


---

### 评论 #6 — boxerab (2016-12-20T00:47:06Z)

@jedwards-AMD  thanks. I will wait for full opencl 1.2 support. Not going to ask you when that will be :)

---

### 评论 #7 — jedwards-AMD (2016-12-20T16:26:08Z)

Your GPU and CPU look capable, and from the output above I appears your agent is a Fiji GPU. The motherboard also looks good. The failure of the vector_copy HSA sample indicates you don't have a brig file in the same directory as the sample executable, but you can get a device.

Can you run your OpenCL application using strace, like this: 'strace <app_name>` 

Send me the output. I think you have some kind of configuration problem.

---

### 评论 #8 — rjfnobre (2016-12-20T17:57:37Z)

Strace for the execution of the OpenCL application:
https://gist.github.com/rjfnobre/93037ec893576ca2deb78b5c03a162ae

---

### 评论 #9 — rjfnobre (2016-12-22T10:57:15Z)

Any ideas on what may be the cause?

---

### 评论 #10 — parallelo (2016-12-23T04:20:25Z)

FYI - This simple example works on my development system.  

Start by installing ROCm and its OpenCL implementation: 

`sudo apt-get install rocm opencl-rocm`

Then, build and run this very simple OCL app..

Grab the HelloWorld sample:  
`wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cpp`
`wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cl`

Build it using the default ROCm OpenCL include and library locations: 
`g++ -I /opt/rocm/opencl/include/opencl1.2  ./HelloWorld.cpp -o HelloWorld -L /opt/rocm/opencl/lib/x86_64 -lOpenCL`

Run it:
`./HelloWorld 
`

---

### 评论 #11 — rjfnobre (2016-12-23T11:10:34Z)

Finally OpenCL is working!

I was missing the 'opencl-rocm' package.
It was not automatically instaled by upgradint the ROCm packages.

After that I just had to remove the 'AMDAPPSDK-3.0' OpenCL libraries from the $LD_LIBRARY environment variable.

---

### 评论 #12 — parallelo (2016-12-23T15:38:25Z)

Happy to hear it.  We'll plan to post a simple ROCm OpenCL Quickstart Guide on GPUOpen.com to ensure it is more clear for everyone. 

---

### 评论 #13 — boxerab (2016-12-23T15:41:32Z)

awesome!! Fantastic. OK, can't help myself - any idea on when full OpenCL 1.2 support is coming to ROCm ?
Need image support.  Thanks!

---

### 评论 #14 — jedwards-AMD (2017-01-03T19:14:15Z)

I cannot confirm specific dates, but full support should be available in a summer release.

---

### 评论 #15 — boxerab (2017-01-03T19:21:22Z)

Great, thank you @jedwards-AMD .  Can't wait!

---
