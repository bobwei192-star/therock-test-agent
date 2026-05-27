# ImportError: librocsolver.so.0: cannot open shared object file: No such file or directory

> **Issue #1563**
> **状态**: closed
> **创建时间**: 2021-08-24T05:43:55Z
> **更新时间**: 2021-09-07T12:47:13Z
> **关闭时间**: 2021-09-07T12:47:12Z
> **作者**: showrav-ansary
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1563

## 描述

I have tried many times. Install/Re-installs. Even reinstalled my OS. Changed the kernel. Nothing seems to fix it.
My Configuration:

```
 screenfetch
                          ./+o+-       showrav@WigglyTuff
                  yyyyy- -yyyyyy+      OS: Ubuntu 20.04 focal
               ://+//////-yyyyyyo      Kernel: x86_64 Linux 5.8.0-050800-generic
           .++ .:/++++++/-.+sss/`      Uptime: 25m
         .:++o:  /++++++++/:--:/-      Packages: 1850
        o:+o+:++.`..```.-/oo+++++/     Shell: bash 5.0.17
       .:+o:+o/.          `+sssoo+/    Resolution: 1360x768
  .++/+:+oo+o:`             /sssooo.   DE: GNOME 3.36.5
 /+++//+:`oo+o               /::--:.   WM: Mutter
 \+/+o+++`o++o               ++////.   WM Theme: Adwaita
  .++.o+++oo+:`             /dddhhh.   GTK Theme: Material-Black-Pistachio-4.0 [GTK2/3]
       .+.o+oo:.          `oddhhhh+    Icon Theme: Papirus
        \+.++o+o``-````.:ohdhhhhh+     Font: Ubuntu 11
         `:o+++ `ohhhhhhhhyo++os:      Disk: 52G / 247G (22%)
           .o:`.syhhhhhhh/.oo++o`      CPU: Intel Core i7-7700 @ 8x 4.2GHz [59.0°C]
               /osyyyyyyo++ooo+++/     GPU: AMD/ATI Ellesmere [Radeon RX 580]
                   ````` +oo+++o\:     RAM: 2068MiB / 23989MiB
                          `oo++.      


```
The error I am facing : 
```
>>> import tensorflow as tf
Traceback (most recent call last):
  File "/home/showrav/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 64, in <module>
    from tensorflow.python._pywrap_tensorflow_internal import *
ImportError: librocsolver.so.0: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/showrav/.local/lib/python3.8/site-packages/tensorflow/__init__.py", line 41, in <module>
    from tensorflow.python.tools import module_util as _module_util
  File "/home/showrav/.local/lib/python3.8/site-packages/tensorflow/python/__init__.py", line 40, in <module>
    from tensorflow.python.eager import context
  File "/home/showrav/.local/lib/python3.8/site-packages/tensorflow/python/eager/context.py", line 35, in <module>
    from tensorflow.python import pywrap_tfe
  File "/home/showrav/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tfe.py", line 28, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "/home/showrav/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 83, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "/home/showrav/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 64, in <module>
    from tensorflow.python._pywrap_tensorflow_internal import *
ImportError: librocsolver.so.0: cannot open shared object file: No such file or directory


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/errors

for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.

```

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-08-24T07:43:55Z)

Thanks @showrav-ansary for reaching out.
Let me look into this for you.

---

### 评论 #2 — ROCmSupport (2021-08-24T07:44:39Z)

Hi @showrav-ansary 
I am able to reproduce the problem.
Hope you have installed tensorflow-rocm as pip3 install tensorflow-rocm and tried to launch/import it as _import tensorflow as tf_.
Though librocsolver.so.0 is part of /opt/rocm/lib, its not picking it.
export LD_LIBRARY_PATH=/opt/rocm/lib solves this problem for now. But we need to fix this problem anyway.
I will file an internal ticket and assign to the developer. Will keep posting the updates.
Thank you.

---

### 评论 #3 — showrav-ansary (2021-08-26T06:10:21Z)

@ROCmSupport Thank you for replying, I had to manually install [librocsolver](https://rocsolver.readthedocs.io/en/latest/userguide_install.html) for `Ubuntu 20.04` because `librocsolver` was __NOT__ present in `/opt/rocm/lib` while `Ubuntu 18.04` did not require the manual installation. The `xenial` repo for `rocm 3.5.xx` automatically does the trick. But same is not true for `Ubuntu 20.04`.

---

### 评论 #4 — ROCmSupport (2021-09-07T11:24:10Z)

Thanks @showrav-ansary for the update.
You mean you are not observing this issue anymore?


---

### 评论 #5 — showrav-ansary (2021-09-07T12:42:49Z)

@ROCmSupport The issue is resolved.

---

### 评论 #6 — ROCmSupport (2021-09-07T12:47:12Z)

Thanks for the confirmation.
Am closing this, Thank you.

---
