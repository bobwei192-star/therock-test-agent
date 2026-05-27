# Failed to load the native Tensorflow runtime after upgrading to ROCm 2.3

> **Issue #764**
> **状态**: closed
> **创建时间**: 2019-04-13T16:15:59Z
> **更新时间**: 2019-04-15T13:24:26Z
> **关闭时间**: 2019-04-13T20:11:41Z
> **作者**: SandboChang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/764

## 描述

Hi,

On upgrading to ROCm 2.3, now importing tensorflow throws this message:
```
~/.local/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow.py in <module>
     57 
---> 58   from tensorflow.python.pywrap_tensorflow_internal import *
     59   from tensorflow.python.pywrap_tensorflow_internal import __version__

~/.local/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py in <module>
     27             return _mod
---> 28     _pywrap_tensorflow_internal = swig_import_helper()
     29     del swig_import_helper

~/.local/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py in swig_import_helper()
     23             try:
---> 24                 _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
     25             finally:

/usr/lib/python3.6/imp.py in load_module(name, file, filename, details)
    242         else:
--> 243             return load_dynamic(name, filename, file)
    244     elif type_ == PKG_DIRECTORY:

/usr/lib/python3.6/imp.py in load_dynamic(name, path, file)
    342             name=name, loader=loader, origin=path)
--> 343         return _load(spec)
    344 

ImportError: /home/spooky/.local/lib/python3.6/site-packages/tensorflow/python/../libtensorflow_framework.so: undefined symbol: hipModuleGetGlobal

During handling of the above exception, another exception occurred:

ImportError                               Traceback (most recent call last)
<ipython-input-1-ff89de3f2891> in <module>
      3 import numpy as np
      4 import matplotlib.pyplot as plt
----> 5 import tensorflow as tf
      6 import time

~/.local/lib/python3.6/site-packages/tensorflow/__init__.py in <module>
     22 
     23 # pylint: disable=g-bad-import-order
---> 24 from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import
     25 
     26 from tensorflow._api.v1 import app

~/.local/lib/python3.6/site-packages/tensorflow/python/__init__.py in <module>
     47 import numpy as np
     48 
---> 49 from tensorflow.python import pywrap_tensorflow
     50 
     51 # Protocol buffers

~/.local/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow.py in <module>
     72 for some common reasons and solutions.  Include the entire stack trace
     73 above this error message when asking for help.""" % traceback.format_exc()
---> 74   raise ImportError(msg)
     75 
     76 # pylint: enable=wildcard-import,g-import-not-at-top,unused-import,line-too-long

ImportError: Traceback (most recent call last):
  File "/home/spooky/.local/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/home/spooky/.local/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/home/spooky/.local/lib/python3.6/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/usr/lib/python3.6/imp.py", line 243, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib/python3.6/imp.py", line 343, in load_dynamic
    return _load(spec)
ImportError: /home/spooky/.local/lib/python3.6/site-packages/tensorflow/python/../libtensorflow_framework.so: undefined symbol: hipModuleGetGlobal


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/errors

for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.
```
Would you have any ideas?
I am on ubuntu 18.04.2 LTS, kernel is 4.15.0-47-generic

---

## 评论 (4 条)

### 评论 #1 — SandboChang (2019-04-13T16:23:20Z)

Solved, as I am running a jupyter notebook server off another lower privilege user account, 
somehow it has an older version installed and then the jupyter notebook was trying to load that (1.13.1),
but apparently when upgrading ROCm the system wide one was updated to 1.13.2.

Now removing both, and then I just installed the system wide one with sudo, it can import tensorflow without any issues.

---

### 评论 #2 — sunway513 (2019-04-13T22:03:55Z)

@SandboChang , the tensorflow-rocm-1.13.1 whl package is no longer compatible with the ROCm2.3 user-bit environment. 
Therefore, we bumped the minor version of Tensorflow 1.13 release branch (r1.13-rocm) and uploaded the refreshed whl package compatible to ROCm2.3, the current whl package version is 1.13.2. 
If you have installed tensorflow-rocm package on your system prior to ROCm2.3, the following commands would get it updated to the tip:
`pip3 install tensorflow-rocm --upgrade`

---

### 评论 #3 — xxshazxx (2019-04-15T09:58:33Z)

Hello, 
I've updated the system to ROCm 2.3 and I was using Anaconda with tensorflow-rocm.
Right now I get the errore message "Failed to load the native TensorFlow runtime" after upgrading to tensorflow-rocm      1.13.2
Any help to solve it?

Ubuntu 16.04, Kernel 4.19.0-041900

Thanks

---

### 评论 #4 — sunway513 (2019-04-15T13:24:26Z)

Hi @xxshazxx , could you create a new issue in tensorflow-rocm repo:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues
Please help provide steps to reproduce. 

---
