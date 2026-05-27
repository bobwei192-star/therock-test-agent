# vector_copy: Create the program failed

> **Issue #124**
> **状态**: closed
> **创建时间**: 2017-05-17T13:43:39Z
> **更新时间**: 2017-07-09T08:10:44Z
> **关闭时间**: 2017-07-09T08:10:44Z
> **作者**: oheid
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/124

## 描述

What is going wrong here? vector_copy on my Ryzen CPU + R9 480 GPU stops prematurely at the HSA finalizer loading stage:
```
./vector_copy
Profiling of privileged counters is not available
Profiling is not available
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program failed.
```

---

## 评论 (11 条)

### 评论 #1 — grmat (2017-05-17T17:04:17Z)

Might be related to #120 

---

### 评论 #2 — gstoner (2017-05-17T17:51:13Z)

We uploaded updated driver which address #120  please update your driver if you think you have this issue. 

---

### 评论 #3 — oheid (2017-05-18T09:14:54Z)

Unfortunately I don't think this helps: I don't even have the OpenCL tree installed.
Just to make sure I got it right: samples/vector_copy depends solely only on ROCK kernel, ROCT thunk, ROCR runtime and the binary HSA-finalizer-AMD?
Actually my problem looks much like ROCR-Runtime issue # 21 (sorry - how do you crosslink to another subtree?). My strace dump is identical to patricklauer's:
```
write(1, "Creating the queue succeeded.\n", 30Creating the queue succeeded.
) = 30
write(1, "\"Obtaining machine model\" succee"..., 37"Obtaining machine model" succeeded.
) = 37
write(1, "\"Getting agent profile\" succeede"..., 35"Getting agent profile" succeeded.
) = 35
open("vector_copy_base.brig", O_RDONLY) = 4
fstat(4, {st_mode=S_IFREG|0664, st_size=3456, ...}) = 0
fstat(4, {st_mode=S_IFREG|0664, st_size=3456, ...}) = 0
lseek(4, 0, SEEK_SET)                   = 0
read(4, "HSA BRIG\1\0\0\0\0\0\0\0\200\r\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 3456) = 3456
lseek(4, 3456, SEEK_SET)                = 3456
close(4)                                = 0
write(1, "Create the program failed.\n", 27Create the program failed.
) = 27
exit_group(1)                           = ?
+++ exited with 1 +++
```
I use amdgpu graphics driver and the latest ROCx git versions.

---

### 评论 #4 — gstoner (2017-05-18T23:54:42Z)

Your mixing the wrong Linux kernel  did you first try the install instruction on ROCm.gihub.io and use the repo server before you tried to build your ROCm  release 

---

### 评论 #5 — oheid (2017-05-19T14:31:50Z)

Interesting - thanks for the hint!
I ended up building my own 4.9.0 ROCK kernel because I couldn't boot kernel-4.9.0_kfd_compute_rocm_rel_1.5_80-2 binary from yum repository: The last boot message was "reached target basic system" (and dracut timeout messages a minute or so later).
My own kernel boots fine though. I built ROCK, ROCT and ROCR from the latest master sources (all pulled less 5 days ago), and I also tried the yum-archived ROCT and ROCR binaries on top of my kernel, with identical negative result in vector_copy (see above).
Thanks for your help! Please tell me if you need any more info or logfile.

---

### 评论 #6 — oheid (2017-05-20T12:12:46Z)

The latest  vector_copy.c  is a bit more verbose:
```
./vector_copy 
Profiling of privileged counters is not available
Profiling is not available
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx803.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Load module from file succeeded.
Create the program failed: 100b.
```
As an aside: kmtreopen from ROCT-Thunk-Interface passes all 5 iterations.

---

### 评论 #7 — oheid (2017-05-29T17:18:01Z)

I finally got vector_copy working as expected with a self-built ROCK kernel under Fedora 25, after solving two issues which the Ubuntu 16.04 install procedure did not show:
1) make xconfig: choose arch/x86/configs/rock-rel_defconfig instead of the default config. The name of the resulting kernel is 4.9.0-kfd, not 4.9.0. Ubuntu defaults to the proper config.
I also did
`echo "add_drivers+=\"amdkfd\"" >> /etc/dracut.conf.d/amdkfd.conf` 
to make sure amdkfd.ko is in initramfs.
2) libhsa-ext-finalize64.so.1 and libhsa-ext-image64.so.1 have to be included in the library path, e.g. by creating symbolic links from /opt/rocm/lib or by including /opt/rocm/hsa/lib/.

---

### 评论 #8 — oheid (2017-05-30T14:35:51Z)

Another potential pitfall: The rocm config file configures the AHCI driver as ahci.ko module, but Fedora 25 does not normally include it into initramfs, so booting from SATA will invariably fail with "/dev/root not found". A solution is to 
`echo "add_drivers+=\" ahci \"" >> /etc/dracut.conf.d/amdkfd.conf`
and rebuild initramfs, or compile the AHCI driver into the kernel as the default (non-kfd) config file does.
I needed this initramfs fix also for the ROCK kernel binary from yum archive.

---

### 评论 #9 — oheid (2017-06-04T09:59:31Z)

Some more sanity measures I needed to do for ROCm on Fedora 25:
- [ ] set `Option "TearFree" "off"` in xorg.conf "Device" section. TearFree randomly hangs X, seemingly due to a race condition when swapping screen buffers.
- [ ] `blacklist evbug` module to avoid massive dmesg flooding. Seems harmless otherwise (?)
- [ ] re-enable SELinux by `CONFIG_SECURITY_SELINUX_CHECKREQPROT_VALUE=1` and  `CONFIG_DEFAULT_SECURITY="selinux"` in kernel config.

---

### 评论 #10 — gstoner (2017-07-02T17:48:19Z)

Ok I let the team know of these changes from Fedora 24 to Fedora 25 

---

### 评论 #11 — oheid (2017-07-09T08:10:44Z)

The TearFree issue appears to be fixed in ROCm-1.6 

---
