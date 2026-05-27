# ROCm many times slower than Clover  (on Raven Ridge and RX 580)

> **Issue #625**
> **状态**: closed
> **创建时间**: 2018-11-26T12:33:16Z
> **更新时间**: 2021-01-07T10:29:42Z
> **关闭时间**: 2021-01-07T10:29:42Z
> **作者**: vsavkin2018
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/625

## 描述

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

---

## 评论 (10 条)

### 评论 #1 — vsavkin2018 (2018-11-27T15:26:49Z)

Here are results from RX580 4Gb:

$ python distm-d.py 
Input  bytes: 48000000
Output bytes: 144000000
Choose platform:
[0] <pyopencl.Platform 'AMD Accelerated Parallel Processing' at 0x7ff192340df0>
[1] <pyopencl.Platform 'Clover' at 0x7ff189a70180>
Choice [0]:
Set the environment variable PYOPENCL_CTX='' to avoid being asked again.
CL 0 time= 5.09001994133
CPU time= 28.7973811626
difference 0:  3.29079960011e-05
$ python distm-d.py 
Input  bytes: 48000000
Output bytes: 144000000
Choose platform:
[0] <pyopencl.Platform 'AMD Accelerated Parallel Processing' at 0x7f5a08947df0>
[1] <pyopencl.Platform 'Clover' at 0x7f5a00077180>
Choice [0]:1
Set the environment variable PYOPENCL_CTX='1' to avoid being asked again.
CL 0 time= 1.71260595322
CPU time= 29.076002121
difference 0:  3.26281746084e-05

So it's still 3 times slower than Clover.
Another thing is I haven't managed to run OpenCL on dual-GPU configuration (interated + RX 580) - clinfo kept getting Segmentation faults - is it expected?

This is clinfo output after disabling integrated GPU:
```Number of platforms:				 2
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
  Board name:					 Ellesmere [Radeon RX 470/480]
  Device Topology:				 PCI[ B#1, D#0, F#0 ]
  Max compute units:				 36
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
  Max clock frequency:				 1340Mhz
  Address bits:					 64
  Max memory allocation:			 3650722201
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26591
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 4294967296
  Constant buffer size:				 3650722201
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 3650722201
  Max global variable size:			 3650722201
  Max global variable preferred total size:	 4294967296
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
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
  Platform ID:					 0x7fab7c2b6df0
  Name:						 gfx803
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
  Max compute units:				 36
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
  Max clock frequency:				 1340Mhz
  Address bits:					 64
  Max memory allocation:			 3216061440
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
  Global memory size:				 4294967296
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
  Platform ID:					 0x7fab76d6d180
  Name:						 Radeon RX 580 Series (POLARIS10, DRM 3.27.0, 4.19.2, LLVM 6.0.0)
  Vendor:					 AMD
  Device OpenCL C version:			 OpenCL C 1.1 
  Driver version:				 18.1.9
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.1 Mesa 18.1.9
  Extensions:					 cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_fp16



```

---

### 评论 #2 — jlgreathouse (2018-11-27T18:15:32Z)

I don't have a system available to test this on at the moment, but to answer one of your questions: integrated GPU + discrete GPU setups are currently known not to work at this time (ROCm 1.9.2).

---

### 评论 #3 — 3D-360 (2018-11-27T19:24:39Z)

> to answer one of your questions: integrated GPU + discrete GPU setups are currently known not to work at this time (ROCm 1.9.2).

I have just built a Gigabyte AB350M desktop with a Ryzen 2400G APU and Vega56 graphics card running Ubuntu18.04 and ROCm.
Right now clinfo and rocminfo do not see the APU, but they do see the Vega56 card.
Are you saying that if I remove the Vega56, then clinfo & rocminfo will report the APU?

---

### 评论 #4 — jlgreathouse (2018-11-27T19:33:38Z)

It will likely depend on your BIOS, for a few reasons:

- If you have your integrated GPU disabled in your BIOS, then you can use a Raven Ridge APU as the host CPU for a dGPU. You will not see the iGPU in Linux or in any of the ROCm tools. Some BIOSs will disable your iGPU if you set PCIe VGA as your primary graphics device and have a dGPU installed. Others will allow you explicitly enable/disable the iGPU.
- If your BIOS does not have a proper CRAT table to describe the APU, then your iGPU will not currently be detected by the ROCm software and thus only your dGPU will work.

If your BIOS does not have a proper CRAT table, then removing your dGPU will not allow ROCm to work with your APU's iGPU.

If your BIOS does have a proper CRAT table and your iGPU is enabled, then removing your dGPU should allow ROCm to work with your APU's iGPU. As of ROCm 1.9, HCC and HIP do not yet work with these iGPUs.

If your BIOS does have a proper CRAT table and your iGPU is enabled, but you also have a dGPU installed, I believe that ROCM software will crash. This is because the combination of using both iGPU + dGPU does not yet work in ROCm.

---

### 评论 #5 — 3D-360 (2018-11-27T22:39:35Z)

> the combination of using both iGPU + dGPU does not yet work in ROCm.

OK, I removed the dGP, and now clinfo &  rocminfo see the APU!!!!!

Here are my conclusions concerning the Gigabyte AB350M-Gaming 3 motherboard
 with Ryzen 2400G and BIOS version 23 running Ubuntu 18.04.1 & kernel 4.19.4:

   1) The AB350M mobo with BIOS 23 works with ROCm!
   2) Because the AB350M works with ROCm, this board must have a good CRAT
   3) As you said about ROCm 1.9.2: clinfo and rocminfo do NOT work with both iGPU and dGPU.
       The system does boot Ubuntu 18.04, but clinfo & rocminfo segfault.
   4) Because ROCm does not fully support APUs, HIP & HCC do not work yet

So I say go get yourself this mobo & start testing ROCm & the 2400G<g>. 

There is one little gotcha with this motherboard.  In order to upgrade the BIOS from 22 to 23, I had to install a non-APU Ryzen.  The 2400G is too new for BIOS 22, so I had to swap in an older Ryzen to upgrade the BIOS.  After the BIOS upgrade the 2400G worked fine.  Maybe Gigabyte will start shipping boards with the newer BIOS soon.


---

### 评论 #6 — vsavkin2018 (2018-11-28T09:26:18Z)

I found the reason for speed differences in this case. It's workgroup size - it is automatically chosen (code contains None), and ROCm chooses (256, 1) while Clover - (16,16). After changing this parameter to (16,16) or (8,8) I got very similar execution speed from both engines.

However, I plan to test 1D case later today or tomorrow - I got performance gap in that case too, and I think it cannot be explained by workgroup size alone.

---

### 评论 #7 — vsavkin2018 (2018-11-28T16:19:24Z)

So, in 1D case ROCm is still 30% slower than Clover on simple linear algebra problem.

OpenCL kernels here (file kernel2.cl):
```
__kernel void dist2(
    const int D, const int Nb, const int m,
    __global const float *M_g, __global const float *xm_g, 
    const int res_ofs, __global float *res_g)
{
  int gid = get_global_id(0);
  if (gid>=Nb) { return; }
  float sum = 0.0f, c = 0.0f;
  __global const float *our_x = xm_g + D*m;
  __global const float *our_M = M_g + D*gid;
  int ii, i;

  for (i=0, ii=0; i<=D-8;  ii++, i+=8) {
    float8 k = vload8(ii, our_M) - vload8(ii, our_x);
    float y, t;
#define onestep(I) y=mad(k.I,k.I,c); t=sum+y; c=y-(t-sum); sum=t;
    onestep(s0);
    onestep(s1);
    onestep(s2);
    onestep(s3);
    onestep(s4);
    onestep(s5);
    onestep(s6);
    onestep(s7);
  }

  for (; i<D;  i++) {
    float k = our_M[i] - our_x[i];
    float y = mad(k, k, c);
    float t = sum + y;
    c = y + (sum - t);
    sum = t;
  }
  res_g[res_ofs+gid] = sum;
}

__kernel void distt(
    const int D, const int Nb, const int m,
    __global const float *Mt_g, __global const float *xm_g, 
    const int res_ofs, __global float *res_g)
{
  int gid = get_global_id(0);
  if (gid>=Nb) { return; }
  float sum = 0.0f, c = 0.0f;
  int xm_ofs = D*m;
  for (int i=0; i<D;  i++) {
    float k = Mt_g[i*Nb+gid] - xm_g[xm_ofs+i];
    float y = mad(k, k, c);
    float t = sum + y;
    c = y + (sum - t); 
    sum = t;
  }
  res_g[res_ofs+gid] = sum;
}

/* __kernel void testcpy(
    const int D, const int N,
    __global const float *M_g, __global float *T_g)
{
  int gid = get_global_id(0);
  T_g[gid] = M_g[gid];
} */

```

and python code here (file cl2.py):
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import sys
from time import time

D=260
N=500000
Nb=65536
M=25

Nbufsize = min(N, Nb)


M_np = np.random.rand(N, D).astype(np.float32)
xm_np = np.random.rand(M, D).astype(np.float32)

M_g_sz = M_np[:Nbufsize].nbytes
print("M_g_sz", M_g_sz)

resm_np = np.empty((M, N)).astype(np.float32)

#print("M_np: ", M_np)
#print("x_np: ", x_np)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
M_g = cl.Buffer(ctx, mf.READ_ONLY | mf.HOST_WRITE_ONLY, size = M_np[:Nbufsize].nbytes)
xm_g = cl.Buffer(ctx, mf.READ_ONLY | mf.HOST_WRITE_ONLY, size = xm_np.nbytes)
res_g = cl.Buffer(ctx, mf.WRITE_ONLY | mf.HOST_READ_ONLY, size = resm_np[0].nbytes)

prg = cl.Program(ctx, open("kernel2.cl").read()).build()


t1 = time()
cl.enqueue_copy(queue, xm_g, xm_np)
for m in range(M):
    res_ofs = 0
    while res_ofs < N:
	res_next = min(res_ofs+Nb, N)
	cl.enqueue_copy(queue, M_g, M_np[res_ofs:res_next])
	#print("enqueue", "%d:%d"%(res_ofs, res_next))
        N1 = res_next-res_ofs
	prg.dist2(queue, ((N1+255)& ~0xff,), (256,), np.int32(D), np.int32(N1), 
	    np.int32(m),
	    M_g, xm_g, 
	    np.int32(res_ofs),res_g)
	res_ofs = res_next
    #print("got m:", m)
    cl.enqueue_copy(queue, resm_np[m], res_g)
    queue.finish()
    #print("resm_np[m]:", resm_np[m])

t2 = time()

print("CL 0 time=",t2-t1)


res1m_np = np.empty((M, N)).astype(np.float32)
t1 = time()
MTC = {}
for m in range(M):
    res_ofs = 0
    while res_ofs < N:
	res_next = min(res_ofs+Nb, N)
	if MTC.has_key(res_ofs):
	    mtc = MTC[res_ofs]
	else:
	    mtc = M_np[res_ofs:res_next].transpose().copy()
	    MTC[res_ofs] = mtc
	cl.enqueue_copy(queue, M_g, mtc)
        N1 = res_next-res_ofs
	prg.distt(queue, ((N1+255)& ~0xff,), (256,), np.int32(D), np.int32(N1), 
	    np.int32(m),
	    M_g, xm_g, 
	    np.int32(res_ofs),res_g)
	res_ofs = res_next
    cl.enqueue_copy(queue, res1m_np[m], res_g)
    queue.finish()

t2 = time()
  
  
#print("CL T: ", res1m_np)
print("CL T time=",t2-t1)

M_g.release()

resm_cpu = np.empty((M, N)).astype(np.float32);
t1 = time()
for m in range(M):
    for i in range(N):
	    k = (M_np[i] - xm_np[m]).astype(np.float64) 
	    resm_cpu[m, i] = np.dot(k, k)
t2 = time()

#print("CPU: ", resm_cpu)
print("CPU time=",t2-t1)

print("difference 0: ",
    np.fabs(resm_cpu-resm_np).max(), 
    np.fabs(resm_cpu-resm_np).mean())
print("difference t: ",
    np.fabs(resm_cpu-res1m_np).max(),
    np.fabs(resm_cpu-res1m_np).mean())
```

The task is for each of M vectors of dimension D to find its euclidian distance to each of N another D-dimensioned vectors. To work around small allocation size on some devices, N vectors are divided into chunks up to Nb in size. I have two kernels that differ in layout of input data in memory (normal order and transposed).
This is the output on RX 580:

$ python cl2.py 
M_g_sz 68157440
Choose platform:
[0] <pyopencl.Platform 'AMD Accelerated Parallel Processing' at 0x7fd16223fdf0>
[1] <pyopencl.Platform 'Clover' at 0x7fd1593b5180>
Choice [0]:1
Set the environment variable PYOPENCL_CTX='1' to avoid being asked again.
CL 0 time= 2.97138094902
CL T time= 3.211602211
CPU time= 32.364315033
difference 0:  3.8147e-06 1.15088e-07
difference t:  3.8147e-06 1.15088e-07
vsavkin@ryzen:~/tmp/t$ python cl2.py 
M_g_sz 68157440
Choose platform:
[0] <pyopencl.Platform 'AMD Accelerated Parallel Processing' at 0x7f358252fdf0>
[1] <pyopencl.Platform 'Clover' at 0x7f35796a5180>
Choice [0]:0
Set the environment variable PYOPENCL_CTX='0' to avoid being asked again.
CL 0 time= 3.86957788467
CL T time= 4.05169892311
CPU time= 32.3760340214
difference 0:  3.8147e-06 1.14635e-07
difference t:  3.8147e-06 1.14635e-07

ROCm is about 30% slower in both cases.

---

### 评论 #8 — emerth (2018-12-21T19:08:50Z)

@vsavkin2018 
Sorry to butt in with somewhat off topic...

Do you have this code executing on the Raven Ridge GPU, or are you using the Raven Ridge solely as a CPU?



---

### 评论 #9 — vsavkin2018 (2019-03-18T16:03:12Z)

I had to disable integrated GPU to use ROCm, so only CPU part is used.
Just have checked with rocm 2.2: after enabling IGD in BIOS, rocminfo no longer crashes, but still no ROCm platform in clinfo output.

---

### 评论 #10 — ROCmSupport (2021-01-07T10:29:42Z)

Hi @vsavkin2018 
The mentioned cards are not officially supported.
Thank you.

---
