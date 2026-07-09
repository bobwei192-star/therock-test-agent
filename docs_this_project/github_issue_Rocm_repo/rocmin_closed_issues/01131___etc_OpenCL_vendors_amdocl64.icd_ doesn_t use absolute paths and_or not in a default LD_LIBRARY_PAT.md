# `/etc/OpenCL/vendors/amdocl64.icd` doesn't use absolute paths and/or not in a default LD_LIBRARY_PATH

- **Issue #:** 1131
- **State:** closed
- **Created:** 2020-06-04T14:20:31Z
- **Updated:** 2021-08-08T13:01:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/1131

Something does install `/etc/OpenCL/vendors/amdocl64.icd` but it isn't in any package, so I suspect this is put there by some post-install script, which feels unnecessary.

Also it simply doesn't work because it is only using the name of the .so file without the path:

```
$ cat /etc/OpenCL/vendors/amdocl64.icd 
libamdocl64.so
$
```

So by default `ocl-icd-libopencl1` (providing `/usr/lib/x86_64-linux-gnu/libOpenCL.so.1.0.0`)  will not be able to find it and simply ignore it.

Tested with `clinfo` version 2.2.18.04.06-1 (https://github.com/Oblomov/clinfo) and `ocl-icd-libopencl1` version 2.2.12-4 ( https://forge.imag.fr/projects/ocl-icd/ ) generic loader. 

```
$ clinfo | egrep -i 'Parallel|HSA'
$
```


Putting absolute path into the icd defintion:

```
$ cat /etc/OpenCL/vendors/amdocl64.icd
/opt/rocm-3.5.0/opencl/lib/libamdocl64.so
$
```

solves it:

```
$ clinfo | egrep -i 'Parallel|HSA'
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Name                                   AMD Accelerated Parallel Processing
  Driver Version                                  3137.0 (HSA1.1,LC)
$
```

