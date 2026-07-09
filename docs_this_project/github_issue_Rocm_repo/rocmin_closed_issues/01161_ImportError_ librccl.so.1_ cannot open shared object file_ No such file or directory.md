# ImportError: librccl.so.1: cannot open shared object file: No such file or directory

- **Issue #:** 1161
- **State:** closed
- **Created:** 2020-06-23T12:12:57Z
- **Updated:** 2021-08-10T13:48:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/1161

Hello, I am trying to install rocm but got the above error when trying to import tensorflow
" ImportError: librccl.so.1: cannot open shared object file: No such file or directory "
My set up is:

ubuntu 20.04
rocm 3.5
tensorflow-rocm 2.2.0
gpu rx580
cpu intel 9100f
( using anaconda, if that matter )

I saw some other guys has same error he fix it with:
`yum install rccl`
I used 
`sudo apt install rccl`
installing was successful but I still got same error.
What should I do?
