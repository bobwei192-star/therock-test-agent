# OpenCL performance regression on Gromacs

> **Issue #93**
> **状态**: closed
> **创建时间**: 2017-03-04T00:08:42Z
> **更新时间**: 2020-11-18T11:34:16Z
> **关闭时间**: 2020-11-18T11:34:16Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/93

## 描述

I measure up to 1.5x kernel performance regression with the ROCm 1.4 release compared to AMDGPU-PRO. The application is GROMACS version 2016.2.

---

## 评论 (77 条)

### 评论 #1 — gstoner (2017-03-04T03:50:52Z)

Yes that compiler was not optimized yet like we said when we released the OpenCL developer preview, It was  for functional  testing only.   What you seeing is the compiler is spilling registers and missing few more optimizations which we have been working on.   One of the things we now have Assembler so we push the performance well beyond what you seeing on AMDGPU Pro


  Do you have test you like us run..  We have been testing some of the GROMACS benchmarks

G


On Mar 3, 2017, at 6:08 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


I measure up to 1.5x kernel performance regression with the ROCm 1.4 release compared to AMDGPU-PRO. The application is GROMACS version 2016.2.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuVkxff-g3gXziYR4Hzk95J5_5NwYks5riKuLgaJpZM4MS4y2>.



---

### 评论 #2 — pszi1ard (2017-03-04T14:33:59Z)

Thanks for the feedback. I know the compiler as released in 1.4 was far from optimal. However, for GROMACS after correctness performance is the second most important functionality, so my report is technically concerning an application functionality :)

It would be great if you could include some testing/benchmarks in your internal testing. We have a mall number of hot kernels and quite peculiar application behavior that tends to stress the driver and cause API overhead), so those aspect would be good to get tested and improved if needed. Let me know how would you like to proceed.

---

### 评论 #3 — pszi1ard (2017-03-04T15:40:06Z)

I've had another look at some internal GROMACS profiler counters and there are strong indications that the runtime is using a lot of CPU resources resulting in both increased host-side cost of enqueue and increased interference with work executed on the CPU concurrently with the GPU. Are such issues also known/expected?

---

### 评论 #4 — gstoner (2017-03-04T17:55:40Z)

the base driver team dropped in some last minute changes on 1.4 which we seeing some quirkiness.

This is one of the GROMACS test we are running,    We found a core issue in this 1.4 and Gromacs already  which we working on now.

cd /root/Desktop/ISV/Gromacs-2016/gromacs-2016
export GMX_OCL_FILE_PATH=/usr/local/gromacs/share/gromacs/opencl
cd ~/Gromacs-2016/gromacs-2016/build/bin/rnase_cubic/
../gmx grompp -f pme_verlet.mdp
../gmx mdrun

On Mar 4, 2017, at 9:40 AM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


I've had another look at some internal GROMACS profiler counters and there are strong indications that the runtime is using a lot of CPU resources resulting in both increased host-side cost of enqueue and increased interference with work executed on the CPU concurrently with the GPU. Are such issues also known/expected?

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-284159117>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuceccuI_iNw5bGbD8ONX-EgazA52ks5riYXXgaJpZM4MS4y2>.



---

### 评论 #5 — pszi1ard (2017-03-04T19:32:08Z)

@gstoner Sounds good. The test case you are using is pretty decent, but a bit more coverage of input sizes/use-cases and some command line tweaks to run only the kernels of interest might nor hurt.

Briefly, this is what's of strong interest and I'd recommend tracking (using a at least a few test cases):

* (post-load balancing) Average execution time of the hottest offloaded kernel across _a range of_ input sizes. Bad performance with very small kernels can become showstoppers for strong scaling (hence the emphasis on the range of problem sized), e.g. see [1] where besides getting good peak, the left-hand "tail" is what would be great if improved;
* OpenCL API overhead which, especially at peak performance (< 1 ms/iteration) can be quite significant. What's also a concern is the behavior of the driver overhead under high kernel issue rate and when starved (by application threads) which has been a serious issue in the past, e.g. see [2].

[1] GROMACS 5.1 / 2016 GPU kernel throughput https://drive.google.com/file/d/0B6dQqsegA1FMZk5kNXI4SzVhbzNyT0NackpCY05FNlM1dWNv/view?usp=sharing
[2] API overhead in GROMACS runs on a three fglrx versions. https://drive.google.com/open?id=0B6dQqsegA1FMLTJZb2NRWUlLbHc

Let me know if you need more input and  what other feedback would be useful for you. I'd really like to see the Vega GPUs hit the ground running (hopefully with rocm and also mesa!), but so far software stack issues have been the one thing that has been limiting both development and user adoption.

---

### 评论 #6 — gstoner (2017-03-04T19:38:08Z)

When you did into the core kernel,  what is critical section running on the GPU that you see the most.   Is it GEMM or some other kernel function.    What is the average gpu local memory needed for running real jobs  4GB, 8GB or more?   Also when you do multi-gpu enablement are you looking at library like NCCL on CUDA side now.


On Mar 4, 2017, at 1:32 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> Sounds good. The test case you are using is pretty decent, but a bit more coverage of input sizes/use-cases and some command line tweaks to run only the kernels of interest might nor hurt.

Briefly, this is what's of strong interest and I'd recommend tracking (using a at least a few test cases):

  *   (post-load balancing) Average execution time of the hottest offloaded kernel across a range of input sizes. Bad performance with very small kernels can become showstoppers for strong scaling (hence the emphasis on the range of problem sized), e.g. see [1] where besides getting good peak, the left-hand "tail" is what would be great if improved;
  *   OpenCL API overhead which, especially at peak performance (< 1 ms/iteration) can be quite significant. What's also a concern is the behavior of the driver overhead under high kernel issue rate and when starved (by application threads) which has been a serious issue in the past, e.g. see [2].

[1] GROMACS 5.1 / 2016 GPU kernel throughput https://drive.google.com/file/d/0B6dQqsegA1FMZk5kNXI4SzVhbzNyT0NackpCY05FNlM1dWNv/view?usp=sharing
[2] API overhead in GROMACS runs on a three fglrx versions. https://drive.google.com/open?id=0B6dQqsegA1FMLTJZb2NRWUlLbHc

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-284175198>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubTCWlfqiLaZ2KmJ36AkuQSuDCAJks5ribw5gaJpZM4MS4y2>.



---

### 评论 #7 — pszi1ard (2017-03-04T19:55:40Z)

> When you did into the core kernel,  what is critical section running on the GPU that you see the most.   Is it GEMM or some other kernel function.

If I understand correctly, you're asking about the GPU algorithm that run on the critical path? It's not GEMM, but a pair interaction algorithm (based on neighbor list traversal), but we use our own SIMD-tuned algorithm.

> What is the average gpu local memory needed for running real jobs  4GB, 8GB or more?  

Not sure if you are referring to local or global memory in OpenCL terminology (I assume the latter given the Gigabytes)?

> Also when you do multi-gpu enablement are you looking at library like NCCL on CUDA side now.

No, at the moment all communication is done on the CPU using MPI/shared memory.
We are porting more code to offload to GPUs and I have been looking into CUDA GPUDirect and NCCL, but OpenCL porting will likely lag behind CUDA, so it is unlikely to be important in the next year or so.

---

### 评论 #8 — pszi1ard (2017-03-04T20:07:27Z)

>> What is the average gpu local memory needed for running real jobs 4GB, 8GB or more?
> Not sure if you are referring to local or global memory in OpenCL terminology (I assume the latter given the Gigabytes)?

@gstoner forgot to answer: for typical runs we need <200 Mb, for pretty much all relevant cases <1 Gb. This may increase a little as we're moving to offloading more, but ultimately GROMACS runs in the strong-scaling regime where the performance practical for research is only achieved when the per-node data is very little.


---

### 评论 #9 — gstoner (2017-03-04T20:19:45Z)

Yes,  it should have be dig into
On Mar 4, 2017, at 2:07 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


What is the average gpu local memory needed for running real jobs 4GB, 8GB or more?
Not sure if you are referring to local or global memory in OpenCL terminology (I assume the latter given the Gigabytes)?

@gstoner<https://github.com/gstoner> forgot to answer: for typical runs we need <200 Mb, for pretty much all relevant cases <1 Gb. This may increase a little as we're moving to offloading more, but ultimately GROMACS runs in the strong-scaling regime where the performance practical for research is only achieved when the per-node data is very little.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-284177323>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuRXo0WFErXSFwN8UepMsYrH0PLqIks5ricSAgaJpZM4MS4y2>.



---

### 评论 #10 — pszi1ard (2017-03-04T20:23:54Z)

> Yes,  it should have be dig into

@gstoner Could you clarify?

Also, maybe my above late edit was missed, so let me reiterate it:

Let me know if you need more input and what other feedback would be useful for you. I'd really like to see the Vega GPUs hit the ground running (hopefully with rocm and also mesa!), but so far software stack issues have been the one thing that has been limiting both development and user adoption.



---

### 评论 #11 — gstoner (2017-03-04T20:24:41Z)

What I am looking for is what is the critical section in your kernel.

Greg
On Mar 4, 2017, at 2:23 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


Yes, it should have be dig into

@gstoner<https://github.com/gstoner> Could you clarify?

Also, maybe my above late edit was missed, so let me reiterate it:

Let me know if you need more input and what other feedback would be useful for you. I'd really like to see the Vega GPUs hit the ground running (hopefully with rocm and also mesa!), but so far software stack issues have been the one thing that has been limiting both development and user adoption.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-284178291>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duba3xQB_63eYyMCjcFkHlIOwtIZ6ks5richbgaJpZM4MS4y2>.



---

### 评论 #12 — gstoner (2017-03-04T20:25:36Z)

Critical performance section

greg
On Mar 4, 2017, at 2:23 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


Yes, it should have be dig into

@gstoner<https://github.com/gstoner> Could you clarify?

Also, maybe my above late edit was missed, so let me reiterate it:

Let me know if you need more input and what other feedback would be useful for you. I'd really like to see the Vega GPUs hit the ground running (hopefully with rocm and also mesa!), but so far software stack issues have been the one thing that has been limiting both development and user adoption.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-284178291>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duba3xQB_63eYyMCjcFkHlIOwtIZ6ks5richbgaJpZM4MS4y2>.



---

### 评论 #13 — pszi1ard (2017-03-04T20:35:45Z)

@gstoner The kernel is [here](https://github.com/gromacs/gromacs/blob/master/src/gromacs/mdlib/nbnxn_ocl/nbnxn_ocl_kernel_amd.clh). It implements [a pair-interaction algorithm](http://www.sciencedirect.com/science/article/pii/S2352711015000059#f000015) that's [tuned for SIMD architectures](http://www.sciencedirect.com/science/article/pii/S2352711015000059#f000020).

* Single precision 
* significant amount of 32-bit integer ops
* arithmetically intensive (~15 Flops/byte)
* uses lots of registers
* typically instruction latency-bound on GPUs


---

### 评论 #14 — gstoner (2017-03-04T20:36:33Z)

Thanks.

greg
On Mar 4, 2017, at 2:35 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


The kernel is here<https://github.com/gromacs/gromacs/blob/master/src/gromacs/mdlib/nbnxn_ocl/nbnxn_ocl_kernel_amd.clh>. It implements a pair-interaction algorithm<http://www.sciencedirect.com/science/article/pii/S2352711015000059#f000015> that's tuned for SIMD architectures<http://www.sciencedirect.com/science/article/pii/S2352711015000059#f000020>.

  *   Single precision
  *   significant ampount of 32-bit integer ops
  *   arithmetically intensive (~15 Flops/byte)
  *   uses lots of registers, typically instruction latency-bound. Lots of Integers ops

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-284178980>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYlo9NP_r-y8GSApLjGwtGw0koHhks5ricshgaJpZM4MS4y2>.



---

### 评论 #15 — gstoner (2017-03-04T20:37:59Z)

Do you have FIJI? 

greg

---

### 评论 #16 — pszi1ard (2017-03-04T20:38:04Z)

PS: the kernel loves lane shuffle for reduction which we're greatly missing on AMD hardware!

---

### 评论 #17 — pszi1ard (2017-03-04T20:40:28Z)

We have an R9 Nano for development. (BTW performance compared to the green guys was on the PDF linked earlier: https://drive.google.com/file/d/0B6dQqsegA1FMZk5kNXI4SzVhbzNyT0NackpCY05FNlM1dWNv/view?usp=sharing)

---

### 评论 #18 — gstoner (2017-03-04T20:40:49Z)

Did you see this article AMD GCN Assembly: Cross-Lane Operations  http://gpuopen.com/amd-gcn-assembly-cross-lane-operations/

We can do this now inside the new compiler we had lot of hardware that was masked by the old compiler 

Posted on August 10, 2016 by Ben Sander
 Boltzmann, GCN, GPU, HCC, HIP, HSA
Cross-lane operations are an efficient way to share data between wavefront lanes. This article covers in detail the cross-lane features that GCN3 offers.  I’d like to thank Ilya Perminov of Luxsoft for co-authoring this blog post.

Terminology
We’ll be optimizing communication between work-items, so it is important to start with a consistent set of terminology:

The basic execution unit of an AMD GCN GPU is called a wavefront, which is basically a SIMD vector.
A wavefront comprises 64 parallel elements, called lanes, that each represent a separate work item.
A lane index is a coordinate of the work item in a wavefront, with a value ranging from 0 to 63.
Because a wavefront is the lowest level that flow control can affect, groups of 64 work items execute in lockstep. The actual GCN hardware implements 16-wide SIMD, so wavefronts decompose into groups of 16 lanes called wavefront rows that are executed on 4 consecutive cycles.
This hardware organization affects cross-lane operations – some operations work at the wavefront level and some only at the row level. We’ll discuss the details below.

Why Not Just Use LDS?
Local data share (LDS) was introduced exactly for that reason: to allow efficient communication and data sharing between threads in the same compute unit. LDS is a low-latency RAM physically located on chip in each compute unit (CU). Still, most actual compute instructions operate on data in registers. Now, let’s look at the peak-performance numbers. The memory bandwidth of AMD’s Radeon R9 Fury X is an amazing 512 GB/s. Its LDS implementation has a total memory bandwidth of (1,050 GHz) * (64 CUs) * (32 LDS banks) * (4 bytes per read per lane) = 8.6 TB/s. Just imagine reading all the content of a high-capacity 8 TB HDD in one second! Moreover, the LDS latency is an order of magnitude less than that of global memory, helping feed all 4,096 insatiable ALUs. LDS is only available on a workgroup level.

At the same time, the register bandwidth is (1,050 GHz) * (64 CUs) * (64 lanes) * (12 bytes per lane) = 51.6 TB/s. That’s another order of magnitude, so communication between threads is much slower than just crunching data in the thread registers.

But can we do better by sharing? The answer is yes, if we further reduce our scope from a workgroup to a single wavefront.

---

### 评论 #19 — pszi1ard (2017-03-04T20:44:57Z)

> Did you see this article AMD GCN Assembly: Cross-Lane Operations http://gpuopen.com/amd-gcn-assembly-cross-lane-operations/

I have seen it, but I did not think it was possible to use in-line ASM with OpenCL. Or is there some other way to implement it in OpenCL?

> We can do this now inside the new compiler we had lot of hardware that was masked by the old compiler

So how and when will you expose it in the (OpenCL) compiler?

---

### 评论 #20 — gstoner (2017-03-04T20:53:54Z)

We fixed that with the new OpenCL compiler using native code generator.     We want to give ability to fully express the hardware even when the compiler can not generate the instructions.   We figured every one needed if we needed it for our work on miOpen our deep learning solver and Tensile.   We have been working on GCN ISA assembly optimized kernel for a number of the key convolutions and now GEMMS

Next OpenCL drop on ROCm will 100% OpenSource so you since see better into the tools.

I do not know if you saw this one  on Sub Dword Addressing as well  http://gpuopen.com/using-sub-dword-addressing-on-amd-gpus-with-rocm/


Greg
On Mar 4, 2017, at 2:44 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


Did you see this article AMD GCN Assembly: Cross-Lane Operations http://gpuopen.com/amd-gcn-assembly-cross-lane-operations/

I have seen it, but I did not think it was possible to use in-line ASM with OpenCL. Or is there some other way to implement it in OpenCL?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-284179570>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuVySj4LcoN8iaBDAtnNvB-9mfgY6ks5ric1KgaJpZM4MS4y2>.



---

### 评论 #21 — pszi1ard (2017-03-05T02:25:13Z)

> We fixed that with the new OpenCL compiler using native code generator.     We want to give ability to fully express the hardware even when the compiler can not generate the instructions.   We figured every one needed if we needed it for our work on miOpen our deep learning solver and Tensile.

That sounds great. How will this be exposed? Will you add OpenCL extensions for the equivalent permute/swizzle intrinsics supported in HCC? Will you allow inline ASM in OpenCL?

> I do not know if you saw this one  on Sub Dword Addressing as well  http://gpuopen.com/using-sub-dword-addressing-on-amd-gpus-with-rocm/

No, I have not. Thanks for the link. In our current kernels I doubt we can use these tricks. We need SP for floating point; integer data is either 32-bit bitmasks or indices that do not lend themselves well to packing.

---

### 评论 #22 — gstoner (2017-03-05T14:31:54Z)


On Mar 4, 2017, at 8:25 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


We fixed that with the new OpenCL compiler using native code generator. We want to give ability to fully express the hardware even when the compiler can not generate the instructions. We figured every one needed if we needed it for our work on miOpen our deep learning solver and Tensile.

That sounds great. How will this be exposed? Will you add OpenCL extensions for the equivalent permute/swizzle intrinsics supported in HCC? Will you allow inline ASM in OpenCL?

We will have intrinsics for you to get access to them,  in addition  you will be able to do inline asm in OpenCL.   HCC and OpenCL both now use CLANG FrontEnd so we making sure match functionality in both languages.

Greg



---

### 评论 #23 — pszi1ard (2017-03-06T18:29:33Z)

Sound good. Is there an ETA/release schedule for 1.5 and later? Actually, do you have _any_ ROCm roadmap/plans regarding features, support, etc. that you can share?

---

### 评论 #24 — pszi1ard (2017-07-13T19:53:38Z)

I have tested ROCm 1.6 release and my initial kernel-only performance assessment is: performance is still 30%-40% lower than what I measured with the old fglrx stack (and the early versions of AMDGPU-PRO). Here's the data with GROAMCS 2016 obtained using a benchmark that runs a wide range of input sizes:
- [Fiji](https://docs.google.com/spreadsheets/d/1q-0FeIA4Lba2PNZ_VXjdUuKt_68J4MZhMnX8Dkr0E5M/pubchart?oid=246898455&format=interactive)
- [Hawaii](https://docs.google.com/spreadsheets/d/1q-0FeIA4Lba2PNZ_VXjdUuKt_68J4MZhMnX8Dkr0E5M/pubchart?oid=829979419&format=interactive)


---

### 评论 #25 — BorisI (2017-07-13T21:42:01Z)

It's possible to optimize performance bottlenecks by replacing the kernels with native ISA. Here's a repository with examples and how-to's: https://github.com/ROCm-Developer-Tools/LLVM-AMDGPU-Assembler-Extra

---

### 评论 #26 — Kirpich30000 (2017-07-13T21:48:56Z)

BTW,

llvm supports gcn inline assembly (the syntax is the same as https://gcc.gnu.org/onlinedocs/gcc/Using-Assembly-Language-with-C.html)
You can try to use it. Disclaimer - it's not easy, but it works =)

Simple example can be found here https://github.com/ROCm-Developer-Tools/LLVM-AMDGPU-Assembler-Extra/blob/master/examples/gfx8/s_memrealtime_inline.cl

---

### 评论 #27 — nevion (2017-07-14T08:16:55Z)

@jstefanop don't get toxic.  This is the last place we need that.  Growing pains with an inspectable  environment and tangable changes by going opensource with a fully open background fed with modern clang.   The relevance and importance of this project and AMD has never been higher. They need to know you mean business but you need to stay a customer too so you get your stuff performing, crypto guys and image processing/dense computations too.  It's clear they got alot on their plate and things look ready for a rapid evolution to kick ass status, but it's hard to know what day that is watching and waiting as we have been.  Have the patience of Buddha, remove your last line in your previous message, and contact AMD product marketing as officially as your university allows you to and sell the story of your research helping defeat cancer enabled by their hardware - tell them what you need working in a way non-engineers would understand, but with some specifics. Try and get the universities allowance for any marketing blerb on linkedin/hpc news you if you can while imparting the importance of what you need.  Try and make sure everybody wins. Then wait.  Hopefully they'll either strategize differently or get more people to help get things done sooner - or things just work at T+1.

I do wish we knew what was wrong with the current state of the compiler, it's clear a little wonky.   Runtime still has some bugs clearly too but I don't know if those are too bad... if I understood how the runtime worked (or where it is) I'd probably fix some of those issues.

---

### 评论 #28 — gstoner (2017-07-14T12:41:25Z)

The Gromacs issue is different then what @jstefanop woried about he is looking at Currency mining.    What you see in the in the data above is the ROCm compiler is doing it job up to 3 nano sec, Performance slows down where it falls behind,  it was  leading up until then.   @pszi1ard  We are digging into more into it this month,    Is data line for 2236.1 on Fiji  the AMDGPUpro 17.10 driver.  

I am now looking at for Gromacs what is memory utilization at 3 nano sec simulation time  @pszi1ard. thank you for your patience.   We finally have EPYC 4 GPU server we talked about I can also test on.   

Also ROCm 1.6.1 will be out next week,  we did found some firmware issue that were effecting OpenCL.  OpenCL right now on ROCm is Pre-Release Beta.    We are working on making ROCm best product possible,  it is new and it will have issue.   We are digging into to see if it compiler or driver issue.  

We are going back and comparing the exact same compiler that we use on Windows and AMDGPUpro 17.10 driver on ROCm to see if compiler issue or based driver issue.   Base driver issue take longer to triage since we sit on AMDGPU driver same one as the Open source driver uses. So  we have to look at changes in the DRM and even in base linux kernel, and dig though all the firmware changes. 

Here comparison on memory bandwidth for the two compilers 
<img width="533" alt="screen shot 2017-07-14 at 7 31 28 am" src="https://user-images.githubusercontent.com/4129721/28212364-b7179624-6866-11e7-82a4-3a83d160689b.png">
<img width="533" alt="screen shot 2017-07-14 at 7 31 49 am" src="https://user-images.githubusercontent.com/4129721/28212367-b9c09cd6-6866-11e7-8697-0e9297c123f4.png">

---

### 评论 #29 — gstoner (2017-07-14T12:59:36Z)

This is with Vega10 on current  looking at Mixbench for the two compilers 

<img width="614" alt="screen shot 2017-07-14 at 7 54 32 am" src="https://user-images.githubusercontent.com/4129721/28212999-c5c5a956-6869-11e7-8c91-0a0bafb707f3.png">
<img width="615" alt="screen shot 2017-07-14 at 7 57 29 am" src="https://user-images.githubusercontent.com/4129721/28213076-2616e086-686a-11e7-8253-1069bd0dc572.png">

---

### 评论 #30 — pszi1ard (2017-07-14T17:19:29Z)

@BorisI @Kirpich30000 Thanks for the tips, I'm generally not afraid to get my hands dirty with low-level programming, but first I'd like to see others aspects of the stack working, solid and stable i.e. compiler (most importantly reasonable register use), runtime (most importantly low CPU-side launch overhead, consistent async execution), and performance measurement tools. When those are in place, I'll certainly do inline assembly, especially for the workgroup reductions we use.

@jstefanop First of all, please do not hijack my issue that's about *GROMACS* performance regression. Your post was borderline toxic, I agree with @nevion. Additionally, you yourself state: "[the post] has nothing to do with the ROCm project" -- if so, please blog, tweet, or post on reddit about it elsewhere, your message has little relevance to this ROCm github issue.

---

### 评论 #31 — pszi1ard (2017-07-14T17:37:04Z)

@gstoner Thanks for the feedback. Note that the plots I linked are performance/system size (instead of the usual log-log scaling plots); x axis is input size, y axis is average kernel time per iteration/system size. 
It can be seen as kernel throughput (number of interactions calculated per unit of time) which is a useful way to illustrate peak throughput where the curves get flat vs the deterioration with smaller inputs (fewer wavefronts, more overheads, etc.).

> Is data line for 2236.1 on Fiji the AMDGPUpro 17.10 driver.

No, 2236.1 is either 16.5 or 16.6 which had already regressed wrt 2117.7 (which is AFAIR 16.3) which roughly matches the last fglrx (15.302, I think).

> I am now looking at for Gromacs what is memory utilization at 3 nano sec simulation time @pszi1ard. 

Not sure what the 3 nano sec refers to (x axis was input size, amended the plots now to add the missing label).

> We are going back and comparing the exact same compiler that we use on Windows and AMDGPUpro 17.10 driver on ROCm to see if compiler issue or based driver issue.

Note that unless 17.10 fixed the regression from around 16.4, that comparison will not highlight the full extent of the regression I illustrate.

By the way, you might want to also look at register use, that's always been an issue with our kernels (and for that reason I don't think babelstream is a representative case for our kernels even though these are instruction latency bound).


---

### 评论 #32 — gstoner (2017-07-14T17:40:37Z)

Already digging into scheduling and register allocation in LLVM. 

Now with the label it is 3000 atoms where the break happen. 

---

### 评论 #33 — gstoner (2017-07-14T17:46:27Z)

Why I am asking the driver version numbers on FIJI, I am seeing similar behavior in the base driver,  also trying to see if we have an issue core AMDGPU driver and Linux kernel interfaces,  and also map with compilers were used with that driver.   

---

### 评论 #34 — pszi1ard (2017-07-14T19:46:44Z)

> Now with the label it is 3000 atoms where the break happen.

Note that we're running short of work to fill the GPU and get balanced executions below ~10000 atoms; e.g. at 3000 atoms we have around 1100 wavefronts for the entire 64 CU Fiji chip. Even with the low occupancy the kernel suffers from, that's very little.

I've just managed to convince rcprof to work* and it looks like register usage is up at 93 VGPRs from the previous ~80 I recall (and even that's a lot more than it should be).

Just in case, here's the raw data too: https://goo.gl/XjoQxQ

---

### 评论 #35 — gstoner (2017-07-14T20:38:38Z)

@pszi1ard  Very cool,  thank you for the data. 

---

### 评论 #36 — pszi1ard (2017-07-17T15:49:06Z)

@gstoner more profiler data here: https://goo.gl/oT52xL

Further notes:
- I'm still observing very low PCI transfer rates. I've verified that the link speed is 8 GT/s, but as the above profiler output shows achieved bandwidth is only around 2-3 GB/s. 
- I also reproducibly get no asynchronous execution behavior in some cases.
- At the above link you can find reference runs on the same hardware with the old, fgrx driver that was producing code that used 80 VGPRs vs the current 93 for the `nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl` kernel.




---

### 评论 #37 — gstoner (2017-07-17T19:38:00Z)

Can you post the lspic -tvv output


---

### 评论 #38 — gstoner (2017-07-18T00:28:43Z)

So I sent a note to the lead developer on RCP to get this fixed.   

Also we think we found main culprit in lower  memory performance, it was introduced in ROCm 1.4, exasperated in 1.5 and 1.6  in by the base kernel driver team.  Doing some more testing now.  

---

### 评论 #39 — pszi1ard (2017-07-18T00:29:18Z)

```
$ lspci -tvv
-+-[0000:ff]-+-0b.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring
 |           +-0b.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring
 |           +-0b.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 R3 QPI Link 0 & 1 Monitoring
 |           +-0c.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0c.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0c.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0c.3  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0c.4  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0c.5  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0c.6  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0c.7  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Unicast Registers
 |           +-0f.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent
 |           +-0f.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Buffered Ring Agent
 |           +-0f.4  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers
 |           +-0f.5  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers
 |           +-0f.6  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 System Address Decoder & Broadcast Registers
 |           +-10.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCIe Ring Interface
 |           +-10.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCIe Ring Interface
 |           +-10.5  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers
 |           +-10.6  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers
 |           +-10.7  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Scratchpad & Semaphore Registers
 |           +-12.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 0
 |           +-12.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Home Agent 0
 |           +-13.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Target Address, Thermal & RAS Registers
 |           +-13.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Target Address, Thermal & RAS Registers
 |           +-13.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder
 |           +-13.3  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder
 |           +-13.4  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder
 |           +-13.5  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel Target Address Decoder
 |           +-13.6  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Channel 0/1 Broadcast
 |           +-13.7  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Global Broadcast
 |           +-14.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 0 Thermal Control
 |           +-14.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 1 Thermal Control
 |           +-14.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 0 ERROR Registers
 |           +-14.3  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 1 ERROR Registers
 |           +-14.6  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1
 |           +-14.7  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 0 & 1
 |           +-15.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 2 Thermal Control
 |           +-15.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 3 Thermal Control
 |           +-15.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 2 ERROR Registers
 |           +-15.3  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 0 Channel 3 ERROR Registers
 |           +-16.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Target Address, Thermal & RAS Registers
 |           +-16.6  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Channel 2/3 Broadcast
 |           +-16.7  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO Global Broadcast
 |           +-17.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Integrated Memory Controller 1 Channel 0 Thermal Control
 |           +-17.4  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3
 |           +-17.5  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3
 |           +-17.6  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3
 |           +-17.7  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DDRIO (VMSE) 2 & 3
 |           +-1e.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit
 |           +-1e.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit
 |           +-1e.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit
 |           +-1e.3  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit
 |           +-1e.4  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Power Control Unit
 |           +-1f.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 VCU
 |           \-1f.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 VCU
 \-[0000:00]-+-00.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 DMI2
             +-01.0-[01]--
             +-02.0-[02]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series]
             |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Device aae8
             +-03.0-[03]--+-00.0  Advanced Micro Devices, Inc. [AMD/ATI] Hawaii XT [Radeon R9 290X]
             |            \-00.1  Advanced Micro Devices, Inc. [AMD/ATI] Hawaii HDMI Audio
             +-05.0  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Address Map, VTd_Misc, System Management
             +-05.1  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 Hot Plug
             +-05.2  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 RAS, Control Status and Global Errors
             +-05.4  Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 I/O APIC
             +-11.0  Intel Corporation C610/X99 series chipset SPSR
             +-14.0  Intel Corporation C610/X99 series chipset USB xHCI Host Controller
             +-16.0  Intel Corporation C610/X99 series chipset MEI Controller #1
             +-19.0  Intel Corporation Ethernet Connection (2) I218-V
             +-1a.0  Intel Corporation C610/X99 series chipset USB Enhanced Host Controller #2
             +-1b.0  Intel Corporation C610/X99 series chipset HD Audio Controller
             +-1c.0-[04]--
             +-1c.3-[05]----00.0  VIA Technologies, Inc. VL805 USB 3.0 Host Controller
             +-1c.4-[06]----00.0  ASMedia Technology Inc. ASM1042A USB 3.0 Host Controller
             +-1d.0  Intel Corporation C610/X99 series chipset USB Enhanced Host Controller #1
             +-1f.0  Intel Corporation C610/X99 series chipset LPC Controller
             +-1f.2  Intel Corporation C610/X99 series chipset 6-Port SATA Controller [AHCI mode]
             \-1f.3  Intel Corporation C610/X99 series chipset SMBus Controller
```

---

### 评论 #40 — gstoner (2017-07-18T00:30:31Z)

Also seeing some improvement in 4.11 Linux kernel generally over 4.9 linux kernel.

---

### 评论 #41 — pszi1ard (2017-07-18T00:34:39Z)

Sounds good, thanks for the quick feedback.

Do you have any thoughts (or questions) on the register allocation and concurrency issues?

---

### 评论 #42 — gstoner (2017-07-18T00:35:11Z)

can you send  sudo lspci -xxxx and sudo lspci -vvvv

---

### 评论 #43 — gstoner (2017-07-18T00:35:49Z)

Which brand is the motherboard


---

### 评论 #44 — pszi1ard (2017-07-18T00:47:35Z)

sudo lspci -xxxx
https://drive.google.com/open?id=0B6dQqsegA1FMZ0RvSEZNRDFicUk

sudo lspci -vvv
https://drive.google.com/open?id=0B6dQqsegA1FMWkEta3pRUzJ3QTg

```
$ sudo dmidecode | grep "Base Board" -A3
Base Board Information
	Manufacturer: MSI
	Product Name: X99S SLI PLUS (MS-7885)
	Version: 1.0
```

---

### 评论 #45 — gstoner (2017-07-18T00:54:32Z)

I noticed there has been a few SBIOS update for this board, including for GPU support.  Have you update it.  This is the latest SBIOS,  I just want to make sure we have this base covered.   

https://us.msi.com/Motherboard/support/X99S-SLI-PLUS.html
Version
1.D
Release Date
2016-07-18
File Size
5.94 MB
 
Description
- Improved Broadwell-E CPU compatibility.
- Improved memory compatibility.
- Improved BIOS multi languages support.

---

### 评论 #46 — pszi1ard (2017-07-18T01:35:34Z)

Sure, I can try to have the BIOS upgraded. Note that no such issues were observed with the previous AMD drivers (nor NVIDIA), so I suspect that it might not solve the issue.

---

### 评论 #47 — gstoner (2017-07-18T03:08:07Z)

Fiji Nano located in Bus 02:00.0 is only running at PCie Gen1 speed while the Hawaii XT located in Bus 03:00.0 is running at full PCIe speed. Can you swap the PCIe slots to see if there’s a problem with the slot where Fiji Nano is currently situated?
 
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca) (prog-if 00 [VGA controller])
                Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Radeon R9 FURY X / NANO
                Physical Slot: 6
                Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx+
                Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                Latency: 0, Cache Line Size: 32 bytes
                Interrupt: pin A routed to IRQ 52
                Region 0: Memory at e0000000 (64-bit, prefetchable) [size=256M]
                Region 2: Memory at f0000000 (64-bit, prefetchable) [size=2M]
                Region 4: I/O ports at e000 [size=256]
                Region 5: Memory at fbe00000 (32-bit, non-prefetchable) [size=256K]
                Expansion ROM at fbe40000 [disabled] [size=128K]
                Capabilities: [48] Vendor Specific Information: Len=08 <?>
                Capabilities: [50] Power Management version 3
                                Flags: PMEClk- DSI- D1+ D2+ AuxCurrent=0mA PME(D0-,D1+,D2+,D3hot+,D3cold+)
                                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
                                DevCap:               MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 unlimited
                                                ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset-
                                DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                                                RlxdOrd- ExtTag- PhantFunc- AuxPwr- NoSnoop+
                                                MaxPayload 256 bytes, MaxReadReq 512 bytes
                                DevSta: CorrErr+ UncorrErr- FatalErr- UnsuppReq+ AuxPwr- TransPend-
                                LnkCap: Port #0, Speed 8GT/s, Width x16, ASPM not supported, Exit Latency L0s <64ns, L1 <1us
                                                ClockPM- Surprise- LLActRep- BwNot-
                                LnkCtl:  ASPM Disabled; RCB 64 bytes Disabled- CommClk+
                                                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                                
 ## LnkSta: Speed 2.5GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-

                                DevCap2: Completion Timeout: Not Supported, TimeoutDis-, LTR-, OBFF Not Supported
                                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                                                Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                                                Compliance De-emphasis: -6dB
                                LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete+, EqualizationPhase1+
                                                EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
                Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
                                Address: 00000000fee005b8  Data: 0000
                Capabilities: [100 v1] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
                Capabilities: [150 v2] Advanced Error Reporting
                                UESta:   DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                                UEMsk: DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                                CESta:   RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                                CEMsk: RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                                AERCap:               First Error Pointer: 00, GenCap+ CGenEn- ChkCap+ ChkEn-
                Capabilities: [200 v1] #15
                Capabilities: [270 v1] #19
                Capabilities: [2b0 v1] Address Translation Service (ATS)
                                ATSCap:               Invalidate Queue Depth: 00
                                ATSCtl:  Enable-, Smallest Translation Unit: 00
                Capabilities: [2c0 v1] #13
                Capabilities: [2d0 v1] #1b
                Capabilities: [328 v1] Alternative Routing-ID Interpretation (ARI)
                                ARICap: MFVC- ACS-, Next Function: 1
                                ARICtl:  MFVC- ACS-, Function Group: 0
                Kernel driver in use: amdgpu
 
 
Upstream bridge is also stuck at Gen1 speed:
 
00:02.0 PCI bridge: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCI Express Root Port 2 (rev 02) (prog-if 00 [Normal decode])
                Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
                Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                Latency: 0, Cache Line Size: 64 bytes
                Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
                I/O behind bridge: 0000e000-0000efff
                Memory behind bridge: fbe00000-fbefffff
                Prefetchable memory behind bridge: 00000000e0000000-00000000f01fffff
                Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort+ <SERR- <PERR-
                BridgeCtl: Parity- SERR- NoISA- VGA- MAbort- >Reset- FastB2B-
                                PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
                Capabilities: [40] Subsystem: Micro-Star International Co., Ltd. [MSI] Device 7885
                Capabilities: [60] MSI: Enable+ Count=1/2 Maskable+ 64bit-
                                Address: fee00298  Data: 0000
                                Masking: 00000002  Pending: 00000000
                Capabilities: [90] Express (v2) Root Port (Slot+), MSI 00
                                DevCap:               MaxPayload 256 bytes, PhantFunc 0
                                                ExtTag- RBE+
                                DevCtl: Report errors: Correctable+ Non-Fatal+ Fatal+ Unsupported+
                                                RlxdOrd- ExtTag- PhantFunc- AuxPwr- NoSnoop-
                                                MaxPayload 256 bytes, MaxReadReq 128 bytes
                                DevSta: CorrErr- UncorrErr- FatalErr- UnsuppReq- AuxPwr- TransPend-
                                LnkCap: Port #3, Speed 8GT/s, Width x16, ASPM not supported, Exit Latency L0s <512ns, L1 <16us
                                                ClockPM- Surprise+ LLActRep+ BwNot+
                                LnkCtl:  ASPM Disabled; RCB 64 bytes Disabled- CommClk+
                                                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-

                                ##  LnkSta: Speed 2.5GT/s, Width x16, TrErr- Train- SlotClk+ DLActive+ BWMgmt+** ABWMgmt+


                                SltCap:  AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                                                Slot #6, PowerLimit 0.000W; Interlock- NoCompl-
                                SltCtl:    Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                                                Control: AttnInd Off, PwrInd Off, Power- Interlock-
                                SltSta:   Status: AttnBtn- PowerFlt- MRL- CmdCplt- PresDet+ Interlock-
                                                Changed: MRL- PresDet- LinkState-
                                RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible+
                                RootCap: CRSVisible-
                                RootSta: PME ReqID 0000, PMEStatus- PMEPending-
                                DevCap2: Completion Timeout: Range BCD, TimeoutDis+, LTR-, OBFF Not Supported ARIFwd+
                                DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled ARIFwd+
                                LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                                                Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                                                Compliance De-emphasis: -6dB
                                LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete+, EqualizationPhase1+
                                                EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
                Capabilities: [e0] Power Management version 3
                                Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0+,D1-,D2-,D3hot+,D3cold+)
                                Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                Capabilities: [100 v1] Vendor Specific Information: ID=0002 Rev=0 Len=00c <?>
                Capabilities: [110 v1] Access Control Services
                                ACSCap:               SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
                                ACSCtl: SrcValid- TransBlk- ReqRedir- CmpltRedir- UpstreamFwd- EgressCtrl- DirectTrans-
                Capabilities: [148 v1] Advanced Error Reporting
                                UESta:   DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                                UEMsk: DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                                UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                                CESta:   RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                                CEMsk: RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr+
                                AERCap:               First Error Pointer: 00, GenCap- CGenEn- ChkCap- ChkEn-
                Capabilities: [1d0 v1] Vendor Specific Information: ID=0003 Rev=1 Len=00a <?>
                Capabilities: [250 v1] #19
                Capabilities: [280 v1] Vendor Specific Information: ID=0005 Rev=3 Len=018 <?>
                Capabilities: [300 v1] Vendor Specific Information: ID=0008 Rev=0 Len=038 <?>
                Kernel driver in use: pcieport

---

### 评论 #48 — jstefanop (2017-07-18T05:18:37Z)

@gstoner are you guys planning on upgrading the rocm kernel to 4.11? 

---

### 评论 #49 — pszi1ard (2017-07-18T14:17:49Z)

@gstoner From what I've seen that's typically due to power management; if I load the GPU I get this:
```
00:02.0 PCI bridge: Intel Corporation Xeon E7 v3/Xeon E5 v3/Core i7 PCI Express Root Port 2 (rev 02) (prog-if 00 [Normal decode])
[...]
                  LnkSta: Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive+ BWMgmt+ ABWMgmt+
[...]
 02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Fiji [Radeon R9 FURY / NANO Series] (rev ca) (prog-if 00 [VGA controller])
[...]
                  LnkSta: Speed 8GT/s, Width x16, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-

```
What's strange is that the bus the Hawaii GPU on 00:03.0 does not enter into lower perf/power state.

---

### 评论 #50 — pszi1ard (2017-07-18T19:23:34Z)

> I also reproducibly get no asynchronous execution behavior in some cases.

I think I've got that nailed down. It looks like the driver / runtime is quite resource-intensive and it wants core 0 (possibly hw thread 0?) to run on and if it does not have it, it fails to launch GPU tasks until the core frees up. Does that make sense?

I'm collecting detailed data and will post it later.

---

### 评论 #51 — pszi1ard (2017-07-19T00:19:33Z)

Here's more detailed data (also comparing to the CUDA runtime/driver):
https://docs.google.com/spreadsheets/d/1GjIhiWLXsFK5SxE2n88-oz0dYZ3WXXifgIUTyKDE74M/edit?usp=sharing

This essentially seems confirm that if the first core is left empty (that is neither of the hw threads used), performance is good (although clFinish somewhat expensive, it seems). Otherwise, if core 0 gets loaded, the GPU task scheduling behavior is not pretty erratic.

I've also noticed that with this modded 4.9 kernel (4.9.0-kfd-compute-rocm-rel-1.6-77), the per-core load does not show up in monitoring tools, so it looks like something is broken in /proc:
```
$ stress -c 1 &
$ ps aux | grep $!
pszilard 18516  0.0  0.0   7332   960 pts/1    S    02:18   0:00  |           \_ stress -c 1 -t 10
```





---

### 评论 #52 — gstoner (2017-07-19T12:43:07Z)

OpenCL has producer/consumer thread for dispatch,  the OpenCL runtime should not be pinning to the first core,  the Main developer thinks  CQ thread to jump from one core to another if all core has pinned threads to get a fair time share.  He is thinking there must be a heuristic preventing the thread to reschedule on another core.

He is going to try bump the priority of the CQ thread to see if we still have that issue with oversubscription and pinning.  




---

### 评论 #53 — pszi1ard (2017-07-19T14:03:49Z)

> OpenCL has producer/consumer thread for dispatch, 

Not directly related, but GROMACS will by default use all hardware threads available which has not (and seems that it will not) play well with the AMD OpenCL runtime, so we'd need some heuristic to leave some resources available.

How much resources do you expect that this thread requires? Should in theory a hardware thread be enough? Is there one CQ thread only, one per device (perhaps one per application context per device)? I assume he dispatch work is NUMA sensitive?

>  the OpenCL runtime should not be pinning to the first core, the Main developer thinks CQ thread to jump from one core to another if all core has pinned threads to get a fair time share.

I did not assume that either, that's why I was careful to not claim that the runtime's thread is pinned. However, the observations seem to suggest that the thread does not move around. 

> He is going to try bump the priority of the CQ thread to see if we still have that issue with oversubscription and pinning.

Note that even if there are plenty of free cores, I still observe the peculiar behavior.

---

### 评论 #54 — pszi1ard (2017-08-03T01:44:12Z)

Good news: I see improvements on across all performance issues -- great work!
- kernel performance is up by 25-30% and marginally better than the best observed ever (the fglrx reference)
- register count for the particular kernel I looked at `nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl`) is down to 81; still a bit higher than before, but
- the CQ thread issue seems mostly resolved (presumably with the new kernel driver), though I still see significant application slowdown when all threads are used in computation right after the GPU task enqueue (see col 7 and 8 here: https://docs.google.com/spreadsheets/d/1GjIhiWLXsFK5SxE2n88-oz0dYZ3WXXifgIUTyKDE74M/pubchart?oid=939045217);
- measured PCI-E bandwidth is improved: 6.7-9.4 GB/s peak (see https://drive.google.com/drive/folders/0B6dQqsegA1FMa3VYRHNFZmJmcXc)

Remaining issues:
- GPU queue sync (clFinish) still seems quite expensive, ends up taking 10-20% of runtime at short iteration time;
- peak PCI-E transfer rate is still not reached


---

### 评论 #55 — gstoner (2017-08-03T02:06:06Z)


On Aug 2, 2017, at 8:44 PM, Szilárd Páll <notifications@github.com<mailto:notifications@github.com>> wrote:


Good news: I see improvements on across all performance issues -- great work!

  *   kernel performance is up by 25-30% and marginally better than the best observed ever (the fglrx reference)
  *   register count for the particular kernel I looked at nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl) is down to 81; still a bit higher than before, but
  *   the CQ thread issue seems mostly resolved (presumably with the new kernel driver), though I still see significant application slowdown when all threads are used in computation right after the GPU task enqueue (see col 7 and 8 here: https://docs.google.com/spreadsheets/d/1GjIhiWLXsFK5SxE2n88-oz0dYZ3WXXifgIUTyKDE74M/pubchart?oid=939045217);
  *   measured PCI-E bandwidth is improved: 6.7-9.4 GB/s peak (see https://drive.google.com/drive/folders/0B6dQqsegA1FMa3VYRHNFZmJmcXc)

Remaining issues:

  *   GPU queue sync (clFinish) still seems quite expensive, ends up taking 10-20% of runtime at short iteration time;
  *   peak PCI-E transfer rate is still not reached

When you test PCIe bandwidth this is NUMA effects, we are looking into this.

Greg




—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/93#issuecomment-319844667>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DufRINNpMOrgWZnQSqAsyEGI6zgvDks5sUSXtgaJpZM4MS4y2>.



---

### 评论 #56 — pszi1ard (2017-08-06T17:51:55Z)

> When you test PCIe bandwidth this is NUMA effects, we are looking into this.

I'm using a single socket, single NUMA CPU, how can it be a NUMA effect?

Can you comment on the expected driver/runtime expected resource needs and whether my observed clFinish overhead is "normal" and here to stay? We need to provision resources to jitter and overheads.

---

### 评论 #57 — gstoner (2017-08-06T18:11:29Z)

We looking at looking clFINISH

I will look your Xeon since they have internal NUMA organization when you cross a certain level of cores

Greg


---

### 评论 #58 — pszi1ard (2017-08-06T18:34:13Z)

> I will look your Xeon since they have internal NUMA organization when you cross a certain level of cores

It's an LLC single-ring i7 5960X, not a Xeon!
 

---

### 评论 #59 — gstoner (2017-08-06T18:35:05Z)

Thanks it is still Xeon,  just rebranded ; )  Used to work for Intel

Greg



---

### 评论 #60 — pszi1ard (2017-08-06T19:35:49Z)

I have not worked at Intel, but Xeon is a marketing name rather than an arch name, isn't it ;) 
In any case, do you mean that there can be NUMA effect even though it's an LLC single-ring / home agent chip?

---

### 评论 #61 — gstoner (2017-08-06T19:47:42Z)

In some of them, not yours.  

---

### 评论 #62 — pszi1ard (2017-08-28T18:32:39Z)

Update: with ROCm 1.6.148 I see no significant changes in either of the remaining issues (PCIe transfer and task wait/launch overhead -- related to the latter see some numbers here: 
https://docs.google.com/spreadsheets/d/1bKI9FwHh8AGXkK4XtK3qBOTyDJ-7gxbuSTomuLkAEKY/edit?usp=sharing
)

---

### 评论 #63 — gstoner (2017-08-28T19:25:44Z)

Thanks,  I will look this over. 


---

### 评论 #64 — pszi1ard (2017-12-11T14:09:20Z)

Any update on this? We'll be releasing the next major version and it would be good to know whether/what should we advise users.

---

### 评论 #65 — pszi1ard (2018-01-18T17:13:01Z)

Update: for now we ended up recommending the use of ROCm in the new [release documentation](http://manual.gromacs.org/documentation/2018/user-guide/mdrun-performance.html), but I'd be more comfortable if we could test better 1.7 and hopefully have issues solved soon.

---

### 评论 #66 — pszi1ard (2018-05-16T17:29:16Z)

Here's my ROCm 1.8 feedback.

On our test machines PCIe transfer speed is still rather low (about half of what it should be; ~6 GB/s both direction, with transfers of a few MB in size); note that with AMDGPU-PRO 17.5 I get the expected 12 GB/s in both directions.

Kernel performance is slightly improved which is good. However, it seems that (as I suspected) something is off with Vega performance on ROCm. With an AMDGPU-PRO legacy install I seem to get _~30% better_ performance in out main kernel; the other kernels are also faster! This is a huge difference that would immediate make the Vega GPUs quite competitive, so I'd like to get to the bottom of it and hopefully improve it soon. (Still having plenty of trouble with rcp on ROCm so please let me know if your team can look into this.)

---

### 评论 #67 — pszi1ard (2018-05-16T17:29:46Z)

Side-note: what are the identical/different components in ROCm vs AMDGPU-PRO legacy / pal? Is there a thorough documentation on this somewhere?

---

### 评论 #68 — gstoner (2018-05-16T17:56:08Z)

@pszi1ard this is still on the MSI motherboard correct 

---

### 评论 #69 — gstoner (2018-05-16T18:07:17Z)

Side-note: what are the identical/different components in ROCm vs AMDGPU-PRO legacy / pal? Is there a thorough documentation on this somewhere?

We have two compiler,  one is OpenCL using CLANG to LLVM to HSAIL intermediate language,  then it passes IL to the finalizer which then calls the AMD GPU shader compiler which is used for OpenGL and DirectX 12.   This can be supported on ORCA, PAL, and ROCr.  It is proprietary compiler so we can not opensource it. 

The Compiler on ROCm stack is 100% opensource you can find its documentation here. 
https://llvm.org/docs/AMDGPUUsage.html#introduction.  Note this support ROCr  and PAL as well. 





---

### 评论 #70 — gstoner (2018-05-16T18:15:56Z)

Also, can you run this on 1.8 and report the  numbers 
https://github.com/RadeonOpenCompute/rocm_bandwidth_test

---

### 评论 #71 — pszi1ard (2018-05-17T23:54:19Z)

@gstoner Do you mean that the PRO stack uses an entirely different finalizer/codegen so regardless of whether "legacy" mode is used or not there is no similarity with the ROCm compiler?

> Also, can you run this on 1.8 and report the numbers
> tps://github.com/RadeonOpenCompute/rocm_bandwidth_test

This is on an X99 and on random Z97 mobo:
http://termbin.com/r9z2c
http://termbin.com/my5b

The X99 sytem is clearly not getting the peak performance. There is also still some discrepancy between what these HSA benchmarks show and what I measure in GROMACS / OpenCL. 

---

### 评论 #72 — gstoner (2018-05-17T23:59:43Z)

@pszi1ard This benchmark test the bandwidth at ROCr level removing Language Runtime.   So now I am going to go get the team looks over OpenCL mapping to ROCr to see if there is an issue. 

I finally have MSI x99 come in, we do not see this on ASUS X99. 

---

### 评论 #73 — pszi1ard (2018-05-18T18:13:31Z)

> @pszi1ard This benchmark test the bandwidth at ROCr level removing Language Runtime. So now I am going to go get the team looks over OpenCL mapping to ROCr to see if there is an issue.

Thanks! I've not looked at the implementation, does this benchmark use explicitly pinned buffers?

As a side-note:  we've built C++ custom allocator-support for page-alignment and pinning for CUDA, so if there is any use of page-aligning or somehow pinning CPU buffers, we could certainly do that. Any advise you could give is welcome. 

> I finally have MSI x99 come in, we do not see this on ASUS X99.

Great, thanks. In the meantime I'll try to see if we can update the firmware and get back.

---

### 评论 #74 — pszi1ard (2018-08-24T17:12:11Z)

I'm still observing PCIe BW issues. I've three cards, one in the infamous MSI X99 board two in another Asus X99 and other than the RX560 in the latter neither the Fiji nor the Vega card behave as they should wrt PCIe BW:
Fiji + MSI X99 http://termbin.com/ic26
Vega + Asus X99  http://termbin.com/mxpj
R560 + Asus X99 http://termbin.com/4i1x

Note that the the gpu_memory_benchmark also behaves weird, in the few M's regime it peaks >15-16 GB/s which is, I think, not is a reasonable measurement for PCIe BW.

Used ROCm 1.8.2 (rock-dkms  1.8-192). 

Should I file a separate report about this? 

---

### 评论 #75 — gstoner (2018-08-30T14:19:53Z)

We now obsoleted that benchmark gpu_memorybenchmark.   It was using the CPU for timer not GPU like NVIDIA does in it PCIe benchmark.    You should use https://github.com/RadeonOpenCompute/rocm_bandwidth_test 

One thing we just release a Beta of our  ROCm Validation TestSuite beta for validating ROCm on your hardware. 
https://github.com/ROCm-Developer-Tools/ROCmValidationSuite

---

### 评论 #76 — pszi1ard (2018-09-03T19:45:06Z)

Apologies, I forgot about the new bandwidth test tool. Reran with rocm_bandwidth_test (detailed results below) and, not too unexpectedly, I get marginally higher numbers in most cases, with one exception: an RX560 plugged into an Asus X99 with PLX swtiches now performs very poorly with the rocm_bandwidth_test tool:

```
$ ./rocm_bandwidth_test -s 0 -d 1 -m 128
..

================           Benchmark Result         ================
================ Src Device Id: 0 Src Device Type: Cpu ================
================ Dst Device Id: 1 Dst Device Type: Gpu ================

Data Size      Avg Time(us)   Avg BW(GB/s)   Min Time(us)   Peak BW(GB/s)  
128 MB         9715.109667    13.815359      9705.184000    13.829488      

 $ ./rocm_bandwidth_test -s 0 -d 2 -m 128
..

================           Benchmark Result         ================
================ Src Device Id: 0 Src Device Type: Cpu ================
================ Dst Device Id: 2 Dst Device Type: Gpu ================

Data Size      Avg Time(us)   Avg BW(GB/s)   Min Time(us)   Peak BW(GB/s)  
128 MB         90470.829000   1.483547       90465.811000   1.483629       


 $ ./gpu_memory_benchmark -f 0 -t 1 -s 131072
================ User-Defined  Mode Result ===================================
  131072KB                             9.747396

$ ./gpu_memory_benchmark -f 0 -t 2 -s 131072
================ User-Defined  Mode Result ===================================
  131072KB                             13.471502

```


Detailed bench results:
Fiji + MSI X99 http://termbin.com/jv45
Vega + Asus X99 http://termbin.com/0cng
R560 + Asus X99 http://termbin.com/in4c

---

### 评论 #77 — ROCmSupport (2020-11-18T11:25:34Z)

Thanks @pszi1ard 
As its very old issue, and no updates for the last 2 years, this issue is going to be closed.
Request to open a new ticket, if you found any.
Thank you.

---
