# [Issue]: Porting nvdiffrast to AMD Radeon W7900 (gfx1100) - Compilation and Linking Issues

- **Issue #:** 3471
- **State:** closed
- **Created:** 2024-07-29T09:45:49Z
- **Updated:** 2024-08-15T13:32:27Z
- **Labels:** Under Investigation, AMD Radeon Pro W7900, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3471

### Problem Description

I am in the process of porting nvdiffrast to support the AMD Radeon W7900 (gfx1100).
Here are the translations of your questions into English:
 Can you answer the following questions:
1.
- What are the equivalents of CUDA functions in HIP? Are there any alternative versions? What are the names of the header files and the linking libraries? (The official documentation section 6.1.3 states support, but compilation does not recognize them)
- `__all_sync`
- `__ballot_sync`
- `__syncwarp`
- `__any_sync`

The grep command output:
```
./lib/llvm/lib/clang/17/include/__clang_cuda_intrinsics.h:inline __device__ int __all_sync(unsigned int mask, int pred) {
./include/hipify/include/__clang_cuda_intrinsics.h:inline __device__ int __all_sync(unsigned int mask, int pred)
```
The header file indicates that it is only CUDA compatibility code, what does that mean?

2. ROCM supports inline assembly, but I don't know how to find the corresponding strings? The following are just compilation checks that do not support it, and I don't know if the CUDA instructions can be directly migrated to AMD cards without changes?
Inline assembly string for ROCM
Inline ASM statements
Util.inl:23:105: error: invalid % escape in inline assembly string
23 | __device__ __inline__ U32 getLaneMaskLt(void) { U32 r; asm("mov.u32 %0, %lanemask_lt;" : "=r"(r)); return r; }
| ~~~~~~~~~~~~~~~^~~~~~~~~~~~
... (similar errors for other lines)

3. Is there a linking error with the function `float __frcp_rz(float __x) { return __ocml_div_rtz_f32(1.0f, __x); }`?
Error message:
```
lld: error: undefined hidden symbol: __ocml_div_rtz_f32
>>> referenced by __clang_hip_math.h:667 (/opt/rocm-6.1.3/lib/llvm/lib/clang/17/include/__clang_hip_math.h:667)
>>> /tmp/texture-gfx1100-c578c2.o:(TextureFwdKernelCubeNearest1(TextureKernelParams))
... (similar references for other instances)
```

Compilation and linking options:

```python
compile_opts = [
'-DROCM_TORCH', '-DOCML_BASIC_ROUNDED_OPERATIONS'
'-mprintf-kind=buffered', '-g', '-O3', '-w'
'-locml',
'-lamdhip64'
]

link_opts = [
#'-Wl,--no-as-needed',
'-locml',
#'-lhip_hcc',
'-lamdhip64'
]

CUDAExtension(
name="nvdiffrast._C",
sources=source_paths,
extra_compile_args={"nvcc": compile_opts, "hipcc": compile_opts, "cxx": cxx_compiler_flags},
#extra_link_flags={"nvcc": link_opts, "hipcc": link_opts, "cxx": link_opts},
extra_link_flags=link_opts,
extra_link_args=link_opts,
)
```

Please note that the translation provided is a direct translation of the text as requested. However, for technical support or detailed explanations regarding the CUDA and HIP functions, it would be best to consult the official documentation or reach out to the respective communities or support channels.

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

Intel(R) Xeon(R) E-2176M  CPU @ 2.70GHz

### GPU

AMD Radeon Pro W7900

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_