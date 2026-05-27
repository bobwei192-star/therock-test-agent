# hipcc.bin not present after rocm/5.4.x installation

> **Issue #1885**
> **状态**: closed
> **创建时间**: 2023-01-06T19:02:32Z
> **更新时间**: 2023-01-07T06:27:48Z
> **关闭时间**: 2023-01-07T06:27:47Z
> **作者**: xinye83
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1885

## 描述

I tried to install rocm/5.4.0 and rocm/5.4.1 in a SLES 15 SP4 docker container with the following command and `hipcc.bin` is not present
```
amdgpu-install -y --usecase=rocm,hiplibsdk --no-dkms
```

The release note says they are available thought:
https://docs.amd.com/bundle/ROCm-Release-Notes-v5.4/page/Deprecations_and_Warnings.html
https://docs.amd.com/bundle/ROCm-Release-Notes-v5.4.1/page/Deprecations_and_Warnings.html

Please update the documentation to reflect the desired bahaviour.


---

## 评论 (3 条)

### 评论 #1 — Rmalavally (2023-01-06T19:42:47Z)

Thank you for the feedback. 

We are checking with our internal teams about the unavailability of hipcc.bin and will keep you updated.

ROCm Documentation Team


---

### 评论 #2 — Rmalavally (2023-01-06T23:10:53Z)

@xinye83 

Our Development team has indicated that this issue will be fixed in a future release. We have updated our documentation with more details at,

https://docs.amd.com/bundle/ROCm-Release-Notes-v5.4/page/Deprecations_and_Warnings.html
https://docs.amd.com/bundle/ROCm-Release-Notes-v5.4.1/page/Deprecations_and_Warnings.html

Thank you for your feedback.
ROCm Documentation Team

---

### 评论 #3 — xinye83 (2023-01-07T06:27:47Z)

Thanks for the updates!

---
