# ImportError: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory

> **Issue #1852**
> **状态**: closed
> **创建时间**: 2022-11-03T05:56:18Z
> **更新时间**: 2022-11-03T09:48:00Z
> **关闭时间**: 2022-11-03T09:47:59Z
> **作者**: zhishixiang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1852

## 描述

I am running ubuntu 22.04 and tensorflow, but when i try to run this command`import tensorflow as tf`it crash:

`ImportError: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory`

how to solve this problem?



---

## 评论 (8 条)

### 评论 #1 — xuhuisheng (2022-11-03T06:06:35Z)

`libhsa-runtime64.so.1` should be in the `/opt/rocm/lib/` or `/opt/rocm-5.3.0/lib/`

---

### 评论 #2 — zhishixiang (2022-11-03T06:07:54Z)

> 

yes i found it in `/opt/rocm/lib/`

---

### 评论 #3 — xuhuisheng (2022-11-03T06:10:19Z)

So the libhsa-runtime64.so is installed successfully.
Then you can try `export LD_LIBRARY_PATH=/opt/rocm/lib` to tell tensorflow-rocm where to find it. This may solve the problem.

---

### 评论 #4 — zhishixiang (2022-11-03T06:56:49Z)

> So the libhsa-runtime64.so is installed successfully. Then you can try `export LD_LIBRARY_PATH=/opt/rocm/lib` to tell tensorflow-rocm where to find it. This may solve the problem.

I solve this problem, but i meet this new problem:
`2022-11-03 06:55:59.045244: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'librocblas.so'; dlerror: librocblas.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm/lib
 
2022-11-03 06:55:59.045264: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libMIOpen.so'; dlerror: libMIOpen.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm/lib  

2022-11-03 06:55:59.045281: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libhipfft.so'; dlerror: libhipfft.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm/lib  

2022-11-03 06:55:59.045297: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'librocrand.so'; dlerror: librocrand.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm/lib`   

how to fix it?please help me (

---

### 评论 #5 — xuhuisheng (2022-11-03T07:33:48Z)

librocblas.so and libmiopen.so and etc, all of them should be in the `/opt/rocm/lib/` likely directory.

Do you install rocm-libs?

---

### 评论 #6 — zhishixiang (2022-11-03T07:42:45Z)

> librocblas.so and libmiopen.so and etc, all of them should be in the `/opt/rocm/lib/` likely directory.
> 
> Do you install rocm-libs?

no, i try to install it but i found this:
`After this operation, 23.1 GB of additional disk space will be used,`
is this lib really 23.1GB? it is too terrible(

---

### 评论 #7 — xuhuisheng (2022-11-03T08:38:54Z)

In my case, it will cost about 2.2 GB disk.
And rocm-libs contains miopen, which equals cudnn, to imple the dnn speedup mathmetics.
rocblas, rocfft and etc is depended by miopen. So tensorflow and pytorch need miopen installing first.

---

### 评论 #8 — zhishixiang (2022-11-03T09:47:59Z)

ok now it runs thank you

---
