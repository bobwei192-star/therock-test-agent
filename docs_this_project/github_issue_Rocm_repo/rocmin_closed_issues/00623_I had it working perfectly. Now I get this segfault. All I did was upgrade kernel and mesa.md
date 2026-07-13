# I had it working perfectly. Now I get this segfault. All I did was upgrade kernel and mesa.

- **Issue #:** 623
- **State:** closed
- **Created:** 2018-11-25T15:11:38Z
- **Updated:** 2018-11-27T05:52:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/623

```
execve("./rocminfo", ["./rocminfo"], 0x7ffe027d29c0 /* 85 vars */) = 0
brk(NULL)                               = 0x55ad5900a000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffe340ab570) = -1 EINVAL (Invalid argument)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/x86_64/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls/x86_64/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/tls/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/tls", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/x86_64/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/x86_64/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/x86_64/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls/x86_64/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/tls/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/tls", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/x86_64/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/x86_64/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/opt/rocm/hsa/lib/x86_64", 0x7ffe340aa7b0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\326\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=410800, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9ff8122000
mmap(NULL, 2508176, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7ebd000
mprotect(0x7f9ff7f1c000, 2097152, PROT_NONE) = 0
mmap(0x7f9ff811c000, 20480, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x5f000) = 0x7f9ff811c000
mmap(0x7f9ff8121000, 1424, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f9ff8121000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=220873, ...}) = 0
mmap(NULL, 220873, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f9ff7e87000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 \220\10\0\0\0\0\0"..., 832) = 832
lseek(3, 1564608, SEEK_SET)             = 1564608
read(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32) = 32
fstat(3, {st_mode=S_IFREG|0755, st_size=14604792, ...}) = 0
lseek(3, 1564608, SEEK_SET)             = 1564608
read(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32) = 32
mmap(NULL, 1631808, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7cf8000
mprotect(0x7f9ff7d81000, 1007616, PROT_NONE) = 0
mmap(0x7f9ff7d81000, 753664, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x89000) = 0x7f9ff7d81000
mmap(0x7f9ff7e39000, 249856, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x141000) = 0x7f9ff7e39000
mmap(0x7f9ff7e77000, 53248, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17e000) = 0x7f9ff7e77000
mmap(0x7f9ff7e84000, 9792, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f9ff7e84000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 \20\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=14240, ...}) = 0
mmap(NULL, 16528, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7cf3000
mmap(0x7f9ff7cf4000, 4096, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1000) = 0x7f9ff7cf4000
mmap(0x7f9ff7cf5000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x7f9ff7cf5000
mmap(0x7f9ff7cf6000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x7f9ff7cf6000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\340f\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=155408, ...}) = 0
lseek(3, 808, SEEK_SET)                 = 808
read(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32) = 32
mmap(NULL, 131528, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7cd2000
mmap(0x7f9ff7cd8000, 61440, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6000) = 0x7f9ff7cd8000
mmap(0x7f9ff7ce7000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15000) = 0x7f9ff7ce7000
mmap(0x7f9ff7ced000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a000) = 0x7f9ff7ced000
mmap(0x7f9ff7cef000, 12744, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f9ff7cef000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/librt.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0  \0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=35096, ...}) = 0
mmap(NULL, 39416, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7cc8000
mmap(0x7f9ff7cca000, 16384, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x7f9ff7cca000
mmap(0x7f9ff7cce000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6000) = 0x7f9ff7cce000
mmap(0x7f9ff7cd0000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x7000) = 0x7f9ff7cd0000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 \320\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=1587104, ...}) = 0
mmap(NULL, 1589272, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7b43000
mmap(0x7f9ff7b50000, 659456, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xd000) = 0x7f9ff7b50000
mmap(0x7f9ff7bf1000, 872448, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xae000) = 0x7f9ff7bf1000
mmap(0x7f9ff7cc6000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x182000) = 0x7f9ff7cc6000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0000C\2\0\0\0\0\0"..., 832) = 832
lseek(3, 792, SEEK_SET)                 = 792
read(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0\201\336\t\36\251c\324\233E\371SoK\5H\334"..., 68) = 68
fstat(3, {st_mode=S_IFREG|0755, st_size=2136840, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9ff7b41000
lseek(3, 792, SEEK_SET)                 = 792
read(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0\201\336\t\36\251c\324\233E\371SoK\5H\334"..., 68) = 68
lseek(3, 864, SEEK_SET)                 = 864
read(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32) = 32
mmap(NULL, 1848896, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff797d000
mprotect(0x7f9ff799f000, 1671168, PROT_NONE) = 0
mmap(0x7f9ff799f000, 1355776, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x22000) = 0x7f9ff799f000
mmap(0x7f9ff7aea000, 311296, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x16d000) = 0x7f9ff7aea000
mmap(0x7f9ff7b37000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b9000) = 0x7f9ff7b37000
mmap(0x7f9ff7b3d000, 13888, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f9ff7b3d000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 0\0\0\0\0\0\0"..., 832) = 832
lseek(3, 93952, SEEK_SET)               = 93952
read(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32) = 32
fstat(3, {st_mode=S_IFREG|0644, st_size=867312, ...}) = 0
lseek(3, 93952, SEEK_SET)               = 93952
read(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32) = 32
mmap(NULL, 103152, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7963000
mprotect(0x7f9ff7966000, 86016, PROT_NONE) = 0
mmap(0x7f9ff7966000, 69632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f9ff7966000
mmap(0x7f9ff7977000, 12288, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x14000) = 0x7f9ff7977000
mmap(0x7f9ff797b000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17000) = 0x7f9ff797b000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libhsakmt.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360D\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=330584, ...}) = 0
mmap(NULL, 169144, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7939000
mprotect(0x7f9ff793d000, 106496, PROT_NONE) = 0
mmap(0x7f9ff793d000, 81920, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x4000) = 0x7f9ff793d000
mmap(0x7f9ff7951000, 20480, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x18000) = 0x7f9ff7951000
mmap(0x7f9ff7957000, 49152, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1d000) = 0x7f9ff7957000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P3\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=100320, ...}) = 0
mmap(NULL, 102424, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff791f000
mmap(0x7f9ff7922000, 65536, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f9ff7922000
mmap(0x7f9ff7932000, 20480, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x13000) = 0x7f9ff7932000
mmap(0x7f9ff7937000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17000) = 0x7f9ff7937000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=47136, ...}) = 0
mmap(NULL, 50592, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7912000
mprotect(0x7f9ff7915000, 32768, PROT_NONE) = 0
mmap(0x7f9ff7915000, 20480, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f9ff7915000
mmap(0x7f9ff791a000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x8000) = 0x7f9ff791a000
mmap(0x7f9ff791d000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xa000) = 0x7f9ff791d000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=59784, ...}) = 0
mmap(NULL, 62096, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff7902000
mprotect(0x7f9ff7905000, 45056, PROT_NONE) = 0
mmap(0x7f9ff7905000, 28672, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7f9ff7905000
mmap(0x7f9ff790c000, 12288, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xa000) = 0x7f9ff790c000
mmap(0x7f9ff7910000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xd000) = 0x7f9ff7910000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9ff7900000
openat(AT_FDCWD, "/opt/rocm/lib/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libz.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libz.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\320!\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=91912, ...}) = 0
mmap(NULL, 2187280, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff76e9000
mprotect(0x7f9ff76ff000, 2093056, PROT_NONE) = 0
mmap(0x7f9ff78fe000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15000) = 0x7f9ff78fe000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libresolv.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libresolv.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libresolv.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libresolv.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 @\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=88200, ...}) = 0
mmap(NULL, 100512, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff76d0000
mprotect(0x7f9ff76d4000, 69632, PROT_NONE) = 0
mmap(0x7f9ff76d4000, 49152, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x4000) = 0x7f9ff76d4000
mmap(0x7f9ff76e0000, 16384, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x10000) = 0x7f9ff76e0000
mmap(0x7f9ff76e5000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x14000) = 0x7f9ff76e5000
mmap(0x7f9ff76e7000, 6304, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f9ff76e7000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm/lib/libudev.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/hsa/lib/libudev.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/opt/rocm/lib/libudev.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libudev.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 @\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=124888, ...}) = 0
mmap(NULL, 129288, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f9ff76b0000
mmap(0x7f9ff76b4000, 77824, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x4000) = 0x7f9ff76b4000
mmap(0x7f9ff76c7000, 28672, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17000) = 0x7f9ff76c7000
mmap(0x7f9ff76ce000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1d000) = 0x7f9ff76ce000
close(3)                                = 0
writev(2, [{iov_base="./rocminfo", iov_len=10}, {iov_base=": ", iov_len=2}, {iov_base="/opt/rocm/hsa/lib/libhsa-runtime"..., iov_len=39}, {iov_base=": ", iov_len=2}, {iov_base="no version information available"..., iov_len=57}, {iov_base="\n", iov_len=1}], 6./rocminfo: /opt/rocm/hsa/lib/libhsa-runtime64.so.1: no version information available (required by ./rocminfo)
) = 111
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9ff76ae000
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9ff76ab000
arch_prctl(ARCH_SET_FS, 0x7f9ff76ab740) = 0
mprotect(0x7f9ff7b37000, 16384, PROT_READ) = 0
mprotect(0x7f9ff7ced000, 4096, PROT_READ) = 0
mprotect(0x7f9ff76ce000, 4096, PROT_READ) = 0
mprotect(0x7f9ff76e5000, 4096, PROT_READ) = 0
mprotect(0x7f9ff78fe000, 4096, PROT_READ) = 0
mprotect(0x7f9ff7910000, 4096, PROT_READ) = 0
mprotect(0x7f9ff791d000, 4096, PROT_READ) = 0
mprotect(0x7f9ff7937000, 4096, PROT_READ) = 0
mprotect(0x7f9ff7cd0000, 4096, PROT_READ) = 0
mprotect(0x7f9ff7957000, 4096, PROT_READ) = 0
mprotect(0x7f9ff797b000, 4096, PROT_READ) = 0
mprotect(0x7f9ff7cc6000, 4096, PROT_READ) = 0
mprotect(0x7f9ff7cf6000, 4096, PROT_READ) = 0
mprotect(0x7f9ff7e77000, 49152, PROT_READ) = 0
mprotect(0x7f9ff811c000, 16384, PROT_READ) = 0
mprotect(0x55ad58ec8000, 4096, PROT_READ) = 0
mprotect(0x7f9ff814d000, 4096, PROT_READ) = 0
munmap(0x7f9ff7e87000, 220873)          = 0
set_tid_address(0x7f9ff76aba10)         = 5643
set_robust_list(0x7f9ff76aba20, 24)     = 0
rt_sigaction(SIGRTMIN, {sa_handler=0x7f9ff7cd8130, sa_mask=[], sa_flags=SA_RESTORER|SA_SIGINFO, sa_restorer=0x7f9ff7ce43c0}, NULL, 8) = 0
rt_sigaction(SIGRT_1, {sa_handler=0x7f9ff7cd81d0, sa_mask=[], sa_flags=SA_RESTORER|SA_RESTART|SA_SIGINFO, sa_restorer=0x7f9ff7ce43c0}, NULL, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
brk(NULL)                               = 0x55ad5900a000
brk(0x55ad5902b000)                     = 0x55ad5902b000
openat(AT_FDCWD, "/proc/self/status", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "Name:\trocminfo\nUmask:\t0003\nState"..., 1024) = 1024
close(3)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(3, /* 10 entries */, 32768)  = 312
openat(AT_FDCWD, "/sys/devices/system/node/node0/meminfo", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(4, "Node 0 MemTotal:       16413076 "..., 4096) = 1070
read(4, "", 4096)                       = 0
close(4)                                = 0
getdents64(3, /* 0 entries */, 32768)   = 0
close(3)                                = 0
sched_getaffinity(0, 512, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) = 40
openat(AT_FDCWD, "/sys/devices/system/cpu", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(3, /* 30 entries */, 32768)  = 864
getdents64(3, /* 0 entries */, 32768)   = 0
close(3)                                = 0
openat(AT_FDCWD, "/proc/self/status", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "Name:\trocminfo\nUmask:\t0003\nState"..., 1024) = 1024
read(3, "Mems_allowed_list:\t0\nvoluntary_c"..., 1024) = 80
read(3, "", 1024)                       = 0
close(3)                                = 0
clock_getres(CLOCK_MONOTONIC_RAW, {tv_sec=0, tv_nsec=1}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=505883379}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=505911131}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=505931069}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=505951006}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=505971104}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=505991522}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506011490}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506031397}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506051024}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506070490}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506091049}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506110946}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506130623}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506150741}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506170548}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506199422}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506219920}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506240369}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506259805}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506280384}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506300251}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506320198}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506340987}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506360694}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506380461}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506400659}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506420617}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506440564}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506460912}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506480669}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506501048}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506520745}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506540321}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506560659}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506580116}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506600324}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506620161}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506639998}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506659465}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506678190}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506697005}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506716682}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506736750}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506756567}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506776364}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506796041}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506816078}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506835705}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506856123}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506876522}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506896710}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506917408}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506937937}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506957484}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506977892}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=506997458}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507017326}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507037734}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507057922}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507078190}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507097947}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507117413}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507137441}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507156958}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507177015}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507196933}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507217010}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507237298}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507256925}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507277073}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507297331}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507316857}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507340171}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507360559}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507380216}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507400404}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507420682}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507440870}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507460928}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507480885}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507500742}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507520810}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507540467}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507560364}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507580201}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507600449}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507624414}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507647327}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507671643}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507690448}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507710546}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507729942}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507750400}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507770117}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507789604}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507809762}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507829338}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507849576}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507869394}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507891465}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507917684}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507938102}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507957629}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507978107}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=507998285}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508018082}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508038671}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508058689}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508079117}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508099665}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508119452}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508139430}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508159648}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508179134}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508199533}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508219550}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508239407}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508259315}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508278922}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508299019}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508319077}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508338553}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508358631}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508378919}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508398816}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508418794}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508438501}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508458518}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508478526}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508501309}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508521827}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508541955}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508561632}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508581900}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508601396}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508621073}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508640920}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508659806}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508678391}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508697036}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508716572}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508736540}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508755806}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508775893}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508795380}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508815377}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508835084}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508854681}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508874498}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508894005}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508917930}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508937947}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508958065}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508977441}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=508997990}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509017627}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509037494}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509057582}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509077068}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509096895}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509117213}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509136690}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509156988}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509176645}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509196582}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509216860}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509236297}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509256304}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509276452}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509296229}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509316046}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509335673}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509355570}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509375698}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509395185}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509415673}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509435631}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509456049}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509476066}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509496495}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509517023}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509538534}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509558802}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509579981}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509601171}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509621048}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509644472}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509663638}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509682303}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509700798}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509720124}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509739651}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509760089}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509780006}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509800144}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509819751}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509839849}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509860287}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509879954}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509899681}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509926321}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509946068}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509965785}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=509986243}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510006681}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510026569}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510046266}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510065862}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510086982}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510107511}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510127117}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510147065}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510166641}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510186909}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510206877}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510226764}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510247393}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510267000}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510286526}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510305973}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510325479}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510345397}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510365584}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510385792}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510405740}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510425837}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510445895}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510465893}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510485259}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510505266}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510524813}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510544821}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510565149}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510584775}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510604322}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510623799}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510643886}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510663323}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510681898}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510700392}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510719929}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510739776}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510762639}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510782887}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510802915}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510822752}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510842719}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510862717}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510882594}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510908422}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510928220}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510948658}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510968435}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=510988052}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511008169}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511027686}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511047653}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511067811}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511088109}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511108327}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511128144}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511150707}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511170524}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511190612}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511228352}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511254291}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511278937}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511299526}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511319674}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511340232}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511364918}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511388302}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511421675}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511447343}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511474955}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511497667}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511518005}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511537883}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511557720}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511578028}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511598066}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511618183}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511637540}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511658188}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511676763}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511695448}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511714253}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511733910}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511753447}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511773384}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511793592}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511814061}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511833487}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511853575}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511873442}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511893279}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511916443}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511936440}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511956007}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=511979791}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512000160}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512019696}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512039644}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512058940}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512077986}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512097131}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512115947}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512135533}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512154499}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512173976}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512193192}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512212037}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512231463}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512250439}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512269675}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512288871}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512307446}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512326632}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512345838}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512369282}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512389029}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512407684}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512427000}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512445635}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512464410}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512482694}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512500899}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512519463}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512538439}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512556783}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512575869}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512594664}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512613971}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512632716}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512651170}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512668803}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512686056}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512703408}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512721082}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512739927}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512758081}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512777056}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512795150}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512813655}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512832290}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512851015}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512869991}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512888155}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512908503}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512927078}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512945482}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512964819}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=512982712}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513001638}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513020633}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513039258}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513062211}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513081207}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513100092}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513119108}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513137472}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513156588}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513174782}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513193287}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513211702}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513235496}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513257698}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513278677}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513299196}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513320325}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513341275}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513361673}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513382261}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513403211}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513425352}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513446752}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513467381}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513487859}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513508658}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513529027}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513554164}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513575654}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513596864}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513617553}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513639133}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513660393}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513680010}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513699697}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513719444}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513739812}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513760871}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513781560}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513802860}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513823669}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513844308}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513869455}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513914049}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=513958833}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514003276}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514047489}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514091592}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514135985}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514180077}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514224501}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514268884}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514313948}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514358412}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514402925}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514446888}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514491191}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514562855}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514609733}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514653756}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514706024}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514751008}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514794460}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514838222}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514877375}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514911579}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514945433}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=514979707}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515010875}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515042224}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515073583}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515104651}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515142803}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515180133}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515218545}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515250314}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515281783}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515312992}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515344331}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515375950}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515407449}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515438868}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515470217}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515501716}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515533135}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515564494}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515595672}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515626510}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515657648}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515688236}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515718963}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515750011}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515781120}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515812258}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515843557}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515874825}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515905954}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515941150}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=515974422}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516005891}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516037290}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516068689}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516099928}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516131246}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516162365}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516193794}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516225102}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516256341}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516287850}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516319579}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516351048}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516382297}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516413786}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516445065}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516476634}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516507913}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516539111}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516576732}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516608161}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516639509}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516670638}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516701185}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516732243}) = 0
clock_gettime(CLOCK_MONOTONIC_RAW, {tv_sec=121, tv_nsec=516763652}) = 0
futex(0x7f9ff7e8469c, FUTEX_WAKE_PRIVATE, 2147483647) = 0
futex(0x7f9ff7e846a8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
getpid()                                = 5643
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = 3
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/system_properties", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(4, "platform_oem 35498446626881\nplat"..., 4096) = 70
read(4, "", 4096)                       = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 5
fstat(5, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(5, /* 4 entries */, 32768)   = 96
getdents64(5, /* 0 entries */, 32768)   = 0
close(5)                                = 0
close(4)                                = 0
access("/sys/bus/pci", R_OK)            = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/gpu_id", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(4, "0\n", 4096)                    = 2
close(4)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/properties", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(4, "cpu_cores_count 12\nsimd_count 0\n"..., 4096) = 371
read(4, "", 4096)                       = 0
openat(AT_FDCWD, "/proc/cpuinfo", O_RDONLY) = 5
fstat(5, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(5, "processor\t: 0\nvendor_id\t: Authen"..., 1024) = 1024
read(5, " decodeassists pausefilter pfthr"..., 1024) = 1024
read(5, "y svm extapic cr8_legacy abm sse"..., 1024) = 1024
read(5, "\ncpuid level\t: 13\nwp\t\t: yes\nflag"..., 1024) = 1024
read(5, "gement: ts ttp tm hwpstate eff_f"..., 1024) = 1024
read(5, "vm_lock nrip_save tsc_scale vmcb"..., 1024) = 1024
read(5, "popcnt aes xsave avx f16c rdrand"..., 1024) = 1024
read(5, "\ninitial apicid\t: 5\nfpu\t\t: yes\nf"..., 1024) = 1024
read(5, "zes\t: 43 bits physical, 48 bits "..., 1024) = 1024
read(5, "v1 xsaves clzero irperf xsaveerp"..., 1024) = 1024
read(5, "mulqdq monitor ssse3 fma cx16 ss"..., 1024) = 1024
read(5, "blings\t: 12\ncore id\t\t: 5\ncpu cor"..., 1024) = 1024
read(5, "es\nclflush size\t: 64\ncache_align"..., 1024) = 1024
read(5, "dseed adx smap clflushopt sha_ni"..., 1024) = 1024
read(5, "ood nopl nonstop_tsc cpuid extd_"..., 1024) = 1024
read(5, "cpu MHz\t\t: 1365.477\ncache size\t:"..., 1024) = 1024
read(5, "pec_store_bypass\nbogomips\t: 8387"..., 1024) = 210
read(5, "", 1024)                       = 0
close(5)                                = 0
close(4)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/gpu_id", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(4, "11656\n", 4096)                = 6
close(4)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/properties", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(4, "cpu_cores_count 0\nsimd_count 176"..., 4096) = 475
read(4, "", 4096)                       = 0
openat(AT_FDCWD, "/usr/share/hwdata/pci.ids", O_RDONLY) = 5
fstat(5, {st_mode=S_IFREG|0644, st_size=1134006, ...}) = 0
read(5, "#\n#\tList of PCI ID's\n#\n#\tVersion"..., 4096) = 4096
read(5, "ard - Lights-Out\n\t007c  NC7770 1"..., 4096) = 4096
brk(0x55ad5904d000)                     = 0x55ad5904d000
read(5, "Channel SCSI Controller\n\t\t1000 1"..., 4096) = 4096
read(5, "00 9351  MegaRAID SAS 9341-24i\n\t"..., 4096) = 4096
read(5, "08E\n\t\t1000 1010  MegaRAID SATA 3"..., 4096) = 4096
read(5, " Lite)\n\t\t8086 9267  RAID Control"..., 4096) = 4096
read(5, "-0X RAID Controller\n\t\t1000 0531 "..., 4096) = 4096
read(5, "0f  Kaveri [Radeon R7 Graphics]\n"..., 4096) = 4096
read(5, "Pavilion t3030.de Desktop PC\n\t\t1"..., 4096) = 4096
read(5, "\t\t1462 7368  K9AG Neo2\n\t\t17f2 50"..., 4096) = 4096
read(5, "ard\n\t\t8086 3411  SDS2 Mainboard\n"..., 4096) = 4096
read(5, " TX]\n\t4e47  R300 GL [FireGL X1]\n"..., 4096) = 4096
read(5, "2023  RV100 QY [Radeon 7000 Evil"..., 4096) = 4096
read(5, "\n\t5952  RD580 Host Bridge\n\t5954 "..., 4096) = 4096
read(5, "Radeon X300/X550/X1050 Series]\n\t"..., 4096) = 4096
read(5, "Radeon R9 360 OEM\n\t\t1682 0907  R"..., 4096) = 4096
read(5, " 6650M\n\t\t1025 059a  Radeon HD 66"..., 4096) = 4096
read(5, "\n\t\t174b e181  Radeon HD 6570\n\t\t1"..., 4096) = 4096
read(5, "Radeon HD 7470M\n\t\t1179 fb41  Rad"..., 4096) = 4096
read(5, "70 Platinum]\n\t\t1043 3001  Tahiti"..., 4096) = 4096
read(5, "B\n\t\t1da2 e366  Nitro+ Radeon RX "..., 4096) = 4096
read(5, "\n\t\t1787 3000  Radeon HD 6570\n\t68"..., 4096) = 4096
read(5, " 6550M]\n\t\t103c 163c  Pavilion dv"..., 4096) = 4096
read(5, "5 0379  Mobility Radeon HD 5650\n"..., 4096) = 4096
read(5, " 5570\n\t\t174b 3000  Radeon HD 651"..., 4096) = 4096
read(5, "deon HD 6330M\n\t\t1179 fdd2  Radeo"..., 4096) = 4096
brk(0x55ad5906f000)                     = 0x55ad5906f000
read(5, "a XT / Amethyst XT [Radeon R9 38"..., 4096) = 4096
read(5, " FireGL V5200]\n\t\t17aa 2007  Thin"..., 4096) = 4096
read(5, "Radeon HD 4850 512MB GDDR3\n\t9443"..., 4096) = 4096
read(5, " [Mobility Radeon HD 2600]\n\t9583"..., 4096) = 4096
read(5, "adeon R5 Graphics\n\t\t103c 8238  R"..., 4096) = 4096
read(5, "534 [Eagle]\n\t0103  82C538\n\t0104 "..., 4096) = 4096
read(5, "PCI) [A5506B]\n\t\t108d 0016  Rapid"..., 4096) = 4096
read(5, "Alta Lite]\n\t0007  Processor to I"..., 4096) = 4096
read(5, "Adapter (575C)\n\t0302  Winnipeg P"..., 4096) = 4096
read(5, "aRAID 428 Ultra RAID Controller\n"..., 4096) = 4096
read(5, "Mini\n\t1512  Family 14h Processor"..., 4096) = 4096
read(5, " AMD-751 [Irongate] System Contr"..., 4096) = 4096
read(5, " i1 AGP\n\t\t1023 8520  CyberBlade "..., 4096) = 4096
read(5, "ller 4e/Di\n\t\t1028 0170  PowerEdg"..., 4096) = 4096
read(5, "ad 16Mb\n\t\t102b 2179  Millennium "..., 4096) = 4096
read(5, "50 PCIe 64MB\n\t\t102b 0947  Parhel"..., 4096) = 4096
read(5, " SCC USB 2.0 EHCI controller\n\t01"..., 4096) = 4096
read(5, "AGP VGA Display Adapter\n\t0330  3"..., 4096) = 4096
read(5, "lerator\n\t\t1019 7018  SiS PCI Aud"..., 4096) = 4096
read(5, "art Array 712m (Mezzanine RAID c"..., 4096) = 4096
read(5, "0 [FireStar]\n\tc701  82C701 [Fire"..., 4096) = 4096
read(5, "ast DV2000 FireWire Controller\n\t"..., 4096) = 4096
brk(0x55ad59091000)                     = 0x55ad59091000
read(5, "Found in Philips ADSL ANNEX A WL"..., 4096) = 4096
read(5, "Family)\n\t909f  Aeolia SATA AHCI "..., 4096) = 4096
read(5, " Processor\n\t\tecc0 0050  Gina24 r"..., 4096) = 4096
read(5, "309  Imagine 128\n\t2339  Imagine "..., 4096) = 4096
read(5, "\t0021  UniNorth GMAC (Sun GEM)\n\t"..., 4096) = 4096
read(5, "apter\n\t165c  FastLinQ QL45000 Se"..., 4096) = 4096
read(5, "PCI-X HBA\n\t6322  SP212-based 2Gb"..., 4096) = 4096
read(5, "HMCU CNA\n\t\t1077 0007  QLogic 2x1"..., 4096) = 4096
read(5, "312  Intel 21554 PCI-PCI bus bri"..., 4096) = 4096
read(5, " 2)\n\t7031  PCI-CAN/2 (Series 2)\n"..., 4096) = 4096
read(5, "ing Module\n\t71bb  PXI-2584\n\t71bc"..., 4096) = 4096
read(5, "8360LT\n\t761f  PXI-2540\n\t7620  PX"..., 4096) = 4096
read(5, "365\n\t\t1093 77a8  PXIe-6375\n\t\t109"..., 4096) = 4096
read(5, "\t144f 3000  MagicTView CPH060 - "..., 4096) = 4096
read(5, "n)\n\t\t1822 0001  VisionPlus DVB C"..., 4096) = 4096
read(5, "card\n\t2540  IXXAT CAN-Interface "..., 4096) = 4096
read(5, "ane, 5-Port PCI Express Gen 3 (8"..., 4096) = 4096
read(5, " 0013  PIKA PrimeNet MM cPCI 8 ("..., 4096) = 4096
read(5, "gabit LOM Ethernet Adapter\n\t\t147"..., 4096) = 4096
read(5, "ast Ethernet Controller\n\t9210  3"..., 4096) = 4096
read(5, "book\n\t\t104d 810f  VAIO PCG-U1 US"..., 4096) = 4096
read(5, "cb  Omron Corporation\n# nee Ment"..., 4096) = 4096
brk(0x55ad590b3000)                     = 0x55ad590b3000
read(5, "\t\t1048 0c3a  Erazor III LT\n\t\t104"..., 4096) = 4096
read(5, "e  ECS Elitegroup NFORCE3-A939 m"..., 4096) = 4096
read(5, "ny)\n\t00e8  nForce3 EHCI USB 2.0 "..., 4096) = 4096
read(5, " Go 6400]\n\t0169  NV44 [GeForce 6"..., 4096) = 4096
read(5, "3842 a341  256A8N341DX\n\t0222  NV"..., 4096) = 4096
read(5, "ce 7900 GS]\n\t0293  G71 [GeForce "..., 4096) = 4096
read(5, "00]\n\t0343  NV36 [GeForce FX 5700"..., 4096) = 4096
read(5, "25 0392  ET1350\n\t\t1028 020e  Ins"..., 4096) = 4096
read(5, "ce 630a]\n\t0541  MCP67 Memory Con"..., 4096) = 4096
read(5, "92GLM [Quadro FX 3800M]\n\t0620  G"..., 4096) = 4096
read(5, "sor\n\t0754  MCP78S [GeForce 8200]"..., 4096) = 4096
read(5, "150-HD\n\t07da  MCP73 Co-processor"..., 4096) = 4096
read(5, "ce 315M\n\t\t1179 fcf2  GeForce 315"..., 4096) = 4096
read(5, "T215 [GeForce GT 330]\n\t0ca2  GT2"..., 4096) = 4096
read(5, "5M]\n\t0fce  GK107M [GeForce GT 64"..., 4096) = 4096
read(5, "5M]\n\t\t103c 2afb  GeForce 705A\n\t\t"..., 4096) = 4096
read(5, "8 06c0  GeForce 820M\n\t\t1028 06c1"..., 4096) = 4096
read(5, "\t\t17aa 361c  GeForce 820A\n\t\t17aa"..., 4096) = 4096
read(5, "[GeForce GTX 650 Ti Boost]\n\t\t104"..., 4096) = 4096
read(5, " GM107 [GeForce GTX 745]\n\t1389  "..., 4096) = 4096
read(5, "Force GTX 1070 Mobile]\n\t1c00  GP"..., 4096) = 4096
read(5, " e311  Lancer Gen6: LPe31000 Fib"..., 4096) = 4096
brk(0x55ad590d5000)                     = 0x55ad590d5000
read(5, "  S5933_HEPC3\n\t80b9  Harmonix Hi"..., 4096) = 4096
read(5, "5 2300  P4TSV Onboard LAN (RTL81"..., 4096) = 4096
read(5, "\n\t0410  Wildcard TE410P (2nd Gen"..., 4096) = 4096
read(5, "0350 Audigy 2 ZS\n\t\t1102 2003  SB"..., 4096) = 4096
read(5, "# SFF-8087 Mini-SAS 16 port inte"..., 4096) = 4096
read(5, "01  Magnia Z310\n\t\t147b a702  KG7"..., 4096) = 4096
read(5, "ax integrated digital audio\n\t\t10"..., 4096) = 4096
read(5, "ost Bridge\n\t\t1297 f641  FX41 mot"..., 4096) = 4096
read(5, "\t4269  KT880 Host Bridge\n\t4282  "..., 4096) = 4096
read(5, " PCI Bridge\n\tb188  VT8237/8251 P"..., 4096) = 4096
read(5, "t76c506 802.11b Wireless Network"..., 4096) = 4096
read(5, "NT3 PCI Express Internal NTB\n\t80"..., 4096) = 4096
read(5, "\n\t\t1131 2001  Proteus Pro [phili"..., 4096) = 4096
read(5, "hnotrend/Hauppauge DVB card rev2"..., 4096) = 4096
read(5, "Cornet NQ\n\t\t1133 1c08  Diva Serv"..., 4096) = 4096
read(5, "space NIC\n\t\t1137 00ce  VIC 1225T"..., 4096) = 4096
read(5, "  SK-9821 V2.0 Gigabit Ethernet "..., 4096) = 4096
read(5, "Adapter\n\t\t115d 0182  Cardbus Eth"..., 4096) = 4096
read(5, "Advanced Computing\n# nee Polaris"..., 4096) = 4096
read(5, "\n\t\t1028 014f  Latitude X300 lapt"..., 4096) = 4096
read(5, " (x1) Gigabit Ethernet Adapter\n\t"..., 4096) = 4096
read(5, " v2 802.11n N1 Wireless Notebook"..., 4096) = 4096
read(5, "GE)\n\t\t1854 0018  Marvell 88E8036"..., 4096) = 4096
brk(0x55ad590f7000)                     = 0x55ad590f7000
read(5, "3 Gigabit Ethernet Controller (A"..., 4096) = 4096
read(5, "nModem\n\t\t1033 8015  LT WinModem "..., 4096) = 4096
read(5, "f\n\t\t1043 8294  LSI FW322/323 IEE"..., 4096) = 4096
read(5, "ibre Channel Adapter\n\t\t117c 003b"..., 4096) = 4096
read(5, "43  SK-9843 SX\n\t\t1202 9844  SK-9"..., 4096) = 4096
read(5, "37  Voodoo3 AGP\n\t\t121a 0038  Voo"..., 4096) = 4096
read(5, " or cPCI-200 Quad IndustryPack c"..., 4096) = 4096
read(5, "35  SMC2835W V2 Wireless Cardbus"..., 4096) = 4096
read(5, "\t\t270f 2200  ES1371, ES1373 Audi"..., 4096) = 4096
read(5, "kerphone Modem\n\t1032  HCF 56k Mo"..., 4096) = 4096
read(5, "9  Xiotech Corporation\n12aa  SDL"..., 4096) = 4096
read(5, "/SC-BUS, T1/PRI adaptor.\n\t0685  "..., 4096) = 4096
read(5, "udio Processor\n\t8803  Vortex 56k"..., 4096) = 4096
read(5, "2000  CyberSerial (1-port) 16550"..., 4096) = 4096
read(5, "\t0207  GLN180PEX GPS/GLONASS rec"..., 4096) = 4096
read(5, " Express Module Bypass Server Ad"..., 4096) = 4096
read(5, "[BeroNet BN4S0]\n\t\t1397 b566  HFC"..., 4096) = 4096
read(5, "cLink GT4 Adapter\n\t00a0  SyncLin"..., 4096) = 4096
read(5, "ce STX)\n\t\t1043 835d  Virtuoso 10"..., 4096) = 4096
read(5, "08  Aloka Co. Ltd\n1409  Timedia "..., 4096) = 4096
read(5, "NetGlobal 56k+10/100Mb CardBus ("..., 4096) = 4096
read(5, "85  T420-4085 SFP+ Unified Wire "..., 4096) = 4096
brk(0x55ad59119000)                     = 0x55ad59119000
read(5, "ernet Controller\n\t5004  T520-BCH"..., 4096) = 4096
read(5, "410  T580-LP-CR Unified Wire Eth"..., 4096) = 4096
read(5, "ge Controller\n\t5581  T540-5081 U"..., 4096) = 4096
read(5, "e Storage Controller\n\t5695  T540"..., 4096) = 4096
read(5, "nified Wire Ethernet Controller "..., 4096) = 4096
read(5, "087  T6225-6087 Unified Wire Eth"..., 4096) = 4096
read(5, "t Controller [VF]\n\t6809  T6210-B"..., 4096) = 4096
read(5, " 1ff6  Express Flash PM1725b 12."..., 4096) = 4096
read(5, " Ltd\n14b1  Nextcom K.K.\n14b2  EN"..., 4096) = 4096
read(5, "4e3  AMTELCO\n14e4  Broadcom Inc."..., 4096) = 4096
read(5, " 8008  BCM5701 1000Base-T\n\t1646 "..., 4096) = 4096
read(5, "er Adapter\n\t\t103c 7052  NC105T P"..., 4096) = 4096
read(5, "57760 Gigabit Ethernet PCIe\n\t169"..., 4096) = 4096
read(5, " Function\n\t\t103c 1916  FlexFabri"..., 4096) = 4096
read(5, "et Controller\n\t16e1  NetXtreme-C"..., 4096) = 4096
read(5, ".11b/g WLAN\n\t\t103c 1356  Broadco"..., 4096) = 4096
read(5, " AirPort Extreme\n\t\t106b 00e4  Ai"..., 4096) = 4096
read(5, "erator\n\t5850  BCM5850 Crypto Acc"..., 4096) = 4096
read(5, "Adapter\n\t1803  HCF 56k Modem\n\t\t0"..., 4096) = 4096
read(5, "613  Leadtek Winfast 2000XP Expe"..., 4096) = 4096
read(5, "  AG COMMUNICATIONS\n14fa  WANDEL"..., 4096) = 4096
read(5, "Reader Controller\n\t0730  ENE PCI"..., 4096) = 4096
brk(0x55ad5913a000)                     = 0x55ad5913a000
read(5, " Security Ltd\n1576  Viewcast COM"..., 4096) = 4096
read(5, "onnectX-3 IB FDR Dual Port Mezza"..., 4096) = 4096
read(5, " 10Gb/s InfiniBand / 10GigE Adap"..., 4096) = 4096
read(5, " Checker\n\t2928  64 Bit, 66MHz PC"..., 4096) = 4096
read(5, "000 Frame Synchronizer and I/O\n\t"..., 4096) = 4096
read(5, "[Intersil ISL3874]\n167e  ONNTO C"..., 4096) = 4096
read(5, "MP55AG v1.2 802.11abg PCI Adapte"..., 4096) = 4096
read(5, "R5416 Wireless Network Adapter ["..., 4096) = 4096
read(5, "2.11b/g/n mini-PCIe card on a se"..., 4096) = 4096
read(5, "DX501 Reconfigurable Digital I/O"..., 4096) = 4096
read(5, "Module\n\t7029  AP342 14-bit, 12-C"..., 4096) = 4096
read(5, " [LiquidIO II] 2-port 25GbE Inte"..., 4096) = 4096
read(5, "ller\n# port 6 of 8\n\t6815  TW6816"..., 4096) = 4096
read(5, "5 4-Port PCIe 3.0 to SAS/SATA 6G"..., 4096) = 4096
read(5, "lite Design [DNPCIe_80G_A10_LL]\n"..., 4096) = 4096
read(5, "ess PCI Adapter\n\t0681  RT2890 Wi"..., 4096) = 4096
read(5, "T\n\tdb30  FusionHDTV DVB-T Pro\n\td"..., 4096) = 4096
read(5, "232/4-PCI-335 Serial PCI Adapter"..., 4096) = 4096
read(5, " Mezzanine Adapter\n\t\t1924 6521  "..., 4096) = 4096
read(5, "450b\n\t1113  FireSpy450bT\n\t1114  "..., 4096) = 4096
read(5, "363 SATA/IDE Controller\n\t\t1043 8"..., 4096) = 4096
read(5, "BMA Virtual Network Adapter\n\t171"..., 4096) = 4096
read(5, "84  Commex Technologies\n\t0001  V"..., 4096) = 4096
brk(0x55ad5915c000)                     = 0x55ad5915c000
read(5, "cker Ethernet switch device\n\t000"..., 4096) = 4096
read(5, "orage\n\t\t1bb1 0101  Nytro XF1440\n"..., 4096) = 4096
read(5, "Electronics Co., Ltd.\n\t0010  Pro"..., 4096) = 4096
read(5, "32B DPDK Data Mover]\n\t\t1d6c 2001"..., 4096) = 4096
read(5, "et SFP+ PCI Express Adapter\n\t\t1f"..., 4096) = 4096
read(5, "a II 2D+3D\n\t07a1  Wildcat III 62"..., 4096) = 4096
read(5, "uner)\n\t\t1461 c03f  C115 PCI vide"..., 4096) = 4096
read(5, "-COM-2SRJ 2x RS422/RS484 Card w/"..., 4096) = 4096
read(5, " (PC104+)\n\t\t4c53 3001  PLUSTEST "..., 4096) = 4096
read(5, "1092 4207  Stealth III S540\n\t\t10"..., 4096) = 4096
read(5, " Module\n\t1600  CooVOX TDM E1/T1 "..., 4096) = 4096
read(5, "cessor Family DRAM Controller\n\t\t"..., 4096) = 4096
read(5, "ess-to-PCI Bridge A\n\t032a  6700P"..., 4096) = 4096
read(5, "\n\t0819  Medfield Serial IO I2C C"..., 4096) = 4096
read(5, "reless-AC 7260\n# Wilkins Peak 2\n"..., 4096) = 4096
read(5, "00 HS-UART\n\t0937  Quark SoC X100"..., 4096) = 4096
read(5, " NVMe 8.0TB 2.5\" U.2 (P4510)\n\t\t1"..., 4096) = 4096
read(5, "3 v4/Xeon D QuickData Technology"..., 4096) = 4096
read(5, " i7 QPI Link 2\n\t0e3e  Xeon E7 v2"..., 4096) = 4096
read(5, "E5 v2/Core i7 Broadcast Register"..., 4096) = 4096
read(5, "Series LPIO2 I2C Controller #6\n\t"..., 4096) = 4096
read(5, "MT Desktop Connection\n\t\t8086 101"..., 4096) = 4096
read(5, "E mainboard\n\t1051  82801EB/ER (I"..., 4096) = 4096
read(5, "PRO/1000 PF Server Adapter\n\t107f"..., 4096) = 4096
brk(0x55ad5917e000)                     = 0x55ad5917e000
read(5, "dapter\n\t\t1014 0380  10-Gigabit X"..., 4096) = 4096
read(5, " 560FLB Adapter\n\t\t1059 0111  T40"..., 4096) = 4096
read(5, "t NIC (embedded)\n\t\t0e11 b0d7  NC"..., 4096) = 4096
read(5, "Port Server Adapter\n\t\t8086 1030 "..., 4096) = 4096
read(5, "17aa 21ce  ThinkPad T520\n\t\t8086 "..., 4096) = 4096
read(5, "\t8086 1f52  1GbE 4P I350 Mezz\n\t1"..., 4096) = 4096
read(5, "-port 562T Adapter\n\t\t1590 00d2  "..., 4096) = 4096
read(5, "0  Ethernet Converged Network Ad"..., 4096) = 4096
read(5, "40-MTP2\n\t15d1  Ethernet Controll"..., 4096) = 4096
read(5, " Gaussian Mixture Model\n\t\t17aa 2"..., 4096) = 4096
read(5, " Mobile SATA Controller (IDE mod"..., 4096) = 4096
read(5, "et Family MEI Controller #2\n\t1c3"..., 4096) = 4096
read(5, "4-Port SATA/SAS Storage Control "..., 4096) = 4096
read(5, "ntroller\n\t\t1043 108d  VivoBook X"..., 4096) = 4096
read(5, "oot Port 3\n\t1f13  Atom processor"..., 4096) = 4096
read(5, "000/J3xxx/N3xxx Series Trusted E"..., 4096) = 4096
read(5, "IDE Controller\n\t2422  82801AB US"..., 4096) = 4096
read(5, "16  Travelmate 612TX\n\t\t104d 80df"..., 4096) = 4096
read(5, " Amilo M1420\n\t\t4c53 1090  Cx9 / "..., 4096) = 4096
read(5, "atitude X300\n\t\t1028 0163  Latitu"..., 4096) = 4096
read(5, " Precision 470\n\t\t1028 016c  Powe"..., 4096) = 4096
read(5, " GA-8IPE1000 Pro2 motherboard (8"..., 4096) = 4096
read(5, "G/GL[Brookdale-G]/GE Chipset Int"..., 4096) = 4096
read(5, "oard Computer\n\t\t1775 1100  CR11/"..., 4096) = 4096
brk(0x55ad591a0000)                     = 0x55ad591a0000
read(5, "028 0170  PowerEdge 6850 DDR Ini"..., 4096) = 4096
read(5, "herboard\n\t\t103c 2a09  PufferM-UL"..., 4096) = 4096
read(5, "\t\t8086 3476  S5000PSLSATA Server"..., 4096) = 4096
read(5, "rEdge SC440\n\t\t1028 01e6  PowerEd"..., 4096) = 4096
read(5, " EHCI Controller\n\t\t1025 006c  98"..., 4096) = 4096
read(5, "rEdge SC440\n\t\t1028 01e6  PowerEd"..., 4096) = 4096
read(5, "0b\n\t\t103c 30c1  Compaq 6910p\n\t\t1"..., 4096) = 4096
read(5, "d T61/R61\n\t\t17c0 4088  Medion WI"..., 4096) = 4096
read(5, "d  CCM-BOOGIE\n\t2935  82801I (ICH"..., 4096) = 4096
read(5, "werEdge T610 USB EHCI Controller"..., 4096) = 4096
read(5, "otherboard: Intel 82P35 Northbri"..., 4096) = 4096
read(5, "ily System Configuration Control"..., 4096) = 4096
read(5, "rated Memory Controller Channel "..., 4096) = 4096
read(5, "00 Integrated Memory Controller "..., 4096) = 4096
read(5, "a Processor Interrupt Controller"..., 4096) = 4096
read(5, "e Agent 1\n\t2f39  Xeon E7 v3/Xeon"..., 4096) = 4096
read(5, " E5 v3/Core i7 DDRIO (VMSE) 2 & "..., 4096) = 4096
read(5, "rocessor to AGP Controller\n\t\t144"..., 4096) = 4096
read(5, "ess Downstream Port E1\n\t\t103c 31"..., 4096) = 4096
read(5, "ry I/O Controller Hub\n\t35b1  310"..., 4096) = 4096
read(5, "O (ICH10 Family) 4-port SATA IDE"..., 4096) = 4096
read(5, "1JI (ICH10 Family) PCI Express R"..., 4096) = 4096
read(5, " Series/3400 Series Chipset 4 po"..., 4096) = 4096
read(5, "0 Series Chipset High Definition"..., 4096) = 4096
read(5, " E5/Core i7 Unicast Register 4\n\t"..., 4096) = 4096
brk(0x55ad591c2000)                     = 0x55ad591c2000
read(5, "o Advanced-N 6200 2x2 AGN\n\t\t8086"..., 4096) = 4096
read(5, " Core Processor PCIe Controller "..., 4096) = 4096
read(5, "annel 1 Registers\n\t65f7  5100 Ch"..., 4096) = 4096
read(5, " DMA Channel 2\n\t6f53  Xeon Proce"..., 4096) = 4096
read(5, "face\n\t6fbe  Xeon E7 v4/Xeon E5 v"..., 4096) = 4096
read(5, "371AB/EB/MB PIIX4 ACPI\n\t\t15ad 19"..., 4096) = 4096
read(5, "KX/GX Memory controller\n\t84ca  4"..., 4096) = 4096
read(5, "Series/C220 Series Chipset Famil"..., 4096) = 4096
read(5, "ries Chipset Family PCI Express "..., 4096) = 4096
read(5, " MS SMBus 1\n\t8d7f  C610/X99 seri"..., 4096) = 4096
read(5, "\n\t9ce0  Wildcat Point-LP Serial "..., 4096) = 4096
read(5, "Series/C230 Series Chipset Famil"..., 4096) = 4096
read(5, "mily Serial IO I2C Controller #3"..., 4096) = 4096
read(5, "s Root Port #12\n\ta29c  200 Serie"..., 4096) = 4096
read(5, "MI\n\t\t1028 02da  OptiPlex 980\n\t\t1"..., 4096) = 4096
read(5, "/AUW/AUWD AIC-7895B\n\t7896  AIC-7"..., 4096) = 4096
read(5, "9005 02bb  3405\n\t\t9005 02bc  380"..., 4096) = 4096
read(5, "-8i\n\t\t9005 0901  SmartHBA 2100-4"..., 4096) = 4096
read(5, "ort Adapter)\n\t9865  PCI 9865 Mul"..., 4096) = 4096
read(5, "410P quad-span T1/E1/J1 card 3.3"..., 4096) = 4096
read(5, "12\n\t351c  DAG 3.5ECM Fast Ethern"..., 4096) = 4096
read(5, "ller\n\t01  Token ring network con"..., 4096) = 3510
read(5, "", 4096)                       = 0
close(5)                                = 0
close(4)                                = 0
openat(AT_FDCWD, "/dev/dri/renderD128", O_RDWR|O_CLOEXEC) = 4
brk(0x55ad591c0000)                     = 0x55ad591c0000
brk(0x55ad591be000)                     = 0x55ad591be000
brk(0x55ad591bc000)                     = 0x55ad591bc000
brk(0x55ad591ba000)                     = 0x55ad591ba000
brk(0x55ad591b8000)                     = 0x55ad591b8000
brk(0x55ad591b6000)                     = 0x55ad591b6000
brk(0x55ad591b4000)                     = 0x55ad591b4000
brk(0x55ad591b2000)                     = 0x55ad591b2000
brk(0x55ad591b0000)                     = 0x55ad591b0000
brk(0x55ad591ae000)                     = 0x55ad591ae000
brk(0x55ad591ac000)                     = 0x55ad591ac000
brk(0x55ad591aa000)                     = 0x55ad591aa000
brk(0x55ad591a8000)                     = 0x55ad591a8000
brk(0x55ad591a6000)                     = 0x55ad591a6000
brk(0x55ad591a4000)                     = 0x55ad591a4000
brk(0x55ad591a2000)                     = 0x55ad591a2000
brk(0x55ad591a0000)                     = 0x55ad591a0000
brk(0x55ad5919e000)                     = 0x55ad5919e000
brk(0x55ad5919c000)                     = 0x55ad5919c000
brk(0x55ad5919a000)                     = 0x55ad5919a000
brk(0x55ad59198000)                     = 0x55ad59198000
brk(0x55ad59196000)                     = 0x55ad59196000
brk(0x55ad59194000)                     = 0x55ad59194000
brk(0x55ad59192000)                     = 0x55ad59192000
brk(0x55ad59190000)                     = 0x55ad59190000
brk(0x55ad5918e000)                     = 0x55ad5918e000
brk(0x55ad5918c000)                     = 0x55ad5918c000
brk(0x55ad5918a000)                     = 0x55ad5918a000
brk(0x55ad59188000)                     = 0x55ad59188000
brk(0x55ad59186000)                     = 0x55ad59186000
brk(0x55ad59184000)                     = 0x55ad59184000
brk(0x55ad59182000)                     = 0x55ad59182000
brk(0x55ad59180000)                     = 0x55ad59180000
brk(0x55ad5917e000)                     = 0x55ad5917e000
brk(0x55ad5917c000)                     = 0x55ad5917c000
brk(0x55ad5917a000)                     = 0x55ad5917a000
brk(0x55ad59178000)                     = 0x55ad59178000
brk(0x55ad59176000)                     = 0x55ad59176000
brk(0x55ad59174000)                     = 0x55ad59174000
brk(0x55ad59172000)                     = 0x55ad59172000
brk(0x55ad59170000)                     = 0x55ad59170000
brk(0x55ad5916e000)                     = 0x55ad5916e000
brk(0x55ad5916c000)                     = 0x55ad5916c000
brk(0x55ad5916a000)                     = 0x55ad5916a000
brk(0x55ad59168000)                     = 0x55ad59168000
brk(0x55ad59166000)                     = 0x55ad59166000
brk(0x55ad59164000)                     = 0x55ad59164000
brk(0x55ad59162000)                     = 0x55ad59162000
brk(0x55ad59160000)                     = 0x55ad59160000
brk(0x55ad5915e000)                     = 0x55ad5915e000
brk(0x55ad5915c000)                     = 0x55ad5915c000
brk(0x55ad5915a000)                     = 0x55ad5915a000
brk(0x55ad59158000)                     = 0x55ad59158000
brk(0x55ad59156000)                     = 0x55ad59156000
brk(0x55ad59154000)                     = 0x55ad59154000
brk(0x55ad59152000)                     = 0x55ad59152000
brk(0x55ad59150000)                     = 0x55ad59150000
brk(0x55ad5914e000)                     = 0x55ad5914e000
brk(0x55ad5914c000)                     = 0x55ad5914c000
brk(0x55ad5914a000)                     = 0x55ad5914a000
brk(0x55ad59148000)                     = 0x55ad59148000
brk(0x55ad59146000)                     = 0x55ad59146000
brk(0x55ad59144000)                     = 0x55ad59144000
brk(0x55ad59142000)                     = 0x55ad59142000
brk(0x55ad59140000)                     = 0x55ad59140000
brk(0x55ad5913e000)                     = 0x55ad5913e000
brk(0x55ad5913c000)                     = 0x55ad5913c000
brk(0x55ad5913a000)                     = 0x55ad5913a000
brk(0x55ad59138000)                     = 0x55ad59138000
brk(0x55ad59136000)                     = 0x55ad59136000
brk(0x55ad59134000)                     = 0x55ad59134000
brk(0x55ad59131000)                     = 0x55ad59131000
brk(0x55ad5912f000)                     = 0x55ad5912f000
brk(0x55ad5912d000)                     = 0x55ad5912d000
brk(0x55ad5912b000)                     = 0x55ad5912b000
brk(0x55ad59129000)                     = 0x55ad59129000
brk(0x55ad59127000)                     = 0x55ad59127000
brk(0x55ad59125000)                     = 0x55ad59125000
brk(0x55ad59123000)                     = 0x55ad59123000
brk(0x55ad59121000)                     = 0x55ad59121000
brk(0x55ad5911f000)                     = 0x55ad5911f000
brk(0x55ad5911d000)                     = 0x55ad5911d000
brk(0x55ad5911b000)                     = 0x55ad5911b000
brk(0x55ad59119000)                     = 0x55ad59119000
brk(0x55ad59117000)                     = 0x55ad59117000
brk(0x55ad59115000)                     = 0x55ad59115000
brk(0x55ad59113000)                     = 0x55ad59113000
brk(0x55ad59111000)                     = 0x55ad59111000
brk(0x55ad5910f000)                     = 0x55ad5910f000
brk(0x55ad5910d000)                     = 0x55ad5910d000
brk(0x55ad5910b000)                     = 0x55ad5910b000
brk(0x55ad59109000)                     = 0x55ad59109000
brk(0x55ad59107000)                     = 0x55ad59107000
brk(0x55ad59105000)                     = 0x55ad59105000
brk(0x55ad59103000)                     = 0x55ad59103000
brk(0x55ad59101000)                     = 0x55ad59101000
brk(0x55ad590ff000)                     = 0x55ad590ff000
brk(0x55ad590fd000)                     = 0x55ad590fd000
brk(0x55ad590fb000)                     = 0x55ad590fb000
brk(0x55ad590f9000)                     = 0x55ad590f9000
brk(0x55ad590f7000)                     = 0x55ad590f7000
brk(0x55ad590f5000)                     = 0x55ad590f5000
brk(0x55ad590f3000)                     = 0x55ad590f3000
brk(0x55ad590f1000)                     = 0x55ad590f1000
brk(0x55ad590ef000)                     = 0x55ad590ef000
brk(0x55ad590ed000)                     = 0x55ad590ed000
brk(0x55ad590eb000)                     = 0x55ad590eb000
brk(0x55ad590e9000)                     = 0x55ad590e9000
brk(0x55ad590e7000)                     = 0x55ad590e7000
brk(0x55ad590e5000)                     = 0x55ad590e5000
brk(0x55ad590e3000)                     = 0x55ad590e3000
brk(0x55ad590e1000)                     = 0x55ad590e1000
brk(0x55ad590df000)                     = 0x55ad590df000
brk(0x55ad590dd000)                     = 0x55ad590dd000
brk(0x55ad590db000)                     = 0x55ad590db000
brk(0x55ad590d9000)                     = 0x55ad590d9000
brk(0x55ad590d7000)                     = 0x55ad590d7000
brk(0x55ad590d5000)                     = 0x55ad590d5000
brk(0x55ad590d3000)                     = 0x55ad590d3000
brk(0x55ad590d1000)                     = 0x55ad590d1000
brk(0x55ad590cf000)                     = 0x55ad590cf000
brk(0x55ad590cd000)                     = 0x55ad590cd000
brk(0x55ad590cb000)                     = 0x55ad590cb000
brk(0x55ad590c9000)                     = 0x55ad590c9000
brk(0x55ad590c7000)                     = 0x55ad590c7000
brk(0x55ad590c5000)                     = 0x55ad590c5000
brk(0x55ad590c3000)                     = 0x55ad590c3000
brk(0x55ad590c1000)                     = 0x55ad590c1000
brk(0x55ad590bf000)                     = 0x55ad590bf000
brk(0x55ad590bd000)                     = 0x55ad590bd000
brk(0x55ad590bb000)                     = 0x55ad590bb000
brk(0x55ad590b9000)                     = 0x55ad590b9000
brk(0x55ad590b7000)                     = 0x55ad590b7000
brk(0x55ad590b5000)                     = 0x55ad590b5000
brk(0x55ad590b3000)                     = 0x55ad590b3000
brk(0x55ad590b1000)                     = 0x55ad590b1000
brk(0x55ad590af000)                     = 0x55ad590af000
brk(0x55ad590ad000)                     = 0x55ad590ad000
brk(0x55ad590ab000)                     = 0x55ad590ab000
brk(0x55ad590a9000)                     = 0x55ad590a9000
brk(0x55ad590a7000)                     = 0x55ad590a7000
brk(0x55ad590a5000)                     = 0x55ad590a5000
brk(0x55ad590a3000)                     = 0x55ad590a3000
brk(0x55ad590a1000)                     = 0x55ad590a1000
brk(0x55ad5909f000)                     = 0x55ad5909f000
brk(0x55ad5909d000)                     = 0x55ad5909d000
brk(0x55ad5909b000)                     = 0x55ad5909b000
brk(0x55ad59099000)                     = 0x55ad59099000
brk(0x55ad59097000)                     = 0x55ad59097000
brk(0x55ad59095000)                     = 0x55ad59095000
brk(0x55ad59093000)                     = 0x55ad59093000
brk(0x55ad59091000)                     = 0x55ad59091000
brk(0x55ad5908f000)                     = 0x55ad5908f000
brk(0x55ad5908d000)                     = 0x55ad5908d000
brk(0x55ad5908b000)                     = 0x55ad5908b000
brk(0x55ad59089000)                     = 0x55ad59089000
brk(0x55ad59087000)                     = 0x55ad59087000
brk(0x55ad59085000)                     = 0x55ad59085000
brk(0x55ad59083000)                     = 0x55ad59083000
brk(0x55ad59081000)                     = 0x55ad59081000
brk(0x55ad5907f000)                     = 0x55ad5907f000
brk(0x55ad5907d000)                     = 0x55ad5907d000
brk(0x55ad5907b000)                     = 0x55ad5907b000
brk(0x55ad59079000)                     = 0x55ad59079000
brk(0x55ad59077000)                     = 0x55ad59077000
brk(0x55ad59075000)                     = 0x55ad59075000
brk(0x55ad59073000)                     = 0x55ad59073000
brk(0x55ad59071000)                     = 0x55ad59071000
brk(0x55ad5906f000)                     = 0x55ad5906f000
brk(0x55ad5906d000)                     = 0x55ad5906d000
brk(0x55ad5906b000)                     = 0x55ad5906b000
brk(0x55ad59069000)                     = 0x55ad59069000
brk(0x55ad59067000)                     = 0x55ad59067000
brk(0x55ad59065000)                     = 0x55ad59065000
brk(0x55ad59063000)                     = 0x55ad59063000
brk(0x55ad59061000)                     = 0x55ad59061000
brk(0x55ad5905f000)                     = 0x55ad5905f000
brk(0x55ad5905d000)                     = 0x55ad5905d000
brk(0x55ad5905b000)                     = 0x55ad5905b000
brk(0x55ad59059000)                     = 0x55ad59059000
brk(0x55ad59057000)                     = 0x55ad59057000
brk(0x55ad59055000)                     = 0x55ad59055000
brk(0x55ad59053000)                     = 0x55ad59053000
brk(0x55ad59051000)                     = 0x55ad59051000
brk(0x55ad5904f000)                     = 0x55ad5904f000
brk(0x55ad5904d000)                     = 0x55ad5904d000
brk(0x55ad5904b000)                     = 0x55ad5904b000
brk(0x55ad59040000)                     = 0x55ad59040000
ioctl(3, AMDKFD_IOC_GET_PROCESS_APERTURES_NEW, 0x7ffe340aafa0) = 0
ioctl(3, AMDKFD_IOC_ACQUIRE_VM, 0x7ffe340ab140) = 0
mmap(0x1000000, 68702699520, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_NORESERVE, -1, 0) = 0x1000000
ioctl(3, AMDKFD_IOC_SET_MEMORY_POLICY, 0x7ffe340ab120) = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 5
fstat(5, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(5, /* 26 entries */, 32768)  = 984
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_pass_pretrans", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x02\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/int_dte_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0f\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/int_dte_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x10\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pde_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x08\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pde_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x09\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/smi_recv", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x17\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_dte_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0a\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_dte_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0b\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/page_tbl_read_nst", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0d\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_trans_total", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x05\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/page_tbl_read_gst", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0e\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/vapic_int_non_guest", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x15\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/tlb_inv", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x13\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/vapic_int_guest", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x16\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/ign_rd_wr_mmio_1ff8h", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x14\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/smi_blk", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x18\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_pass_untrans", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x01\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/cmd_processed_inv", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x12\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pte_hit", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x06\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_target_abort", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x04\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/cmd_processed", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x11\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_iommu_tlb_pte_mis", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x07\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/page_tbl_read_tot", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x0c\n", 4096)         = 13
close(7)                                = 0
openat(AT_FDCWD, "/sys/bus/event_source/devices/amd_iommu_0/events/mem_pass_excl", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "csource=0x03\n", 4096)         = 13
close(7)                                = 0
getdents64(5, /* 0 entries */, 32768)   = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/perf/iommu/max_concurrent", O_RDONLY) = -1 ENOENT (No such file or directory)
close(5)                                = 0
statfs("/dev/shm/", {f_type=TMPFS_MAGIC, f_bsize=4096, f_blocks=2051634, f_bfree=2032838, f_bavail=2032838, f_files=2051634, f_ffree=2051499, f_fsid={val=[0, 0]}, f_namelen=255, f_frsize=4096, f_flags=ST_VALID|ST_NOSUID|ST_NODEV}) = 0
futex(0x7f9ff7cf20d0, FUTEX_WAKE_PRIVATE, 2147483647) = 0
openat(AT_FDCWD, "/dev/shm/sem.hsakmt_semaphore", O_RDWR|O_NOFOLLOW) = 5
fstat(5, {st_mode=S_IFREG|0664, st_size=32, ...}) = 0
mmap(NULL, 32, PROT_READ|PROT_WRITE, MAP_SHARED, 5, 0) = 0x7f9ff7ebc000
close(5)                                = 0
openat(AT_FDCWD, "/dev/shm/hsakmt_shared_mem", O_RDWR|O_CREAT|O_NOFOLLOW|O_CLOEXEC, 0666) = 5
ftruncate(5, 8)                         = 0
mmap(NULL, 8, PROT_READ|PROT_WRITE, MAP_SHARED, 5, 0) = 0x7f9ff7ebb000
ioctl(3, AMDKFD_IOC_GET_VERSION, 0x7ffe340ab210) = 0
openat(AT_FDCWD, "/proc/cpuinfo", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(7, "processor\t: 0\nvendor_id\t: Authen"..., 1024) = 1024
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/generation_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/system_properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "platform_oem 35498446626881\nplat"..., 4096) = 70
read(7, "", 4096)                       = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 8
fstat(8, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(8, /* 4 entries */, 32768)   = 96
getdents64(8, /* 0 entries */, 32768)   = 0
close(8)                                = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/system/cpu/online", O_RDONLY|O_CLOEXEC) = 7
read(7, "0-11\n", 8192)                 = 5
close(7)                                = 0
sched_getaffinity(0, 128, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) = 40
sched_setaffinity(0, 128, [0])          = 0
sched_setaffinity(0, 128, [1])          = 0
sched_setaffinity(0, 128, [2])          = 0
sched_setaffinity(0, 128, [3])          = 0
sched_setaffinity(0, 128, [4])          = 0
sched_setaffinity(0, 128, [5])          = 0
sched_setaffinity(0, 128, [6])          = 0
sched_setaffinity(0, 128, [7])          = 0
sched_setaffinity(0, 128, [8])          = 0
sched_setaffinity(0, 128, [9])          = 0
sched_setaffinity(0, 128, [10])         = 0
sched_setaffinity(0, 128, [11])         = 0
sched_setaffinity(0, 128, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) = 0
access("/sys/bus/pci", R_OK)            = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/gpu_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "0\n", 4096)                    = 2
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "cpu_cores_count 12\nsimd_count 0\n"..., 4096) = 371
read(7, "", 4096)                       = 0
openat(AT_FDCWD, "/proc/cpuinfo", O_RDONLY) = 8
fstat(8, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(8, "processor\t: 0\nvendor_id\t: Authen"..., 1024) = 1024
read(8, " decodeassists pausefilter pfthr"..., 1024) = 1024
read(8, "y svm extapic cr8_legacy abm sse"..., 1024) = 1024
read(8, "\ncpuid level\t: 13\nwp\t\t: yes\nflag"..., 1024) = 1024
read(8, "gement: ts ttp tm hwpstate eff_f"..., 1024) = 1024
read(8, "vm_lock nrip_save tsc_scale vmcb"..., 1024) = 1024
read(8, "popcnt aes xsave avx f16c rdrand"..., 1024) = 1024
read(8, "\ninitial apicid\t: 5\nfpu\t\t: yes\nf"..., 1024) = 1024
read(8, "zes\t: 43 bits physical, 48 bits "..., 1024) = 1024
read(8, "v1 xsaves clzero irperf xsaveerp"..., 1024) = 1024
read(8, "mulqdq monitor ssse3 fma cx16 ss"..., 1024) = 1024
read(8, "blings\t: 12\ncore id\t\t: 5\ncpu cor"..., 1024) = 1024
read(8, "es\nclflush size\t: 64\ncache_align"..., 1024) = 1024
read(8, "dseed adx smap clflushopt sha_ni"..., 1024) = 1024
read(8, "ood nopl nonstop_tsc cpuid extd_"..., 1024) = 1024
read(8, "cpu MHz\t\t: 1812.508\ncache size\t:"..., 1024) = 1024
read(8, "pec_store_bypass\nbogomips\t: 8387"..., 1024) = 210
read(8, "", 1024)                       = 0
close(8)                                = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/mem_banks/0/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "heap_type 0\nsize_in_bytes 168069"..., 4096) = 72
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/0/io_links/0/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "type 2\nversion_major 0\nversion_m"..., 4096) = 167
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/gpu_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "11656\n", 4096)                = 6
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "cpu_cores_count 0\nsimd_count 176"..., 4096) = 475
read(7, "", 4096)                       = 0
openat(AT_FDCWD, "/usr/share/hwdata/pci.ids", O_RDONLY) = 8
fstat(8, {st_mode=S_IFREG|0644, st_size=1134006, ...}) = 0
read(8, "#\n#\tList of PCI ID's\n#\n#\tVersion"..., 4096) = 4096
read(8, "ard - Lights-Out\n\t007c  NC7770 1"..., 4096) = 4096
read(8, "Channel SCSI Controller\n\t\t1000 1"..., 4096) = 4096
brk(0x55ad59061000)                     = 0x55ad59061000
read(8, "00 9351  MegaRAID SAS 9341-24i\n\t"..., 4096) = 4096
read(8, "08E\n\t\t1000 1010  MegaRAID SATA 3"..., 4096) = 4096
read(8, " Lite)\n\t\t8086 9267  RAID Control"..., 4096) = 4096
read(8, "-0X RAID Controller\n\t\t1000 0531 "..., 4096) = 4096
read(8, "0f  Kaveri [Radeon R7 Graphics]\n"..., 4096) = 4096
read(8, "Pavilion t3030.de Desktop PC\n\t\t1"..., 4096) = 4096
read(8, "\t\t1462 7368  K9AG Neo2\n\t\t17f2 50"..., 4096) = 4096
read(8, "ard\n\t\t8086 3411  SDS2 Mainboard\n"..., 4096) = 4096
read(8, " TX]\n\t4e47  R300 GL [FireGL X1]\n"..., 4096) = 4096
read(8, "2023  RV100 QY [Radeon 7000 Evil"..., 4096) = 4096
read(8, "\n\t5952  RD580 Host Bridge\n\t5954 "..., 4096) = 4096
read(8, "Radeon X300/X550/X1050 Series]\n\t"..., 4096) = 4096
read(8, "Radeon R9 360 OEM\n\t\t1682 0907  R"..., 4096) = 4096
read(8, " 6650M\n\t\t1025 059a  Radeon HD 66"..., 4096) = 4096
read(8, "\n\t\t174b e181  Radeon HD 6570\n\t\t1"..., 4096) = 4096
read(8, "Radeon HD 7470M\n\t\t1179 fb41  Rad"..., 4096) = 4096
read(8, "70 Platinum]\n\t\t1043 3001  Tahiti"..., 4096) = 4096
read(8, "B\n\t\t1da2 e366  Nitro+ Radeon RX "..., 4096) = 4096
read(8, "\n\t\t1787 3000  Radeon HD 6570\n\t68"..., 4096) = 4096
read(8, " 6550M]\n\t\t103c 163c  Pavilion dv"..., 4096) = 4096
read(8, "5 0379  Mobility Radeon HD 5650\n"..., 4096) = 4096
read(8, " 5570\n\t\t174b 3000  Radeon HD 651"..., 4096) = 4096
read(8, "deon HD 6330M\n\t\t1179 fdd2  Radeo"..., 4096) = 4096
read(8, "a XT / Amethyst XT [Radeon R9 38"..., 4096) = 4096
brk(0x55ad59083000)                     = 0x55ad59083000
read(8, " FireGL V5200]\n\t\t17aa 2007  Thin"..., 4096) = 4096
read(8, "Radeon HD 4850 512MB GDDR3\n\t9443"..., 4096) = 4096
read(8, " [Mobility Radeon HD 2600]\n\t9583"..., 4096) = 4096
read(8, "adeon R5 Graphics\n\t\t103c 8238  R"..., 4096) = 4096
read(8, "534 [Eagle]\n\t0103  82C538\n\t0104 "..., 4096) = 4096
read(8, "PCI) [A5506B]\n\t\t108d 0016  Rapid"..., 4096) = 4096
read(8, "Alta Lite]\n\t0007  Processor to I"..., 4096) = 4096
read(8, "Adapter (575C)\n\t0302  Winnipeg P"..., 4096) = 4096
read(8, "aRAID 428 Ultra RAID Controller\n"..., 4096) = 4096
read(8, "Mini\n\t1512  Family 14h Processor"..., 4096) = 4096
read(8, " AMD-751 [Irongate] System Contr"..., 4096) = 4096
read(8, " i1 AGP\n\t\t1023 8520  CyberBlade "..., 4096) = 4096
read(8, "ller 4e/Di\n\t\t1028 0170  PowerEdg"..., 4096) = 4096
read(8, "ad 16Mb\n\t\t102b 2179  Millennium "..., 4096) = 4096
read(8, "50 PCIe 64MB\n\t\t102b 0947  Parhel"..., 4096) = 4096
read(8, " SCC USB 2.0 EHCI controller\n\t01"..., 4096) = 4096
read(8, "AGP VGA Display Adapter\n\t0330  3"..., 4096) = 4096
read(8, "lerator\n\t\t1019 7018  SiS PCI Aud"..., 4096) = 4096
read(8, "art Array 712m (Mezzanine RAID c"..., 4096) = 4096
read(8, "0 [FireStar]\n\tc701  82C701 [Fire"..., 4096) = 4096
read(8, "ast DV2000 FireWire Controller\n\t"..., 4096) = 4096
read(8, "Found in Philips ADSL ANNEX A WL"..., 4096) = 4096
read(8, "Family)\n\t909f  Aeolia SATA AHCI "..., 4096) = 4096
brk(0x55ad590a5000)                     = 0x55ad590a5000
read(8, " Processor\n\t\tecc0 0050  Gina24 r"..., 4096) = 4096
read(8, "309  Imagine 128\n\t2339  Imagine "..., 4096) = 4096
read(8, "\t0021  UniNorth GMAC (Sun GEM)\n\t"..., 4096) = 4096
read(8, "apter\n\t165c  FastLinQ QL45000 Se"..., 4096) = 4096
read(8, "PCI-X HBA\n\t6322  SP212-based 2Gb"..., 4096) = 4096
read(8, "HMCU CNA\n\t\t1077 0007  QLogic 2x1"..., 4096) = 4096
read(8, "312  Intel 21554 PCI-PCI bus bri"..., 4096) = 4096
read(8, " 2)\n\t7031  PCI-CAN/2 (Series 2)\n"..., 4096) = 4096
read(8, "ing Module\n\t71bb  PXI-2584\n\t71bc"..., 4096) = 4096
read(8, "8360LT\n\t761f  PXI-2540\n\t7620  PX"..., 4096) = 4096
read(8, "365\n\t\t1093 77a8  PXIe-6375\n\t\t109"..., 4096) = 4096
read(8, "\t144f 3000  MagicTView CPH060 - "..., 4096) = 4096
read(8, "n)\n\t\t1822 0001  VisionPlus DVB C"..., 4096) = 4096
read(8, "card\n\t2540  IXXAT CAN-Interface "..., 4096) = 4096
read(8, "ane, 5-Port PCI Express Gen 3 (8"..., 4096) = 4096
read(8, " 0013  PIKA PrimeNet MM cPCI 8 ("..., 4096) = 4096
read(8, "gabit LOM Ethernet Adapter\n\t\t147"..., 4096) = 4096
read(8, "ast Ethernet Controller\n\t9210  3"..., 4096) = 4096
read(8, "book\n\t\t104d 810f  VAIO PCG-U1 US"..., 4096) = 4096
read(8, "cb  Omron Corporation\n# nee Ment"..., 4096) = 4096
read(8, "\t\t1048 0c3a  Erazor III LT\n\t\t104"..., 4096) = 4096
brk(0x55ad590c7000)                     = 0x55ad590c7000
read(8, "e  ECS Elitegroup NFORCE3-A939 m"..., 4096) = 4096
read(8, "ny)\n\t00e8  nForce3 EHCI USB 2.0 "..., 4096) = 4096
read(8, " Go 6400]\n\t0169  NV44 [GeForce 6"..., 4096) = 4096
read(8, "3842 a341  256A8N341DX\n\t0222  NV"..., 4096) = 4096
read(8, "ce 7900 GS]\n\t0293  G71 [GeForce "..., 4096) = 4096
read(8, "00]\n\t0343  NV36 [GeForce FX 5700"..., 4096) = 4096
read(8, "25 0392  ET1350\n\t\t1028 020e  Ins"..., 4096) = 4096
read(8, "ce 630a]\n\t0541  MCP67 Memory Con"..., 4096) = 4096
read(8, "92GLM [Quadro FX 3800M]\n\t0620  G"..., 4096) = 4096
read(8, "sor\n\t0754  MCP78S [GeForce 8200]"..., 4096) = 4096
read(8, "150-HD\n\t07da  MCP73 Co-processor"..., 4096) = 4096
read(8, "ce 315M\n\t\t1179 fcf2  GeForce 315"..., 4096) = 4096
read(8, "T215 [GeForce GT 330]\n\t0ca2  GT2"..., 4096) = 4096
read(8, "5M]\n\t0fce  GK107M [GeForce GT 64"..., 4096) = 4096
read(8, "5M]\n\t\t103c 2afb  GeForce 705A\n\t\t"..., 4096) = 4096
read(8, "8 06c0  GeForce 820M\n\t\t1028 06c1"..., 4096) = 4096
read(8, "\t\t17aa 361c  GeForce 820A\n\t\t17aa"..., 4096) = 4096
read(8, "[GeForce GTX 650 Ti Boost]\n\t\t104"..., 4096) = 4096
read(8, " GM107 [GeForce GTX 745]\n\t1389  "..., 4096) = 4096
read(8, "Force GTX 1070 Mobile]\n\t1c00  GP"..., 4096) = 4096
read(8, " e311  Lancer Gen6: LPe31000 Fib"..., 4096) = 4096
read(8, "  S5933_HEPC3\n\t80b9  Harmonix Hi"..., 4096) = 4096
brk(0x55ad590e9000)                     = 0x55ad590e9000
read(8, "5 2300  P4TSV Onboard LAN (RTL81"..., 4096) = 4096
read(8, "\n\t0410  Wildcard TE410P (2nd Gen"..., 4096) = 4096
read(8, "0350 Audigy 2 ZS\n\t\t1102 2003  SB"..., 4096) = 4096
read(8, "# SFF-8087 Mini-SAS 16 port inte"..., 4096) = 4096
read(8, "01  Magnia Z310\n\t\t147b a702  KG7"..., 4096) = 4096
read(8, "ax integrated digital audio\n\t\t10"..., 4096) = 4096
read(8, "ost Bridge\n\t\t1297 f641  FX41 mot"..., 4096) = 4096
read(8, "\t4269  KT880 Host Bridge\n\t4282  "..., 4096) = 4096
read(8, " PCI Bridge\n\tb188  VT8237/8251 P"..., 4096) = 4096
read(8, "t76c506 802.11b Wireless Network"..., 4096) = 4096
read(8, "NT3 PCI Express Internal NTB\n\t80"..., 4096) = 4096
read(8, "\n\t\t1131 2001  Proteus Pro [phili"..., 4096) = 4096
read(8, "hnotrend/Hauppauge DVB card rev2"..., 4096) = 4096
read(8, "Cornet NQ\n\t\t1133 1c08  Diva Serv"..., 4096) = 4096
read(8, "space NIC\n\t\t1137 00ce  VIC 1225T"..., 4096) = 4096
read(8, "  SK-9821 V2.0 Gigabit Ethernet "..., 4096) = 4096
read(8, "Adapter\n\t\t115d 0182  Cardbus Eth"..., 4096) = 4096
read(8, "Advanced Computing\n# nee Polaris"..., 4096) = 4096
read(8, "\n\t\t1028 014f  Latitude X300 lapt"..., 4096) = 4096
read(8, " (x1) Gigabit Ethernet Adapter\n\t"..., 4096) = 4096
read(8, " v2 802.11n N1 Wireless Notebook"..., 4096) = 4096
read(8, "GE)\n\t\t1854 0018  Marvell 88E8036"..., 4096) = 4096
read(8, "3 Gigabit Ethernet Controller (A"..., 4096) = 4096
brk(0x55ad5910b000)                     = 0x55ad5910b000
read(8, "nModem\n\t\t1033 8015  LT WinModem "..., 4096) = 4096
read(8, "f\n\t\t1043 8294  LSI FW322/323 IEE"..., 4096) = 4096
read(8, "ibre Channel Adapter\n\t\t117c 003b"..., 4096) = 4096
read(8, "43  SK-9843 SX\n\t\t1202 9844  SK-9"..., 4096) = 4096
read(8, "37  Voodoo3 AGP\n\t\t121a 0038  Voo"..., 4096) = 4096
read(8, " or cPCI-200 Quad IndustryPack c"..., 4096) = 4096
read(8, "35  SMC2835W V2 Wireless Cardbus"..., 4096) = 4096
read(8, "\t\t270f 2200  ES1371, ES1373 Audi"..., 4096) = 4096
read(8, "kerphone Modem\n\t1032  HCF 56k Mo"..., 4096) = 4096
read(8, "9  Xiotech Corporation\n12aa  SDL"..., 4096) = 4096
read(8, "/SC-BUS, T1/PRI adaptor.\n\t0685  "..., 4096) = 4096
read(8, "udio Processor\n\t8803  Vortex 56k"..., 4096) = 4096
read(8, "2000  CyberSerial (1-port) 16550"..., 4096) = 4096
read(8, "\t0207  GLN180PEX GPS/GLONASS rec"..., 4096) = 4096
read(8, " Express Module Bypass Server Ad"..., 4096) = 4096
read(8, "[BeroNet BN4S0]\n\t\t1397 b566  HFC"..., 4096) = 4096
read(8, "cLink GT4 Adapter\n\t00a0  SyncLin"..., 4096) = 4096
read(8, "ce STX)\n\t\t1043 835d  Virtuoso 10"..., 4096) = 4096
read(8, "08  Aloka Co. Ltd\n1409  Timedia "..., 4096) = 4096
read(8, "NetGlobal 56k+10/100Mb CardBus ("..., 4096) = 4096
read(8, "85  T420-4085 SFP+ Unified Wire "..., 4096) = 4096
read(8, "ernet Controller\n\t5004  T520-BCH"..., 4096) = 4096
brk(0x55ad5912d000)                     = 0x55ad5912d000
read(8, "410  T580-LP-CR Unified Wire Eth"..., 4096) = 4096
read(8, "ge Controller\n\t5581  T540-5081 U"..., 4096) = 4096
read(8, "e Storage Controller\n\t5695  T540"..., 4096) = 4096
read(8, "nified Wire Ethernet Controller "..., 4096) = 4096
read(8, "087  T6225-6087 Unified Wire Eth"..., 4096) = 4096
read(8, "t Controller [VF]\n\t6809  T6210-B"..., 4096) = 4096
read(8, " 1ff6  Express Flash PM1725b 12."..., 4096) = 4096
read(8, " Ltd\n14b1  Nextcom K.K.\n14b2  EN"..., 4096) = 4096
read(8, "4e3  AMTELCO\n14e4  Broadcom Inc."..., 4096) = 4096
read(8, " 8008  BCM5701 1000Base-T\n\t1646 "..., 4096) = 4096
read(8, "er Adapter\n\t\t103c 7052  NC105T P"..., 4096) = 4096
read(8, "57760 Gigabit Ethernet PCIe\n\t169"..., 4096) = 4096
read(8, " Function\n\t\t103c 1916  FlexFabri"..., 4096) = 4096
read(8, "et Controller\n\t16e1  NetXtreme-C"..., 4096) = 4096
read(8, ".11b/g WLAN\n\t\t103c 1356  Broadco"..., 4096) = 4096
read(8, " AirPort Extreme\n\t\t106b 00e4  Ai"..., 4096) = 4096
read(8, "erator\n\t5850  BCM5850 Crypto Acc"..., 4096) = 4096
read(8, "Adapter\n\t1803  HCF 56k Modem\n\t\t0"..., 4096) = 4096
read(8, "613  Leadtek Winfast 2000XP Expe"..., 4096) = 4096
read(8, "  AG COMMUNICATIONS\n14fa  WANDEL"..., 4096) = 4096
read(8, "Reader Controller\n\t0730  ENE PCI"..., 4096) = 4096
read(8, " Security Ltd\n1576  Viewcast COM"..., 4096) = 4096
read(8, "onnectX-3 IB FDR Dual Port Mezza"..., 4096) = 4096
read(8, " 10Gb/s InfiniBand / 10GigE Adap"..., 4096) = 4096
brk(0x55ad5914f000)                     = 0x55ad5914f000
read(8, " Checker\n\t2928  64 Bit, 66MHz PC"..., 4096) = 4096
read(8, "000 Frame Synchronizer and I/O\n\t"..., 4096) = 4096
read(8, "[Intersil ISL3874]\n167e  ONNTO C"..., 4096) = 4096
read(8, "MP55AG v1.2 802.11abg PCI Adapte"..., 4096) = 4096
read(8, "R5416 Wireless Network Adapter ["..., 4096) = 4096
read(8, "2.11b/g/n mini-PCIe card on a se"..., 4096) = 4096
read(8, "DX501 Reconfigurable Digital I/O"..., 4096) = 4096
read(8, "Module\n\t7029  AP342 14-bit, 12-C"..., 4096) = 4096
read(8, " [LiquidIO II] 2-port 25GbE Inte"..., 4096) = 4096
read(8, "ller\n# port 6 of 8\n\t6815  TW6816"..., 4096) = 4096
read(8, "5 4-Port PCIe 3.0 to SAS/SATA 6G"..., 4096) = 4096
read(8, "lite Design [DNPCIe_80G_A10_LL]\n"..., 4096) = 4096
read(8, "ess PCI Adapter\n\t0681  RT2890 Wi"..., 4096) = 4096
read(8, "T\n\tdb30  FusionHDTV DVB-T Pro\n\td"..., 4096) = 4096
read(8, "232/4-PCI-335 Serial PCI Adapter"..., 4096) = 4096
read(8, " Mezzanine Adapter\n\t\t1924 6521  "..., 4096) = 4096
read(8, "450b\n\t1113  FireSpy450bT\n\t1114  "..., 4096) = 4096
read(8, "363 SATA/IDE Controller\n\t\t1043 8"..., 4096) = 4096
read(8, "BMA Virtual Network Adapter\n\t171"..., 4096) = 4096
read(8, "84  Commex Technologies\n\t0001  V"..., 4096) = 4096
read(8, "cker Ethernet switch device\n\t000"..., 4096) = 4096
read(8, "orage\n\t\t1bb1 0101  Nytro XF1440\n"..., 4096) = 4096
read(8, "Electronics Co., Ltd.\n\t0010  Pro"..., 4096) = 4096
brk(0x55ad59171000)                     = 0x55ad59171000
read(8, "32B DPDK Data Mover]\n\t\t1d6c 2001"..., 4096) = 4096
read(8, "et SFP+ PCI Express Adapter\n\t\t1f"..., 4096) = 4096
read(8, "a II 2D+3D\n\t07a1  Wildcat III 62"..., 4096) = 4096
read(8, "uner)\n\t\t1461 c03f  C115 PCI vide"..., 4096) = 4096
read(8, "-COM-2SRJ 2x RS422/RS484 Card w/"..., 4096) = 4096
read(8, " (PC104+)\n\t\t4c53 3001  PLUSTEST "..., 4096) = 4096
read(8, "1092 4207  Stealth III S540\n\t\t10"..., 4096) = 4096
read(8, " Module\n\t1600  CooVOX TDM E1/T1 "..., 4096) = 4096
read(8, "cessor Family DRAM Controller\n\t\t"..., 4096) = 4096
read(8, "ess-to-PCI Bridge A\n\t032a  6700P"..., 4096) = 4096
read(8, "\n\t0819  Medfield Serial IO I2C C"..., 4096) = 4096
read(8, "reless-AC 7260\n# Wilkins Peak 2\n"..., 4096) = 4096
read(8, "00 HS-UART\n\t0937  Quark SoC X100"..., 4096) = 4096
read(8, " NVMe 8.0TB 2.5\" U.2 (P4510)\n\t\t1"..., 4096) = 4096
read(8, "3 v4/Xeon D QuickData Technology"..., 4096) = 4096
read(8, " i7 QPI Link 2\n\t0e3e  Xeon E7 v2"..., 4096) = 4096
read(8, "E5 v2/Core i7 Broadcast Register"..., 4096) = 4096
read(8, "Series LPIO2 I2C Controller #6\n\t"..., 4096) = 4096
read(8, "MT Desktop Connection\n\t\t8086 101"..., 4096) = 4096
read(8, "E mainboard\n\t1051  82801EB/ER (I"..., 4096) = 4096
read(8, "PRO/1000 PF Server Adapter\n\t107f"..., 4096) = 4096
read(8, "dapter\n\t\t1014 0380  10-Gigabit X"..., 4096) = 4096
read(8, " 560FLB Adapter\n\t\t1059 0111  T40"..., 4096) = 4096
read(8, "t NIC (embedded)\n\t\t0e11 b0d7  NC"..., 4096) = 4096
brk(0x55ad59193000)                     = 0x55ad59193000
read(8, "Port Server Adapter\n\t\t8086 1030 "..., 4096) = 4096
read(8, "17aa 21ce  ThinkPad T520\n\t\t8086 "..., 4096) = 4096
read(8, "\t8086 1f52  1GbE 4P I350 Mezz\n\t1"..., 4096) = 4096
read(8, "-port 562T Adapter\n\t\t1590 00d2  "..., 4096) = 4096
read(8, "0  Ethernet Converged Network Ad"..., 4096) = 4096
read(8, "40-MTP2\n\t15d1  Ethernet Controll"..., 4096) = 4096
read(8, " Gaussian Mixture Model\n\t\t17aa 2"..., 4096) = 4096
read(8, " Mobile SATA Controller (IDE mod"..., 4096) = 4096
read(8, "et Family MEI Controller #2\n\t1c3"..., 4096) = 4096
read(8, "4-Port SATA/SAS Storage Control "..., 4096) = 4096
read(8, "ntroller\n\t\t1043 108d  VivoBook X"..., 4096) = 4096
read(8, "oot Port 3\n\t1f13  Atom processor"..., 4096) = 4096
read(8, "000/J3xxx/N3xxx Series Trusted E"..., 4096) = 4096
read(8, "IDE Controller\n\t2422  82801AB US"..., 4096) = 4096
read(8, "16  Travelmate 612TX\n\t\t104d 80df"..., 4096) = 4096
read(8, " Amilo M1420\n\t\t4c53 1090  Cx9 / "..., 4096) = 4096
read(8, "atitude X300\n\t\t1028 0163  Latitu"..., 4096) = 4096
read(8, " Precision 470\n\t\t1028 016c  Powe"..., 4096) = 4096
read(8, " GA-8IPE1000 Pro2 motherboard (8"..., 4096) = 4096
read(8, "G/GL[Brookdale-G]/GE Chipset Int"..., 4096) = 4096
read(8, "oard Computer\n\t\t1775 1100  CR11/"..., 4096) = 4096
read(8, "028 0170  PowerEdge 6850 DDR Ini"..., 4096) = 4096
read(8, "herboard\n\t\t103c 2a09  PufferM-UL"..., 4096) = 4096
brk(0x55ad591b4000)                     = 0x55ad591b4000
read(8, "\t\t8086 3476  S5000PSLSATA Server"..., 4096) = 4096
read(8, "rEdge SC440\n\t\t1028 01e6  PowerEd"..., 4096) = 4096
read(8, " EHCI Controller\n\t\t1025 006c  98"..., 4096) = 4096
read(8, "rEdge SC440\n\t\t1028 01e6  PowerEd"..., 4096) = 4096
read(8, "0b\n\t\t103c 30c1  Compaq 6910p\n\t\t1"..., 4096) = 4096
read(8, "d T61/R61\n\t\t17c0 4088  Medion WI"..., 4096) = 4096
read(8, "d  CCM-BOOGIE\n\t2935  82801I (ICH"..., 4096) = 4096
read(8, "werEdge T610 USB EHCI Controller"..., 4096) = 4096
read(8, "otherboard: Intel 82P35 Northbri"..., 4096) = 4096
read(8, "ily System Configuration Control"..., 4096) = 4096
read(8, "rated Memory Controller Channel "..., 4096) = 4096
read(8, "00 Integrated Memory Controller "..., 4096) = 4096
read(8, "a Processor Interrupt Controller"..., 4096) = 4096
read(8, "e Agent 1\n\t2f39  Xeon E7 v3/Xeon"..., 4096) = 4096
read(8, " E5 v3/Core i7 DDRIO (VMSE) 2 & "..., 4096) = 4096
read(8, "rocessor to AGP Controller\n\t\t144"..., 4096) = 4096
read(8, "ess Downstream Port E1\n\t\t103c 31"..., 4096) = 4096
read(8, "ry I/O Controller Hub\n\t35b1  310"..., 4096) = 4096
read(8, "O (ICH10 Family) 4-port SATA IDE"..., 4096) = 4096
read(8, "1JI (ICH10 Family) PCI Express R"..., 4096) = 4096
read(8, " Series/3400 Series Chipset 4 po"..., 4096) = 4096
read(8, "0 Series Chipset High Definition"..., 4096) = 4096
read(8, " E5/Core i7 Unicast Register 4\n\t"..., 4096) = 4096
read(8, "o Advanced-N 6200 2x2 AGN\n\t\t8086"..., 4096) = 4096
brk(0x55ad591d6000)                     = 0x55ad591d6000
read(8, " Core Processor PCIe Controller "..., 4096) = 4096
read(8, "annel 1 Registers\n\t65f7  5100 Ch"..., 4096) = 4096
read(8, " DMA Channel 2\n\t6f53  Xeon Proce"..., 4096) = 4096
read(8, "face\n\t6fbe  Xeon E7 v4/Xeon E5 v"..., 4096) = 4096
read(8, "371AB/EB/MB PIIX4 ACPI\n\t\t15ad 19"..., 4096) = 4096
read(8, "KX/GX Memory controller\n\t84ca  4"..., 4096) = 4096
read(8, "Series/C220 Series Chipset Famil"..., 4096) = 4096
read(8, "ries Chipset Family PCI Express "..., 4096) = 4096
read(8, " MS SMBus 1\n\t8d7f  C610/X99 seri"..., 4096) = 4096
read(8, "\n\t9ce0  Wildcat Point-LP Serial "..., 4096) = 4096
read(8, "Series/C230 Series Chipset Famil"..., 4096) = 4096
read(8, "mily Serial IO I2C Controller #3"..., 4096) = 4096
read(8, "s Root Port #12\n\ta29c  200 Serie"..., 4096) = 4096
read(8, "MI\n\t\t1028 02da  OptiPlex 980\n\t\t1"..., 4096) = 4096
read(8, "/AUW/AUWD AIC-7895B\n\t7896  AIC-7"..., 4096) = 4096
read(8, "9005 02bb  3405\n\t\t9005 02bc  380"..., 4096) = 4096
read(8, "-8i\n\t\t9005 0901  SmartHBA 2100-4"..., 4096) = 4096
read(8, "ort Adapter)\n\t9865  PCI 9865 Mul"..., 4096) = 4096
read(8, "410P quad-span T1/E1/J1 card 3.3"..., 4096) = 4096
read(8, "12\n\t351c  DAG 3.5ECM Fast Ethern"..., 4096) = 4096
read(8, "ller\n\t01  Token ring network con"..., 4096) = 3510
read(8, "", 4096)                       = 0
close(8)                                = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/mem_banks/0/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "heap_type 2\nsize_in_bytes 429496"..., 4096) = 72
read(7, "", 4096)                       = 0
close(7)                                = 0
brk(0x55ad5920a000)                     = 0x55ad5920a000
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/0/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487744\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/1/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487745\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/2/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487746\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/3/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487747\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/4/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487748\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/5/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487749\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/6/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487750\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/7/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487751\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/8/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487752\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/9/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487753\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/10/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487754\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/11/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487755\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/12/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487756\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/13/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487757\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/14/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487758\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/15/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487759\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/16/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487760\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/17/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487761\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/18/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487762\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/19/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487763\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/20/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487764\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/21/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487765\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/22/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487766\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/23/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487767\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/24/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487768\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/25/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487769\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/26/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487770\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/27/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487771\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/28/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487772\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/29/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487773\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/30/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487774\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/31/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487775\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/32/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487776\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/33/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487777\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/34/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487778\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/35/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487779\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/36/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487780\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/37/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487781\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/38/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487782\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/39/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487783\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/40/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487784\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/41/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487785\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/42/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487786\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/43/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487787\nleve"..., 4096) = 639
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/44/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487744\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/45/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487746\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/46/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487748\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/47/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487750\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/48/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487752\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/49/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487754\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/50/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487756\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/51/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487758\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/52/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487760\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/53/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487762\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/54/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487764\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/55/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487766\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/56/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487768\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/57/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487770\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/58/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487772\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/59/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487774\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/60/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487776\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/61/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487778\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/62/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487780\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/63/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487782\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/64/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487784\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/65/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487786\nleve"..., 4096) = 640
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/66/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487744\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/67/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487746\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/68/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487748\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/69/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487750\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/70/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487752\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/71/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487754\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/72/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487756\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/73/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487758\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/74/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487760\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/75/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487762\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/76/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487764\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/77/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487766\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/78/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487768\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/79/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487770\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/80/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487772\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/81/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487774\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/82/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487776\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/83/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487778\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/84/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487780\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/85/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487782\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/86/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487784\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/caches/87/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "processor_id_low 2147487786\nleve"..., 4096) = 638
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/nodes/1/io_links/0/properties", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "type 2\nversion_major 0\nversion_m"..., 4096) = 168
read(7, "", 4096)                       = 0
close(7)                                = 0
openat(AT_FDCWD, "/sys/devices/virtual/kfd/kfd/topology/generation_id", O_RDONLY) = 7
fstat(7, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(7, "2\n", 4096)                    = 2
close(7)                                = 0
ioctl(3, AMDKFD_IOC_GET_CLOCK_COUNTERS, 0x7ffe340aaeb0) = 0
--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x55ad000000e8} ---
+++ killed by SIGSEGV (core dumped) +++
```

Do the binaries need to be built against the latest kernel every time? I'm going to rebuild and see if I can get it working again.