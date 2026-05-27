# Conda ROCm packages

> **Issue #621**
> **状态**: closed
> **创建时间**: 2018-11-23T06:15:34Z
> **更新时间**: 2022-02-28T10:12:19Z
> **关闭时间**: 2021-01-07T10:25:36Z
> **作者**: iamkucuk
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/621

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Hi all. I think we all know conda well. Since it is widely used and it will help the procedure for installing it correctly, conda packages like tensorflow-rocm(conda install -c rocm tensorflow-rocm) would help community a lot!


---

## 评论 (6 条)

### 评论 #1 — maxcr (2018-11-25T15:34:26Z)

Uh buddy you're asking for python wrappers in the wrong place. I'm working on getting PKGBUILDs for Arch Linux working. You'll probably need an FFI interface for the binaries to talk to Python. 

---

### 评论 #2 — Avatat (2018-11-30T01:57:28Z)

You can use `pip3 install --user tensorflow-rocm` in Anaconda environment :)

---

### 评论 #3 — isuruf (2019-11-14T02:04:37Z)

If you want to install ROCM itself with conda, you can use the `conda-forge` channel. Available packages are in https://github.com/conda-forge/staged-recipes/issues/10123. (Other packages will be added as time permits. If you want other packages, send a PR)

---

### 评论 #4 — ROCmSupport (2021-01-07T10:25:36Z)

We do not have plans to enable ROCm for conda.
You can tweak in your own ways.
Thank you.

---

### 评论 #5 — wangwendong1024 (2022-02-27T03:13:53Z)

(tf-rocm) root@ubuntuamd:/home/pi/benchmarks/scripts/tf_cnn_benchmarks# python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50 --variable_update=parameter_server
Traceback (most recent call last):
  File "/home/pi/benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py", line 38, in <module>
    import tensorflow as tf
  File "/root/.local/lib/python3.9/site-packages/tensorflow/__init__.py", line 37, in <module>
    from tensorflow.python.tools import module_util as _module_util
  File "/root/.local/lib/python3.9/site-packages/tensorflow/python/__init__.py", line 36, in <module>
    from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
  File "/root/.local/lib/python3.9/site-packages/tensorflow/python/pywrap_tensorflow.py", line 24, in <module>
    self_check.preload_check()
  File "/root/.local/lib/python3.9/site-packages/tensorflow/python/platform/self_check.py", line 65, in preload_check
    ctypes.CDLL(cpu_feature_guard_library)
  File "/root/miniconda3/envs/tf-rocm/lib/python3.9/ctypes/__init__.py", line 382, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libamdhip64.so.5: cannot open shared object file: No such file or directory


---

### 评论 #6 — ROCmSupport (2022-02-28T10:12:18Z)

**OSError: libamdhip64.so.5: cannot open shared object file: No such file or directory**
Looks like installation did not go well as its not able to find hip runtime, recommend to check rocm installation.
Thank you.


---
