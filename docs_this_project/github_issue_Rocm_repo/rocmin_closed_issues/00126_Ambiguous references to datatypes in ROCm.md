# Ambiguous references to datatypes in ROCm

- **Issue #:** 126
- **State:** closed
- **Created:** 2017-06-08T20:35:03Z
- **Updated:** 2017-06-12T21:11:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/126

Hello,

I'm running into a name conflict with many of the hip/hcc datatypes such as uchar1-uchar4, float2, char1-char3, etc.

The compilation errors are all along the same message of:

>
In file included from /server-home1/acyeh/relion/relion/src/gpu_utils/cuda_mem_utils.h:6:
In file included from /opt/rocm/hip/include/hip/hip_runtime.h:55:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_runtime.h:48:
In file included from /opt/rocm/hip/include/hip/hip_runtime_api.h:258:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_runtime_api.h:40:
In file included from /opt/rocm/hip/include/hip/hip_texture.h:27:
In file included from /opt/rocm/hip/include/hip/hcc_detail/hip_texture.h:35: 
In file included from /opt/rocm/hip/include/hip/hcc_detail/channel_descriptor.h:27:
/opt/rocm/hip/include/hip/hcc_detail/hip_vector_types.h:1167:42: error: reference to 'uchar1' is ambiguous
DECLOP_MAKE_ONE_COMPONENT(unsigned char, uchar1);
                                         ^
/opt/rocm/hip/include/hip/hcc_detail/hip_vector_types.h:73:8: note: candidate found by name lookup is 'uchar1'
struct uchar1 {
       ^
/opt/rocm/hcc/include/hc_short_vector.inl:45:1: note: candidate found by name lookup is 'hc::short_vector::uchar1'
DECLARE_VECTOR_TYPE_CLASS(unsigned char, uchar);
^
/opt/rocm/hcc/include/hc_short_vector.inl:26:37: note: expanded from macro 'DECLARE_VECTOR_TYPE_CLASS'
typedef __vector<SCALAR_TYPE, 1>    CLASS_PREFIX ## 1; \
                                    ^
<scratch space>:131:1: note: expanded from here
uchar1

Here are the results of hipcc --version:

> HIP version: 1.0.17174
HCC clang version 5.0.0  (based on HCC 1.0.17172-ac6fc20-ae1d3ca-6d828a3 )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/hcc/bin

EDIT: added which files were included in the directory