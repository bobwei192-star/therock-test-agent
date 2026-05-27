# With Linux Kernel 4.16 - Driver Install issue, needs update KCL - ROCm 1.8 cannot allocate memory - Need Update Driver with new KCL

> **Issue #413**
> **状态**: closed
> **创建时间**: 2018-05-12T22:08:39Z
> **更新时间**: 2019-04-24T10:54:17Z
> **关闭时间**: 2019-04-24T10:54:17Z
> **作者**: PhilipDeegan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/413

## 描述

strace output since updating to 1.8 for saxpy

```
futex(0x7f07a87320a8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
open("/opt/rocm/bin/../lib/libmcwamp_hsa.so", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\20<\3\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=5428200, ...}) = 0
mmap(NULL, 6126192, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f07a5b37000
mprotect(0x7f07a5bd5000, 2093056, PROT_NONE) = 0
mmap(0x7f07a5dd4000, 3387392, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x9d000) = 0x7f07a5dd4000
close(3)                                = 0
mprotect(0x7f07a5dd4000, 12288, PROT_READ) = 0
getpid()                                = 9611
open("/dev/kfd", O_RDWR|O_CLOEXEC)      = -1 ENOMEM (Cannot allocate memory)
mmap(NULL, 2052096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f07a5942000
write(2, "There is no device can be used t"..., 53There is no device can be used to do the computation
) = 53
```
I upgraded to kernel 4.16, this was occurring both and after

hoping this is normal
```
philix@fad:~/sand/tmp/hcc$ ll /opt/rocm/lib
lrwxrwxrwx 1 root   root        65 May 12 23:54 libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a -> /opt/rocm/hcc/lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.
```

the following does not exist
```
/opt/rocm/hcc/lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a
```

---

## 评论 (5 条)

### 评论 #1 — PhilipDeegan (2018-05-12T22:10:21Z)

/opt/rocm/bin/rocminfo results in the same

---

### 评论 #2 — gstoner (2018-05-12T23:16:05Z)

It probably moving to the 4.16 kernel since kcl in the base driver not happy

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: ♦♣♠♥ <notifications@github.com>
Sent: Saturday, May 12, 2018 5:08:40 PM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: [RadeonOpenCompute/ROCm] 1.8 Cannot allocate memory (#413)


strace output since updating to 1.8

futex(0x7f07a87320a8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
open("/opt/rocm/bin/../lib/libmcwamp_hsa.so", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\20<\3\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=5428200, ...}) = 0
mmap(NULL, 6126192, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f07a5b37000
mprotect(0x7f07a5bd5000, 2093056, PROT_NONE) = 0
mmap(0x7f07a5dd4000, 3387392, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x9d000) = 0x7f07a5dd4000
close(3)                                = 0
mprotect(0x7f07a5dd4000, 12288, PROT_READ) = 0
getpid()                                = 9611
open("/dev/kfd", O_RDWR|O_CLOEXEC)      = -1 ENOMEM (Cannot allocate memory)
mmap(NULL, 2052096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f07a5942000
write(2, "There is no device can be used t"..., 53There is no device can be used to do the computation
) = 53


I upgraded to kernel 4.16, this was occurring both and after

hoping this is normal

philix@fad:~/sand/tmp/hcc$ ll /opt/rocm/lib
lrwxrwxrwx 1 root   root        65 May 12 23:54 libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a -> /opt/rocm/hcc/lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.


the following does not exist

/opt/rocm/hcc/lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a


—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/413>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuTDcwiMC86rJ7Mm4FMzw-zePxypcks5tx11ogaJpZM4T8lHD>.


---

### 评论 #3 — PhilipDeegan (2018-05-13T11:55:02Z)

yes it seems I hadn't reinstalled the rock-dkms - which failed as you said with kcl

[gist](https://gist.github.com/Dekken/d205f9bf114a764ffabfda19a57808c7)

---

### 评论 #4 — PhilipDeegan (2018-05-14T22:27:55Z)

here's a patch attempt for kcl on kernel 4.16

https://gist.github.com/Dekken/863ca2e8235c442817120afb2e593dd6

---

### 评论 #5 — PhilipDeegan (2018-05-21T18:43:48Z)

@gstoner 
bit more [here](https://github.com/0xz/rock-dkms)

---
