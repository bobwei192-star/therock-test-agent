# ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory

- **Issue #:** 1164
- **State:** closed
- **Created:** 2020-06-24T10:50:46Z
- **Updated:** 2020-06-25T11:56:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1164

Hi!

After updating ROCm and its subsequent libraries to the newest version, I get the following error, after just calling `import tensorflow as tf` in python:
`ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory`

Previously I had a similar error, which was resolved, by installing the following libraries:
`sudo apt update && sudo apt install rocsparse hipsparse`

But now, even after I reinstalled the mentioned libraries, and also ROCm (according to the "Uninstall" and "Install" sections in the [install guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html)), I still get the same error.

Have you seen this behavior before, or do you have any suggestions, what might be the cause of this issue?

My versions (practically the latest of everything, except Ubuntu, which is LTS):
Ubuntu 18.04
ROCm 3.5.1-34
tensorflow-rocm 2.2.0
Python 3.7.6

Hardware:
Ryzen 2600
Vega 56

Thanks