# ROCm OpenCL performance > 10x slower compared to clover

> **Issue #1337**
> **状态**: closed
> **创建时间**: 2020-12-14T07:04:16Z
> **更新时间**: 2021-01-28T06:53:11Z
> **关闭时间**: 2021-01-28T06:53:11Z
> **作者**: jpsollie
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1337

## 描述

Setup:
Amd Threadripper 1950X, 32GB DDR4-3400
2x R9 Nano
Gentoo linux 5.9, no rocm kernel module (due too not supported for 5.9 kernels)
Issue:
benchmarking rocm 3.9 and 3.10 on a system with 2x R9 nano gpus is > 10x slower on ROCm compared to clover (if it runs at all, is highly unstable):
` echo $(date +%%%s.%N%% && ./a.out && date +%%%s.%N%%) >> rocm.txt `
gives (executed 3 times):
```
%1607587105.151533938% Result: 11168608085589920491 Runtime: 0.012519ms %1607587130.296327194%
%1607670831.441274542% Result: 11168608085589920491 Runtime: 0.013072ms %1607670855.944835450% 
%1607670999.627702896% Result: 11168608085589920491 Runtime: 0.012555ms %1607671024.114541166%
```
while on clover, it becomes:
```
%1607525532.830965431% Result: 11168608085589920491 Runtime: 0.000692ms %1607525557.858665546% 
%1607525898.437019510% Result: 11168608085589920491 Runtime: 0.001562ms %1607525923.446692449% 
%1607525926.138453752% Result: 11168608085589920491 Runtime: 0.000700ms %1607525950.744559860%
```
the benchmark was a slightly modified version of opencl-benchmark [here](https://github.com/huytd/opencl-benchmark) on github, modified to ensure its correctness (replaced malloc with calloc, specified opencl version 110) while calculating numbers + increased the load to get more accurate results:
```
kernel void hello(global ulong *val) {                                                                                                                           
size_t i = get_global_id(0);                                                                                                                                   
for (ulong j = 0; j < 10000000000000; j++) {                                                                                                                     
val[i] += j;                                                                                                                                                 
}                                                                                                                                                              
for (ulong j = 0; j < 10000000000000; j++) {                                                                                                                     
val[i] -= j;                                                                                                                                                 
}                                                                                                                                                            
//    val[i] = 0;                                                                                                                                                
for (ulong j = 0; j < 200000000; j++) {                                                                                                                          
val[i] += (j >> 1) * j;                                                                                                                                      
}                                                                                                                                                            
/*  for (ulong j = 0; j < 10000000000; j++) {                                       // system locks up                                                                               
val[i] += j >> 2;                                                                                                                                            
} */                                                                                                                                                         
}
```
If you need it, let me know

---

## 评论 (12 条)

### 评论 #1 — ROCmSupport (2020-12-14T08:39:42Z)

Thanks @jpsollie for reaching out.
We will check and get back soon.
Can you please share the code(with all changes incorporated), so that we can give a try.
Thank you.

---

### 评论 #2 — jpsollie (2020-12-14T08:49:27Z)

gpu.c:
```#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define CL_TARGET_OPENCL_VERSION 110

#ifdef __APPLE__
#include <OpenCL/opencl.h>
#else
#include <CL/cl.h>
#endif

#define MAX_SOURCE_SIZE (0x100000)

int main() {
  cl_device_id device_id = NULL;
  cl_context context = NULL;
  cl_command_queue command_queue = NULL;
  cl_mem memobj = NULL;
  cl_program program = NULL;
  cl_kernel kernel = NULL;
  cl_platform_id platform_id = NULL;
  cl_uint ret_num_devices;
  cl_uint ret_num_platforms;
  cl_int ret;

  cl_ulong val[1];

  FILE *fp;
  char fileName[] = "./sum.cl";
  char *source_str;
  size_t source_size;

  fp = fopen(fileName, "r");
  if (!fp) {
    fprintf(stderr, "Failed to load kernel\n");
    exit(1);
  }
  source_str = (char*)calloc(1, MAX_SOURCE_SIZE);
  source_size = fread(source_str, 1, MAX_SOURCE_SIZE, fp);
  fclose(fp);

  ret = clGetPlatformIDs(1, &platform_id, &ret_num_platforms);
  ret = clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_DEFAULT, 1, &device_id, &ret_num_devices);

  context = clCreateContext(NULL, 1, &device_id, NULL, NULL, &ret);
  command_queue = clCreateCommandQueue(context, device_id, 0, &ret);
  memobj = clCreateBuffer(context, CL_MEM_READ_WRITE | CL_MEM_COPY_HOST_PTR, sizeof(cl_mem), NULL, &ret);
  program = clCreateProgramWithSource(context, 1, (const char **)&source_str, (const size_t *)&source_size, &ret);
  ret = clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);
  kernel = clCreateKernel(program, "hello", &ret);

  ret = clSetKernelArg(kernel, 0, sizeof(cl_mem), (void*)&memobj);

  clock_t begin = clock();

  ret = clEnqueueTask(command_queue, kernel, 0, NULL, NULL);

  ret = clEnqueueReadBuffer(command_queue, memobj, CL_TRUE, 0, sizeof(cl_mem), val, 0, NULL, NULL);

  clock_t end = clock();
  double runtime = (double)(end - begin) / CLOCKS_PER_SEC;

  ret = clFlush(command_queue);
  ret = clFinish(command_queue);
  ret = clReleaseKernel(kernel);
  ret = clReleaseProgram(program);
  ret = clReleaseMemObject(memobj);
  ret = clReleaseCommandQueue(command_queue);
  ret = clReleaseContext(context);

  printf("Result: %llu\n", val[0]);
  printf("Runtime: %lfms\n", runtime);
  
  free(source_str);

  return 0;
}
```
sum.cl (same as above):
```
kernel void hello(global ulong *val) {                                                                                                                           
size_t i = get_global_id(0);                                                                                                                                   
for (ulong j = 0; j < 10000000000000; j++) {                                                                                                                     
val[i] += j;                                                                                                                                                 
}                                                                                                                                                              
for (ulong j = 0; j < 10000000000000; j++) {                                                                                                                     
val[i] -= j;                                                                                                                                                 
}                                                                                                                                                            
//    val[i] = 0;                                                                                                                                                
for (ulong j = 0; j < 200000000; j++) {                                                                                                                          
val[i] += (j >> 1) * j;                                                                                                                                      
}                                                                                                                                                            
/*  for (ulong j = 0; j < 10000000000; j++) {                                       // system locks up                                                                               
val[i] += j >> 2;                                                                                                                                            
} */                                                                                                                                                         
}
```
compiled using:
`gcc -lOpenCL gpu.c `


---

### 评论 #3 — ROCmSupport (2020-12-15T12:13:25Z)

Thanks @jpsollie for the code.
Its showing some code errors for me.

taccuser@taccuser-X399-DESIGNARE-EX:~$ gcc -lOpenCL -I/opt/rocm/opencl/include gpu.c
gpu.c: In function ‘main’:
gpu.c:27:3: error: unknown type name ‘FILE’
   27 |   FILE *fp;
      |   ^~~~
gpu.c:9:1: note: ‘FILE’ is defined in header ‘<stdio.h>’; did you forget to ‘#include <stdio.h>’?
    8 | #include <CL/cl.h>
  +++ |+#include <stdio.h>
    9 | #endif
gpu.c:32:8: warning: implicit declaration of function ‘fopen’ [-Wimplicit-function-declaration]
   32 |   fp = fopen(fileName, "r");
      |        ^~~~~
gpu.c:32:8: note: ‘fopen’ is defined in header ‘<stdio.h>’; did you forget to ‘#include <stdio.h>’?
gpu.c:32:6: warning: assignment to ‘int *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
   32 |   fp = fopen(fileName, "r");
      |      ^
gpu.c:34:5: warning: implicit declaration of function ‘fprintf’ [-Wimplicit-function-declaration]
   34 |     fprintf(stderr, "Failed to load kernel\n");
      |     ^~~~~~~
gpu.c:34:5: warning: incompatible implicit declaration of built-in function ‘fprintf’
gpu.c:34:5: note: include ‘<stdio.h>’ or provide a declaration of ‘fprintf’
gpu.c:34:13: error: ‘stderr’ undeclared (first use in this function)
   34 |     fprintf(stderr, "Failed to load kernel\n");
      |             ^~~~~~
gpu.c:34:13: note: ‘stderr’ is defined in header ‘<stdio.h>’; did you forget to ‘#include <stdio.h>’?
gpu.c:34:13: note: each undeclared identifier is reported only once for each function it appears in
gpu.c:38:17: warning: implicit declaration of function ‘fread’ [-Wimplicit-function-declaration]
   38 |   source_size = fread(source_str, 1, MAX_SOURCE_SIZE, fp);
      |                 ^~~~~
gpu.c:39:3: warning: implicit declaration of function ‘fclose’ [-Wimplicit-function-declaration]
   39 |   fclose(fp);
      |   ^~~~~~
gpu.c:70:3: warning: implicit declaration of function ‘printf’ [-Wimplicit-function-declaration]
   70 |   printf("Result: %llu\n", val[0]);
      |   ^~~~~~
gpu.c:70:3: warning: incompatible implicit declaration of built-in function ‘printf’
gpu.c:70:3: note: include ‘<stdio.h>’ or provide a declaration of ‘printf’
gpu.c:70:22: warning: format ‘%llu’ expects argument of type ‘long long unsigned int’, but argument 2 has type ‘cl_ulong’ {aka ‘long unsigned int’} [-Wformat=]
   70 |   printf("Result: %llu\n", val[0]);
      |                   ~~~^     ~~~~~~
      |                      |        |
      |                      |        cl_ulong {aka long unsigned int}
      |                      long long unsigned int
      |                   %lu


---

### 评论 #4 — jpsollie (2020-12-15T13:11:38Z)

Sorry, wrong C/P,
Adding
`#include <stdio.h>`
at the top fixes it, forgot to include 1st line

---

### 评论 #5 — ROCmSupport (2020-12-16T05:09:00Z)

Hi @jpsollie 
I tried in 2 different machines and below error is observed.

taccuser@taccuser-All-Series:~$ gcc -L/opt/rocm/opencl/lib -I/opt/rocm/opencl/include -lOpenCL gpu.c
gpu.c: In function ‘main’:
gpu.c:71:22: warning: format ‘%llu’ expects argument of type ‘long long unsigned int’, but argument 2 has type ‘cl_ulong {aka long unsigned int}’ [-Wformat=]
   printf("Result: %llu\n", val[0]);
                   ~~~^     ~~~~~~
                   %lu
/tmp/cceDgyFB.o: In function `main':
gpu.c:(.text+0x103): undefined reference to `clGetPlatformIDs'
gpu.c:(.text+0x133): undefined reference to `clGetDeviceIDs'
gpu.c:(.text+0x167): undefined reference to `clCreateContext'
gpu.c:(.text+0x18d): undefined reference to `clCreateCommandQueue'
gpu.c:(.text+0x1b6): undefined reference to `clCreateBuffer'
gpu.c:(.text+0x1dd): undefined reference to `clCreateProgramWithSource'
gpu.c:(.text+0x20a): undefined reference to `clBuildProgram'
gpu.c:(.text+0x22a): undefined reference to `clCreateKernel'
gpu.c:(.text+0x24b): undefined reference to `clSetKernelArg'
gpu.c:(.text+0x27a): undefined reference to `clEnqueueTask'
gpu.c:(.text+0x2b1): undefined reference to `clEnqueueReadBuffer'
gpu.c:(.text+0x2ee): undefined reference to `clFlush'
gpu.c:(.text+0x300): undefined reference to `clFinish'
gpu.c:(.text+0x312): undefined reference to `clReleaseKernel'
gpu.c:(.text+0x324): undefined reference to `clReleaseProgram'
gpu.c:(.text+0x336): undefined reference to `clReleaseMemObject'
gpu.c:(.text+0x348): undefined reference to `clReleaseCommandQueue'
gpu.c:(.text+0x35a): undefined reference to `clReleaseContext'
collect2: error: ld returned 1 exit status


---

### 评论 #6 — jpsollie (2020-12-16T05:42:52Z)

Those are linker errors. Any idea why your opencl libs do not find any function? Because those are definitely not code-related, more like gcc not finding the right OpenCL.so library for linking the opencl functions against

---

### 评论 #7 — baryluk (2020-12-26T01:06:05Z)

You need to put `-lOpenCL` AFTER gpu.c. Like this: `cc -o gpu gpu.c  -lOpenCL`. The order is important.

---

### 评论 #8 — baryluk (2020-12-26T01:12:41Z)

@jpsollie Please add error handling to your code, with error messages to screen and exit.. One of the cl* functions is returning an error for me. So this example can't be run.

---

### 评论 #9 — baryluk (2020-12-26T01:16:03Z)

Closer inspection of your code, shows it is not using OpenCL APIs correctly. It is making calls which are prohibited by OpenCL standard, and if you do, it is undefined behaviour. It can work, it can do something, it can be ignored, it can crash, who knows.

---

### 评论 #10 — ROCmSupport (2021-01-05T07:27:08Z)

Hi @jpsollie 
Can you please respond to @baryluk comments above.
Thank you.

---

### 评论 #11 — jpsollie (2021-01-05T10:56:53Z)

when I look at this one: https://github.com/RadeonOpenCompute/ROCm/issues/1265#issuecomment-753898516
does it still matter?

---

### 评论 #12 — ROCmSupport (2021-01-28T06:53:11Z)

Thanks @jpsollie for the point.
gfx8 is no more officially supported device. Closing it now.
Thank you.

---
