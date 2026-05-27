# ROCm driver for Ubuntu 14.04.5 (Kernel 4.4) and Vega Frontier

> **Issue #578**
> **状态**: closed
> **创建时间**: 2018-10-16T01:50:01Z
> **更新时间**: 2019-03-12T16:07:20Z
> **关闭时间**: 2019-03-12T16:07:20Z
> **作者**: anirbannag
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/578

## 描述

Is the ROCm driver supported for Ubuntu 14.04.5 and Vega Frontier? We are trying to install in a university server and changing the operating system is tricky because the department won't support issues/problems for other OS. Is there any way to use the Vega Frontier GPU on such an operating system? We are trying to run compute workloads. 

---

## 评论 (3 条)

### 评论 #1 — anirbannag (2018-10-16T03:11:53Z)

The guide says the GPU will be listed with the following two commands, but I get the following errors:

/opt/rocm/bin/rocminfo

/opt/rocm/bin/rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by /opt/rocm/bin/rocminfo)
/opt/rocm/bin/rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.20' not found (required by /opt/rocm/hsa/lib/libhsa-runtime64.so.1)
/opt/rocm/bin/rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by /opt/rocm/hsa/lib/libhsa-runtime64.so.1)

/opt/rocm/opencl/bin/x86_64/clinfo

terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

---

### 评论 #2 — kentrussell (2019-03-12T12:18:46Z)

The issue is that the runtime was compiled with a GCC of 3.4.20/21, and thus rocminfo can't work if there is a lower version of GCC installed (a GCC issue). Is it possible to upgrade the version of GCC on the system?

---

### 评论 #3 — jlgreathouse (2019-03-12T16:07:20Z)

To be a bit more direct here: no, ROCm no longer supports Ubuntu 14.04. Our `rock-dkms` driver no longer supports kernel 4.4 and we do not plan to go back and have it do so. This kernel is also too old to support ROCm using the baseline kernel itself. As such, I do not expect ROCm to work on your Ubuntu 14.04 system.

---
