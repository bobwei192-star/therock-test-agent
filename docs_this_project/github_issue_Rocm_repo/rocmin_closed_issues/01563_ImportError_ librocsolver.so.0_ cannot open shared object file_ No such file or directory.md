# ImportError: librocsolver.so.0: cannot open shared object file: No such file or directory

- **Issue #:** 1563
- **State:** closed
- **Created:** 2021-08-24T05:43:55Z
- **Updated:** 2021-09-07T12:47:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/1563

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