# ImportError: librocblas.so.0: cannot open shared object file: No such file or directory

- **Issue #:** 1621
- **State:** closed
- **Created:** 2021-11-18T14:40:53Z
- **Updated:** 2021-11-22T07:36:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/1621

Hello, I have installed tensorflow on ROCm in my Ubuntu 20.04 distro.
I have followed all the step provided in the official ROCm [page](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html).

I also have installed tensorflow-rocm following the guide [here](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html).

Now I am facing the following issue while trying to 
`import tensorflow`
**ImportError: librocblas.so.0: cannot open shared object file: No such file or directory**

This is the full traceback of the execution:

> Traceback (most recent call last):
>   File "/home/raffaele/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 64, in <module>
>     from tensorflow.python._pywrap_tensorflow_internal import *
> ImportError: librocblas.so.0: cannot open shared object file: No such file or directory
> 
> During handling of the above exception, another exception occurred:
> 
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "/home/raffaele/.local/lib/python3.8/site-packages/tensorflow/__init__.py", line 41, in <module>
>     from tensorflow.python.tools import module_util as _module_util
>   File "/home/raffaele/.local/lib/python3.8/site-packages/tensorflow/python/__init__.py", line 40, in <module>
>     from tensorflow.python.eager import context
>   File "/home/raffaele/.local/lib/python3.8/site-packages/tensorflow/python/eager/context.py", line 35, in <module>
>     from tensorflow.python import pywrap_tfe
>   File "/home/raffaele/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tfe.py", line 28, in <module>
>     from tensorflow.python import pywrap_tensorflow
>   File "/home/raffaele/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 83, in <module>
>     raise ImportError(msg)
> ImportError: Traceback (most recent call last):
>   File "/home/raffaele/.local/lib/python3.8/site-packages/tensorflow/python/pywrap_tensorflow.py", line 64, in <module>
>     from tensorflow.python._pywrap_tensorflow_internal import *
> ImportError: librocblas.so.0: cannot open shared object file: No such file or directory
> 
> 
> Failed to load the native TensorFlow runtime.
> 
> See https://www.tensorflow.org/install/errors
> 
> for some common reasons and solutions.  Include the entire stack trace
> above this error message when asking for help.

My configuration is:
_AMD Ryzen 5 3600
AMD Radeon RX 5600 XT_

I am quite a newbie to linux, maybe I am missing something stupid. I don't know.
Thanks for the help