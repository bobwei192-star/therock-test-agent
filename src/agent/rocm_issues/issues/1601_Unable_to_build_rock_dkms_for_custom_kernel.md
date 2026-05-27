# Unable to build rock dkms for custom kernel

> **Issue #1601**
> **状态**: closed
> **创建时间**: 2021-10-27T23:11:51Z
> **更新时间**: 2024-01-24T22:32:35Z
> **关闭时间**: 2024-01-24T22:32:35Z
> **作者**: tsipa
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1601

## 描述

What i did:

rpm -ivh rock-dkms-4.3-59.el7.noarch.rpm rock-dkms-firmware-4.3-59.el7.noarch.rpm
dkms build -m amdgpu -v 4.3-59.el7 -k 5.12.0
where 5.12.0 is a custom kernel
I got:
https://pastebin.com/AYf7DmTB
"gcc: fatal error: cannot specify -o with -c, -S or -E with multiple files"

I investigated a little up to the running make with debug and i know it's running something like:
https://pastebin.com/sSYqWppF
and the problem is `-I./include ./include/linux/compiler-version.h` stanza which incorrect in terms of syntax, but now i'm struggling to figure out where it's coming from in makefiles.

I know that this problem was reported relatively recently for ubuntu as well.
https://github.com/RadeonOpenCompute/ROCm/issues/1125

---

## 评论 (4 条)

### 评论 #1 — tsipa (2021-10-28T15:48:09Z)

Okay, the problem is this commit https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/commit/7f686562967d46395d862ac72282313e05f38a3d

`$(filter-out -I%/uapi -include %/kconfig.h,$(LINUXINCLUDE))`

will remove all words that matches patterns:
```
-I%/uapi
 -include
%/kconfig.h,
```
so it translates string 
`-I./include -I./arch/x86/include/uapi -I./arch/x86/include/generated/uapi -I./include/uapi -I./include/generated/uapi -include ./include/linux/compiler-version.h -include ./include/linux/kconfig.h`

to
`-I./include -include ./include/linux/compiler-version.h -include ./include/linux/kconfig.h`
by removing  `-I%/uapi`
then to
`-I./include ./include/linux/compiler-version.h ./include/linux/kconfig.h`
by removing `-include`

then to
`-I./include ./include/linux/compiler-version.h`
which is syntactically incorrent.


I will prepare pull request

---

### 评论 #2 — ROCmSupport (2021-11-03T10:23:06Z)

Thanks @tsipa for reaching out.
I recommend to open issues specific to kernel @ [https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver](url) as they are handled separately. 
I found that you already created PR for this issue there: https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/pull/117
So no pending action item is here for now.
Anyhow, I will talk to Kernel team on this and will update.

---

### 评论 #3 — ROCmSupport (2021-11-16T13:04:36Z)

Hi @tsipa 
Good news. Some flags need to be enabled w.r.to newer versions of GCC.
Work is completed and changes are pushed into internal builds. It will be part of next ROCm versions like ROCm 5.0(most likely).
Thank you.

---

### 评论 #4 — nartmada (2024-01-24T22:32:35Z)

Closing this issue as work is completed back in Nov 16, 2021.  

---
