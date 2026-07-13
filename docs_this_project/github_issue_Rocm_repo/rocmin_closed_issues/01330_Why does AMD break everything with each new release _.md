# Why does AMD break everything with each new release ?

- **Issue #:** 1330
- **State:** closed
- **Created:** 2020-12-11T18:50:56Z
- **Updated:** 2021-06-06T16:35:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/1330

Today, after a system update, rocm was totally broken again. 

hipcc --version
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang++": No such file or directory at /opt/rocm-3.10.0/hip/bin/hipconfig line 141.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm-3.10.0/hip/bin/hipconfig line 142.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm-3.10.0/hip/bin/hipconfig line 145.
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang": No such file or directory at /opt/rocm/bin/hipcc line 203.
Use of uninitialized value $HIP_CLANG_VERSION in pattern match (m//) at /opt/rocm/bin/hipcc line 204.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm/bin/hipcc line 208.
Use of uninitialized value $HIP_CLANG_VERSION in concatenation (.) or string at /opt/rocm/bin/hipcc line 846.
HIP version: 3.10.20465-f9876b8d
Can't exec "/opt/rocm-3.10.0/llvm/bin/clang": No such file or directory at /opt/rocm/bin/hipcc line 895.


Looked at github:

"Upgrade to AMD ROCm v3.10 Not Supported
An upgrade from previous releases to AMD ROCm v3.10 is not supported. A fresh and clean installation of AMD ROCm v3.10 is recommended."

Sorry for the rant, but do you really think we have time to remove all AMD traces and reinstall on each update ? 