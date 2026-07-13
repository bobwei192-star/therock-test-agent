# ROCm many times slower than Clover  (on Raven Ridge and RX 580)

- **Issue #:** 625
- **State:** closed
- **Created:** 2018-11-26T12:33:16Z
- **Updated:** 2021-01-07T10:29:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/625

I have just started to look at ROCm. My system is Debian Stretch with Linux kernel 4.19.2 built from source with make-kpkg, ROCm 1.9.307 (?) from repo "http://repo.radeon.com/rocm/apt/debian/ xenial main", Mesa 18.1.9-1~bpo9+1 from debian-backports, CPU being Ryzen 5 2400G.

During testing I noticed very poor performance on some kernels. To isolate this problem, I wrote a very naive implementation of dot-product computation (see code below). It takes N vectors of dimension D and computes NxN matrix of scalar products for each pair of vectors using Kahan summation, then it compares a result with np.dot (double precision used for numpy CPU computations).

This is the output I got for D=2000 and N=6000:
$ python distm-d.py 
Input  bytes: 48000000
Output bytes: 144000000
Choose platform:
[0] <pyopencl.Platform 'AMD Accelerated Parallel Processing' at 0x7f34adb54df0>
[1] <pyopencl.Platform 'Clover' at 0x7f34a5284180>
Choice [0]:
Set the environment variable PYOPENCL_CTX='' to avoid being asked again.
CL 0 time= 64.8843910694
CPU time= 29.4383089542
difference 0:  3.20791181139e-05
$ python distm-d.py 
Input  bytes: 48000000
Output bytes: 144000000
Choose platform:
[0] <pyopencl.Platform 'AMD Accelerated Parallel Processing' at 0x7fbcb49c7df0>
[1] <pyopencl.Platform 'Clover' at 0x7fbcac0f7180>
Choice [0]:1
Set the environment variable PYOPENCL_CTX='1' to avoid being asked again.
CL 0 time= 5.95208716393
CPU time= 29.8313188553
difference 0:  3.18529055221e-05

So, ROCm is more than 10 times slower than Mesa/Clover, and slower than numpy single-threaded code.
I might  get an RX 580 card for testing on the same platform in a few days, will return with an update.

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import sys
from time import time

D=2000
N=6000


M_np = np.random.rand(N, D).astype(np.float32)
res_np = np.empty((N, N)).astype(np.float32)
print("Input  bytes:", M_np.nbytes)
print("Output bytes:", res_np.nbytes)


ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
M_g = cl.Buffer(ctx, mf.READ_ONLY, size = M_np.nbytes)
res_g = cl.Buffer(ctx, mf.READ_WRITE, size = res_np.nbytes)

prg = cl.Program(ctx, """
__kernel void distm(
    const int N, const int D,
    __global const float *M_g,
    __global float *res_g)
{
    int x = get_global_id(0);
    int y = get_global_id(1);
    if ((x>=N) || (y>=N)) { return; }
    float sum = 0.0f, c = 0.0f;
    for (int i=0; i<D; i++) {
        float z = mad(M_g[x*D+i], M_g[y*D+i], -c);
        float t = sum+z;
        c = (t-sum) - z;
        sum = t;
    }
    res_g[y*N+x] = sum;
}

""").build()


t1 = time()
cl.enqueue_copy(queue, M_g, M_np)
prg.distm(queue, (N,N), None, np.int32(N), np.int32(D), 
	    M_g, res_g) 
cl.enqueue_copy(queue, res_np, res_g)
queue.finish()
t2 = time()

print("CL 0 time=",t2-t1)


M_g.release()
res_g.release()

t1 = time()
Md = M_np.astype(np.float64)
Mt = Md.transpose()
res_cpu = np.dot(Md, Mt)
t2 = time()

print("CPU time=",t2-t1)
print("difference 0: ",np.fabs(res_cpu-res_np).max())
```

And here is /opt/rocm/opencl/bin/x86_64/clinfo output:
```
Number of platforms:				 2
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2679.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.1 Mesa 18.1.9
  Platform Name:				 Clover
  Platform Vendor:				 Mesa
  Platform Extensions:				 cl_khr_icd


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 AMD Ryzen 5 2400G with Radeon Vega Graphics
  Device Topology:				 PCI[ B#6, D#0, F#0 ]
  Max compute units:				 11
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1250Mhz
  Address bits:					 64
  Max memory allocation:			 268435456
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 5597
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 1073741824
  Constant buffer size:				 268435456
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 268435456
  Max global variable size:			 268435456
  Max global variable preferred total size:	 1073741824
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 Yes
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 1
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7fbbbfb1fdf0
  Name:						 gfx902-xnack
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2679.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 


  Platform Name:				 Clover
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Max compute units:				 11
  Max work items dimensions:			 3
    Max work items[0]:				 256
    Max work items[1]:				 256
    Max work items[2]:				 256
  Max work group size:				 256
  Preferred vector width char:			 16
  Preferred vector width short:			 8
  Preferred vector width int:			 4
  Preferred vector width long:			 2
  Preferred vector width float:			 4
  Preferred vector width double:		 2
  Native vector width char:			 16
  Native vector width short:			 8
  Native vector width int:			 4
  Native vector width long:			 2
  Native vector width float:			 4
  Native vector width double:			 2
  Max clock frequency:				 1250Mhz
  Address bits:					 64
  Max memory allocation:			 2409498624
  Image support:				 No
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 32768
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 No
    Round to +ve and infinity:			 No
    IEEE754-2008 fused multiply-add:		 No
  Cache type:					 None
  Cache line size:				 0
  Cache size:					 0
  Global memory size:				 3221225472
  Constant buffer size:				 2147483647
  Max number of constant args:			 16
  Local memory type:				 Scratchpad
  Local memory size:				 32768
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 0
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Platform ID:					 0x7fbbba7f8180
  Name:						 AMD RAVEN (DRM 3.27.0, 4.19.2, LLVM 6.0.0)
  Vendor:					 AMD
  Device OpenCL C version:			 OpenCL C 1.1 
  Driver version:				 18.1.9
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.1 Mesa 18.1.9
  Extensions:					 cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_fp16



```