# [Issue]: llvm -O0 bug on gfx1100: Illegal instruction detected: Invalid dpp_ctrl value: wavefront shifts are not supported on GFX10+

- **Issue #:** 5826
- **State:** closed
- **Created:** 2026-01-02T15:55:44Z
- **Updated:** 2026-02-11T20:04:56Z
- **Labels:** status: triage
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5826

### Problem Description

Git commit
commit https://github.com/ggml-org/llama.cpp/commit/b96b82fc852b83ea6f58ffcdc264308f60f79211

Operating systems
Windows

GGML backends
HIP

Problem description & steps to reproduce
Environment

OS: Windows 11
GPU: AMD Radeon RX 7900 XTX (gfx1100 / RDNA3)
HIP SDK / ROCm: 6.4
Compiler: clang++ from ROCm 6.4
Build system: CMake + Ninja
Summary

When building llama.cpp with HIP enabled on Windows using Debug configuration, compilation fails with an illegal DPP instruction error targeting gfx1100.
The same configuration builds successfully in Release mode.

This appears to be a compiler/backend issue triggered only in Debug builds (-O0), where LLVM emits unsupported DPP wavefront shift instructions for GFX10+ GPUs.

CMake Configuration

cmake .. -G Ninja ^
  -DCMAKE_BUILD_TYPE=Debug ^
  -DLLAMA_CURL=OFF ^
  -DCMAKE_C_COMPILER="D:/AMD/ROCm/6.4/bin/clang.exe" ^
  -DCMAKE_CXX_COMPILER="D:/AMD/ROCm/6.4/bin/clang++.exe" ^
  -DCMAKE_CXX_FLAGS="-Og -g -Wno-everything" ^
  -DCMAKE_C_FLAGS="-Og -g -Wno-everything" ^
  -DGGML_HIP=ON ^
  -DGGML_HIPBLAS=ON ^
  -DGGML_HIP_ROCWMMA_FATTN=OFF ^
  -DGGML_HIP_CXX_FLAGS="-w" ^
  -DGPU_TARGETS="gfx1100"
Build Failure

The build fails while compiling a HIP source file:

ggml/src/ggml-cuda/mmf.cu

with the following error:

error: Illegal instruction detected: Invalid dpp_ctrl value:
wavefront shifts are not supported on GFX10+

renamable $vgpr2 = V_MOV_B32_dpp $vgpr2(tied-def 0), $vgpr1,
dpp_ctrl:304, row_mask:15, bank_mask:15

16 warnings and 1 error generated when compiling for gfx1100.

This happens only in Debug builds.
Release builds succeed without any issues.

Additional Observations

GGML_HIP_ROCWMMA_FATTN is explicitly disabled, so this does not appear to be related to ROCWMMA attention kernels.

The error is triggered during compilation, not at runtime.

The generated instruction uses a DPP wavefront shift, which is not supported on GFX10+ (including GFX11 / gfx1100).

This strongly suggests a LLVM/HIP codegen issue under Debug / -O0, where unsupported DPP instructions are emitted.

Using optimization levels like -Og or -O1 avoids similar issues elsewhere, but the Debug configuration still ends up passing -O0 to the HIP compilation.

Expected Behavior

Debug builds with HIP enabled should not emit illegal DPP instructions for GFX10+ GPUs, and should compile successfully, similar to Release builds.

Actual Behavior

Debug build fails during HIP compilation due to illegal DPP wavefront shift instructions.

Possible Cause (Speculation)

LLVM HIP backend appears to emit legacy DPP wavefront shift instructions when compiling with -O0 for gfx1100, which are invalid on GFX10+ architectures.
Release builds likely optimize away or rewrite the affected IR paths.

Please let me know if additional logs, compiler flags, or a minimal reproduction would be helpful.

Thank you for your work on llama.cpp.

First Bad Commit
No response

Compile command
cmake .. -G Ninja ^
  -DCMAKE_BUILD_TYPE=Debug ^
  -DLLAMA_CURL=OFF ^
  -DCMAKE_C_COMPILER="D:/AMD/ROCm/6.4/bin/clang.exe" ^
  -DCMAKE_CXX_COMPILER="D:/AMD/ROCm/6.4/bin/clang++.exe" ^
  -DCMAKE_CXX_FLAGS="-Og -g -Wno-everything" ^
  -DCMAKE_C_FLAGS="-Og -g -Wno-everything" ^
  -DGGML_HIP=ON ^
  -DGGML_HIPBLAS=ON ^
  -DGGML_HIP_ROCWMMA_FATTN=OFF ^
  -DGGML_HIP_CXX_FLAGS="-w" ^
  -DGPU_TARGETS="gfx1100"
Relevant log output
[383/462] Building CXX object ggml/src/ggml-hip/CMakeFiles/ggml-hip.dir/__/ggml-cuda/mmf.cu.obj
FAILED: ggml/src/ggml-hip/CMakeFiles/ggml-hip.dir/__/ggml-cuda/mmf.cu.obj
ccache D:\AMD\ROCm\6.4\bin\clang++.exe -DGGML_BACKEND_BUILD -DGGML_BACKEND_SHARED -DGGML_HIP_NO_VMM -DGGML_SCHED_MAX_COPIES=4 -DGGML_SHARED -DGGML_USE_HIP -DUSE_PROF_API=1 -D_CRT_SECURE_NO_WARNINGS -D_XOPEN_SOURCE=600 -D__HIP_PLATFORM_AMD__=1 -Dggml_hip_EXPORTS -IU:/cpp/llama.cpp/ggml/src/ggml-hip/.. -IU:/cpp/llama.cpp/ggml/src/../include -isystem D:/AMD/ROCm/6.4/include -Og -g -Wno-everything -O0 -g -Xclang -gcodeview -D_DEBUG -D_DLL -D_MT -Xclang --dependent-lib=msvcrtd -std=gnu++17 -Wmissing-declarations -Wmissing-noreturn -Wall -Wextra -Wpedantic -Wcast-qual -Wno-unused-function -Wunreachable-code-break -Wunreachable-code-return -Wmissing-prototypes -Wextra-semi -x hip --offload-arch=gfx1100 -MD -MT ggml/src/ggml-hip/CMakeFiles/ggml-hip.dir/__/ggml-cuda/mmf.cu.obj -MF ggml\src\ggml-hip\CMakeFiles\ggml-hip.dir\__\ggml-cuda\mmf.cu.obj.d -o ggml/src/ggml-hip/CMakeFiles/ggml-hip.dir/__/ggml-cuda/mmf.cu.obj -c U:/cpp/llama.cpp/ggml/src/ggml-cuda/mmf.cu
In file included from U:/cpp/llama.cpp/ggml/src/ggml-cuda/mmf.cu:2:
In file included from U:/cpp/llama.cpp/ggml/src/ggml-cuda\mmf.cuh:3:
In file included from U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:19:
In file included from U:/cpp/llama.cpp/ggml/src/ggml-cuda\common.cuh:21:
U:/cpp/llama.cpp/ggml/src/ggml-hip/..\ggml-common.h:180:9: warning: anonymous types declared in an anonymous union are an extension [-Wnested-anon-types]
  180 |         struct {
      |         ^
U:/cpp/llama.cpp/ggml/src/ggml-hip/..\ggml-common.h:208:9: warning: anonymous types declared in an anonymous union are an extension [-Wnested-anon-types]
  208 |         struct {
      |         ^
U:/cpp/llama.cpp/ggml/src/ggml-hip/..\ggml-common.h:229:9: warning: anonymous types declared in an anonymous union are an extension [-Wnested-anon-types]
  229 |         struct {
      |         ^
U:/cpp/llama.cpp/ggml/src/ggml-hip/..\ggml-common.h:270:9: warning: anonymous types declared in an anonymous union are an extension [-Wnested-anon-types]
  270 |         struct {
      |         ^
U:/cpp/llama.cpp/ggml/src/ggml-hip/..\ggml-common.h:297:9: warning: anonymous types declared in an anonymous union are an extension [-Wnested-anon-types]
  297 |         struct {
      |         ^
U:/cpp/llama.cpp/ggml/src/ggml-hip/..\ggml-common.h:314:9: warning: anonymous types declared in an anonymous union are an extension [-Wnested-anon-types]
  314 |         struct {
      |         ^
In file included from U:/cpp/llama.cpp/ggml/src/ggml-cuda/mmf.cu:2:
In file included from U:/cpp/llama.cpp/ggml/src/ggml-cuda\mmf.cuh:3:
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:754:87: warning: function 'load_ldmatrix' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
  754 |             tile<32, 4, half2> & t, const half2 * __restrict__ xs0, const int stride) {
      |                                                                                       ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:779:90: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
  779 |             tile<16, 8, int> & D, const tile<16, 4, int> & A, const tile<8, 4, int> & B) {
      |                                                                                          ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:801:90: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
  801 |             tile<16, 8, int> & D, const tile<16, 8, int> & A, const tile<8, 8, int> & B) {
      |                                                                                          ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:829:96: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
  829 |             tile<16, 4, half2> & D, const tile<16, 8, half2> & A, const tile<8, 8, half2> & B) {
      |                                                                                                ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:854:97: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
  854 |             tile<16, 8, half2> & D, const tile<16, 8, half2> & A, const tile<16, 8, half2> & B) {
      |                                                                                                 ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:925:96: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
  925 |             tile<16, 8, float> & D, const tile<16, 8, half2> & A, const tile<8, 8, half2> & B) {
      |                                                                                                ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:950:110: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
  950 |             tile<16, 8, float> & D, const tile<16, 8, nv_bfloat162> & A, const tile<8, 8, nv_bfloat162> & B) {
      |                                                                                                              ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:1127:92: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
 1127 |             tile<32, 32, int> & D, const tile<32, 4, int> & A, const tile<32, 4, int> & B) {
      |                                                                                            ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:1163:126: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
 1163 |             tile<32, 8, float> & D, const tile<32, 4, half2> & A, const tile<8, 4, half2, DATA_LAYOUT_I_MAJOR_MIRRORED> & B) {
      |                                                                                                                              ^
U:/cpp/llama.cpp/ggml/src/ggml-cuda\mma.cuh:1183:126: warning: function 'mma' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
 1183 |             tile<32, 4, half2> & D, const tile<32, 4, half2> & A, const tile<8, 4, half2, DATA_LAYOUT_J_MAJOR_MIRRORED> & B) {
      |                                                                                                                              ^
error: Illegal instruction detected: Invalid dpp_ctrl value: wavefront shifts are not supported on GFX10+
renamable $vgpr2 = V_MOV_B32_dpp $vgpr2(tied-def 0), $vgpr1, 304, 15, 15, -1, implicit $exec
16 warnings and 1 error generated when compiling for gfx1100.
ninja: build stopped: subcommand failed.

### Operating System

Windows

### CPU

AMD 7950x

### GPU

AMD Radeon RX 7900xtx

### ROCm Version

ROCm 6.4

### ROCm Component

llvm-project

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_