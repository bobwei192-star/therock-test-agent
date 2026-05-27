# Performance issue with JCulpit Opencl-experiments Application on 1950X and 2 x Vega64.  - Wrong Wave Size Set in App.

> **Issue #265**
> **状态**: closed
> **创建时间**: 2017-11-27T10:12:06Z
> **更新时间**: 2017-12-01T23:29:18Z
> **关闭时间**: 2017-12-01T23:29:18Z
> **作者**: rico666
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/265

## 描述

So I thought when going for ROCm, investing in top-end AMD hardware would be a good idea...

So far, the only bright spot is the 1950X performance. The OpenCL performance of the two Vega64 cards can only be classified as nonexistant.

After two-man-weeks worth of hassle setting things up on a Ubuntu 17.10 to the point where clinfo at least doesn't crash, I'm trying to let some OpenCL programs run. And there are the results:

```
root@amd:~/tools-master# ./cl-demo 10 1000000
Choose platform:
[0] Advanced Micro Devices, Inc.
Enter choice: 0
Choose device:
[0] gfx900
[1] gfx900
Enter choice: 0
---------------------------------------------------------------------
NAME: gfx900
VENDOR: Advanced Micro Devices, Inc.
PROFILE: FULL_PROFILE
VERSION: OpenCL 1.2 
... yadda yadda ...
*** Set CL_HELPER_NO_COMPILER_OUTPUT_NAG=1 to disable this message.
0.000006 s
0.019669 GB/s
GOOD
```
0.019669 GB/s - wow. A 1080Ti does 170 GB/s there.

Trying another benchmark program, gives me warnings right away:

```
benchmarking... /tmp/AMD_4742_41/t_4742_43.cl:140:2: warning: null character ignored [-Wnull-character]
}<U+0000>
 ^
/tmp/AMD_4802_41/t_4802_43.cl:140:2: warning: null character ignored [-Wnull-character]
}<U+0000>
 ^
1 warning generated.
o*** Error in `./opencl-bench': corrupted double-linked list: 0x0000559cb21948b0 ***
```

Of course both programs work on everything from WX4100 over all the 1050/1060/1070/1080 and Quadro and Tesla cards.

So how am I going to improve things from here?

For starters, I'd like to know why https://github.com/jcupitt/opencl-experiments/tree/master/tools-master

gives me 8500 times worse benchmark results on a Vega64 than on a 1080Ti. Maybe from there on things will get better.

Some system info

```
root@amd:~/tools-master# lspci -v | grep -i vga
0a:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega [Radeon RX Vega] (rev c1) (prog-if 00 [VGA controller])
43:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega [Radeon RX Vega] (rev c1) (prog-if 00 [VGA controller])

root@amd:~/tools-master# uname -a
Linux amd 4.11.0-kfd-compute-rocm-rel-1.6-180 #1 SMP Tue Oct 10 08:15:38 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux

cat /opt/rocm/.info/version -> 1.6.180
```

---

## 评论 (14 条)

### 评论 #1 — gstoner (2017-11-27T14:29:29Z)

@rico666  First if your read our documentation you see we do not support 17.10 currently.   You're judging the stack by one application which is an experiment .   You might want to ask differently for help.   

We run a large number of applications on the stack during Q/A internally.  This is the first time we see this benchmark,  We look at this benchmark and let you know where the performance is being spent. 

---

### 评论 #2 — gstoner (2017-11-27T14:32:27Z)

If your interested in performance take a look at this benchmark 
https://github.com/ekondis/mixbench

---

### 评论 #3 — rico666 (2017-11-27T17:02:50Z)

Not exactly asking for help, merely making statements about ROCm performance on top AMD hardware.

I am judging the stack by its performance on **two** applications - one of which is mine and the other (JCulpit master-tools) is a very primitive low-level benchmark. Some years of SW-engineering have taught me to start with the less complex things.

As per your mixbench suggestion:

```
root@amd:~/mixbench# make
echo '#define VERSION_INFO "'`./query_version.sh`'"' >version_info.h
g++ -c -O2 -I/usr/local/cuda/include -Wall main-cuda.cpp -o main-cuda.o
main-cuda.cpp:9:10: fatal error: cuda.h: No such file or directory
 #include <cuda.h>
          ^~~~~~~~
compilation terminated.
Makefile:76: recipe for target 'main-cuda.o' failed
make: *** [main-cuda.o] Error 1
```

I have set the OpenCL paths, I have no CUDA on the machine. Seems it won't build without cuda. See above lessons about "less complex things".

addendum:

The reason I'm using a "Ubuntu 17.10 skeleton" is just because Ubuntu 16.04 installation failed on these Vega64 cards completely and because to keep things simple I didn't want to go for Gentoo this time. The right kernel, ROCm env and libs are in place. I do not expect to get prefabricated .deb packages.

addendum2:

The performance so far is abysmal. Changing the title does not change _that_.

addendum3:

at first, no problems with mixbench on my P50 notebook (Arch Linux, Quadro M2000M -> therefore CUDA installed)

```
# make
g++ -c -O2 -I/opt/cuda/include -Wall main-cuda.cpp -o main-cuda.o
/opt/cuda/bin/nvcc -gencode=arch=compute_60,code=\"compute_60\" -gencode=arch=compute_30,code=\"compute_30\" -O2 -I/opt/cuda/include --compiler-options -fno-strict-aliasing --ptxas-options=-v -Xptxas -dlcm=cg -DUNIX -c mix_kernels_cuda.cu -o mix_kernels_cuda.o
```
unfortunately after some minutes

https://github.com/ekondis/mixbench/issues/7


---

### 评论 #4 — ekondis (2017-11-27T17:43:59Z)

Just try `make mixbench-ocl-ro` or  `make mixbench-ocl-alt` to build the opencl only benchmarks.
Also, uncomment the 3rd line in Makefile in case the header/library path cannot be found.

---

### 评论 #5 — chriselrod (2017-11-27T19:43:25Z)

I could open a separate issue if this doesn't have enough overlap.
Although I think it's related and may add to the issue. I'm on Ubuntu 16.04, 1950x, and Vega 64.

I tried ArrayFire's test suite, and experienced issues which I reported below:
https://groups.google.com/forum/#!topic/arrayfire-users/SupCI8sTcdM
My problems were:

- A lot of segfaults on OpenCL tests for linear algebra functions, especially factorizations and inversion.
- OpenCL was often well over 6x slower than the CPU. I could rerun tests to post all the timings here.

In the ArrayFire google group, Pavan said:

> Arrayfire passes tests on a varied set of opencl platforms. In my experience if there's tests failing the issues are in the opencl driver. Especially something that's as untested as rocm + Vega.

I didn't immediately comment here because I'm not planning on using ArrayFire, and these matrix operations are also available here: https://github.com/ROCmSoftwarePlatform/hipeigen
I'll try running hipeigen tests tonight.
I'll also try writing a few kernels over the next few weeks and seeing how they perform.

---

### 评论 #6 — gstoner (2017-11-28T00:40:26Z)

It is really capable of lot more, we have tuned libraries now for ROCm 1.7 

<img width="1345" alt="screen shot 2017-11-17 at 8 44 41 am" src="https://user-images.githubusercontent.com/4129721/33296583-ffd4fef0-d3a1-11e7-9e67-b7d9b063a427.png">

@chriselrod Most Likely there needs some library level tuning in Arrayfire. 

I will look at the applications since it not what we have been seeing. 



---

### 评论 #7 — briansp2020 (2017-11-28T00:48:55Z)

@gstoner Will AMD release videos of SC17 presentations? I'm interested in Xilinx stuff and TensorFlow.

---

### 评论 #8 — Srinivasuluch (2017-11-30T15:29:57Z)

Hello rico666,

Can you check whether your workload is correct i.e "./cl-demo 1000000 10" ?
On AMD: You tried "./cl-demo 10 1000000" 
On Nvidia :  i guess, you tried "./cl-demo 1000000 10"

The arg1 & arg2 are misplaced which leads to wrong results.


---

### 评论 #9 — jamilbk (2017-11-30T15:40:49Z)

@Srinivasuluch is right -- I get about 60 GB/s on my Vega FE for this test on ROCm 1.6.4:

```shell
jamil@fridge:~/tmp/opencl-experiments/tools-master (master=) % ./cl-demo 100000 10
Choose platform:
[0] Advanced Micro Devices, Inc.
Enter choice: 
Choose device:
[0] gfx900
[1] gfx900
[2] gfx900
[3] gfx900
Enter choice: 3
---------------------------------------------------------------------
NAME: gfx900
VENDOR: Advanced Micro Devices, Inc.
PROFILE: FULL_PROFILE
VERSION: OpenCL 1.2 
EXTENSIONS: cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 
DRIVER_VERSION: 1.1 (HSA,LC)

Type: GPU 
EXECUTION_CAPABILITIES: Kernel 
GLOBAL_MEM_CACHE_TYPE: Read-Write (2)
CL_DEVICE_LOCAL_MEM_TYPE: Local (1)
SINGLE_FP_CONFIG: 0xbf
QUEUE_PROPERTIES: 0x2

VENDOR_ID: 4098
MAX_COMPUTE_UNITS: 64
MAX_WORK_ITEM_DIMENSIONS: 3
MAX_WORK_GROUP_SIZE: 256
PREFERRED_VECTOR_WIDTH_CHAR: 4
PREFERRED_VECTOR_WIDTH_SHORT: 2
PREFERRED_VECTOR_WIDTH_INT: 1
PREFERRED_VECTOR_WIDTH_LONG: 1
PREFERRED_VECTOR_WIDTH_FLOAT: 1
PREFERRED_VECTOR_WIDTH_DOUBLE: 1
MAX_CLOCK_FREQUENCY: 1600
ADDRESS_BITS: 64
MAX_MEM_ALLOC_SIZE: 14588628172
IMAGE_SUPPORT: 1
MAX_READ_IMAGE_ARGS: 128
MAX_WRITE_IMAGE_ARGS: 8
IMAGE2D_MAX_WIDTH: 16384
IMAGE2D_MAX_HEIGHT: 16384
IMAGE3D_MAX_WIDTH: 2048
IMAGE3D_MAX_HEIGHT: 2048
IMAGE3D_MAX_DEPTH: 2048
MAX_SAMPLERS: 26723
MAX_PARAMETER_SIZE: 1024
MEM_BASE_ADDR_ALIGN: 1024
MIN_DATA_TYPE_ALIGN_SIZE: 128
GLOBAL_MEM_CACHELINE_SIZE: 64
GLOBAL_MEM_CACHE_SIZE: 16384
GLOBAL_MEM_SIZE: 17163091968
MAX_CONSTANT_BUFFER_SIZE: 14588628172
MAX_CONSTANT_ARGS: 8
LOCAL_MEM_SIZE: 65536
ERROR_CORRECTION_SUPPORT: 0
PROFILING_TIMER_RESOLUTION: 1
ENDIAN_LITTLE: 1
AVAILABLE: 1
COMPILER_AVAILABLE: 1
MAX_WORK_GROUP_SIZES: 1024 1024 1024 
---------------------------------------------------------------------
*** Kernel compilation resulted in non-empty log message.
*** Set environment variable CL_HELPER_PRINT_COMPILER_OUTPUT=1 to see more.
*** NOTE: this may include compiler warnings and other important messages
***   about your code.
*** Set CL_HELPER_NO_COMPILER_OUTPUT_NAG=1 to disable this message.
0.000020 s
60.715840 GB/s
GOOD
```

Still not the 170 GB/s claimed for a 1080ti, but at least it's a sign nothing is drastically wrong.



---

### 评论 #10 — jamilbk (2017-11-30T15:45:39Z)

And FWIW, I happen to have another box with a 1080ti in it for testing, and I get about 111 GB/s for that, not 170 GB/s:

```shell
jamil@cooler:~/tmp/opencl-experiments/tools-master (master=) % ./cl-demo 100000 10
./cl-demo: /usr/local/cuda-8.0/lib64/libOpenCL.so.1: no version information available (required by ./cl-demo)
Choose platform:
[0] NVIDIA Corporation
Enter choice: 
Choose device:
[0] GeForce GTX 1080 Ti
Enter choice: 
---------------------------------------------------------------------
NAME: GeForce GTX 1080 Ti
VENDOR: NVIDIA Corporation
PROFILE: FULL_PROFILE
VERSION: OpenCL 1.2 CUDA
EXTENSIONS: cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_
local_int32_extended_atomics cl_khr_fp64 cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing cl_nv_compiler_option
s cl_nv_device_attribute_query cl_nv_pragma_unroll cl_nv_copy_opts cl_nv_create_buffer
DRIVER_VERSION: 384.90

Type: GPU 
EXECUTION_CAPABILITIES: Kernel 
GLOBAL_MEM_CACHE_TYPE: Read-Write (2)
CL_DEVICE_LOCAL_MEM_TYPE: Local (1)
SINGLE_FP_CONFIG: 0xbf
QUEUE_PROPERTIES: 0x3

VENDOR_ID: 4318
MAX_COMPUTE_UNITS: 28
MAX_WORK_ITEM_DIMENSIONS: 3
MAX_WORK_GROUP_SIZE: 1024
PREFERRED_VECTOR_WIDTH_CHAR: 1
PREFERRED_VECTOR_WIDTH_SHORT: 1
PREFERRED_VECTOR_WIDTH_INT: 1
PREFERRED_VECTOR_WIDTH_LONG: 1
PREFERRED_VECTOR_WIDTH_FLOAT: 1
PREFERRED_VECTOR_WIDTH_DOUBLE: 1
MAX_CLOCK_FREQUENCY: 1582
ADDRESS_BITS: 64
MAX_MEM_ALLOC_SIZE: 2928771072
IMAGE_SUPPORT: 1
MAX_READ_IMAGE_ARGS: 256
MAX_WRITE_IMAGE_ARGS: 16
IMAGE2D_MAX_WIDTH: 16384
IMAGE2D_MAX_HEIGHT: 32768
IMAGE3D_MAX_WIDTH: 16384
IMAGE3D_MAX_HEIGHT: 16384
IMAGE3D_MAX_DEPTH: 16384
MAX_SAMPLERS: 32
MAX_PARAMETER_SIZE: 4352
MEM_BASE_ADDR_ALIGN: 4096
MIN_DATA_TYPE_ALIGN_SIZE: 128
GLOBAL_MEM_CACHELINE_SIZE: 128
GLOBAL_MEM_CACHE_SIZE: 458752
GLOBAL_MEM_SIZE: 11715084288
MAX_CONSTANT_BUFFER_SIZE: 65536
MAX_CONSTANT_ARGS: 9
LOCAL_MEM_SIZE: 49152
ERROR_CORRECTION_SUPPORT: 0
PROFILING_TIMER_RESOLUTION: 1000
ENDIAN_LITTLE: 1
AVAILABLE: 1
COMPILER_AVAILABLE: 1
MAX_WORK_GROUP_SIZES: 1024 1024 64 
---------------------------------------------------------------------
*** Kernel compilation resulted in non-empty log message.
*** Set environment variable CL_HELPER_PRINT_COMPILER_OUTPUT=1 to see more.
*** NOTE: this may include compiler warnings and other important messages
***   about your code.
*** Set CL_HELPER_NO_COMPILER_OUTPUT_NAG=1 to disable this message.
0.000011 s
111.822426 GB/s
GOOD
```

---

### 评论 #11 — gstoner (2017-11-30T17:29:49Z)

@rico666 

Ok we found there were number of issues   The app  does not use the correct Wave size for AMD GPU's 

Also, we need the local size to be 64. Apply the following change to cl-demo.c:
 
diff --git a/tools-master/cl-demo.c b/tools-master/cl-demo.c
index f57bee0..522744e 100644
--- a/tools-master/cl-demo.c
+++ b/tools-master/cl-demo.c
@@ -85,7 +85,7 @@ int main(int argc, char **argv)
   for (int trip = 0; trip < ntrips; ++trip)
   {
     SET_4_KERNEL_ARGS(knl, buf_a, buf_b, buf_c, n);
-    size_t ldim[] = { 32 };
**+    size_t ldim[] = { 64 };**
     size_t gdim[] = { ((n + ldim[0] - 1)/ldim[0])*ldim[0] };
     CALL_CL_GUARDED(clEnqueueNDRangeKernel,
         (queue, knl,

Prior to this change we saw 

./cl-demo 1048576 10000
0.000096 s
130.862762 GB/s


We did see make file was not compiling with optimization  
build cl-demo with -O3 (gcc -O3  -std=gnu99 -ocl-demo cl-demo.c cl-helper.c -lOpenCL), the Makefile does not set the optimization flag.

---

### 评论 #12 — rico666 (2017-11-30T18:18:05Z)

I can confirm a few things:

@Srinivasuluch I can confirm that swapping the params yields ~100+ GB/s with my Vega64s - which probably solves the greatest mystery.

I tried -O3 in the Makefile, but there are no differences in speed. I'd assume the host application is a very thin shell so optimizing it has no effect.

I will re-bench and report the 1080Ti results to make sure I was not spreading any false facts/exaggerating. Not sure how much the system speed plays a role (7820X + 2 x 1080Ti is the other reference system)

Using  ./cl-demo 1048576 10000 I get very consistent 143.15 GB/s for both Vega64s

---

### 评论 #13 — rico666 (2017-11-30T18:24:56Z)

Setting size_t ldim[] = { 64 }; I get

183 GB/s with ./cl-demo 1000000 10
260 GB/s, with ./cl-demo 1048576 10000

which looks very good, but I have to perform the same changes on the Nvidia reference system.




---

### 评论 #14 — rico666 (2017-11-30T21:17:50Z)

on the Nvidia 1080Ti sys:
185 GB/s with ./cl-demo 1000000 10   (ldim = 32)
254 GB/s with ./cl-demo 1000000 10   (ldim = 64)
360 GB/s with ./cl-demo 1048576 10000   (ldim = 64)

Ok. The biggest performance difference (due to swapping the params of cl-demo) is my bad.  I think the remaining difference in performance may be due to relatively new support of vega64 by ROCm 1.6 - probably 1.7 will be better there. 

I think the ticket can be closed. I did mention another application (mine) that gives me a hard time on Vega64, but I think it's better if I open a new ticket focusing on that and giving more details.

---
