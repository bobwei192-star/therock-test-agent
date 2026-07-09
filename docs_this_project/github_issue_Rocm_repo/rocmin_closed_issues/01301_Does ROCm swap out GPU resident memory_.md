# Does ROCm swap out GPU resident memory?

- **Issue #:** 1301
- **State:** closed
- **Created:** 2020-11-23T12:59:11Z
- **Updated:** 2020-12-07T19:36:53Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/1301

ROCm 3.9, Ubuntu 20.04, RX 5700

In OpenCL, I tried some experiments to check whether the buffer swap out (GPU->CPU) happens or not.
I repeated below steps without any memory release operation.

1. Create 3 buffers (2GB for each, 6GB total)
2. Launch vector addition kernel with those buffers

My GPU has 8GB memory and I expected that it can't be repeated more than once.
But somehow those steps are repeated many times (4 or 5 time) and crashed.

Can someone explain what is happening?
Are memory buffers evicted from GPU memory?

```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <CL/cl.h>
#include <time.h>
 
inline static void _OPENCL(cl_int ret,
  const char *file = __builtin_FILE(), int line = __builtin_LINE()) {
  if (ret != CL_SUCCESS) {
    printf("[%s:%d] OpenCL error %d\n", file, line, ret);
    exit(EXIT_FAILURE);
  }
}

static inline float diff_timespec_ms(struct timespec st, struct timespec ed)
{
  return (ed.tv_sec - st.tv_sec) * 1000 +
    (ed.tv_nsec - st.tv_nsec) / 1000000.0;
}

#define START_STOPWATCH                                     \
  {                                                            \
    struct timespec st;                                        \
    clock_gettime(CLOCK_MONOTONIC, &st);
#define STOP_STOPWATCH(tg)                                  \
    struct timespec ed;                                        \
    clock_gettime(CLOCK_MONOTONIC, &ed);                       \
    fprintf(stderr,"%s: %fms\n", tg, diff_timespec_ms(st, ed));\
  }

// OpenCL kernel. Each work item takes care of one element of c
const char *kernelSource =                                       "\n" \
"#pragma OPENCL EXTENSION cl_khr_fp64 : enable                    \n" \
"__kernel void vecAdd(  __global double *a,                       \n" \
"                       __global double *b,                       \n" \
"                       __global double *c,                       \n" \
"                       const unsigned int n)                    \n" \
"{                                                               \n" \
"    //Get our global thread ID                                  \n" \
"    int id = get_global_id(0);                                  \n" \
"                                                                \n" \
"    //Make sure we do not go out of bounds                      \n" \
"    if (id < n)                                                 \n" \
"        c[id] = a[id] + b[id];                                  \n" \
"}                                                               \n" \
                                                                "\n" ;
 
int main( int argc, char* argv[] )
{
    // Length of vectors
    unsigned int n = 1024 * 1024 * 500;
 
    // Host input vectors
    double *h_a;
    double *h_b;
    // Host output vector
    double *h_c;
 
    // Device input buffers
    cl_mem d_a[100];
    cl_mem d_b[100];
    // Device output buffer
    cl_mem d_c[100];
 
    cl_platform_id cpPlatform;        // OpenCL platform
    cl_device_id device_id;           // device ID
    cl_context context;               // context
    cl_command_queue queue;           // command queue
    cl_program program;               // program
    cl_kernel kernel;                 // kernel
 
    // Size, in bytes, of each vector
    size_t bytes = n*sizeof(double);
 
    // Allocate memory for each vector on host
    h_a = (double*)malloc(bytes);
    h_b = (double*)malloc(bytes);
    h_c = (double*)malloc(bytes);
 
    // Initialize vectors on host
    int i;
    for( i = 0; i < n; i++ )
    {
        h_a[i] = 0.1;
        h_b[i] = 0.1;
    }
 
    size_t globalSize, localSize;
    cl_int err;
 
    // Number of work items in each local work group
    localSize = 64;
 
    // Number of total work items - localSize must be devisor
    globalSize = ceil(n/(float)localSize)*localSize;
 
    // Bind to platform
    err = clGetPlatformIDs(1, &cpPlatform, NULL);
 
    // Get ID for the device
    err = clGetDeviceIDs(cpPlatform, CL_DEVICE_TYPE_GPU, 1, &device_id, NULL);

    char tmp[1024] = {0,};
    clGetDeviceInfo(device_id, CL_DEVICE_NAME, 1024, tmp, NULL);
      printf("%s\n",tmp);
 
    // Create a context 
    context = clCreateContext(0, 1, &device_id, NULL, NULL, &err);
 
    // Create a command queue
    queue = clCreateCommandQueue(context, device_id, 0, &err);
 
    // Create the compute program from the source buffer
    program = clCreateProgramWithSource(context, 1,
                            (const char **) & kernelSource, NULL, &err);
 
    // Build the program executable
    clBuildProgram(program, 0, NULL, NULL, NULL, NULL);
 
    // Create the compute kernel in the program we wish to run
    kernel = clCreateKernel(program, "vecAdd", &err);
 
    // Create the input and output arrays in device memory for our calculation
    

    for (int j = 0; j < 5; j++) {
      d_a[j] = clCreateBuffer(context, CL_MEM_READ_WRITE, bytes, NULL, &err);
      _OPENCL(err);

      d_b[j] = clCreateBuffer(context, CL_MEM_READ_WRITE, bytes, NULL, &err);
      _OPENCL(err);

      d_c[j] = clCreateBuffer(context, CL_MEM_READ_WRITE, bytes, NULL, &err);
      _OPENCL(err);
    }

    for (int j = 0; j < 5; j++) {
      if (j == 4) j = 0;
      printf("%d\n", j);
      cl_int err;

      // Write our data set into the input array in device memory
      err = clEnqueueWriteBuffer(queue, d_a[j], CL_TRUE, 0,
                                   bytes, h_a, 0, NULL, NULL);
      err |= clEnqueueWriteBuffer(queue, d_b[j], CL_TRUE, 0,
                                   bytes, h_b, 0, NULL, NULL);
 
      // Set the arguments to our compute kernel
      err  = clSetKernelArg(kernel, 0, sizeof(cl_mem), &d_a[j]);
      err |= clSetKernelArg(kernel, 1, sizeof(cl_mem), &d_b[j]);
      err |= clSetKernelArg(kernel, 2, sizeof(cl_mem), &d_c[j]);
      err |= clSetKernelArg(kernel, 3, sizeof(unsigned int), &n);
      _OPENCL(err);
  
      // Execute the kernel over the entire range of the data set 
      err = clEnqueueNDRangeKernel(queue, kernel, 1, NULL, &globalSize, &localSize,
                            0, NULL, NULL);
      _OPENCL(err);
      
      // Wait for the command queue to get serviced before reading back results
      _OPENCL(clFinish(queue));

            // Read the results from the device
      _OPENCL(clEnqueueReadBuffer(queue, d_c[j], CL_TRUE, 0,
                      bytes, h_c, 0, NULL, NULL ));
   
      /*
      _OPENCL(clEnqueueMigrateMemObjects(queue, 1, &d_a[j], CL_MIGRATE_MEM_OBJECT_HOST, 0, nullptr, nullptr));
      _OPENCL(clEnqueueMigrateMemObjects(queue, 1, &d_b[j], CL_MIGRATE_MEM_OBJECT_HOST, 0, nullptr, nullptr));
      _OPENCL(clEnqueueMigrateMemObjects(queue, 1, &d_c[j], CL_MIGRATE_MEM_OBJECT_HOST, 0, nullptr, nullptr));
      _OPENCL(clFinish(queue));
      */

      //Sum up vector c and print result divided by n, this should equal 1 within error
      double sum = 0;
      for(i=0; i<n; i++)
              sum += h_c[i];
      printf("final result: %f\n", sum/n);
  }
 
  // release OpenCL resources
  return 0;
}


```