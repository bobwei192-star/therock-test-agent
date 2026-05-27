# OpenCL crash when not run as root

> **Issue #62**
> **状态**: closed
> **创建时间**: 2016-12-28T21:38:03Z
> **更新时间**: 2017-01-04T03:20:38Z
> **关闭时间**: 2017-01-04T03:20:38Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/62

## 描述

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

---

## 评论 (9 条)

### 评论 #1 — nevion (2016-12-30T18:31:07Z)

Hm, I suspected but thought I addressed permissions of /dev/kfd before posting - but just to confirm this is a permissions issue on /dev/kfd.

new permissions:
 `crw-rw-rw- 1 root video 244, 0 Dec 30 13:01 /dev/kfd`

I edited /etc/udev/rules.d/kfd.rules to contain:
`KERNEL=="kfd", MODE="0666", GROUP="video"`

And also added my user to the video group.  I'm not sure if this is the best group for the job but it is on most distros and makes a modicum of sense.

Issue is up for closing but please patch kfd.rules - not sure which repo it's in atm.

---

### 评论 #2 — jedwards-AMD (2017-01-03T17:42:19Z)

Can you provide the output of 'uname -a', so I can confirm you have the correct kernel installed. I configured my /dev/kfd (via udev config file) and I had no problem running clinfo. The fact that you are trying to open an amdgpu-pro file indicates to me that you don't have the correct version of amdgpu installed (ROCm doesn't currently run on the pro driver).


---

### 评论 #3 — nevion (2017-01-03T19:00:52Z)

@jedwards-AMD 
Linux ar96607 4.6.0-kfd-compute-rocm-rel-1.4-16 #1 SMP Tue Dec 13 13:14:21 EST 2016 x86_64 x86_64 x86_64 GNU/Linux

The query function will fail to open /dev/kfd if the perms aren't correct and by default root:root owns /dev/kfd - although I'm not sure why 0666 wouldn't have worked...  You can see it'w working with an invalid file descriptor in the above fstat/ioctl calls prior to segfault.... after I did that change things worked fine with both ROCm and AMDGPU Pro.

I do have the AMDGPU Pro installed but I guess we're seeing some mixing and matching going on - though I'm not really sure of the outcome.   I learned running other programs eventually that I needed to target the runtime I needed to run against with LD_LIBRARY_PATH - and it seems both AMDGPU pros cl stack and rocm's can run on the same kernel with this method.

---

### 评论 #4 — jedwards-AMD (2017-01-03T20:16:18Z)

I think you identified the problem; your LD_LIBRARY_PATH is set for you non-root user and is pointing to AMDGPU Pro libraries that require the AMDGPU Pro driver set. I would check the user's environment, and make sure LD_LIBRARY_PATH is empty. I don't think this has anything to do with the permissions of /dev/kfd. I was able to run with the root:video ownership set.

From your strace output I don't ever see an attempt to open the /dev/kfd file, which would look like this:

open("/dev/kfd", O_RDWR|O_CLOEXEC)      = 5

Basically, your user mode libraries are trying to call down into the compatible amdgpu pro driver interfaces, which are not installed.

---

### 评论 #5 — nevion (2017-01-03T20:25:12Z)

er... no LD_LIBRARY_PATH I'm setting right as I invoke the binaries - and this is the way I'm making things work.

I'll see if I can post another strace illustrating the open later tonight.

I have AMD GPU pro driver interfaces installed.  If I don't use LD_LIBRARY_PATH (because rocm is in /opt and AMDGPU Pro is in /usr), everything goes to the AMDGPU Pro runtime.

---

### 评论 #6 — jedwards-AMD (2017-01-03T21:03:18Z)

Does the file /etc/ld.so.conf.d/x86_64-opencl-rom.conf exist? This is the configuration file that updates the ldconfig environment to put the opencl libraries in the ld search path. This does seem to be a problem with multiple versions of OpenCL installed on the system, however.

---

### 评论 #7 — nevion (2017-01-03T22:11:39Z)

yes it does, but having both AMDGPU pro installed and rocm opencl is bound to clash and LD_LIBRARY_PATH is a way of dealing with that ... this is solved with different vendor runtimes via platform and ICD files to help load the vendor specific runtime, IIRC.  Maybe both runtimes should take part in that?

---

### 评论 #8 — nevion (2017-01-03T23:52:49Z)

Ok I have the explination for this bug - it is not a ROCm issue, but a AMDGPU-Pro issue.

When running headless (x installed, just no DISPLAY running), with a user not in the video group, under Ubuntu 16.04 and using the AMDGPU-Pro runtime, you will get the above crash loading up the OpenCL runtime.  The file descriptor the runtime is erroneously using without checking in the result above is the result of calling open on /dev/dri/* - these files are all group-owned by video.

However video is a half deprecated group.  Especially on Ubuntu, you do not need to be in video to log into the system.  But it's Ubuntu and complicated in the name of simple... so I don't know what should be the fixes.

I do know 2 things:

- Failed opens of this significance should be checked and reported/aborted on appropriately before things get to a confusing segfault later.
- The runtime should work without the user being in the video group, ideally. If not this should be documented better.

Since this is AMDGPU-Pro - I can't fault the ROCm project for that but well, this bug exists here now and there's probably overlap of code and people... so please pass the bug report along the right channels?

---

### 评论 #9 — gstoner (2017-01-04T03:15:59Z)

I will talk to the team looking after this driver. 


---
