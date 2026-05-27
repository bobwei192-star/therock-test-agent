# Bristol ridge support

> **Issue #122**
> **状态**: closed
> **创建时间**: 2017-05-16T14:11:26Z
> **更新时间**: 2017-07-01T21:40:35Z
> **关闭时间**: 2017-07-01T21:40:35Z
> **作者**: trinayan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/122

## 描述

Hi,

Thanks for all the great work with ROCM. 
I wanted to know what Bristol Ridge boards are supported by ROCM. I heard of some HP and Lenovo laptops shipping with them as well as some desktop parts. Any recommended boards that the developers have experience with? 


Best,
Trinayan

---

## 评论 (5 条)

### 评论 #1 — trinayan (2017-05-18T22:03:09Z)

Any info on this matter? Thanks

---

### 评论 #2 — gstoner (2017-05-18T23:35:10Z)

I was told this one works by HSA Foundation President 
HP Pavilion - 15z Touch Laptop
Product number: V1M95AV

---

### 评论 #3 — trinayan (2017-05-19T02:44:46Z)

Thanks a lot. I am trying to do some frequency scaling experiments on heterogeneous architectures. Currently I use a Jetson but an APU will be the best target for this work if it allows different memory frequency, gpu frequencies. You mentioned before that rocm-smi does not support Carrizzo . So I am wondering if this APU has some support for frequency scaling or not on ROCM. If it has it will be the best device for my work. It would be very helpful if someone in your lab can verify this before I buy the product. Thanks for the help again.

---

### 评论 #4 — glossner (2017-05-28T13:41:50Z)

I can confirm the vector add sample works on the HP 15t V1M95AV laptop. It is also on sale for memorial day (I have no affiliation with HP or AMD. I am President of HSAF).

glossner@glossner-HSA-HP-Pavillion:/opt/rocm/hsa/sample$ ./vector_copy 
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx801.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
Passed validation.
Freeing kernel argument memory buffer succeeded.
Destroying the signal succeeded.
Destroying the executable succeeded.
Destroying the code object succeeded.
Destroying the queue succeeded.
Freeing in argument memory buffer succeeded.
Freeing out argument memory buffer succeeded.
Shutting down the runtime succeeded.



---

### 评论 #5 — gstoner (2017-07-01T21:40:35Z)

HSA President reported 1.6 is working on the HP Laptop 

---
