# Segmentation Faults when running hsa/hip code samples

> **Issue #52**
> **状态**: closed
> **创建时间**: 2016-12-09T07:13:30Z
> **更新时间**: 2017-03-15T20:43:56Z
> **关闭时间**: 2017-02-22T16:17:35Z
> **作者**: ptrkrysik
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/52

## 描述

I've installed rocm package on Ubuntu 16.04 in accordance to the Readme on a laptop with AMD PRO A12-8800B R7 processor. When running any code sample compiled from  /opt/rocm/hsa/sample or  /opt/rocm/hip/sample directories I get segmentation fault error.

uname -r 
gives:
4.6.0-kfd-compute-rocm-rel-1.3-74


---

## 评论 (33 条)

### 评论 #1 — ptrkrysik (2016-12-10T09:35:02Z)

Same situation on a fresh Ubuntu 14.04 installation.

---

### 评论 #2 — ptrkrysik (2016-12-11T16:00:04Z)

Attached is crash report from Ubuntu 16.04

[_opt_rocm_hsa_sample_vector_copy.1000.crash.zip](https://github.com/RadeonOpenCompute/ROCm/files/644553/_opt_rocm_hsa_sample_vector_copy.1000.crash.zip)


---

### 评论 #3 — alexeib55 (2016-12-13T05:00:55Z)

Having same symptoms with fresh install of Rocm 1.3 of 16.04 Ubuntu, same kernel, System uses AMD FX8370 on Asus 970 Motherboard + Radeon RX480. Is this a supported confirguration?

---

### 评论 #4 — briansp2020 (2016-12-13T18:42:43Z)

@alexeib55 Please, check out the hardware requirement.
https://rocm.github.io/hardware.html

> CPU support: ROCm requires CPUs with PCIe Gen3 atomics capability, such as the Intel Xeon E5v3 and newer Xeon processors. It also supports consumer CPUs, such as Haswell-class Intel Core CPUs (v3 and newer). We know you’re going to ask—yes, ROCm is optimized to pull all the rich capabilities out of the new AMD Zen-based processors.

---

### 评论 #5 — alexeib55 (2016-12-13T22:27:51Z)

Can you list specific Intel consumer CPU models?  Also, I thought that ROCm 1.3 also added supported on the latest AMD consumer cards such as RX480.  Is that not the case?  If so, can you update HW requirement link to show which ones?

---

### 评论 #6 — gstoner (2016-12-14T03:08:34Z)

We support Core i3, i5, i7 Haswell or newer Consumer CPU's ( Haswell, Broadwell, Skylake) in the PCIe Gen3 x16 lanes.  Note some consumer motherboard have x16 edge connectors that really x4 lanes running PCIe Gen2.   ROCm 1.3 which released in November added RX480, RX470 and RX460, WX7100, WX5100, and WX4100 support for the Polaris family of products.   

---

### 评论 #7 — ptrkrysik (2016-12-14T06:40:21Z)

You don't support any of AMD's APU's anymore?

---

### 评论 #8 — gstoner (2016-12-14T12:46:05Z)

We still support the Carrizo APU and Bristol Ridge APU's, but your System vendor has to have in the System BIOS set up the CRAT Table correctly and also allow you to turn on IOMMUv2.   We have been finding a number of systems that we not properly configured or have the BIOS flag for you to turn IOMMUv2.        One thing the current ROCm Open Source Platform  is purpose built as a  headless linux GPU computing platform designed for servers.   

We have been looking at ROCm core capabilities for supporting broader set of languages into our standard linux drivers so you can get X11, OpenGL and Vulcan.  

---

### 评论 #9 — ptrkrysik (2016-12-14T13:25:09Z)

I've bought HP EliteBook 725 G3 with Carrizo (AMD PRO A12-8800B R7) specifically to evaluate how HSA is usable as a technology simplifying coding for GPUs.

In case of success I might be able to convince my team to use AMD's chips. What I expect after reading AMD's promotional materials is that HSA in Carrizo might offer something in-between CPU's SIMD instructions and discrete GPUs in terms of performance and ease of application to accelerate different kinds of computations. This is what I try to achieve with this computer.

1. Can you tell me how can I check if BIOS of my computer enables what need to be enabled in order to test HSA on this laptop?

2. Can someone confirm if ROCm 1.3 installed on ubuntu from packages provided here is working on any supported configuration? (working: it is possible to run examples without segfaults)

---

### 评论 #10 — ptrkrysik (2016-12-14T13:46:04Z)

I did (with ROCm kernel):
dmesg|grep   -A 6 IOMMUv2

and got:

[    1.950540] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    1.950727] usb 1-1: new high-speed USB device number 2 using ehci-pci
[    1.955955] CRAT table not found
[    1.955964] Virtual CRAT table created for CPU
[    1.955966] Parsing CRAT table with 1 nodes
[    1.955969] Creating topology SYSFS entries
[    1.955990] Topology: Add CPU node

Does this mean that CRAT table is set up correctly?

---

### 评论 #11 — jedwards-AMD (2016-12-14T15:41:44Z)

This means your SBIOS doesn't contain a CRAT table, so a virtual one was created for you. You may or may not be able to get a integrated GPU device; this depends on if the GPU is enabled by the BIOS. If you can run the vector_copy sample, you should have a valid GPU. Otherwise, no GPU is detectable.

---

### 评论 #12 — ptrkrysik (2016-12-15T05:45:14Z)

This computer doesn't have any other GPU device than AMD/ATI built-in
the AMD Carrizo APU. For sure the integrated GPU is not disabled.

vector_copy not only doesn't work but it throws segfault as well.


---

### 评论 #13 — jedwards-AMD (2016-12-15T13:35:16Z)

What is the output of vector copy? Also, do you know what line of the vector copy program the segfault occurs in?

Another thing to check is what modules are loaded. Attach the 'lsmod | grep kfd' output. I will tell you that all of these failures point to a non-detectable GPU.

---

### 评论 #14 — ptrkrysik (2016-12-15T17:42:48Z)

> What is the output of vector copy? Also, do you know what line of the
> vector copy program the segfault occurs in?

Program segfaults before any output is produced.
The line and the output of gdb:
vector_copy.c:154
154	    err = hsa_init();
(gdb) next

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7b783ec in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1

> Another thing to check is what modules are loaded. Attach the 'lsmod |
> grep kfd' output. I will tell you that all of these failures point to a
> non-detectable GPU.
> 

lsmod |grep kfd
amdkfd                188416  3
amd_iommu_v2           20480  1 amdkfd


---

### 评论 #15 — ptrkrysik (2016-12-16T09:23:53Z)

The GPU should be detectable as it is integrated with the Carrizo processor (which is said to be first one that support HSA 1.0 specification) in the laptop . For sure the integrated GPU is not disabled by BIOS. Is there some direct way to check if BIOS (or something else) is an obstacle to fully initialize everything so HSA could work?

---

### 评论 #16 — jedwards-AMD (2016-12-16T16:38:50Z)

There might be, but I would have to know what BIOS you are using. The BIOS is provided by the motherboard vendor, and it may or may not provided the required configuration to support the APU's GPU device. The APU devices have very specific system BIOS requirements if they are going to be used as ROCm enabled devices, leveraged via the HSA architecture and runtime specification. The system BIOS requirements were provided to the OEM vendors, and it is their responsibility to integrate the specifications into their own system BIOS implementations. Please contact HP for a BIOS that support the APU as a ROCm device.

---

### 评论 #17 — ptrkrysik (2016-12-17T17:05:15Z)

If I contact HP for updated BIOS it would be best to have 100% (or at
least 90%) proof that points to the BIOS as a source of problems with
making HSA work on this laptop.

Currently what I know for sure is that virtual Component Resource
Association Table (CRAT) table is created for CPU and GPU when the
driver is loaded (look the dmesg messages that I posted before). From
reading prints in kfd_crat.c file it looks that it is correct situation:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdkfd/kfd_crat.c#L1102

I don't see any other option than creation of virtual CRAT table there.
So probably the information from dmesg that "Virtual CRAT table created
for GPU" is not a symptom of a problem but information about correct
situation. (Disclaimer: I looked at this file for a few minutes only).


---

### 评论 #18 — gstoner (2016-12-17T19:19:32Z)

Ability to turn on IOMMUv2  as well

greg
On Dec 17, 2016, at 11:05 AM, Piotr Krysik <notifications@github.com<mailto:notifications@github.com>> wrote:

If I contact HP for updated BIOS it would be best to have 100% (or at
least 90%) proof that points to the BIOS as a source of problems with
making HSA work on this laptop.

Currently what I know for sure is that virtual Component Resource
Association Table (CRAT) table is created for CPU and GPU when the
driver is loaded (look the dmesg messages that I posted before). From
reading prints in kfd_crat.c file it looks that it is correct situation:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdkfd/kfd_crat.c#L1102

I don't see any other option than creation of virtual CRAT table there.
So probably the information from dmesg that "Virtual CRAT table created
for GPU" is not a symptom of a problem but information about correct
situation. (Disclaimer: I looked at this file for a few minutes only).

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/52#issuecomment-267773975>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuWTB92LBurPVlpMKpOGpiOfAnFIEks5rJBZMgaJpZM4LIpYt>.



---

### 评论 #19 — ptrkrysik (2016-12-17T20:24:59Z)

Regarding IOMMUv2 - the driver loads and doesn't inform that the IOMMUv2 functionality is not available. In dmesg I get:
AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>

Looking here:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/iommu/amd_iommu_v2.c#L953

in case IOMMUv2 was not supported I would get following messages:
AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
AMD IOMMUv2 functionality not available on this system

Summarizing: from dmesg message it seems that amdkfd configures CRAT tables correctly and IOMMUv2 driver is loaded correctly as well (no proof of lack of support for HSA in computer's BIOS here).

---

### 评论 #20 — gstoner (2016-12-17T20:35:00Z)

It switch in the system bios you have turn it on

Get Outlook for iOS<https://aka.ms/o0ukef>




On Sat, Dec 17, 2016 at 2:25 PM -0600, "Piotr Krysik" <notifications@github.com<mailto:notifications@github.com>> wrote:


Regarding IOMMUv2 - the driver loads and doesn't inform that the IOMMUv2 functionality is not available. In dmesg I get:
AMD IOMMUv2 driver by Joerg Roedel jroedel@suse.de<mailto:jroedel@suse.de>

Looking here:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/iommu/amd_iommu_v2.c#L953

in case IOMMUv2 was not supported I would get following messages:
AMD IOMMUv2 driver by Joerg Roedel jroedel@suse.de<mailto:jroedel@suse.de>
AMD IOMMUv2 functionality not available on this system

Summarizing: from dmesg message it seems that amdkfd configures CRAT tables correctly and IOMMUv2 driver is loaded correctly as well (no proof of lack of support for HSA in computer's BIOS here).

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/52#issuecomment-267784715>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuXY2NZFi7_d4WGflHX7xsb19owG0ks5rJEUcgaJpZM4LIpYt>.


---

### 评论 #21 — ptrkrysik (2016-12-17T20:47:19Z)

@gstoner, I don't have such switch in the computer's BIOS config, but (as I have written in the previous message) I don't have any indication that IOMMUv2 is not enabled by default already. To the contrary - the IOMMUv2 driver doesn't complain about unsupported hardware as it should if it was the case here:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/iommu/amd_iommu_v2.c#L952

---

### 评论 #22 — gstoner (2016-12-17T21:13:09Z)


By default the OEM have not turned on IOMMUv2  when running Windows 10.   You have  boot into the systems bios and via your keyboard toggle it on, you have to lucky enough to bios that let you toggle it on an off.  For Dell Inspiron Desktop with AMD FX 8800P for internal development system we had to chase Dell who handed us off to there ODM to fix the System BIOS.     Note we do not have these laptops in our Lab since we focused on Server and Workstation class systems primary.

I send a note to our HP sales person to see if there is anything that can be done with this bios.  But with the bigger companies it takes longer to get a response. if we can not get resolution I might just send you Fiji Nano so you can do development.

One  can go back and try original HSA Runtime and Driver on the HSA Foundation site  to see it works if that work then it issue in ROCm if does not work it is the CRAT TABLE and IOMMUv2.

One thing

Here are the system we publicly state have been tested with ROCm.
http://gpuopen.com/radeon-open-compute-new-era-heterogeneous-in-hpc-ultrascale-computing-the-boltzmann-initiative-delivering-new-opportunities-in-gpu-computing-research/

  *   Desktop Systems – Core i5 or Core i7, Xeon E3 V5
     *   ASUS X99-E WS with INTEL I7-5960X CPU
     *   ASUS Z97 PRO with i7-4790
     *   ASUS Z97-PRO(Wi-Fi ac)/USB 3.1 with i7-4790
     *   Supermicro SYS-5039a-iL with a Xeon E3 V5 – E3-1240V5 3.5G
  *   Workstation Intel Xeon E5 2640 v3  or E5 2667 v3
     *   Supermicro SYS-7038A-I
     *   Supermicro SYS-7048GR-TR

  *   Servers -Intel Xeon E5 2640 v3 or  E5 2667 v3
     *   Supermicro SYS-1028GQ-TRT
     *   Supermicro SYS-2028 GR-TRHT
     *   Supermicro SYS-7048GR-TR
     *   Inspur K888
     *   Dell C4130

We have AMD Ryzen CPU System and Naples Server CPU’s under test.
APU we do testing on development system that have controlled system bios

https://rocm.github.io/hardware.html

Hardware to Play ROCm
ROCm Platform Supports Two Graphics Core Next (GCN) GPU Generations

GFX7: Radeon R9 290 4 GB, Radeon R9 290X 8 GB, Radeon R9 390 8 GB, Radeon R9 390X 8 GB, FirePro W9100 (16GB), FirePro S9150 (16 GB) and FirePro S9170 (32 GB);

GFX8: Radeon RX 480, Radeon RX 470, Radeon RX 460,Radeon R9 Nano, Radeon R9 Fury, Radeon R9 Fury XRadeon Pro WX7100, Radeon Pro WX5100,Radeon Pro WX4100, and FirePro S9300 x2.

CPU support: ROCm requires CPUs with PCIe Gen3 atomics capability, such as the Intel Xeon E5v3 and newer Xeon processors. It also supports consumer CPUs, Intel Core i3, Intel Core i5, Intel Core i7 CPUs (v3 (Haswell) and newer).



On Dec 17, 2016, at 2:47 PM, Piotr Krysik <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner>, I don't have such switch in the computer's BIOS config, but (as I have written in the previous message) I don't have any indication that IOMMUv2 is not enabled by default already. To the contrary - the IOMMUv2 driver doesn't complain about unsupported hardware as it should if it was the case here:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/iommu/amd_iommu_v2.c#L952

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/52#issuecomment-267785763>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuZyy-bQ2yTvy_OS9xRT8pSHvUJwZks5rJEpYgaJpZM4LIpYt>.



---

### 评论 #23 — ptrkrysik (2016-12-27T22:45:28Z)

@gstoner, I managed to install original HSA runtime and kernel. The result I got is better than what I got for ROCm installed from packages. This is the output or the vector_copy example:

Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name failed.

For original HSA Runtime and driver vector_copy example went pass HSA initialization. There seems to be some regression in ROCm that makes it segfault on HSA init that worked before.

again: can anyone tell if current ROCm installed from packages workes without segfault on any harware configuration? It would be helpful to know this.

Can you tell me if the result I got proves that IOMMUv2 is turned on in the computer's BIOS or not?

---

### 评论 #24 — gstoner (2016-12-27T23:41:05Z)

It failed

Get Outlook for iOS<https://aka.ms/o0ukef>




On Tue, Dec 27, 2016 at 4:45 PM -0600, "Piotr Krysik" <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner>, I managed to install original HSA runtime and kernel. The result I got is better than what I got for ROCm installed from packages. This is the output or the vector_copy example:

Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name failed.

For original HSA Runtime and driver vector_copy example went pass HSA initialization. There seems to be some regression in ROCm that makes it segfault on HSA init that worked before.

again: can anyone tell if current ROCm installed from packages workes without segfault on any harware configuration? It would be helpful to know this.

Can you tell me if the result I got proves that IOMMUv2 is turned on in the computer's BIOS or not?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/52#issuecomment-269393564>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duf7_N6ieJgOnEkl0G1yGQL82HXDCks5rMZUIgaJpZM4LIpYt>.


---

### 评论 #25 — ptrkrysik (2016-12-29T11:58:51Z)

@gstoner, I'm aware that the test failed. What I need to know is if the fact that it failed later than before (after HSA initialization) gives any information regarding the source of the problem. Is it BIOS from HP for 100% or not?

---

### 评论 #26 — ptrkrysik (2017-01-03T08:09:18Z)

@gstoner and other AMD/ATI developers here, I want to point you to a brochure from HP/AMD that advertises HP 725/745/755 G3 laptops as supporting HSA:
http://www.amd.com/Documents/2015-HP-Discover-03.pdf

 "Revolutionary new HSA technology enables the CPU and GPU to work cooperatively, in parallel, to unlock the full potential of your business PC. " - this is just one of the quotes in which HSA support in these laptops is advertised. It is information like this and other that could be found on AMD website (search for: amd hsa hp g3 , to get other examples) that led me to choose HP 725 G3 laptop in order to give a try to AMD HSA.

In the event that AMD/HP decided that it doesn't support HSA in these HP laptops despite advertising opposite - this would be not only grossly disappointing but also it is a good method to permanently lose some customers.

---

### 评论 #27 — gstoner (2017-01-03T18:29:42Z)

Happy New Year,  now we all back in the office post the holiday break.  Underststand we stated ROCm is focused on Server Based Computing, it was not released as a driver for  our general consumer products which our APU.   Note we were very restrictive of what we did and did not support at launch.    This is the original blog.   Over time we have been relaxing which ASIC we support,  with is posted on ROCm website.    On Carizzo APU support, we test it on our internal development boards which has the SBIOS set correctly.  We do not have access to every system on the market, we have been publishing known tested systems for ROCm that we can support.  Even with this I will first see if I can get access to this Laptop to check to see if the BIOS is correctly setup since. you can not confirm IOMMUv2 is working nor it has proper CRAT table.

Note Because ROCm is designed for server it is a headless driver. Which means it meant to be run without X11 and run console only mode.  OpenGL will be support on EGL in headless mode as well.

Note OpenCL 2.0 via  SVM and Atomics on windows and Linux support HSA capabilities.


ROCm: Platform For A New Era of Heterogeneous in HPC and Ultrascale Computing
Posted on January 26, 2016 by Greg Stoner
 Boltzmann Initiative<http://gpuopen.com/tag/boltzmann-initiative/>, HCC Compiler<http://gpuopen.com/tag/hcc-compiler/>, HIP<http://gpuopen.com/tag/hip/>, HPC<http://gpuopen.com/tag/hpc/>, HSA<http://gpuopen.com/tag/hsa/>, OpenGL<http://gpuopen.com/tag/opengl/>, ROC<http://gpuopen.com/tag/roc/>

The ROCm Platform Deliver on the Vison of the  Boltzmann Initiative,  Bringing a New Opportunities in GPU Computing Research

On November 16th, 2015, the Radeon Technology Group rolled out Boltzmann Initiative with three core foundation elements:

  *   New Linux(R) Driver and Runtime Stack optimized for HPC & Ultra scale class computing,
  *   Heterogeneous C and C++ compiler which best address the whole system not just a single device
  *   HIP acknowledging the need for platform choice when utilizing GPU computing API

Today the Radeon Technology Group is releasing a preview version of the ROCm  which contains the ROCm Kernel  driver (ROCK-Kernel-Driver<https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver>) and ROCm runtime (ROCR-Runtime<https://github.com/RadeonOpenCompute/ROCR-Runtime>), allowing the exploration of what is possible with the open GPU computing foundation. The objective of this release is to start a dialog with the commercial and academic HPC communities that will shape the future direction of the Boltzmann Initiative, both for the coming year and beyond.

We are excited to present to you our first public release of the Boltzmann driver and runtime with HCC and HIP.

Using our knowledge of the HSA Standards<http://www.hsafoundation.com/html/HSA_Library.htm> and, more importantly, the HSA 1.0 Runtime<http://www.hsafoundation.com/html/HSA_Library.htm#Runtime/Topics/Runtime_title_page.htm%3FTocPath%3DHSA%2520Runtime%2520Programmer%25E2%2580%2599s%2520Reference%2520Manual%2520Version%25201.0%2520%7C_____0> we have been able to successfully extended support to the dGPU with critical features for NUMA class acceleration. As a result, the ROCK driver is composed of several components based on our efforts to develop the Heterogeneous System Architecture for APUs, including the new AMDGPU driver, the Kernel Fusion Driver (KFD), the HSA+ Runtime and an LLVM based compilation stack for the building of key language support. This support starts with AMD’s FIJI Family of dGPU, but support is planned to expand in the future to include future ASICS.

Key Features in this release:

  *   User Mode Queues
  *   User Mode DMA
  *   Coarse-grain Shared Virtual Memory
  *   Multi-GPU Enablement
  *   HSA Signals and Atomics (Using PCIe Gen3 Platform Atomics)
  *   HCC Compiler <https://gpuopen.com/compute-product/hcc-heterogeneous-compute-compiler/> with C & C++ Support with Parallel STL
  *   HIP Runtime<https://gpuopen.com/compute-product/hip-convert-cuda%E2%80%A6-portable-c-code/>
     *   HIP: C++ Heterogeneous-Compute Interface for Portability
  *   Supports Mesa X11 and OpenGL for Development Workstations

Initial Target Platform Requirements

  *   CPU: Intel Haswell or Newer, Core i5, Core™ i7; Xeon E3 v4 & v5; Xeon E5 v3
  *   GPU currently we only support Fiji ASIC which is in the AMD R9 Nano, R9 Fury x and R9 Fury

  *   We will be adding unique AMD CPU devices in the future

With this release to help the developer get more comfortable with ROCK  driver and the ROCR API and tools, the default mode is supporting Mesa X11 and OpenGL.

This introductory development platform will enable programmers to become familiar with the environment, configuration and tools available with the Boltzmann driver.

Future releases are planned to include exciting new feature, including:

  *   Peer to Peer Multi-GPU supports with Large Bar support
  *   GPU enabled Peer to Peer with RDMA support for Mellanox and Chelsio Network cards
  *   HCC built on the Lighting Compiler with Native GCN ISA code generation
  *   GCN ISA Assembler and Disassembler
  *   Process Concurrency & Preemption
  *   System Manageability Tools

Since this is an early access release and we are still in development towards the production ready version ROCK driver and ROCR runtime we recommend this version of the Radeon Open Compute platform for research and early application development, and we recommend it only on a test clusters until the final release.

Also being released are key math libraries that support the HCC compiler and runtime. These include HcBLAS<https://gpuopen.com/compute-product/hcblas/>, HcFFT<https://gpuopen.com/compute-product/hcfft/>, HcSparse, and HcRNG. We are also releasing a number sample applications that showcase the abilities of the ROCK runtime/driver with HCC and HIP in the Deep Neural Networks and Molecular Dynamics application domain.

Current systems the ROCR runtime have been tested on which also support PCIe Large BAR needed for Peer to Peer and RDMA support.

  *   Desktop Systems – Core i5 or Core i7, Xeon E3 V5
     *   ASUS X99-E WS with INTEL I7-5960X CPU
     *   ASUS Z97 PRO with i7-4790
     *   ASUS Z97-PRO(Wi-Fi ac)/USB 3.1 with i7-4790
     *   Supermicro SYS-5039a-iL with a Xeon E3 V5 – E3-1240V5 3.5G
  *   Workstation Intel Xeon E5 2640 v3  or E5 2667 v3
     *   Supermicro SYS-7038A-I
     *   Supermicro SYS-7048GR-TR

  *   Servers -Intel Xeon E5 2640 v3 or  E5 2667 v3
     *   Supermicro SYS-1028GQ-TRT
     *   Supermicro SYS-2028 GR-TRHT
     *   Supermicro SYS-7048GR-TR

As we kick off the program, we would like to thank three partners that were instrumental in making this release possible: First is MultiCoreWare, who was instrumental in getting HCC, HcMath libraries and HcTorch7 and HcCaffe to market.  Also, Continuum Analytics, Anaconda with Numba which accelerates Python running on ROCK enabled DGPU’s and HSA enabled APU devices is delivery amazing results. Supermicro for working with us closely on server hardware and bios optimization.

We are looking forward to engaging with the community with a new foundation for HPC, Ultrascale, and Academic Research GPU Computing Initiatives and see what you create in the coming year.

GitHub Links to the driver and runtime.

  *   ROCm Kernel Driver <https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver>
  *   ROCm Runtime <https://github.com/RadeonOpenCompute/ROCR-Runtime>
  *   ROCm Thunk Interface<https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface>

Gregory Stoner is Senior Director Radeon Open Compute at AMD. Links to third party sites and references to third party trademarks are provided for convenience and illustrative purposes only. Unless explicitly stated, AMD is not responsible for the contents of such links, and no third party endorsement of AMD or any of its products is implied.

This is what we are publicly stating we support on ROCM website https://rocm.github.io/hardware.html
Hardware to Play ROCm
ROCm Platform Supports Two Graphics Core Next (GCN) GPU Generations

GFX7: Radeon R9 290 4 GB, Radeon R9 290X 8 GB, Radeon R9 390 8 GB, Radeon R9 390X 8 GB, FirePro W9100 (16GB), FirePro S9150 (16 GB) and FirePro S9170 (32 GB); strong half-rate double-precision performance

GFX8: Radeon RX 480, Radeon RX 470, Radeon RX 460,Radeon R9 Nano, Radeon R9 Fury, Radeon R9 Fury XRadeon Pro WX7100, Radeon Pro WX5100,Radeon Pro WX4100, and FirePro S9300 x2; revolutionary HBM memories with 512 GB/s per ASIC. Currently the highest efficiency at 46 Gflops/watt. The R9 Nano delivers 8 Tflops and the S9300x2 delivers a solid 13.9 Tflops of single-precision performance to attack machine-learning, molecular-dynamics, energy and signal-processing problems.

Supported CPU's

ROCm Platform Leverage PCIe Atomics (Fetch ADD,Compare and SWAP, Unconditional SWAP, AtomicsOpCompletion) To find out more about PCIe atomics<https://github.com/RadeonOpenCompute/RadeonOpenCompute.github.io/blob/master/ROCmPCIeFeatures.md> which are only supported on PCIe Gen3 Enabled CPU's and PCIe Gen3 Switches like Broadcom PLX. When you install your GPU's Make sure you install them on real PCIe Gen3 x16 or x8 lanes directly on CPU's Root I/O controller or PCIe Switch directly attached to the CPU's Root I/O controller. We have seen many issue with Consumer motherboard which support Physical x16 Connectors, but the connector is electrically connected as PCIe Gen2 x4, if you see this it is typically hanging off the Southbridge PCIe I/O controller. If you mother is configured this way please do not use this connector for your GPU's..

Current CPU which support PCIe Gen3 + PCIe Atomics are:

  *     Intel Xeon E5 v3 or newer CPU's
  *     Intel Xeon E3 v3 or newer CPU's
  *    Intel Core i7 v3, Core i5 v3, Core i3 v3 or newer CPU's
  *    AMD Ryzen CPU's
  *    AMD Naples Server CPU
  *    Cavium Thunder X Server Processor

GPU Support of PCIe Atomics

  *   Our GFX8 GPU's ( FIJI &  Polaris Familiy) use PCIe Gen 3 and PCIe Atomics

  *   Our GF7 GPU's Radeon R9 290, R9 390, AMD FirePro S9150, S9170 do not support PCIe Atomics. For these GPU's we still recommend PCIe Gen3 enabled CPU's.

Not Supported or Very Limited Support Under ROCm

  *   We do not support ROCm with PCIe Gen 2 enabled CPU's such as the AMD Opteron, Phenom, Phenom II, , Athlon, Athlon X2, Athlon II and Older Intel Xeon and Intel Core Architecture and Pentium CPU's.
  *   We also do not support AMD Carrizo and Kaveri APU with external GPU Attached are not supported by ROCm
  *   Thunderbolt 1 and 2 enabled GPU's are not Support by ROCm.  Thunderbolt 1 & 2 are PCIe Gen2 based.
  *   AMD Carrizo based APU have limited support due to OEM & ODM's Carrizo enabled Laptop, All In One System and Desktop system had inconsistency in supporting the correct System BIOS configurations for ROCm driver enablement. Before you buy a Carrizo system to run ROCm.  You should check the SBIOS to see if has an option to enable IOMMUv2. If this is enabled, next we need test for the correct CRAT Table support to properly configure the driver.

Potential Future APU Support

I know many of you are looking forward to support ROCm on APU system which support Fine Grained Shared Virtual Memory and cache coherency between the CPU and GPU. In the 2017 we plan on testing commercial AM4 Socketed Bristol Ridge and Raven Ridge motherboard. Just like we still waiting to get access to them, once we get our first board we blog about the experience and begin building up a list of motherboard that are qualified with ROCm

More Information on ROCm-Supported Server-Capable Hardware
FirePro S9150

  *   Single precision (Float32): 5.07 Tflops
  *   Double precision (Float64): 2.53 Tflops
  *   16 GB GDDR5 512-bit bus at 320 GB/s with ECC
  *   225 watts
  *   S9150 information<http://www.amd.com/en-us/products/graphics/workstation/firepro-remote-graphics/s9150>
  *   S9150 datasheet<http://www.amd.com/Documents/firepro-s9150-datasheet.pdf>

FirePro S9170

  *   Single precision (Float32): 5.24 Tflops
  *   Double precision (Float64): 2.62 Tflops
  *   32 GB GDDR5 512-bit bus at 320 GB/s with ECC
  *   275 watts
  *   S9170 information<http://www.amd.com/en-us/products/graphics/server/s9170>
  *   S9170 datasheet<http://www.amd.com/Documents/AMD-FirePro-S9170-Datasheet.pdf>

FirePro S9300 X2

  *   Half precision (Float16): 13.9 Tflops
  *   Single precision (Float32): 13.9 Tflops
  *   Double precision (Float64): 0.87 Tflops
  *   8 GB of HBM1 Memory at 1 TB/s (2x 512 GB/s)
  *   300 watts
  *   S9300 X2 information<http://www.amd.com/en-us/products/graphics/server/s9300-x2>
  *   S9300 X2 datasheet<http://www.amd.com/Documents/s9300-x2-datasheet.pdf>

Radeon R9 Nano

  *   Half precision (Float16): 8.19 Tflops
  *   Single precision (Float32): 8.19 Tflops
  *   Double precision (Float64): 0.511 Tflops
  *   4 GB HBM1 memory at 512 GB/s
  *   175 watts
  *   46 Gflops/watt (single precision)
  *   R9 Nano information<http://www.amd.com/en-us/products/graphics/desktop/r9>


On Jan 3, 2017, at 2:09 AM, Piotr Krysik <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> and other AMD/ATI developers here, I want to point you to a brochure from HP/AMD that advertises HP 725/745/755 G3 laptops as supporting HSA:
http://www.amd.com/Documents/2015-HP-Discover-03.pdf

"Revolutionary new HSA technology enables the CPU and GPU to work cooperatively, in parallel, to unlock the full potential of your business PC. " - this is just one of the quotes in which HSA support in these laptops is advertised. It is information like this and other that could be found on AMD website (search for: amd hsa hp g3 , to get other examples) that led me to choose HP 725 G3 laptop in order to give a try to AMD HSA.

In event that AMD/HP decided that it doesn't support HSA in these HP laptops despite advertising opposite - this would be not only grossly disappointing but also it is a good method to permanently lose some customers.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/52#issuecomment-270066163>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuayJGvBX97PBp6_5EbX3IGy4ISCCks5rOgIvgaJpZM4LIpYt>.



---

### 评论 #28 — ptrkrysik (2017-02-22T21:05:53Z)

This problem wasn't really solved. At least some comment before closing
it would be nice.

You can conclude that AMD has ended the short life of HSA support for
Carrizzo APUs in laptops (which might be true, as you admitted you don't
have laptops in your lab). This is a bit sad answer, but I can live with
it. Such admission might act as a warning for others who get too much
excited about AMD's announcement of cool new technologies, so they won't
be as easily mislead by advertisements.

Saying that it is HP's BIOS fault that HSA is not working and directing
me to contact HP for a proof is a total non-solution. HP even doesn't
have a procedure for asking such question. There is no way I can get in
contact with a person in HP who can solve this problem or show me a
proof that everything is fine on their side.


---

### 评论 #29 — jedwards-AMD (2017-02-22T21:45:35Z)

I understand your frustration, but it is misdirected. You must understand that HSA support on Carrizo has nothing to do with the ROCm project or the platforms ROCm is targeting. The HSA Runtime is an open source project, and is still available on the HSA GitHub website if you would like to continue to use it. Unfortunately, to properly support Carrizo APUs with HSA on every platform requires system manufacturer to pick up the CRAT specification. If the system integrators did not add that table to the BIOS there isn't much AMD can do about it. This is not a problem with ROCm. AMD controls all of the firmware and software components and doesn't have to rely on system integrators to create special configuration tables in the BIOS.

Greg Stoner's post has provided you with ROCm supported platforms and ASICS.

---

### 评论 #30 — gstoner (2017-02-23T02:45:20Z)

I am willing to send you a Fiji nano as replacement gpu. If you feel this will remedy your issue.

G

Get Outlook for iOS<https://aka.ms/o0ukef>




On Wed, Feb 22, 2017 at 1:06 PM -0800, "Piotr Krysik" <notifications@github.com<mailto:notifications@github.com>> wrote:

This problem wasn't really solved. At least some comment before closing
it would be nice.

You can conclude that AMD has ended the short life of HSA support for
Carrizzo APUs in laptops (which might be true, as you admitted you don't
have laptops in your lab). This is a bit sad answer, but I can live with
it. Such admission might act as a warning for others who get too much
excited about AMD's announcement of cool new technologies, so they won't
be as easily mislead by advertisements.

Saying that it is HP's BIOS fault that HSA is not working and directing
me to contact HP for a proof is a total non-solution. HP even doesn't
have a procedure for asking such question. There is no way I can get in
contact with a person in HP who can solve this problem or show me a
proof that everything is fine on their side.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/52#issuecomment-281803845>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudCH-j0iw7NPMKR6AlBrzAWjcavfks5rfKMxgaJpZM4LIpYt>.


---

### 评论 #31 — ptrkrysik (2017-02-24T08:32:40Z)

@gstoner, our aim was mainly to check how shared virtual memory provided
by AMD APUs can simplify implementation of algorithms working both on
CPU and GPU cores.

However, we can accept the solution offered by you, as it will let us
test the tools that (hopefully) will fully support APUs in the future.

How can we get in contact? My e-mail address is ptrkrysik@gmail.com.



---

### 评论 #32 — ptrkrysik (2017-03-15T20:41:54Z)

I would like to let know everybody who might read this thread that I got
Fiji nano card offered as a replacement by Gregory Stoner. The card
works and with it I'm able to run sample codes distributed with ROCm.


---

### 评论 #33 — gstoner (2017-03-15T20:43:56Z)

Your welcome..   We have new release coming lots of great updates . 

---
