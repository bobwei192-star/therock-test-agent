# RocM HIP vs OpenCL performance

- **Issue #:** 1679
- **State:** closed
- **Created:** 2022-02-16T10:40:03Z
- **Updated:** 2024-05-07T21:12:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/1679

Dear ROCM developers.

First I wanted to thanks for creating the HIP interface.

I was trying to asses the performance of HIP vs OpenCL

I tried to use the miniBUDE benchmark. Is a benchmark that came out of ISC 2021 as best paper award.

https://github.com/UoB-HPC/miniBUDE

I tried to run that benchmark on my Vega 64. With ROCM 4.5.

Than I also tried to take the CUDA version. converted manually to hip (just have to change some cuda function into hip). Activate shared memory (because the OpenCL version use shared memory). (-ffast-math to emulate the OpenCL options)


I am not sure why is happening. looking at the .s with --save-temps

main-hip-amdgcn-amdhsa-gfx900:xnack-.s. It seems that OpenCL has the tendency to create a kernel that use much more register (with less occupancy) than the one with HIP.



I attach the CUDA version converted to HIP because is condensated everything in one file can be compiled easily with

hipcc -O3 -march=native -std=c++14 -ffast-math -mcpu=gfx900:xnack- -DUSE_SHARED bude.cpp -o bude

and run with

./bude -n 131072 -w 128

The original OpenCL miniBUDE

is in the original repo 

https://github.com/UoB-HPC/miniBUDE/tree/master/opencl

I run as well with

./bude -n 131072 -w 128

P.S. I make sure that shared is used on both cases and NUM_TD_PER_THREAD=4 


Thanks gmarkomanolis. I missed that option.






