# ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory

> **Issue #442**
> **状态**: closed
> **创建时间**: 2018-06-26T13:42:28Z
> **更新时间**: 2018-06-27T11:12:51Z
> **关闭时间**: 2018-06-27T11:12:51Z
> **作者**: psi43
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/442

## 描述

Hey, 

I've been using NVidia GPUs for a while now, but I wanted to try using an AMD GPU to see how they compare (and eventually switch to AMD due to NVidia's prices). 

I installed ROCm and the HelloWorld example ran through without any issues. Afterwards, I installed tensorflow-gpu and other dependencies of my machine learning project. When I try to run it, the following error comes up: 

```
Traceback (most recent call last):
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/usr/lib/python3.5/imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib/python3.5/imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "Object_detection_dir.py", line 22, in <module>
    import tensorflow as tf
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/__init__.py", line 24, in <module>
    from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/__init__.py", line 49, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/pywrap_tensorflow.py", line 74, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/home/oliverreipschlaeger/.local/lib/python3.5/site-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/usr/lib/python3.5/imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib/python3.5/imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory
```

Now I googled to find out where to get the libcublas.so.9.0 file and found out that it's one of the files installed when installing NVidia CUDA. 
Do I need to install that despite using an AMD GPU? 

As for the hardware specs, I built my PC with the readme ( https://github.com/RadeonOpenCompute/ROCm ) in mind, so hardware shouldn't be the problem. 

I would really appreciate some pointers to what to do or what I did wrong. Thank you so much! 

---

## 评论 (6 条)

### 评论 #1 — briansp2020 (2018-06-26T14:35:18Z)

How did you install tensorflow? It seems like you are running CUDA compiled version. To run ROCm version of tensorflow, you need to download tensorflow whl file manually or build from source.
I have a write up on how to install tensorflow on ROCm (for an older version) but the idea is the same.
http://briansp2020.github.io/2017/11/05/fast_ai_ROCm/

The latest whl file released is tensorflow 1.3 at http://repo.radeon.com/rocm/misc/tensorflow/

---

### 评论 #2 — whchung (2018-06-26T15:33:10Z)

/cc @parallelo for awareness

`tensorflow-gpu` on PyPI doesn't support AMD ROCm. As @briansp2020 mentioned please download TensorFlow 1.3 whl at http://repo.radeon.com/rocm/misc/tensorflow/ .

We are in the home stretch getting TensorFlow 1.8 released, whl package would be hosted on AMD website as well as PyPI.

---

### 评论 #3 — psi43 (2018-06-26T16:38:42Z)

Great, thank you @briansp2020 and @whchung. I'll try that first thing tomorrow. I just followed the instructions on how to get it to work, but I guess I must have missed that. Thank you! 

I think I saw the whl files about a week ago in the instructions but the link seemed to be dead. I'll try your suggestions, thanks a lot! 

---

### 评论 #4 — briansp2020 (2018-06-26T17:02:05Z)

@whchung It's great to hear that 1.8 will be ready soon. What will the package be called? tensorflow-rocm? 

---

### 评论 #5 — psi43 (2018-06-27T10:26:06Z)

I believe I got it to run with your suggestion (on python3). When running my .py script, I get the following output: 

```
2018-06-27 12:20:41.698509: W tensorflow/stream_executor/rocm/rocm_driver.cc:405] creating context when one is currently active; existing: 0x7f4230379570
2018-06-27 12:20:41.698624: I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] Found device 0 with properties:
name: Device 67ef
AMDGPU ISA: gfx803
memoryClockRate (GHz) 1.176
pciBusID 0000:01:00.0
Total memory: 4.00GiB
Free memory: 3.75GiB
2018-06-27 12:20:41.698644: I tensorflow/core/common_runtime/gpu/gpu_device.cc:928] DMA: 0
2018-06-27 12:20:41.698648: I tensorflow/core/common_runtime/gpu/gpu_device.cc:938] 0:   Y
2018-06-27 12:20:41.698666: I tensorflow/core/common_runtime/gpu/gpu_device.cc:996] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Device 67ef, pci bus id: 0000:01:00.0)
```
Does that mean it works? I'm unsure, because using [radeontop](https://github.com/clbr/radeontop), it shows that the GPU goes up to 2.5% in the Graphics Pipe, but it quickly goes down to 0% again. With that in mind, my CPU goes up to 100% when running the .py file. 

Using rocm-smi, the output looks as follows 

```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   43.0c   7.59W    387Mhz   300Mhz   33.73%   auto      0%
================================================================================
====================           End of ROCm SMI Log          ====================
```

Oh and @briansp2020, your tutorial was helpful, but sadly the [HipEigen](https://github.com/ROCmSoftwarePlatform/hipeigen) GitHub page and the [hip version of TensorFlow](https://github.com/ROCmSoftwarePlatform/hiptensorflow/blob/hip/README.ROCm.md) both direct to 404 Not Found pages (I'm assuming the projects restructured?)

---

### 评论 #6 — gstoner (2018-06-27T11:12:51Z)

Operator Error,  closing issue

---
