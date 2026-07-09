# valgrind error

- **Issue #:** 991
- **State:** closed
- **Created:** 2020-01-03T13:45:26Z
- **Updated:** 2023-12-18T17:21:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/991

Reproducer can be found [here](https://github.com/GrokImageCompression/latke)

```
==5442== Mismatched free() / delete / delete []
==5442==    at 0x4C3123B: operator delete(void*) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==5442==    by 0x5DB9D4A: amd::hsa::loader::AmdHsaCodeLoader::DestroyExecutable(amd::hsa::loader::Executable*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x5D9901E: HSA::hsa_executable_destroy(hsa_executable_s) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x4F93173: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==    by 0x10FD2CBF: ???
==5442==    by 0x4F942E6: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==    by 0x11E507BF: ???
==5442==    by 0x4F442D2: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==  Address 0x10949d10 is 0 bytes inside a block of size 51 alloc'd
==5442==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==5442==    by 0x5A0B9B9: strdup (strdup.c:42)
==5442==    by 0x5DC26FE: amd::hsa::loader::ExecutableImpl::Freeze(char const*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x5DB9C05: amd::hsa::loader::AmdHsaCodeLoader::FreezeExecutable(amd::hsa::loader::Executable*, char const*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x5D99311: HSA::hsa_executable_freeze(hsa_executable_s, char const*) (in /opt/rocm/hsa/lib/libhsa-runtime64.so.1.1.9)
==5442==    by 0x4F93FAD: ??? (in /opt/rocm/opencl/lib/x86_64/libamdocl64.so)
==5442==    by 0x100000000001101: ???
==5442==    by 0x76D5C3F: ???
==5442==    by 0x7C2AE3F: ???
==5442==    by 0x10907CEF: ???
==5442==    by 0x30: ???
==5442==    by 0x18: ???
==5442== 
```