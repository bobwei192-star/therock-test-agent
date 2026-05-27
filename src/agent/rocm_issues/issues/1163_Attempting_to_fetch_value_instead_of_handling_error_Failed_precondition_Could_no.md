# Attempting to fetch value instead of handling error Failed precondition: Could not load dynamic library 'libhip_hcc.so'; dlerror: libhip_hcc.so: cannot open shared object file: No such file or directory

> **Issue #1163**
> **状态**: closed
> **创建时间**: 2020-06-24T07:42:28Z
> **更新时间**: 2020-12-17T04:47:44Z
> **关闭时间**: 2020-12-17T04:47:44Z
> **作者**: vuquocan1987
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1163

## 描述

I installed the tensorflow_rocm with rocm stack on my computer, but when I tried to create a model I got such error.

My set up is:

ubuntu 18.04.04
rocm 3.5.1
tensorflow-rocm 2.2.0
gpu rx580
cpu intel 9100f

What is wrong?

---

## 评论 (7 条)

### 评论 #1 — xuhuisheng (2020-06-24T15:59:58Z)

it seems that ldconfig cannot find the soft link of hip_hcc,
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm/hip/lib
then it run well

Ubuntu 18.04.04
ROCm 3.5.1-34
tensorflow-rocm 2.2.0
Python 3.6.0 with anaconda

Hardware:
cpu I7 4770
gpu RX 580

---

### 评论 #2 — vuquocan1987 (2020-06-25T06:52:08Z)

thank you very much, this does solve my problem. Do you know why though?

---

### 评论 #3 — ghost (2020-06-25T10:54:59Z)

Solves the problem partially but not fully

---

### 评论 #4 — xuhuisheng (2020-06-25T11:46:38Z)

> 
> 
> thank you very much, this does solve my problem. Do you know why though?

At this moment, I dont know why caused this situation.
The libhip_hcc.so and related files are in the /opt/rocm/hip/lib directory, but even if  I run `sudo ldconfig`, but `tensorflow-rocm` cannot find these `.so` files.

---

### 评论 #5 — papadako (2020-06-25T20:49:43Z)

I am not sure either. If you delete libhiprtc.so then ldconfig will find libhip_hcc.so.
Check my post https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/1019#issuecomment-649432182 about another workaround

> > thank you very much, this does solve my problem. Do you know why though?
> 
> At this moment, I dont know why caused this situation.
> The libhip_hcc.so and related files are in the /opt/rocm/hip/lib directory, but even if I run `sudo ldconfig`, but `tensorflow-rocm` cannot find these `.so` files.



---

### 评论 #6 — kk-1 (2020-08-21T14:18:43Z)

Hello Folks,
I had the same problem.
I saw that the library libhip_hcc is moved to (as symlink!!!):
/usr/lib/aomp/lib

Here 2 ways:
1-) You can create symlink to "libamdhip64.so" in the PATH manually or
2-) You can install the aomp and set the LD_LIBRARY_PATH in your .profile like that (got some extras but just get the idea!):

`export LD_LIBRARY_PATH="/usr/lib/aomp/lib:/usr/lib/aomp/lib64:/opt/rocm/lib:/opt/rocm/lib64:/opt/rocm/opencl/lib/x86_64:$LD_LIBRARY_PATH"`


BTW I got:
openSUSE Tumbleweed: rpm based system
rocm 3.7.0
aomp 11.8

Cheers!!!

---

### 评论 #7 — ROCmSupport (2020-12-17T04:47:44Z)

Hi @vuquocan1987 and all,
Thanks for reaching out.
This issue is fixed and no more observed with the recent ROCm release versions.
Recommend to try with 3.10.
Thank you.


---
