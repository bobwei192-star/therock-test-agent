# Trivial OpenCL program fails under ROCm upstream kernel with gfx900

> **Issue #893**
> **状态**: closed
> **创建时间**: 2019-09-26T19:54:42Z
> **更新时间**: 2019-11-27T23:43:00Z
> **关闭时间**: 2019-11-27T23:43:00Z
> **作者**: drkoller
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/893

## 描述

Included below is a very simple OpenCL program that does not work correctly on several of our ROCm installations (upstream Linux kernel driver and gfx900 cards). The program simply creates two OpenCL buffers, writes data into them, and then reads the data back and verifies that the values are unchanged. If the total size of the two buffers exceeds one megabyte, then the data gets corrupted under ROCm OpenCL.

We've tested this program on several different desktop computers, all running Ubuntu 18.04 with kernel versions ranging from 4.19 through 5.2.  We used ROCm versions 2.6.22 and 2.7.27 and the upstream kernel driver (**not** `rock-dkms`), with ROCm OpenCL driver versions ranging from 2906.7 through 2949.0. Each test computer had either an RX Vega 56 or Vega 64 card (gfx900) installed. The program misbehaved (non-deterministically) when run on these computers with ROCm. However, the test computers ran the program successfully when a gfx803 card was used instead, or if the ROCk kernel driver was installed, or if ROCm was replaced with the AMDGPU-PRO OpenCL driver.

Program C++ source code:
```
#include <stdio.h>
#include <vector>
#include <CL/opencl.h>

#define DATA_SIZE 1200000
#define OPENCL_PLATFORM 0
#define OPENCL_DEVICE 0

int main(void)
{
  cl_uint platformIdCount = 0;
  clGetPlatformIDs (0, NULL, &platformIdCount);
  std::vector<cl_platform_id> platformIds (platformIdCount);
  clGetPlatformIDs (platformIdCount, platformIds.data (), NULL);

  cl_uint deviceIdCount;
  clGetDeviceIDs(platformIds[OPENCL_PLATFORM], CL_DEVICE_TYPE_ALL, 0, NULL, &deviceIdCount);
  std::vector<cl_device_id> deviceIds (deviceIdCount);
  clGetDeviceIDs (platformIds[OPENCL_PLATFORM], CL_DEVICE_TYPE_ALL, deviceIdCount, deviceIds.data(), NULL);

  char deviceName[500];
  clGetDeviceInfo(deviceIds[OPENCL_DEVICE], CL_DEVICE_NAME, 500, deviceName, NULL);
  printf("OpenCL Device: %s\n", deviceName);

  const cl_context_properties contextProperties [] = {CL_CONTEXT_PLATFORM,
    reinterpret_cast<cl_context_properties> (platformIds[OPENCL_PLATFORM]), 0};

  cl_context context = clCreateContext(contextProperties, 1, &deviceIds[OPENCL_DEVICE], NULL, NULL, NULL);
  cl_command_queue commands = clCreateCommandQueue(context, deviceIds[OPENCL_DEVICE], 0, NULL);

  cl_mem inbuf1 = clCreateBuffer(context, CL_MEM_READ_ONLY, DATA_SIZE, NULL, NULL);
  cl_mem inbuf2 = clCreateBuffer(context, CL_MEM_READ_ONLY, DATA_SIZE, NULL, NULL);

  unsigned char *data1 = new unsigned char[DATA_SIZE];
  for (int i = 0; i < DATA_SIZE; i++)
    data1[i] = i % 256;

  unsigned char *data2 = new unsigned char[DATA_SIZE];
  for (int i = 0; i < DATA_SIZE; i++)
    data2[i] = (i+128) % 256;

  clEnqueueWriteBuffer(commands, inbuf1, CL_TRUE, 0, DATA_SIZE, data1, 0, NULL, NULL);
  clEnqueueWriteBuffer(commands, inbuf2, CL_TRUE, 0, DATA_SIZE, data2, 0, NULL, NULL);

  unsigned char *data3 = new unsigned char[DATA_SIZE]();
  unsigned char *data4 = new unsigned char[DATA_SIZE]();

  clEnqueueReadBuffer(commands, inbuf1, CL_TRUE, 0, DATA_SIZE, data3, 0, NULL, NULL);
  clEnqueueReadBuffer(commands, inbuf2, CL_TRUE, 0, DATA_SIZE, data4, 0, NULL, NULL);

  unsigned int correct = 0;
  for (int i = 0; i < DATA_SIZE; i++)
    if (data1[i] == data3[i] && data2[i] == data4[i])
      ++correct;
  printf ("%d out of %d bytes read back correctly.\n", correct, DATA_SIZE);
}
```
The program functions correctly under the ROCm/gfx900/upstream kernel configuration only if the total memory of the two buffers is less than a megabyte, or if only one buffer is created instead of two.

Other simple OpenCL programs that create multiple buffers fail on our ROCm systems as well. For example, the program here:

https://github.com/HandsOnOpenCL/Exercises-Solutions/blob/master/Exercises/Exercise02/C/vadd_c.c

fails similarly if the `LENGTH` macro definition is increased to make the input buffer sizes exceed one megabyte.

Our testing suggests that this is a bug somewhere in the ROCm OpenCL software stack when using the upstream kernel and gfx900 GPU. I'm happy to provide further information that would help resolve this.

---

## 评论 (6 条)

### 评论 #1 — Moading (2019-09-26T20:29:44Z)

Hi, I am developing an OpenCL program that uses about 20 buffers with a size between 1 and 10.000 MB. Reading and writing these buffers works under ROCm.

You are creating inbuf1 and inbuf2 with CL_MEM_READ_ONLY but you are performing both reads and writes. Maybe you have to create these buffers with CL_MEM_READ_WRITE ?

---

### 评论 #2 — drkoller (2019-09-26T20:52:12Z)

Thanks for your comment, @Moading. I'm glad that ROCm OpenCL is working well for you. Can you compile and run the posted program successfully on your system? Do any of your software component versions differ significantly from those I posted?

 The CL_MEM_READ_ONLY flag applies when the buffer is accessed by a kernel, which doesn't matter in this case, since no kernels are executed. Using CL_MEM_READ_WRITE did not affect my test results.

---

### 评论 #3 — acowley (2019-09-27T02:21:48Z)

FWIW, I've not encountered what you're seeing, and your program works for me. Tested using ROCm 2.7 on NixOS with Linux 5.2.13 and an RX580 (gfx803) GPU. I tried bumping `#define DATA_SIZE 12000000` and ran the program in a bash loop 100x, but didn't see any failures.

---

### 评论 #4 — Moading (2019-09-27T10:15:20Z)

Same here, the program runns successfully using ROCm 2.6.22 on ubuntu 18.4.3. THe GPU is a gfx803. DATA_SIZE was 512000000.

---

### 评论 #5 — drkoller (2019-09-27T18:22:23Z)

Thanks a lot to both of you, @acowley and @Moading, for taking the time to run this test program and share your results. This helps us to isolate the cause of the problem.

The erroneous behavior that we're observing is only on gfx900 cards with ROCm using the upstream Linux kernel driver. The program works correctly on our gfx803 cards or when using the ROCk kernel driver (`rock-dkms`).

---

### 评论 #6 — drkoller (2019-11-27T23:43:00Z)

The problematic behavior seems to have gone away after upgrading to Ubuntu 19.10, kernel version 5.3, and ROCm version 2.9, so I am closing this issue.

---
