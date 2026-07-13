# One solution to rocminfo fails with HSA_STATUS_ERROR_OUT_OF_RESOURCES

- **Issue #:** 1088
- **State:** closed
- **Created:** 2020-04-23T19:09:47Z
- **Updated:** 2020-10-22T03:44:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1088

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