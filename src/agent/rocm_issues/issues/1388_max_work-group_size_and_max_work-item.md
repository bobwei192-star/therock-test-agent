# max work-group size and max work-item

> **Issue #1388**
> **状态**: closed
> **创建时间**: 2021-02-20T13:01:43Z
> **更新时间**: 2021-02-25T15:10:40Z
> **关闭时间**: 2021-02-25T15:10:40Z
> **作者**: zjin-lcf
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1388

## 描述

 clinfo shows the following info for AMD GPUs. Is it right ?  
 
```
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
   Max work group size:                           256
```
Thanks


---

## 评论 (11 条)

### 评论 #1 — seesturm (2021-02-20T13:19:05Z)

Not sure what is actually asked here but maybe the comments in #330 give answers.

---

### 评论 #2 — zjin-lcf (2021-02-20T13:35:26Z)

Thank you for  your quick reply.  Since it is *max* work group size,  could AMD people replace 256 with 1024 ?  

The runtime returns INVALID_WORK_GROUP_SIZE error when the work-group size of a kernel is, for example, 1000.  Must a user modify his/her program or can the AMD OpenCL runtime/driver handle the issue transparently ?   

Running such kernel on an Nvidia GPU does not have such problem.  On an Intel GPU, the max work-group size is, for example, 256. Then it makes sense that a user will need to set the work-group size appropriately. 

---

### 评论 #3 — ROCmSupport (2021-02-22T06:34:37Z)

I would say that you should look at the Max work items[] outputs of clinfo to understand the maximum work items that the hardware limits you to. This is found by querying each of the dimensions of CL_DEVICE_MAX_WORK_ITEM_SIZES.

In reality, there are multiple limits in play, and that's why it's a bit non-clear exactly what to report for "max work group size". 
However, if we reported the maximum work group size as 1024, and then the runtime failed when you tried to enqueue a kernel with 512 threads per workgroup, we would get many complaints about the runtime being broken. So we are ok to keep "max work group = 256" description.

I recommend you to set local_work_size to NULL., wherever needed, which solves your problem.

The current ROCm OpenCL runtime allows you to set local_work_size to NULL and it will run with the reqd_work_group_size() of > 256 threads. You can also set local_work_size to the same dimensions as your reqd_work_group_size() attribute and it will work. (e.g. setting local_work_size={1024,1,1} and reqd_work_group_size(1024,1,1)). If you don't set reqd_work_group_size(), however, requesting local_work_size={1024,1,1} will fail.

---

### 评论 #4 — ROCmSupport (2021-02-22T06:35:27Z)

Hi @zjin-lcf ,
Please let me know if you still have doubts on this.
Thank you.

---

### 评论 #5 — zjin-lcf (2021-02-22T12:37:55Z)

The runtime should not fail in the first place when a user requests a work-group size of 512.

Thanks.

---

### 评论 #6 — ROCmSupport (2021-02-24T08:09:52Z)

Hi @zjin-lcf 
Can you please share your code so that I will check and get back.
Thank you.

---

### 评论 #7 — gandryey (2021-02-24T16:14:11Z)

> The runtime should not fail in the first place when a user requests a work-group size of 512.

- Runtime will fail a launch with 512 if the compiled kernel can't be executed with 512.
- In order to execute a kernel with a workgroup size > 256, the application has to 
   - use __attribute__((work_group_size_hint(X, Y, Z))) to specify the desired workgroup size, so the compiler can generate appropriate code
   - call clGetKernelWorkGroupInfo() with CL_KERNEL_WORK_GROUP_SIZE or/and CL_KERNEL_COMPILE_WORK_GROUP_SIZE to find out the allowed workgroup size

---

### 评论 #8 — zjin-lcf (2021-02-24T16:29:21Z)

I understand that a user may just do with whatever a vendor offers. 

When the work-group size of a kernel is 1000, an Nvidia GPU can launch it successfully. So ROCM will also launch the kernel successfully as long as a user 
1. set a NULL value for work-group size in a host program  OR
2. use attribute((work_group_size_hint(X, Y, Z))) to specify the desired workgroup size (i.e. 1000) in a kernel, and specify the same value (i.e. 1000) in a host program

option 1 suggests that your runtime select a work-group size.

Is that right ?

Thanks





---

### 评论 #9 — gandryey (2021-02-24T16:59:51Z)

I'm not very familiar with NV HW. AMD can launch 1024 also, but we can't compile a kernel optimally to satisfy that requirement. Basically only 256 is possible always and anything bigger will introduce the pressure on VGPRs. 256 VGPRs are available always for <=256, but if the app wants to launch 512, then it's 128 VGPRs and 1024 - 64 VGPRs respectively. 
Compiler can't assume 1024 by default, because that would require to limit VGPRs to 64 and potentially cause a spill. Hence we let the developers to decide the optimal workgroup size.

1. NULL option will choose 256 by default or the compiled workgroup, the app specified with attribute((work_group_size_hint(X, Y, Z))) 
2. That is correct. The app can force 1024 in compilation and then send the same size from the host.

There is no real advantage to have >256 workgroup size, unless the kernel is specially written to use local/shared memory and/or local/shared memory usage is more important than the pressure of VGPRs.  

---

### 评论 #10 — ROCmSupport (2021-02-25T07:34:48Z)

Hi @zjin-lcf 
Request you to try as suggested by @gandryey and share an update.
Thank you.

---

### 评论 #11 — zjin-lcf (2021-02-25T15:10:40Z)

I will close the issue. Thank you for your answers. 

---
