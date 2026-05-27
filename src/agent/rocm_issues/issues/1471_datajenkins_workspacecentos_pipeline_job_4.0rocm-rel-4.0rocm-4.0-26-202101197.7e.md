# /data/jenkins_workspace/centos_pipeline_job_4.0/rocm-rel-4.0/rocm-4.0-26-20210119/7.7/external/hip-on-vdi/rocclr/hip_code_object.cpp:120: guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")

> **Issue #1471**
> **状态**: closed
> **创建时间**: 2021-05-12T13:20:35Z
> **更新时间**: 2021-05-31T09:42:19Z
> **关闭时间**: 2021-05-31T09:42:19Z
> **作者**: X-ailsa
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1471

## 描述

*(无描述)*

---

## 评论 (4 条)

### 评论 #1 — xuhuisheng (2021-05-12T14:15:27Z)

I suggest to check if there is a gfx03 - RX580 issue.
https://github.com/xuhuisheng/rocm-build/tree/master/gfx803

I found the error message is exactly the same with Pytorch on gfx803.
https://github.com/xuhuisheng/rocm-build/tree/master/gfx803#pytorch-181-crashed-on-gfx803

Please execute `/opt/rocm/bin/rocminfo` to confirm GPU ASIC. Only a few GPU are supported by ROCm.

---

### 评论 #2 — X-ailsa (2021-05-15T09:43:45Z)

GPU: Radeon RX 580 Series
The version of pytorch installed on my computer: torch==1.8.1+rocm4.0.1
Thank you very much. I tried the solution you provided, but I couldn't find the file: torch-1.8.0a0+56b43f4-cp38-cp38-linux_x86_64.whl

---

### 评论 #3 — xuhuisheng (2021-05-16T02:27:18Z)

@X-ailsa
You need compile pytorch from source by yourself.
Or you can try this : https://github.com/xuhuisheng/rocm-gfx803

---

### 评论 #4 — ROCmSupport (2021-05-31T09:37:56Z)

Thanks @X-ailsa 
Thanks for reaching out.
As we are NOT officially supporting gfx8 devices with ROCm anymore, I will close this issue.
@xuhuisheng, Thanks for your help.
Feel free to open a new issue, if any, in future.

---
