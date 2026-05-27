# ROCm OpenCL causes applications like Gimp to crash

> **Issue #954**
> **状态**: closed
> **创建时间**: 2019-11-30T18:32:31Z
> **更新时间**: 2023-12-18T16:10:09Z
> **关闭时间**: 2023-12-18T16:10:09Z
> **作者**: luyatshimbalanga
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/954

## 描述

Latest update of ROCm OpenCL caused applications like GIMP to crash with enabled Hardware Acceleration (OpenCL). Here is the original report on GIMP gitlab: https://gitlab.gnome.org/GNOME/gimp/issues/4303

---

## 评论 (6 条)

### 评论 #1 — luyatshimbalanga (2019-11-30T18:57:53Z)

```
GNU Image Manipulation Program version 2.10.14
git-describe: GIMP_2_10_12-511-ga4f55d6c7e
C compiler:
	Using built-in specs.
	COLLECT_GCC=gcc
	COLLECT_LTO_WRAPPER=/usr/libexec/gcc/x86_64-redhat-linux/9/lto-wrapper
	OFFLOAD_TARGET_NAMES=nvptx-none
	OFFLOAD_TARGET_DEFAULT=1
	Target: x86_64-redhat-linux
	Configured with: ../configure --enable-bootstrap --enable-languages=c,c++,fortran,objc,obj-c++,ada,go,d,lto --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --with-isl --enable-offload-targets=nvptx-none --without-cuda-driver --enable-gnu-indirect-function --enable-cet --with-tune=generic --with-arch_32=i686 --build=x86_64-redhat-linux
	Thread model: posix
	gcc version 9.2.1 20190827 (Red Hat 9.2.1-1) (GCC) 

using babl version 0.1.72 (compiled against version 0.1.72)
using GEGL version 0.4.18 (compiled against version 0.4.18)
using GLib version 2.62.3 (compiled against version 2.62.2)
using GdkPixbuf version 2.40.0 (compiled against version 2.40.0)
using GTK+ version 2.24.32 (compiled against version 2.24.32)
using Pango version 1.44.7 (compiled against version 1.44.7)
using Fontconfig version 2.13.92 (compiled against version 2.13.92)
using Cairo version 1.16.0 (compiled against version 1.16.0)

```
> fatal error: Segmentation fault

Stack trace:
```

# Stack traces obtained from PID 17494 - Thread 17494 #

[New LWP 17495]
[New LWP 17496]
[New LWP 17497]
[New LWP 17498]
[New LWP 17499]
[New LWP 17500]
[New LWP 17501]
[New LWP 17502]
[New LWP 17503]
[New LWP 17504]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
0x00007feeb115a87c in read () from /lib64/libpthread.so.0
  Id   Target Id                                  Frame 
* 1    Thread 0x7feeb03f1dc0 (LWP 17494) "gimp"   0x00007feeb115a87c in read () from /lib64/libpthread.so.0
  2    Thread 0x7feea319b700 (LWP 17495) "worker" 0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
  3    Thread 0x7feea299a700 (LWP 17496) "worker" 0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
  4    Thread 0x7feea2199700 (LWP 17497) "worker" 0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
  5    Thread 0x7feea1998700 (LWP 17498) "worker" 0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
  6    Thread 0x7feea1197700 (LWP 17499) "worker" 0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
  7    Thread 0x7feea0996700 (LWP 17500) "worker" 0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
  8    Thread 0x7fee93fff700 (LWP 17501) "worker" 0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
  9    Thread 0x7fee937fe700 (LWP 17502) "gmain"  0x00007feeb1074a6f in poll () from /lib64/libc.so.6
  10   Thread 0x7fee92ffd700 (LWP 17503) "gdbus"  0x00007feeb1074a6f in poll () from /lib64/libc.so.6
  11   Thread 0x7fee8a62f700 (LWP 17504) "gimp"   0x00007feeb107634b in ioctl () from /lib64/libc.so.6

Thread 11 (Thread 0x7fee8a62f700 (LWP 17504)):
#0  0x00007feeb107634b in ioctl () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007fee8a658848 in kmtIoctl () from /opt/rocm/lib64/libhsakmt.so.1
No symbol table info available.
#2  0x00007fee8a65302e in hsaKmtWaitOnMultipleEvents () from /opt/rocm/lib64/libhsakmt.so.1
No symbol table info available.
#3  0x00007fee8a8c4a75 in core::Signal::WaitAny(unsigned int, hsa_signal_s const*, hsa_signal_condition_t const*, long const*, unsigned long, hsa_wait_state_t, long*) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
No symbol table info available.
#4  0x00007fee8a8ae5aa in AMD::hsa_amd_signal_wait_any(unsigned int, hsa_signal_s*, hsa_signal_condition_t*, long*, unsigned long, hsa_wait_state_t, long*) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
No symbol table info available.
#5  0x00007fee8a8be190 in core::Runtime::AsyncEventsLoop(void*) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
No symbol table info available.
#6  0x00007fee8a884087 in os::ThreadTrampoline(void*) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
No symbol table info available.
#7  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#8  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 10 (Thread 0x7fee92ffd700 (LWP 17503)):
#0  0x00007feeb1074a6f in poll () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb132379e in g_main_context_iterate.isra () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb1323b23 in g_main_loop_run () from /lib64/libglib-2.0.so.0
No symbol table info available.
#3  0x00007feeb15a494a in gdbus_shared_thread_func () from /lib64/libgio-2.0.so.0
No symbol table info available.
#4  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#5  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#6  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 9 (Thread 0x7fee937fe700 (LWP 17502)):
#0  0x00007feeb1074a6f in poll () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb132379e in g_main_context_iterate.isra () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb13238d3 in g_main_context_iteration () from /lib64/libglib-2.0.so.0
No symbol table info available.
#3  0x00007feeb1323921 in glib_worker_main () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#5  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#6  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 8 (Thread 0x7fee93fff700 (LWP 17501)):
#0  0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb136fb23 in g_cond_wait () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb18068fb in gegl_parallel_distribute_thread_func () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#3  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#5  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 7 (Thread 0x7feea0996700 (LWP 17500)):
#0  0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb136fb23 in g_cond_wait () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb18068fb in gegl_parallel_distribute_thread_func () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#3  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#5  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 6 (Thread 0x7feea1197700 (LWP 17499)):
#0  0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb136fb23 in g_cond_wait () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb18068fb in gegl_parallel_distribute_thread_func () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#3  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#5  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 5 (Thread 0x7feea1998700 (LWP 17498)):
#0  0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb136fb23 in g_cond_wait () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb18068fb in gegl_parallel_distribute_thread_func () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#3  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#5  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 4 (Thread 0x7feea2199700 (LWP 17497)):
#0  0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb136fb23 in g_cond_wait () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb18068fb in gegl_parallel_distribute_thread_func () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#3  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#5  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 3 (Thread 0x7feea299a700 (LWP 17496)):
#0  0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb136fb23 in g_cond_wait () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb18068fb in gegl_parallel_distribute_thread_func () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#3  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#5  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 2 (Thread 0x7feea319b700 (LWP 17495)):
#0  0x00007feeb107a1ad in syscall () from /lib64/libc.so.6
No symbol table info available.
#1  0x00007feeb136fb23 in g_cond_wait () from /lib64/libglib-2.0.so.0
No symbol table info available.
#2  0x00007feeb18068fb in gegl_parallel_distribute_thread_func () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#3  0x00007feeb134cf52 in g_thread_proxy () from /lib64/libglib-2.0.so.0
No symbol table info available.
#4  0x00007feeb11504e2 in start_thread () from /lib64/libpthread.so.0
No symbol table info available.
#5  0x00007feeb107f693 in clone () from /lib64/libc.so.6
No symbol table info available.

Thread 1 (Thread 0x7feeb03f1dc0 (LWP 17494)):
#0  0x00007feeb115a87c in read () from /lib64/libpthread.so.0
No symbol table info available.
#1  0x00007feeb1c888b7 in gimp_stack_trace_print () from /lib64/libgimpbase-2.0.so.0
No symbol table info available.
#2  0x00005557c15f1010 in gimp_eek ()
No symbol table info available.
#3  0x00005557c15f144e in gimp_fatal_error ()
No symbol table info available.
#4  0x00005557c15f1ae0 in gimp_sigfatal_handler ()
No symbol table info available.
#5  <signal handler called>
No symbol table info available.
#6  0x00007fee89b18068 in ?? () from /opt/rocm/hsa/lib/libhsa-ext-image64.so.1
No symbol table info available.
#7  0x00007fee8a8905e9 in amd::GpuAgent::GetInfo(hsa_agent_info_t, void*) const () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
No symbol table info available.
#8  0x00007fee8a8a280f in HSA::hsa_agent_get_info(hsa_agent_s, hsa_agent_info_t, void*) () from /opt/rocm/hsa/lib/libhsa-runtime64.so.1
No symbol table info available.
#9  0x00007fee8ac83733 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#10 0x00007fee8ac83e32 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#11 0x00007fee8ac8545a in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#12 0x00007fee8ac5228f in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#13 0x00007fee8ac4d297 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#14 0x00007fee8ac20ad5 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#15 0x00007fee8ad983c9 in ?? () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#16 0x00007fee8ac20c0c in clIcdGetPlatformIDsKHR () from /opt/rocm/opencl/lib/x86_64/libamdocl64.so
No symbol table info available.
#17 0x00007fee8b0263c5 in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
No symbol table info available.
#18 0x00007fee8b02818f in ?? () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
No symbol table info available.
#19 0x00007feeb115897f in __pthread_once_slow () from /lib64/libpthread.so.0
No symbol table info available.
#20 0x00007fee8b0268f1 in clGetPlatformIDs () from /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
No symbol table info available.
#21 0x00007feeb1852e29 in gegl_cl_init_load_device_info.constprop () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#22 0x00007feeb1853c73 in gegl_cl_init_common () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#23 0x00007feeb1803be1 in gegl_config_use_opencl_notify () from /lib64/libgegl-0.4.so.0
No symbol table info available.
#24 0x00007feeb140d742 in g_closure_invoke () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#25 0x00007feeb1421604 in signal_emit_unlocked_R () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#26 0x00007feeb142a3ae in g_signal_emit_valist () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#27 0x00007feeb142a9d3 in g_signal_emit () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#28 0x00007feeb14121c4 in g_object_dispatch_properties_changed () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#29 0x00007feeb1411aed in g_object_notify_queue_thaw () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#30 0x00007feeb1415bb9 in g_object_set_valist () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#31 0x00007feeb1416744 in g_object_set () from /lib64/libgobject-2.0.so.0
No symbol table info available.
#32 0x00005557c1a1aa41 in gimp_gegl_init ()
No symbol table info available.
#33 0x00005557c15f068c in app_run ()
No symbol table info available.
#34 0x00005557c15f00be in main ()
No symbol table info available.
[Inferior 1 (process 17494) detached]

```
Unfortunable, I am unable to obtain the debug symbol as it appears such tool seems unavailable for Ryzen APU.

---

### 评论 #2 — emoon (2019-12-03T13:58:00Z)

If you try to run a program such as `clinfo` does that crash also? (that is the case for me)

---

### 评论 #3 — luyatshimbalanga (2019-12-09T05:33:30Z)

Surprisingly, using ```clinfo``` with rocm-opencl runs fine. Not to mention rocm-open is the only version running great although sightly slower on Davinci Resolve.
I am currently using the amdgpu-pro-opencl as a workaround although it reads the GPU part of Ryzen 2500u as "Unknown AMD GPU".

---

### 评论 #4 — btspce (2019-12-23T07:33:46Z)

When hsa-ext-rocr-dev from ROCm 2.10 or 3.0 is installed for image support clinfo crashes and so does Darktable. Last version that worked was hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux from ROCm 2.9. I downgraded just that package and Darktable Gimp and others that require image support work again.

---

### 评论 #5 — nartmada (2023-12-13T21:22:21Z)

Hi @luyatshimbalanga, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #6 — nartmada (2023-12-18T16:10:09Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
