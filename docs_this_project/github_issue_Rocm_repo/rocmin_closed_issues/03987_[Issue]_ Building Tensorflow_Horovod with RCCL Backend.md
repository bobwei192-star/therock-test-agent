# [Issue]: Building Tensorflow/Horovod with RCCL Backend 

- **Issue #:** 3987
- **State:** closed
- **Created:** 2024-11-04T04:10:11Z
- **Updated:** 2025-05-29T06:37:07Z
- **Labels:** Under Investigation, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3987

### Problem Description

The current ROCm documentation outlines methods to build/install TensorFlow2. 
However, a crucial component for multi-GPU scaling is neglected, i.e. `horovod`.  

Here, building `horovod` with RCCL backend fails during configure stage.    

### Operating System

RHEL 8.9

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 6.1.0

### ROCm Component

rccl

### Steps to Reproduce

```
$ conda create -n tf+rocm_6.1+mpich python=3.10
$ conda activate tf+rocm_6.1+mpich  

$ pip install  tensorflow-rocm==2.15.0 -f https://repo.radeon.com/rocm/manylinux/rocm-rel-6.1/ 

$ module purge 
$ module load cmake/3.30.1
$ module load PrgEnv-cray/8.5.0 craype-x86-genoa  craype-accel-amd-gfx942 rocm/6.1.1

$ export HOROVOD_WITH_TENSORFLOW=1 
$ export HOROVOD_GPU=ROCM 
$ export HOROVOD_GPU_OPERATIONS=NCCL 
$ export HOROVOD_ROCM_PATH=$ROCM_PATH 

$ pip install --no-cache-dir --force-reinstall git+https://github.com/horovod/horovod.git@v0.28.1

   -- Build Horovod for ROCm
      CMake Error at horovod/common/ops/rocm/CMakeLists.txt:21 (hip_add_library):
        Unknown CMake command "hip_add_library".
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

- Despite using a recent version of cmake, there error indicates that `hip_add_library` command is not available. 
- I have tried containers provided at https://hub.docker.com/r/rocm/tensorflow, unfortunately they are built without `horovod`. 

### Additional Information

_No response_