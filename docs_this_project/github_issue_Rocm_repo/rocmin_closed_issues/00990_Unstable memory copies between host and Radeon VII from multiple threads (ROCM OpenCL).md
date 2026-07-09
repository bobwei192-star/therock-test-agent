# Unstable memory copies between host and Radeon VII from multiple threads (ROCM OpenCL)

- **Issue #:** 990
- **State:** closed
- **Created:** 2020-01-02T14:31:50Z
- **Updated:** 2020-01-09T15:42:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/990

Hi there,

I recently bought a Radeon VII and I've been experimenting with ROCM for an OpenCL-enabled research code. The application uses multiple threads to stream data in and out of multiple OpenCL compute devices and uses host memory to store and synchronize the information to host memory between iterations. 

I've been using clEnqueue(Read|Write)BufferRect to facilitate the memory copies. This has worked fairly well with other OpenCL implementations such as Portable OpenCL and NVIDIA's implementation. However with ROCM on my Radeon VII the copies seem to be unstable and crash my system. They nearly always force a reboot. 

Attached [here](https://github.com/RadeonOpenCompute/ROCm/files/4016157/test_one_init.cpp.txt) is some C++ code that replicates the issue that I'm seeing. On other OpenCL platforms it is stable and returns the time taken to copy 170 slices of a 1024^3 grid, usually about 1 second per device. On the Radeon VII with ROCM it takes either up to a minute to complete the copy or else crashes my system. At this stage I don't know if the  graphics card has a problem or the ROCM library I am using has a bug. Here is a summary of relevant software/hardware:

- OpenSUSE 15.1 with kernel 5.4.6-1.ge5f8301-default
- ROCM OpenCL 2.0.0 (package rocm-opencl*) from http://repo.radeon.com/rocm/zyp/3.0/. 
- AMDGPU-pro drivers (19.30-934562) for the Radeon VII. 
- CPU is a Threadripper 2950x on a Gigabyte Designare X399 motherboard.
- Compiler g++-8 (SUSE Linux) 8.2.1 20180831 [gcc-8-branch revision 264010]

Hope this is enough information to be useful. I'd really like to find a resolution to the problem! The example code is reproduced below.

```C++
#include <thread>
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cassert>
#include <iostream>
#include <chrono>
#include "CL/cl.hpp"

#define TARGET_DEVICES CL_DEVICE_TYPE_ALL

#define NX 1024
#define NY 1024
#define NZ 1024
#define NTHREADS 6
#define MAXCHAR 100

typedef double float_type;

// OpenCL error checking function
void errchk(cl_int code, const char* activity) {
    if (code!=CL_SUCCESS) {
        printf("OpenCL Error: code %d at %s \n", code, activity);
    }
    assert(code==CL_SUCCESS);
}

void worker(int64_t rank, int64_t nworkers, float_type* host_ptr, 
        cl_platform_id compute_platform, cl_device_id compute_device) {

    // Errorcode on transactions
    cl_int errcode;

    // Create a context and a command queue
    const cl_context_properties prop[] = { CL_CONTEXT_PLATFORM, (cl_context_properties)compute_platform, 0 };
    cl_context compute_context=clCreateContext(prop, 1, &compute_device, NULL, NULL, &errcode);
    errchk(errcode,"creating a context");
    cl_command_queue compute_queue=clCreateCommandQueue(compute_context, compute_device, 0, &errcode);

    // Allocate memory on the compute context
    size_t nbytes_buffer=NX*NY*sizeof(float_type);
    cl_mem buffer = clCreateBuffer(compute_context, CL_MEM_READ_WRITE, nbytes_buffer, NULL, &errcode);
    errchk(errcode,"creating a buffer");

    // Get the name of the device
    char cname[MAXCHAR];
    errchk(clGetDeviceInfo(compute_device, 
        CL_DEVICE_NAME, 
        MAXCHAR,
        (void*)cname,
        NULL),"retrieving device name");
    std::string device_name(cname);

    // Work out how many slices to process for each thread
    int64_t slice_size=NZ/nworkers;
    int64_t start=rank*slice_size;
    int64_t stop=(rank+1)*slice_size;
    if (rank==nworkers-1) {
        stop=NZ;
    }

    // Start the clock
    auto t1=std::chrono::high_resolution_clock::now(); // Start the timer

    // Iterate over slices
    for (int64_t z=start; z<stop; z++) {

        // Copy a slice of the domain to the device with WriteBufferRect
        size_t host_origin[3] = {0, 0, (size_t)z};
        size_t buffer_origin[3] = {0, 0, 0};
        size_t region[3] = {NX*sizeof(float_type), NY, 1};
        errchk(clEnqueueWriteBufferRect(compute_queue, buffer, CL_TRUE, buffer_origin, 
                host_origin, region, 0, 0, 0, 0, host_ptr, 0, NULL, NULL), "copy from host to device buffer");

        // Do some operation on the device buffer, in this case we fill it with something....
        float_type fill=(float_type)z;
        errchk(clEnqueueFillBuffer(compute_queue, buffer, &fill, sizeof(float_type), 0, nbytes_buffer, 0, NULL, NULL), "fill buffer");
        
        // Copy the slice back to the host array
        errchk(clEnqueueReadBufferRect(compute_queue, buffer, CL_TRUE, buffer_origin, 
                host_origin, region, 0, 0, 0, 0, host_ptr, 0, NULL, NULL), "copy from device to host buffer");

    }

    // Stop the clock
    auto t2=std::chrono::high_resolution_clock::now(); 
    auto diff=std::chrono::duration_cast<std::chrono::duration<double>>(t2-t1);
    double dt=diff.count(); // Get the difference in seconds

    // Finish and release resources
    errchk(clReleaseMemObject(buffer), "Releasing the buffer");
    errchk(clReleaseCommandQueue(compute_queue), "Releasing compute_queue");
    errchk(clReleaseContext(compute_context), "Releasing the context");

    std::cout << "Device " << device_name << " finished " << stop-start << " slices in " << dt << " seconds." << std::endl;
}

int main() {
    // Make some host memory, NX is fastest axis
    float_type *array = new float_type [NX*NY*NZ];
    
    // Errorcode on transactions
    cl_int errcode;

    // Fetch all platforms
    cl_uint numPlatforms;
    std::vector<cl_platform_id> platforms;

    // Fetch the number of platforms
    errchk(clGetPlatformIDs(0, NULL, &numPlatforms),"getting number of platforms");
    platforms.resize(numPlatforms);
    errchk(clGetPlatformIDs(numPlatforms, platforms.data(), NULL),"getting the platforms");

    // Platform id
    std::vector<cl_platform_id> temp_platforms; 
    std::vector<cl_device_id> devices;    

    // Loop over platforms and find devices
    for (cl_uint i=0; i<numPlatforms; i++) {
        cl_uint ndevices;
        errcode=clGetDeviceIDs(platforms[i], TARGET_DEVICES, 0, NULL, &ndevices);

        if (errcode==CL_SUCCESS) {
            cl_device_id* temp_devices = new cl_device_id[ndevices];
            errchk(clGetDeviceIDs(platforms[i], TARGET_DEVICES, ndevices, temp_devices, NULL),"fill devices array");
            for (cl_uint n=0; n<ndevices; n++) {
                devices.push_back(temp_devices[n]);
                temp_platforms.push_back(platforms[i]);    
            }
            delete [] temp_devices;
        }    
    }

    std::cout << "Number of devices found = " << devices.size() << std::endl;    

    // Make sure we have found at least one compute device
    if (devices.size()==0) {
        std::cerr << "Sorry, couldn't find any valid OpenCL devices" << std::endl;
        exit(EXIT_FAILURE);
    }

    // Execute threads, one thread for each slice along NZ
    std::thread worker_threads[NTHREADS];
    for (int64_t t=0; t<NTHREADS; t++) {
        cl_uint index = t%devices.size();
        worker_threads[t]=std::thread(worker, t, (int64_t)NTHREADS, array, 
                temp_platforms[index], devices[index]);
    }

    // Wait for threads to finish
    for (int64_t t=0; t<NTHREADS; t++) {
        worker_threads[t].join();
    }

    delete [] array;
}
```
