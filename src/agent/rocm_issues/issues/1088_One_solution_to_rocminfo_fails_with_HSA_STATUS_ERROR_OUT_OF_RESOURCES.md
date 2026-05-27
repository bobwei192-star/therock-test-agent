# One solution to rocminfo fails with HSA_STATUS_ERROR_OUT_OF_RESOURCES

> **Issue #1088**
> **状态**: closed
> **创建时间**: 2020-04-23T19:09:47Z
> **更新时间**: 2020-10-22T03:44:50Z
> **关闭时间**: 2020-05-17T09:00:36Z
> **作者**: emerth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1088

## 描述

This is a demonstration of a way to debug a certain class of HSA_STATUS_ERROR_OUT_OF_RESOURCES error encountered when running some rocm tools.

My system is a fresh Ubuntu 18.04.4 LTS install with Ubuntu's upstream kernel "Linux 5.3.0-050300-generic #201909152230 SMP Sun Sep 15 22:32:54 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux" installed. Then rocm 3.3.0 installed via apt-get install rocm-dev. Then rocminfo only works for root but not regular user. As a regular user rocminfo reports the dreaded HSA_STATUS_ERROR_OUT_OF_RESOURCES message and fails.


Lots of issues posted about this already, most of them not very useful, no solution, or you know, "Reinstall everything". I thought that went out with Macintosh "reinstall your system folder". A couple pointed to files in /dev/dri/ having unexpected ownership or very restrictive rights. None of these were the case for me.

If you can run rocminfo successfully as root or via su, but it fails as a regular user then you need to consider that root can read & write every file on the system, but regular users cannot. Possibly there is a file that rocminfo wants to use but is being denied access to. But how to find the file?

There is a Linux program called strace that is very helpful with this question. It will tell you what files a process is accessing, and can identify files where there are permission errors.


So, one way to approach the problem:

Run rocminfo as a regular user thus:

```
emerth@radeon-2:~$ /opt/rocm/bin/rocminfo
```


See the dreaded error message:

```
ROCk module is loaded
emerth is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

Now, run it thus instead:

`emerth@radeon-2:~$ strace /opt/rocm/bin/rocminfo`

See all the stuff strace prints with this gem at the end of the output:

```
...
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 EACCES (Permission denied)
write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
) = 101
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -283, SEEK_CUR)                = -1 ESPIPE (Illegal seek)
exit_group(4104)                        = ?
+++ exited with 8 +++
```


Look at the line starting with openat(...)! It is telling you that rocminfo attempted to open the file /dev/kfd but was denied permission! It might be the case that rocminfo was trying to use some other file: but in that case you would see a message mentioning that other file not this one. You get the idea, right?

Look at the /dev/kfd file:

```
emerth@radeon-2:~$ ls -lF /dev/kfd
crw------- 1 root root 239, 0 Apr 23 18:23 /dev/kfd
```

You do not have read/write access to it.

Give yourself access:
```
emerth@radeon-2:~$ sudo chmod 666 /dev/kfd
```


Run rocminfo again:

```
emerth@radeon-2:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
emerth is member of video group
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 5 1600X Six-Core Processor
  Marketing Name:          AMD Ryzen 5 1600X Six-Core Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   3600
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            12
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65862000(0x3ecf970) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65862000(0x3ecf970) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        TRUE
  ISA Info:
    N/A
*******
Agent 2
*******
  Name:                    gfx906
  Marketing Name:          Vega 20
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 26287(0x66af)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1802
  BDFID:                   2304
  Internal Node ID:        1
  Compute Unit:            60
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    2560(0xa00)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16760832(0xffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx906
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    gfx906
  Marketing Name:          Vega 20
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          4096(0x1000)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
  Chip ID:                 26287(0x66af)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   1802
  BDFID:                   3072
  Internal Node ID:        2
  Compute Unit:            60
  SIMDs per CU:            4
  Shader Engines:          4
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      FALSE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        40(0x28)
  Max Work-item Per CU:    2560(0xa00)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    16760832(0xffc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Acessible by all:        FALSE
    Pool 2
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Acessible by all:        FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx906
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
emerth@radeon-2:~$

```

Bob's yer uncle! You have successfully used a Linux debugging tool to find out why rocminfo was failing when run as a normal user. 

Leaving /dev/kfd world readable/writable may or may not be safe. Perhaps the KFD devs could weigh in on this?

---

## 评论 (11 条)

### 评论 #1 — ableeker (2020-04-27T11:13:53Z)

Nice! This show why strace is useful indeed. We've used strace to find out why clinfo segfaulted. It showed that it's caused because it couldn't find libncurses5. Go figure... Anyway, I'm no expert, but I think you're right about the permission issue.

However, isn't the udev rule supposed to fix that in a safer way? In the installation guide it says in the section about Upstream Kernel Drivers that you have to create file /etc/udev/rules.d/70-kfd.rules with content 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"'. This looks to me like it adds access to users in the video group only.

---

### 评论 #2 — emerth (2020-04-28T05:42:39Z)

Udev is the correct way to do it. I never got that far in the install guide before trying strace.  I really should have read further!

---

### 评论 #3 — jackyin68 (2020-04-28T11:36:40Z)

Hi, how to solve this,
sudo chmod 777 /dev/kfd
crwxrwxrwx 1 root render 236, 0 4月  28 19:23 /dev/kfd
**But when type sudo strace /opt/rocm/bin/rocminfo, still:**
-----------------------------------------------------------------------------|
----------------------------------------------------------------------------\ /
write(1, "\33[37mnlp is member of video grou"..., 38nlp is member of video group
) = 38
getpid()                                = 2957
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (无法分配内存)
write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-3.1/rocminfo/rocminfo.cc:1102
) = 101
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -351, SEEK_CUR)                = -1 ESPIPE (非法 seek 操作)
exit_group(4104)                        = ?
+++ exited with 8 +++


---

### 评论 #4 — emerth (2020-04-29T00:57:31Z)

> 
> 
> Hi, how to solve this,
> sudo chmod 777 /dev/kfd
> crwxrwxrwx 1 root render 236, 0 4月 28 19:23 /dev/kfd
> **But when type sudo strace /opt/rocm/bin/rocminfo, still:**
> ----------------------------------------------------------------------------\ /
> write(1, "\33[37mnlp is member of video grou"..., 38nlp is member of video group
> ) = 38
> getpid() = 2957
> openat(AT_FDCWD, "/dev/kfd", O_RDWR
> write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-3.1/rocminfo/rocminfo.cc:1102
> ) = 101
> write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
> ) = 228
> write(1, "\33[0m", 4) = 4
> lseek(3, -351, SEEK_CUR) = -1 ESPIPE (非法 seek 操作)
> exit_group(4104) = ?
> +++ exited with 8 +++

That, Jackie, is a different problem. My investigation was resolved because rocm needed to open the /dev/kfd file but the file system permissions were incorrect. Your problem appears to be that rocm can open the /dev/kfd file but cannot write to it. I do not know why.

If you post the entire output from strace it might be more clear what is going on.  I cannot promise I can solve it though. It might be a problem to talk to the ROCm developers about.

If you do post the entire output can you select it all and click the "<>" format button so github renders the text as code (ie verbatim).

---

### 评论 #5 — jackyin68 (2020-04-29T10:30:19Z)

``nlp@nlp-E580:~$ strace /opt/rocm/bin/rocminfo
execve("/opt/rocm/bin/rocminfo", ["/opt/rocm/bin/rocminfo"], 0x7ffd3d8f2730 /* 63 vars */) = 0
brk(NULL)                               = 0x2340000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffdb368ebf0) = -1 EINVAL (无效的参数)
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fec0ecaa000
readlink("/proc/self/exe", "/opt/rocm-3.1.0/bin/rocminfo", 4096) = 28
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/tls/haswell/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/tls/haswell/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/tls/haswell/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/tls/haswell", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/tls/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/tls/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/tls/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/tls", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/haswell/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/haswell/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/haswell/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/haswell", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/tls/haswell/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/tls/haswell/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/tls/haswell/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/tls/haswell", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/tls/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/tls/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/tls/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/tls", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/haswell/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/haswell/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/haswell/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/haswell", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/x86_64/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/x86_64", 0x7ffdb368de40) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libhsa-runtime64.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220&\1\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=975296, ...}) = 0
mmap(NULL, 2869328, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e9ed000
mprotect(0x7fec0eaa4000, 2093056, PROT_NONE) = 0
mmap(0x7fec0eca3000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xb6000) = 0x7fec0eca3000
mmap(0x7fec0eca9000, 2128, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0eca9000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../lib64", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../hsa/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hsa/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hsa/lib", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../hsa/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../../hsa/lib", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hcc/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hcc/lib", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../hip/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../hip/lib", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../opencl/lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../../lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/tls", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/haswell/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/haswell/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/haswell/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/haswell", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/x86_64/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/x86_64", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/data/jenkins_workspace/compute-rocm-rel-3.1/out/ubuntu-16.04/16.04/lib", 0x7ffdb368de20) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=87794, ...}) = 0
mmap(NULL, 87794, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fec0e9d7000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libstdc++.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\240\341\t\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=1952928, ...}) = 0
mmap(NULL, 1968128, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e7f6000
mprotect(0x7fec0e88c000, 1286144, PROT_NONE) = 0
mmap(0x7fec0e88c000, 983040, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x96000) = 0x7fec0e88c000
mmap(0x7fec0e97c000, 299008, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x186000) = 0x7fec0e97c000
mmap(0x7fec0e9c6000, 57344, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1cf000) = 0x7fec0e9c6000
mmap(0x7fec0e9d4000, 10240, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0e9d4000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib64/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../hsa/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360q\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32, 848) = 32
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0cBR\340\305\370\2609W\242\345)q\235A\1"..., 68, 880) = 68
fstat(3, {st_mode=S_IFREG|0755, st_size=2029224, ...}) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0", 32, 848) = 32
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0cBR\340\305\370\2609W\242\345)q\235A\1"..., 68, 880) = 68
mmap(NULL, 2036952, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e604000
mprotect(0x7fec0e629000, 1847296, PROT_NONE) = 0
mmap(0x7fec0e629000, 1540096, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x25000) = 0x7fec0e629000
mmap(0x7fec0e7a1000, 303104, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19d000) = 0x7fec0e7a1000
mmap(0x7fec0e7ec000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1e7000) = 0x7fec0e7ec000
mmap(0x7fec0e7f2000, 13528, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0e7f2000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../../../lib/libgcc_s.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\3405\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=104984, ...}) = 0
mmap(NULL, 107592, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e5e9000
mmap(0x7fec0e5ec000, 73728, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7fec0e5ec000
mmap(0x7fec0e5fe000, 16384, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15000) = 0x7fec0e5fe000
mmap(0x7fec0e602000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x18000) = 0x7fec0e602000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fec0e5e7000
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libhsakmt.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200F\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=189592, ...}) = 0
mmap(NULL, 2261032, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e3be000
mprotect(0x7fec0e3d8000, 2093056, PROT_NONE) = 0
mmap(0x7fec0e5d7000, 61440, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19000) = 0x7fec0e5d7000
mmap(0x7fec0e5e6000, 40, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0e5e6000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/tls/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/tls/haswell/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/tls/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/tls/haswell", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/tls/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/tls/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/tls", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/haswell/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/haswell", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/tls/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64/tls/haswell/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/tls/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64/tls/haswell", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64/tls/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/tls/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64/tls", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64/haswell/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64/haswell", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/tls/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64/tls/haswell/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/tls/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64/tls/haswell", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/tls/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64/tls/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/tls/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64/tls", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/haswell/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64/haswell/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/haswell/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64/haswell", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/x86_64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64/x86_64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib64/libelf.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib64", 0x7ffdb368dda0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libelf.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\2005\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=109200, ...}) = 0
mmap(NULL, 110976, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e3a2000
mmap(0x7fec0e3a5000, 73728, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7fec0e3a5000
mmap(0x7fec0e3b7000, 20480, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x15000) = 0x7fec0e3b7000
mmap(0x7fec0e3bc000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19000) = 0x7fec0e3bc000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libdl.so.2", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 \22\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=18816, ...}) = 0
mmap(NULL, 20752, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e39c000
mmap(0x7fec0e39d000, 8192, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1000) = 0x7fec0e39d000
mmap(0x7fec0e39f000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7fec0e39f000
mmap(0x7fec0e3a0000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7fec0e3a0000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libpthread.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\201\0\0\0\0\0\0"..., 832) = 832
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0w\\\273\377\370\24Ef`xg\200\260\263\264\0"..., 68, 824) = 68
fstat(3, {st_mode=S_IFREG|0755, st_size=157224, ...}) = 0
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0w\\\273\377\370\24Ef`xg\200\260\263\264\0"..., 68, 824) = 68
mmap(NULL, 140408, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e379000
mmap(0x7fec0e380000, 69632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x7000) = 0x7fec0e380000
mmap(0x7fec0e391000, 20480, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x18000) = 0x7fec0e391000
mmap(0x7fec0e396000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1c000) = 0x7fec0e396000
mmap(0x7fec0e398000, 13432, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0e398000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/librt.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/librt.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 7\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=40040, ...}) = 0
mmap(NULL, 44000, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e36e000
mprotect(0x7fec0e371000, 24576, PROT_NONE) = 0
mmap(0x7fec0e371000, 16384, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7fec0e371000
mmap(0x7fec0e375000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x7000) = 0x7fec0e375000
mmap(0x7fec0e377000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x8000) = 0x7fec0e377000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\300\363\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=1369352, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fec0e36c000
mmap(NULL, 1368336, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e21d000
mmap(0x7fec0e22c000, 684032, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xf000) = 0x7fec0e22c000
mmap(0x7fec0e2d3000, 618496, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xb6000) = 0x7fec0e2d3000
mmap(0x7fec0e36a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x14c000) = 0x7fec0e36a000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../lib64", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../hsa/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hsa/lib", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../../hsa/lib", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hcc/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hcc/lib", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../hip/lib/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../hip/lib", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../opencl/lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/tls", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/haswell/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/haswell/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/haswell/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/haswell", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64/libnuma.so.1", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
stat("/opt/rocm-3.1.0/bin/../lib/../../lib/x86_64", 0x7ffdb368dce0) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libnuma.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0204\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=47960, ...}) = 0
mmap(NULL, 51104, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e210000
mprotect(0x7fec0e213000, 32768, PROT_NONE) = 0
mmap(0x7fec0e213000, 20480, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7fec0e213000
mmap(0x7fec0e218000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x8000) = 0x7fec0e218000
mmap(0x7fec0e21b000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xa000) = 0x7fec0e21b000
close(3)                                = 0
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../../../lib64/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/opt/rocm-3.1.0/bin/../lib/../hsa/lib/libpci.so.3", O_RDONLY|O_CLOEXEC) = -1 ENOENT (没有那个文件或目录)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libpci.so.3", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\3008\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=64280, ...}) = 0
mmap(NULL, 66192, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e1ff000
mprotect(0x7fec0e202000, 49152, PROT_NONE) = 0
mmap(0x7fec0e202000, 32768, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x3000) = 0x7fec0e202000
mmap(0x7fec0e20a000, 12288, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xb000) = 0x7fec0e20a000
mmap(0x7fec0e20e000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xe000) = 0x7fec0e20e000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libz.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200\"\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=108936, ...}) = 0
mmap(NULL, 110776, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e1e3000
mprotect(0x7fec0e1e5000, 98304, PROT_NONE) = 0
mmap(0x7fec0e1e5000, 69632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x7fec0e1e5000
mmap(0x7fec0e1f6000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x13000) = 0x7fec0e1f6000
mmap(0x7fec0e1fd000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19000) = 0x7fec0e1fd000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fec0e1e1000
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libresolv.so.2", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 G\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=101320, ...}) = 0
mmap(NULL, 113280, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e1c5000
mprotect(0x7fec0e1c9000, 81920, PROT_NONE) = 0
mmap(0x7fec0e1c9000, 65536, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x4000) = 0x7fec0e1c9000
mmap(0x7fec0e1d9000, 12288, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x14000) = 0x7fec0e1d9000
mmap(0x7fec0e1dd000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x17000) = 0x7fec0e1dd000
mmap(0x7fec0e1df000, 6784, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0e1df000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libudev.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\20X\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=174272, ...}) = 0
mmap(NULL, 178440, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fec0e199000
mmap(0x7fec0e19e000, 110592, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x5000) = 0x7fec0e19e000
mmap(0x7fec0e1b9000, 40960, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x20000) = 0x7fec0e1b9000
mmap(0x7fec0e1c3000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x29000) = 0x7fec0e1c3000
close(3)                                = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fec0e197000
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fec0e194000
arch_prctl(ARCH_SET_FS, 0x7fec0e194780) = 0
mprotect(0x7fec0e7ec000, 12288, PROT_READ) = 0
mprotect(0x7fec0e396000, 4096, PROT_READ) = 0
mprotect(0x7fec0e1c3000, 4096, PROT_READ) = 0
mprotect(0x7fec0e1dd000, 4096, PROT_READ) = 0
mprotect(0x7fec0e1fd000, 4096, PROT_READ) = 0
mprotect(0x7fec0e20e000, 4096, PROT_READ) = 0
mprotect(0x7fec0e21b000, 4096, PROT_READ) = 0
mprotect(0x7fec0e36a000, 4096, PROT_READ) = 0
mprotect(0x7fec0e377000, 4096, PROT_READ) = 0
mprotect(0x7fec0e3a0000, 4096, PROT_READ) = 0
mprotect(0x7fec0e3bc000, 4096, PROT_READ) = 0
mprotect(0x7fec0e5d7000, 12288, PROT_READ) = 0
mprotect(0x7fec0e602000, 4096, PROT_READ) = 0
mprotect(0x7fec0e9c6000, 45056, PROT_READ) = 0
mprotect(0x7fec0eca3000, 20480, PROT_READ) = 0
mprotect(0x60b000, 4096, PROT_READ)     = 0
mprotect(0x7fec0ecd9000, 4096, PROT_READ) = 0
munmap(0x7fec0e9d7000, 87794)           = 0
set_tid_address(0x7fec0e194a50)         = 3010
set_robust_list(0x7fec0e194a60, 24)     = 0
rt_sigaction(SIGRTMIN, {sa_handler=0x7fec0e380bf0, sa_mask=[], sa_flags=SA_RESTORER|SA_SIGINFO, sa_restorer=0x7fec0e38e3c0}, NULL, 8) = 0
rt_sigaction(SIGRT_1, {sa_handler=0x7fec0e380c90, sa_mask=[], sa_flags=SA_RESTORER|SA_RESTART|SA_SIGINFO, sa_restorer=0x7fec0e38e3c0}, NULL, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [RTMIN RT_1], NULL, 8) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
brk(NULL)                               = 0x2340000
brk(0x2361000)                          = 0x2361000
openat(AT_FDCWD, "/proc/self/status", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "Name:\trocminfo\nUmask:\t0002\nState"..., 1024) = 1024
read(3, "0000,00000000,00000000,00000000,"..., 1024) = 347
close(3)                                = 0
openat(AT_FDCWD, "/sys/devices/system/node", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(3, /* 10 entries */, 32768)  = 312
openat(AT_FDCWD, "/sys/devices/system/node/node0/meminfo", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0444, st_size=4096, ...}) = 0
read(4, "Node 0 MemTotal:       16291876 "..., 4096) = 1173
read(4, "", 4096)                       = 0
close(4)                                = 0
getdents64(3, /* 0 entries */, 32768)   = 0
close(3)                                = 0
sched_getaffinity(0, 512, [0, 1, 2, 3, 4, 5, 6, 7]) = 8
openat(AT_FDCWD, "/sys/devices/system/cpu", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=0, ...}) = 0
getdents64(3, /* 26 entries */, 32768)  = 752
getdents64(3, /* 0 entries */, 32768)   = 0
close(3)                                = 0
openat(AT_FDCWD, "/proc/self/status", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "Name:\trocminfo\nUmask:\t0002\nState"..., 1024) = 1024
read(3, "0000,00000000,00000000,00000000,"..., 1024) = 347
read(3, "", 1024)                       = 0
close(3)                                = 0
uname({sysname="Linux", nodename="nlp-E580", ...}) = 0
futex(0x7fec0e9d46bc, FUTEX_WAKE_PRIVATE, 2147483647) = 0
futex(0x7fec0e9d46c8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
pipe2([3, 4], O_CLOEXEC)                = 0
prlimit64(0, RLIMIT_NOFILE, NULL, {rlim_cur=65535, rlim_max=65535}) = 0
prlimit64(0, RLIMIT_NOFILE, NULL, {rlim_cur=65535, rlim_max=65535}) = 0
mmap(NULL, 36864, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7fec0e9e4000
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone(child_stack=0x7fec0e9ecff0, flags=CLONE_VM|CLONE_VFORK|SIGCHLD) = 3011
munmap(0x7fec0e9e4000, 36864)           = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
close(4)                                = 0
fcntl(3, F_SETFD, 0)                    = 0
fstat(3, {st_mode=S_IFIFO|0600, st_size=0, ...}) = 0
read(3, "amdgpu               4833280  1\n"..., 4096) = 367
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0), ...}) = 0
--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=3011, si_uid=1000, si_status=0, si_utime=0, si_stime=0} ---
write(1, "\33[37mROCk module is loaded\33[0m\n", 31ROCk module is loaded
) = 31
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 4
connect(4, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (没有那个文件或目录)
close(4)                                = 0
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 4
connect(4, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (没有那个文件或目录)
close(4)                                = 0
openat(AT_FDCWD, "/etc/nsswitch.conf", O_RDONLY|O_CLOEXEC) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=545, ...}) = 0
read(4, "# /etc/nsswitch.conf\n#\n# Example"..., 4096) = 545
read(4, "", 4096)                       = 0
close(4)                                = 0
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=87794, ...}) = 0
mmap(NULL, 87794, PROT_READ, MAP_PRIVATE, 4, 0) = 0x7fec0e9d7000
close(4)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libnss_compat.so.2", O_RDONLY|O_CLOEXEC) = 4
read(4, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0$\0\0\0\0\0\0"..., 832) = 832
fstat(4, {st_mode=S_IFREG|0644, st_size=43968, ...}) = 0
mmap(NULL, 47264, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 4, 0) = 0x7fec0e188000
mmap(0x7fec0e18a000, 28672, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x2000) = 0x7fec0e18a000
mmap(0x7fec0e191000, 4096, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x9000) = 0x7fec0e191000
mmap(0x7fec0e192000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x9000) = 0x7fec0e192000
close(4)                                = 0
mprotect(0x7fec0e192000, 4096, PROT_READ) = 0
munmap(0x7fec0e9d7000, 87794)           = 0
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=87794, ...}) = 0
mmap(NULL, 87794, PROT_READ, MAP_PRIVATE, 4, 0) = 0x7fec0e9d7000
close(4)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libnss_nis.so.2", O_RDONLY|O_CLOEXEC) = 4
read(4, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\2005\0\0\0\0\0\0"..., 832) = 832
fstat(4, {st_mode=S_IFREG|0644, st_size=55928, ...}) = 0
mmap(NULL, 58760, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 4, 0) = 0x7fec0e179000
mmap(0x7fec0e17c000, 32768, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x3000) = 0x7fec0e17c000
mmap(0x7fec0e184000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0xb000) = 0x7fec0e184000
mmap(0x7fec0e186000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0xc000) = 0x7fec0e186000
close(4)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libnsl.so.1", O_RDONLY|O_CLOEXEC) = 4
read(4, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0 ]\0\0\0\0\0\0"..., 832) = 832
fstat(4, {st_mode=S_IFREG|0644, st_size=105528, ...}) = 0
mmap(NULL, 117336, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 4, 0) = 0x7fec0e15c000
mmap(0x7fec0e161000, 65536, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x5000) = 0x7fec0e161000
mmap(0x7fec0e171000, 16384, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x15000) = 0x7fec0e171000
mmap(0x7fec0e175000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x18000) = 0x7fec0e175000
mmap(0x7fec0e177000, 6744, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0e177000
close(4)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libnss_files.so.2", O_RDONLY|O_CLOEXEC) = 4
read(4, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\3005\0\0\0\0\0\0"..., 832) = 832
fstat(4, {st_mode=S_IFREG|0644, st_size=51832, ...}) = 0
mmap(NULL, 79672, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 4, 0) = 0x7fec0e148000
mmap(0x7fec0e14b000, 28672, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x3000) = 0x7fec0e14b000
mmap(0x7fec0e152000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0xa000) = 0x7fec0e152000
mmap(0x7fec0e154000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0xb000) = 0x7fec0e154000
mmap(0x7fec0e156000, 22328, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fec0e156000
close(4)                                = 0
mprotect(0x7fec0e154000, 4096, PROT_READ) = 0
mprotect(0x7fec0e175000, 4096, PROT_READ) = 0
mprotect(0x7fec0e186000, 4096, PROT_READ) = 0
munmap(0x7fec0e9d7000, 87794)           = 0
openat(AT_FDCWD, "/etc/group", O_RDONLY|O_CLOEXEC) = 4
lseek(4, 0, SEEK_CUR)                   = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=1028, ...}) = 0
mmap(NULL, 1028, PROT_READ, MAP_SHARED, 4, 0) = 0x7fec0ecd8000
lseek(4, 1028, SEEK_SET)                = 1028
munmap(0x7fec0ecd8000, 1028)            = 0
close(4)                                = 0
openat(AT_FDCWD, "/proc/self/loginuid", O_RDONLY) = 4
read(4, "1000", 12)                     = 4
close(4)                                = 0
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 4
connect(4, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (没有那个文件或目录)
close(4)                                = 0
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 4
connect(4, {sa_family=AF_UNIX, sun_path="/var/run/nscd/socket"}, 110) = -1 ENOENT (没有那个文件或目录)
close(4)                                = 0
openat(AT_FDCWD, "/etc/passwd", O_RDONLY|O_CLOEXEC) = 4
lseek(4, 0, SEEK_CUR)                   = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=2754, ...}) = 0
mmap(NULL, 2754, PROT_READ, MAP_SHARED, 4, 0) = 0x7fec0ecd8000
lseek(4, 2754, SEEK_SET)                = 2754
munmap(0x7fec0ecd8000, 2754)            = 0
close(4)                                = 0
openat(AT_FDCWD, "/etc/passwd", O_RDONLY|O_CLOEXEC) = 4
lseek(4, 0, SEEK_CUR)                   = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=2754, ...}) = 0
mmap(NULL, 2754, PROT_READ, MAP_SHARED, 4, 0) = 0x7fec0ecd8000
lseek(4, 2754, SEEK_SET)                = 2754
munmap(0x7fec0ecd8000, 2754)            = 0
close(4)                                = 0
openat(AT_FDCWD, "/etc/group", O_RDONLY|O_CLOEXEC) = 4
lseek(4, 0, SEEK_CUR)                   = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=1028, ...}) = 0
mmap(NULL, 1028, PROT_READ, MAP_SHARED, 4, 0) = 0x7fec0ecd8000
lseek(4, 1028, SEEK_SET)                = 1028
fstat(4, {st_mode=S_IFREG|0644, st_size=1028, ...}) = 0
munmap(0x7fec0ecd8000, 1028)            = 0
close(4)                                = 0
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 4
fstat(4, {st_mode=S_IFREG|0644, st_size=87794, ...}) = 0
mmap(NULL, 87794, PROT_READ, MAP_PRIVATE, 4, 0) = 0x7fec0e9d7000
close(4)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libnss_systemd.so.2", O_RDONLY|O_CLOEXEC) = 4
read(4, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\340W\0\0\0\0\0\0"..., 832) = 832
fstat(4, {st_mode=S_IFREG|0644, st_size=231544, ...}) = 0
mmap(NULL, 235944, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 4, 0) = 0x7fec0e10e000
mmap(0x7fec0e113000, 151552, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x5000) = 0x7fec0e113000
mmap(0x7fec0e138000, 49152, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x2a000) = 0x7fec0e138000
mmap(0x7fec0e144000, 16384, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 4, 0x35000) = 0x7fec0e144000
close(4)                                = 0
mprotect(0x7fec0e144000, 12288, PROT_READ) = 0
munmap(0x7fec0e9d7000, 87794)           = 0
rt_sigprocmask(SIG_BLOCK, [HUP USR1 USR2 PIPE ALRM CHLD TSTP URG VTALRM PROF WINCH IO], [], 8) = 0
gettid()                                = 3010
socket(AF_UNIX, SOCK_DGRAM|SOCK_CLOEXEC, 0) = 4
connect(4, {sa_family=AF_UNIX, sun_path=@"userdb-5c51e63df4e942589c0576b5e921b1d9"}, 42) = -1 ECONNREFUSED (拒绝连接)
close(4)                                = 0
openat(AT_FDCWD, "/run/systemd/userdb/", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
fstat(4, {st_mode=S_IFDIR|0755, st_size=60, ...}) = 0
brk(0x2384000)                          = 0x2384000
getdents64(4, /* 3 entries */, 32768)   = 96
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 5
connect(5, {sa_family=AF_UNIX, sun_path="/run/systemd/userdb/io.systemd.DynamicUser"}, 45) = 0
getpid()                                = 3010
epoll_create1(EPOLL_CLOEXEC)            = 6
timerfd_create(CLOCK_MONOTONIC, TFD_CLOEXEC|TFD_NONBLOCK) = 7
epoll_ctl(6, EPOLL_CTL_ADD, 7, {EPOLLIN, {u32=37109280, u64=37109280}}) = 0
epoll_ctl(6, EPOLL_CTL_ADD, 5, {0, {u32=37111152, u64=37111152}}) = 0
gettid()                                = 3010
getdents64(4, /* 0 entries */, 32768)   = 0
close(4)                                = 0
epoll_ctl(6, EPOLL_CTL_MOD, 5, {EPOLLIN|EPOLLOUT, {u32=37111152, u64=37111152}}) = 0
openat(AT_FDCWD, "/proc/sys/kernel/random/boot_id", O_RDONLY|O_NOCTTY|O_CLOEXEC) = 4
read(4, "78de50c9-fca6-41c7-8ced-61241d80"..., 38) = 37
read(4, "", 1)                          = 0
close(4)                                = 0
timerfd_settime(7, TFD_TIMER_ABSTIME, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=583, tv_nsec=775188000}}, NULL) = 0
epoll_wait(6, [{EPOLLOUT, {u32=37111152, u64=37111152}}], 4, 0) = 1
timerfd_create(CLOCK_BOOTTIME, TFD_CLOEXEC|TFD_NONBLOCK) = 4
close(4)                                = 0
sendto(5, "{\"method\":\"io.systemd.UserDataba"..., 131, MSG_DONTWAIT|MSG_NOSIGNAL, NULL, 0) = 131
epoll_ctl(6, EPOLL_CTL_MOD, 5, {EPOLLIN, {u32=37111152, u64=37111152}}) = 0
epoll_wait(6, [], 4, 0)                 = 0
mmap(NULL, 135168, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fec0e0ed000
mremap(0x7fec0e0ed000, 135168, 139264, MREMAP_MAYMOVE) = 0x7fec0e0cb000
recvfrom(5, "{\"error\":\"io.systemd.UserDatabas"..., 135152, MSG_DONTWAIT, NULL, NULL) = 66
epoll_ctl(6, EPOLL_CTL_MOD, 5, {0, {u32=37111152, u64=37111152}}) = 0
epoll_wait(6, [], 4, 0)                 = 0
epoll_wait(6, [], 4, 0)                 = 0
epoll_ctl(6, EPOLL_CTL_DEL, 5, NULL)    = 0
close(5)                                = 0
munmap(0x7fec0e0cb000, 139264)          = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
close(6)                                = 0
close(7)                                = 0
openat(AT_FDCWD, "/etc/group", O_RDONLY|O_CLOEXEC) = 4
lseek(4, 0, SEEK_CUR)                   = 0
fstat(4, {st_mode=S_IFREG|0644, st_size=1028, ...}) = 0
mmap(NULL, 1028, PROT_READ, MAP_SHARED, 4, 0) = 0x7fec0ecd8000
lseek(4, 1028, SEEK_SET)                = 1028
fstat(4, {st_mode=S_IFREG|0644, st_size=1028, ...}) = 0
munmap(0x7fec0ecd8000, 1028)            = 0
close(4)                                = 0
rt_sigprocmask(SIG_BLOCK, [HUP USR1 USR2 PIPE ALRM CHLD TSTP URG VTALRM PROF WINCH IO], [], 8) = 0
gettid()                                = 3010
socket(AF_UNIX, SOCK_DGRAM|SOCK_CLOEXEC, 0) = 4
connect(4, {sa_family=AF_UNIX, sun_path=@"userdb-5c51e63df4e942589c0576b5e921b1d9"}, 42) = -1 ECONNREFUSED (拒绝连接)
close(4)                                = 0
openat(AT_FDCWD, "/run/systemd/userdb/", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 4
fstat(4, {st_mode=S_IFDIR|0755, st_size=60, ...}) = 0
getdents64(4, /* 3 entries */, 32768)   = 96
socket(AF_UNIX, SOCK_STREAM|SOCK_CLOEXEC|SOCK_NONBLOCK, 0) = 5
connect(5, {sa_family=AF_UNIX, sun_path="/run/systemd/userdb/io.systemd.DynamicUser"}, 45) = 0
epoll_create1(EPOLL_CLOEXEC)            = 6
timerfd_create(CLOCK_MONOTONIC, TFD_CLOEXEC|TFD_NONBLOCK) = 7
epoll_ctl(6, EPOLL_CTL_ADD, 7, {EPOLLIN, {u32=37109280, u64=37109280}}) = 0
epoll_ctl(6, EPOLL_CTL_ADD, 5, {0, {u32=37056896, u64=37056896}}) = 0
getdents64(4, /* 0 entries */, 32768)   = 0
close(4)                                = 0
epoll_ctl(6, EPOLL_CTL_MOD, 5, {EPOLLIN|EPOLLOUT, {u32=37056896, u64=37056896}}) = 0
timerfd_settime(7, TFD_TIMER_ABSTIME, {it_interval={tv_sec=0, tv_nsec=0}, it_value={tv_sec=583, tv_nsec=775188000}}, NULL) = 0
epoll_wait(6, [{EPOLLOUT, {u32=37056896, u64=37056896}}], 4, 0) = 1
sendto(5, "{\"method\":\"io.systemd.UserDataba"..., 131, MSG_DONTWAIT|MSG_NOSIGNAL, NULL, 0) = 131
epoll_ctl(6, EPOLL_CTL_MOD, 5, {EPOLLIN, {u32=37056896, u64=37056896}}) = 0
epoll_wait(6, [{EPOLLIN, {u32=37056896, u64=37056896}}], 4, 0) = 1
brk(0x23a5000)                          = 0x23a5000
recvfrom(5, "{\"error\":\"io.systemd.UserDatabas"..., 131080, MSG_DONTWAIT, NULL, NULL) = 66
epoll_ctl(6, EPOLL_CTL_MOD, 5, {0, {u32=37056896, u64=37056896}}) = 0
epoll_wait(6, [], 4, 0)                 = 0
epoll_wait(6, [], 4, 0)                 = 0
epoll_ctl(6, EPOLL_CTL_DEL, 5, NULL)    = 0
close(5)                                = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
close(6)                                = 0
close(7)                                = 0
write(1, "\33[37mnlp is member of video grou"..., 38nlp is member of video group
) = 38
getpid()                                = 3010
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (无法分配内存)
write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-3.1/rocminfo/rocminfo.cc:1102
) = 101
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -351, SEEK_CUR)                = -1 ESPIPE (非法 seek 操作)
exit_group(4104)                        = ?
+++ exited with 8 +++


---

### 评论 #6 — emerth (2020-05-01T05:04:21Z)

This line near the end of your strace output makes me think that either your GPU or your CPU is running out of memory:

`openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (无法分配内存)
`

If your GPU is running out of memory then I think you need to reduce your batch size or use a simpler model. If your CPU is running out of memory then perhaps you can get more RAM or change your job to use less memory.

Also, please post logs and such as CODE. Unformated computer output is hard to read.

---

### 评论 #7 — ndmphuc (2020-05-17T03:07:21Z)

Run this command `# strace /opt/rocm/bin/rocminfo` and I got this at the end:

`openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (Cannot allocate memory)
write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
) = 101
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -368, SEEK_CUR)                = -1 ESPIPE (Illegal seek)
exit_group(4104)                        = ?
+++ exited with 8 +++
`
My PC Ubuntu has 64GB RAM. I used Firepro S9300 x2 which has 4GB RAM x2, and a Quadro NVS 310 512MB for monitor display. Please help me solving this. Thanks!

---

### 评论 #8 — emerth (2020-05-17T08:58:30Z)

> 
> 
> Run this command `# strace /opt/rocm/bin/rocminfo` and I got this at the end:
> 
> `openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (Cannot allocate memory) write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102 ) = 101 write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events. ) = 228 write(1, "\33[0m", 4) = 4 lseek(3, -368, SEEK_CUR) = -1 ESPIPE (Illegal seek) exit_group(4104) = ? +++ exited with 8 +++ `
> My PC Ubuntu has 64GB RAM. I used Firepro S9300 x2 which has 4GB RAM x2, and a Quadro NVS 310 512MB for monitor display. Please help me solving this. Thanks!

Read the first line of the text you posted. 

---

### 评论 #9 — emerth (2020-05-17T09:00:36Z)

Closing because people are starting to ask me to "make my computer work" who clearly can't be bothered to read the instructions or read their strace output.

---

### 评论 #10 — krishoza (2020-10-21T17:40:39Z)

@emerth any comment on `openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 EAGAIN (Resource temporarily unavailable)`

---

### 评论 #11 — emerth (2020-10-22T03:31:33Z)

Only that your /dev/kfd is likely not readable and writeable by the account you are using.

Read my original post in this thread. Anything beyond that I can suggest that you get out your copy of "Advanced Programming in the UNIX Environment" by by W. Richard Stevens, or that you look at the man page for openat() and the associated pages for POSIX IO generally.

I don't mean to be terse in my answer. The problem is that I cannot debug a computer or process I have no access to. I am not actually a ROCm expert - I'm just pretty good sometimes at debugging programs. When I made the original post I had just debugged a particular issue with my then ROCm installation. Your bug might be quite different.

---
