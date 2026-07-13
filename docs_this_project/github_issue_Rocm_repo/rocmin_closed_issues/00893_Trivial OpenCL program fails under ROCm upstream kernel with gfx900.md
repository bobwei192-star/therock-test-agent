# Trivial OpenCL program fails under ROCm upstream kernel with gfx900

- **Issue #:** 893
- **State:** closed
- **Created:** 2019-09-26T19:54:42Z
- **Updated:** 2019-11-27T23:43:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/893

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