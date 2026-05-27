# ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory

> **Issue #1164**
> **状态**: closed
> **创建时间**: 2020-06-24T10:50:46Z
> **更新时间**: 2020-06-25T11:56:42Z
> **关闭时间**: 2020-06-25T11:56:42Z
> **作者**: HaromKutya
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1164

## 描述

Hi!

After updating ROCm and its subsequent libraries to the newest version, I get the following error, after just calling `import tensorflow as tf` in python:
`ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory`

Previously I had a similar error, which was resolved, by installing the following libraries:
`sudo apt update && sudo apt install rocsparse hipsparse`

But now, even after I reinstalled the mentioned libraries, and also ROCm (according to the "Uninstall" and "Install" sections in the [install guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html)), I still get the same error.

Have you seen this behavior before, or do you have any suggestions, what might be the cause of this issue?

My versions (practically the latest of everything, except Ubuntu, which is LTS):
Ubuntu 18.04
ROCm 3.5.1-34
tensorflow-rocm 2.2.0
Python 3.7.6

Hardware:
Ryzen 2600
Vega 56

Thanks

---

## 评论 (4 条)

### 评论 #1 — xuhuisheng (2020-06-24T15:57:13Z)

try remove rocm-dkms, and reinstall 3.5.1
I just install 3.5.1 from refresh, and tensorflow-rocm report cannot find libhipspare, then sudo apt install hipspare and reboot, it run well.

Ubuntu 18.04
ROCm 3.5.1-34
tensorflow-rocm 2.2.0
Python 3.6.0 with anaconda

Hardware:
I7 4770
RX 580

---

### 评论 #2 — HaromKutya (2020-06-24T17:37:11Z)

> try remove rocm-dkms, and reinstall 3.5.1
> I just install 3.5.1 from refresh, and tensorflow-rocm report cannot find libhipspare, then sudo apt install hipspare and reboot, it run well.
> 
> Ubuntu 18.04
> ROCm 3.5.1-34
> tensorflow-rocm 2.2.0
> Python 3.6.0 with anaconda
> 
> Hardware:
> I7 4770
> RX 580

I've tried just that, but unfortunately the issue is the same.
It reports ImportError on libhipsparse.so.0 right after installing hipsparse and rebooting.

P.S.: I'm also using anaconda for managing python libraries, but I don't think that matters at the end.

---

### 评论 #3 — xuhuisheng (2020-06-25T11:33:42Z)

I reinstall rocm-3.5.1 in vm, and re-produce this issue.
After `sudo apt install rocm-dkms`, there is no libhipsparse.so.0 in /opt/rocm/lib
`sudo apt install hipspare`, we can found 3 libhipsparse.so* in /opt/rocm/lib
But at this time, import tensorflow as tf always report cannot find libhipsparse.so.0.

Then `sudo ldconfig`, refresh ld cache, the tensorflow-rocm can find libhipsparse.so now.

---

### 评论 #4 — HaromKutya (2020-06-25T11:56:41Z)

> I reinstall rocm-3.5.1 in vm, and re-produce this issue.
> After `sudo apt install rocm-dkms`, there is no libhipsparse.so.0 in /opt/rocm/lib
> `sudo apt install hipspare`, we can found 3 libhipsparse.so* in /opt/rocm/lib
> But at this time, import tensorflow as tf always report cannot find libhipsparse.so.0.
> 
> Then `sudo ldconfig`, refresh ld cache, the tensorflow-rocm can find libhipsparse.so now.

Thanks!!
That resolved the initial issue. Then it turned out that the RCCL is also missing, so i've installed that, and had to do an ld cache refresh again, but it finally works!

Because this resolved it, I'm closing the issue. Thanks again.

---
