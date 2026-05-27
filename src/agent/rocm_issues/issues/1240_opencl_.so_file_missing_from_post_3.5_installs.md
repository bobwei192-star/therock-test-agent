# opencl .so file missing from post 3.5 installs

> **Issue #1240**
> **状态**: closed
> **创建时间**: 2020-09-23T21:42:05Z
> **更新时间**: 2020-09-24T01:29:38Z
> **关闭时间**: 2020-09-24T01:29:38Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1240

## 描述

I am running Ubuntu 18.04.5 with 5.4 kernel. I have had ROCm installed since version 2.
Whenever I upgrade ROCm since 3.5, the opencl .so files remain in my 3.5 folder.
 
So, even with 3.8, I have to keep 3.5 install folder around to be able to use OpenCL.

Is this correct? For a fresh 3.8 install, which library is used for enabling OpenCL ?

---

## 评论 (3 条)

### 评论 #1 — baryluk (2020-09-23T22:26:50Z)

Be more specific. What packages you installed, what versions, which distro. Are you using deb files using apt, or rpm / yum?

The library is definitively there:

```
root@debian:~# dpkg -S libamdocl64.so
rocm-opencl3.8.0: /opt/rocm-3.8.0/opencl/lib/libamdocl64.so
root@debian:~#
```

same for clinfo, etc.


Also take a look at https://github.com/RadeonOpenCompute/ROCm/issues/1131  , which might help you make it work better.


---

### 评论 #2 — boxerab (2020-09-23T22:50:09Z)

@baryluk thanks! I tried your absolute path fix to the icd file, and now I can run regular `clinfo`, not the one on the ROCm directory.

---

### 评论 #3 — boxerab (2020-09-24T01:29:38Z)

I ended up doing a fresh install, and the problem has disappeared.

---
