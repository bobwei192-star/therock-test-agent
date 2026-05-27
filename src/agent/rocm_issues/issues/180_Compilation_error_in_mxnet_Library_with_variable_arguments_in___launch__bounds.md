# Compilation error in mxnet Library with variable arguments in __launch__bounds__

> **Issue #180**
> **状态**: closed
> **创建时间**: 2017-08-11T12:43:04Z
> **更新时间**: 2017-10-11T09:51:39Z
> **关闭时间**: 2017-10-11T09:51:39Z
> **作者**: sriharikarnam
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/180

## 描述

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

---

## 评论 (4 条)

### 评论 #1 — whchung (2017-08-11T13:55:46Z)

@sriharikarnam could you shed some lights on the version of ROCm stack you are using. From the error log it seems you could be using an older version of HIP which doesn't support VA_ARGS. In the latest implementation it is already supported:

https://github.com/ROCm-Developer-Tools/HIP/blob/master/include/hip/hcc_detail/hip_runtime.h#L151

---

### 评论 #2 — sriharikarnam (2017-08-17T09:21:48Z)

We were using ROCm 1.5 and recently migrated to latest version of ROCm (i.e., version : 1.6.127). With the latest ROCm we are still facing below issue:

../mxnet_thrust/Thrust/thrust/system/cuda/detail/bulk/detail/cuda_launcher/triple_chevron_launcher.hpp:63:1: **error:** 'amdgpu_flat_work_group_size' attribute requires an integer constant
__bulk_launch_bounds__(block_size, 0)

**Url for `reference:**
https://github.com/ROCmSoftwarePlatform/Thrust

#
**Error Log:**

../mxnet_thrust/Thrust/thrust/system/cuda/detail/bulk/detail/cuda_launcher/triple_chevron_launcher.hpp:63:1: error: 'amdgpu_flat_work_group_size' attribute requires an integer constant
__bulk_launch_bounds__(block_size, 0)
^                      ~~~~~~~~~~
../mxnet_thrust/Thrust/thrust/system/cuda/detail/bulk/detail/cuda_launcher/triple_chevron_launcher.hpp:45:78: note: expanded from macro '__bulk_launch_bounds__'
#define __bulk_launch_bounds__(num_threads_per_block, num_blocks_per_sm) __launch_bounds__(num_threads_per_block, num_blocks_per_sm)
                                                                             ^                 ~~~~~~~~~~~~~~~~~~~~~
/opt/rocm/include/hip/hcc_detail/hip_runtime.h:160:18: note: expanded from macro '__launch_bounds__'
    __VA_ARGS__, launch_bounds_impl1, launch_bounds_impl0)(__VA_ARGS__)
                 ^                                         ~~~~~~~~~~~
/opt/rocm/include/hip/hcc_detail/hip_runtime.h:158:42: note: expanded from macro 'select_impl_'
#define select_impl_(_1, _2, impl_, ...) impl_
                                         ^
/opt/rocm/include/hip/hcc_detail/hip_runtime.h:156:20: note: expanded from macro 'launch_bounds_impl1'
    __attribute__((amdgpu_flat_work_group_size(1, requiredMaxThreadsPerBlock),\

[launch_bounds_error_log.txt](https://github.com/RadeonOpenCompute/ROCm/files/1230774/launch_bounds_error_log.txt)




---

### 评论 #3 — whchung (2017-10-06T17:02:08Z)

@sriharikarnam I've submitted a workaround branch `fix_for_ctu_hcc` to temporarily get around the launch bound error you are experiencing. please help review it.

---

### 评论 #4 — sriharikarnam (2017-10-11T09:51:39Z)

@whchung Thanks! Issue is fixed, we are doing regression testing. If we find anything abnormal will report in another ticket. Closing this

---
