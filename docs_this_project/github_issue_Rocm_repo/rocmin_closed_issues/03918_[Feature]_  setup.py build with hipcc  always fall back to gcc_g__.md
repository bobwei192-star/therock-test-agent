# [Feature]:  setup.py build with hipcc  always fall back to gcc/g++

- **Issue #:** 3918
- **State:** closed
- **Created:** 2024-10-18T06:27:07Z
- **Updated:** 2024-10-23T07:16:31Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3918

### Suggestion Description

hi, rocm expert, I am trying to build a rocm lib as an python package with setuptools. I tried a few ways, neither works, can someone give a hint ?


```py
ext_modules = [
    CppExtension(
        "mylib",
        [$csrc],
        include_dirs = ["/opt/rocm/include/"],
        library_dirs = ["/opt/rocm/lib/"],
        libraries = ["hiprtc", "hipblas"],
        extra_compile_args={
            "hipcc": hipcc_flags,
        },
        extra_link_args = ["-L/opt/rocm/lib", "-lhiprtc", "-lhipblas"], #  Linking HIP runtime and HIPBL
    )
]
```

the build is always fallback to `c++/gcc`, rather `hipcc` as I wanted.  also tried to replace `CppExtention` with `CUDAExtention`, neither works.

 [torch issue](https://github.com/pytorch/pytorch/pull/35897), looks CppExtension has supported for hipcc, or do we need a customized hipcppExtension ?

Thanks again
David 




### Operating System

Ubuntu 22.04

### GPU

mi300

### ROCm Component

6.2.2