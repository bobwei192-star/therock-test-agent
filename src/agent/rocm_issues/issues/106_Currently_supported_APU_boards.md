# Currently supported APU boards

> **Issue #106**
> **状态**: closed
> **创建时间**: 2017-04-17T03:10:40Z
> **更新时间**: 2018-01-31T13:12:51Z
> **关闭时间**: 2017-07-02T17:41:18Z
> **作者**: trinayan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/106

## 描述

I want a APU which supports RoCm . I know Kaveri isn't and there is possibly limited support for Carrizo. Could anyone tell me specific Carrizo APU boards or products available that are Rocm compatible currently?  

---

## 评论 (25 条)

### 评论 #1 — nevion (2017-04-17T03:14:03Z)

+1

---

### 评论 #2 — gstoner (2017-04-17T03:57:57Z)

I have ask why do you want APU,  Fine Grained SVM?  the performance of Carizzo APU is Single Precsion performance is slower then a RX460 GPU which are $99 or less now and you can get on Ryzen CPU which much faster then a Steamroller CPU's in Carizzo.  AMD Ryzen 5 1400 $169, and it uses a $99 dollar motherboard ( ASUS, MSI)  if you looking for low cost development system.  


We do internally have Carizzo system working a Dell Inspiron i3656-3355,  but it needs a Custom SystemBios Update to support the right CRAT table and option to turn on IOMMUv2.  It real pain to flash the SBIOS on the system.  We used in the early days of development of ROCm, it is still under test.  

---

### 评论 #3 — nevion (2017-04-17T04:10:35Z)

Even with ryzen vs kaveri you could do some int/float32 workloads faster with the APU provided local memory and the gpu cores are exploited properly.  There's a couple of places fine grained SVM is useful (GPU kernel daemons/IPC) Agreed that Ryzen is much faster in all other regards - was painful running c++ compilations on kaveri.

Low latency signal processing can make use of APUs provided the dispatch latency and zero copy properties are held and that the APU can complete computations faster than the transfer + computation time of whatever GPUs (say Vega)... it's an interesting niche environment where less (APU) can be more (wallclock faster than GPU).

---

### 评论 #4 — gstoner (2017-04-17T04:54:21Z)

Ok make since if your aiming to that class of solution.  I understand the benefits of the APU,  Kaveri was mess for Fine grain memory performance - it was less 8 GB/s which put you under the 12 GB/s we can get for Usermode DMA based transfers going.  The performant memory path on Kaveri was IO coherent.   Carrizo fixed this so you better memory bandwidth.  Now it is still shared with the CPU.    One thing if you can keep your problem on  Vega10 it has   16 GB of HBM memory at 500 GB/s   ( you can try this FIJI Nano today ) vs 25.6 GB/s and maximum of 16 GB of memory on total system on Carrizo.      But if your problem needs fine grain synchronization  with the CPU then the APU wins currently.   Lots of great work going on to address today PCIe bottlenecks.




On Apr 16, 2017, at 11:10 PM, Jason Newton <notifications@github.com<mailto:notifications@github.com>> wrote:


Even with ryzen vs kaveri you could do some int/float32 workloads faster with the APU provided local memory and the gpu cores are exploited properly. There's a couple of places fine grained SVM is useful (GPU kernel daemons/IPC) Agreed that Ryzen is much faster in all other regards - was painful running c++ compilations on kaveri.

Low latency signal processing can make use of APUs provided the dispatch latency and zero copy properties are held and that the APU can complete computations faster than the transfer + computation time of whatever GPUs (say Vega)... it's an interesting niche environment where less (APU) can be more (wallclock faster than GPU).

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/106#issuecomment-294401590>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Dub90xiHxooTyYQdzH43nCdSPyiM8ks5rwuY7gaJpZM4M-1K5>.



---

### 评论 #5 — trinayan (2017-04-17T12:47:26Z)

@gstoner : Thanks for your reply. We need it for research work. We are studying some workloads that exercise both CPU and GPU and although we could do it on a discrete GPU with coarse grained sharing, the APU architecture provides fine grained sharing and is better suited for the work. We could still try using OpenCL 2.0 versions of our code on an APU running the closed source AMD driver but Rocm being open source provides more flexibility especially when it comes to tools.

---

### 评论 #6 — gstoner (2017-04-17T13:12:37Z)

Trinayan,   where you based if you can us 110/120 Power ( The Dell is only 110/120 do priority power supply)  ,  I have Dell I can send you from the HSA Foundation for academic research.   It pre loaded with ROCm 1.4 I believe and BIOS.    I am also the Chairman and MD of the HSA Foundation. 

---

### 评论 #7 — gstoner (2017-04-17T13:24:19Z)

Note a Bristol Ridge ( it a socketed Carizzo)  system should work, but we only have internal development boards, we need to test a public shipping system before I say yes it compatible.  We have to check a system  SBIOS to see if can support the IOMMUV2 and does it have correct CRAT table setup.  CRAT is extension to ACPI SRAT Table for topology information. So you can see what it is doing http://lxr.free-electrons.com/source/drivers/gpu/drm/amd/amdkfd/kfd_crat.h     

The one we are looking forward to is the Zen based RavenRidge APU,.  It is not out yet, but lot of information on it on the web. 

---

### 评论 #8 — gstoner (2017-04-17T13:30:53Z)

One thing this all get easier when ROCm is a standard part of the OEM testing procedures,  Remember ROCm is 1 Year old,  April 4th is when we launched it.  One thing since your working on ROCm with OpenCL you have big lift in capability with ROCm 1.5, we still shooting to have it out near the end of this month,  We hopping to get it out on the 21st the same day as ROCm 1.0 was released to GitHub. 


---

### 评论 #9 — trinayan (2017-04-17T18:36:33Z)

@gstoner  : Thanks for the information. I believe we have the same Carizzo board here at Northeastern University. But recently many of the heterogeneous benchmarks that were working before are not working after updating to 1.4 . So I thought maybe there are other boards.We are trying to figure out what is the issue.  The same set of benchmarks work correctly on a dgpu system running rocm
I am also waiting eagerly for the RavenRidge APU boards to come out. 

Is 1.5 going to provide full support for OpenCL 2.0? I believe for 1.4 it is limited support only.

---

### 评论 #10 — briansp2020 (2017-04-25T16:17:39Z)

Is 1.5 coming this month? Only a few days left in the month...

---

### 评论 #11 — gstoner (2017-04-25T16:23:16Z)

Yep..  We been hard at work on this.

greg
On Apr 25, 2017, at 11:17 AM, Brian <notifications@github.com<mailto:notifications@github.com>> wrote:


Is 1.5 coming this month? Only a few days left in the month...

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/106#issuecomment-297083583>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSV14PoSupFW0Lla5TMBdWYBBJOLks5rzhyjgaJpZM4M-1K5>.



---

### 评论 #12 — zpodlovics (2017-05-04T10:28:31Z)

Please do not phase out the APU support (this is what happened with the Kaveri APU), there are lot's of functionality that only possible with (zero-copy) fine grained memory sharing, where the APU could be used as a low-latency co-processor. eg.:

https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/go

Also an APU with integrated HBM (even with limited 4-32GB (or more) capacity) would be an really-realy interesting target for development, especially when combined with a chip integrated high-speed communication with other nodes.

Please keep up your good work, and deliver the hw&sw to us that we can use for future development!

---

### 评论 #13 — gstoner (2017-05-04T11:03:06Z)

We are not planning to phase them out, but we will be more selective in what we support.    Thank you for the link.  It great to see 5 year of work on HSA has merit beyond our labs. 

---

### 评论 #14 — maxlem (2017-05-07T20:32:48Z)

Rare owner of a Bristol Ridge Laptop (Hp envy x360). I *think* I have iommu_v2 up and running from the fact that:
`ps -ef | grep iommu
root       164     2  0 14:11 ?        00:00:00 [amd_iommu_v2]
maxime    2899  2524  0 16:27 pts/3    00:00:00 grep --color=auto iommu
`
Currently running on rocm 1.5 kernel. clinfo reckon my gpu and grants me opencl 2.0 API:
`  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx801
`
 Helloworld works. I'm quite surprized, had no hope it would be working.

If you want me to run a few tests/benchmark or help out ring me. Thank you for your hard work.

Max

---

### 评论 #15 — gstoner (2017-05-07T21:27:17Z)

This is very good news.  We had report the new Bristol Ridge APU from HP were working had a proper CRAT Table and IOMMUv2 support.


Love to see more  data on the system.    Bablestream ( formally GPU Stream) ,  Mixbench, and any other app.


On May 7, 2017, at 3:32 PM, maxlem <notifications@github.com<mailto:notifications@github.com>> wrote:


Rare owner of a Bristol Ridge Laptop (Hp envy x360). I think I have iommu_v2 up and running from the fact that:
ps -ef | grep iommu root 164 2 0 14:11 ? 00:00:00 [amd_iommu_v2] maxime 2899 2524 0 16:27 pts/3 00:00:00 grep --color=auto iommu
Currently running on rocm 1.5 kernel. clinfo reckon my gpu and grants me opencl 2.0 API:
`
clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU) Success (1)
Platform Name AMD Accelerated Parallel Processing
Device Name gfx801

`
Helloworld works. I'm quite surprized, had no hope it would be working.

If you want me to run a few tests/benchmark or help out ring me. Thank you for your hard work.

Max

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/106#issuecomment-299732561>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSa7CgG_PeEk3AwOsm0Vnz9fVB41ks5r3ipxgaJpZM4M-1K5>.



---

### 评论 #16 — maxlem (2017-05-08T08:03:28Z)

don't know how to build babelstream, but here are mixbench results:

maxime@maxime-HP-ENVY-x360-m6-Convertible:~/workspace/bench/mixbench$ ./mixbench-ocl-ro
mixbench-ocl/read-only (v0.02-10-g79d284c)
Use "-h" argument to see available options
------------------------ Device specifications ------------------------
Platform:            AMD Accelerated Parallel Processing
Device:              gfx801/Advanced Micro Devices, Inc.
Driver version:      1.1 (HSA,LC)
Address bits:        64
GPU clock rate:      757 MHz
Total global mem:    1024 MB
Max allowed buffer:  256 MB
OpenCL version:      OpenCL 1.2 
Total CUs:           8
-----------------------------------------------------------------------
Buffer size:            256MB
Workgroup size:         256
Elements per workitem:  8
Workitem fusion degree: 4
Workitem stride:        NDRange
Buffer allocation:      Device allocated
Loading kernel source file...
Precompilation of kernels... [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]
---------------------------------------------------------- CSV data ----------------------------------------------------------
Experiment ID, Single Precision ops,,,,              Double precision ops,,,,              Integer operations,,, 
Compute iters, Flops/byte, ex.time,  GFLOPS, GB/sec, Flops/byte, ex.time,  GFLOPS, GB/sec, Iops/byte, ex.time,   GIOPS, GB/sec
            0,      0.250,   12.29,    2.73,  10.92,      0.125,   24.50,    1.37,  10.96,     0.250,   11.76,    2.85,  11.42
            1,      0.750,   11.93,    8.44,  11.25,      0.375,   24.29,    4.14,  11.05,     0.750,   11.73,    8.58,  11.44
            2,      1.250,   11.84,   14.17,  11.34,      0.625,   24.17,    6.94,  11.11,     1.250,   11.80,   14.22,  11.38
            3,      1.750,   11.82,   19.87,  11.35,      0.875,   24.76,    9.49,  10.84,     1.750,   11.85,   19.82,  11.33
            4,      2.250,   12.37,   24.41,  10.85,      1.125,   26.90,   11.23,   9.98,     2.250,   11.73,   25.74,  11.44
            5,      2.750,   12.40,   29.77,  10.83,      1.375,   26.39,   13.99,  10.17,     2.750,   11.72,   31.48,  11.45
            6,      3.250,   12.49,   34.93,  10.75,      1.625,   26.44,   16.50,  10.15,     3.250,   11.79,   37.01,  11.39
            7,      3.750,   12.44,   40.46,  10.79,      1.875,   26.28,   19.16,  10.22,     3.750,   11.77,   42.75,  11.40
            8,      4.250,   12.40,   46.00,  10.82,      2.125,   26.46,   21.56,  10.14,     4.250,   11.68,   48.86,  11.50
            9,      4.750,   12.30,   51.81,  10.91,      2.375,   26.53,   24.03,  10.12,     4.750,   11.76,   54.22,  11.42
           10,      5.250,   12.34,   57.09,  10.87,      2.625,   26.69,   26.40,  10.06,     5.250,   11.77,   59.87,  11.40
           11,      5.750,   12.31,   62.67,  10.90,      2.875,   26.59,   29.02,  10.09,     5.750,   11.77,   65.55,  11.40
           12,      6.250,   12.37,   67.84,  10.85,      3.125,   26.69,   31.43,  10.06,     6.250,   11.79,   71.12,  11.38
           13,      6.750,   12.40,   73.07,  10.83,      3.375,   26.59,   34.07,  10.09,     6.750,   11.79,   76.84,  11.38
           14,      7.250,   12.38,   78.60,  10.84,      3.625,   26.71,   36.44,  10.05,     7.250,   11.80,   82.50,  11.38
           15,      7.750,   12.39,   83.97,  10.84,      3.875,   27.79,   37.42,   9.66,     7.750,   17.64,   58.97,   7.61
           16,      8.250,   15.48,   71.55,   8.67,      4.125,   30.27,   36.58,   8.87,     8.250,   11.69,   94.70,  11.48
           17,      8.750,   12.32,   95.34,  10.90,      4.375,   26.81,   43.81,  10.01,     8.750,   11.75,   99.98,  11.43
           18,      9.250,   12.37,  100.36,  10.85,      4.625,   26.51,   46.84,  10.13,     9.250,   11.71,  106.01,  11.46
           20,     10.250,   12.28,  112.07,  10.93,      5.125,   26.09,   52.73,  10.29,    10.250,   11.69,  117.70,  11.48
           22,     11.250,   12.39,  121.91,  10.84,      5.625,   26.23,   57.58,  10.24,    11.250,   11.75,  128.54,  11.43
           24,     12.250,   12.26,  134.05,  10.94,      6.125,   26.43,   62.20,  10.16,    12.250,   11.76,  139.86,  11.42
           28,     14.250,   12.43,  153.83,  10.79,      7.125,   26.30,   72.72,  10.21,    14.250,   11.88,  160.95,  11.29
           32,     16.250,   12.29,  177.45,  10.92,      8.125,   26.48,   82.36,  10.14,    16.250,   11.77,  185.23,  11.40
           40,     20.250,   12.35,  220.11,  10.87,     10.125,   26.63,  102.06,  10.08,    20.250,   12.02,  226.15,  11.17
           48,     24.250,   12.39,  262.67,  10.83,     12.125,   26.54,  122.64,  10.11,    24.250,   13.76,  236.47,   9.75
           56,     28.250,   12.31,  308.02,  10.90,     14.125,   26.88,  141.04,   9.99,    28.250,   15.83,  239.54,   8.48
           64,     32.250,   12.33,  350.94,  10.88,     16.125,   26.55,  163.03,  10.11,    32.250,   17.96,  241.01,   7.47
           80,     40.250,   12.26,  440.52,  10.94,     20.125,   26.47,  204.11,  10.14,    40.250,   22.71,  237.89,   5.91
           96,     48.250,   12.45,  519.98,  10.78,     24.125,   26.48,  244.58,  10.14,    48.250,   27.16,  238.40,   4.94
          128,     64.250,   15.62,  551.92,   8.59,     32.125,   28.74,  300.01,   9.34,    64.250,   36.58,  235.77,   3.67
          192,     96.250,   22.52,  573.70,   5.96,     48.125,   37.13,  347.93,   7.23,    96.250,   55.32,  233.54,   2.43
          256,    128.250,   29.05,  592.64,   4.62,     64.125,   47.68,  361.04,   5.63,   128.250,   72.34,  237.94,   1.86
------------------------------------------------------------------------------------------------------------------------------

Probably won't break records on memory bw. hp crippled the system, using only single channel. sad.

---

### 评论 #17 — maxlem (2017-05-08T08:19:06Z)

BabelStream:
maxime@maxime-HP-ENVY-x360-m6-Convertible:~/workspace/bench/BabelStream$ ./ocl-stream 
BabelStream
Version: 3.2
Implementation: OpenCL
Running kernels 100 times
Precision: double
Array size: 268.4 MB (=0.3 GB)
Total size: 805.3 MB (=0.8 GB)
Using OpenCL device gfx801
Driver: 1.1 (HSA,LC)
Reduction kernel config: 32 groups of size 256
Function    MBytes/sec  Min (sec)   Max         Average     
Copy        10704.365   0.05015     0.06160     0.05186     
Mul         10713.620   0.05011     0.06317     0.05166     
Add         10330.118   0.07796     0.08789     0.07891     
Triad       10415.968   0.07731     0.08422     0.07841     
Dot         11729.476   0.04577     0.05692     0.04783     


---

### 评论 #18 — maxlem (2017-05-08T08:31:01Z)

no OpenCL 2.0 after all :(
Why is that so?

---

### 评论 #19 — gstoner (2017-05-08T12:08:44Z)

It supports OpenCL 2.0 kernel language all the feature of OpenCL minus Pipes and DeviceEnqueue.


On May 8, 2017, at 3:31 AM, maxlem <notifications@github.com<mailto:notifications@github.com>> wrote:


no OpenCL 2.0 after all :(
Why is that so?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/106#issuecomment-299805701>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudW9saxoZPe1Mjz1x_epwz0yLENMks5r3tLFgaJpZM4M-1K5>.



---

### 评论 #20 — gstoner (2017-05-08T13:47:46Z)

Thank you.

Greg
On May 8, 2017, at 3:19 AM, maxlem <notifications@github.com<mailto:notifications@github.com>> wrote:


BabelStream:
maxime@maxime-HP-ENVY-x360-m6-Convertible:~/workspace/bench/BabelStream$ ./ocl-stream
BabelStream
Version: 3.2
Implementation: OpenCL
Running kernels 100 times
Precision: double
Array size: 268.4 MB (=0.3 GB)
Total size: 805.3 MB (=0.8 GB)
Using OpenCL device gfx801
Driver: 1.1 (HSA,LC)
Reduction kernel config: 32 groups of size 256
Function MBytes/sec Min (sec) Max Average
Copy 10704.365 0.05015 0.06160 0.05186
Mul 10713.620 0.05011 0.06317 0.05166
Add 10330.118 0.07796 0.08789 0.07891
Triad 10415.968 0.07731 0.08422 0.07841
Dot 11729.476 0.04577 0.05692 0.04783

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/106#issuecomment-299803168>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DueJeqXuBXNElJ4MPLyd6YYeVb7W1ks5r3s_7gaJpZM4M-1K5>.



---

### 评论 #21 — maxlem (2017-05-08T16:21:49Z)

Quite a dog. memory-bw wise heh?

If you need me for anything else, will be glad to help. Oh and I'm on Ubuntu 16.10 btw.

---

### 评论 #22 — maxlem (2017-05-08T16:26:54Z)

Ah, one last question, do you support zero copy? Simply mapping a buffer with flag CL_MEM_USE_HOST_PTR will do it?



---

### 评论 #23 — gstoner (2017-05-09T17:18:30Z)

Yes, CL_MEM_USE_HOST_PTR buffers are ZeroCopy.
On May 8, 2017, at 11:26 AM, maxlem <notifications@github.com<mailto:notifications@github.com>> wrote:


Ah, one last question, do you support zero copy? Simply mapping a buffer with flag CL_MEM_USE_HOST_PTR will do it?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/106#issuecomment-299917394>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYqlCK31W_HJijRqoCMJay84A52Yks5r30JPgaJpZM4M-1K5>.



---

### 评论 #24 — Yougmark (2018-01-31T01:31:53Z)

@maxlem Wow! I just got HP envy x360 with Raven Ridge, but the CRAT table is invalid for APU.  The APU is recognized as CPU only and the Vega iGPU is recognized as a dGPU.

Did you do anything to setup ACPI CRAT table?

Thanks,
- Ming

---

### 评论 #25 — maxlem (2018-01-31T13:12:51Z)

No, but my unit has bristol ridge. The only thing I remember changing in
bios is something regarding partitions, to enable dual-boot. Sorry I can't
help.

On Tue, Jan 30, 2018 at 8:31 PM, Ming Yang <notifications@github.com> wrote:

> @maxlem <https://github.com/maxlem> Wow! I just got HP envy x360 with
> Raven Ridge, but the CRAT table is invalid for APU. The APU is recognized
> as CPU only and the Vega iGPU is recognized as a dGPU.
>
> Did you do anything to setup ACPI CRAT table?
>
> Thanks,
>
>    - Ming
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/106#issuecomment-361793445>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AJ-Jqfnihg5vVlT5BMKZd7QItA5_rDrXks5tP8KMgaJpZM4M-1K5>
> .
>


---
