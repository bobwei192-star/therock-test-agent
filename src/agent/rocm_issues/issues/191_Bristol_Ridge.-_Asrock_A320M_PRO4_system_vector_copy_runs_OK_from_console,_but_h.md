# Bristol Ridge.- Asrock A320M PRO4 system: vector_copy runs OK from console, but hangs in an ssh terminal

> **Issue #191**
> **状态**: closed
> **创建时间**: 2017-08-31T16:14:07Z
> **更新时间**: 2017-09-06T10:44:46Z
> **关闭时间**: 2017-09-06T10:41:29Z
> **作者**: jcoiner
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/191

## 描述

**EDIT: To summarize, disabling MSI interrupt mode caused a number of things to stop hanging.**

Has anyone seen this? I have vector_copy running OK in a local login console. When I ssh to the same machine, as the same user, running the same binary, it hangs after "Dispatching the kernel succeeded":

john@dash80:~/foo/sample$ ./vector_copy 
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx801.
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
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
^C

... until I CTRL-C it. These are the only differences in environment variables, they look innocuous to me:

$ diff env.broke env.ok
> HUSHLOGIN=FALSE
7,16d7
< LANGUAGE=en_US:en
< LC_ADDRESS=en_US.UTF-8
< LC_IDENTIFICATION=en_US.UTF-8
< LC_MEASUREMENT=en_US.UTF-8
< LC_MONETARY=en_US.UTF-8
< LC_NAME=en_US.UTF-8
< LC_NUMERIC=en_US.UTF-8
< LC_PAPER=en_US.UTF-8
< LC_TELEPHONE=en_US.UTF-8
< LC_TIME=en_US.UTF-8
30,33c21
< SSH_CLIENT=10.1.10.10 58700 22
< SSH_CONNECTION=10.1.10.10 58700 10.1.10.139 22
< SSH_TTY=/dev/pts/0
< TERM=xterm
---
> TERM=linux
38,39c26,29
< XDG_SESSION_COOKIE=82e17aa530f16aa39d3f90245120ccef-1504192969.909757-1513324773
< XDG_SESSION_ID=2
---
> XDG_SEAT=seat0
> XDG_SESSION_COOKIE=82e17aa530f16aa39d3f90245120ccef-1504192925.158758-1897242416
> XDG_SESSION_ID=1
> XDG_VTNR=1

Before I spend time on this, is it a known issue? This should work, right?

FWIW, after the hang, I can still run vector_copy at the local console and it runs fine. I can even run it at the console _while another vector_copy instance in the ssh is hanging_ and it runs fine on the console. So the GPU isn't getting completely hung; it's probably not a CP hang.

Thanks
John

---

## 评论 (21 条)

### 评论 #1 — jcoiner (2017-08-31T16:52:56Z)

ps. this is on a Bristol Ridge APU, Asrock A320M PRO4 with bios version 3.00, Ubuntu 16.04.3 with no X server running, and ROCm 1.6.

---

### 评论 #2 — gstoner (2017-09-02T12:03:10Z)

We never seen this,  SSH is the standard way we log into the system for ROCm, by default ROCm is designed to be headless.   We do not see this issue on Xeon E5, Core or EPYC based servers nor Desktop machine  I7 Extreme, Xeon E3, Core I7 Core i5, Ryzen and Threadripper system we work on mostly these days. 

Are you sure SSH is correctly configured?

---

### 评论 #3 — gstoner (2017-09-02T12:05:18Z)

Also, can you try clinfo instead 

---

### 评论 #4 — jcoiner (2017-09-02T14:04:48Z)

Thanks. The SSH config on both client and server are whatever Ubuntu gives you by default. Except sometimes I also enable X forwarding. With and without X forwarding made no difference.

'clinfo' reports identical text at the console and in a remote shell, except for the 'Platform ID' field. (The 'Platform ID' field value changes every time I run clinfo. It looks like it's printing a pointer value, maybe this is a bug?)

Here's the clinfo output:

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
  Board name:                                    AMD A8-9600 RADEON R7, 10 COMPUTE CORES 4C+6G
  Device Topology:                               PCI[ B#0, D#1, F#0 ]
  Max compute units:                             6
  Max work items dimensions:                     3
    Max work items[0]:                           256
    Max work items[1]:                           256
    Max work items[2]:                           256
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           900Mhz
  Address bits:                                  64
  Max memory allocation:                         268435456
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    39028
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            1073741824
  Constant buffer size:                          268435456
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            0
  Max pipe active reservations:                  0
  Max pipe packet size:                          0
  Max global variable size:                      268435456
  Max global variable preferred total size:      1073741824
  Max read/write image args:                     64
  Max on device events:                          0
  Queue on device max size:                      0
  Max on device queues:                          0
  Queue on device preferred size:                0
  SVM capabilities:                              
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           Yes
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            1
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:                                
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:                              
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:                            
    Out-of-Order:                                No
    Profiling :                                  No
  Platform ID:                                   0x7fa6a0802598
  Name:                                          gfx801
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0 
  Driver version:                                1.1 (HSA,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2 
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_gl_sharing cl_amd_media_ops cl_amd_media_ops2 cl_khr_subgroups cl_khr_depth_images cl_amd_liquid_flash cl_amd_copy_buffer_p2p 

Do you have any tips on how to debug something like this? Are there tracing facilities in the runtime, thunk or kernel module?


---

### 评论 #5 — gstoner (2017-09-02T14:08:05Z)

Sounds more like issue in the base Linux kernel of Linux kernel graphics driver, since the userland is working fine on the console 

---

### 评论 #6 — gstoner (2017-09-02T14:09:10Z)

Can you run hip or HCC app  while running  SSH

---

### 评论 #7 — jcoiner (2017-09-02T14:17:37Z)

Another data point: I can get the hang at the console, just by piping the output to a file.

This runs ok at the console:  > ./vector_copy
and this hangs:  > ./vector_copy >& log
and this hangs:  > ./vector_copy > log
and this runs ok:  > ./vector_copy 2>&1

Crazy! Something is sensitive to exactly which pty or tty (??) the stdout is plumbed into.

---

### 评论 #8 — jcoiner (2017-09-02T14:30:44Z)

The kernel is the ROCK kernel, compiled from source checked out from github about two days ago.

This hang was also happening with the stock ROCm 1.6 kernel. If you'd rather support that one, I could certainly switch back to it. Compiling from source didn't seem to help or hurt things. I haven't recompiled any other components yet, everything else is ROCm 1.6 off-the-shelf. (At least it should be. AMDGPU PRO was installed previously, and I wiped it. ldd confirms that only rocm libs are getting pulled into vector_copy)

---

### 评论 #9 — jcoiner (2017-09-02T14:36:14Z)

Strace on the hanging and nonhanging vector_copies shows some differences that happen somewhat earlier than the actual hang. The earliest diff is this:

open("/dev/shm/sem.hsakmt_semaphore", O_RDWR|O_NOFOLLOW) = 4   // will run ok
 vs.
open("/dev/shm/sem.hsakmt_semaphore", O_RDWR|O_NOFOLLOW) = -1 ENOENT (No such file or directory)   // will go on to hang!

Everything else up to that point looked identical (ignoring the huge volume of pointer differences.)


---

### 评论 #10 — jcoiner (2017-09-02T14:48:03Z)

This is the 'square' HIP app, it produces the same result in either VNC or at the console:

john@dash80:~/foo/square$ make
make: Nothing to be done for 'all'.
john@dash80:~/foo/square$ ./square.hip.out 
info: running on device AMD A8-9600 RADEON R7, 10 COMPUTE CORES 4C+6G
info: architecture on AMD GPU device is: 801
info: allocate host mem (  7.63 MB)
info: allocate device mem (  7.63 MB)
info: copy Host2Device
info: launch 'vector_square' kernel
info: copy Device2Host
Segmentation fault

Hmm, let's try another sample...

john@dash80:~/foo$ cp -R /opt/rocm/hip/samples/2_Cookbook/0_MatrixTranspose .
john@dash80:~/foo$ cd 0_MatrixTranspose/
john@dash80:~/foo/0_MatrixTranspose$ 
john@dash80:~/foo/0_MatrixTranspose$ make
/opt/rocm/hip/bin/hipcc -g   -c -o MatrixTranspose.o MatrixTranspose.cpp
/opt/rocm/hip/bin/hipcc MatrixTranspose.o -o MatrixTranspose
./MatrixTranspose
Device name AMD A8-9600 RADEON R7, 10 COMPUTE CORES 4C+6G
Makefile:29: recipe for target 'test' failed
make: *** [test] Segmentation fault

Is there a better sample than these? I'm just poking around /opt/rocm and picking samples at random.

Compiling 'square' for debug and running in gdb shows this stack trace:

#0  0x00007ffff6f84ec6 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#1  0x00007ffff6f8510a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2  0x00007ffff467a68c in waitComplete ()
    at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:3721
#3  0x00007ffff467b75d in operator() ()
    at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:3819
#4  _M_invoke<> ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1530
#5  operator() ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1520
#6  operator() ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1342
#7  0x00007ffff467b6f2 in _M_invoke ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1856
#8  0x00007ffff467b667 in operator() ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:2267
#9  _M_do_set ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:527
#10 0x00007ffff7416a99 in __pthread_once_slow (once_control=0xc56288, 
    init_routine=0x7ffff65e9ac0 <__once_proxy>) at pthread_once.c:116
#11 0x00007ffff467bc4b in __gthread_once ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/x86_64-linux-gnu/c++/5.4.0/bits/gthr-default.h:699
#12 call_once<void (std::__future_base::_State_baseV2::*)(std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *), std::__future_base::_State_baseV2 *, std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *> ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/mutex:738
#13 _M_set_result ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:386
#14 _M_complete_async ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1606
#15 0x00007ffff46685b6 in wait ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:319
#16 wait ()
    at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:656
#17 wait ()
    at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:1148
#18 0x00007ffff4669834 in copy_ext ()
    at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:3345
#19 0x00007ffff7b53a5b in ihipStream_t::locked_copySync(void*, void const*, unsigned long, unsigned int, bool) () from /opt/rocm/hip/lib/libhip_hcc.so
#20 0x00007ffff7b7b0bf in hipMemcpy () from /opt/rocm/hip/lib/libhip_hcc.so
#21 0x000000000041e41d in main (argc=1, argv=0x7fffffffe208) at square.hipref.cpp:90






---

### 评论 #11 — gstoner (2017-09-02T14:48:56Z)

Try and HCC sample

Greg
On Sep 2, 2017, at 9:48 AM, jcoiner <notifications@github.com<mailto:notifications@github.com>> wrote:


This is the 'square' HIP app, it produces the same result in either VNC or at the console:

john@dash80:/foo/square$ make
make: Nothing to be done for 'all'.
john@dash80:/foo/square$ ./square.hip.out
info: running on device AMD A8-9600 RADEON R7, 10 COMPUTE CORES 4C+6G
info: architecture on AMD GPU device is: 801
info: allocate host mem ( 7.63 MB)
info: allocate device mem ( 7.63 MB)
info: copy Host2Device
info: launch 'vector_square' kernel
info: copy Device2Host
Segmentation fault

Hmm, let's try another sample...

john@dash80:/foo$ cp -R /opt/rocm/hip/samples/2_Cookbook/0_MatrixTranspose .
john@dash80:/foo$ cd 0_MatrixTranspose/
john@dash80:/foo/0_MatrixTranspose$
john@dash80:/foo/0_MatrixTranspose$ make
/opt/rocm/hip/bin/hipcc -g -c -o MatrixTranspose.o MatrixTranspose.cpp
/opt/rocm/hip/bin/hipcc MatrixTranspose.o -o MatrixTranspose
./MatrixTranspose
Device name AMD A8-9600 RADEON R7, 10 COMPUTE CORES 4C+6G
Makefile:29: recipe for target 'test' failed
make: *** [test] Segmentation fault

Is there a better sample than these? I'm just poking around /opt/rocm and picking samples at random.

Compiling 'square' for debug and running in gdb shows this stack trace:

#0 0x00007ffff6f84ec6 in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#1<https://github.com/RadeonOpenCompute/ROCm/pull/1> 0x00007ffff6f8510a in ?? () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
#2<https://github.com/RadeonOpenCompute/ROCm/pull/2> 0x00007ffff467a68c in waitComplete ()
at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:3721
#3<https://github.com/RadeonOpenCompute/ROCm/issues/3> 0x00007ffff467b75d in operator() ()
at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:3819
#4<https://github.com/RadeonOpenCompute/ROCm/issues/4> _M_invoke<> ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1530
#5<https://github.com/RadeonOpenCompute/ROCm/pull/5> operator() ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1520
#6<https://github.com/RadeonOpenCompute/ROCm/issues/6> operator() ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1342
#7<https://github.com/RadeonOpenCompute/ROCm/issues/7> 0x00007ffff467b6f2 in _M_invoke ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:1856
#8<https://github.com/RadeonOpenCompute/ROCm/issues/8> 0x00007ffff467b667 in operator() ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/functional:2267
#9<https://github.com/RadeonOpenCompute/ROCm/pull/9> _M_do_set ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:527
#10<https://github.com/RadeonOpenCompute/ROCm/issues/10> 0x00007ffff7416a99 in __pthread_once_slow (once_control=0xc56288,
init_routine=0x7ffff65e9ac0 <__once_proxy>) at pthread_once.c:116
#11<https://github.com/RadeonOpenCompute/ROCm/issues/11> 0x00007ffff467bc4b in __gthread_once ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/x86_64-linux-gnu/c++/5.4.0/bits/gthr-default.h:699
#12<https://github.com/RadeonOpenCompute/ROCm/issues/12> call_once<void (std::__future_base::_State_baseV2::*)(std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> *, bool *), std::__future_base::_State_baseV2 *, std::function<std::unique_ptr<std::__future_base::_Result_base, std::__future_base::_Result_base::_Deleter> ()> , bool > ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/mutex:738
#13<https://github.com/RadeonOpenCompute/ROCm/issues/13> _M_set_result ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:386
#14<https://github.com/RadeonOpenCompute/ROCm/pull/14> _M_complete_async ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:1606
#15<https://github.com/RadeonOpenCompute/ROCm/issues/15> 0x00007ffff46685b6 in wait ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:319
#16<https://github.com/RadeonOpenCompute/ROCm/issues/16> wait ()
at /usr/lib/gcc/x86_64-linux-gnu/5.4.0/../../../../include/c++/5.4.0/future:656
#17<https://github.com/RadeonOpenCompute/ROCm/issues/17> wait ()
at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:1148
#18<https://github.com/RadeonOpenCompute/ROCm/issues/18> 0x00007ffff4669834 in copy_ext ()
at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/external/hcc-tot/lib/hsa/mcwamp_hsa.cpp:3345
#19<https://github.com/RadeonOpenCompute/ROCm/pull/19> 0x00007ffff7b53a5b in ihipStream_t::locked_copySync(void, void const, unsigned long, unsigned int, bool) () from /opt/rocm/hip/lib/libhip_hcc.so
#20<https://github.com/RadeonOpenCompute/ROCm/pull/20> 0x00007ffff7b7b0bf in hipMemcpy () from /opt/rocm/hip/lib/libhip_hcc.so
#21<https://github.com/RadeonOpenCompute/ROCm/issues/21> 0x000000000041e41d in main (argc=1, argv=0x7fffffffe208) at square.hipref.cpp:90

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/191#issuecomment-326748538>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuUTkEegrA9TxKJZr2dmF5uK2_oyTks5seWqlgaJpZM4PJEad>.



---

### 评论 #12 — jcoiner (2017-09-02T14:54:21Z)

Is there an HCC sample within the ROCm source tree or under /opt? I'm looking...

---

### 评论 #13 — gstoner (2017-09-02T14:56:59Z)

Just try this. https://github.com/RadeonOpenCompute/hcc/tree/clang_tot_upgrade/benchmarks/benchEmptyKernel


https://github.com/ROCm-Developer-Tools/HCC-Example-Application/tree/master/SyncVsAsyncArrayCopy


HIP I would try HIPinfo


Greg
On Sep 2, 2017, at 9:54 AM, jcoiner <notifications@github.com<mailto:notifications@github.com>> wrote:


Is there an HCC sample within the ROCm source tree or under /opt? I'm looking...

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/191#issuecomment-326748914>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuawytB91avA1Px9e4xY-hs5_NDddks5seWwegaJpZM4PJEad>.



---

### 评论 #14 — jcoiner (2017-09-02T15:13:12Z)

Thanks. I found ./hcc/benchmarks/benchEmptyKernel in the git checkout of ROCm. Copied it, compiled it. Result:

john@dash80:~/foo/benchEmptyKernel$ ./bench 

Iterations per test:              10000
Bursts (#dispatches before sync): 1

        pfe time, active (us):                  11.543153
        pfe time, blocked (us):                 11.683086
        grid_launch time, active (us):          13.487871
        grid_launch time, blocked (us):         13.483976
could not open code object './nullkernel-gfx803.hsaco'
bench: hsacodelib.CPP:25: Kernel load_hsaco(hc::accelerator_view *, const char *, const char *): Assertion `0' failed.
Aborted

Hmm, maybe a symlink will fix this?

john@dash80:~/foo/benchEmptyKernel$ ln -s nullkernel-gfx801.hsaco nullkernel-gfx803.hsaco
john@dash80:~/foo/benchEmptyKernel$ ./bench 

Iterations per test:              10000
Bursts (#dispatches before sync): 1

        pfe time, active (us):                  11.504269
        pfe time, blocked (us):                 11.675636
        grid_launch time, active (us):          13.435274
        grid_launch time, blocked (us):         13.462351
dispatch_hsa_kernel+withcompletion+activewait : 11.45826
dispatch_hsa_kernel+nocompletion+activewait   : 14.187812
john@dash80:~/foo/benchEmptyKernel$ echo $?
0

I don't know how to interpret those numbers, but it didn't print an obvious error and the exit code was 0 so I guess that's ok? This ran in a VNC where the vector_copy normally hangs.


---

### 评论 #15 — jcoiner (2017-09-04T15:01:31Z)

A data point: in InterruptSignal::WaitRelaxed(), increasing the kMaxElapsed timeout from 200uS to 200mS allows vector_copy to pass in an ssh terminal or in a VNC (both contexts where it hung before.)

Passing cases never reach the blocking hsaKmtWaitOnEvent() call in WaitRelaxed(), they find the value they're waiting for in the polling loop. Failing cases time out while polling, call hsaKmtWaitOnEvent() to block, and this never returns.

I guess there's nothing special about the ssh terminal, except probably timings shake out a bit differently exposing a race condition. This probably means the GPU is never hanging, and the race is purely host-side.

If I rewrite WaitRelaxed() to always block, this always hangs, at least for me:
```
hsa_signal_value_t InterruptSignal::WaitRelaxed(
    hsa_signal_condition_t condition, hsa_signal_value_t compare_value,
    uint64_t timeout, hsa_wait_state_t wait_hint) {
  uint32_t prior = atomic::Increment(&waiting_);

  // assert(prior == 0 && "Multiple waiters on interrupt signal!");
  // Allow only the first waiter to sleep (temporary, known to be bad).
  if (prior != 0) wait_hint = HSA_WAIT_STATE_ACTIVE;

  MAKE_SCOPE_GUARD([&]() { atomic::Decrement(&waiting_); });

  int64_t value;

  timer::fast_clock::time_point start_time = timer::fast_clock::now();

  uint64_t hsa_freq;
  HSA::hsa_system_get_info(HSA_SYSTEM_INFO_TIMESTAMP_FREQUENCY, &hsa_freq);
  const timer::fast_clock::duration fast_timeout =
      timer::duration_from_seconds<timer::fast_clock::duration>(
          double(timeout) / double(hsa_freq));

  bool condition_met = false;

  bool first = true;

  while (true) {
    if (invalid_) return 0;

    if (!first) {
        value = atomic::Load(&signal_.value, std::memory_order_relaxed);

        switch (condition) {
        case HSA_SIGNAL_CONDITION_EQ: {
            condition_met = (value == compare_value);
            break;
        }
        case HSA_SIGNAL_CONDITION_NE: {
            condition_met = (value != compare_value);
            break;
        }
        case HSA_SIGNAL_CONDITION_GTE: {
            condition_met = (value >= compare_value);
            break;
        }
        case HSA_SIGNAL_CONDITION_LT: {
            condition_met = (value < compare_value);
            break;
        }
        default:
            return 0;
        }
        if (condition_met) {
            return hsa_signal_value_t(value);
        }
    }
    first = false;

    timer::fast_clock::time_point time = timer::fast_clock::now();
    if (time - start_time > fast_timeout) {
      value = atomic::Load(&signal_.value, std::memory_order_relaxed);
      return hsa_signal_value_t(value);
    }
    
    if (wait_hint == HSA_WAIT_STATE_ACTIVE) {
      continue;
    }

    uint32_t wait_ms;
    auto time_remaining = fast_timeout - (time - start_time);
    uint64_t ct=timer::duration_cast<std::chrono::milliseconds>(
      time_remaining).count();
    wait_ms = (ct>0xFFFFFFFEu) ? 0xFFFFFFFEu : ct;
    hsaKmtWaitOnEvent(event_, wait_ms);
  }
}
```

---

### 评论 #16 — jcoiner (2017-09-05T19:02:06Z)

I think something goes wrong during interrupts setup on this system.

From adding pr_debug statements to the amdkfd module, it appears that kfd_signal_event_interrupt() never gets called in the hanging case. I believe we expect this to be called when the GPU signals the event.

Digging deeper, I'm getting this sequence of kernel messages. This is an edited subset of my dmesg; I removed a bunch of intervening messages that seemed irrelevant:

[    2.943868] amdgpu 0000:00:01.0: amdgpu: using MSI.
[    2.943893] [drm] amdgpu: irq initialized.
[    2.944440] JPC BOZO enabled compute eop on pipe 0
[    2.945000] JPC BOZO gfx_v8_0_kiq_set_interrupt_state() enable on ME 2
[    2.946842] JPC BOZO cz_ih_disable_interrupts
[    2.946849] JPC BOZO cz_ih_enable_interrupts
[    2.946849] JPC BOZO did cz_ih_irq_init
[    5.444193] JPC BOZO in amdgpu_enable_vblank_kms, type = 0, returns 0
[    6.127721] JPC BOZO 1/60 processing IH interrupt in amdgpu_ih_process
[    6.127724] JPC BOZO 1/60 calling amdgpu_amdkfd_interrupt in amdgpu_ih_process
   // ^^ these repeat every second until vblank is disabled. The "1/60" means I'm only printing once per 60 calls. So we're really getting a 60hz interrupt, probably for vblank
[   10.719634] JPC BOZO in amdgpu_disable_vblank_kms, type = 0
[   15.706926] JPC BOZO in amdgpu_enable_vblank_kms, type = 0, returns 0
[   16.119758] JPC BOZO 1/60 processing IH interrupt in amdgpu_ih_process
[   16.119764] JPC BOZO 1/60 calling amdgpu_amdkfd_interrupt in amdgpu_ih_process
   // ^^ again these repeat every second until vblank disabled again
[   22.236073] JPC BOZO in amdgpu_disable_vblank_kms, type = 0
[   41.082023] JPC BOZO in amdgpu_enable_vblank_kms, type = 0, returns 0
[   41.091431] do_IRQ: 0.147 No irq handler for vector
[   41.137110] ------------[ cut here ]------------
[   41.137130] WARNING: CPU: 2 PID: 1448 at drivers/gpu/drm/drm_atomic_helper.c:1122 drm_atomic_helper_wait_for_vblanks.part.16+0x25f/0x270 [drm_kms_helper]
[   41.137131] [CRTC:40] vblank wait timed out

The 'JPC BOZO' messages are ones I added. What appears to be happening is that the first two times vblank interrupt is enabled, we get a stream of 60hz interrupts as expected. The 3rd time that the kernel tries to enable vblank, we get a scary "No irq handler for vector" message and then we never get another interrupt from the gfx core again. (And the gfx core isn't hung; the vector_copy still passes if I force it to poll only.)

I tried booting with pci=nomsi,noaer to rule out MSI problems, but that panicked on boot before even mounting the root filesystem. So I haven't ruled out MSI problems yet.

In other news, this system's console behaves oddly. It takes several seconds to ALT-F[n] to another virtual terminal, and it also takes several seconds to wake up from sleep. Once it wakes up or switches terminals, it's responsive like normal. When the console wakes up from these multi-second comas, there are new messages in dmesg about "vblank wait timed out", and new messages on the console about "flip_done timed out". At first I thought that was unrelated to OpenCL program hangs, but now I'm thinking maybe a single problem with interrupts setup is causing a spectrum of troubles.


---

### 评论 #17 — jcoiner (2017-09-05T19:29:44Z)

Disabling MSI support in the amdgpu driver (but not for the whole kernel) allows vector_copy to run reliably! I'm finally seeing the kfd_signal_event_interrupt() calls which wake the user process up from a call to hsaKmtWaitOnEvent().

This is how I disabled MSI:

```
diff --git a/drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c b/drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c
index cf5dfdb..67549ae 100644
--- a/drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c
+++ b/drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c
@@ -208,7 +208,9 @@ static bool amdgpu_msi_ok(struct amdgpu_device *adev)
        else if (amdgpu_msi == 0)
                return false;
 
-       return true;
+        // JPC BOZO change MSI default to false
+        pr_debug("JPC BOZO default MSI to false!\n");
+       return false;//true;
 }
```

... which is the wrong way to do it, as there's also a kernel module option, if I only knew how to set that...

This raises questions: is there a bug in amdgpu interrupts setup on Bristol Ridge, is it a BIOS bug, or something else? I know nothing about interrupts setup, I'm just pattern-matching my way through here so I'll probably stop debugging this now and go ahead with disabling MSI as a workaround.


---

### 评论 #18 — jcoiner (2017-09-05T20:04:39Z)

Disabling MSI in amdgpu also fixes the trouble with laggy virtual console switching, it's now instantaneous like it should be.

---

### 评论 #19 — gstoner (2017-09-05T20:09:25Z)

Do you know if IOMMUv2 is enabled in your SBIOS. 

---

### 评论 #20 — jcoiner (2017-09-05T23:14:36Z)

Yes, IOMMUv2 is enabled in the BIOS and recognized at kernel startup.

```
john@dash80:~$ dmesg | grep -i iommu
[    1.256370] AMD-Vi: IOMMU performance counters supported
[    1.256892] iommu: Adding device 0000:00:01.0 to group 0
[    1.256985] iommu: Using direct mapping for device 0000:00:01.0
[    1.257059] iommu: Adding device 0000:00:02.0 to group 1
[    1.257079] iommu: Adding device 0000:00:02.4 to group 1
[    1.257216] iommu: Adding device 0000:00:03.0 to group 2
[    1.257354] iommu: Adding device 0000:00:08.0 to group 3
[    1.257501] iommu: Adding device 0000:00:09.0 to group 4
[    1.257518] iommu: Adding device 0000:00:09.2 to group 4
[    1.257661] iommu: Adding device 0000:00:10.0 to group 5
[    1.257802] iommu: Adding device 0000:00:11.0 to group 6
[    1.257944] iommu: Adding device 0000:00:12.0 to group 7
[    1.258096] iommu: Adding device 0000:00:14.0 to group 8
[    1.258114] iommu: Adding device 0000:00:14.3 to group 8
[    1.258285] iommu: Adding device 0000:00:18.0 to group 9
[    1.258303] iommu: Adding device 0000:00:18.1 to group 9
[    1.258322] iommu: Adding device 0000:00:18.2 to group 9
[    1.258339] iommu: Adding device 0000:00:18.3 to group 9
[    1.258356] iommu: Adding device 0000:00:18.4 to group 9
[    1.258373] iommu: Adding device 0000:00:18.5 to group 9
[    1.258392] iommu: Adding device 0000:05:00.0 to group 1
[    1.258405] iommu: Adding device 0000:05:00.1 to group 1
[    1.258417] iommu: Adding device 0000:05:00.2 to group 1
[    1.258432] iommu: Adding device 0000:06:04.0 to group 1
[    1.258447] iommu: Adding device 0000:06:06.0 to group 1
[    1.258461] iommu: Adding device 0000:06:07.0 to group 1
[    1.258482] iommu: Adding device 0000:09:00.0 to group 1
[    1.259032] AMD-Vi: Found IOMMU at 0000:00:00.2 cap 0x40
[    1.261943] perf: amd_iommu: Detected. (0 banks, 0 counters/bank)
[    2.773448] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[   38.122229] vboxpci: IOMMU found
```

Also Xorg started working now that interrupt setup is working better with MSI disabled. Formerly X hung almost immediately on startup, now it's working well under ROCm.

---

### 评论 #21 — jcoiner (2017-09-06T10:41:29Z)

Interestingly, the MSI mode bit is only used in 3 places in amdgpu. It gates the call to pci_enable_msi() in amdgpu_irq_init(), and the corresponding call to pci_disable_msi() in amdgpu_irq_fini().

Also it shows up in this code in cz_ih_irq_init() [and the corresponding functions for other chips]:

```
	/* Default settings for IH_CNTL (disabled at first) */
	ih_cntl = RREG32(mmIH_CNTL);
	ih_cntl = REG_SET_FIELD(ih_cntl, IH_CNTL, MC_VMID, 0);

	if (adev->irq.msi_enabled)
		ih_cntl = REG_SET_FIELD(ih_cntl, IH_CNTL, RPTR_REARM, 1);
	WREG32(mmIH_CNTL, ih_cntl);
```
That looks a little suspicious. If we want to set RPTR_REARM when msi=1, do we want to clear it when msi=0? Or should it always be 1? Either way we could remove the conditional.

There are no other uses of the msi bit in amdgpu or amdkfd. Whatever goes wrong when msi is enabled, the problem is likely outside the ROCm drivers. Let's close this, it seems out of scope for ROCM.

---
