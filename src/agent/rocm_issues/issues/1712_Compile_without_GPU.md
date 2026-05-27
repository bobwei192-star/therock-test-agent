# Compile without GPU?

> **Issue #1712**
> **状态**: closed
> **创建时间**: 2022-03-21T06:46:29Z
> **更新时间**: 2024-02-02T16:31:16Z
> **关闭时间**: 2024-02-02T16:31:15Z
> **作者**: xlindo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1712

## 描述

I am working on the ported stuff for RISC-V, and now stucked in the compilation of ROCR-Runtime.

Could anyone please tell me that if it is necessary to compile ROCm with an existing supported GPU? If not, please tell me the files I need to modify, and then compile without a GPU.

Thanks!

---

## 评论 (12 条)

### 评论 #1 — xlindo (2022-03-24T09:57:15Z)

@xuhuisheng 
Can you help me?

---

### 评论 #2 — xuhuisheng (2022-03-24T10:25:11Z)

@xlindo Actually, I didnot need gpu to run build scripts. So what error do you meet?

---

### 评论 #3 — xlindo (2022-03-31T11:46:07Z)

> @xlindo Actually, I didnot need gpu to run build scripts. So what error do you meet?

Thanks for your information.

I have also just compiled the project successfully with your scripts. 

But it may not work without a GPU.

So, if a GPU is necessary for programming or working with ROCm?

If not, how to modify these stuff, i.e. program and run with CPU only.

Thanks.

---

### 评论 #4 — xuhuisheng (2022-03-31T13:01:26Z)

No, You cannot run ROCm without a GPU.
The aim of ROCm is speed up computing ML. There is no reason to run HIP on CPU.

But, if you are interest in hip-cpu, I think you can have a look at <https://github.com/ROCm-Developer-Tools/HIP-CPU>
I havn't test it before, not sure whether it can run properly.

---

### 评论 #5 — xlindo (2022-03-31T13:19:01Z)

@xuhuisheng 

Thanks for your advice.

Yes, I am actually testing HIP-CPU.

But it seems that the upper components like **MIOpen is not possible running upon it solely**? Since the lower components for MIOpen must be ROCm, and ROCm relies on GPU.

---

### 评论 #6 — xlindo (2022-04-01T03:22:59Z)

@xuhuisheng 

I am working on RISC-V accelerator.

I want to use the fundamentals of the whole ROCm for CPU(RISC-V), heterogenuous CPU(multiple RISC-V) or CPU+GPU. And then optimize the pipeline.

First of all, I want to compile ROCm runtime. But I am not sure if ROCm on RISC-V solely works or not.

---

### 评论 #7 — xlindo (2022-04-01T07:23:44Z)

@xuhuisheng 

In short, could you please tell me how to add a new device to ROCm?

Thanks a lot!



---

### 评论 #8 — xuhuisheng (2022-04-01T07:54:48Z)

It is hard to say.
ROCm use roct-thunk-interface to fetch device information for drm. for my background, I cannot understand the driver codes, althought it is opensource.
And there could be some closesource codes in firmware.

So I will believe, you can try to imple your aql. Emm~, there was a hsafoudation, which is founded by AMD, apple, and I think OpenCL is part of it. Last year, the website had been shutdown, So I cannot show you the pdf.

---

### 评论 #9 — xlindo (2022-04-01T08:25:52Z)

@xuhuisheng 

Great information. Thanks.

I will try, even it looks like hard.

---

### 评论 #10 — xuhuisheng (2022-04-01T08:28:11Z)

Here is hsafoundation website : <https://hsafoundation.com/>, wish it could help

---

### 评论 #11 — abhimeda (2024-01-25T03:29:18Z)

@xlindo Hi, is your issue resolved in the latest ROCm? If so can we close this ticket?

---

### 评论 #12 — xlindo (2024-02-02T16:31:15Z)

> thx, but sorry I cannot answer since I am not working on it now

thx, but sorry I cannot answer since I am not working on it now

---
