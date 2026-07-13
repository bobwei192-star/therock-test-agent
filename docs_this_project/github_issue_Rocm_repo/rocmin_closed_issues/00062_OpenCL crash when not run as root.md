# OpenCL crash when not run as root

- **Issue #:** 62
- **State:** closed
- **Created:** 2016-12-28T21:38:03Z
- **Updated:** 2017-01-04T03:20:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/62

If I sudo clinfo (included with ROCm) or other OpenCL runtime using programs, things work fine, but if I run as a normal user - I get segfaults.

Ubuntu 16.04, with the 4.6.0 kfd compute rocm rel kernel. Side question - is this kernel necessary for running in 16.04 with the rest of the rocm ecosystem?  I know KFD is up streamed and all but I just want to confirm expectations that for now only the rocm repository kernel is blessed.

  KFD permissions:
```
ls -l /dev/kfd
crw-rw-rw- 1 root root 244, 0 Dec 27 13:57 /dev/kfd
```
  gdb output:
```
Program received signal SIGSEGV, Segmentation fault.
0x00007ffff061bd22 in amdgpu_query_gpu_info ()
   from /usr/lib/x86_64-linux-gnu/amdgpu-pro/libdrm_amdgpu.so.1
```
  strace:
```
[pid 11117] open("/usr/lib/x86_64-linux-gnu/amdgpu-pro/libdrm_amdgpu.so.1", O_RDONLY|O_CLOEXEC) = 8
[pid 11117] read(8, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\32\0\0\0\0\0\0"..., 832) = 832
[pid 11117] fstat(8, {st_mode=S_IFREG|0644, st_size=39680, ...}) = 0
[pid 11117] mmap(NULL, 2135328, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 8, 0) = 0x7fe873f6e000
[pid 11117] mprotect(0x7fe873f78000, 2093056, PROT_NONE) = 0
[pid 11117] mmap(0x7fe874177000, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 8, 0x9000) = 0x7fe874177000
[pid 11117] close(8)                    = 0
[pid 11117] munmap(0x7fe883ec7000, 122004) = 0
[pid 11117] fstat(-1, 0x7fffb93330f0)   = -1 EBADF (Bad file descriptor)
[pid 11117] ioctl(-1, DRM_IOCTL_GET_CLIENT, 0x7fffb9333190) = -1 EBADF (Bad file descriptor)
[pid 11117] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x110} ---
[pid 11117] +++ killed by SIGSEGV (core dumped) +++
```

Please let me know if you have any ideas of misconfigurations I might have.