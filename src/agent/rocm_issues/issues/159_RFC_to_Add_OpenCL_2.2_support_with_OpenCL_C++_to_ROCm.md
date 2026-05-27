# RFC to Add OpenCL 2.2 support with OpenCL C++ to ROCm

> **Issue #159**
> **状态**: closed
> **创建时间**: 2017-07-10T19:31:45Z
> **更新时间**: 2020-11-19T11:57:06Z
> **关闭时间**: 2020-11-18T11:33:52Z
> **作者**: nevion
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/159

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

To support better modularity, composability, really useful constructs such as classes, lambdas, and templates, compile time polymorphism (**very useful for performance gains over C and has a large following in CUDA**), genericity including the use of type traits, and ultimately sophisticated maximum performance focused device-side libraries such as CUB, please support OpenCL C++ in ROCm.

While ROCm already supports multiple families (HCC, OpenMP, HIP, AMP?) offering similar capabilities in separate components, none offer the simultaneous promise of an industry backed standard and a fine level control. HCC/AMP/OpenMP lack finer levels of control (in particular memory related) necessary for the highest performance code. HCC effectively compare to the vendor lock-in CUDA offers, although the project is opensource, and this ultimately islands code, in a sense.  This choice over vendors (or similarly unreliance on a single vendor) is often what drives the choice of developers and project managers to invest in OpenCL.  HIP is the most attractive option of these and essentially CUDA-lite, but not quite in runtime or operations supported and its not clear what it does and doesn't have - which is to say it doesn't follow a standard in earnest.  One more feature OpenCL has on all of these approaches is JIT compilation  - an incredibly powerful option in the right hands [(Watch this GTC video of NVidia's Jitify project for a great overview of the technique and it's importance, which OpenCL made easy from day 1!)](http://on-demand-gtc.gputechconf.com/gtcnew/on-demand-gtc.php?searchByKeyword=jitify&searchItems=&sessionTopic=&sessionEvent=&sessionYear=&sessionFormat=&submit=&select=)


ROCm has the opportunity to be first for widespread conformance and whip the rest of industry into shape.  It is not clear, with the exception of HIP, why someone would choose to invest in the other options over OpenCL C++ when they do not offer the promise of an industry standard and inherent performance from tighter control (gauging HCC and OpenMP as comparable to AMP).

Please keep this ticket open to collect support.

[This slide](http://images.anandtech.com/doci/9039/OCL21_Cpp.png) mentions a birds eye view of the feature, original source is slide 5 from [The 2016 OpenCL state of the union](http://www.iwocl.org/wp-content/uploads/iwocl-2016-opencl-state-union.pdf).  Note this feature was added ala carte to OpenCL 2.1, but more in the family in OpenCL 2.2.




---

## 评论 (37 条)

### 评论 #1 — gstoner (2017-07-10T20:10:06Z)

Note: This is a  Request for Comment (RFC)  on the desire to extend our OpenCL Library and Compiler to be extended to support  OpenCL C++ conforming the 2.2 Specification running on the ROCm platform in addition to the ROCm platforms already enabled two  C++ enabled languages listed bellow.  

On this project, note now that we have open sourced our OpenCL Runtime and Compiler frontend this could be done via community developments.   

Current C++ enabled ROCm Languages 
- HCC a single Source Parallel C++  this compiler will also have OpenMP 4.5/5.0 support for C & C++ 
 -  HCC support classes, lambdas, and templates, and compile time polymorphism it builds on the ISO  C++ 14 and C++ 17 standard.   We are building out Parallel STL library for HCC. 

- HIP which is Static C++ Kernel language with c time api.   Which is similar to the Cuda API.
    - Ports of CUB, Thrust and NCCL are under development will be released this summer. 

---

### 评论 #2 — pszi1ard (2017-07-13T21:00:26Z)

Of those languages listed, OpenCL is the only one that's an open standard. Additionally, there are projects invested in OpenCL many risking technical debt and wasted effort by keeping OpenCL support alive essentially only for AMD GPUs -- a good example being the project I'm involved in (despite the rather low user-interest).

It's a bit worrying that to an RFE requesting that AMD catches up with the standard after an understandable step backward (from OpenCL 2.0), the answer is that the community "could do it". While others could indeed do it, is it likely that it will just organically happen given that as far as I can tell there is very little in terms of OSS community around ROCm? Are there any stakeholders that showed interest to do the work and have made plans or perhaps are already working on it? I think the community would appreciate knowing that continued OpenCL investment is worth it.

Overall, I applaud the efforts to release a fully open GPU compute stack and I'm hoping we'll see soon plans of a path forward to supporting the more recent versions of the OpenCL standard.

---

### 评论 #3 — gstoner (2017-07-13T22:17:55Z)

We moving to opencl 2.1  in a future release. So we have all platforms supported windows  and Linux. Still working on timing.   Note  we are getting more traction on HIP.



---

### 评论 #4 — gstoner (2017-07-13T22:27:58Z)

@pszi1ard  we have not seen any industry traction on c++ version of opencl.  Check Intel, Nvidia, and Apple.

---

### 评论 #5 — nevion (2017-07-13T22:40:42Z)

@gstoner I think that's because compilers for these purposes are hard work and we've had to take what we could get as developers, not because of community disinterest.  The industry support for versions of OpenCL is all over the place, tending towards the 1.2 side - without that being higher, it suggests C++ was never a possibility because of the large technical gap.

---

### 评论 #6 — gstoner (2017-07-13T23:03:36Z)

That is the issue opencl1.2 is the de facto standard.

@nevion it little more then because developing a  compiler is hard, there are business reasons for this.  When I meet with customers in North America is the Open Standard is less important they see CUDA as Industry standard and want a solution to solve their current problem there Developer population is trained on CUDA and they see a limited number of students who know OpenCL coming out of school.  

We have National Labs who only want OpenMP and C++ solution from us who will not use OpenCL. 

In Europe, I see more Open Standard Matter, but even here we have a number of customers who see CUDA like a solution is important to them.  

We have been talking to a lot of companies over the last three years, it really what developer population is comfortable with and we have to have a solution to service these markets, Which is why we made ROCm language Neutral.  You pick what you want.  

Now we will not always track to the latest spec update from Khronos Group since it does not alway make business sense to do so.   

@pszi1ard We support OpenCL 2.0 minus PIPES and Device Enqueue ( Dynamic Parallelism)  on the ROCm stack.  It would be really good to understand what true benefit you are getting from OpenCL 2.0 over OpenCL 1.2 as developer beyond C11 Atomics, Global Address Spaces,  Shared Virtual Memory which is support for OpenCL on ROCm.    

---

### 评论 #7 — gstoner (2017-07-13T23:12:02Z)

Also, HCC follows ISO C++.standard. Built on one of the best implementations with clang,  Which is an industry standard.   For C++ the community we talk too broadly wants us engaged in ISO standards body for our C++ work, not other bodies.



---

### 评论 #8 — boxerab (2017-07-15T02:21:35Z)

@gstoner thanks for this info. I think it would be help to have a roadmap for HIP development, so that developers will feel confident investing time in it. Will it eventually match all of the capabilities of OpenCL 2, for example ? And be cross platform ?  I've been developing OpenCL apps for the past 3 years, but because of nVidia lock-in behaviour, I need another solution for their platform, which is the vast majority of discrete graphics cards at the moment, (hopefully changing soon).  I looked at HIP, but because it is linux only at the moment, I'm afraid I'm going to have to bite the bullet and port my OpenCL code to CUDA.  This is video transcoding, not HPC or Deep Learning, so windows is a critical platform to support.

I realize there is much to do for AMD and limited resources, but I really do need a cross platform solution now, or at least a plan for getting there in the next 6-12 months.  Having a road map would help a lot.






---

### 评论 #9 — gstoner (2017-07-15T03:56:44Z)

HIP has more feature then OpenCL 2.0.  it better maps to ROCr runtime api capabilities,   We will be bring HCC and HIP to Windows, we just need to get it to feature maturity level before we moved it over.  HIP currently also run on NVIDA using there NVCC compiler.



  *   Developers can code in C++ as well as mix host and device C++ code in their source files. HIP C++ code can use templates, lambdas, classes and so on.

  *   HIP provides pointers and host-side pointer arithmetic.
  *   HIP provides device-level control over memory allocation and placement.
  *   HIP offers an offline compilation model.
  *   Cross-lane instructions including shfl, ballot, any, all


Are you asking about GL Interop and Texture Support, these are in development.


http://rocm-developer-tools.github.io/HIP/

Table Comparing Syntax for Different Compute APIs
Term    CUDA    HIP     HC      C++AMP  OpenCL
Device  int deviceId    int deviceId    hc::accelerator concurrency::
accelerator     cl_device
Queue   cudaStream_t    hipStream_t     hc::
accelerator_view        concurrency::
accelerator_view        cl_command_queue
Event   cudaEvent_t     hipEvent_t      hc::
completion_future       concurrency::
completion_future       cl_event
Memory  void *  void *  void *; hc::array; hc::array_view       concurrency::array;
concurrency::array_view cl_mem

        grid    grid    extent  extent  NDRange
        block   block   tile    tile    work-group
        thread  thread  thread  thread  work-item
        warp    warp    wavefront       N/A     sub-group

Thread-
index   threadIdx.x     hipThreadIdx_x  t_idx.local[0]  t_idx.local[0]  get_local_id(0)
Block-
index   blockIdx.x      hipBlockIdx_x   t_idx.tile[0]   t_idx.tile[0]   get_group_id(0)
Block-
dim     blockDim.x      hipBlockDim_x   t_ext.tile_dim[0]       t_idx.tile_dim0 get_local_size(0)
Grid-dim        gridDim.x       hipGridDim_x    t_ext[0]        t_ext[0]        get_global_size(0)

Device Kernel   __global__      __global__      lambda inside hc::
parallel_for_each or [[hc]]     restrict(amp)   __kernel
Device Function __device__      __device__      [[hc]] (detected automatically in many case)    restrict(amp)   Implied in device compilation
Host Function   __host_(default)        __host_ (default)       [[cpu]] (default)       restrict(cpu) (default) Implied in host compilation.
Host + Device Function  __host____device__      __host____device__      [[hc]] [[cpu]]  restrict(amp,cpu)       No equivalent
Kernel Launch   <<< >>> hipLaunchKernel hc::
parallel_for_each       concurrency::
parallel_for_each       clEnqueueNDRangeKernel

Global Memory   __global__      __global__      Unnecessary / Implied   Unnecessary / Implied   __global
Group Memory    __shared__      __shared__      tile_static     tile_static     __local
Constant        __constant__    __constant__    Unnecessary / Implied   Unnecessary / Implied   __constant

        __syncthreads   __syncthreads   tile_static.barrier()   t_idx.barrier() barrier(CLK_LOCAL_MEMFENCE)
Atomic Builtins atomicAdd       atomicAdd       hc::atomic_fetch_add    concurrency::
atomic_fetch_add        atomic_add
Precise Math    cos(f)  cos(f)  hc::
precise_math::cos(f)    concurrency::
precise_math::cos(f)    cos(f)
Fast Math       __cos(f)        __cos(f)        hc::
fast_math::cos(f)       concurrency::
fast_math::cos(f)       native_cos(f)
Vector  float4  float4  hc::
short_vector::float4    concurrency::
graphics::float_4       float4

###Notes

  1.  For HC and C++AMP, assume a captured tiled_ext named "t_ext" and captured extent named "ext". These languages use captured variables to pass information to the kernel rather than using special built-in functions so the exact variable name may vary.
  2.  The indexing functions (starting with thread-index) show the terminology for a 1D grid. Some APIs use reverse order of xyz / 012 indexing for 3D grids.
  3.  HC allows tile dimensions to be specified at runtime while C++AMP requires that tile dimensions be specified at compile-time. Thus hc syntax for tile dims is t_ext.tile_dim[0] while C++AMP is t_ext.tile_dim0.











---

### 评论 #10 — gstoner (2017-07-15T04:24:41Z)

It already in the hcc and hip docs. We are working new online documentation  so it be easier to find.





---

### 评论 #11 — boxerab (2017-07-15T16:02:41Z)

Thanks, Greg. I am more excited about HIP now :)  

---

### 评论 #12 — gstoner (2017-07-15T16:14:10Z)


I put the table at the bottom of this article for now.  

ROCm, Lingua Franca, C++, OpenCL and Python

The open-source ROCm stack offers multiple programming-language choices. The goal is to give you a range of tools to help solve the problem at hand. Here, we describe some of the options and how to choose among them.

HCC: Heterogeneous Compute Compiler

What is the Heterogeneous Compute (HC) API? It’s a C++ dialect with extensions to launch kernels and manage accelerator memory. It closely tracks the evolution of C++ and will incorporate parallelism and concurrency features as the C++ standard does. For example, HC includes early support for the C++17 Parallel STL. At the recent ISO C++ meetings in Kona and Jacksonville, the committee was excited about enabling the language to express all forms of parallelism, including multicore CPU, SIMD and GPU. We’ll be following these developments closely, and you’ll see HC move quickly to include standard C++ capabilities.

The Heterogeneous Compute Compiler (HCC) provides two important benefits:

Ease of development

A full C++ API for managing devices, queues and events
C++ data containers that provide type safety, multidimensional-array indexing and automatic data management
C++ kernel-launch syntax using parallel_for_each plus C++11 lambda functions
A single-source C++ programming environment---the host and source code can be in the same source file and use the same C++ language; templates and classes work naturally across the host/device boundary
HCC generates both host and device code from the same compiler, so it benefits from a consistent view of the source code using the same Clang-based language parser
Full control over the machine

Access AMD scratchpad memories (“LDS”)
Fully control data movement, prefetch and discard
Fully control asynchronous kernel launch and completion
Get device-side dependency resolution for kernel and data commands (without host involvement)
Obtain HSA agents, queues and signals for low-level control of the architecture using the HSA Runtime API
Use direct-to-ISA compilation
When to Use HC

Use HC when you're targeting the AMD ROCm platform: it delivers a single-source, easy-to-program C++ environment without compromising performance or control of the machine.

HIP: Heterogeneous-Computing Interface for Portability

What is Heterogeneous-Computing Interface for Portability (HIP)? It’s a C++ dialect designed to ease conversion of Cuda applications to portable C++ code. It provides a C-style API and a C++ kernel language. The C++ interface can use templates and classes across the host/kernel boundary.

The Hipify tool automates much of the conversion work by performing a source-to-source transformation from Cuda to HIP. HIP code can run on AMD hardware (through the HCC compiler) or Nvidia hardware (through the NVCC compiler) with no performance loss compared with the original Cuda code.

Programmers familiar with other GPGPU languages will find HIP very easy to learn and use. AMD platforms implement this language using the HC dialect described above, providing similar low-level control over the machine.

When to Use HIP

Use HIP when converting Cuda applications to portable C++ and for new projects that require portability between AMD and Nvidia. HIP provides a C++ development language and access to the best development tools on both platforms.

OpenCL™: Open Compute Language

What is OpenCL? It’s a framework for developing programs that can execute across a wide variety of heterogeneous platforms. AMD, Intel and Nvidia GPUs support version 1.2 of the specification, as do x86 CPUs and other devices (including FPGAs and DSPs). OpenCL provides a C run-time API and C99-based kernel language.

When to Use OpenCL

Use OpenCL when you have existing code in that language and when you need portability to multiple platforms and devices. It runs on Windows, Linux and Mac OS, as well as a wide variety of hardware platforms (described above).

Anaconda Python With Numba

What is Anaconda? It’s a modern open-source analytics platform powered by Python. Continuum Analytics, a ROCm platform partner, is the driving force behind it. Anaconda delivers high-performance capabilities including acceleration of HSA APUs, as well as ROCm-enabled discrete GPUs via Numba. It gives superpowers to the people who are changing the world.

Numba

Numba gives you the power to speed up your applications with high-performance functions written directly in Python. Through a few annotations, you can just-in-time compile array-oriented and math-heavy Python code to native machine instructions---offering performance similar to that of C, C++ and Fortran---without having to switch languages or Python interpreters.

Numba works by generating optimized machine code using the LLVM compiler infrastructure at import time, run time or statically (through the included Pycc tool). It supports Python compilation to run on either CPU or GPU hardware and is designed to integrate with Python scientific software stacks, such as NumPy.

When to Use Anaconda

Use Anaconda when you’re handling large-scale data-analytics, scientific and engineering problems that require you to manipulate large data arrays.

Wrap-Up

From a high-level perspective, ROCm delivers a rich set of tools that allow you to choose the best language for your application.

HCC (Heterogeneous Compute Compiler) supports HC dialects
HIP is a run-time library that layers on top of HCC (for AMD ROCm platforms; for Nvidia, it uses the NVCC compiler)
The following will soon offer native compiler support for the GCN ISA:
OpenCL 1.2+
Anaconda (Python) with Numba
All are open-source projects, so you can employ a fully open stack from the language down to the metal. AMD is committed to providing an open ecosystem that gives developers the ability to choose; we are excited about innovating quickly using open source and about interacting closely with our developer community. More to come soon!

---

### 评论 #13 — gstoner (2017-07-15T16:18:52Z)

I hope you're aware of all this documentation for now 

#### AMDGPU LLVM Compiler 

* [Doucmentation for AMDGPU Code Generator in LVVM](http://llvm.org/docs/AMDGPUUsage.html)

#### HCC

* [HCC overview](https://github.com/RadeonOpenCompute/hcc/wiki)
* [How to use HCC and select a GPU device](https://github.com/RadeonOpenCompute/hcc/wiki#how-to-use-hcc)
* [HCC language API documentation](http://scchan.github.io/hcc/)
* [HC API: Moving Beyond C++ AMP for Accelerated GPU Computing](https://github.com/RadeonOpenCompute/hcc/blob/master/doc/markdown/Home.md)
* [HCC Saxpy example](https://gist.github.com/scchan/540d410456e3e2682dbf018d3c179008)

#### HIP

* [HIP porting guide: overview and
  how-to](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/blob/master/docs/markdown/hip_porting_guide.md)
* [HIP terminology comparison with OpenCL, Cuda, C++ AMP and HCC](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/blob/master/docs/markdown/hip_terms.md)
* [HIP run-time API overview and documentation
  (Doxygen)](http://gpuopen-professionalcompute-tools.github.io/HIP/)
* [HIP kernel-language overview](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/blob/master/docs/markdown/hip_kernel_language.md)
* [HIP FAQ](https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/blob/master/docs/markdown/hip_faq.md)

#### GCN ISA, ROCm Object Format, ABI and Assembly Documentation 

* [GCN Architecture overview](https://www.amd.com/Documents/GCN_Architecture_whitepaper.pdf)
* [GCN Architecure crash course by Lala Mah](http://www.slideshare.net/DevCentralAMD/gs4106-the-amd-gcn-architecture-a-crash-course-by-layla-mah)
* [GFX7 GCN ISA Southern Islands manual---Hawaii ]( http://bit.ly/29t5aQP)
* [GFX8  GCN Version 3---Tonga, Fiji and Polaris ](http://amd-dev.wpengine.netdna-cdn.com/wordpress/media/2013/12/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf)
* [AMD GPU-compute application binary interface (ABI) ](https://github.com/RadeonOpenCompute/ROCm-ComputeABI-Doc/blob/master/AMDGPU-ABI.md)
* [Documentation covering helper tools for ROCm GCN LLVM assembler](https://github.com/RadeonOpenCompute/LLVM-AMDGPU-Assembler-Extra/blob/master/README.md)
* [GCN float16](GCN_Float16.html)
* [ROC device library---Open Compute Math Library  intrinsics](https://github.com/RadeonOpenCompute/ROCm-Device-Libs/blob/master/doc/OCML.md)


---

### 评论 #14 — gstoner (2017-07-15T16:32:08Z)

Following with tradition of making this open source program all the documentation online. We are using Sphinx and Read the doc for the documentation. 

The link to the [ROCm Online Documentation](http://rocm-documentation.readthedocs.io/en/latest/index.html) while it under development. 
Where we have [ROCm Github Documentation Source](https://github.com/RadeonOpenCompute/ROCm_Documentation)

---

### 评论 #15 — boxerab (2017-07-15T16:41:45Z)

Thanks, I will RTFM :)  

---

### 评论 #16 — gstoner (2017-07-15T16:47:34Z)

That last link was to show where we going it still under constructions.  The link above from [ROCm Website](rocm.github.io) are the best place away to start


---

### 评论 #17 — boxerab (2017-07-15T17:21:23Z)

Great, thanks.

---

### 评论 #18 — gstoner (2017-07-16T01:08:41Z)

Looks like OpenCL 1.2 getting cemented a little more in the business  Google Rolled out OpenCL 1.2 on Vulkan with Codeplay's help. 
https://github.com/google/clspv
https://github.com/google/clspv/blob/master/docs/OpenCLCOnVulkan.md   OpenCL 1.2 on Vulkan.  

Interesting to see, since I help start Vulkan effort at Khronos group,  pushing in the main proposal we called XGL. 

---

### 评论 #19 — boxerab (2017-07-16T01:14:47Z)

This is very good to see. I've heard rumours that OpenCL will merge into Vulkan. Creating something like Metal, only more powerful, and cross-platform.

---

### 评论 #20 — gstoner (2017-07-16T01:18:12Z)

Looks to be a subset of OpenCL 1.2 

---

### 评论 #21 — boxerab (2017-07-16T01:31:11Z)

Here is the press release:

https://www.codeplay.com/portal/07-14-17-codeplay-release-clspv-an-opencl-tool-for-vulkan-enabled-devices

---

### 评论 #22 — gstoner (2017-07-16T01:32:38Z)

Some notes on the clspv:

Yep.. 

**This is a prototype, with known issues. However, it does compile significant portions of kernels
It uses close to top-of-tree versions of LLVM and Clang as third-party projects - this is not a fork**
It is mainly a set of LLVM module passes. The flow starts with the SPIR code generated from stock Clang, then massages it into SPIR-V for Vulkan
It exercises SPV_KHR_variable_pointers (rev13)

---

### 评论 #23 — jstefanop (2017-07-24T22:04:49Z)

@gstoner have the GCN/NCU Docs for Vegas architecture been release yet? Other than some high level slides and overview, I haven't been able to find any technical documents on Vegas NCU.

---

### 评论 #24 — gstoner (2017-07-25T12:27:22Z)

It not out yet,  it with the legal team for final review.

---

### 评论 #25 — preda (2017-08-21T00:49:24Z)

The VEGA ISA link changed to: http://developer.amd.com/wordpress/media/2013/12/Vega_Shader_ISA_28July2017-1.pdf


---

### 评论 #26 — pszi1ard (2017-10-12T15:13:55Z)

> The VEGA ISA link changed to: http://developer.amd.com/wordpress/media/2013/12/Vega_Shader_ISA_28July2017-1.pdf

Dead link.

---

### 评论 #27 — gstoner (2017-10-13T01:14:12Z)

@pszi1ard  http://rocm-documentation.readthedocs.io/en/latest/GCN_ISA_Manuals/testdocbook.html#testdocbook   You now get the Vega ISA  online here 

---

### 评论 #28 — robbert-harms (2019-04-23T10:19:56Z)

What is the current status of this? I am eager to use ROCm with OpenCL 2.2 for my applications.

---

### 评论 #29 — oscarbg (2019-04-26T02:18:33Z)

+1 

---

### 评论 #30 — SteveBronder (2019-06-22T01:59:43Z)

+1

---

### 评论 #31 — orz-- (2019-09-11T02:34:28Z)

+1

---

### 评论 #32 — Moading (2019-09-11T09:09:14Z)

+1 as HCC is dead. HIP is no industry tandard and might be deprecated tomorrow.
In my opinion OpenCL is the way to go due to portability, especially when Intel enters the GPU market next year.

---

### 评论 #33 — ekondis (2019-09-11T20:57:21Z)

SYCL is also an alternative as a single source C++ programming model for GPUs.

---

### 评论 #34 — ROCmSupport (2020-11-18T11:26:12Z)

Thanks @nevion 
As its very old issue, and no updates for the last 2 years, this issue is going to be closed.
Request to open a new ticket, if you found any.
Thank you.

---

### 评论 #35 — pszi1ard (2020-11-18T14:37:04Z)

Does this mean "#wontfix"?

---

### 评论 #36 — ROCmSupport (2020-11-19T06:08:36Z)

Hi @pszi1ard 
As part of process improvement, we requested you to close very old(>2 years) open ticket.
Request you to open a new ticket, if you still face the same/new problem, where you will get fast updates.
Thank you.

---

### 评论 #37 — mirh (2020-11-19T11:57:05Z)

The bot is kinda badly calibrated. It's true this issue is more than 2 years old, but it's false that no update happened in the last 2 years. 

---
