# "ImportError: libamdhip64.so.5: cannot open shared object file: No such file or directory" and other hip libraries

> **Issue #1753**
> **状态**: closed
> **创建时间**: 2022-06-13T16:20:48Z
> **更新时间**: 2022-11-22T13:06:32Z
> **关闭时间**: 2022-06-13T16:45:55Z
> **作者**: SandboChang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1753

## 描述

I have successfully installed ROCm 5.0 following 
https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/How_To_Install_ROCm.html#_Installation_Methods
which now I can see my Radeon VII through rocminfo.

```
sandbo@csns2:/opt/rocm-5.0.0/bin$ rocminfo
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 7 2700X Eight-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 2700X Eight-Core Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      65536(0x10000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    3981916(0x3cc25c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    3981916(0x3cc25c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    3981916(0x3cc25c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx906
  Uuid:                    GPU-ec0678e172fd5d72
  Marketing Name:          AMD Radeon VII
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      8192(0x2000) KB
  Chip ID:                 26287(0x66af)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1801
  BDFID:                   256
  Internal Node ID:        1
  Compute Unit:            60
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    2560(0xa00)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16760832(0xffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```

Following that, I tried to install two python libraries with pip3:
-  tensorflow-rocm
-  cupy-rocm-5-0
While both installed apparently successfully, upon importing them there was import error:

Within python3 from terminal,
importing tensorflow
```
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.8/dist-packages/tensorflow/__init__.py", line 37, in <module>
    from tensorflow.python.tools import module_util as _module_util
  File "/usr/local/lib/python3.8/dist-packages/tensorflow/python/__init__.py", line 36, in <module>
    from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
  File "/usr/local/lib/python3.8/dist-packages/tensorflow/python/pywrap_tensorflow.py", line 26, in <module>
    self_check.preload_check()
  File "/usr/local/lib/python3.8/dist-packages/tensorflow/python/platform/self_check.py", line 65, in preload_check
    ctypes.CDLL(cpu_feature_guard_library)
  File "/usr/lib/python3.8/ctypes/__init__.py", line 373, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory
```

importing cupy (5.0 for ROCm)
```
>>> import cupy
Traceback (most recent call last):
  File "/home/sandbo/.local/lib/python3.8/site-packages/cupy/__init__.py", line 18, in <module>
    from cupy import _core  # NOQA
  File "/home/sandbo/.local/lib/python3.8/site-packages/cupy/_core/__init__.py", line 1, in <module>
    from cupy._core import core  # NOQA
ImportError: libamdhip64.so.5: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/sandbo/.local/lib/python3.8/site-packages/cupy/__init__.py", line 20, in <module>
    raise ImportError(f'''
ImportError:
================================================================
Failed to import CuPy.

If you installed CuPy via wheels (cupy-cudaXXX or cupy-rocm-X-X), make sure that the package matches with the version of CUDA or ROCm installed.

On Linux, you may need to set LD_LIBRARY_PATH environment variable depending on how you installed CUDA/ROCm.
On Windows, try setting CUDA_PATH environment variable.

Check the Installation Guide for details:
  https://docs.cupy.dev/en/latest/install.html

Original error:
  ImportError: libamdhip64.so.5: cannot open shared object file: No such file or directory
================================================================
```


Apparently some path objects are missing. I tried to follow an older guide to do the export:
```
echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/rocprofiler/bin:/opt/rocm/opencl/bin' | sudo tee -a /etc/profile.d/rocm.sh
echo 'export PATH=$PATH:/opt/rocm-5.0.0/bin:/opt/rocm-5.0.0/rocprofiler/bin:/opt/rocm-5.0.0/opencl/bin' | sudo tee -a /etc/profile.d/rocm.sh
```

But they didn't help.
Appreciated if you could point me to what might be missing.

---

## 评论 (2 条)

### 评论 #1 — SandboChang (2022-06-13T16:45:46Z)

Solved:
Somehow in ld.so.conf.d, the rocm related stuff is only 
10-rocm-opencl.conf

Inside, there is only the line /opt/rocm-5.0.0/opencl/lib
I added the line
```
/opt/rocm/lib
```
followed by executing
sudo ldconfig

Now the import inside python3 works as expected.

---

### 评论 #2 — Martinc4321 (2022-11-22T13:06:32Z)

Hi, and many thanks.
However, to be more precise I will add more information.
For ubuntu 22.04. and ROCm version 5.3.3 which was finally the one, that was possible to install/use without issues. 
(till this error)

As you said it is necessary to add/append the line:
`/opt/rocm/lib`

However, name of file was changed, so more generally you need to look to this folder
`/etc/ld.so.conf.d/`

and look for folder that contains 'rocm'. In my case it was:
`sudo nano /etc/ld.so.conf.d/x86_64-rocm-opencl.conf`

Then, after I run mentioned command:
`sudo ldconfig`

Everything run properly.

---
