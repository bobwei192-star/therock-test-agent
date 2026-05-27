# ROCm driver attempts to write temporary file into readonly directory and stops working

> **Issue #822**
> **状态**: closed
> **创建时间**: 2019-06-16T17:46:42Z
> **更新时间**: 2024-01-14T04:42:38Z
> **关闭时间**: 2024-01-14T04:42:38Z
> **作者**: o-alquimista
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/822

## 描述

The problem:
Hashcat is unable to use the OpenCL device unless it is run as root.

See issue filed for Hashcat: https://github.com/hashcat/hashcat/issues/2062

A Hashcat developer analyzed the problem and came up with a workaround that enables me to run their application without root privileges:
`export TMPDIR=$HOME/`

The conclusion from their end is that the problem is not with Hashcat. See their [comment](https://github.com/hashcat/hashcat/issues/2062#issuecomment-502664272).

The part of the strace command they pointed at:
```
12147 openat(AT_FDCWD, "/usr/local/share/hashcat/OpenCL/t_12147_16-f6e20b.o", O_RDWR|O_CREAT|O_EXCL|O_CLOEXEC, 0600) = -1 EACCES (Permissão negada)
```

I've attached the output of two strace commands used by Hashcat to study the problem.

[strace-clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/3297591/strace-clinfo.txt)
[strace-hashcat.txt](https://github.com/RadeonOpenCompute/ROCm/files/3297592/strace-hashcat.txt)

ROCm runtime version: **2.4.0-1** (from [AUR](https://aur.archlinux.org/packages/rocm-opencl-runtime/))
OS: Arch Linux
Kernel version: 5.1.9-arch1-1-ARCH
Device: AMD RX 560 4GB

**Running with an unprivileged, default user:**
```
$ hashcat -a 3 -m 0 -O 8743b52063cd84097a65d1633f5c74f5
hashcat (v5.1.0-1151-g5e0eb288) starting...

clGetPlatformIDs(): CL_PLATFORM_NOT_FOUND_KHR

ATTENTION! No OpenCL-compatible or CUDA-compatible platform found.

You are probably missing the OpenCL or CUDA runtime installation.

* AMD GPUs on Linux require this driver:
  "RadeonOpenCompute (ROCm)" Software Platform (1.6.180 or later)
* Intel CPUs require this runtime:
  "OpenCL Runtime for Intel Core and Intel Xeon Processors" (16.1.1 or later)
* Intel GPUs on Linux require this driver:
  "OpenCL 2.0 GPU Driver Package for Linux" (2.0 or later)
* NVIDIA GPUs require this runtime and/or driver (both):
  "NVIDIA Driver" (418.56 or later)
  "CUDA Toolkit" (10.1 or later)

Started: Sun Jun 16 14:31:15 2019
Stopped: Sun Jun 16 14:31:15 2019
```

**Running as root: device found**
```
$ sudo hashcat -a 3 -m 0 -O 8743b52063cd84097a65d1633f5c74f5
hashcat (v5.1.0-1151-g5e0eb288) starting...

OpenCL API (OpenCL 2.0 AMD-APP.internal (2874.0)) - Platform #1 [Advanced Micro Devices, Inc.]
==============================================================================================
* Device #1: gfx803, 3481/4096 MB allocatable, 14MCU

(...) Job starts and completes successfully.
```

**`clinfo` output:**
```
$ clinfo
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.0 AMD-APP.internal (2874.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_object_metadata cl_amd_event_callback 
  Platform Max metadata object keys (AMD)         8
  Platform Extensions function suffix             AMD

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx803
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 
  Driver Version                                  2874.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X]
  Device Topology (AMD)                           PCI-E, 01:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               14
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1176MHz
  Graphics IP (AMD)                               8.3
  Device Partition                                (core)
    Max number of sub-devices                     14
    Supported partition types                     None
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
    Denormals                                     No
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
  Global memory size                              4294967296 (4GiB)
  Global free memory (AMD)                        4192256 (3.998GiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           3650722201 (3.4GiB)
  Unified memory for Host and Device              No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   No
    Base address alignment for 2D image buffers   0 bytes
    Pitch alignment for 2D image buffers          0 pixels
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory syze per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        3650722201 (3.4GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties                                
    Out-of-order execution                        No
    Profiling                                     Yes
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  P2P devices (AMD)                               (n/a)
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 21:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             14
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  No platform
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   No platform
  clCreateContext(NULL, ...) [default]            No platform
  clCreateContext(NULL, ...) [other]              Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx803
```

---

## 评论 (5 条)

### 评论 #1 — kentrussell (2019-06-19T13:42:27Z)

Looks related to https://github.com/RadeonOpenCompute/ROCm/issues/823

---

### 评论 #2 — ulyssesrr (2019-06-26T04:41:18Z)

> Looks related to #823

Don't think so. I can execute LuxMark but not hashcat as a regular user. The issue here is that ROCm OpenCL Runtime, under some circunstances, attempts to write the compiled kernel to a directory where the regular user has no write permissions.

For instance, hashcat has a bunch of kernels stored on /usr/share/hashcat/OpenCL/, a regular user can read, but not write, into that directory.

More specifically:

> opencl/compiler/driver/src/driver/AmdCompiler.cpp

```cpp
std::string NewTempName(const char* dir, const char* prefix, const char* ext, bool pid = true) const {
    static std::atomic_size_t counter(1);
    if (!dir) { dir = tempDir; }
    std::ostringstream name;
    name << dir << "/" << prefix << getpid() << "_" << counter++;
    if (ext) { name << "." << ext; }
    return name.str();
  }
```

`dir` would fallback to `tempDir`, which is /tmp, if null

But hashcat strace shows ROCm attempting to create the file in /usr/share/hashcat/OpenCL/, meaning that `dir` was set to the kernel source  folder(?) (probably from `NewTempFile()`):
```shell
openat(AT_FDCWD, "/usr/share/hashcat/OpenCL/t_16160_16-d916da.o", O_RDWR|O_CREAT|O_EXCL|O_CLOEXEC, 0600) = -1 EACCES (Permission denied)
```


Maybe it should always favor the `tempDir`.



---

### 评论 #3 — brabes (2019-08-08T12:59:11Z)

Nope, it has nothing to do with `NewTempName`. The issue actually _is_ with hashcat.

A debug build of version 2.6.0 run through `strace -k` reveals the source of the failing `open` call:
```
openat(AT_FDCWD, "/usr/share/hashcat/OpenCL/t_7041_16-9589b5.o", O_RDWR|O_CREAT|O_EXCL|O_CLOEXEC, 0600) = -1 EACCES (Permission denied)
 > /usr/lib/libpthread-2.29.so(__open64+0xda) [0x1326a]
 > /opt/rocm/opencl/lib/x86_64/libamdocl64.so(llvm::sys::fs::openFile(llvm::Twine const&, int&, llvm::sys::fs::CreationDisposition, llvm::sys::fs::FileAccess, llvm::sys::fs::OpenFlags, unsigned int)+0xdd) [0x363af4d]
 > /opt/rocm/opencl/lib/x86_64/libamdocl64.so(createUniqueEntity(llvm::Twine const&, int&, llvm::SmallVectorImpl<char>&, bool, unsigned int, FSEntity, llvm::sys::fs::OpenFlags)+0x14d) [0x363cccd]
 > /opt/rocm/opencl/lib/x86_64/libamdocl64.so(llvm::sys::fs::createTemporaryFile(llvm::Twine const&, llvm::StringRef, int&, llvm::SmallVectorImpl<char>&, FSEntity)+0x110) [0x363cf90]
 > /opt/rocm/opencl/lib/x86_64/libamdocl64.so(llvm::sys::fs::createTemporaryFile(llvm::Twine const&, llvm::StringRef, llvm::SmallVectorImpl<char>&)+0x23) [0x363d1b3]
 > /opt/rocm/opencl/lib/x86_64/libamdocl64.so(clang::driver::Driver::GetTemporaryPath[abi:cxx11](llvm::StringRef, llvm::StringRef) const+0x77) [0xaa6e17]
 > /opt/rocm/opencl/lib/x86_64/libamdocl64.so(clang::driver::Driver::GetNamedOutputPath(clang::driver::Compilation&, clang::driver::JobAction const&, char const*, llvm::StringRef, bool, bool, llvm::StringRef) const+0x8f9) [0xab7d09]
 > /opt/rocm/opencl/lib/x86_64/libamdocl64.so(clang::driver::Driver::BuildJobsForActionNoCache(clang::driver::Compilation&, clang::driver::Action const*, clang::driver::ToolChain const*, llvm::StringRef, bool, bool, char const*, std::map<std::pair<clang::driver::Action const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, clang::driver::InputInfo, std::less<std::pair<clang::driver::Action const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >, std::allocator<std::pair<std::pair<clang::driver::Action const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const, clang::driver::InputInfo> > >&, clang::driver::Action::OffloadKind) const+0x109d) [0xaba75d]
...
```

If you follow `llvm::sys::fs::createTemporaryFile` it ends up calling the following function in `llvm-roc-ocl-2.6.0/lib/support/Unix/Path.inc` line 1088

```c++
static const char *getEnvTempDir() {
  // Check whether the temporary directory is specified by an environment
  // variable.
  const char *EnvironmentVariables[] = {"TMPDIR", "TMP", "TEMP", "TEMPDIR"};
  for (const char *Env : EnvironmentVariables) {
    if (const char *Dir = std::getenv(Env))
      return Dir;
  }

  return nullptr;
}
```

It turns out `TMP` was being set to the hashcat shared folder by hashcat itself. This comes from the following (abridged) code which is part of `folder_config_init` in hashcat's `src/folder.c` line 397. That is why setting `TMPDIR`, which is checked first, bypasses this problem.

```c
  /**
   * There are a lot of problems related to bad support of -I parameters when building the kernel.
   * Each OpenCL runtime handles it slightly differently.
   * The most problematic is with new AMD drivers on Windows, which cannot handle quote characters!
   * The best workaround found so far is to modify the TMP variable (only inside hashcat process) before the runtime is loaded.
   */

  char *cpath;

  #if defined (_WIN)

  hc_asprintf (&cpath, "%s\\OpenCL\\", shared_dir);

  char *cpath_real;

  hc_asprintf (&cpath_real, "%s\\OpenCL\\", shared_dir);

  #else

  hc_asprintf (&cpath, "%s/OpenCL/", shared_dir);

  char *cpath_real = (char *) hcmalloc (PATH_MAX);

/** SNIP **/

  //if (getenv ("TMP") == NULL)
  if (1)
  {
    char *tmp;

    hc_asprintf (&tmp, "TMP=%s", cpath_real);

    putenv (tmp);
  }

/** SNIP **/
```



---

### 评论 #4 — nartmada (2024-01-14T04:05:49Z)

Hi @o-alquimista, is this still an issue?  Please close the ticket is the issue is gone.  Thanks.

---

### 评论 #5 — o-alquimista (2024-01-14T04:42:38Z)

@nartmada Hi. Sorry, I haven't been using ROCm lately. I'll reopen the issue if I ever hit this problem again. Thanks.

---
