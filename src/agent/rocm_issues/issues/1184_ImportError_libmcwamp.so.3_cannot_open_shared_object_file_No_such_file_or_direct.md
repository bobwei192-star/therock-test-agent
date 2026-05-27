# ImportError: libmcwamp.so.3: cannot open shared object file: No such file or directory

> **Issue #1184**
> **状态**: closed
> **创建时间**: 2020-07-24T17:41:59Z
> **更新时间**: 2021-01-18T08:48:16Z
> **关闭时间**: 2021-01-06T11:56:18Z
> **作者**: ronihaddad
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1184

## 描述

Yes, we are working on the whl packages which are build with ROCm3.5 user bit packages. Those will be updated very soon.

_Originally posted by @sunway513 in https://github.com/RadeonOpenCompute/ROCm/issues/1126#issuecomment-639083730_





I recently encountered this error while running tensorflow-rocm version 1.14.5 Im using python 3.7.5 adn the issue persists when I use python 3.6.8 as well.
Im using ubuntu 19.10 and ROCM 3.5



heres the full error message:
```


`>>> import tensorflow
Traceback (most recent call last):
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/home/roni/ve/ve/lib/python3.7/imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "/home/roni/ve/ve/lib/python3.7/imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: libmcwamp.so.3: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/__init__.py", line 28, in <module>
    from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/__init__.py", line 49, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow.py", line 74, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/home/roni/ve/ve/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/home/roni/ve/ve/lib/python3.7/imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "/home/roni/ve/ve/lib/python3.7/imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: libmcwamp.so.3: cannot open shared object file: No such file or directory

Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/errors

for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.
```


after days of research I found out that tensorflow 1.14.5 does not work with ROCM 3.5
but if I use tensorflow version two I get another error message because I'm using tflearn:

`ModuleNotFoundError: No module named 'tensorflow.contrib'`

So basically I cannot use tensorflow 1.14 because rocm 3.5 doesnt work with it and I cannot use tensorflow 2 because that doesnt work with tflearn.
Please help I've been trying to solve it for about a week!

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2020-12-16T11:23:00Z)

Hi @ronihaddad 
Thanks for reaching out.
I am not able to reproduce with the latest ROCm releases.
Can you please try with the latest ROCm 3.10 or 4.0 and share me an update.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-01-06T11:56:18Z)

This issue is not reproduced anymore with the latest ROCm release like ROCm 4.0.
Thank you.

---

### 评论 #3 — ronihaddad (2021-01-18T08:48:16Z)

> This issue is not reproduced anymore with the latest ROCm release like ROCm 4.0.
> Thank you.

Thanks for getting back!
I have tried to resolve the issue previously by using an older version of ubuntu I will try downloading ROCm 4.0 when I get back to that project.
Thanks again for the help!

---
