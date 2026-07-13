# [Issue]: rocm-clinfo 6.2.0 segmentation fault

- **Issue #:** 3664
- **State:** closed
- **Created:** 2024-09-03T14:13:25Z
- **Updated:** 2024-10-07T15:28:21Z
- **Labels:** Under Investigation, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3664

### Problem Description

`rocm-clinfo` crashes.

Despite the GPU may not be any longer supported, rocm-clinfo should handle the exception without crashing.
Please remove `AMD Radeon VII` label, cause it was a random GPU I selected in the limited-choice menu concerning GPU type
```
OS:
NAME="Fedora Linux"
VERSION="40 (KDE Plasma)"

CPU: 
model name      : AMD Ryzen 5 3600 6-Core Processor

GPU:
  Name:                    AMD Ryzen 5 3600 6-Core Processor  
  Marketing Name:          AMD Ryzen 5 3600 6-Core Processor  
  Name:                    gfx803                             
  Marketing Name:          AMD Radeon RX 480 Graphics         
      Name:                    amdgcn-amd-amdhsa--gfx803 
```
```
# coredumpctl gdb 2050183
           PID: 2050183 (rocm-clinfo)
           UID: 1000 (user)
           GID: 1000 (user)
        Signal: 11 (SEGV)
     Timestamp: Tue 2024-09-03 16:01:21 CEST (2min 49s ago)
  Command Line: rocm-clinfo
    Executable: /usr/bin/rocm-clinfo
 Control Group: /user.slice/user-1000.slice/user@1000.service/app.slice/app-org.kde.yakuake@autostart.service
          Unit: user@1000.service
     User Unit: app-org.kde.yakuake@autostart.service
         Slice: user-1000.slice
     Owner UID: 1000 (user)
       Boot ID: 31dd572ef5774add8ec96d9b45ea797d
    Machine ID: 56106060e6fd4ce59080ab83290e52dc
      Hostname: machine
       Storage: /var/lib/systemd/coredump/core.rocm-clinfo.1000.31dd572ef5774add8ec96d9b45ea797d.2050183.1725372081000000.zst (present)
  Size on Disk: 1.6M
       Package: rocclr/6.2.0-1.fc40
      build-id: 1fe1a0ad46b8199df7fac9014d376c6be119c14a
       Message: Process 2050183 (rocm-clinfo) of user 1000 dumped core.
                
                Module libhsakmt.so.1 from rpm hsakmt-1.0.6-41.rocm6.2.0.fc40.x86_64
                Module libnuma.so.1 from rpm numactl-2.0.16-5.fc40.x86_64
                Module libhsa-runtime64.so.1 from rpm rocm-runtime-6.2.0-2.fc40.x86_64
                Module libamd_comgr.so.2 from rpm rocm-compilersupport-18-2.rocm6.2.0.fc40.x86_64
                Module libSPIRV-Tools-link.so from rpm spirv-tools-2024.3-2.fc40.x86_64
                Module libSPIRV-Tools.so from rpm spirv-tools-2024.3-2.fc40.x86_64
                Module libSPIRV-Tools-opt.so from rpm spirv-tools-2024.3-2.fc40.x86_64
                Module libLLVMSPIRVLib.so.18.1 from rpm spirv-llvm-translator-18.1.2-1.fc40.x86_64
                Module libRusticlOpenCL.so.1 from rpm mesa-24.1.6-1.fc40.x86_64
                Module libdrm_amdgpu.so.1 from rpm libdrm-2.4.123-1.fc40.x86_64
                Module libdrm_radeon.so.1 from rpm libdrm-2.4.123-1.fc40.x86_64
                Module pipe_radeonsi.so from rpm mesa-24.1.6-1.fc40.x86_64
                Module libtinfo.so.6 from rpm ncurses-6.4-12.20240127.fc40.x86_64
                Module libedit.so.0 from rpm libedit-3.1-53.20240808cvs.fc40.x86_64
                Module libffi.so.8 from rpm libffi-3.4.4-7.fc40.x86_64
                Module libexpat.so.1 from rpm expat-2.6.2-1.fc40.x86_64
                Module libdrm.so.2 from rpm libdrm-2.4.123-1.fc40.x86_64
                Module libelf.so.1 from rpm elfutils-0.191-4.fc40.x86_64
                Module libzstd.so.1 from rpm zstd-1.5.6-1.fc40.x86_64
                Module libz.so.1 from rpm zlib-ng-2.1.7-1.fc40.x86_64
                Module libMesaOpenCL.so.1 from rpm mesa-24.1.6-1.fc40.x86_64
                Module libOpenCL.so.1 from rpm ocl-icd-2.3.2-6.fc40.x86_64
                Module rocm-clinfo from rpm rocclr-6.2.0-1.fc40.x86_64
                Stack trace of thread 2050183:
                #0  0x00007f76b617cb49 __memset_avx2_unaligned_erms (libc.so.6 + 0x16db49)
                #1  0x00007f76a0838860 _ZNK4rocr3AMD8GpuAgent14AssembleShaderEPKcNS1_14AssembleTargetERPvRm (libhsa-runtime64.so.1 + 0x38860)
                #2  0x00007f76a083a92b _ZN4rocr3AMD8GpuAgent13PostToolsInitEv (libhsa-runtime64.so.1 + 0x3a92b)
                #3  0x00007f76a0851b9d _ZN4rocr3HSA8hsa_initEv (libhsa-runtime64.so.1 + 0x51b9d)
                #4  0x00007f76a99505d4 _ZN3amd3roc6Device4initEv (libamdocl64.so.6.2 + 0xb85d4)
                #5  0x00007f76a99b2863 _ZN3amd6Device4initEv (libamdocl64.so.6.2 + 0x11a863)
                #6  0x00007f76a991d14d _ZZNSt9once_flag18_Prepare_executionC4IZSt9call_onceIZ22clIcdGetPlatformIDsKHREUlvE_JEEvRS_OT_DpOT0_EUlvE_EERS5_ENUlvE_4_FUNEv (libamdocl64.so.6.2 + 0x8514d)
                #7  0x00007f76b60aba4b __pthread_once_slow (libc.so.6 + 0x9ca4b)
                #8  0x00007f76b60abab9 ___pthread_once (libc.so.6 + 0x9cab9)
                #9  0x00007f76a991cfae __gthread_once (libamdocl64.so.6.2 + 0x84fae)
                #10 0x00007f76b65d9465 _find_and_check_platforms (libOpenCL.so.1 + 0xd465)
                #11 0x00007f76b65db68c _initClIcd (libOpenCL.so.1 + 0xf68c)
                #12 0x0000561bdba113b0 _ZN2cl8Platform3getEPSt6vectorIS0_SaIS0_EE (rocm-clinfo + 0xc3b0)
                #13 0x0000561bdba085be main (rocm-clinfo + 0x35be)
                #14 0x00007f76b6039088 __libc_start_call_main (libc.so.6 + 0x2a088)
                #15 0x00007f76b603914b __libc_start_main_impl (libc.so.6 + 0x2a14b)
                #16 0x0000561bdba0eaa5 _start (rocm-clinfo + 0x9aa5)
                
                Stack trace of thread 2050185:
                #0  0x00007f76b60a2da9 __futex_abstimed_wait_common64 (libc.so.6 + 0x93da9)
                #1  0x00007f76b60a57f9 __pthread_cond_wait_common (libc.so.6 + 0x967f9)
                #2  0x00007f76a9f57a9d cnd_wait (pipe_radeonsi.so + 0x157a9d)
                #3  0x00007f76a9f3aa0b util_queue_thread_func (pipe_radeonsi.so + 0x13aa0b)
                #4  0x00007f76a9f579fc impl_thrd_routine (pipe_radeonsi.so + 0x1579fc)
                #5  0x00007f76b60a66d7 start_thread (libc.so.6 + 0x976d7)
                #6  0x00007f76b612a60c __clone3 (libc.so.6 + 0x11b60c)
                
                Stack trace of thread 2050184:
                #0  0x00007f76b60a2da9 __futex_abstimed_wait_common64 (libc.so.6 + 0x93da9)
                #1  0x00007f76b60a57f9 __pthread_cond_wait_common (libc.so.6 + 0x967f9)
                #2  0x00007f76a9f57a9d cnd_wait (pipe_radeonsi.so + 0x157a9d)
                #3  0x00007f76a9f3aa0b util_queue_thread_func (pipe_radeonsi.so + 0x13aa0b)
                #4  0x00007f76a9f579fc impl_thrd_routine (pipe_radeonsi.so + 0x1579fc)
                #5  0x00007f76b60a66d7 start_thread (libc.so.6 + 0x976d7)
                #6  0x00007f76b612a60c __clone3 (libc.so.6 + 0x11b60c)
                
                Stack trace of thread 2050187:
                #0  0x00007f76b60a2da9 __futex_abstimed_wait_common64 (libc.so.6 + 0x93da9)
                #1  0x00007f76b60a57f9 __pthread_cond_wait_common (libc.so.6 + 0x967f9)
                #2  0x00007f76a9f57a9d cnd_wait (pipe_radeonsi.so + 0x157a9d)
                #3  0x00007f76a9f3aa0b util_queue_thread_func (pipe_radeonsi.so + 0x13aa0b)
                #4  0x00007f76a9f579fc impl_thrd_routine (pipe_radeonsi.so + 0x1579fc)
                #5  0x00007f76b60a66d7 start_thread (libc.so.6 + 0x976d7)
                #6  0x00007f76b612a60c __clone3 (libc.so.6 + 0x11b60c)
                
                Stack trace of thread 2050189:
                #0  0x00007f76b60a2da9 __futex_abstimed_wait_common64 (libc.so.6 + 0x93da9)
                #1  0x00007f76b60a57f9 __pthread_cond_wait_common (libc.so.6 + 0x967f9)
                #2  0x00007f76a9f57a9d cnd_wait (pipe_radeonsi.so + 0x157a9d)
                #3  0x00007f76a9f3aa0b util_queue_thread_func (pipe_radeonsi.so + 0x13aa0b)
                #4  0x00007f76a9f579fc impl_thrd_routine (pipe_radeonsi.so + 0x1579fc)
                #5  0x00007f76b60a66d7 start_thread (libc.so.6 + 0x976d7)
                #6  0x00007f76b612a60c __clone3 (libc.so.6 + 0x11b60c)
                
                Stack trace of thread 2050186:
                #0  0x00007f76b60a2da9 __futex_abstimed_wait_common64 (libc.so.6 + 0x93da9)
                #1  0x00007f76b60a57f9 __pthread_cond_wait_common (libc.so.6 + 0x967f9)
                #2  0x00007f76a9f57a9d cnd_wait (pipe_radeonsi.so + 0x157a9d)
                #3  0x00007f76a9f3aa0b util_queue_thread_func (pipe_radeonsi.so + 0x13aa0b)
                #4  0x00007f76a9f579fc impl_thrd_routine (pipe_radeonsi.so + 0x1579fc)
                #5  0x00007f76b60a66d7 start_thread (libc.so.6 + 0x976d7)
                #6  0x00007f76b612a60c __clone3 (libc.so.6 + 0x11b60c)
                
                Stack trace of thread 2050188:
                #0  0x00007f76b60a2da9 __futex_abstimed_wait_common64 (libc.so.6 + 0x93da9)
                #1  0x00007f76b60a57f9 __pthread_cond_wait_common (libc.so.6 + 0x967f9)
                #2  0x00007f76a9f57a9d cnd_wait (pipe_radeonsi.so + 0x157a9d)
                #3  0x00007f76a9f3aa0b util_queue_thread_func (pipe_radeonsi.so + 0x13aa0b)
                #4  0x00007f76a9f579fc impl_thrd_routine (pipe_radeonsi.so + 0x1579fc)
                #5  0x00007f76b60a66d7 start_thread (libc.so.6 + 0x976d7)
                #6  0x00007f76b612a60c __clone3 (libc.so.6 + 0x11b60c)
                ELF object binary architecture: AMD x86-64

GNU gdb (Fedora Linux) 14.2-3.fc40
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /usr/bin/rocm-clinfo...
Reading symbols from /usr/lib/debug/usr/bin/rocm-clinfo-6.2.0-1.fc40.x86_64.debug...
[New LWP 2050183]
[New LWP 2050185]
[New LWP 2050184]
[New LWP 2050187]
[New LWP 2050189]
[New LWP 2050186]
[New LWP 2050188]

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.fedoraproject.org/>
Enable debuginfod for this session? (y or [n]) n
Debuginfod has been disabled.
To make this setting permanent, add 'set debuginfod enabled off' to .gdbinit.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
Core was generated by `rocm-clinfo'.
Program terminated with signal SIGSEGV, Segmentation fault.
--Type <RET> for more, q to quit, c to continue without paging--c
#0  __memset_avx2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memset-vec-unaligned-erms.S:246
246             VMOVU   %VMM(0), (%rdi)
[Current thread is 1 (Thread 0x7f76b64b5740 (LWP 2050183))]
(gdb) set height 0
(gdb) set print elements 0
(gdb) set print frame-arguments all
(gdb) thread apply all backtrace

Thread 7 (Thread 0x7f76a28006c0 (LWP 2050188)):
#0  0x00007f76b60a2da9 in __futex_abstimed_wait_common64 (private=0, futex_word=0x561bfb99f780, expected=0, op=393, abstime=0x0, cancel=true) at futex-internal.c:57
#1  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x561bfb99f780, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#2  0x00007f76b60a2e2f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x561bfb99f780, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0) at futex-internal.c:139
#3  0x00007f76b60a57f9 in __pthread_cond_wait_common (cond=0x561bfb99f758, mutex=<optimized out>, clockid=0, abstime=0x0) at pthread_cond_wait.c:503
#4  ___pthread_cond_wait (cond=0x561bfb99f758, mutex=<optimized out>) at pthread_cond_wait.c:618
#5  0x00007f76a9f57a9d in cnd_wait (cond=<optimized out>, mtx=<optimized out>) at ../src/c11/impl/threads_posix.c:135
#6  0x00007f76a9f3aa0b in util_queue_thread_func (input=input@entry=0x561bfb9e40f0) at ../src/util/u_queue.c:290
#7  0x00007f76a9f579fc in impl_thrd_routine (p=<optimized out>) at ../src/c11/impl/threads_posix.c:67
#8  0x00007f76b60a66d7 in start_thread (arg=<optimized out>) at pthread_create.c:447
#9  0x00007f76b612a60c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 6 (Thread 0x7f76a3e006c0 (LWP 2050186)):
#0  0x00007f76b60a2da9 in __futex_abstimed_wait_common64 (private=0, futex_word=0x561bfb911f08, expected=0, op=393, abstime=0x0, cancel=true) at futex-internal.c:57
#1  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x561bfb911f08, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#2  0x00007f76b60a2e2f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x561bfb911f08, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0) at futex-internal.c:139
#3  0x00007f76b60a57f9 in __pthread_cond_wait_common (cond=0x561bfb911ee0, mutex=<optimized out>, clockid=0, abstime=0x0) at pthread_cond_wait.c:503
#4  ___pthread_cond_wait (cond=0x561bfb911ee0, mutex=<optimized out>) at pthread_cond_wait.c:618
#5  0x00007f76a9f57a9d in cnd_wait (cond=<optimized out>, mtx=<optimized out>) at ../src/c11/impl/threads_posix.c:135
#6  0x00007f76a9f3aa0b in util_queue_thread_func (input=input@entry=0x561bfb9902a0) at ../src/util/u_queue.c:290
#7  0x00007f76a9f579fc in impl_thrd_routine (p=<optimized out>) at ../src/c11/impl/threads_posix.c:67
#8  0x00007f76b60a66d7 in start_thread (arg=<optimized out>) at pthread_create.c:447
#9  0x00007f76b612a60c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 5 (Thread 0x7f76a1e006c0 (LWP 2050189)):
#0  0x00007f76b60a2da9 in __futex_abstimed_wait_common64 (private=0, futex_word=0x561bfb9f2ee0, expected=0, op=393, abstime=0x0, cancel=true) at futex-internal.c:57
#1  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x561bfb9f2ee0, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#2  0x00007f76b60a2e2f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x561bfb9f2ee0, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0) at futex-internal.c:139
#3  0x00007f76b60a57f9 in __pthread_cond_wait_common (cond=0x561bfb9f2eb8, mutex=<optimized out>, clockid=0, abstime=0x0) at pthread_cond_wait.c:503
#4  ___pthread_cond_wait (cond=0x561bfb9f2eb8, mutex=<optimized out>) at pthread_cond_wait.c:618
#5  0x00007f76a9f57a9d in cnd_wait (cond=<optimized out>, mtx=<optimized out>) at ../src/c11/impl/threads_posix.c:135
#6  0x00007f76a9f3aa0b in util_queue_thread_func (input=input@entry=0x561bfba28e30) at ../src/util/u_queue.c:290
#7  0x00007f76a9f579fc in impl_thrd_routine (p=<optimized out>) at ../src/c11/impl/threads_posix.c:67
#8  0x00007f76b60a66d7 in start_thread (arg=<optimized out>) at pthread_create.c:447
#9  0x00007f76b612a60c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 4 (Thread 0x7f76a34006c0 (LWP 2050187)):
#0  0x00007f76b60a2da9 in __futex_abstimed_wait_common64 (private=0, futex_word=0x561bfb9120b8, expected=0, op=393, abstime=0x0, cancel=true) at futex-internal.c:57
#1  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x561bfb9120b8, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#2  0x00007f76b60a2e2f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x561bfb9120b8, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0) at futex-internal.c:139
#3  0x00007f76b60a57f9 in __pthread_cond_wait_common (cond=0x561bfb912090, mutex=<optimized out>, clockid=0, abstime=0x0) at pthread_cond_wait.c:503
#4  ___pthread_cond_wait (cond=0x561bfb912090, mutex=<optimized out>) at pthread_cond_wait.c:618
#5  0x00007f76a9f57a9d in cnd_wait (cond=<optimized out>, mtx=<optimized out>) at ../src/c11/impl/threads_posix.c:135
#6  0x00007f76a9f3aa0b in util_queue_thread_func (input=input@entry=0x561bfb9904e0) at ../src/util/u_queue.c:290
#7  0x00007f76a9f579fc in impl_thrd_routine (p=<optimized out>) at ../src/c11/impl/threads_posix.c:67
#8  0x00007f76b60a66d7 in start_thread (arg=<optimized out>) at pthread_create.c:447
#9  0x00007f76b612a60c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 3 (Thread 0x7f76a94006c0 (LWP 2050184)):
#0  0x00007f76b60a2da9 in __futex_abstimed_wait_common64 (private=0, futex_word=0x561bfb90da68, expected=0, op=393, abstime=0x0, cancel=true) at futex-internal.c:57
#1  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x561bfb90da68, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#2  0x00007f76b60a2e2f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x561bfb90da68, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0) at futex-internal.c:139
#3  0x00007f76b60a57f9 in __pthread_cond_wait_common (cond=0x561bfb90da40, mutex=<optimized out>, clockid=0, abstime=0x0) at pthread_cond_wait.c:503
#4  ___pthread_cond_wait (cond=0x561bfb90da40, mutex=<optimized out>) at pthread_cond_wait.c:618
#5  0x00007f76a9f57a9d in cnd_wait (cond=<optimized out>, mtx=<optimized out>) at ../src/c11/impl/threads_posix.c:135
#6  0x00007f76a9f3aa0b in util_queue_thread_func (input=input@entry=0x561bfb90b920) at ../src/util/u_queue.c:290
#7  0x00007f76a9f579fc in impl_thrd_routine (p=<optimized out>) at ../src/c11/impl/threads_posix.c:67
#8  0x00007f76b60a66d7 in start_thread (arg=<optimized out>) at pthread_create.c:447
#9  0x00007f76b612a60c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 2 (Thread 0x7f76a8a006c0 (LWP 2050185)):
#0  0x00007f76b60a2da9 in __futex_abstimed_wait_common64 (private=0, futex_word=0x561bfb956048, expected=0, op=393, abstime=0x0, cancel=true) at futex-internal.c:57
#1  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x561bfb956048, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#2  0x00007f76b60a2e2f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x561bfb956048, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x0, private=private@entry=0) at futex-internal.c:139
#3  0x00007f76b60a57f9 in __pthread_cond_wait_common (cond=0x561bfb956020, mutex=<optimized out>, clockid=0, abstime=0x0) at pthread_cond_wait.c:503
#4  ___pthread_cond_wait (cond=0x561bfb956020, mutex=<optimized out>) at pthread_cond_wait.c:618
#5  0x00007f76a9f57a9d in cnd_wait (cond=<optimized out>, mtx=<optimized out>) at ../src/c11/impl/threads_posix.c:135
#6  0x00007f76a9f3aa0b in util_queue_thread_func (input=input@entry=0x561bfb9569a0) at ../src/util/u_queue.c:290
#7  0x00007f76a9f579fc in impl_thrd_routine (p=<optimized out>) at ../src/c11/impl/threads_posix.c:67
#8  0x00007f76b60a66d7 in start_thread (arg=<optimized out>) at pthread_create.c:447
#9  0x00007f76b612a60c in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 1 (Thread 0x7f76b64b5740 (LWP 2050183)):
#0  __memset_avx2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memset-vec-unaligned-erms.S:246
#1  0x00007f76a0838860 in memset (__dest=<optimized out>, __ch=0, __len=<optimized out>) at /usr/include/bits/string_fortified.h:59
#2  rocr::AMD::GpuAgent::AssembleShader (this=this@entry=0x561bfbb1c650, func_name=func_name@entry=0x7f76a08e8173 "TrapHandler", assemble_target=assemble_target@entry=rocr::AMD::GpuAgent::AssembleTarget::ISA, code_buf=@0x561bfbb1ca50: 0x0, code_buf_size=@0x561bfbb1ca58: 4096) at /usr/src/debug/rocm-runtime-6.2.0-2.fc40.x86_64/src/core/runtime/amd_gpu_agent.cpp:393
#3  0x00007f76a083a92b in rocr::AMD::GpuAgent::BindTrapHandler (this=0x561bfbb1c650) at /usr/src/debug/rocm-runtime-6.2.0-2.fc40.x86_64/src/core/runtime/amd_gpu_agent.cpp:2147
#4  rocr::AMD::GpuAgent::PostToolsInit (this=0x561bfbb1c650) at /usr/src/debug/rocm-runtime-6.2.0-2.fc40.x86_64/src/core/runtime/amd_gpu_agent.cpp:887
#5  0x00007f76a0851b9d in rocr::core::Runtime::Load (this=0x561bfbb160c0) at /usr/src/debug/rocm-runtime-6.2.0-2.fc40.x86_64/src/core/runtime/runtime.cpp:1915
#6  rocr::core::Runtime::Acquire () at /usr/src/debug/rocm-runtime-6.2.0-2.fc40.x86_64/src/core/runtime/runtime.cpp:139
#7  rocr::HSA::hsa_init () at /usr/src/debug/rocm-runtime-6.2.0-2.fc40.x86_64/src/core/runtime/hsa.cpp:206
#8  0x00007f76a99505d4 in amd::roc::Device::init () at /usr/src/debug/rocclr-6.2.0-1.fc40.x86_64/rocclr/device/rocm/rocdevice.cpp:479
#9  0x00007f76a99b2863 in amd::Device::init () at /usr/src/debug/rocclr-6.2.0-1.fc40.x86_64/rocclr/device/device.cpp:605
#10 amd::Runtime::init() [clone .isra.0] () at /usr/src/debug/rocclr-6.2.0-1.fc40.x86_64/rocclr/platform/runtime.cpp:76
#11 0x00007f76a991d14d in std::once_flag::_Prepare_execution::_Prepare_execution<std::call_once<clIcdGetPlatformIDsKHR::{lambda()#1}>(std::once_flag&, clIcdGetPlatformIDsKHR::{lambda()#1}&&)::{lambda()#1}>(clIcdGetPlatformIDsKHR::{lambda()#1}&)::{lambda()#1}::_FUN() () at /usr/src/debug/rocclr-6.2.0-1.fc40.x86_64/opencl/amdocl/cl_icd.cpp:224
#12 0x00007f76b60aba4b in __pthread_once_slow (once_control=0x7f76a99f63f0 <clIcdGetPlatformIDsKHR::initOnce>, init_routine=0x7f76b62e5f60 <std::__once_proxy()>) at pthread_once.c:116
#13 0x00007f76b60abab9 in ___pthread_once (once_control=<optimized out>, init_routine=<optimized out>) at pthread_once.c:143
#14 0x00007f76a991cfae in __gthread_once (__once=0x7f76a99f63f0 <clIcdGetPlatformIDsKHR::initOnce>, __func=<optimized out>) at /usr/include/c++/14/x86_64-redhat-linux/bits/gthr-default.h:713
#15 std::call_once<clIcdGetPlatformIDsKHR(cl_uint, _cl_platform_id**, cl_uint*)::<lambda()> > (__once=@0x7f76a99f63f0: {_M_once = 1}, __f=@0x7ffc8f3a341f: {<No data fields>}) at /usr/include/c++/14/mutex:916
#16 clIcdGetPlatformIDsKHR (num_entries=<optimized out>, platforms=0x0, num_platforms=0x7ffc8f3a34ac) at /usr/src/debug/rocclr-6.2.0-1.fc40.x86_64/opencl/amdocl/cl_icd.cpp:274
#17 0x00007f76b65d9465 in _find_and_check_platforms (num_icds=3) at /usr/src/debug/ocl-icd-2.3.2-6.fc40.x86_64/ocl_icd_loader.c:479
#18 __initClIcd () at /usr/src/debug/ocl-icd-2.3.2-6.fc40.x86_64/ocl_icd_loader.c:890
#19 _initClIcd_real () at /usr/src/debug/ocl-icd-2.3.2-6.fc40.x86_64/ocl_icd_loader.c:941
#20 0x00007f76b65db68c in _initClIcd () at /usr/src/debug/ocl-icd-2.3.2-6.fc40.x86_64/ocl_icd_loader.c:970
#21 clGetPlatformIDs (num_entries=0, platforms=0x0, num_platforms=0x7ffc8f3a35f4) at /usr/src/debug/ocl-icd-2.3.2-6.fc40.x86_64/ocl_icd_loader.c:1135
#22 0x0000561bdba113b0 in cl::Platform::get (platforms=platforms@entry=0x7ffc8f3a37b0) at /usr/src/debug/rocclr-6.2.0-1.fc40.x86_64/opencl/tools/clinfo/../../khronos/headers/opencl2.2/CL/cl2.hpp:2474
#23 0x0000561bdba085be in main (argc=<optimized out>, argv=<optimized out>) at /usr/src/debug/rocclr-6.2.0-1.fc40.x86_64/opencl/tools/clinfo/clinfo.cpp:75
```