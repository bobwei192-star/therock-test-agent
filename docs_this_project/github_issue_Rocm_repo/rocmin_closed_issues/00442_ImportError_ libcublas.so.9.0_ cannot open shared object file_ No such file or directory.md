# ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory

- **Issue #:** 442
- **State:** closed
- **Created:** 2018-06-26T13:42:28Z
- **Updated:** 2018-06-27T11:12:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/442

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