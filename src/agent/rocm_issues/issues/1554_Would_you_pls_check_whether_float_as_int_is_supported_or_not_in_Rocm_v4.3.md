# Would you pls check whether float_as_int  is supported or not in Rocm v4.3

> **Issue #1554**
> **状态**: closed
> **创建时间**: 2021-08-12T02:07:04Z
> **更新时间**: 2021-08-17T02:25:00Z
> **关闭时间**: 2021-08-17T02:25:00Z
> **作者**: cyberspicecai
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1554

## 描述

when I use /opt/rocm-4.3.0/bin/hipconvertinplace-perl.sh to convert the source code, I got unsupported device function "float_as_int" and unsupported device function "int_as_float" warning.
But the file:///C:/Users/Administrator/Downloads/AMD_HIP_Supported_CUDA_API_Reference_Guide_v4.3.pdf list this function in HIP-Supported CUDA API.
Thanks.

---

## 评论 (5 条)

### 评论 #1 — Rmalavally (2021-08-13T18:30:11Z)

Thank you for reaching out. For the ROCm v4.3.0 release, the latest scripts for hipification are available at: 

https://github.com/ROCm-Developer-Tools/HIPIFY/tree/master/bin

**Note:** The device functions int_as_float and float_as_int are unsupported; the supported are __int_as_float and __float_as_int.

AMD ROCm Documentation Team

---

### 评论 #2 — cyberspicecai (2021-08-15T12:08:05Z)

> Thank you for reaching out. For the ROCm v4.3.0 release, the latest scripts for hipification are available at:
> 
> https://github.com/ROCm-Developer-Tools/HIPIFY/tree/master/bin
> 
> **Note:** The device functions int_as_float and float_as_int are unsupported; the supported are __int_as_float and __float_as_int.
> 
> AMD ROCm Documentation Team
Thanks your reply.  But I check the URL  you provide and find that the hipconvertinplace-perl.sh update date is 4 years ago. Am I right?


---

### 评论 #3 — ROCmSupport (2021-08-16T04:27:17Z)

Hi @cyberspicecai 
The hipconvertinplace-perl.sh is just a wrapper around hipify-perl. See https://github.com/ROCm-Developer-Tools/HIPIFY/blob/master/bin/hipconvertinplace-perl.sh#L18. hipify-perl is constantly being updated. Last update was 5 days back.
Hope it helps.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-08-16T04:35:12Z)

Feel free to close the issue, if you are happy with the resolution.
Thank you.

---

### 评论 #5 — cyberspicecai (2021-08-17T02:25:00Z)

thanks for your reply and your kindness.

---
