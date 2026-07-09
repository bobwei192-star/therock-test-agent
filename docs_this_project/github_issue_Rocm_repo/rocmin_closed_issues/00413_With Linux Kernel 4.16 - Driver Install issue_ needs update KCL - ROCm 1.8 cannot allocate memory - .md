# With Linux Kernel 4.16 - Driver Install issue, needs update KCL - ROCm 1.8 cannot allocate memory - Need Update Driver with new KCL

- **Issue #:** 413
- **State:** closed
- **Created:** 2018-05-12T22:08:39Z
- **Updated:** 2019-04-24T10:54:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/413

strace output since updating to 1.8 for saxpy

```
futex(0x7f07a87320a8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
open("/opt/rocm/bin/../lib/libmcwamp_hsa.so", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\20<\3\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=5428200, ...}) = 0
mmap(NULL, 6126192, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f07a5b37000
mprotect(0x7f07a5bd5000, 2093056, PROT_NONE) = 0
mmap(0x7f07a5dd4000, 3387392, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x9d000) = 0x7f07a5dd4000
close(3)                                = 0
mprotect(0x7f07a5dd4000, 12288, PROT_READ) = 0
getpid()                                = 9611
open("/dev/kfd", O_RDWR|O_CLOEXEC)      = -1 ENOMEM (Cannot allocate memory)
mmap(NULL, 2052096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f07a5942000
write(2, "There is no device can be used t"..., 53There is no device can be used to do the computation
) = 53
```
I upgraded to kernel 4.16, this was occurring both and after

hoping this is normal
```
philix@fad:~/sand/tmp/hcc$ ll /opt/rocm/lib
lrwxrwxrwx 1 root   root        65 May 12 23:54 libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a -> /opt/rocm/hcc/lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.
```

the following does not exist
```
/opt/rocm/hcc/lib/libclang_rt.builtins-@CMAKE_SYSTEM_PROCESSOR@.a
```