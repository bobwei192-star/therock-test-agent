# [Issue]: ROCm fails to offload when `LIBRARY_PATH` contains other `lib` path

- **Issue #:** 3875
- **State:** closed
- **Created:** 2024-10-09T11:02:51Z
- **Updated:** 2024-11-12T21:45:48Z
- **Labels:** Under Investigation, AMD Instinct MI250X, ROCm 6.0.0, ROCm 5.7.1, ROCm 5.7.0, ROCm 6.1.0, ROCm 6.2.0, AMD Radeon RX 7900 GRE
- **URL:** https://github.com/ROCm/ROCm/issues/3875

### Problem Description

HPC systems commonly like to use some kind of system to manage programs and libraries and offer them to users. 
Some of these options include OpenHPC, EasyBuild and Spack. However, users can also manually write and maintain their modules with something like `Lmod`.

---

When trying to do offloading on such a system, the chance is high that it will simply fail. The error message on older ROCm versions is completely confusing, newer ones are a bit better in that regard.

ROCm 5.7.0:
```console
$ amdclang -fopenmp --offload-arch=gfx90a test.c
/opt/apps/software/ROCm/5.7.0/llvm/bin/llvm-link: No such file or directory
clang: error: amdgcn-link command failed with exit code 1 (use -v to see invocation)
```

ROCm 6.2.0:
```console
$ amdclang -fopenmp --offload-arch=gfx90a test.c
/opt/apps/software/ROCm/6.2.0/lib/llvm/bin/llvm-link: No such file or directory: '[SOME_OTHER_MODULE_PREFIX]/lib/libomptarget-amdgpu-gfx90a.bc'
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

ROCm will not choose the library folder of ROCm itself. Instead, the bytecode file is searched in the _first_ path in `LIBRARY_PATH` which contains `/lib` in its folder name. This breaks for EasyBuild easily.

On [LUMI](https://lumi-supercomputer.eu/) for example, just doing the following commands is sufficient to trigger the issue:

```console
$ module load LUMI/24.03 partition/G PrgEnv-amd

Lmod is automatically replacing "craype-x86-rome" with "craype-x86-trento".


Lmod is automatically replacing "craype-accel-host" with "craype-accel-amd-gfx90a".


Lmod is automatically replacing "cce/17.0.1" with "amd/6.0.3".


Lmod is automatically replacing "PrgEnv-cray/8.5.0" with "PrgEnv-amd/8.5.0".


Due to MODULEPATH changes, the following have been reloaded:
  1) cray-libsci/24.03.0

The following have been reloaded with a version change:
  1) cray-mpich/8.1.29 => cray-mpich/8.1.28

$ module load libunwind/1.6.2-cpeAMD-24.03

Lmod is automatically replacing "PrgEnv-amd/8.5.0" with "cpeAMD/24.03".


The following have been reloaded with a version change:
  1) cray-mpich/8.1.28 => cray-mpich/8.1.29

$ cc -fopenmp test.c
/opt/rocm-6.0.3/lib/llvm/bin/llvm-link: No such file or directory
clang: error: amdgcn-link command failed with exit code 1 (use -v to see invocation)
```

### Operating System

Ubuntu 22.04 / SLES

### CPU

-/-

### GPU

AMD Instinct MI250X, AMD Radeon RX 7900 GRE

### ROCm Version

ROCm 6.2.0, ROCm 6.1.0, ROCm 6.0.0, ROCm 5.7.1, ROCm 5.7.0

### ROCm Component

llvm-project, ROCm

### Steps to Reproduce

This is extremely easy to reproduce.

#### On a system with an environment system and a ROCm module

With a ROCm module loaded, e.g. 
```lua
------------------------------------------------------------------------------
   /opt/cray/pe/lmod/modulefiles/core/rocm/6.0.3.lua:
------------------------------------------------------------------------------
unsetenv("CRAY_LMOD_AMD_CONTROL_TK_LOAD")
help([[6.0.3
/opt/rocm-6.0.3
This modulefile defines the system paths and environment
variables needed to use the ROCm Toolkit. The ROCm modulefile
enables ROC Profiler, ROC Tracer, HIP, and ROCr.

This module is required to interface with AMD accelerators for
all programming environments.

To use CPE's AMD environment with amd libraries, load the amd
modulefile. The core "amd" compiler modulefile is required if access
to AMD compatible libraries is necessary.

Mixed compiler modules (such as amd-mixed) do not extend the CPE Lmod
hierarchy and can be loaded with core compilers (such as cce).

===================================================================
To see AMD/6.0.3 release information,
  visit https://rocmdocs.amd.com/en/latest
===================================================================

To make this the default version, execute:
/opt/admin-pe/set_default_craypkg/set_default_rocm_6.0.3

Certain components, files or programs contained within this package or
product are Copyright 2021-2023 Hewlett Packard Enterprise Development LP.

]])
whatis("Defines the system paths and environment variables required for the ROCm Toolkit.")
setenv("CRAY_ROCM_DIR","/opt/rocm-6.0.3")
setenv("CRAY_ROCM_PREFIX","/opt/rocm-6.0.3")
setenv("CRAY_ROCM_VERSION","6.0.3")
setenv("ROCM_PATH","/opt/rocm-6.0.3")
setenv("HIP_LIB_PATH","/opt/rocm-6.0.3/lib")
prepend_path("PATH","/opt/rocm-6.0.3/bin")
prepend_path("MANPATH","/opt/rocm-6.0.3/share/man")
prepend_path("CMAKE_PREFIX_PATH","/opt/rocm-6.0.3/lib/cmake/hip")
setenv("CRAY_ROCM_INCLUDE_OPTS","-I/opt/rocm-6.0.3/include -I/opt/rocm-6.0.3/include/rocprofiler -I/opt/rocm-6.0.3/include/roctracer -I/opt/rocm-6.0.3/include/hip -D__HIP_PLATFORM_AMD__")
setenv("CRAY_ROCM_POST_LINK_OPTS"," -L/opt/rocm-6.0.3/lib -L/opt/rocm-6.0.3/lib/rocprofiler -L/opt/rocm-6.0.3/lib/roctracer -lamdhip64")
prepend_path("LD_LIBRARY_PATH","/opt/rocm-6.0.3/lib")
prepend_path("LD_LIBRARY_PATH","/opt/rocm-6.0.3/lib/rocprofiler")
prepend_path("LD_LIBRARY_PATH","/opt/rocm-6.0.3/lib/roctracer")
append_path("PE_PRODUCT_LIST","CRAY_ROCM")
prepend_path("PKG_CONFIG_PATH","/usr/lib64/pkgconfig")
prepend_path("PE_PKGCONFIG_LIBS","rocm-6.0.3")
```

try the following steps:

```console
$ export LIBRARY_PATH=/lib:${LIBRARY_PATH}
$ echo "int main(){return 0;}" >> test.c
$ amdclang -fopenmp --offload-arch=gfx90a test.c
```

This will end in the error message shown above.

#### In the ROCm Docker container

One is not required to have any environment system present. The issue can also be triggered completely manually with the following steps.

```console
$ docker run -it rocm/dev-ubuntu-22.04:6.2.1
$ echo "int main(){return 0;}" > test.c
$ env
HOSTNAME=81f80725142e
PWD=/
HOME=/root
LS_COLORS=[...]
TERM=xterm
SHLVL=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_=/usr/bin/env
$ # First, show that building works fine when not changing the environment.
$ # ROCm is not in PATH by default, so use absolute path
$ /opt/rocm/bin/amdclang -fopenmp --offload-arch=gfx90a test.c && echo "Success"
Success
$ export LIBRARY_PATH=/lib:${LIBRARY_PATH}
$ /opt/rocm/bin/amdclang -fopenmp --offload-arch=gfx90a test.c && echo "Success"
/opt/rocm-6.2.1/lib/llvm/bin/llvm-link: No such file or directory: '/lib/libomptarget-amdgpu-gfx90a.bc'
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

It's worth noting that only ROCm has this issue. Upstream LLVM works completely fine:

```console
$ module load Clang/18.1.8 ROCm
$ export LIBRARY_PATH=/lib:${LIBRARY_PATH}
$ clang -fopenmp --offload-arch=gfx1101 test.c 
$ echo $?
0
```