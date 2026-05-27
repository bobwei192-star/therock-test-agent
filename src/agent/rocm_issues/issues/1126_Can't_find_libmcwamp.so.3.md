# Can't find libmcwamp.so.3

> **Issue #1126**
> **状态**: closed
> **创建时间**: 2020-06-04T08:02:03Z
> **更新时间**: 2020-06-05T06:06:53Z
> **关闭时间**: 2020-06-05T05:46:13Z
> **作者**: codecor-cn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1126

## 负责人

- sunway513

## 描述

use tensorflow-rocm2.1.1
centos 8.1  rocm3.5
`
import tensorflow as tf
ImportError: libmcwamp.so.3: cannot open shared object file: No such file or directory
`


---

## 评论 (11 条)

### 评论 #1 — thesleort (2020-06-04T13:02:49Z)

I was using OpenCL yesterday with ROCm 3.3 and upgraded today to ROCm 3.5. For me I was missing libOpenCL.so. Did a complete reinstall of ROCm 3.5 (removing it and then installing it again) and now everything works again.

My system is Ubuntu 20.04
Threadripper 1900x and Vega 56

---

### 评论 #2 — dagrim (2020-06-04T13:57:55Z)

Same thing here : 
- using Ubuntu 18.04 bionic
- ROCm 3.5 (all packages installed)
- python 3.8 + tensorflow-rocm

Error upon importing tensorflow : 
ImportError: libmcwamp.so.3: cannot open shared object file: No such file or directory

The files libmcwamp.so.3 and libmcwamp.so don't exist in /opt/rocm (neither anywhere else on the system).

Am I missing a package ?

---

### 评论 #3 — H-Ribeiro (2020-06-04T15:50:15Z)

> I was using OpenCL yesterday with ROCm 3.3 and upgraded today to ROCm 3.5. For me I was missing libOpenCL.so. Did a complete reinstall of ROCm 3.5 (removing it and then installing it again) and now everything works again.
> 
> My system is Ubuntu 20.04
> Threadripper 1900x and Vega 56

Hi, I have a similar setup.
Are you able to install and use ROCm 3.5 without any special configurations or pre-requirements?

Thanks

---

### 评论 #4 — Reinercas (2020-06-04T19:00:40Z)

Hi, I have the exact same problem:
`ImportError: libmcwamp.so.3: cannot open shared object file: No such file or directory`

Using:
Ubuntu 20.04
rocm 3.5
tensorflow-rocm 2.2.0rc5

---

### 评论 #5 — scchan (2020-06-04T19:19:38Z)

That is due to a long overdue change to HIP.  With ROCm 3.5, we are moving to the new HIP implementation which comes with a new runtime.  You'll probably have to update to a newer Tensorflow binary built by ROCm 3.5.  Perhaps @sunway513 could provide some information on that.

---

### 评论 #6 — sunway513 (2020-06-04T19:58:43Z)

Yes, we are working on the whl packages which are build with ROCm3.5 user bit packages. Those will be updated very soon. 

---

### 评论 #7 — sunway513 (2020-06-04T23:38:25Z)

Hi @codecor-cn  , we've released the tensorflow-rocm packages built with ROCm3.5 environment.
For details please refer to the following document:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md

---

### 评论 #8 — codecor-cn (2020-06-05T03:47:40Z)

> Hi @codecor-cn , we've released the tensorflow-rocm packages built with ROCm3.5 environment.
> For details please refer to the following document:
> https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md

when i upgraded to this version, problem libmcwamp.so  not found has gone away, but
libhipsparse.so.0: cannot open shared object file: No such file or directory 

Traceback (most recent call last):
  File "/usr/local/lib64/python3.6/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/usr/local/lib64/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/usr/local/lib64/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/usr/lib64/python3.6/imp.py", line 243, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib64/python3.6/imp.py", line 343, in load_dynamic
    return _load(spec)
ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory

---

### 评论 #9 — sunway513 (2020-06-05T04:04:10Z)

@codecor-cn please try to install rocsparse/hipsparse library:
`sudo apt update && sudo apt install rocsparse hipsparse`
You can also try the integrated docker containers for a faster deployment:
https://hub.docker.com/r/rocm/tensorflow

---

### 评论 #10 — codecor-cn (2020-06-05T05:45:54Z)

> @codecor-cn please try to install rocsparse/hipsparse library:
> `sudo apt update && sudo apt install rocsparse hipsparse`
> You can also try the integrated docker containers for a faster deployment:
> https://hub.docker.com/r/rocm/tensorflow

i use centos 8 not ubuntu but you can still use yum install rocsparse hipsparse.
then another error appeared  "ImportError: librccl.so.1: cannot open shared object file: No such file or directory"

1. need install rccl
yum install rccl
or
git clone git@github.com:ROCmSoftwarePlatform/rccl.git
./install -i

2. not found librocblas.so libMIOpen.so librocfft.so librocrand.so
yum install rocm-libs miopen-hip

it's done

---

### 评论 #11 — codecor-cn (2020-06-05T05:46:13Z)

thanks every one!

---
