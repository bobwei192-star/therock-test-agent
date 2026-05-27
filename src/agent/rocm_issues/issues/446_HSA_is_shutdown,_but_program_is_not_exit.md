# HSA is shutdown, but program is not exit.

> **Issue #446**
> **状态**: closed
> **创建时间**: 2018-06-28T02:36:17Z
> **更新时间**: 2018-08-14T15:11:44Z
> **关闭时间**: 2018-08-14T15:11:44Z
> **作者**: WeiChunyu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/446

## 描述

OMEN-by-HP-Laptop
Model: 15-ax211TX
OS: Ubuntu 16.04.4 LTS (Xenial Xerus)
CPU: Intel Core i5-7300HQ
Graphics Card:AMD Radeon RX 460

wei@OMEN-by-HP-Laptop:~$ cd /opt/rocm/hsa/sample/
wei@OMEN-by-HP-Laptop:/opt/rocm/hsa/sample$ ./vector_copy
...
Shutting down the runtime succeeded.
But program isn't exit.
As shown, when press Enter or Control C, even if no new command prompt appeared.
 rocminfo and opencl programs also have the same situation.
![2018-06-27 15-49-18](https://user-images.githubusercontent.com/22558386/42009832-9b350142-7abe-11e8-86a2-ab22abd7ae5d.png)


---

## 评论 (4 条)

### 评论 #1 — jedwards-AMD (2018-06-28T14:29:34Z)

Can you provide dmesg output?

---

### 评论 #2 — WeiChunyu (2018-06-29T10:37:24Z)

As the photo shows, there is no other output.

---

### 评论 #3 — jedwards-AMD (2018-06-29T14:30:16Z)

What I mean is, can you open another terminal and run the command 'dmeag' to get output of kernel error messages? This will tell us if a kernel error occurred. If the entire system is hung, we need to look at the /var/log/kern.log file to determine what happened after we reboot.

---

### 评论 #4 — WeiChunyu (2018-06-30T07:43:01Z)

dmesg 
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/2151514/dmesg.txt)

kern.log
[kern.log](https://github.com/RadeonOpenCompute/ROCm/files/2151515/kern.log)


---
