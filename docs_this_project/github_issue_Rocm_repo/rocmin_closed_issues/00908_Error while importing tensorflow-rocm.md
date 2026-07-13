# Error while importing tensorflow-rocm

- **Issue #:** 908
- **State:** closed
- **Created:** 2019-10-13T09:04:43Z
- **Updated:** 2019-11-13T21:02:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/908

Hi, I followed the instructions to install rocm on Ubuntu 18.04 everythings seems to work fine, running /opt/rocm/bin/rocm-smi outputs

========================ROCm System Management Interface========================
WARNING: GPU[0] : Unable to read /sys/class/drm/card0/device/gpu_busy_percent
GPU Temp AvgPwr SCLK MCLK Fan Perf PwrCap VRAM% GPU%
0 37.0c N/A 300Mhz 1200Mhz None% auto N/A N/A N/A
==============================End of ROCm SMI Log ==============================

I trying to use Vega 11 on my Ryzen 3400G, I'm aware that I cannot run HIP, but I possibly could run opencl on this APU, my first step is to import tensorflow, but I got an error, this one:

Python 3.6.8 (default, Oct 7 2019, 12:59:55)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

import tensorflow as tf
Traceback (most recent call last):
File "", line 1, in
File "/usr/local/lib/python3.6/dist-packages/tensorflow/init.py", line 28, in
from tensorflow.python import pywrap_tensorflow # pylint: disable=unused-import
File "/usr/local/lib/python3.6/dist-packages/tensorflow/python/init.py", line 47, in
import numpy as np
ModuleNotFoundError: No module named 'numpy'

Are there any guides on how to install Tensorflow for opencl?
I'll give updates with regards to this soon. meanwhile thank you guys for this project, it really is a great thing. Cheers!