# [Issue]: ROCm on WSL2 failed on RX 7800 XT

- **Issue #:** 3402
- **State:** closed
- **Created:** 2024-07-07T10:17:44Z
- **Updated:** 2026-05-14T19:41:14Z
- **Labels:** AMD Radeon RX 7900 XT, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3402

### Problem Description

Hello. I am planning to use ROCm 6.1.3 on Windows WSL2. As you can see, the latest 24.6.1 driver released by AMD officially supports the installation and use of ROCm on WSL2, but my RX 7800 XT, which I use, is not listed in the support list. However, my graphics card can use ROCm normally on the Linux platform and run PyTorch projects, so I wanted to see if it would work on WSL2 as well. After following the official guidance, I installed ROCm 6.1.3 on my WSL2, but the rocminfo command seems to fail to run successfully. It gave the following error:

```bash
ROCR: unsupported GPU
hsa api call failure at: ./sources/wsl/tools/rocminfo/rocminfo.cc:1087
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

Furthermore, I wanted to know the specific details of the error, so I used the 'strace' tool for debugging:

```bash
strace -o rocminfo_trace.txt /opt/rocm/bin/rocminfo
```

I obtained the following results:

```bash
execve("/usr/bin/rocminfo", ["rocminfo"], 0x7ffd5d11cc30 /* 14 vars */) = 0
brk(NULL)                               = 0x585d5daba000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffd3ed39f80) = -1 EINVAL (Invalid argument)
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x76f39a852000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/glibc-hwcaps/x86-64-v3/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/glibc-hwcaps/x86-64-v3", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/glibc-hwcaps/x86-64-v2/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/glibc-hwcaps/x86-64-v2", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls/haswell/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls/haswell/x86_64", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls/haswell/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls/haswell", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls/x86_64", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/tls", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/haswell/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/haswell/x86_64", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/haswell/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/haswell", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/x86_64", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/foreman/build/hsa-runtime-rocr4wsl-amdgpu-1.13.0/../hsa-runtime-rocr4wsl-amdgpu-1.13.0/rocr4wsl", 0x7ffd3ed391a0, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=29383, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 29383, PROT_READ, MAP_PRIVATE, 3, 0) = 0x76f39a84a000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-6.1.3/lib/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=581064, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 590864, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a7b9000
mprotect(0x76f39a7ca000, 491520, PROT_NONE) = 0
mmap(0x76f39a7ca000, 360448, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x11000) = 0x76f39a7ca000
mmap(0x76f39a822000, 126976, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x69000) = 0x76f39a822000
mmap(0x76f39a842000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x88000) = 0x76f39a842000
mmap(0x76f39a848000, 5136, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x76f39a848000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=2260296, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 2275520, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a400000
mprotect(0x76f39a49a000, 1576960, PROT_NONE) = 0
mmap(0x76f39a49a000, 1118208, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x9a000) = 0x76f39a49a000
mmap(0x76f39a5ab000, 454656, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1ab000) = 0x76f39a5ab000
mmap(0x76f39a61b000, 57344, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x21a000) = 0x76f39a61b000
mmap(0x76f39a629000, 10432, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x76f39a629000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=125488, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 127720, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a799000
mmap(0x76f39a79c000, 94208, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x76f39a79c000
mmap(0x76f39a7b3000, 16384, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a000) = 0x76f39a7b3000
mmap(0x76f39a7b7000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1d000) = 0x76f39a7b7000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\237\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0 \0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0"..., 48, 848) = 48
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0I\17\357\204\3$\f\221\2039x\324\224\323\236S"..., 68, 896) = 68
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=2220400, ...}, AT_EMPTY_PATH) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2264656, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a000000
mprotect(0x76f39a028000, 2023424, PROT_NONE) = 0
mmap(0x76f39a028000, 1658880, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x76f39a028000
mmap(0x76f39a1bd000, 360448, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1bd000) = 0x76f39a1bd000
mmap(0x76f39a216000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x215000) = 0x76f39a216000
mmap(0x76f39a21c000, 52816, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x76f39a21c000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/wsl/lib/libdxcore.so", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0555, st_size=942048, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 968348, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a6ac000
mmap(0x76f39a70f000, 512000, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x62000) = 0x76f39a70f000
mmap(0x76f39a78c000, 32768, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xde000) = 0x76f39a78c000
mmap(0x76f39a794000, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xe5000) = 0x76f39a794000
mmap(0x76f39a795000, 13980, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x76f39a795000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libelf.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=117400, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x76f39a6aa000
mmap(NULL, 119176, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a68c000
mprotect(0x76f39a68f000, 102400, PROT_NONE) = 0
mmap(0x76f39a68f000, 81920, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x76f39a68f000
mmap(0x76f39a6a3000, 16384, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17000) = 0x76f39a6a3000
mmap(0x76f39a6a8000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b000) = 0x76f39a6a8000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=940560, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 942344, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a319000
mmap(0x76f39a327000, 507904, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xe000) = 0x76f39a327000
mmap(0x76f39a3a3000, 372736, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x8a000) = 0x76f39a3a3000
mmap(0x76f39a3fe000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xe4000) = 0x76f39a3fe000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=21448, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 16424, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a687000
mmap(0x76f39a688000, 4096, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1000) = 0x76f39a688000
mmap(0x76f39a689000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x76f39a689000
mmap(0x76f39a68a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x76f39a68a000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=14432, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 16424, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a682000
mmap(0x76f39a683000, 4096, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1000) = 0x76f39a683000
mmap(0x76f39a684000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x76f39a684000
mmap(0x76f39a685000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x76f39a685000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libz.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=108936, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 110776, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x76f39a666000
mprotect(0x76f39a668000, 98304, PROT_NONE) = 0
mmap(0x76f39a668000, 69632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x76f39a668000
mmap(0x76f39a679000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x13000) = 0x76f39a679000
mmap(0x76f39a680000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19000) = 0x76f39a680000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x76f39a664000
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x76f39a661000
arch_prctl(ARCH_SET_FS, 0x76f39a661740) = 0
set_tid_address(0x76f39a661a10)         = 5144
set_robust_list(0x76f39a661a20, 24)     = 0
rseq(0x76f39a6620e0, 0x20, 0, 0x53053053) = 0
mprotect(0x76f39a216000, 16384, PROT_READ) = 0
mprotect(0x76f39a680000, 4096, PROT_READ) = 0
mprotect(0x76f39a685000, 4096, PROT_READ) = 0
mprotect(0x76f39a68a000, 4096, PROT_READ) = 0
mprotect(0x76f39a3fe000, 4096, PROT_READ) = 0
mprotect(0x76f39a6a8000, 4096, PROT_READ) = 0
mprotect(0x76f39a78c000, 32768, PROT_READ) = 0
mprotect(0x76f39a7b7000, 4096, PROT_READ) = 0
mprotect(0x76f39a61b000, 45056, PROT_READ) = 0
mprotect(0x76f39a842000, 16384, PROT_READ) = 0
mprotect(0x585d5d21b000, 4096, PROT_READ) = 0
mprotect(0x76f39a88c000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x76f39a84a000, 29383)           = 0
openat(AT_FDCWD, "/dev/dxg", O_RDONLY|O_CLOEXEC) = 3
getrandom("\x90\xe0\x8b\xfe\x82\xe4\x89\x51", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x585d5daba000
brk(0x585d5dadb000)                     = 0x585d5dadb000
futex(0x76f39a62977c, FUTEX_WAKE_PRIVATE, 2147483647) = 0
uname({sysname="Linux", nodename="DESKTOP-AUV4FO0", ...}) = 0
ioctl(3, _IOC(_IOC_READ|_IOC_WRITE, 0x47, 0x14, 0x10), 0x7ffd3ed38aa0) = 0
ioctl(3, _IOC(_IOC_READ|_IOC_WRITE, 0x47, 0x14, 0x10), 0x7ffd3ed38aa0) = 0
ioctl(3, _IOC(_IOC_READ|_IOC_WRITE, 0x47, 0x9, 0x18), 0x7ffd3ed37990) = 0
ioctl(3, _IOC(_IOC_READ|_IOC_WRITE, 0x47, 0x9, 0x18), 0x7ffd3ed36d90) = 0
write(2, "ROCR: unsupported GPU\n", 22) = 22
newfstatat(1, "", {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0x2), ...}, AT_EMPTY_PATH) = 0
write(1, "\33[31mhsa api call failure at: ./"..., 76) = 76
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228) = 228
write(1, "\33[0m", 4)                   = 4
exit_group(4104)                        = ?
+++ exited with 8 +++

```

I would like to know if anyone can help fix this issue?

### Operating System

Windows 11 Professional 23H2

### CPU

12th Gen Intel(R) Core(TM) i5-12600KF   3.70 GHz

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.1.0

### ROCm Component

rocminfo

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_