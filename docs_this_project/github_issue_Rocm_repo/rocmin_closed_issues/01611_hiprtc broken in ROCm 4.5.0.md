# hiprtc broken in ROCm 4.5.0

- **Issue #:** 1611
- **State:** closed
- **Created:** 2021-11-04T16:27:58Z
- **Updated:** 2022-02-04T11:58:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/1611

Our code, PyFR, has been using hiprtc for ~9 months now without issue across several versions of ROCm (I am unsure why the release notes are claiming it as a new API with 4.5.0).  However, we are observing problems with the newly released ROCm 4.5.0.  Specifically, our kernels which we compile at runtime have `#include <hip/hip_runtime.h>` as this is needed to get access to `hipThreadIdx_x` and friends.  However, with 4.5.0 this include results in a string of compiler errors from the runtime:
```
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:55:46: error: redefinition of 'enable_if'
template <bool __B, class __T = void> struct enable_if {};
^
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:55:46: note: previous definition is here
template <bool __B, class __T = void> struct enable_if {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:56:29: error: redefinition of 'enable_if<true, __T>'
template <class __T> struct enable_if<true, __T> { typedef __T type; };
^~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:56:29: note: previous definition is here
template <class __T> struct enable_if<true, __T> { typedef __T type; };
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:58:8: error: redefinition of 'true_type'
struct true_type { static const __constant__ bool value = true; };
^
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:58:8: note: previous definition is here
struct true_type { static const __attribute__((constant)) bool value = true; };
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:59:8: error: redefinition of 'false_type'
struct false_type { static const __constant__ bool value = false; };
^
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:59:8: note: previous definition is here
struct false_type { static const __attribute__((constant)) bool value = false; };
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:60:26: error: redefinition of 'true_or_false_type'
template<bool _B> struct true_or_false_type : public false_type {};
^
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:60:26: note: previous definition is here
template<bool _B> struct true_or_false_type : public false_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:61:19: error: redefinition of 'true_or_false_type<true>'
template<> struct true_or_false_type<true> : public true_type {};
^~~~~~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:61:19: note: previous definition is here
template<> struct true_or_false_type<true> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:63:29: error: redefinition of 'is_integral'
template <class _Tp> struct is_integral : public false_type {};
^
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:63:29: note: previous definition is here
template <class _Tp> struct is_integral : public false_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:64:20: error: redefinition of 'is_integral<bool>'
template <> struct is_integral<bool> : public true_type {};
^~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:64:20: note: previous definition is here
template <> struct is_integral<bool> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:65:20: error: redefinition of 'is_integral<char>'
template <> struct is_integral<char> : public true_type {};
^~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:65:20: note: previous definition is here
template <> struct is_integral<char> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:66:20: error: redefinition of 'is_integral<signed char>'
template <> struct is_integral<signed char> : public true_type {};
^~~~~~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:66:20: note: previous definition is here
template <> struct is_integral<signed char> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:67:20: error: redefinition of 'is_integral<unsigned char>'
template <> struct is_integral<unsigned char> : public true_type {};
^~~~~~~~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:67:20: note: previous definition is here
template <> struct is_integral<unsigned char> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:68:20: error: redefinition of 'is_integral<wchar_t>'
template <> struct is_integral<wchar_t> : public true_type {};
^~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:68:20: note: previous definition is here
template <> struct is_integral<wchar_t> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:69:20: error: redefinition of 'is_integral<short>'
template <> struct is_integral<short> : public true_type {};
^~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:69:20: note: previous definition is here
template <> struct is_integral<short> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:70:20: error: redefinition of 'is_integral<unsigned short>'
template <> struct is_integral<unsigned short> : public true_type {};
^~~~~~~~~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:70:20: note: previous definition is here
template <> struct is_integral<unsigned short> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:71:20: error: redefinition of 'is_integral<int>'
template <> struct is_integral<int> : public true_type {};
^~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:71:20: note: previous definition is here
template <> struct is_integral<int> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:72:20: error: redefinition of 'is_integral<unsigned int>'
template <> struct is_integral<unsigned int> : public true_type {};
^~~~~~~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:72:20: note: previous definition is here
template <> struct is_integral<unsigned int> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:73:20: error: redefinition of 'is_integral<long>'
template <> struct is_integral<long> : public true_type {};
^~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:73:20: note: previous definition is here
template <> struct is_integral<long> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:74:20: error: redefinition of 'is_integral<unsigned long>'
template <> struct is_integral<unsigned long> : public true_type {};
^~~~~~~~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:74:20: note: previous definition is here
template <> struct is_integral<unsigned long> : public true_type {};
^
In file included from /tmp/comgr-8b6112/input/CompileSource:1:
In file included from /opt/rocm-4.5.0/include/hip/hip_runtime.h:62:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_runtime.h:79:
In file included from /opt/rocm-4.5.0/include/hip/amd_detail/hip_ldg.h:27:
/opt/rocm-4.5.0/include/hip/amd_detail/amd_hip_vector_types.h:75:20: error: redefinition of 'is_integral<long long>'
template <> struct is_integral<long long> : public true_type {};
^~~~~~~~~~~~~~~~~~~~~~
/long_pathname_so_that_rpms_can_package_the_debug_info/src/external/hipamd/include/hip/amd_detail/amd_hip_vector_types.h:75:20: note: previous definition is here
template <> struct is_integral<long long> : public true_type {};
^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated when compiling for gfx908.
Error: Failed to compile source (from CL or HIP source to LLVM IR).
```

The issue appears to be that files included by `hip_runtime.h` are redefining types.

The release notes state the the hiprtc behaviour has been changed to more closely match nvrtc.  However, nvrtc defines equivalent values to `hipThreadIdx_x` (`threadIdx.x`).  