# Safe to upgrade?

> **Issue #331**
> **状态**: closed
> **创建时间**: 2018-02-11T06:15:07Z
> **更新时间**: 2018-02-16T22:41:51Z
> **关闭时间**: 2018-02-16T22:41:51Z
> **作者**: chriselrod
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/331

## 描述

Hi,

I am on Ubuntu 16.04 and rocking ROCm with Ryzen and Vega.
I added the Padoka PPA Mesa, but haven't actually upgraded to Mesa git yet (I am still on 17.2.4).

Additionally, when I do:
```bash
$ sudo apt-get install libclblas-dev
[sudo] password for chris: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libclblas2 libdrm-dev libgl1-mesa-dev libpthread-stubs0-dev libx11-dev libx11-doc libx11-xcb-dev libxau-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxcb-randr0-dev libxcb-render0-dev libxcb-shape0-dev libxcb-sync-dev
  libxcb-xfixes0-dev libxcb1-dev libxdamage-dev libxdmcp-dev libxext-dev libxfixes-dev libxshmfence-dev libxxf86vm-dev mesa-common-dev ocl-icd-libopencl1 ocl-icd-opencl-dev opencl-headers x11proto-core-dev x11proto-damage-dev x11proto-dri2-dev x11proto-fixes-dev
  x11proto-gl-dev x11proto-input-dev x11proto-kb-dev x11proto-xext-dev x11proto-xf86vidmode-dev xorg-sgml-doctools xtrans-dev
```

```bash
$ sudo apt-get install libclfft-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libclfft2 libdrm-dev libgl1-mesa-dev libpthread-stubs0-dev libx11-dev libx11-doc libx11-xcb-dev libxau-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxcb-randr0-dev libxcb-render0-dev libxcb-shape0-dev libxcb-sync-dev
  libxcb-xfixes0-dev libxcb1-dev libxdamage-dev libxdmcp-dev libxext-dev libxfixes-dev libxshmfence-dev libxxf86vm-dev mesa-common-dev ocl-icd-libopencl1 ocl-icd-opencl-dev opencl-headers x11proto-core-dev x11proto-damage-dev x11proto-dri2-dev x11proto-fixes-dev
  x11proto-gl-dev x11proto-input-dev x11proto-kb-dev x11proto-xext-dev x11proto-xf86vidmode-dev xorg-sgml-doctools xtrans-dev
```

```bash
$ sudo apt-get install libglfw3-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libdrm-dev libgl1-mesa-dev libglfw3 libglu1-mesa-dev libpthread-stubs0-dev libx11-dev libx11-doc libx11-xcb-dev libxau-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxcb-randr0-dev libxcb-render0-dev libxcb-shape0-dev
  libxcb-sync-dev libxcb-xfixes0-dev libxcb1-dev libxcursor-dev libxdamage-dev libxdmcp-dev libxext-dev libxfixes-dev libxi-dev libxinerama-dev libxrandr-dev libxrender-dev libxshmfence-dev libxxf86vm-dev mesa-common-dev x11proto-core-dev x11proto-damage-dev
  x11proto-dri2-dev x11proto-fixes-dev x11proto-gl-dev x11proto-input-dev x11proto-kb-dev x11proto-randr-dev x11proto-render-dev x11proto-xext-dev x11proto-xf86vidmode-dev x11proto-xinerama-dev xorg-sgml-doctools xtrans-dev
```

The number of packages that would be installed is rather...large, and I am concerned that some of them will conflict with ROCm.
Is it safe to install these? If not, are there any good workarounds? Trying to build these from source?

I ask, because I had installed these, and I do not remember what else over the past month. I did not reboot my computer over that time, but when I finally did just now, it would not -- after grub, everything was blank. Googling, it sounded like GPU driver problems.
So I wiped everything, reinstalled, and started over.
Hence my concern over how sensitive ROCm is.

I primarily use ROCm through Julia. Julia's CLArray's library requires CLBLAS and CLFFT as dependencies. It's a little limiting to only have access to GPGPU through compiling HIP into shared libraries, although that has been working well.

On that note, compiling `hipcc -shared -fPIC name.cpp -o name.so` gives me a warning that `shared` was an unused argument, but everything works as intended.

Thanks for the great work, and looking forward to Linux Kernel 17.

PS. 
I do not have a background in C++ or GPGPU/Cuda, so I found basic things like this
https://github.com/ROCm-Developer-Tools/HIP/tree/master/samples/2_Cookbook
very helpful as an introduction.

EDIT:
This isn't so much an issue as a question.
Is there a better place to ask?

EDIT:
Are there some settings I can change in VSCode so that its linter works correctly?
For `hipLaunchKernel`, `__global__`, etc:
`grep -r hipLaunchKernel .` from within `/opt/rocm`, and all I find is the obvious `hip/include`. Adding this does not stop VSCode from registering these as errors. But the code compiles fine.
Is there some way I can make it aware of `hipcc`?
Or some other better supported editor?

---

## 评论 (11 条)

### 评论 #1 — chriselrod (2018-02-13T04:51:06Z)

No one else answers -> science.
Installed them all and rebooted. Everything still works fine. Not sure what went wrong earlier, but I'll just stay away from `sudo apt-get upgrade` on this computer for a while.

I will leave this issue open though until I get an answer on text editors:

Currently I am using VSCode. Unfortunately, even though I have added the following to the include path:

- /opt/rocm/hip/include
- /opt/rocm/hcc/include
- /opt/rocm/include

Hip functions still all register as errors, as well as declarations like `__global__ void kernalname(...)`. These compile and run fine with hipcc.
Is there something I am missing to make VSCode hip-aware?

Or, is there an alternative supported text editor?

---

### 评论 #2 — gstoner (2018-02-13T13:51:49Z)

You asked number of question

I have to see who works with VScode on the team, it is not something we use in the broader team.   I will add it to the task to look at for future release so we have this document.      When we document it, it will be a section in this our master online documentation http://rocm-documentation.readthedocs.io/en/latest/index.html 

One thing we been working with the Julia community on a native port to ROCm, which will also upgrade to our newer BLAS ( rocBLAS)  and FFT( rocFFT)  library which is a huge improvement over clBLAS and clFFT. 


---

### 评论 #3 — briansp2020 (2018-02-13T14:48:43Z)

That doc still talks about 1.6 as the current release.
http://rocm-documentation.readthedocs.io/en/latest/Current_Release_Notes/Current-Release-Notes.html


---

### 评论 #4 — gstoner (2018-02-13T16:09:46Z)

We update the Current release note when we role out 1.7.1 

---

### 评论 #5 — chriselrod (2018-02-13T17:43:57Z)

> One thing we been working with the Julia community on a native port to ROCm, which will also upgrade to our newer BLAS ( rocBLAS) and FFT( rocFFT) library which is a huge improvement over clBLAS and clFFT.

Wow, can't wait. Both the native port (instead of the transpiler, like `OpenCL.jl`) and the upgraded libraries. I benchmarked sgemm for 5000 x 5000 matrices at about 45ms for clBLAS vs 23ms with hipBLAS. Definitely a huge improvement. I probably wont bother wrapping rocfft in ccalls to test it, and am guessing the difference there is similar.
I also haven't tried hipEigen, but it also looks great. `OpenCL.jl` currently has no support for matrix factorizations / linear algebra beyond matrix multiplication.

Any idea about a time frame?

---

### 评论 #6 — preda (2018-02-14T09:24:27Z)

@gstoner : Is there some comparison of clFFT and rocFFT? or, why is rocFFT an improvement over clFFT? thanks!

> our newer BLAS ( rocBLAS) and FFT( rocFFT) library which is a huge improvement over clBLAS and clFFT.


---

### 评论 #7 — gstoner (2018-02-14T16:02:36Z)

rocFFT is big improvement over clFFT,  it pick up on number of lessons learned developing clFFT.  rocBLAS on Vega10 will show  large number of improvement,   We just added hgemm support as well.

On Feb 14, 2018, at 3:24 AM, Mihai Preda <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> : Is there some comparison of clFFT and rocFFT? or, why is rocFFT an improvement over clFFT? thanks!

our newer BLAS ( rocBLAS) and FFT( rocFFT) library which is a huge improvement over clBLAS and clFFT.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/331#issuecomment-365544474>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DudHYazxk39YA27q0sG_3yiqgrRkwks5tUqZNgaJpZM4SBOU0>.



---

### 评论 #8 — psteinb (2018-02-14T16:16:35Z)

Are people interested in a comparison of rocFFT vs clFFT vs cuFFT?

I am the co-maintainer of 
[gearshifft](https://github.com/mpicbg-scicomp/gearshifft/) and would be 
happy to benchmark rocFFT if the community thinks this is helpful. And 
if I get access to a Vega10.

PS. See our current results [here](https://www.kcod.de/gearshifft/).


---

### 评论 #9 — preda (2018-02-15T20:54:17Z)

@gstoner : my limited investigation shows that, at this stage, rocFFT is unfortunately slower than clFFT. 


---

### 评论 #10 — gstoner (2018-02-15T22:24:10Z)

rocBLAS is faster.  I asked the team to look at the compiler optimization,  also the rocFFT need to look at hot loop optimizations in ASM. 

---

### 评论 #11 — gstoner (2018-02-15T22:24:57Z)

Check out tensile  https://github.com/ROCmSoftwarePlatform/Tensile

---
