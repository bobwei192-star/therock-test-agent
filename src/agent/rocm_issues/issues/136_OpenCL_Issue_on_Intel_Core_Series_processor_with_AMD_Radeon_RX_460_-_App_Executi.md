# OpenCL  Issue on Intel Core Series processor with AMD Radeon RX 460 -  App Execution  issue with clinfo and  luxmark 

> **Issue #136**
> **状态**: closed
> **创建时间**: 2017-06-28T10:18:49Z
> **更新时间**: 2018-06-03T14:57:22Z
> **关闭时间**: 2018-06-03T14:57:22Z
> **作者**: muralimk51
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/136

## 描述

Hi,
I am using Skylake	board with AMD Radeon ™ RX 460 Graphics and installed the rocm1.5 package after setting proxy as mentioned in https://github.com/RadeonOpenCompute/ROCm
apt-get install rocm rocm-opencl.
1. When I execute the command below, not getting any information for "clinfo"
root@bdk:/opt/rocm/opencl/bin/x86_64# ./clinfo 
<..not getting any log..>

2. Also installed "luxmark-linux64-v3.1.tar.bz2" package and executed  in skylake, But getting below error:
root@bdk:/luxmark-v3.1# ./luxmark
Profiling is not available
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
./luxmark: line 12:  3339 Aborted                 ./luxmark.bin "$@"

Could you please let me know what is the issue and how to proceed on this above issue.

---

## 评论 (16 条)

### 评论 #1 — gstoner (2017-06-28T11:05:11Z)

Did you check if the stack was working first?  

cd /opt/rocm/hsa/sample
make
./vector_copy

---

### 评论 #2 — muralimk51 (2017-06-28T11:11:51Z)

Dear gstoner, Thanks for your reply

Executed as below:
root@bdk:/opt/rocm/hsa/sample# ls
Makefile  vector_copy_base.brig  vector_copy_base.hsail  vector_copy.c  vector_copy_full.brig  vector_copy_full.hsail
root@bdk:/opt/rocm/hsa/sample# make
gcc -c -I/opt/rocm/include -o vector_copy.o vector_copy.c -std=c99
gcc -Wl,--unresolved-symbols=ignore-in-shared-libs vector_copy.o -L/opt/rocm/lib -lhsa-runtime64 -o vector_copy

root@bdk:/opt/rocm/hsa/sample# ls -alh
total 88K
drwxrwxr-x 2 root root 4.0K Jun 28 20:08 .
drwxrwxr-x 6 root root 4.0K Jun 28 19:38 ..
-rw-rw-r-- 1 root root 2.4K Apr  5 00:54 Makefile
-rwxr-xr-x 1 root root  23K Jun 28 20:08 vector_copy
-rw-rw-r-- 1 root root 3.4K Apr  5 00:54 vector_copy_base.brig
-rw-rw-r-- 1 root root 2.5K Apr  5 00:54 vector_copy_base.hsail
-rw-rw-r-- 1 root root  15K Apr  5 00:54 vector_copy.c
-rw-rw-r-- 1 root root 3.4K Apr  5 00:54 vector_copy_full.brig
-rw-rw-r-- 1 root root 2.5K Apr  5 00:54 vector_copy_full.hsail
-rw-r--r-- 1 root root  18K Jun 28 20:08 vector_copy.o

root@bdk:/opt/rocm/hsa/sample# ./vector_copy 
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
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
|
<..cursor not released after this above message..>

I am getting above messages and read https://streamhpc.com/blog/2017-05-03/amd-rocm-1-5-linux-driver-stack-is-out/?upm_export=print -> here vectory_copy is printing full log
Could you please let me know how to resolve the above issue

---

### 评论 #3 — gstoner (2017-06-28T12:09:54Z)

The driver is not loading 
Can you type lspci -vv | grep AMD

---

### 评论 #4 — gstoner (2017-06-28T12:13:43Z)

Sorry  I need my Coffee,  driver loaded still run lspci.    But you may also need the Dev package for OpenCL.     One thing we getting ready to release new drop of ROCm tomorrow. 

---

### 评论 #5 — muralimk51 (2017-06-28T12:24:32Z)

Dear gstoner,

root@bdk:~# lspci -vv | grep AMD
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67ef (rev cf) (prog-if 00 [VGA controller])
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0

As you mentioned that  "The driver is not loading" -> How can I load, Just i executed below commands
apt-get install rocm rocm-opencl  (Ref: https://github.com/RadeonOpenCompute/ROCm )

Could you please tell me did I missed anything to load the driver


---

### 评论 #6 — gstoner (2017-06-28T12:49:09Z)

sudo apt-get install rocm rocm-opencl-dev
On Jun 28, 2017, at 7:24 AM, muralimk51 <notifications@github.com<mailto:notifications@github.com>> wrote:


Dear gstoner,

root@bdk:~# lspci -vv | grep AMD
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67ef (rev cf) (prog-if 00 [VGA controller])
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aae0

As you mentioned that "The driver is not loading" -> How can I load, Just i executed below commands
apt-get install rocm rocm-opencl (Ref: https://github.com/RadeonOpenCompute/ROCm )

Could you please tell me did I missed anything to load the driver

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/136#issuecomment-311644088>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuZgW4dZ8FleYHgj6rMstlbH7Z5piks5sIkYBgaJpZM4OHxJD>.



---

### 评论 #7 — muralimk51 (2017-06-28T12:56:56Z)

Dear gstoner,

Any inputs to resolve the above issue.

---

### 评论 #8 — gstoner (2017-06-28T13:00:35Z)

The driver loaded.    Can you compile a hip sample and see if runs, 

Next we need to load the developer release of OpenCL sudo apt-get install rocm rocm-opencl-dev
 
 

---

### 评论 #9 — muralimk51 (2017-06-28T13:22:15Z)

Dear gstoner,

I can compile hip as below :
1.
root@bdk:/opt/rocm/hip/samples/0_Intro/bit_extract# make
/opt/rocm/hip/bin/hipcc  bit_extract.cpp -o bit_extract

root@bdk:/opt/rocm/hip/samples/0_Intro/bit_extract# ls -alh
total 596K
drwxr-xr-x 2 root root 4.0K Jun 28 22:14 .
drwxr-xr-x 6 root root 4.0K Jun 28 19:38 ..
-rwxr-xr-x 1 root root 575K Jun 28 22:14 bit_extract
-rw-r--r-- 1 root root 3.5K Apr  5 00:54 bit_extract.cpp
-rw-r--r-- 1 root root  488 Apr  8 16:42 Makefile
-rw-r--r-- 1 root root  302 Apr  5 00:54 README.md

root@bdk:/opt/rocm/hip/samples/0_Intro/bit_extract# ./bit_extract 
<..no prints - cursor is not releasing>

2. 
root@bdk:/opt/rocm/hip/samples/0_Intro/square# make
/opt/rocm/hip/bin/hipcc  square.hipref.cpp -o square.hip.out

root@bdk:/opt/rocm/hip/samples/0_Intro/square# ls -alh
total 600K
drwxr-xr-x 2 root root 4.0K Jun 28 22:19 .
drwxr-xr-x 6 root root 4.0K Jun 28 19:38 ..
-rw-r--r-- 1 root root  323 Apr 27 18:52 Makefile
-rw-r--r-- 1 root root  592 Apr  5 00:54 README.md
-rw-r--r-- 1 root root 3.1K Apr  5 00:54 square.cu
-rwxr-xr-x 1 root root 575K Jun 28 22:19 square.hip.out
-rw-r--r-- 1 root root 3.3K Apr 27 18:52 square.hipref.cpp

root@bdk:/opt/rocm/hip/samples/0_Intro/square# ./square.hip.out 
<..no prints - cursor is not releasing>

3. Also installed "apt-get install rocm rocm-opencl-dev" but still facing the same issue as in comment:1

---

### 评论 #10 — jedwards-AMD (2017-06-28T15:18:53Z)

This looks like an issue is occurring when the runtime attempts to convert the code object into an executable for the device. Can you get a back trace of the hang?

---

### 评论 #11 — muralimk51 (2017-06-29T04:05:15Z)

Dear jedwards,
Thanks for your reply,  In above cases I am not seeing any hang issue.
But, When I execute "./clinfo" or "./bit_extract" or "./square.hip.out" I am not getting any prints -> Cursor is just blinking after this step.
When I do ctrl+c, cursor will get release.
Could you please let me know any other possibilities to find out the exact issue.


---

### 评论 #12 — gsedej (2017-06-29T22:53:02Z)

Not a dev here, but do you by any chance have any PPA enabled for graphics drivers (like OIBAF)?

Can you post `dmesg`output, after 1) restart computer 2) run samples and clinfo ?
You can install `pastebinit`and then just `dmesg | pastebinit`

---

### 评论 #13 — muralimk51 (2017-06-30T13:20:41Z)

Dear gsedej, jedwards, gstoner

Thanks for your help.  The above issue got resolved. 
Just I installed kernel headers first and kernel image next, I think kernel headers are not installed properly earlier.
I don't know how the above related to clinfo and luxmark, But now I am getting all correct results.

Thanks for your valuable time.

But Now I am facing two issues as below:
1. When I execute clinfo as below:
root@bdk:~# cd /opt/rocm/opencl/bin/x86_64/
root@bdk:/opt/rocm/opencl/bin/x86_64# ls
clang  clinfo  ld.lld  llc  llvm-link  llvm-objdump  opt
root@bdk:/opt/rocm/opencl/bin/x86_64# ./clinfo
...
It's listing for  only "CL_DEVICE_TYPE_GPU"
I am not seeing entries for Device Type "CL_DEVICE_TYPE_CPU" , How to get this, Do I need to install any other package.

2. When I execute "luxmark-v3.1" For Hotel Lobby scene(mode: GPUs)  it's taking long time to pop out the image(picture) on Display window (OpenCL GPUs window)

Could you please let me know if any solution for this.

---

### 评论 #14 — gstoner (2017-07-01T21:49:22Z)

Can you try our new release here are updated instructions for installing 1.6  https://github.com/ROCm/ROCm.github.io/blob/master/ROCmInstall.md

We also have new install FAQ install issues you need to watch for and how to fix the issues. 
https://rocm.github.io/install_issues.html

---

### 评论 #15 — muralimk51 (2017-07-03T06:18:07Z)

Dear gstoner,
Thanks you. I will try installing 1.6, Thanks

---

### 评论 #16 — szellmann (2017-10-02T13:34:32Z)

Hi, I have similar problems to the ones the OP reported with running clinfo and vector_copy. When **not being root**, clinfo just hangs indefinitely. hsa vector_copy segfaults with the below stack trace when being run with user privileges. Both programs run just fine when being executed with root privileges (which I'd rather avoid..).

```
> gdb --args /opt/rocm/hsa/sample/vector_copy
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /opt/rocm/hsa/sample/vector_copy...(no debugging symbols found)...done.
(gdb) run
Starting program: /opt/rocm/hsa/sample/vector_copy 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff55f3700 (LWP 3265)]
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

Thread 1 "vector_copy" received signal SIGSEGV, Segmentation fault.
__GI_fseek (fp=0x0, offset=0, whence=2) at fseek.c:35
35      fseek.c: No such file or directory.
(gdb) thread apply all bt

Thread 2 (Thread 0x7ffff55f3700 (LWP 3265)):
#0  0x00007ffff7872f07 in ioctl () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007ffff75618a8 in ?? () from /opt/rocm/libhsakmt/lib/libhsakmt.so.1
#2  0x00007ffff755c2ec in hsaKmtWaitOnMultipleEvents () from /opt/rocm/libhsakmt/lib/libhsakmt.so.1
#3  0x00007ffff7b7ad14 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#4  0x00007ffff7b783e8 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#5  0x00007ffff7b509d7 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#6  0x00007ffff6f266ba in start_thread (arg=0x7ffff55f3700) at pthread_create.c:333
#7  0x00007ffff787d3dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 1 (Thread 0x7ffff7fa3740 (LWP 3259)):
#0  __GI_fseek (fp=0x0, offset=0, whence=2) at fseek.c:35
#1  0x0000000000401228 in load_module_from_file ()
#2  0x0000000000401883 in main ()
(gdb)
```
```
> dmesg | grep kfd
[    0.000000] Linux version 4.11.0-kfd-compute-rocm-rel-1.6-148 (jenkins@jenkins-raptor-5) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #1 SMP Wed Aug 23 12:00:35 CDT 2017
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.11.0-kfd-compute-rocm-rel-1.6-148 root=UUID=1c265fc8-a6ab-4158-afa9-07c046193295 ro
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.11.0-kfd-compute-rocm-rel-1.6-148 root=UUID=1c265fc8-a6ab-4158-afa9-07c046193295 ro
[    1.392440] usb usb1: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.400137] usb usb2: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.464910] usb usb3: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.469149] usb usb4: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.473489] usb usb5: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.477750] usb usb6: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-148 xhci-hcd
[    1.678889] kfd kfd: Initialized module
[    2.657572] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[    2.657768] kfd kfd: Reserved 2 pages for cwsr.
[    2.657817] kfd kfd: added device 1002:67df
```
```
> uname -a
Linux visamd 4.11.0-kfd-compute-rocm-rel-1.6-148 #1 SMP Wed Aug 23 12:00:35 CDT 2017 x86_64 x86_64 x86_64 GNU/Linux
```
```
>  cat /etc/issue
Ubuntu 16.04.3 LTS \n \l
```
```
> cat /proc/cpuinfo 
processor       : 0
vendor_id       : AuthenticAMD
cpu family      : 23
model           : 1
model name      : AMD Ryzen 7 1800X Eight-Core Processor
stepping        : 1
microcode       : 0x8001126
cpu MHz         : 2200.000
cache size      : 512 KB
physical id     : 0
siblings        : 16
core id         : 0
cpu cores       : 8
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_l2 mwaitx hw_pstate vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero irperf arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic overflow_recov succor smca
bugs            : fxsave_leak sysret_ss_attrs null_seg
bogomips        : 7186.16
TLB size        : 2560 4K pages
clflush size    : 64
cache_alignment : 64
address sizes   : 48 bits physical, 48 bits virtual
power management: ts ttp tm hwpstate eff_freq_ro [13] [14]
...
```
```
root:~# /opt/rocm/opencl/bin/x86_64/clinfo 
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.0 AMD-APP (2450.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Device 67df
  Device Topology:                               PCI[ B#39, D#0, F#0 ]
  Max compute units:                             36

...
```
```
> apt list --installed | grep rocm

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

linux-headers-4.11.0-kfd-compute-rocm-rel-1.6-148/Ubuntu 16.04,now 4.11.0-kfd-compute-rocm-rel-1.6-148-1 amd64 [installed,automatic]
linux-image-4.11.0-kfd-compute-rocm-rel-1.6-148/Ubuntu 16.04,now 4.11.0-kfd-compute-rocm-rel-1.6-148-1 amd64 [installed,automatic]
rocm/Ubuntu 16.04,now 1.6.148 amd64 [installed]
rocm-dev/Ubuntu 16.04,now 1.6.148 amd64 [installed,automatic]
rocm-device-libs/Ubuntu 16.04,now 0.0.1 amd64 [installed,automatic]
rocm-opencl/Ubuntu 16.04,now 1.2.0-1430311 amd64 [installed]
rocm-opencl-dev/Ubuntu 16.04,now 1.2.0-1430311 amd64 [installed]
rocm-profiler/Ubuntu 16.04,now 5.1.6400 amd64 [installed,automatic]
rocm-smi/Ubuntu 16.04,now 1.0.0-25-gbdb99b4 amd64 [installed,automatic]
rocm-utils/Ubuntu 16.04,now 1.0.0 amd64 [installed,automatic]
```

---
