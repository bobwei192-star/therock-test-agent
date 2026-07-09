# [Issue]: Memory Leak using GROMACS with ROCm >= 7.1.1

- **Issue #:** 5948
- **State:** closed
- **Created:** 2026-02-10T15:57:07Z
- **Updated:** 2026-04-09T12:11:19Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5948

### Problem Description

Running GROMACS workloads with ROCm >= 7.1.1 (7.0.0 untested) we see huge memory leaks.
The leak was found after we upgraded from ROCm 6.1.3 to 7.1.1 but it is also present in 7.2.0 ~and not present in 6.4.4~
I also tested the 7.2.0 driver (30.30) with ROCm 6.1.3 but leak was still happening, which makes me believe the error is not in library but the driver.

### Operating System

Alma 9.7

### CPU

AMD EPYC 7452 32-Core Processor

### GPU

MI210

### ROCm Version

7.1.1, 7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

Because there is a difference between building GROMACS for 7.2.0 and 7.1.1, I split the reproduce steps into those versions. The instructions for 7.1.1 also work for the older ROCm versions because it still uses LLVM20 and not 22 like 7.2.0.

Depending on those differences we need slightly different versions but the concept stays the same. We build adaptivecpp and use it to build gromacs with mpi and ucx support. You need `rocm-llvm-devel` and make sure to change the GPU targets (gfx..) to whatever model you are using.

# Build

Building GROMACS with AdaptiveCpp, MPI and UCX

## 7.1.1

Get AdaptiveCpp v25.10.0 https://github.com/AdaptiveCpp/AdaptiveCpp and build with 
```
cmake .. -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang -DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm/ -DACPP_COMPILER_FEATURE_PROFILE=minimal -DCMAKE_INSTALL_PREFIX=~/.adaptivecpp
make -j
make install % To ~/.adaptivecpp where we tell gromacs to look for it
```

Get GROMACS v2025.4 https://gitlab.com/gromacs/gromacs and build with
```
cmake .. -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang -DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -DGMX_GPU=SYCL -DGMX_SYCL=ACPP -DACPP_TARGETS='hip:gfx90a' -Dadaptivecpp_DIR=~/.adaptivecpp/lib/cmake/AdaptiveCpp/ -Dhipsycl_DIR=~/.adaptivecpp/lib/cmake/hipSYCL/  -DGMX_MPI=on
```

## 7.2.0

Get AdaptiveCpp https://github.com/alexschroeter/AdaptiveCpp branch llvm-22-getDecl and build with 
```
cmake .. -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang -DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm/ -DACPP_COMPILER_FEATURE_PROFILE=minimal -DCMAKE_INSTALL_PREFIX=~/.adaptivecpp -DACPP_EXPERIMENTAL_LLVM=ON
make -j
make install % To ~/.adaptivecpp where we tell gromacs to look for it
```

Get GROMACS v2025.4 https://gitlab.com/gromacs/gromacs and build with
```
cmake .. -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang -DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -DGMX_GPU=SYCL -DGMX_SYCL=ACPP -DACPP_TARGETS='hip:gfx90a' -Dadaptivecpp_DIR=~/.adaptivecpp/lib/cmake/AdaptiveCpp/ -Dhipsycl_DIR=~/.adaptivecpp/lib/cmake/hipSYCL/  -DGMX_MPI=on
```

# Run GROMACS

Download the prod.tpr https://next.hessenbox.de/index.php/s/fKEHLSpcNYPXSa6
```
mkdir gromacs_run
cd gromacs_run
cp <path to download>/prod.tpr .
for i in {1..8}; do mkdir res$i && cp prod.tpr res$i;done
% if you have 8 gpus
mpirun -np 8 <path to gromacs build>/bin/gmx_mpi mdrun -ntomp 8 -pin on -multidir rep* -deffnm prod
% if you have 1 gpu
mpirun -np 1 <path to gromacs build>/bin/gmx_mpi mdrun -ntomp 8 -pin on -deffnm prod
```

watch the leak eat all the memory

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support


OS:
NAME="AlmaLinux"
VERSION="9.7 (Moss Jungle Cat)"

CPU:
model name      : AMD EPYC 7452 32-Core Processor

GPU:
  Name:                    AMD EPYC 7452 32-Core Processor
  Marketing Name:          AMD EPYC 7452 32-Core Processor
  Name:                    AMD EPYC 7452 32-Core Processor
  Marketing Name:          AMD EPYC 7452 32-Core Processor
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
  Name:                    gfx90a
  Marketing Name:          AMD Instinct MI210
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-

### Additional Information

_No response_