# Could not run 'aten::empty_strided' with arguments from the 'HIP' backend

> **Issue #1629**
> **状态**: closed
> **创建时间**: 2021-11-26T08:34:27Z
> **更新时间**: 2024-01-27T04:18:23Z
> **关闭时间**: 2024-01-27T04:18:23Z
> **作者**: ablazet
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1629

## 描述


When I ran the resnet50 model on gfx900 device, I found the problem "Could not run 'aten::empty_strided' with arguments from the 'HIP' backend". The version used was  rocm4.2 and pytorch1.10.0，so how should I solve the problem？

---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2021-11-26T10:19:48Z)

Thanks @ablazeTang for reaching out.
Can you please share the exact steps(step by step) for better understanding and also to reproduce the problem. 
Please share below outputs also.
_/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
dmesg_
Thank you.

---

### 评论 #2 — ROCmSupport (2022-05-09T05:11:59Z)

I am closing this as there is no update for the last 6 months.
Request to open new issues, if any, for quick resolutions.
Thank you.

---

### 评论 #3 — randomstuff (2022-08-29T09:11:34Z)

I reached the same problem [when trying to run Stable Diffusion on top of the diffusers package](https://www.gabriel.urdhr.fr/2022/08/28/trying-to-run-stable-diffusion-on-amd-ryzen-5-5600g/) :

> NotImplementedError: Could not run 'aten::empty_strided' with arguments from the 'HIP' backend. This could be because the operator doesn't exist for this backend, or was omitted during the selective/custom build process (if using custom build). If you are a Facebook employee using PyTorch on mobile, please visit https://fburl.com/ptmfixes for possible resolutions.

But this seems to be a problem in pytorch.

---

### 评论 #4 — randomstuff (2022-08-29T10:51:52Z)

@ablazet For me, this was caused by trying to use the "hip" PyTorch device. [You are expected to use the "cuda" device.](https://pytorch.org/docs/stable/notes/hip.html#hip-interfaces-reuse-the-cuda-interfaces)

---

### 评论 #5 — abhimeda (2023-12-20T19:35:35Z)

@ablazet Is the issue still reproducible with the latest ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #6 — abhimeda (2023-12-20T22:07:47Z)

@ablazet I hope you were able to resolve your issue with this? Can we close this issue?

---

### 评论 #7 — nartmada (2024-01-27T04:18:23Z)

Closing this ticket as there is no update for the last 6 months.  Thanks.

---
