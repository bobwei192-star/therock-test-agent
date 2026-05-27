# OpenCL missing libhsa-ext-finalize64.so.1

> **Issue #537**
> **状态**: closed
> **创建时间**: 2018-09-15T14:12:57Z
> **更新时间**: 2018-12-05T01:44:59Z
> **关闭时间**: 2018-10-21T19:49:50Z
> **作者**: sjug
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/537

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

After installing the OpenCL path for ROCm 1.9, and following the [HelloWorld test](https://github.com/RadeonOpenCompute/ROCm#upon-restart-to-test-your-opencl-instance). 

I'm unable to run `HelloWorld` as I get the error:
```
[user@host test]$ ./HelloWorld
LoadLib(libhsa-ext-finalize64.so.1) failed: libhsa-ext-finalize64.so.1: cannot open shared object file: No such file or directory
Segmentation fault (core dumped)
```

I've tried on Ubuntu and Fedora and both of them have the same issue. This library `libhsa-ext-finalize64.so.1` is not found in any package in the repo.

---

## 评论 (32 条)

### 评论 #1 — jlgreathouse (2018-09-15T21:52:59Z)

What commands did you run to perform this installation? Was this a clean installation or an upgrade from a previous version of ROCm?

Could you show me the output of the following commands?
`clinfo`
(on Ubuntu): `apt list | grep rocm`



---

### 评论 #2 — sjug (2018-09-15T23:26:20Z)

It was a clean installation of ROCm, I just installed `rocm-opencl` and then manually had to install `hsa-amd-aqlprofile` as well because I was getting errors about `libhsa-amd-aqlprofile64.so.1` missing.


```
[user@host ~]$ clinfo                                   
LoadLib(libhsa-ext-finalize64.so.1) failed: libhsa-ext-finalize64.so.1: cannot open shared object file: No such file or directory
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP.internal (2574.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 
  Platform Max metadata object keys (AMD)         8
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx900
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  2574.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Vega 10 XT [Radeon RX Vega 64]
  Device Topology (AMD)                           PCI-E, 46:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               64
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1630MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     (n/a)
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple              64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              8573157376 (7.984GiB)
  Global free memory (AMD)                        8370176 (7.982GiB)
  Global memory channels (AMD)                    64
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           7287183769 (6.787GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26751
    Max size for 1D images from buffer            65536 pixels
    Max 1D or 2D image array size                 2048 images
    Max 2D image size                             16384x16384 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                8
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        7287183769 (6.787GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  P2P devices (AMD)                               (n/a)
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 19:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             64
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.12
  ICD loader Profile                              OpenCL 2.2
```

Packages:
```
hsakmt-roct 1.0.9-8
hsa-amd-aqlprofile 1.0.0-1
hsa-ext-rocr-dev 1.1.9-8
hsa-rocr-dev 1.1.9-8
rocm-opencl 1.2.0
```

---

### 评论 #3 — jlgreathouse (2018-09-15T23:44:39Z)

"Driver 2574" is the OpenCL runtime from ROCm 1.8.x, so it looks like some part of your installation process did not work properly.

What commands did you run to perform this installation?
Was this a clean installation or an upgrade from a previous version of ROCm?

In addition, could you show the entire output of the following commands?
`which clinfo`
``ldd `which clinfo` ``
`cat /etc/OpenCL/vendors/amdocl64.icd`
``find /opt -name `cat /etc/OpenCL/vendors/amdocl64.icd` ``
`apt list | grep rocm` (looking for the full output of this)
`apt list --installed | grep ^roc`

---

### 评论 #4 — sjug (2018-09-16T01:25:40Z)

Ah I think it might be because I tried to compile the https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime, but it doesn't have a `roc-1.9.x` branch so I built off master.

which clinfo:
`/usr/bin/clinfo`

ldd `which clinfo`:
```
        linux-vdso.so.1 (0x00007fff869d7000)
        libOpenCL.so.1 => /usr/lib/libOpenCL.so.1 (0x00007fa86f150000)
        libdl.so.2 => /usr/lib/libdl.so.2 (0x00007fa86f14b000)
        libc.so.6 => /usr/lib/libc.so.6 (0x00007fa86ef87000)
        /lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fa86f5b3000)
```

cat /etc/OpenCL/vendors/amdocl64.icd:
`libamdocl64.so`

find /opt -name `cat /etc/OpenCL/vendors/amdocl64.icd`:
`/opt/rocm/opencl/lib/libamdocl64.so`

I don't have access to Ubuntu right now for the apt specifics.

---

### 评论 #5 — jlgreathouse (2018-09-16T03:54:25Z)

Hi @sjug 

I just build from ROCm-OpenCL-Runtime on the master branch, and I am unable to reproduce this problem on Ubuntu 16.04/ROCm 1.9.

One note: `clinfo` is not normally installed into /usr/bin/clinfo -- this is the normal 'apt' clinfo, rather than the one that comes with ROCm, so I'm a little worried about how exactly you went about installing ROCm.

Rather than installing Ubuntu a few times over the weekend to try to guess at a way to reproduce your issue (  :)  )  -- could you give me a step-by-step list of what you did so that I can try to reproduce it? This will help me fix the issue for you.

---

### 评论 #6 — jlgreathouse (2018-09-16T03:55:52Z)

Oh, I suppose something to note: if you are building your own OpenCL runtime from ROCm-OpenCL-Runtime, make sure that you either install it, or set `LD_LIBRARY_PATH` to point to the `build/lib` directory which contains the newly-built `libamdocl64.so`

---

### 评论 #7 — sjug (2018-09-16T03:58:20Z)

Thanks @jlgreathouse let me try to sort out this mess before you spend any more time on it.

---

### 评论 #8 — jlgreathouse (2018-09-16T04:35:30Z)

Hi @sjug 

I don't mean to take an aggressive stance or anything like that. I'm hoping that fixing your issue won't be too hard -- if I can figure out how to recreate the problem, I can hopefully help track down what went wrong and give you a workaround or a fix. :)

My first worry was that our 1.9.0 release to the OpenCL runtime source code repo was out of sync with the code we released, but I don't think that's the case since I was able to build a working OpenCL installation from the current GitHub repo.

The error message you're seeing -- that the HSAIL finalizer library can't be found, makes sense to me. IIRC, we removed the HSAIL finalizer in ROCm 1.9.0. The 1.8.x OpenCL runtime might have expected to have the HSAIL finalizer around for the legacy HSAIL compilation path.

However, if you're building and running the most up-to-date OpenCL runtime (from master), it should not try to use the HSAIL finalizer. You're also seeing an old OpenCL runtime version based on your `clinfo` output. As such, I'm wondering if you have an old OpenCL installation being loaded, but it can't properly find all the ROCm 1.8.x libraries because you've upgraded ROCm to 1.9.0.

For example, I see that you have `libamdocl64.so` sitting in `/opt/rocm/opencl/lib/`. This may be the ROCm 1.8.x OpenCL library, even though you have a newly-built version of `libamdocl64.so` sitting in your build directory for ROCm-OpenCL-Runtime. The latter may work with your current ROCm installation, while the old file sitting in `/opt/rocm/opencl/lib/` may not. This assumes you've done a partial ROCm 1.8.x->1.9.0 upgrade, though. It's only a guess, because I don't know how you set your systems up. :)

---

### 评论 #9 — sjug (2018-09-17T00:42:17Z)

@jlgreathouse No not at all, you've been excellent thanks for your patience.

I prefer to compile on my own when at all possible rather than using binaries and that seems the be the root of the problems here. I cleaned out the system and rebuilt all the dependencies from scratch again, with the 1.9.x branch for everything other than rocm-opencl which was on master. However, I ended up right back to the same issue again with 1.8.x artifact errors.

So I cleaned up again, tried an exclusively binary install and everything worked perfectly as expected.

I'm a bit confused as to where I'm going wrong as even the basic directory structure of the binary packages vs the `make install` is totally different. Is there something I'm missing?

For example building `rocm-opencl` running:
```
mkdir -p build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/rocm/opencl ..
make
make install
```
Makes a directory tree of:
```
opt/
opt/rocm/
opt/rocm/opencl/
opt/rocm/opencl/bin/
opt/rocm/opencl/bin/clang
opt/rocm/opencl/bin/clang++
opt/rocm/opencl/bin/clang-8
opt/rocm/opencl/bin/clang-cl
opt/rocm/opencl/bin/clang-cpp
opt/rocm/opencl/bin/clang-format
opt/rocm/opencl/bin/clang-import-test
opt/rocm/opencl/bin/clang-offload-bundler
opt/rocm/opencl/bin/clang-refactor
opt/rocm/opencl/bin/clang-rename
opt/rocm/opencl/bin/clinfo
opt/rocm/opencl/bin/git-clang-format
opt/rocm/opencl/bin/hmaptool
opt/rocm/opencl/bin/ld.lld
opt/rocm/opencl/bin/ld64.lld
opt/rocm/opencl/bin/lld
opt/rocm/opencl/bin/lld-link
opt/rocm/opencl/bin/roc-cl
opt/rocm/opencl/bin/wasm-ld
opt/rocm/opencl/include/
opt/rocm/opencl/include/amd_hsa_common.h
opt/rocm/opencl/include/amd_hsa_elf.h
opt/rocm/opencl/include/amd_hsa_kernel_code.h
opt/rocm/opencl/include/amd_hsa_queue.h
opt/rocm/opencl/include/amd_hsa_signal.h
opt/rocm/opencl/include/clang-c/
opt/rocm/opencl/include/clang-c/BuildSystem.h
opt/rocm/opencl/include/clang-c/CXCompilationDatabase.h
opt/rocm/opencl/include/clang-c/CXErrorCode.h
opt/rocm/opencl/include/clang-c/CXString.h
opt/rocm/opencl/include/clang-c/Documentation.h
opt/rocm/opencl/include/clang-c/Index.h
opt/rocm/opencl/include/clang-c/Platform.h
opt/rocm/opencl/include/device_amd_hsa.h
opt/rocm/opencl/include/hsa.h
opt/rocm/opencl/include/llvm/
opt/rocm/opencl/include/llvm-c/
opt/rocm/opencl/include/llvm-c/lto.h
opt/rocm/opencl/include/llvm/Target/
opt/rocm/opencl/include/llvm/Target/AMDGPU/
opt/rocm/opencl/include/llvm/Target/AMDGPU/AMDGPU.h
opt/rocm/opencl/include/llvm/Target/AMDGPU/Disassembler/
opt/rocm/opencl/include/llvm/Target/AMDGPU/Disassembler/CodeObjectDisassembler.h
opt/rocm/opencl/include/ockl.h
opt/rocm/opencl/include/ockl_hsa.h
opt/rocm/opencl/include/ocml.h
opt/rocm/opencl/include/opencl2.2/
opt/rocm/opencl/include/opencl2.2/CL/
opt/rocm/opencl/include/opencl2.2/CL/cl.h
opt/rocm/opencl/include/opencl2.2/CL/cl.hpp
opt/rocm/opencl/include/opencl2.2/CL/cl2.hpp
opt/rocm/opencl/include/opencl2.2/CL/cl_d3d10.h
opt/rocm/opencl/include/opencl2.2/CL/cl_d3d11.h
opt/rocm/opencl/include/opencl2.2/CL/cl_dx9_media_sharing.h
opt/rocm/opencl/include/opencl2.2/CL/cl_ext.h
opt/rocm/opencl/include/opencl2.2/CL/cl_gl.h
opt/rocm/opencl/include/opencl2.2/CL/cl_gl_ext.h
opt/rocm/opencl/include/opencl2.2/CL/cl_platform.h
opt/rocm/opencl/include/opencl2.2/CL/opencl.h
opt/rocm/opencl/lib/
opt/rocm/opencl/lib/clang/
opt/rocm/opencl/lib/clang/8.0.0/
opt/rocm/opencl/lib/clang/8.0.0/include/
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_builtin_vars.h
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_cmath.h
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_complex_builtins.h
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_device_functions.h
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_intrinsics.h
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_libdevice_declares.h
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_math_forward_declares.h
opt/rocm/opencl/lib/clang/8.0.0/include/__clang_cuda_runtime_wrapper.h
opt/rocm/opencl/lib/clang/8.0.0/include/__stddef_max_align_t.h
opt/rocm/opencl/lib/clang/8.0.0/include/__wmmintrin_aes.h
opt/rocm/opencl/lib/clang/8.0.0/include/__wmmintrin_pclmul.h
opt/rocm/opencl/lib/clang/8.0.0/include/adxintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/altivec.h
opt/rocm/opencl/lib/clang/8.0.0/include/ammintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/arm64intr.h
opt/rocm/opencl/lib/clang/8.0.0/include/arm_acle.h
opt/rocm/opencl/lib/clang/8.0.0/include/arm_fp16.h
opt/rocm/opencl/lib/clang/8.0.0/include/arm_neon.h
opt/rocm/opencl/lib/clang/8.0.0/include/armintr.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx2intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512bitalgintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512bwintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512cdintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512dqintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512erintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512fintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512ifmaintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512ifmavlintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512pfintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vbmi2intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vbmiintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vbmivlintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vlbitalgintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vlbwintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vlcdintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vldqintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vlintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vlvbmi2intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vlvnniintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vnniintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vpopcntdqintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avx512vpopcntdqvlintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/avxintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/bmi2intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/bmiintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/cetintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/cldemoteintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/clflushoptintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/clwbintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/clzerointrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/cpuid.h
opt/rocm/opencl/lib/clang/8.0.0/include/cuda_wrappers/
opt/rocm/opencl/lib/clang/8.0.0/include/cuda_wrappers/algorithm
opt/rocm/opencl/lib/clang/8.0.0/include/cuda_wrappers/complex
opt/rocm/opencl/lib/clang/8.0.0/include/cuda_wrappers/new
opt/rocm/opencl/lib/clang/8.0.0/include/emmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/f16cintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/float.h
opt/rocm/opencl/lib/clang/8.0.0/include/fma4intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/fmaintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/fxsrintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/gfniintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/htmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/htmxlintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/ia32intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/immintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/inttypes.h
opt/rocm/opencl/lib/clang/8.0.0/include/invpcidintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/iso646.h
opt/rocm/opencl/lib/clang/8.0.0/include/limits.h
opt/rocm/opencl/lib/clang/8.0.0/include/lwpintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/lzcntintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/mm3dnow.h
opt/rocm/opencl/lib/clang/8.0.0/include/mm_malloc.h
opt/rocm/opencl/lib/clang/8.0.0/include/mmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/module.modulemap
opt/rocm/opencl/lib/clang/8.0.0/include/movdirintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/msa.h
opt/rocm/opencl/lib/clang/8.0.0/include/mwaitxintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/nmmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/opencl-c.h
opt/rocm/opencl/lib/clang/8.0.0/include/pconfigintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/pkuintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/pmmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/popcntintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/prfchwintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/ptwriteintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/rdseedintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/rtmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/s390intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/sgxintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/shaintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/smmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/stdalign.h
opt/rocm/opencl/lib/clang/8.0.0/include/stdarg.h
opt/rocm/opencl/lib/clang/8.0.0/include/stdatomic.h
opt/rocm/opencl/lib/clang/8.0.0/include/stdbool.h
opt/rocm/opencl/lib/clang/8.0.0/include/stddef.h
opt/rocm/opencl/lib/clang/8.0.0/include/stdint.h
opt/rocm/opencl/lib/clang/8.0.0/include/stdnoreturn.h
opt/rocm/opencl/lib/clang/8.0.0/include/tbmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/tgmath.h
opt/rocm/opencl/lib/clang/8.0.0/include/tmmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/unwind.h
opt/rocm/opencl/lib/clang/8.0.0/include/vadefs.h
opt/rocm/opencl/lib/clang/8.0.0/include/vaesintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/varargs.h
opt/rocm/opencl/lib/clang/8.0.0/include/vecintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/vpclmulqdqintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/waitpkgintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/wbnoinvdintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/wmmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/x86intrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/xmmintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/xopintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/xsavecintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/xsaveintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/xsaveoptintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/xsavesintrin.h
opt/rocm/opencl/lib/clang/8.0.0/include/xtestintrin.h
opt/rocm/opencl/lib/libLTO.so
opt/rocm/opencl/lib/libLTO.so.8svn
opt/rocm/opencl/lib/libOpenCL.so.1.2
opt/rocm/opencl/lib/libamdocl64.so
opt/rocm/opencl/lib/libclang.so
opt/rocm/opencl/lib/libclang.so.8
opt/rocm/opencl/lib/libclang.so.8svn
opt/rocm/opencl/lib/libopencl_driver.a
opt/rocm/opencl/lib/ockl.amdgcn.bc
opt/rocm/opencl/lib/oclc_correctly_rounded_sqrt_off.amdgcn.bc
opt/rocm/opencl/lib/oclc_correctly_rounded_sqrt_on.amdgcn.bc
opt/rocm/opencl/lib/oclc_daz_opt_off.amdgcn.bc
opt/rocm/opencl/lib/oclc_daz_opt_on.amdgcn.bc
opt/rocm/opencl/lib/oclc_finite_only_off.amdgcn.bc
opt/rocm/opencl/lib/oclc_finite_only_on.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_700.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_701.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_702.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_801.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_802.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_803.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_810.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_900.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_902.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_904.amdgcn.bc
opt/rocm/opencl/lib/oclc_isa_version_906.amdgcn.bc
opt/rocm/opencl/lib/oclc_unsafe_math_off.amdgcn.bc
opt/rocm/opencl/lib/oclc_unsafe_math_on.amdgcn.bc
opt/rocm/opencl/lib/ocml.amdgcn.bc
opt/rocm/opencl/lib/opencl.amdgcn.bc
opt/rocm/opencl/share/
opt/rocm/opencl/share/clang/
opt/rocm/opencl/share/clang/clang-format-bbedit.applescript
opt/rocm/opencl/share/clang/clang-format-diff.py
opt/rocm/opencl/share/clang/clang-format-sublime.py
opt/rocm/opencl/share/clang/clang-format.el
opt/rocm/opencl/share/clang/clang-format.py
opt/rocm/opencl/share/clang/clang-rename.el
opt/rocm/opencl/share/clang/clang-rename.py
opt/rocm/opencl/share/opt-viewer/
opt/rocm/opencl/share/opt-viewer/opt-diff.py
opt/rocm/opencl/share/opt-viewer/opt-stats.py
opt/rocm/opencl/share/opt-viewer/opt-viewer.py
opt/rocm/opencl/share/opt-viewer/optpmap.py
opt/rocm/opencl/share/opt-viewer/optrecord.py
opt/rocm/opencl/share/opt-viewer/style.css
```

Where together the binary packages rocm-opencl & rocm-opencl-dev create:
```
opt/
opt/rocm/
opt/rocm/opencl/
opt/rocm/opencl/bin/
opt/rocm/opencl/bin/x86_64/
opt/rocm/opencl/bin/x86_64/clang
opt/rocm/opencl/bin/x86_64/clinfo
opt/rocm/opencl/bin/x86_64/ld.lld
opt/rocm/opencl/bin/x86_64/llc
opt/rocm/opencl/bin/x86_64/llvm-link
opt/rocm/opencl/bin/x86_64/llvm-objdump
opt/rocm/opencl/bin/x86_64/opt
opt/rocm/opencl/include/
opt/rocm/opencl/include/CL/
opt/rocm/opencl/include/CL/cl.h
opt/rocm/opencl/include/CL/cl.hpp
opt/rocm/opencl/include/CL/cl_ext.h
opt/rocm/opencl/include/CL/cl_gl.h
opt/rocm/opencl/include/CL/cl_gl_ext.h
opt/rocm/opencl/include/CL/cl_platform.h
opt/rocm/opencl/include/CL/opencl.h
opt/rocm/opencl/include/opencl-c.h
opt/rocm/opencl/lib/
opt/rocm/opencl/lib/x86_64/
opt/rocm/opencl/lib/x86_64/bitcode/
opt/rocm/opencl/lib/x86_64/bitcode/irif.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/ockl.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_correctly_rounded_sqrt_off.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_correctly_rounded_sqrt_on.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_daz_opt_off.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_daz_opt_on.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_finite_only_off.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_finite_only_on.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_700.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_701.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_702.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_801.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_802.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_803.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_810.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_900.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_902.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_904.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_isa_version_906.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_unsafe_math_off.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/oclc_unsafe_math_on.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/ocml.amdgcn.bc
opt/rocm/opencl/lib/x86_64/bitcode/opencl.amdgcn.bc
opt/rocm/opencl/lib/x86_64/libOpenCL.so
opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
opt/rocm/opencl/lib/x86_64/libamdocl64.so
opt/rocm/opencl/lib/x86_64/libcltrace.so
```

Should I be building it some other way to get something similar to the binary?

---

### 评论 #10 — jlgreathouse (2018-09-18T02:12:43Z)

Hi @sjug 

I can confirm the problem. It appears that our team did not get the ROCm 1.9 release of the OpenCL runtime or driver pushed out to GitHub after building and packaging it for release. We are working with the teams inside AMD to get this release -- it will hopefully fix the main issue you're running into, where your OpenCL version is not the same between the binary release and the from-source build.

Second: you're right that, even when building from source, you don't end up with exactly the same files that you see from a source build. I'll admit that we do a bit of data-movement internally when packaging to clean up what files are shipped and where they're placed. Once we get the ROCm 1.9 release out, I'll try to put up a quick shell script that will "clean up" the install properly. :)

---

### 评论 #11 — jlgreathouse (2018-09-20T19:54:05Z)

Hi @sjug 

The source for the ROCm 1.9 release of the OpenCL runtime has been released. It is now available on the roc-1.9.x branch at https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime

The build still puts things into non-standard locations, but it builds all the required files. The following script should build and install the OpenCL runtime from source and get it installed properly on your system. It also adds debug symbols. :)

Note that if you want to build a different version, you would need to change the "-b" argument on the repo init line. If you want to install in a non-standard location, you would want to change basically all of the "/opt/rocm/opencl/" instances (sorry, this isn't a robust, production-ready script that takes this as an argument or anything like that).

This script is also Ubuntu-specific, since it does some `apt-get` stuff at the top. However, it should guide you in the right direction for which files to move where on your own repo.

I believe we have a fixed CMakeList.txt internally, but it might not have made it into the release branch by the time we locked down ROCm 1.9. Hopefully this script will only be needed until the next ROCm release. 

```bash
#!/bin/bash
###############################################################################
# Copyright (c) 2018 Advanced Micro Devices, Inc. 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################

# Download and build the AMD OpenCL Runtime and Driver
sudo apt-get install ocaml ocaml-findlib python-z3 git-svn
mkdir -p ~/bin/
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
mkdir -p ~/opencl/
cd ~/opencl/
~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git -b roc-1.9.x -m opencl.xml
~/bin/repo sync
cd opencl
mkdir -p build && cd build
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_INSTALL_PREFIX=/opt/rocm/opencl/ ..
make -j `nproc`
sudo make install
sudo mkdir -p /etc/OpenCL/vendors/
sudo cp ~/opencl/opencl/api/opencl/config/amdocl64.icd /etc/OpenCL/vendors/
echo 'export LD_LIBRARY_PATH=/opt/rocm/opencl/lib/x86_64:/opt/rocm/hsa/lib:$LD_LIBRARY_PATH' | sudo tee -a /etc/profile.d/rocm.sh
echo 'export PATH=$PATH:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin/x86_64' | sudo tee -a /etc/profile.d/rocm.sh
echo '/opt/rocm/opencl/lib/x86_64' | sudo tee -a /etc/ld.so.conf.d/x86_64-rocm-opencl.conf
sudo ldconfig

# Fix up OpenCL installation locations

# Should have this in /opt/rocm/opencl/lib/x86_64/:
# bitcode  libamdocl64.so  libcltrace.so  libOpenCL.so  libOpenCL.so.1
sudo mkdir -p /opt/rocm/opencl/lib/x86_64/bitcode/
sudo mv /opt/rocm/opencl/lib/*.bc /opt/rocm/opencl/lib/x86_64/bitcode/
sudo mv /opt/rocm/opencl/lib/libOpenCL.so.1.2 /opt/rocm/opencl/lib/x86_64/
sudo ln -s /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1.2 /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
sudo ln -s /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1 /opt/rocm/opencl/lib/x86_64/libOpenCL.so
sudo mv /opt/rocm/opencl/lib/libamdocl64.so /opt/rocm/opencl/lib/x86_64/
sudo rm -f /opt/rocm/opencl/lib/lib*
sudo rm -rf /opt/rocm/opencl/lib/clang/

# $ ls /opt/rocm/opencl/bin/x86_64/
# clang  clinfo  ld.lld  llc  llvm-link  llvm-objdump  opt
sudo mkdir -p /opt/rocm/opencl/bin/x86_64/
# missing llc, llvm-link, llvm-objdump opt, but these are not
# needed for libOpenCL.so operation
for i in clang clang-[0-9] clinfo ld.lld lld; do sudo mv /opt/rocm/opencl/bin/$i /opt/rocm/opencl/bin/x86_64/; done
sudo rm -f /opt/rocm/opencl/bin/clang*
sudo rm -f /opt/rocm/opencl/bin/git-clang-format
sudo rm -f /opt/rocm/opencl/bin/ld64.lld
sudo rm -f /opt/rocm/opencl/bin/lld-link
sudo rm -f /opt/rocm/opencl/bin/roc-cl
sudo rm -f /opt/rocm/opencl/bin/wasm-ld

# $ ls /opt/rocm/opencl/include/
# CL  opencl-c.h
#$ ls /opt/rocm/opencl/include/CL/
#cl_ext.h  cl_gl_ext.h  cl_gl.h  cl.h  cl.hpp  cl_platform.h  opencl.h
sudo mv /opt/rocm/opencl/include/opencl2.2/ /tmp/
sudo rm -rf /opt/rocm/opencl/include/*
sudo mkdir -p /opt/rocm/opencl/include/CL/
sudo mv /tmp/opencl2.2/CL/ /opt/rocm/opencl/include/
sudo rm /opt/rocm/opencl/include/CL/cl_d3d*
sudo rm /opt/rocm/opencl/include/CL/cl_dx9*
sudo rm /opt/rocm/opencl/include/CL/cl2.hpp
```

---

### 评论 #12 — sjug (2018-09-20T20:12:03Z)

Hey @jlgreathouse,

Thanks very much, I saw `roc-1.9.x` appear and kicked off a build earlier but I haven't had time to follow up on the failures. It seems that there is a new dependency on the Perl subversion libraries now as well, as that build failed with: 
```
Can't locate SVN/Core.pm in @INC (you may need to install the SVN::Core module)
```
Once the equivalent of the `libsvn-perl` ubuntu package was installed the issue was resolved.

I also appreciate the build script, this will help me ensure my packaging is similar.

A few questions:
- Why is the preferred make target `RelWithDebInfo`?
- Why do you add manual library and header loading overrides to point to `/opt/rocm/*` instead of adding them directly to `/usr/{lib,include}` or subdirectories within the standard structure?



---

### 评论 #13 — jlgreathouse (2018-09-20T20:22:12Z)

What distro are you seeing the libsvn-perl issue on? At least on Ubuntu, git-svn (which is a requirement for the ROCm OpenCL runtime) depends on libsvn-perl, and so should be installed if you `apt install git-svn`. git-svn installation is listed in the README at least back to roc-1.6.x.

*My* preferred make is RelWithDebInfo because I usually rebuild our open source libraries to include debug symbols. Because I'm debugging problems for people on GitHub and I like being able to use GDB. You can change that to "Release" if you don't care about that -- our .deb and .rpm files build with "Release".

My script is trying to put things in the same location as the .deb and .rpm files. The ROCm team is currently keeping all (or most) of its software in the /opt/rocm/ directory on user systems, as this seems to be a bit more portable across distros and means we don't have conflicts with other libraries. In any case, my script above is just trying to match what our package distributions do.

---

### 评论 #14 — sjug (2018-09-20T20:31:45Z)

I do most of my development on Arch Linux with testing on whatever distro necessary, usually Fedora/RHEL. It's odd that dependency was there before as I built ROCm master prior to the 1.9 bits being merged without the perl svn libs. Thanks for the clarification once again.

Any chance you could take a look at https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/44 as well?

I'll work through building ROCm and all deps from scratch again and then close this issue.

---

### 评论 #15 — jlgreathouse (2018-09-20T20:43:53Z)

Ah, sorry to say that I'm not at all familiar with the package dependencies on Arch. Hopefully things move smoothly from here on out. :)

---

### 评论 #16 — sjug (2018-10-21T19:49:50Z)

Able to build and package from source for ROCm 1.9 and dependencies. 

---

### 评论 #17 — jlgreathouse (2018-10-24T04:50:16Z)

Any thoughts on sharing the build scripts (or list of directions) you're using? I'm interested in putting together a repo of scripts for various not-officially-supported distros to help users build ROCm from source. As per a few other issues requesting this. :)

---

### 评论 #18 — sjug (2018-10-26T01:33:29Z)

Sure, in Arch there's already the Arch User Repository ([AUR](https://aur.archlinux.org/)) which I used as as a starting point. I can update them there and share them wherever you'd like.

---

### 评论 #19 — clapbr (2018-12-03T21:22:51Z)

> Sure, in Arch there's already the Arch User Repository ([AUR](https://aur.archlinux.org/)) which I used as as a starting point. I can update them there and share them wherever you'd like.

Can you share that please?


edit: I'm updating a few rocm packages to 1.9.x in AUR.  I still need to figure the above mentioned dir structure problems. I got it working locally but I'm not sure it's 100% correct


https://aur.archlinux.org/packages/hsa-rocr/ - ready
https://aur.archlinux.org/packages/hsa-ext-rocr/ - ready
https://aur.archlinux.org/packages/rocm-opencl-git - next to do

---

### 评论 #20 — maxcr (2018-12-04T20:36:32Z)

Whenever I use your PKGBUILD I get 

```
hsa api call failure at line 952, file: /home/maxr/src/rocm/rocminfo/rocminfo.cc. Call returned 4104
```

But whenever I use my PKGBUILD it works fine.

Are you just decompressing the debian packages and installing those instead of building from source? I've had this working for a few weeks now. Should I just submit my packages to AUR anyway. I've got a couple projects for my client waiting on this and I want to know whether I should move forward cleaning up the directory structure on these or who the onus is on.

---

### 评论 #21 — maxcr (2018-12-04T20:37:38Z)

Maybe add me as a maintainer. Here's my pkgbuilds.

```
# Maintainer: Max <max.conrad.robbins@gmail.com>

pkgbase=rocm-thunk
pkgname=('rocm-thunk')
_gitname='ROCT-Thunk-Interface'
pkgver=roc.r0.g238782c
pkgrel=1
arch=('i686' 'x86_64')
url="https://gpuopen.com/"
license=('GPL2')
makedepends=('gcc' 'cmake' 'git')
source=("$_gitname::git+https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface.git#branch=roc-1.9.x")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$_gitname"
  git describe --long --tags | sed 's/\([^-]*-\)/r/2;s/-/./g'
}

prepare() {
  cd "$srcdir/$_gitname"
  [[ -d build ]] && rm -rf build
  mkdir build
}

build() {
  cd "$srcdir/$_gitname/build/"
  cmake \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm/ \
    ..
  make
}

package () {
  cd "$srcdir/$_gitname/build/"
  make DESTDIR="$pkgdir" install
  cd "$srcdir/$_gitname/"
  cp -r "./include" "$pkgdir/opt/rocm/lib64"
}

```

```
# Maintainer: Max <max.conrad.robbins@gmail.com>

pkgbase=rocm-rocr
pkgname=('rocm-rocr')
_gitname='ROCR-Runtime'
pkgver=roc.r1.gbc92d3a
pkgrel=1
arch=('i686' 'x86_64')
url="https://gpuopen.com/"
license=('GPL2')
makedepends=('gcc' 'cmake' 'git' 'rocm-thunk')
source=("$_gitname::git+https://github.com/RadeonOpenCompute/ROCR-Runtime.git#branch=roc-1.9.x")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$_gitname"
  git describe --long --tags | sed 's/\([^-]*-\)/r/2;s/-/./g'
}

prepare() {
  cd "$srcdir/$_gitname/src/"
  [[ -d build ]] && rm -rf build
  mkdir build
}

build() {
  cd "$srcdir/$_gitname/src/build/"
  cmake \
    -D CMAKE_PREFIX_PATH=/opt/rocm/ \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm/lib64/ \
    ..
  make
}

package () {
  cd "$srcdir/$_gitname/src/build/"
  make DESTDIR="$pkgdir" install
}

```

---

### 评论 #22 — maxcr (2018-12-04T21:18:33Z)

This is the working directory structure. My PKGBUILD's do not reflect this but I'm currently fixing it. If by any chance you fix yours before mine make it reflect this. Obviously permissions should be `root:root` this was a tarball backup of working known good configuration before I started testing my PKGBUILD's.

```
drwxr-xr-- 9 maxr users 4.0K Nov 19 00:09 .
drwxr-xr-x 4 maxr users 4.0K Dec  4 13:40 ..
drwxr-xr-- 2 maxr users 4.0K Nov 19 00:15 bin
drwxr-xr-- 4 maxr users 4.0K Nov 18 20:56 hsa
drwxr-xr-- 3 maxr users 4.0K Nov 18 23:17 include
drwxr-xr-- 2 maxr users 4.0K Nov 25 08:13 lib
lrwxrwxrwx 1 maxr users   13 Nov 18 23:45 lib64 -> /opt/rocm/lib
drwxr-xr-- 2 maxr users 4.0K Nov 19 00:32 libhsakmt
drwxr-xr-- 4 maxr users 4.0K Nov 18 21:07 rocm_smi
drwxr-xr-- 3 maxr users 4.0K Nov 18 22:40 share
```

```
./bin
├── rocm_agent_enumerator
└── rocminfo
./hsa
├── include
│   └── hsa
│       ├── amd_hsa_common.h
│       ├── amd_hsa_elf.h
│       ├── amd_hsa_kernel_code.h
│       ├── amd_hsa_queue.h
│       ├── amd_hsa_signal.h
│       ├── Brig.h
│       ├── hsa_api_trace.h
│       ├── hsa_ext_amd.h
│       ├── hsa_ext_finalize.h
│       ├── hsa_ext_image.h
│       ├── hsa.h
│       ├── hsa_ven_amd_aqlprofile.h
│       └── hsa_ven_amd_loader.h
└── lib
    ├── libhsa-runtime64.so -> libhsa-runtime64.so.1
    ├── libhsa-runtime64.so.1 -> libhsa-runtime64.so.1.9.1
    ├── libhsa-runtime64.so.1.9.0
    └── libhsa-runtime64.so.1.9.1
./include
├── hsa -> ../hsa/include/hsa
├── hsakmt.h
├── hsakmttypes.h
└── linux
    └── kfd_ioctl.h
./lib
├── lib64 -> /opt/rocm/lib64
├── libhsakmt.so -> libhsakmt.so.1
├── libhsakmt.so.1 -> libhsakmt.so.1.0.6
├── libhsakmt.so.1.0.6
└── libhsa-runtime64.so -> ../hsa/lib/libhsa-runtime64.so
./lib64 [error opening dir]
./libhsakmt
└── LICENSE.md
./rocm_smi
├── include
│   └── rocm_smi
│       └── rocm_smi.h
└── lib
    ├── librocm_smi64.so -> librocm_smi64.so.1
    ├── librocm_smi64.so.1 -> librocm_smi64.so.1.0.0
    └── librocm_smi64.so.1.0.0
./share
└── rocm
    └── cmake
        ├── ROCMAnalyzers.cmake
        ├── ROCMClangTidy.cmake
        ├── ROCMConfig.cmake
        ├── ROCMCppCheck.cmake
        ├── ROCMCreatePackage.cmake
        ├── ROCMInstallSymlinks.cmake
        ├── ROCMInstallTargets.cmake
        ├── ROCMPackageConfigHelpers.cmake
        └── ROCMSetupVersion.cmake

11 directories, 40 files

```


This is what all of the subsequent packages expect. Especially `rocminfo` and the `smi controller`. The only concerning thing is the circular symlink between `lib` and `lib64`. Don't know why the packages create those. Perhaps delete one of those manually in the `pkgbuild`.



---

### 评论 #23 — clapbr (2018-12-04T21:36:58Z)

I'm still waiting the old maintainer "leidola" to give me access to the other packages. I'll add you as a maintainer on the pkgs I already own, I need your AUR username. The https://aur.archlinux.org/packages/hsakmt-roct also needs update. I'm in doubt if we should use 1.9.x or master for everything. 

---

### 评论 #24 — maxcr (2018-12-04T21:49:20Z)

1.9.x I had some weird errors on master, but once I switched to 1.9.x everything went away and worked fine. Just make sure you have amdkfd in mkinicpio . And we should be golden. My AUR username is `WeenieHut`. I really appreciate the quick reply!

`MODULES=(amdgpu amdkfd)`

---

### 评论 #25 — maxcr (2018-12-04T21:58:49Z)

For some reason I needed to use GCC7 for rocm-rocr to build successfully in my initial tests, but seems to be building fine on GCC8 now... Were there updates to the 1.9.x branch @jlgreathouse ? Or do I need to document my changes better?

---

### 评论 #26 — clapbr (2018-12-04T22:01:03Z)

@maxcr 

added WeenieHut to:
https://aur.archlinux.org/packages/hsa-rocr/
https://aur.archlinux.org/packages/hsa-ext-rocr/
https://aur.archlinux.org/packages/rocm-utils/

other packages needing update pending old owner transfer:
https://aur.archlinux.org/packages/hsakmt-roct
https://aur.archlinux.org/packages/rocm-opencl-git/
 
not sure if needs updating:
https://aur.archlinux.org/packages/hipsycl-rocm-git/
https://aur.archlinux.org/packages/rocm-smi/



---

### 评论 #27 — maxcr (2018-12-04T22:05:43Z)

@clapbr <3 I'm going to dig up all of my build notes and post them here so you can replicate my dir structure for PKGBUILDs without error.

---

### 评论 #28 — maxcr (2018-12-04T22:09:32Z)

*Using GCC7*

My initial tests which made it work fine. Using GCC8 yeilded the segfaulting errors that people are currently complaining about.

```
git clone git@github.com:RadeonOpenCompute/ROCT-Thunk-Interface.git
git checkout remotes/origin/roc-1.9.x
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/ ..
make
sudo make install
git clone git@github.com:RadeonOpenCompute/ROCR-Runtime.git
git checkout remotes/origin/roc-1.9.x
mkdir build
cmake -D CMAKE_PREFIX_PATH=/opt/rocm/ -DCMAKE_INSTALL_PREFIX=/opt/rocm/ ..
make
sudo make install
git clone git@github.com:RadeonOpenCompute/rocminfo.git
mkdir build
cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/ ..
make
sudo make install

```

---

### 评论 #29 — clapbr (2018-12-04T22:12:31Z)

> For some reason I needed to use GCC7 for rocm-rocr to build successfully in my initial tests, but seems to be building fine on GCC8 now... Were there updates to the 1.9.x branch @jlgreathouse ? Or do I need to document my changes better?

I also had the same prob with gcc8 but it's gone on my setup. 

Considering we need to update multiple AUR packages depending on each other plus directory fixes, wouldn't be better to maintain everything rocm related in a new full package conflicting with all the old splits, then abandon the old ones?

> @clapbr <3 I'm going to dig up all of my build notes and post them here so you can replicate my dir structure for PKGBUILDs without error.

Oka.

We should move this discussion to a new place, maybe a staging git for the future packages. 

---

### 评论 #30 — clapbr (2018-12-05T00:03:50Z)

Additional things to keep in mind:

- opencl-amd from AUR uses the same .icd filename as rocm for the loader. Old packages solved this renaming rocm's icd to a different name.
- Should we add the paths for the user to profile.d?
- clinfo package (not sure about Arch, I'm in Manjaro) will have precedence over rocm's unless we conflict with it.

edit:

On your rocm-rocr PKGBUILD we need to do ldconfig or rocm-opencl build will fail not finding rocr.
something like
```
mkdir -p "$pkgdir/etc/ld.so.conf.d"
echo "/opt/rocm/?" > "$pkgdir/etc/ld.so.conf.d/hsa.conf"
```

---

### 评论 #31 — maxcr (2018-12-05T00:34:17Z)

> 
> 
> Additional things to keep in mind:
> 
>     * opencl-amd from AUR uses the same .icd filename as rocm for the loader. Old packages solved this renaming rocm's icd to a different name.
> 
>     * Should we add the paths for the user to profile.d?
> 
>     * clinfo package (not sure about Arch, I'm in Manjaro) will have precedence over rocm's unless we conflict with it.
> 
> 
> edit:
> 
> On your rocm-rocr PKGBUILD we need to do ldconfig or rocm-opencl build will fail not finding rocr.
> something like
> 
> ```
> mkdir -p "$pkgdir/etc/ld.so.conf.d"
> echo "/opt/rocm/?" > "$pkgdir/etc/ld.so.conf.d/hsa.conf"
> ```

Yeah I had a hacky solution by adding an ld path to my `.zshrc` or `.bashrc` but that seems much more optimal.

---

### 评论 #32 — clapbr (2018-12-05T00:55:12Z)

@maxcr 

https://github.com/clapbr/arch-rocm - let's do the package development there for cleaness here. Sent you an invite. continuing discussion at https://github.com/clapbr/arch-rocm/issues/1

---
