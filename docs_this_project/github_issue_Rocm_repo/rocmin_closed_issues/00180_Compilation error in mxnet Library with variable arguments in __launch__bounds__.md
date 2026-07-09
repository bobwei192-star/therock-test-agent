# Compilation error in mxnet Library with variable arguments in __launch__bounds__

- **Issue #:** 180
- **State:** closed
- **Created:** 2017-08-11T12:43:04Z
- **Updated:** 2017-10-11T09:51:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/180

Background: Porting Mxnet Deep Learning framework to ROCm Platform

Issue: Compilaton error while passing variable arguments to __launch__bounds__. (see log for reference)


Please support for fixing the variable arguments instantiation.


Url for reference:

https://github.com/ROCmSoftwarePlatform/mxnet/tree/master/src

The reference file src/operator/nn/../tensor/broadcast_reduce-inl.cuh in mxnet and line number 14


---------------------------------------------------------------------------------------------
Error log :
--------------------------------------------------------------------------------------------
src/operator/nn/../tensor/broadcast_reduce-inl.cuh:14:1: error: unknown type name '__launch_bounds__'
__launch_bounds__(kMaxThreadsPerBlock)
^
src/operator/nn/../tensor/broadcast_reduce-inl.cuh:15:1: error: expected unqualified-id
__global__ void binary_broadcast_kernel(const int N, const bool addto,
^
/opt/rocm/include/hip/hcc_detail/host_defines.h:51:20: note: expanded from macro '__global__'
#define __global__ __attribute__((hc, weak))
                   ^
In file included from src/operator/nn/softmax.cc:6:
In file included from src/operator/nn/./softmax-inl.h:14:
In file included from src/operator/nn/../tensor/broadcast_reduce_op.h:15:
In file included from src/operator/nn/../tensor/./elemwise_binary_broadcast_op.h:18:
In file included from src/operator/nn/../tensor/./broadcast_reduce-inl.h:156:
src/operator/nn/../tensor/broadcast_reduce-inl.cuh:58:33: error: too few arguments provided to function-like macro invocation
__launch_bounds__(nthread_reduce)
                                ^
/opt/rocm/include/hip/hcc_detail/hip_runtime.h:151:9: note: macro '__launch_bounds__' defined here
#define __launch_bounds__(requiredMaxThreadsPerBlock, minBlocksPerMultiprocessor)
        ^
In file included from src/operator/nn/softmax.cc:6:
In file included from src/operator/nn/./softmax-inl.h:14:
In file included from src/operator/nn/../tensor/broadcast_reduce_op.h:15:
In file included from src/operator/nn/../tensor/./elemwise_binary_broadcast_op.h:18:
In file included from src/operator/nn/../tensor/./broadcast_reduce-inl.h:156:
src/operator/nn/../tensor/broadcast_reduce-inl.cuh:58:1: error: unknown type name '__launch_bounds__'
__launch_bounds__(nthread_reduce)
^
src/operator/nn/../tensor/broadcast_reduce-inl.cuh:59:1: error: expected unqualified-id
__global__ void reduce_kernel(const int N, const int M, const bool addto,
^
/opt/rocm/include/hip/hcc_detail/host_defines.h:51:20: note: expanded from macro '__global__'
#define __global__ __attribute__((hc, weak))
        ^