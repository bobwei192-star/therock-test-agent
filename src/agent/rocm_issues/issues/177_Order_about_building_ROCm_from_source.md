# Order about building ROCm from source

> **Issue #177**
> **状态**: closed
> **创建时间**: 2017-08-03T02:38:35Z
> **更新时间**: 2018-06-03T14:58:46Z
> **关闭时间**: 2018-06-03T14:58:46Z
> **作者**: lintcoder
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/177

## 描述

Recently I want to build the whole ROCm from source code,  since there are so many repos and no clear steps, it's difficult for me to decide the right order to build the whole project. Here is my opinion about the order as follows,  each represents one repo in ROCm, please tell me if it's right ? @gstoner 

1. ROCK-Kernel-Driver
2. ROCT-Thunk-Interface
3. ROCR-Runtime 
4. ROCm-Device-Libs
5. compiler-runtime
6. HCC
7. HIP
8. ROC-smi
9. ATMI


---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-08-03T02:39:52Z)

Yes that would be correct order,  Also I am working on new documentation. 


---

### 评论 #2 — lintcoder (2017-08-03T03:03:09Z)

thanks, I want to build it on my ubunu16.04-arm64 server, when I run "make rock-rel_defconfig" following the  readme of ROCK-Kernel-Driver,  errors like "can't find rock-rel_defconfig" occur and the file .config can't be generated, while on x86_64 it worked,  should I replace the command with "make defconfig" ? @gstoner 

---

### 评论 #3 — lintcoder (2017-08-07T02:29:18Z)

I replace "make rock-rel_defconfig" with "make defconfig" and make && make install, but the new kernel can't be loaded successfully and kernel file names like vmlinuz-4.9.0-00001-gfbf6230-dirty, what should I do ?  @gstoner 

---
