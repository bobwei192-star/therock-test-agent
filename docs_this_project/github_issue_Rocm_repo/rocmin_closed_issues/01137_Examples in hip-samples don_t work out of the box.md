# Examples in hip-samples don't work out of the box

- **Issue #:** 1137
- **State:** closed
- **Created:** 2020-06-06T19:13:45Z
- **Updated:** 2021-02-15T10:36:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/1137

```
root@debian:/opt/rocm-3.5.0/hip/samples/0_Intro/square# make
../../../bin/hipify-perl square.cu > square.cpp
../../../bin/hipcc  square.cpp -o square.out
Can't exec "/opt/rocm/hcc/bin/hcc": No such file or directory at ../../../bin/hipcc line 245.
Use of uninitialized value $HCC_VERSION in pattern match (m//) at ../../../bin/hipcc line 246.
Use of uninitialized value $HCC_VERSION_MAJOR in substitution (s///) at ../../../bin/hipcc line 249.
Can't exec "/opt/rocm/hcc/bin/hcc-config": No such file or directory at ../../../bin/hipcc line 258.
Use of uninitialized value $HCC_VERSION_MAJOR in string eq at ../../../bin/hipcc line 263.
Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at ../../../bin/hipcc line 686.
Use of uninitialized value $targetsStr in substitution (s///) at ../../../bin/hipcc line 687.
Use of uninitialized value $targetsStr in split at ../../../bin/hipcc line 693.
Can't exec "/opt/rocm/hcc/bin/hcc": No such file or directory at ../../../bin/hipcc line 857.
failed to execute: No such file or directory
make: *** [Makefile:21: square.out] Error 255
$
```

