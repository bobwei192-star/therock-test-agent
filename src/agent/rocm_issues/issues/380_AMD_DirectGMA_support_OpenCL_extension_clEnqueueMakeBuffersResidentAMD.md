# AMD DirectGMA support ? OpenCL extension clEnqueueMakeBuffersResidentAMD ?

> **Issue #380**
> **状态**: closed
> **创建时间**: 2018-04-04T09:49:13Z
> **更新时间**: 2018-05-12T13:09:19Z
> **关闭时间**: 2018-05-12T13:09:19Z
> **作者**: raph38130
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/380

## 描述

Dear all,

does RoCM amdgpu driver actually support DirectGMA ? I can compile but have error in clEnqueueMakeBuffersResidentAMD .
I don't see cl_amd_bus_addressable_memory extension with clinfo ?

in this code 1st line is ok
2nd line fired ERROR


`cl_mem busAddressableBuff_ = clCreateBuffer(context, CL_MEM_BUS_ADDRESSABLE_AMD, 1*1024, 0, &err);
if(err)printf(" error CL_MEM_BUS_ADDRESSABLE_AMD %d\n",err);
 // Get physical address
err = clEnqueueMakeBuffersResidentAMD(queue, 0, &busAddressableBuff_, true, &busAddr_, 0,0,0);
if(err)printf(" ERROR clEnqueueMakeBuffersResidentAMD%d\n",err);`

best regards

---

## 评论 (7 条)

### 评论 #1 — gstoner (2018-04-04T16:12:52Z)

No, it does not. Rocm supports p2p via native foundation in the driver.  Also, there is p2p API now in OpenCL


________________________________



---

### 评论 #2 — raph38130 (2018-04-04T16:20:36Z)

okay
so what is the recommended solution to push data via DMA (either from  FPGA or a mellanox RNIC)  into the GPU ?

---

### 评论 #3 — gstoner (2018-04-04T16:37:57Z)

 Mellonox NIC never was. supported via DirectGMA,  since it did not support RDMA and Peer Direct.   We now have native support in the driver for PeerDirect  (  https://community.mellanox.com/docs/DOC-2486 ) and RDMA

Please look at this documentation on how we support Mellanox

http://rocm-documentation.readthedocs.io/en/latest/Remote_Device_Programming/Remote-Device-Programming.html.  With 1.7.1 all this is working on Intel,  We found issue in base driver with offset how it was set up that impacted EPYC,  with 1.7.2 which will be out soon this working EPYC as well.

We support FPA via number of different solution,  Persistent Kernel,  there is longer term solution to support user mode queues to dispatch work to the FPGA

Greg




---

### 评论 #4 — gstoner (2018-04-04T16:45:51Z)

One thing we have been doing research via the HSA Foundation on with FPGA is libHSA. http://ieeexplore.ieee.org/document/8122108/ 

Abstract:
Various signal and image processing applications require vast acceleration in order to enable real-time processing and meet constraints in power consumption. On FPGAs these applications can be implemented as application-specific circuit. Although IP cores for various applications exist, even interfacing these usually requires experienced knowledge in hardware design. Using FPGAs or other accelerators in a heterogeneous system from a host CPU would simplify the usage of accelerator hardware for a common software developer. Recognizing this, several companies and partners from academia created the HSA Foundation (Heterogeneous System Architecture Foundation) to define a platform specification for heterogeneous system requirements as a macro-architecture for efficient and easy targeting heterogeneous processors from popular high-level languages like C/C++, Python, Java and other domain specific languages. In this paper we present an IP library (LibHSA), that greatly simplifies integration of hardware accelerator functions into existing HSA compliant systems. This allows accelerators to take advantage of the existing HSA programming model, libraries, compilers and toolchains. We will demonstrate the work of LibHSA utilizing a programmable image processor implementation on a Xilinx FPGA. The image processor supports low-level algorithms, e.g. Sobel, Median, Laplace, or Gauss. Our results show a substantial decrease integrating customized hardware accelerators using the LibHSA infrastructure. To our knowledge, our library is the first approach for integrating reconfigurable hardware into an HSA compliant system.
Published in: Design and Architectures for Signal and Image Processing (DASIP), 2017 Conference on

---

### 评论 #5 — preda (2018-04-04T22:17:31Z)

@gstoner: could you please post a link to the libHSA paper that does not require "IEEE purchase", non-member $33 for the PDF !?

---

### 评论 #6 — gstoner (2018-04-04T23:20:39Z)

I was looking on Google I can not find one.  I can ask the authors 


---

### 评论 #7 — Styx85 (2018-04-08T11:14:11Z)

You can request it directly from the author via [ResearchGate](https://www.researchgate.net/publication/321400291_LibHSA_One_step_towards_mastering_the_era_of_heterogeneous_hardware_accelerators_using_FPGAs) or if it is allowed in your country of residence access it directly via [Sci-Hub](http://sci-hub.tw)

---
