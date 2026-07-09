# transformers package does not find tensorflow package

- **Issue #:** 1371
- **State:** closed
- **Created:** 2021-02-06T02:22:36Z
- **Updated:** 2021-02-08T15:08:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/1371

```
$ pip3 list | grep tensorflow
tensorflow-datasets      4.2.0               
tensorflow-estimator     2.4.0               
tensorflow-metadata      0.27.0              
tensorflow-rocm          2.4.0              
```
```
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> import transformers as tm
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
>>> 
```

Can someone advice how to make tensorflow-rocm visible to transformers package?