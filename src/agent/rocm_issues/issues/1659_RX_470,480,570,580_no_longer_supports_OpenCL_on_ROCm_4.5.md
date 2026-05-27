# RX 470,480,570,580 no longer supports OpenCL on ROCm 4.5

> **Issue #1659**
> **状态**: closed
> **创建时间**: 2022-01-22T13:29:39Z
> **更新时间**: 2025-05-19T20:51:02Z
> **关闭时间**: 2023-02-13T02:18:17Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1659

## 描述

cf: https://github.com/RadeonOpenCompute/ROCm/issues/1608

And **please don't close this issue** until we have a clear answer - has polaris support been intentionally dropped from ROCm
after only 6 years, or is this an error ?

---

## 评论 (76 条)

### 评论 #1 — ROCmSupport (2022-01-28T13:22:37Z)

AFAIK, we have not removed any code intentionally. But maybe something changed in the stack and we don't validate gfx8 on ROCm, so it might not be working anymore.
One thing from support point of view, each card has some duration of support. We can not continue supporting cards for more number of years as per business standards. As new cards coming into the  market, we keep adding the new ones into the supported list and keep dropping the old ones after certain amount of time, which is the process.

Anyhow, I am not closing this ticket right now. Let me wait for some time.
Thank you.

---

### 评论 #2 — boxerab (2022-01-29T01:20:28Z)

@ROCmSupport  the RX 590 was released in 2018. This is way too early to drop support.

https://www.techpowerup.com/gpu-specs/radeon-rx-590.c3322

---

### 评论 #3 — xuhuisheng (2022-01-29T02:19:04Z)

Maybe you mean OpenCL. The MIOpen run succeed only with a small patch.

---

### 评论 #4 — kvirikroma (2022-02-08T14:06:51Z)

@boxerab I solved this issue by using a docker image of certain version for tensorflow-rocm, when I had tried to use a tensorflow with rx570. Here's my repo with a few little scripts that I used to automate this process: https://github.com/kvirikroma/tensorflow-rocm-legacy
Maybe this will be helpful for you

---

### 评论 #5 — boxerab (2022-02-08T14:24:52Z)

@kvirikroma thank you. I need OpenCL support. That's gone now.

---

### 评论 #6 — Umio-Yasuno (2022-02-10T07:35:44Z)

Is it possible that this commit is the cause?
https://github.com/ROCm-Developer-Tools/ROCclr/commit/16044d1b30b822bb135a389c968b8365630da452

---

### 评论 #7 — boxerab (2022-02-10T13:11:39Z)

> Is it possible that this commit is the cause? [ROCm-Developer-Tools/ROCclr@16044d1](https://github.com/ROCm-Developer-Tools/ROCclr/commit/16044d1b30b822bb135a389c968b8365630da452)

This looks exactly like where OpenCL was disabled. Is it difficult to
build ROCclr with this patch reverted ?

---

### 评论 #8 — xuhuisheng (2022-02-10T13:59:23Z)

I can have a try do patch ROCclr for OpenCL, but I am not familiar with OpenCL, could you show me a demo for testing?

---

### 评论 #9 — Flakebi (2022-02-10T14:12:12Z)

Here are a few examples: https://rocmdocs.amd.com/en/latest/Programming_Guides/Opencl-programming-guide.html#example
The Example Code 1 can be compiled and run with `g++ -std=c++17 -o test test.cpp -g -lOpenCL -O2 && ./test`

---

### 评论 #10 — boxerab (2022-02-10T14:15:02Z)

> I can have a try do patch ROCclr for OpenCL, but I am not familiar with OpenCL, could you show me a demo for testing?

those examples look good, also there is a `clinfo` binary in the `/opt/rocm/opencl/bin` folder, I believe, that can quickly tell
 you if the card is recognized as an opencl device.

---

### 评论 #11 — xuhuisheng (2022-02-10T14:25:05Z)

I am afraid of it is not work, for just revert this commits.
I comment out `return false` of `device/device.hpp`, recompiling HIP with ROCclr, but /opt/rocm/opencl/bin/clinfo cannot find any devices , either.
```
work@e0454438e38a:~/rocm-build$ /opt/rocm/opencl/bin/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.2 AMD-APP.dbg (3361.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               0

```

My card is RX580.

---

### 评论 #12 — boxerab (2022-02-10T14:27:29Z)

Thanks, so it looks like AMD really did remove support

---

### 评论 #13 — Atemu (2022-02-10T14:41:18Z)

And intentionally so.

---

### 评论 #14 — Atemu (2022-02-10T14:42:13Z)

Has anyone tried to set `ROC_ENABLE_PRE_VEGA` to true? Default seems to be false.

---

### 评论 #15 — boxerab (2022-02-10T14:42:35Z)

hmmm, that's an interesting idea

---

### 评论 #16 — boxerab (2022-02-11T21:18:22Z)

@ROCmSupport can you comment on Polaris support in recently released ROCm 5.0 ?

---

### 评论 #17 — MathiasMagnus (2022-02-14T10:12:57Z)

Dear @ROCmSupport,

> We can not continue supporting cards for more number of years as per business standards.

Nvidia recently dropped Kepler support in CUDA in June 2021, when Kepler was released 2012 April. That's 9 years of support. RX 470 was released June 2016, so ~5 years. A bit over half as much. People who bought an RX 590 (released in 2018 November, easily on shelves throughout 2019) only got 2 years of support. **2 years of support!**

I'm teaching GPGPU to physicists at university and we have a BYOD policy (teaching OpenCL, HIP/CUDA, SYCL) and easily the students who suffer the most are those sporting AMD hardware (myself included, running an RX 580 laptop). It's increasingly hard to install and run any of these APIs. Everything stems from the spotty gfx803 support moved to "partial support" (whatever that means) way too early. AMD shouldn't release products they won't support.

_(FWIW even in my professional capacity it's becoming harder to justify recommending CDNA products, due to all of them being gfx9XYZ variants for such a long time. I can't say with a straight face that MI100s/MI200s will not share the same fate as RX 590s, that MI200 successors won't sport a new ISA and gfx9XYZ will be dropped ever so swiftly, being an ancient ISA flavor. Professional Fiji owners have been burned like this before, not just consumer card owners.)_

My experience trying to get gfx803 working:

- HIP doesn't work with DKMS or with Ubuntu 20.04 upstream kernel
```
mate@GL702ZC:~$ /opt/rocm/bin/rocm-smi


======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr   SCLK    MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
0    55.0c  14.253W  608Mhz  2000Mhz  0%   auto  68.0W     7%   0%    
================================================================================
WARNING:  		 One or more commands failed
============================= End of ROCm SMI Log ==============================
mate@GL702ZC:~$ sudo /opt/rocm/bin/rocminfo 
ROCk module is loaded
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1143
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```
- OpenCL ROCr runtime doesn't detect the device, even with `ROC_ENABLE_PRE_VEGA` set.
- OpenCL orca runtime mostly works but
  - crashes inside the runtime when creating the interop context.
  - Failed to finalize BRIG when having `work_group_reduce_add` function in use inside the kernel. (Missing device built-in)
  
The user experience is bad with all APIs. This doesn't incentivize users to upgrade and buy AMD HW.

---

### 评论 #18 — FelixSchwarz (2022-02-14T21:02:46Z)

> Has anyone tried to set `ROC_ENABLE_PRE_VEGA` to true? Default seems to be false.

I tried that using a self-compiled ROCm 5.0 stack on Fedora but still no dice (same as @MathiasMagnus). However if someone is collecting patches to re-enable Polaris in ROCm, please let me know. Seems like there is no easy solution but maybe it isn't that hard...

---

### 评论 #19 — dagrim (2022-02-14T22:19:49Z)

I have OpenCL working in Ubuntu 20.04 with an RX570. Here is what I did :
- install ROCm 4.5.2
- get the 21.10 Radeon Software for Linux for Ubuntu 20.04 .tar.xz from here : https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-10
- extract the .tar.xz
- extract the `opencl-orca-amdgpu-pro-icd_21.10-1247438_amd64.deb` and `ocl-icd-libopencl1-amdgpu-pro_21.10-1247438_amd64.deb` files
- check that you get those 4 files : `opt/amdgpu-pro/lib/x86_64-linux-gnu/{libamdocl12cl64.so,libamdocl-orca64.so,libOpenCL.so.1.2,libOpenCL.so.1}`
- put those 4 files into a custom directory, say `/opt/myopencl/lib/`
- create a new file `/etc/OpenCL/vendors/myopencl.icd` with only 1 line : `/opt/myopencl/lib/libamdocl-orca64.so`
- try `clinfo` ; here is what I get : 
```
Number of platforms                               2
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.1 AMD-APP (3224.4)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
  Platform Host timer resolution                  1ns
  Platform Extensions function suffix             AMD

  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 21.2.0-devel (git-eb6d990 2021-05-04 focal-oibaf-ppa)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     Ellesmere
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.2 AMD-APP (3224.4)
  Driver Version                                  3224.4
  Device OpenCL C Version                         OpenCL C 1.2 
  Device Type                                     GPU
  Device Board Name (AMD)                         AMD Radeon RX 570 Series
[...]
```



---

### 评论 #20 — boxerab (2022-02-14T22:30:06Z)

> I have OpenCL working in Ubuntu 20.04 with an RX570. Here is what I did :
> 
> * install ROCm 4.5.2
> * get the 21.10 Radeon Software for Linux for Ubuntu 20.04 .tar.xz from here : https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-10
> * extract the .tar.xz
> * extract the `opencl-orca-amdgpu-pro-icd_21.10-1247438_amd64.deb` and `ocl-icd-libopencl1-amdgpu-pro_21.10-1247438_amd64.deb` files
> * check that you get those 4 files : `opt/amdgpu-pro/lib/x86_64-linux-gnu/{libamdocl12cl64.so,libamdocl-orca64.so,libOpenCL.so.1.2,libOpenCL.so.1}`
> * put those 4 files into a custom directory, say `/opt/myopencl/lib/`
> * create a new file `/etc/OpenCL/vendors/myopencl.icd` with only 1 line : `/opt/myopencl/lib/libamdocl-orca64.so`
> * try `clinfo` ; here is what I get :
> 
> ```
> Number of platforms                               2
>   Platform Name                                   AMD Accelerated Parallel Processing
>   Platform Vendor                                 Advanced Micro Devices, Inc.
>   Platform Version                                OpenCL 2.1 AMD-APP (3224.4)
>   Platform Profile                                FULL_PROFILE
>   Platform Extensions                             cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 
>   Platform Host timer resolution                  1ns
>   Platform Extensions function suffix             AMD
> 
>   Platform Name                                   Clover
>   Platform Vendor                                 Mesa
>   Platform Version                                OpenCL 1.1 Mesa 21.2.0-devel (git-eb6d990 2021-05-04 focal-oibaf-ppa)
>   Platform Profile                                FULL_PROFILE
>   Platform Extensions                             cl_khr_icd
>   Platform Extensions function suffix             MESA
> 
>   Platform Name                                   AMD Accelerated Parallel Processing
> Number of devices                                 1
>   Device Name                                     Ellesmere
>   Device Vendor                                   Advanced Micro Devices, Inc.
>   Device Vendor ID                                0x1002
>   Device Version                                  OpenCL 1.2 AMD-APP (3224.4)
>   Driver Version                                  3224.4
>   Device OpenCL C Version                         OpenCL C 1.2 
>   Device Type                                     GPU
>   Device Board Name (AMD)                         AMD Radeon RX 570 Series
> [...]
> ```

Nice. But I see that only OpenCL 1.2 is supported - used to be 2.x with earlier ROCm versions. Also, do you even need ROCm, as you are getting OpenCL from the amdgpu driver ?

---

### 评论 #21 — dagrim (2022-02-15T08:01:32Z)

You're right on both points : 
1. ROCm is probably not needed, indeed. Any OpenCL icd would work.
2. The Platform version advertises OpenCL 2.1, and the device version 1.2. In fact, I did not even notice since that solution allowed my OpenCL workflow to run successfully.


---

### 评论 #22 — xuhuisheng (2022-02-15T13:38:22Z)

I think I used wrong package, after recompile rocm-opencl-runtime, clinfo can display gfx803 device.
I will upload my package in this week, everyone who is interest in opencl and gfx803 can have a test.

BTW, My card is RX580, test on ubuntu-20.04 and ROCm-5.0.0.

---

### 评论 #23 — boxerab (2022-02-15T14:23:04Z)

> I think I used wrong package, after recompile rocm-opencl-runtime, clinfo can display gfx803 device. I will upload my package in this week, everyone who is interest in opencl and gfx803 can have a test.
> 
> BTW, My card is RX580, test on ubuntu-20.04 and ROCm-5.0.0.

Thanks. If you can document what you did to recompile the runtime, we can try it.

---

### 评论 #24 — Umio-Yasuno (2022-02-15T14:33:57Z)

https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime#building

> 
> Follow these steps:
> 
> -   Build ROCclr first. Follow the steps in the following link to build ROCclr
>    [ROCclr Readme](https://github.com/ROCm-Developer-Tools/ROCclr)
>    In this step, $OPENCL_DIR and $ROCclr_DIR are defined.
> 
> -   Building OpenCL
> Run these commands:
> 
> ```bash
> cd "$OPENCL_DIR"
> mkdir -p build; cd build
> cmake -DUSE_COMGR_LIBRARY=ON -DCMAKE_PREFIX_PATH="$ROCclr_DIR/build;/opt/rocm/" ..
> make -j$(nproc)
> ```
> 
> Note: For release build, add "-DCMAKE_BUILD_TYPE=Release" to the cmake command line.

---

### 评论 #25 — boxerab (2022-02-15T14:37:40Z)

> https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime#building
> 
> > Follow these steps:
> > 
> > * Build ROCclr first. Follow the steps in the following link to build ROCclr
> >   [ROCclr Readme](https://github.com/ROCm-Developer-Tools/ROCclr)
> >   In this step, $OPENCL_DIR and $ROCclr_DIR are defined.
> > * Building OpenCL
> >   Run these commands:
> > 
> > ```shell
> > cd "$OPENCL_DIR"
> > mkdir -p build; cd build
> > cmake -DUSE_COMGR_LIBRARY=ON -DCMAKE_PREFIX_PATH="$ROCclr_DIR/build;/opt/rocm/" ..
> > make -j$(nproc)
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > Note: For release build, add "-DCMAKE_BUILD_TYPE=Release" to the cmake command line.

Did you change any settings or variables before building ? 


---

### 评论 #26 — Umio-Yasuno (2022-02-15T14:49:12Z)

> > https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime#building
> > > Follow these steps:
> > > 
> > > * Build ROCclr first. Follow the steps in the following link to build ROCclr
> > >   [ROCclr Readme](https://github.com/ROCm-Developer-Tools/ROCclr)
> > >   In this step, $OPENCL_DIR and $ROCclr_DIR are defined.
> > > * Building OpenCL
> > >   Run these commands:
> > > 
> > > ```shell
> > > cd "$OPENCL_DIR"
> > > mkdir -p build; cd build
> > > cmake -DUSE_COMGR_LIBRARY=ON -DCMAKE_PREFIX_PATH="$ROCclr_DIR/build;/opt/rocm/" ..
> > > make -j$(nproc)
> > > ```
> > > 
> > > 
> > >     
> > >       
> > >     
> > > 
> > >       
> > >     
> > > 
> > >     
> > >   
> > > Note: For release build, add "-DCMAKE_BUILD_TYPE=Release" to the cmake command line.
> 
> Did you change any settings or variables before building ?

Sorry, I haven't tried it in my environment yet.  
At least, I think ROCclr and ROCm-OpenCL-Runtime need to rebuilt to enable OpenCL for gfx803, .

---

### 评论 #27 — xuhuisheng (2022-02-16T02:23:52Z)

I had uploaded patched rocm-opencl-runtime package to github.
<https://github.com/xuhuisheng/rocm-gfx803/releases/download/rocm500/rocm-opencl_2.0.0-local_amd64.deb>

The patch file: <https://github.com/xuhuisheng/rocm-build/blob/feature/build/patch/31.rocm-opencl-runtime-rocclr-gfx803-1.patch>
Just change ROC_ENABLE_PRE_VEGA from false to true.

The build script: <https://github.com/xuhuisheng/rocm-build/blob/feature/build/31.rocm-opencl-runtime.sh>

And please make sure you are testing on ubuntu-20.04 with ROCm-5.0.0 and gfx803 card.

`/opt/rocm/bin/opencl/bin/clinfo`

<details><summary>detail</summary>
<p>

```
work@2ff13ecae2ec:~/rocm-build$ /opt/rocm/opencl/bin/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.2 AMD-APP.dbg (3406.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Radeon RX 580 Series
  Device Topology:                               PCI[ B#2, D#0, F#0 ]
  Max compute units:                             36
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
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
  Max clock frequency:                           1340Mhz
  Address bits:                                  64
  Max memory allocation:                         7301444400
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            16384
  Max image 3D height:                           16384
  Max image 3D depth:                            8192
  Max samplers within kernel:                    26591
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
  Global memory size:                            8589934592
  Constant buffer size:                          7301444400
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          3006477104
  Max global variable size:                      7301444400
  Max global variable preferred total size:      8589934592
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
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
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7f4c522adc80
  Name:                                          gfx803
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0
  Driver version:                                3406.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.2
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program

```

</p></details>

---

### 评论 #28 — FelixSchwarz (2022-02-16T05:57:00Z)

@xuhuisheng Thank you for your comment. It encouraged me to try again and it works now. I'm not sure why this is as I just recompiled my RPMs but `clinfo` now detects my gfx803 device as well. :-)

---

### 评论 #29 — xuhuisheng (2022-02-16T06:19:59Z)

@FelixSchwarz 
I rechecked building scripts, when we compile rocm-opencl-runtime, it will trigger compiling ROCclr, So It shouldn't effect the result.

My problem is, at first time, I am wrong to compile HIP, not ROCm-OpenCL-Runtime.

---

### 评论 #30 — FelixSchwarz (2022-02-16T07:24:39Z)

sorry for spamming here but I just found out why patching `ROC_ENABLE_PRE_VEGA` did not have an effect for me previously: I needed to install `rocm-comgr` as well. I happened to build all of my RPMs with `mock` so I missed comgr even though it was present at build time.

---

### 评论 #31 — FelixSchwarz (2022-02-16T07:31:01Z)

> My problem is, at first time, I am wrong to compile HIP, not ROCm-OpenCL-Runtime.

@xuhuisheng Maybe you can check the work [Debian's ROCm team](https://salsa.debian.org/rocm-team/) is doing and/or use their [mailing list](https://lists.debian.org/debian-ai/). Fedora is present there as well.

---

### 评论 #32 — Atemu (2022-02-19T08:44:10Z)

@SolitaryDragon that's completely unrelated to this issue. Please put it in an appropriate place instead (a new issue for example) and don't ping all of us who are waiting on updates on this specific issue.

---

### 评论 #33 — sampie (2022-02-19T10:31:48Z)

There should be a list of supported cards and the period during which the card is being supported so that users would know the expected end date of the support for their card. And I also agree that is way too early for Polaris to go out of support as it is widely being used.

---

### 评论 #34 — John-Gee (2022-02-23T07:05:01Z)

If the patch works, can it be made into a PR and accepted by AMD? @ROCmSupport @johnbridgman

---

### 评论 #35 — lamdalamda (2022-02-27T04:14:56Z)

That's why there is still few developers outside AMD trying to migrate their softwares to ROCm after it has been released for five years. I have a gfx803 test platform for coding and was planning to migrate the CUDA code to hip so that I can use the juicy FP64 performance of Mi instinct. I spend several hours changing the linux kernel, uninstall the old ROCm and dealing with all stupid conflict. I was that ambitious until I notice that the ROCm 5.0 no longer support gfx803 and I can never perform local test to debug and see if my migration works. Who the hell will ever do the migration work on the HPC platform? Who paid for the GPU hours? Now I feel I am literally a clown. Come on, you are trying to persuade people to switch to a new platform which is 10 years younger, your MI250 is a game changer but your FP64 is 0 FLOP if I cannot run my software on it. Do something @ROCmSupport 

---

### 评论 #36 — BloodyMess (2022-03-07T00:45:42Z)

> I had uploaded patched rocm-opencl-runtime package to github. https://github.com/xuhuisheng/rocm-gfx803/releases/download/rocm500/rocm-opencl_2.0.0-local_amd64.deb
> 
> The patch file: https://github.com/xuhuisheng/rocm-build/blob/feature/build/patch/31.rocm-opencl-runtime-rocclr-gfx803-1.patch Just change ROC_ENABLE_PRE_VEGA from false to true.
> 
> The build script: https://github.com/xuhuisheng/rocm-build/blob/feature/build/31.rocm-opencl-runtime.sh
> 
> And please make sure you are testing on ubuntu-20.04 with ROCm-5.0.0 and gfx803 card.
> 
> `/opt/rocm/bin/opencl/bin/clinfo`
> detail

Has anyone gotten this building and working on an ubuntu 18.04 based system?

My reason is that I'm on elementaryOS 5.1.7 (18.04 based) and am wary of trying to upgrade to the latest 6.x release because the only "upgrade" path they support from 5.1.7 is to do a clean install.

My video card is a RX590.

---

### 评论 #37 — CosmicFusion (2022-03-08T16:05:29Z)

> sorry for spamming here but I just found out why patching `ROC_ENABLE_PRE_VEGA` did not have an effect for me previously: I needed to install `rocm-comgr` as well. I happened to build all of my RPMs with `mock` so I missed comgr even though it was present at build time.

So from what I understand that doesn't work because because AMD forgot/temporarily disabled/disabled this Flag for some reason so if AMD was to enabled it Polaris would "Un-Officially Supported" rather the being "Dropped" is that correct or Am I not understanding it right ? Plz answer

---

### 评论 #38 — CosmicFusion (2022-03-15T18:45:14Z)

> @xuhuisheng Thank you for your comment. It encouraged me to try again and it works now. I'm not sure why this is as I just recompiled my RPMs but `clinfo` now detects my gfx803 device as well. :-)

Could you make a guide on how to build this for fedora or at least send me an RPM ? Plz

---

### 评论 #39 — FelixSchwarz (2022-03-15T20:58:18Z)

@CosmicFusion very little free time now but basically you can use https://copr.fedorainfracloud.org/coprs/fschwarz/rocm-f35/builds/ + a patch for rocm-opencl from https://copr.fedorainfracloud.org/coprs/mystro256/rocm-opencl/ . I guess it's best if you send me an email so I don't have to spam this bug tracker.

---

### 评论 #40 — BloodyMess (2022-03-16T03:58:32Z)

I've got DaVinci Resolve 17.4.5 build 7 mostly working on elementary 5.1.7 (ubuntu 18.04), with a radeon RX590.

Blender Cycles is working fine now.

Here's a demo of the results:
https://youtu.be/u_TQaArfROE

---

### 评论 #41 — bluescarni (2022-03-30T13:49:47Z)

> I had uploaded patched rocm-opencl-runtime package to github. https://github.com/xuhuisheng/rocm-gfx803/releases/download/rocm500/rocm-opencl_2.0.0-local_amd64.deb
> 
> The patch file: https://github.com/xuhuisheng/rocm-build/blob/feature/build/patch/31.rocm-opencl-runtime-rocclr-gfx803-1.patch Just change ROC_ENABLE_PRE_VEGA from false to true.
> 
> The build script: https://github.com/xuhuisheng/rocm-build/blob/feature/build/31.rocm-opencl-runtime.sh
> 
> And please make sure you are testing on ubuntu-20.04 with ROCm-5.0.0 and gfx803 card.
> 
> `/opt/rocm/bin/opencl/bin/clinfo`
> detail

Thanks a lot for the patch! It fixed the detection of my RX 570 on my Gentoo system.

---

### 评论 #42 — keryell (2022-04-05T18:54:25Z)

> AFAIK, we have not removed any code intentionally. But maybe something changed in the stack and we don't validate gfx8 on ROCm, so it might not be working anymore. One thing from support point of view, each card has some duration of support. We can not continue supporting cards for more number of years as per business standards. As new cards coming into the market, we keep adding the new ones into the supported list and keep dropping the old ones after certain amount of time, which is the process.

This is open-source software and thus this should follow the spirit of mind openness.
There is a difference between supporting something officially and forbidding something explicitly instead of just allowing it as a best effort and welcoming outside contributions to make things just work™.
Something working, even if not supported, is better than something not working. :-)

---

### 评论 #43 — John-Gee (2022-04-10T08:58:16Z)

Thanks to xuhuisheng 's patch, Arch's rocm now enables again Pre Vega cards (only on AUR so far, but there is hope arch4edu will pick it up and then eventually community).

---

### 评论 #44 — stefanharjes (2022-05-29T09:18:32Z)

> > I had uploaded patched rocm-opencl-runtime package to github. https://github.com/xuhuisheng/rocm-gfx803/releases/download/rocm500/rocm-opencl_2.0.0-local_amd64.deb
> > The patch file: https://github.com/xuhuisheng/rocm-build/blob/feature/build/patch/31.rocm-opencl-runtime-rocclr-gfx803-1.patch Just change ROC_ENABLE_PRE_VEGA from false to true.
> > The build script: https://github.com/xuhuisheng/rocm-build/blob/feature/build/31.rocm-opencl-runtime.sh
> > And please make sure you are testing on ubuntu-20.04 with ROCm-5.0.0 and gfx803 card.
> > `/opt/rocm/bin/opencl/bin/clinfo`
> > detail
> 
> Thanks a lot for the patch! It fixed the detection of my RX 570 on my Gentoo system.

could you please elaborate? did you manually install or emerge the rocm-opencl-runtime-5.0.2? When I patch the ebuild,
I do not get clinto to recognize my gfx803.

Thansk


---

### 评论 #45 — eriklindahl (2022-08-18T15:38:25Z)

We have communicated this directly to AMD through other channels, but I can only agree with the comments this is a really bad decision.

As a Fortune 500 company bidding for some of the largest supercomputers in the world, I would hope AMD is aware that high performance GPU computing is not merely a matter of what GPUs can run a particular version of a driver, but that it is a landscape of infrastructure including hundreds of packages of software that need to be ported, validated, and debugged.

We happen to develop GROMACS, which is a fairly broadly used computational chemistry package, and we're also fortunate enough that we have access to plenty of centers with the latest hardware. However... we also rely on having extensive CI testing with hosts using lower-power-versions of cards (because those hosts need to both have 2 AMD cards, 2 NVIDIA cards, and 2 Intel cards) that we *really* don't want to keep updating and changing all the time, not to mention that we don't want to have to put 6x 300W cards in any of them.

AMD's decision to only formally support the very latest cards drawing hundreds of watts effectively means that you are making it impossible to test things on ROCm version 4 or later, including OpenCL 2.1.

It's of course perfectly fine to say that's our problem (which it is :-), but this simply means the latest ROCm releases is no longer a tier-0 tested platform for GROMACS, and if this doesn't change before the end of the year, I see no alternative but to recommend users to go with GPUs from other vendors instead :-/




---

### 评论 #46 — CosmicFusion (2022-08-18T16:02:19Z)

hi everyone , i think i have a definitive answer , although AMD isn't communicating with us properly , they seem to have told the fedora team , that they want to support gfx803 , but are too busy on other things , so they dropped it from official to expermintal 
see : https://fedoraproject.org/wiki/SIGs/HC#HW_Support
so if you want to use your gfx803 gpu you need to : 

```
sudo echo   'ROC_ENABLE_PRE_VEGA=1' >> /etc/environment
```
and no patch is needed.

i have tested this on my RX 580 and it work in opencl & hip.

i also spoke with the blender team. 

since they choose to not put gfx803 in their hip targets

they said that there is a possibility for them to make it work ,
but they don't wanna because : 
"WE DON'T WANT TO PUT THE IMPRESSION THAT IT IS ON THE ROADMAP SINCE IT'S NOT OFFICIALLY SUPPORTED BY AMD." 

### EDIT :
testing that env var was done in rocm-5.2.1 from repo.radeon.com

[clinfo-out.txt](https://github.com/RadeonOpenCompute/ROCm/files/9375566/clinfo-out.txt)
[hipinfo-out.txt](https://github.com/RadeonOpenCompute/ROCm/files/9375567/hipinfo-out.txt)



---

### 评论 #47 — Mhowser (2022-09-08T04:37:41Z)

> so if you want to use your gfx803 gpu you need to :
> 
> `sudo echo   'ROC_ENABLE_PRE_VEGA=1' >> /etc/environment`
> and no patch is needed.


Is this exclusive to Fedora only? Or can we use this on other distros?




---

### 评论 #48 — CosmicFusion (2022-09-08T07:42:13Z)

> > so if you want to use your gfx803 gpu you need to :
> > 
> > `sudo echo   'ROC_ENABLE_PRE_VEGA=1' >> /etc/environment`
> > and no patch is needed.
> 
> 
> Is this exclusive to Fedora only? Or can we use this on other distros?
> 
> 
> 

Can be used on all distros , tested on
 PopOS using repo.radeon.com , and fedora using their packages , and my personal built from source ones

---

### 评论 #49 — BloodyMess (2022-09-09T21:47:46Z)

> > > so if you want to use your gfx803 gpu you need to :
> > > `sudo echo   'ROC_ENABLE_PRE_VEGA=1' >> /etc/environment`
> > > and no patch is needed.
> > 
> > 
> > Is this exclusive to Fedora only? Or can we use this on other distros?
> 
> Can be used on all distros , tested on PopOS using repo.radeon.com , and fedora using their packages , and my personal built from source ones

The page you linked on Fedora says (I added bold-italic to highlight):

> Most products starting with vega 10 (Radeon RX Vega) should work without configuration, but any pre-vega HW, such as the RX 400's or 500's, will require setting (**_note this is no longer required for rocm-opencl-5.2.1-2 or later_**):
>```
>    export ROC_ENABLE_PRE_VEGA=1
>```
Can anyone confirm this is correct for the latest ROCm releases?

EDIT:
I think that the statement about not needing the environment variable for version 5.2.1-2 or later might only apply to the builds by Fedora. The AMD ROCm release version numbers don't have a "-2" at the end.

---

### 评论 #50 — xuhuisheng (2022-09-10T02:56:48Z)

I test on ROCm-5.2.3 + RX580, and it works.

I think it is an undocumented environment variable to controll whether we can use OPENCL on gfx803.


---

### 评论 #51 — BloodyMess (2022-09-10T03:36:06Z)

> I test on ROCm-5.2.3 + RX580, and it works.
> 
> I think it is an undocumented environment variable to controll whether we can use OPENCL on gfx803.

Yes, I agree with that.

What I think is happening regarding that phrase on [the Fedora page](https://fedoraproject.org/wiki/SIGs/HC#HW_Support), is that Fedora is doing their ROCm builds from 5.2.1-2 onward with that variable defaulting to true (or maybe their build package sets the environment variable when the installation is done?).

So, the rest of us non-Fedora users have to continue setting that environment variable.

---

### 评论 #52 — Mhowser (2022-09-10T07:58:38Z)

Is anybody able to test if HIP could be used with this method as well?

---

### 评论 #53 — CosmicFusion (2022-09-10T09:03:16Z)

> Is anybody able to test if HIP could be used with this method as well?

HIP doesn't directly depend on ROCclr , and thus works on gfx803 ootb , and I can run hip code with it ,  but forcing blender to render on it caused a white render , so there is an issue on the blender side that needs fixing

---

### 评论 #54 — Mhowser (2022-09-10T09:15:18Z)

That's exactly the use case I wanted to test myself, I couldn't even get Blender to detect my RX 580 yet.

---

### 评论 #55 — xuhuisheng (2022-09-10T09:32:27Z)

@CosmicFusion 
hi, recently, I just find out the blender is a 3d designer app, as 3d max.
And because of my rx580 character , I do some dig for blender on gfx803 with ROCm. Unfortunately, even latest blender-3.3 said it can support gfx900, gfx803 always export a abnormal image.
Compiling OK, export image wont get right result.

---

### 评论 #56 — CosmicFusion (2022-09-10T09:56:00Z)

> @CosmicFusion 
> hi, recently, I just find out the blender is a 3d designer app, as 3d max.
> And because of my rx580 character , I do some dig for blender on gfx803 with ROCm. Unfortunately, even latest blender-3.3 said it can support gfx900, gfx803 always export a abnormal image.
> Compiling OK, export image wont get right result.

Me and GloriousEggroll tried adding gfx803 to blender 3.4 , it either renders a white image or a red mess , this is blender issue not a hip one as I can compile hip code successfully on my RX 580

---

### 评论 #57 — rajhlinux (2022-09-17T05:09:51Z)

[CosmicFusion](https://github.com/CosmicFusion)

> > > so if you want to use your gfx803 gpu you need to :
> > > `sudo echo   'ROC_ENABLE_PRE_VEGA=1' >> /etc/environment`
> > > and no patch is needed.
> > 
> > 
> > Is this exclusive to Fedora only? Or can we use this on other distros?
> 
> Can be used on all distros , tested on PopOS using repo.radeon.com , and fedora using their packages , and my personal built from source ones

You think I can use OpenCL 1.2 on FreeBSD 13.1 for my RX-580 GPU? I need to run OpenCV or "Dlib" machine vision frameworks using my GPU for accelerated computations for face recognition. `clinfo` shows I am using clover with my gpu supporting only opencl 1.1 when it should be 2.0, using MESA drivers.

---

### 评论 #58 — redthing1 (2022-12-20T05:25:11Z)

Wow, I got it to work using https://github.com/rocm-arch/rocm-arch/blob/master/README.md and `HSA_OVERRIDE_GFX_VERSION=10.3.0`

---

### 评论 #59 — owariee (2022-12-24T21:44:24Z)

> AFAIK, we have not removed any code intentionally. But maybe something changed in the stack and we don't validate gfx8 on ROCm, so it might not be working anymore. One thing from support point of view, each card has some duration of support. We can not continue supporting cards for more number of years as per business standards. As new cards coming into the market, we keep adding the new ones into the supported list and keep dropping the old ones after certain amount of time, which is the process.
> 
> Anyhow, I am not closing this ticket right now. Let me wait for some time. Thank you.

i dont seen this being a valid response from AMD as a consumer, i never, really, never, seen a driver for a series of cards dropping support for a feature that is marketed in the cards on purpose, so really, fix this ASAP.  Community are handling your issues for you, on arch polaris works just fine with a patched package from AUR (https://archlinux.org/packages/community-testing/x86_64/rocm-opencl-runtime/)

---

### 评论 #60 — John-Gee (2022-12-24T23:56:18Z)

> > AFAIK, we have not removed any code intentionally. But maybe something changed in the stack and we don't validate gfx8 on ROCm, so it might not be working anymore. One thing from support point of view, each card has some duration of support. We can not continue supporting cards for more number of years as per business standards. As new cards coming into the market, we keep adding the new ones into the supported list and keep dropping the old ones after certain amount of time, which is the process.
> > Anyhow, I am not closing this ticket right now. Let me wait for some time. Thank you.
> 
> i dont seen this being a valid response from AMD as a consumer, i never, really, never, seen a driver for a series of cards dropping support for a feature that is marketed in the cards on purpose, so really, fix this ASAP. Community are handling your issues for you, on arch polaris works just fine with a patched package from AUR ([archlinux.org/packages/community-testing/x86_64/rocm-opencl-runtime](https://archlinux.org/packages/community-testing/x86_64/rocm-opencl-runtime/))

You don't need to patch ROCm anymore, ROC_ENABLE_PRE_VEGA=1 should be enough.

---

### 评论 #61 — redthing1 (2022-12-29T16:09:33Z)

@CosmicFusion I attempted blender port as well. I have successfully run the 3.3 ROCm build. But when I used the same patches for 3.4 I got the same thing you said, some white and red mess.

---

### 评论 #62 — CosmicFusion (2022-12-29T18:02:13Z)

> @CosmicFusion I attempted blender port as well. I have successfully run the 3.3 ROCm build. But when I used the same patches for 3.4 I got the same thing you said, some white and red mess.

wait do you mean you were able to successfully render on blender using 3.3?

---

### 评论 #63 — Mhowser (2023-01-08T06:31:59Z)

> > @CosmicFusion I attempted blender port as well. I have successfully run the 3.3 ROCm build. But when I used the same patches for 3.4 I got the same thing you said, some white and red mess.
> 
> wait do you mean you were able to successfully render on blender using 3.3?

@redthing1 what is the hardware that you used?

---

### 评论 #64 — CosmicFusion (2023-01-08T10:17:31Z)

> > > @CosmicFusion I attempted blender port as well. I have successfully run the 3.3 ROCm build. But when I used the same patches for 3.4 I got the same thing you said, some white and red mess.
> > 
> > wait do you mean you were able to successfully render on blender using 3.3?
> 
> @redthing1 what is the hardware that you used?

Gigabyte RX 580 8GB with only the ROC_ENABLE_PRE_VEGA=1, for the record this still works in ROCm 5.4.1 for OpenCL, but i haven't tested HIP since 5.2.3 and blender 3.4 alpha or beta i don't remember, and that was without the HSA OVERRIDE env, I currently have exams so i can't test

EDIT : Ohh you are not talking to me lol

---

### 评论 #65 — redthing1 (2023-01-10T21:55:33Z)

> > > @CosmicFusion I attempted blender port as well. I have successfully run the 3.3 ROCm build. But when I used the same patches for 3.4 I got the same thing you said, some white and red mess.
> > 
> > 
> > wait do you mean you were able to successfully render on blender using 3.3?
> 
> @redthing1 what is the hardware that you used?



> > > > @CosmicFusion I attempted blender port as well. I have successfully run the 3.3 ROCm build. But when I used the same patches for 3.4 I got the same thing you said, some white and red mess.
> > > 
> > > 
> > > wait do you mean you were able to successfully render on blender using 3.3?
> > 
> > 
> > @redthing1 what is the hardware that you used?
> 
> Gigabyte RX 580 8GB with only the ROC_ENABLE_PRE_VEGA=1, for the record this still works in ROCm 5.4.1 for OpenCL, but i haven't tested HIP since 5.2.3 and blender 3.4 alpha or beta i don't remember, and that was without the HSA OVERRIDE env, I currently have exams so i can't test
> 
> EDIT : Ohh you are not talking to me lol

Well funny enough. He used the exact same hardware as me. Gigabyte RX 580 8GB with only the ROC_ENABLE_PRE_VEGA=1

---

### 评论 #66 — boxerab (2023-02-09T20:16:02Z)

> Well funny enough. He used the exact same hardware as me. Gigabyte RX 580 8GB with only the ROC_ENABLE_PRE_VEGA=1

@redthing1 what Linux distribution are you using ? And how do you set ROC_ENABLE_PRE_VEGA=1 ?  Do you have to set this variable before you install ?

---

### 评论 #67 — redthing1 (2023-02-09T22:15:36Z)

> > Well funny enough. He used the exact same hardware as me. Gigabyte RX 580 8GB with only the ROC_ENABLE_PRE_VEGA=1
> 
> @redthing1 what Linux distribution are you using ? And how do you set ROC_ENABLE_PRE_VEGA=1 ? Do you have to set this variable before you install ?

Yes

---

### 评论 #68 — boxerab (2023-02-09T22:19:50Z)

> > > Well funny enough. He used the exact same hardware as me. Gigabyte RX 580 8GB with only the ROC_ENABLE_PRE_VEGA=1
> > 
> > 
> > @redthing1 what Linux distribution are you using ? And how do you set ROC_ENABLE_PRE_VEGA=1 ? Do you have to set this variable before you install ?
> 
> Yes

Great! I tried running install script from 
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.3/page/How_to_Install_ROCm.html
but I didn't have the env variable set and it failed to find the cl device. I guess I could set it first and then try again.



---

### 评论 #69 — boxerab (2023-02-10T00:31:58Z)

Alright, I admit defeat. Tried to install 5.4.3 on Ubuntu 22 from install script with `ROC_ENABLE_PRE_VEGA` env variable set in `/etc/environment`. No cl device detected.

Fedora 37 works right out of the box, so I will stick with Fedora.

Unfortunately, the performance of my cl kernels is 50% of what I used to get with ROCm 3.x

---

### 评论 #70 — CosmicFusion (2023-02-10T06:33:22Z)

> Alright, I admit defeat. Tried to install 5.4.3 on Ubuntu 22 from install script with `ROC_ENABLE_PRE_VEGA` env variable set in `/etc/environment`. No cl device detected.
> 
> Fedora 37 works right out of the box, so I will stick with Fedora.
> 
> Unfortunately, the performance of my cl kernels is 50% of what I used to get with ROCm 3.x

You need to run this
```
sudo usermod -aG video $LOGNAME
sudo usermod -aG render $LOGNAME
reboot

```

---

### 评论 #71 — boxerab (2023-02-10T13:31:37Z)

> You need to run this
> 
> ```
> sudo usermod -aG video $LOGNAME
> sudo usermod -aG render $LOGNAME
> reboot
> ```

Thanks,  I will stick with Fedora, as I prefer it to clunky old Ubuntu. I am assuming that perf won't change between the two distributions.

---

### 评论 #72 — boxerab (2023-02-13T02:18:17Z)

As a matter of fact, running my kernels on Fedora 37 with latest packaged ROCm gives same performance as with 3.x ROCm.

I am quite happy with the Fedora 37 packages and their support for Polaris cards. 
Going to close this.


---

### 评论 #73 — Mhowser (2023-02-13T14:34:55Z)

So we must use Fedora if we want to use our cards for anything compute related? Can these packages be ported over to other distros?

---

### 评论 #74 — boxerab (2023-02-13T14:42:48Z)

> So we must use Fedora if we want to use our cards for anything compute related? Can these packages be ported over to other distros?

Some here have got it working for officially supported Ubuntu 22 with AMD packages, unfortunately I only had luck with Fedora. Also I believe there is support on Arch. For other distros I'm not sure.

---

### 评论 #75 — tsl0922 (2023-04-20T06:43:52Z)

> > So we must use Fedora if we want to use our cards for anything compute related? Can these packages be ported over to other distros?
> 
> Some here have got it working for officially supported Ubuntu 22 with AMD packages, unfortunately I only had luck with Fedora. Also I believe there is support on Arch. For other distros I'm not sure.

I can confirm that rocm-5.4.3 works on Ubuntu 22.04.2 LTS / Python 3.10.6 for stable-diffusion-webui, using a manually compiled pytorch 1.13.1 with `PYTORCH_ROCM_ARCH=gfx803`.

https://github.com/tsl0922/pytorch-gfx803

---

### 评论 #76 — vittorio88 (2023-09-10T20:34:54Z)

@tsl0922 Hey, so it seem that with `ROCM_ENABLE_PRE_VEGA` enabled, RX580 and family works just fine?

Why is it that TORCH requires to be manually compiled? 
Just to add: `export PYTORCH_ROCM_ARCH=gfx803` ?

Why is this not the default for Torch, and do you know if/where this was changed in Torch code?

---
