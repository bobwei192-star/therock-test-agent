# When will compute units (CU) reservation be included?

> **Issue #363**
> **状态**: closed
> **创建时间**: 2018-03-15T12:58:36Z
> **更新时间**: 2020-09-10T16:24:27Z
> **关闭时间**: 2020-09-10T16:24:27Z
> **作者**: Yougmark
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/363

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I noticed this great technique compute units reservation in Polaris whitepaper, which says programmers can partition the device via API extensions.  But I don't think it's included in the open-source software stack.

This technique is great for real-time systems.  Also, currently not implemented clCreateSubDevices in OpenCL runtime can be enabled with this technique.

Will this be included in ROCm?  When?

Thanks,
Ming

---

## 评论 (4 条)

### 评论 #1 — gstoner (2018-03-17T13:19:11Z)

This is equivalent of CU MASKING  is compute unit reservation which KFD support today.   We are looking at it. 

---

### 评论 #2 — Yougmark (2018-03-17T14:24:08Z)

I see.  CU Masking is implemented in HSA runtime and libhsakmt.  But it seems OpenCL does not have an interface to use it.  Very interesting!  Will look into this.  Thank you!

Ming

---

### 评论 #3 — mirh (2019-12-23T13:20:36Z)

Any update (or should this be moved to OpenCL-Runtime?)

It would be nice to have the incoming TAN work on a fully open stack. 

---

### 评论 #4 — jlgreathouse (2020-09-10T16:24:27Z)

This feature is available in HIP as of ROCm 3.6 using the API `hipExtStreamCreateWithCUMask()`. See [this header](https://github.com/ROCm-Developer-Tools/HIP/blob/roc-3.6.x/include/hip/hcc_detail/hip_runtime_api.h#L852) for documentation. AMD does not plan on adding a similar feature to our OpenCL at this time.

However, now that both HIP and OpenCL use our common language runtime, ROCclr, you could perhaps hack your own version of the OpenCL runtime using similar techniques for research purposes. See [this patch](https://github.com/ROCm-Developer-Tools/HIP/commit/7dd5b19290cbe3364d1bc334317af277e6e528ef#diff-9b19b5d4faa1ae017074109f7f2511a6R55) for how this feature was added to our HIP runtime. You could likely make similar changes into `clCreateCommandQueueWithProperties()` [somewhere around here](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/rocm-3.7.0/amdocl/cl_command.cpp#L151) if you wanted to test CU masking for your OpenCL applications. However, as I mentioned, AMD does not plan on adding this feature into `clCreateSubDevices()` at this time.

---
