# opencl install question

> **Issue #156**
> **状态**: closed
> **创建时间**: 2017-07-07T17:49:46Z
> **更新时间**: 2017-07-08T20:24:33Z
> **关闭时间**: 2017-07-08T20:11:00Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/156

## 描述

Can I install both `rocm-opencl` and `rocm-opencl-dev` packages, or do I only need one of them ?

Also, how do I "make the ROCm kernel your default kernel."  ?

---

## 评论 (31 条)

### 评论 #1 — jedwards-AMD (2017-07-07T17:52:46Z)

If you want to develop OpenCL applications, you need to install rocm-opencl-dev. If you only want the runtime, just install rocm-opencl. The rocm-opencl-dev package requires rocm-opencl.

---

### 评论 #2 — boxerab (2017-07-07T17:59:04Z)

Thanks! I figured out how to set rocm kernel in grub, but I do get errors about PCI devices on booting.
Yet, I did try the vector_copy sample, and it works without error. Is there a way of running clinfo on my cards ?

---

### 评论 #3 — jedwards-AMD (2017-07-07T18:01:07Z)

If you have rocm-opencl-dev installed, clinfo should be in the /opt/rocm/opencl/bin/x86_64 directory. You should be able to run it.

---

### 评论 #4 — boxerab (2017-07-07T18:02:18Z)

thank you. Install was pretty smooth. 

On boot, I get an ACPI error, and also:

`Invalid PCI ROM signature: expected ... got 0xffff`

I have two cards, second one on x4 slot. Perhaps this is causing the error.



---

### 评论 #5 — boxerab (2017-07-07T18:02:47Z)

One thing about building vector_copy : I needed to run make as sudo. Install instructions
just say
`make`




---

### 评论 #6 — boxerab (2017-07-07T18:05:30Z)

Awesome, clinfo works fine. Only sees one card, but that is fine with me for now.

---

### 评论 #7 — boxerab (2017-07-07T18:09:18Z)

The following might be added to opencl install instructions :

Set an environment variable that points to the installation directory for OpenCL:
`export OPENCL_ROOT=/opt/rocm/opencl`

---

### 评论 #8 — boxerab (2017-07-07T18:10:50Z)

Do I need to set `OPENCL_INCLUDE_ROOT` and `OPENCL_LIBRARY_ROOT`  ?

---

### 评论 #9 — boxerab (2017-07-07T18:12:13Z)

No worries. As I said, install was very smooth, so looking forward to testing my app out.

---

### 评论 #10 — jedwards-AMD (2017-07-07T18:13:36Z)

Yes, the packaging for the vector_copy sample has a permissions issue. We are going to replace vector_copy in the future, so we haven't bother fixing this problem. I am sorry for the inconvenience.

---

### 评论 #11 — jedwards-AMD (2017-07-07T18:15:06Z)

The environment variables OPENCL_ROOT, OPENCL_INCLUDE_ROOT and OPENCL_LIBRARY_ROOT are all vestiges of the old AMD APPSDK. The installation of the rocm-opencl packages do not explicitly set them. 

---

### 评论 #12 — boxerab (2017-07-07T18:19:32Z)

I see. I have a cmake script that detects the opencl sdk. I will add some code to detect rocm. 
How do you recommend approaching this ?

Here is an example of such a cmake find file:


https://github.com/Kitware/VisCL/blob/master/CMake/FindOpenCL.cmake

---

### 评论 #13 — boxerab (2017-07-07T18:20:55Z)

Perhaps we can add these changes upstream.

---

### 评论 #14 — jedwards-AMD (2017-07-07T18:27:10Z)

Actually we are in the process of adding package management to all of the ROCm associated components, including the ROCr runtime, HIP, HCC, and the higher level libraries. We want to do the same for OpenCL as well. I will create a ticket for this, and hopefully we can get it in by next release.

---

### 评论 #15 — boxerab (2017-07-07T18:28:33Z)

Sounds great. So, how would that work for my cmake project ? How would I detect rocm opencl  with this new management ?

---

### 评论 #16 — boxerab (2017-07-07T18:34:56Z)

In the mean time, what can I set for OPENCL_INCLUDE_DIR and OPENCL_LIBRARY ?

---

### 评论 #17 — jedwards-AMD (2017-07-07T18:38:20Z)

You would be able to use the find_package() CMake call for any of the ROCm packages. You would still have to set the CMAKE_MODULE_PATH, but only to the value /opt/rocm. All the package management information would exist in subdirectories that automatically searched by find_package. See the CMake documentation for more information on how this would work.

---

### 评论 #18 — jedwards-AMD (2017-07-07T18:43:04Z)

All the OpenCL header files are in /opt/rocm/opencl/include (this includes the CL subdirectory). All the OpenCL libraries are in /opt/rocm/opencl/lib/x86_64.

---

### 评论 #19 — boxerab (2017-07-07T18:47:59Z)

find_package support would be really nice - hope you're able to get this in soon.
In the meantime will hard-code those directories you mentioned. Thanks!

---

### 评论 #20 — boxerab (2017-07-08T00:03:34Z)

Note: 

To get this running I needed to set

`OPENCL_INCLUDE_DIR` to `/opt/rocm/opencl/include`

and

`OPENCL_LIBRARY` to  `/opt/rocm/opencl/lib/x86_64/libamdocl64.so`

---

### 评论 #21 — boxerab (2017-07-08T00:12:01Z)

I have quite a few different kernels that share common functionality, so I use the  `-I` include directive to include these common *.cl files. It looks like the current opencl compiler ignores `-I`.  This makes
it hard for me to get my kernels running.

Compiler warning:  `warning: argument unused during compilation: '-I ./'`


Can someone please open an internal ticket for this ?

Thanks!

---

### 评论 #22 — boxerab (2017-07-08T13:05:40Z)

Correction: include directive is working fine.  It seems the compiler doesn't like the `inline` keyword on 
kernel methods.  Please ignore comment above.

---

### 评论 #23 — nevion (2017-07-08T13:18:21Z)

@boxerab you mean like #77 ? 

---

### 评论 #24 — boxerab (2017-07-08T13:35:12Z)

Yes, that was exactly the error I was getting!  This is code that was working fine on windows.

---

### 评论 #25 — gstoner (2017-07-08T14:16:34Z)


Remember OpenCL C language is based on C99, so it uses the C99 semantics (which are different than the c89 or c++ semantics) for the inline keyword.  For C99 “static inline” is the proper declaration for functions that should be inlined in the current translation unit.

---

### 评论 #26 — boxerab (2017-07-08T15:20:00Z)

OK, thanks Greg. Since this is OpenCL, is the inline keyword even necessary ?

---

### 评论 #27 — boxerab (2017-07-08T15:20:16Z)

Does it help the compiler in any way ?

---

### 评论 #28 — boxerab (2017-07-08T15:24:20Z)

Getting back to my code, I make heavy use of OpenCL events. Right now, I can compile all of my kernels, but it looks like events are not working. I will be digging in to this issue, but has anyone tested kernels with events under rocm ?

---

### 评论 #29 — boxerab (2017-07-08T20:10:46Z)

I will close this - install issues have been resolved. Thanks to everyone for their help!

---

### 评论 #30 — nevion (2017-07-08T20:15:06Z)

@boxerab  by the way on the inline keyword for performance/inlining in general, yes I've observed it to change things on gcc and even the old fglrx/amd app sdk, which was particularly sensitive to it for register usage IIRC.  I don't know how much difference inlining makes on ROCm but prior experiences tell me it will have an effect, even with optimizations on.

---

### 评论 #31 — boxerab (2017-07-08T20:24:33Z)

Thanks. At first I just removed the `inline`, but in the end I switched to `static inline`.
Perhaps it is just me being superstitious :) but I don't want to mess with my current performance,
which is very high on RX 470 on windows.



---
