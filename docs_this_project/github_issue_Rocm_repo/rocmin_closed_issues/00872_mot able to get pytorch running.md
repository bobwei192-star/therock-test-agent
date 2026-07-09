# mot able to get pytorch running

- **Issue #:** 872
- **State:** closed
- **Created:** 2019-08-21T21:01:27Z
- **Updated:** 2023-08-05T18:27:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/872

i followed this description:
[https://github.com/ROCmSoftwarePlatform/pytorch/wiki/Building-PyTorch-for-ROCm](url)

and get this issue...

`[ 44%] Linking CXX static library ../../lib/libonnx.a
[ 44%] Built target onnx
[ 44%] Building HIPCC object caffe2/CMakeFiles/torch.dir/__/aten/src/THH/torch_generated_THHBlas.hip.o
[ 44%] Building HIPCC object caffe2/CMakeFiles/torch.dir/__/aten/src/THH/torch_generated_THHStorage.hip.o
[ 44%] Building HIPCC object caffe2/CMakeFiles/torch.dir/__/aten/src/THH/torch_generated_THHSleep.hip.o
[ 44%] Building HIPCC object caffe2/CMakeFiles/torch.dir/__/aten/src/THH/torch_generated_THHReduceApplyUtils.hip.o
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:37:28: error: unknown type name 'cudaStream_t'
__host__ __device__ inline cudaStream_t default_stream()
                           ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:39:10: error: use of undeclared identifier 'cudaStreamLegacy'
  return cudaStreamLegacy;
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:43:1: error: unknown type name 'cudaStream_t'
cudaStream_t __host__ __device__ 
^
/opt/rocm/include/thrust/system/cuda/detail/par.h:50:1: error: unknown type name 'cudaError_t'
cudaError_t THRUST_RUNTIME_FUNCTION
^
/opt/rocm/include/thrust/system/cuda/detail/par.h:53:3: error: use of undeclared identifier 'cudaDeviceSynchronize'; did you mean 'hipDeviceSynchronize'?
  cudaDeviceSynchronize();
  ^~~~~~~~~~~~~~~~~~~~~
  hipDeviceSynchronize
/opt/rocm/include/hip/hcc_detail/hip_runtime_api.h:334:12: note: 'hipDeviceSynchronize' declared here
hipError_t hipDeviceSynchronize(void);
           ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:54:10: error: use of undeclared identifier 'cudaGetLastError'; did you mean 'hipGetLastError'?
  return cudaGetLastError();
         ^~~~~~~~~~~~~~~~
         hipGetLastError
/opt/rocm/include/hip/hcc_detail/hip_runtime_api.h:592:12: note: 'hipGetLastError' declared here
hipError_t hipGetLastError(void);
           ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:62:3: error: unknown type name 'cudaStream_t'
  cudaStream_t stream;
  ^
/data/pytorch/aten/src/THH/THHBlas.hip:257:17: warning: rocblas_gemm_strided_batched_ex: The workspace_size and workspace arguments are obsolete, and will be ignored [-W#pragma-messages]
  THCublasCheck(rocblas_gemm_strided_batched_ex(handle, opa, opb, (int)m, (int)n, (int)k,
                ^
/opt/rocm/rocblas/include/rocblas-functions.h:2231:41: note: expanded from macro 'rocblas_gemm_strided_batched_ex'
                                        ROCBLAS_VA_OPT_PRAGMA(GCC warning "rocblas_gemm_strided_batched_ex: The workspace_size and workspace arguments are obsolete, and will be ignored", __VA_ARGS__) \
                                        ^
/opt/rocm/rocblas/include/rocblas-functions.h:50:5: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA'
    ROCBLAS_VA_OPT_PRAGMA_IMPL(pragma, ROCBLAS_VA_OPT_COUNT(__VA_ARGS__))
    ^
/opt/rocm/rocblas/include/rocblas-functions.h:48:51: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA_IMPL'
#define ROCBLAS_VA_OPT_PRAGMA_IMPL(pragma, count) ROCBLAS_VA_OPT_PRAGMA_IMPL2(pragma, count)
                                                  ^
/opt/rocm/rocblas/include/rocblas-functions.h:47:52: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA_IMPL2'
#define ROCBLAS_VA_OPT_PRAGMA_IMPL2(pragma, count) ROCBLAS_VA_OPT_PRAGMA_SELECT##count(pragma)
                                                   ^
<scratch space>:100:1: note: expanded from here
ROCBLAS_VA_OPT_PRAGMA_SELECTN
^
/opt/rocm/rocblas/include/rocblas-functions.h:46:52: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA_SELECTN'
#define ROCBLAS_VA_OPT_PRAGMA_SELECTN(pragma, ...) _Pragma(#pragma)
                                                   ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:66:26: error: unknown type name 'cudaStream_t'
  execute_on_stream_base(cudaStream_t stream_ = default_stream())
                         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:71:10: error: unknown type name 'cudaStream_t'
      on(cudaStream_t const &s) const
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:79:10: error: unknown type name 'cudaStream_t'
  friend cudaStream_t __host__ __device__
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:85:10: error: unknown type name 'cudaError_t'
  friend cudaError_t THRUST_RUNTIME_FUNCTION
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:96:12: error: use of undeclared identifier 'cudaGetLastError'; did you mean 'hipGetLastError'?
    return cudaGetLastError();
           ^~~~~~~~~~~~~~~~
           hipGetLastError
/opt/rocm/include/hip/hcc_detail/hip_runtime_api.h:592:12: note: 'hipGetLastError' declared here
hipError_t hipGetLastError(void);
           ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:107:21: error: unknown type name 'cudaStream_t'
  execute_on_stream(cudaStream_t stream) : base_t(stream){};
                    ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:105:25: error: type 'thrust::cuda_cub::execute_on_stream::base_t' (aka 'execute_on_stream_base<thrust::cuda_cub::execute_on_stream>') is not a direct or virtual base of 'thrust::cuda_cub::execute_on_stream'
  execute_on_stream() : base_t(){};
                        ^~~~~~
/opt/rocm/include/thrust/system/cuda/detail/par.h:138:6: error: unknown type name 'cudaStream_t'
  on(cudaStream_t const &stream) const
     ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:39:
In file included from /opt/rocm/include/thrust/system/cuda/detail/copy.h:99:
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:60:5: error: unknown type name 'cudaError'
    cudaError status;
    ^
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:61:14: error: no member named 'trivial_copy_to_device' in namespace 'thrust::cuda_cub'; did you mean 'hip_rocprim::trivial_copy_from_device'?
    status = cuda_cub::trivial_copy_to_device(dst,
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             hip_rocprim::trivial_copy_from_device
/opt/rocm/include/thrust/system/hip/detail/util.h:62:1: note: 'hip_rocprim::trivial_copy_from_device' declared here
trivial_copy_from_device(Type* dst, Type const* src, size_t count, hipStream_t stream)
^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:39:
In file included from /opt/rocm/include/thrust/system/cuda/detail/copy.h:99:
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:64:47: error: no member named 'stream' in namespace 'thrust::cuda_cub'; did you mean 'hip_rocprim::stream'?
                                              cuda_cub::stream(device_s));
                                              ^~~~~~~~~~~~~~~~
                                              hip_rocprim::stream
/opt/rocm/include/thrust/system/hip/detail/util.h:55:33: note: 'hip_rocprim::stream' declared here
__host__ __device__ hipStream_t stream(execution_policy<Derived>& policy)
                                ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:39:
In file included from /opt/rocm/include/thrust/system/cuda/detail/copy.h:99:
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:65:5: error: no member named 'throw_on_error' in namespace 'thrust::cuda_cub'; did you mean 'hip_rocprim::throw_on_error'?
    cuda_cub::throw_on_error(status, "__copy::trivial_device_copy H->D: failed");
    ^~~~~~~~~~~~~~~~~~~~~~~~
    hip_rocprim::throw_on_error
/opt/rocm/include/thrust/system/hip/detail/util.h:113:33: note: 'hip_rocprim::throw_on_error' declared here
static void __host__ __device__ throw_on_error(hipError_t status, char const* msg)
                                ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated.
1 warning generated.
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:37:28: error: unknown type name 'cudaStream_t'
__host__ __device__ inline cudaStream_t default_stream()
                           ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:39:10: error: use of undeclared identifier 'cudaStreamLegacy'
  return cudaStreamLegacy;
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:43:1: error: unknown type name 'cudaStream_t'
cudaStream_t __host__ __device__ 
^
/opt/rocm/include/thrust/system/cuda/detail/par.h:50:1: error: unknown type name 'cudaError_t'
cudaError_t THRUST_RUNTIME_FUNCTION
^
/opt/rocm/include/thrust/system/cuda/detail/par.h:53:3: error: use of undeclared identifier 'cudaDeviceSynchronize'; did you mean 'hipDeviceSynchronize'?
  cudaDeviceSynchronize();
  ^~~~~~~~~~~~~~~~~~~~~
  hipDeviceSynchronize
/opt/rocm/include/hip/hcc_detail/hip_runtime_api.h:334:12: note: 'hipDeviceSynchronize' declared here
hipError_t hipDeviceSynchronize(void);
           ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:54:10: error: use of undeclared identifier 'cudaGetLastError'; did you mean 'hipGetLastError'?
  return cudaGetLastError();
         ^~~~~~~~~~~~~~~~
         hipGetLastError
/opt/rocm/include/hip/hcc_detail/hip_runtime_api.h:592:12: note: 'hipGetLastError' declared here
hipError_t hipGetLastError(void);
           ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:62:3: error: unknown type name 'cudaStream_t'
  cudaStream_t stream;
  ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:66:26: error: unknown type name 'cudaStream_t'
  execute_on_stream_base(cudaStream_t stream_ = default_stream())
                         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:71:10: error: unknown type name 'cudaStream_t'
      on(cudaStream_t const &s) const
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:79:10: error: unknown type name 'cudaStream_t'
  friend cudaStream_t __host__ __device__
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:85:10: error: unknown type name 'cudaError_t'
  friend cudaError_t THRUST_RUNTIME_FUNCTION
         ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:96:12: error: use of undeclared identifier 'cudaGetLastError'; did you mean 'hipGetLastError'?
    return cudaGetLastError();
           ^~~~~~~~~~~~~~~~
           hipGetLastError
/opt/rocm/include/hip/hcc_detail/hip_runtime_api.h:592:12: note: 'hipGetLastError' declared here
hipError_t hipGetLastError(void);
           ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:34:
/opt/rocm/include/thrust/system/cuda/detail/par.h:107:21: error: unknown type name 'cudaStream_t'
  execute_on_stream(cudaStream_t stream) : base_t(stream){};
                    ^
/opt/rocm/include/thrust/system/cuda/detail/par.h:105:25: error: type 'thrust::cuda_cub::execute_on_stream::base_t' (aka 'execute_on_stream_base<thrust::cuda_cub::execute_on_stream>') is not a direct or virtual base of 'thrust::cuda_cub::execute_on_stream'
  execute_on_stream() : base_t(){};
                        ^~~~~~
/opt/rocm/include/thrust/system/cuda/detail/par.h:138:6: error: unknown type name 'cudaStream_t'
  on(cudaStream_t const &stream) const
     ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:39:
In file included from /opt/rocm/include/thrust/system/cuda/detail/copy.h:99:
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:60:5: error: unknown type name 'cudaError'
    cudaError status;
    ^
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:61:14: error: no member named 'trivial_copy_to_device' in namespace 'thrust::cuda_cub'; did you mean 'hip_rocprim::trivial_copy_from_device'?
    status = cuda_cub::trivial_copy_to_device(dst,
             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             hip_rocprim::trivial_copy_from_device
/opt/rocm/include/thrust/system/hip/detail/util.h:62:1: note: 'hip_rocprim::trivial_copy_from_device' declared here
trivial_copy_from_device(Type* dst, Type const* src, size_t count, hipStream_t stream)
^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:39:
In file included from /opt/rocm/include/thrust/system/cuda/detail/copy.h:99:
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:64:47: error: no member named 'stream' in namespace 'thrust::cuda_cub'; did you mean 'hip_rocprim::stream'?
                                              cuda_cub::stream(device_s));
                                              ^~~~~~~~~~~~~~~~
                                              hip_rocprim::stream
/opt/rocm/include/thrust/system/hip/detail/util.h:55:33: note: 'hip_rocprim::stream' declared here
__host__ __device__ hipStream_t stream(execution_policy<Derived>& policy)
                                ^
In file included from /data/pytorch/aten/src/THH/THHStorage.hip:7:
In file included from /opt/rocm/include/thrust/system/cuda/execution_policy.h:39:
In file included from /opt/rocm/include/thrust/system/cuda/detail/copy.h:99:
/opt/rocm/include/thrust/system/cuda/detail/internal/copy_cross_system.h:65:5: error: no member named 'throw_on_error' in namespace 'thrust::cuda_cub'; did you mean 'hip_rocprim::throw_on_error'?
    cuda_cub::throw_on_error(status, "__copy::trivial_device_copy H->D: failed");
    ^~~~~~~~~~~~~~~~~~~~~~~~
    hip_rocprim::throw_on_error
/opt/rocm/include/thrust/system/hip/detail/util.h:113:33: note: 'hip_rocprim::throw_on_error' declared here
static void __host__ __device__ throw_on_error(hipError_t status, char const* msg)
                                ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated.
CMake Error at torch_generated_THHStorage.hip.o.cmake:174 (message):
  Error generating file
  /data/pytorch/build/caffe2/CMakeFiles/torch.dir/__/aten/src/THH/./torch_generated_THHStorage.hip.o


caffe2/CMakeFiles/torch.dir/build.make:84: recipe for target 'caffe2/CMakeFiles/torch.dir/__/aten/src/THH/torch_generated_THHStorage.hip.o' failed
make[2]: *** [caffe2/CMakeFiles/torch.dir/__/aten/src/THH/torch_generated_THHStorage.hip.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/data/pytorch/aten/src/THH/THHBlas.hip:257:17: warning: rocblas_gemm_strided_batched_ex: The workspace_size and workspace arguments are obsolete, and will be ignored [-W#pragma-messages]
  THCublasCheck(rocblas_gemm_strided_batched_ex(handle, opa, opb, (int)m, (int)n, (int)k,
                ^
/opt/rocm/rocblas/include/rocblas-functions.h:2231:41: note: expanded from macro 'rocblas_gemm_strided_batched_ex'
                                        ROCBLAS_VA_OPT_PRAGMA(GCC warning "rocblas_gemm_strided_batched_ex: The workspace_size and workspace arguments are obsolete, and will be ignored", __VA_ARGS__) \
                                        ^
/opt/rocm/rocblas/include/rocblas-functions.h:50:5: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA'
    ROCBLAS_VA_OPT_PRAGMA_IMPL(pragma, ROCBLAS_VA_OPT_COUNT(__VA_ARGS__))
    ^
/opt/rocm/rocblas/include/rocblas-functions.h:48:51: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA_IMPL'
#define ROCBLAS_VA_OPT_PRAGMA_IMPL(pragma, count) ROCBLAS_VA_OPT_PRAGMA_IMPL2(pragma, count)
                                                  ^
/opt/rocm/rocblas/include/rocblas-functions.h:47:52: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA_IMPL2'
#define ROCBLAS_VA_OPT_PRAGMA_IMPL2(pragma, count) ROCBLAS_VA_OPT_PRAGMA_SELECT##count(pragma)
                                                   ^
<scratch space>:100:1: note: expanded from here
ROCBLAS_VA_OPT_PRAGMA_SELECTN
^
/opt/rocm/rocblas/include/rocblas-functions.h:46:52: note: expanded from macro 'ROCBLAS_VA_OPT_PRAGMA_SELECTN'
#define ROCBLAS_VA_OPT_PRAGMA_SELECTN(pragma, ...) _Pragma(#pragma)
                                                   ^
1 warning generated.
CMakeFiles/Makefile2:5573: recipe for target 'caffe2/CMakeFiles/torch.dir/all' failed
make[1]: *** [caffe2/CMakeFiles/torch.dir/all] Error 2
Makefile:138: recipe for target 'all' failed
make: *** [all] Error 2
Traceback (most recent call last):
  File "setup.py", line 756, in <module>
    build_deps()
  File "setup.py", line 321, in build_deps
    cmake=cmake)
  File "/data/pytorch/tools/build_pytorch_libs.py", line 63, in build_caffe2
    cmake.build(my_env)
  File "/data/pytorch/tools/setup_helpers/cmake.py", line 330, in build
    self.run(build_args, my_env)
  File "/data/pytorch/tools/setup_helpers/cmake.py", line 143, in run
    check_call(command, cwd=self.build_dir, env=env)
  File "/usr/lib/python3.6/subprocess.py", line 311, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['cmake', '--build', '.', '--target', 'install', '--config', 'Release', '--', '-j', '4']' returned non-zero exit status 2.
+ cleanup
+ retcode=1
+ set +x
=================== sccache compilation log ===================
=========== If your build fails, please take a look at the log above for possible reasons ===========
Compile requests                 0
Compile requests executed        0
Cache hits                       0
Cache misses                     0
Cache timeouts                   0
Cache read errors                0
Forced recaches                  0
Cache write errors               0
Compilation failures             0
Cache errors                     0
Non-cacheable compilations       0
Non-cacheable calls              0
Non-compilation calls            0
Unsupported compiler calls       0
Average cache write          0.000 s
Average cache read miss      0.000 s
Average cache read hit       0.000 s
Cache location             Local disk: "/root/.cache/sccache"
Cache size                     181 MiB
Max cache size                  10 GiB
Stopping sccache server...
Compile requests                 0
Compile requests executed        0
Cache hits                       0
Cache misses                     0
Cache timeouts                   0
Cache read errors                0
Forced recaches                  0
Cache write errors               0
Compilation failures             0
Cache errors                     0
Non-cacheable compilations       0
Non-cacheable calls              0
Non-compilation calls            0
Unsupported compiler calls       0
Average cache write          0.000 s
Average cache read miss      0.000 s
Average cache read hit       0.000 s
Cache location             Local disk: "/root/.cache/sccache"
Cache size                     181 MiB
Max cache size                  10 GiB
cache directory                     /root/.ccache
primary config                      /root/.ccache/ccache.conf
secondary config      (readonly)    /usr/local/etc/ccache.conf
cache hit (direct)                     0
cache hit (preprocessed)               0
cache miss                             0
cache hit rate                      0.00 %
cleanups performed                     0
files in cache                         0
cache size                           0.0 kB
max cache size                       5.0 GB
`