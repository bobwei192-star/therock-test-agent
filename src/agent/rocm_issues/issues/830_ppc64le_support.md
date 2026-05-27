# ppc64le support

> **Issue #830**
> **状态**: closed
> **创建时间**: 2019-06-28T19:35:11Z
> **更新时间**: 2024-03-22T08:45:03Z
> **关闭时间**: 2024-03-21T22:22:04Z
> **作者**: ticlazau
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/830

## 描述

Hello,

is ROCm supported on ppc64le - CentOS or Ubuntu?

Thx,
FM

---

## 评论 (12 条)

### 评论 #1 — madscientist159 (2019-08-28T21:07:44Z)

Also curious about support, in theory it should be able to be added but has AMD done any work toward this goal?

---

### 评论 #2 — illuhad (2019-08-28T21:11:46Z)

Early versions of ROCm claimed to support ppc64le - no idea what happened since then. I played with recent versions on Power8 but was unsuccessful (see #800)

---

### 评论 #3 — darkbasic (2023-02-17T13:57:52Z)

AMD, is there any news on this? Do we really need to wait for rusticl to support SyCL and HIP? Hopefully ROCm won't be the next AMDVLK, but I'm starting to lose hope.

---

### 评论 #4 — nartmada (2024-02-02T21:42:57Z)

I am really sorry for the delay.  It should work in latest ROCm 6.0.2.  Can you please give it a try?  Thanks.

---

### 评论 #5 — darkbasic (2024-02-03T08:42:27Z)

@nartmada awesome I'll give it a try, thanks!

---

### 评论 #6 — nartmada (2024-02-14T04:24:08Z)

@darkbasic, please let us know how it goes with ROCm 6.0.2.  Thanks.

---

### 评论 #7 — darkbasic (2024-02-26T09:20:23Z)

@nartmada I'm sorry for the delay, unfortunately I still have the same issue as before:
```
talos2 ~ # clinfo 
clinfo: /var/tmp/portage/dev-libs/rocm-opencl-runtime-6.0.2/work/clr-rocm-6.0.2/rocclr/os/os_posix.cpp:321: static void amd::Os::currentStackInfo(unsigned char**, size_t*): Assertion `Os::currentStackPtr() >= *base - *size && Os::currentStackPtr() < *base && "just checking"' failed.
Aborted (core dumped)
```

Previous archived issue about this: https://github.com/ROCm/ROCm-OpenCL-Runtime/issues/158
In addition to the previous patches/workarounds I had to use the `-DNO_WARN_X86_INTRINSICS` compile flag to get it to build, but it still fails at runtime as it did before.

---

### 评论 #8 — darkbasic (2024-02-26T09:23:09Z)

Full build log without `-DNO_WARN_X86_INTRINSICS`: [rocm-opencl-runtime-6.0.2.build.log](https://github.com/ROCm/ROCm/files/14402368/rocm-opencl-runtime-6.0.2.build.log)

---

### 评论 #9 — darkbasic (2024-02-26T09:52:49Z)

I've also opened a brand new issue on the new repo: https://github.com/ROCm/clr/issues/61

---

### 评论 #10 — tucnak (2024-03-07T15:52:20Z)

@nartmada We have been trying to get our MI50 card working on a POWER9 system, and in this quest we had built everything from scratch, had to mess with some obscure kernel versions (freedesktop) that is what AMD is using apparently for their cutting-edge changes but to no avail. The runtime would still be incredibly unreliable, have to be recovered periodically, running into [horrible issues](https://github.com/ROCm/ROCK-Kernel-Driver/issues/147) which haven't bee addressed. I understand that the consumer cards aren't supported, but isn't MI50 datacenter-grade and supposed to be stable? We no longer have appetite for messing with the kernels, and would have to stick to debian-stable, i.e. 6.1.76 at the time of writing this comment. AMD is the only vendor to properly support IOMMU, and indeed we're prepared to go through the effort of building userspace ROCm components in a VM image but before we would do that, we want to be sure that the kernel business is stable, and isn't going to mess up our host like it did numerous times prior.

---

### 评论 #11 — saadrahim (2024-03-21T22:22:04Z)

ROCm only supports x86_64 based CPU architectures. In addition, we have additional dependencies on CPU and PCIe features as documented at https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#cpu-support.

@nartmada was mistaken when he suggested to try the latest versions.

---

### 评论 #12 — darkbasic (2024-03-22T08:45:02Z)

"dependencies on CPU and PCIe features" sounds like corporate bullsh*t to me: it translates to pcie atomics according to that page. @madscientist159 doesn't power 8 already support PCIe atomics?

Honestly it looks like George Hotz was right suggesting to look at Intel for compute.

---
