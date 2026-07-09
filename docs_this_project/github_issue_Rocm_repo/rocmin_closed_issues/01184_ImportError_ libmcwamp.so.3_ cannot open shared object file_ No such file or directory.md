# ImportError: libmcwamp.so.3: cannot open shared object file: No such file or directory

- **Issue #:** 1184
- **State:** closed
- **Created:** 2020-07-24T17:41:59Z
- **Updated:** 2021-01-18T08:48:16Z
- **URL:** https://github.com/ROCm/ROCm/issues/1184

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