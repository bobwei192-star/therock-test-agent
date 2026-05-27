# Blender 2.80 Cycles testing, compiling kernel hangs, ROCm 1.8.0

> **Issue #402**
> **状态**: closed
> **创建时间**: 2018-05-05T21:10:50Z
> **更新时间**: 2020-12-17T03:38:46Z
> **关闭时间**: 2020-12-17T03:38:45Z
> **作者**: boberfly
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/402

## 描述

Hi all,

I'm just testing Blender Cycles from the bleeding edge branch as well as 2.79b with ROCm 1.8.0 OpenCL on a Vega10 Frontier Edition, running on a HP z620 Workstation (2x E5-2680v2's, 64GB RAM, Quadro k2000 for display). Currently this is the debug I get from the command line using --debug-cycles:

```I0505 14:02:50.856982  5927 session.cpp:701] Requested features:
Experimental features: Off
Max nodes group: 3
Nodes features: 6
Use Hair: True
Use Object Motion: False
Use Camera Motion: True
Use Baking: False
Use Subsurface: True
Use Volume: True
Use Branched Integrator: True
Use Patch Evaluation: False
Use Transparent Shadows: True
Use Principled BSDF: False
Use Denoising: False
I0505 14:02:50.857064  5927 opencl_base.cpp:216] Loading kernels for platform AMD Accelerated Parallel Processing, device Vega 10 XTX [Radeon Vega Frontier Edition].
I0505 14:02:50.857336  5927 opencl_util.cpp:288] OpenCL program split not found in cache.
I0505 14:02:50.897501  5927 opencl_util.cpp:288] Kernel file /home/alex/.cache/cycles/kernels/cycles_kernel_split_33D08D521DA35BC482B41E5979556C99_DBB1D123AFA735A3DDBE5D0BD2C271B9.clbin either doesn't exist or failed to be loaded by driver.
Compiling OpenCL program split
I0505 14:02:50.926681  5927 opencl_util.cpp:288] Build flags: -D__SPLIT_KERNEL__ -D__NODES_MAX_GROUP__=3 -D__NODES_FEATURES__=6 -D__NO_OBJECT_MOTION__ -D__NO_BAKING__ -D__NO_PATCH_EVAL__ -D__NO_SHADOW_TRICKS__ -D__NO_PRINCIPLED__ -D__NO_DENOISING__ -D__NO_SHADER_RAYTRACE__ -D__COMPUTE_DEVICE_GPU__
I0505 14:02:50.926702  5927 opencl_util.cpp:315] Build options passed to clBuildProgram: '-cl-no-signed-zeros -cl-mad-enable -D__KERNEL_OPENCL_AMD__ -D__SPLIT_KERNEL__ -D__NODES_MAX_GROUP__=3 -D__NODES_FEATURES__=6 -D__NO_OBJECT_MOTION__ -D__NO_BAKING__ -D__NO_PATCH_EVAL__ -D__NO_SHADOW_TRICKS__ -D__NO_PRINCIPLED__ -D__NO_DENOISING__ -D__NO_SHADER_RAYTRACE__ -D__COMPUTE_DEVICE_GPU__'.
```

Currently it looks like the compiler just hangs here for quite some time, I can let it run for awhile and see if it eventually compiles, but it seems like something to look into. I can try to help test here as best as I can to assist the ROCm developers.

Cheers!

---

## 评论 (25 条)

### 评论 #1 — gstoner (2018-05-05T23:40:20Z)

It may not be hung but is still compiling just for a long time.  I have the team look at this 

Greg

---

### 评论 #2 — boberfly (2018-05-06T08:31:34Z)

@gstoner cheers Greg

I ran it to about 2 hours, seems like it doesn't finish but it was slowly memory leaking up to about 30gb or so before I killed it.

---

### 评论 #3 — boberfly (2018-05-09T21:32:43Z)

Just an update, I got amdgpu-pro's OpenCL ICD but using rock-dkms on the kernel-side as a test (the amdgpu-dkms which comes with amdgpu-pro does compile against kernel 4.15, however amdkfd causes a kernel oops when I do a clinfo same with 4.13 so I stayed with rock-dkms).

The one found here:
```
https://support.amd.com/en-us/download/workstation?os=Linux%20x86_64#
```

This does work and I was able to successfully compile the kernels that Blender Cycles produces, I guess the OpenCL that ships with amdgpu-pro uses the proprietary compiler instead. Anyways thought I'd test it. My card seems to match these numbers for FE more or less:
```
https://code.blender.org/2017/11/cycles-benchmark-amd-update-new-benchmark-file/
```
Cheers, hoping to test the next release of the OpenCL compiler! :)

---

### 评论 #4 — gstoner (2018-05-10T01:16:00Z)

Thanks

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Alex Fuller <notifications@github.com>
Sent: Wednesday, May 9, 2018 2:32:45 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Blender 2.80 Cycles testing, compiling kernel hangs, ROCm 1.8.0 (#402)


Just an update, I got amdgpu-pro's OpenCL ICD but using rock-dkms on the kernel-side as a test (the amdgpu-dkms which comes with amdgpu-pro does compile against kernel 4.15, however amdkfd causes a kernel oops when I do a clinfo same with 4.13 so I stayed with rock-dkms).

The one found here:

https://support.amd.com/en-us/download/workstation?os=Linux%20x86_64#


This does work and I was able to successfully compile the kernels that Blender Cycles produces, I guess the OpenCL that ships with amdgpu-pro uses the proprietary compiler instead. Anyways thought I'd test it. My card seems to match these numbers for FE more or less:

https://code.blender.org/2017/11/cycles-benchmark-amd-update-new-benchmark-file/


Cheers, hoping to test the next release of the OpenCL compiler! :)

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/402#issuecomment-387882202>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuS-8sJtI92EMTWLVdpVh9awQZxcjks5tw2B9gaJpZM4Tzy0V>.


---

### 评论 #5 — boberfly (2018-08-19T02:55:26Z)

Hi @gstoner 
I've been able to get some time to test ROCm 1.8.2 it's the same result with the stable blender 2.79, and the latest 2.80 out of the box has issues with requiring cl_khr_fp16 (I believe a recent patch went in to support half floats). I can look into fixing the last one with the code base once I compile cycles from scratch, or report it to the cycles team. Have you or your team had a chance to investigate the compile hangs yet? Indigo Bench doesn't run yet either.

Kind regards

---

### 评论 #6 — boberfly (2018-09-03T04:05:10Z)

Hi,
Recent testing of the latest Blender 2.80 and ROCm 1.8.3, I've got a patch pending with the Blender/Cycles devs here:
https://developer.blender.org/D3669

I've successfully compiled Blender/Cycles with this patch and the compiling of the kernel doesn't complain about this previous missing pragma now, however it is displaying the same problem as Blender 2.79 now (hangs and just leaks memory slowly).

Cheers.

---

### 评论 #7 — advancingu (2018-12-14T23:49:49Z)

Seeing the same issue as @boberfly where kernel compilation never seems to finish and memory usage slowly goes up over time. This is with ROCm 1.9.307, a Radeon Vega 56 and Blender 2.80 with today's build.
@gstoner Any updates on this? I just got this card, hoping Blender would finally work...

---

### 评论 #8 — boberfly (2018-12-15T00:22:02Z)

@advancingu I haven't had the time to invest in this yet, but I was going to compile the bleeding edge OpenCL stack and debug where it is getting stuck on, maybe try a bleeding edge LLVM also...

---

### 评论 #9 — akostadinov (2019-01-07T15:55:05Z)

Another use case, with 1.9 I saw meagre performance. With 2.x things go very fast for me. Maybe try the 2.x latest driver and make sure to compile Blender against the rocm opencl version. I'm running on RHEL 7.6 though.

---

### 评论 #10 — dragontamer (2019-01-17T23:23:52Z)

Threadripper 1950x, Sapphire Vega64 here, ROCm 2.0, Ubuntu 18.04. 

After around 350+ seconds, the various OpenCL kernels finish compiling. However, the kernels are very slow and segfault in a lot of test cases. In other cases, it seems like the OpenCL kernels have entered an infinite loop and are no longer responsive.

When testing on Windows 10 (same hardware), the OpenCL Kernels compile much faster and complete a lot of my personal tests in just 15 minutes or so (about 3x than my Threadripper 1950x).

---

### 评论 #11 — SandboChang (2019-03-22T18:38:11Z)

Just trying Blender 2.79 with ROCm 2.2 and VegaFE/R7, it seems the cycle rendering is broken and once selected it froze the program. CPU works fine though.

Update, actually Windows 10 with Vega 56 failed as well. So it may be a more general drive issue.

---

### 评论 #12 — boberfly (2019-03-22T21:26:10Z)

Hi @SandboChang 
I've recently tried it as well with ROCm 2.2 and with Blender 2.80 the shader compiling for split kernels are multi-threaded, however they take around 7-8 minutes to compile for me each, but they do finish now instead of hanging forever. The compiled kernels however are extremely slow, but it did start to render tiles for me. I am using a Vega FE 16GB.

---

### 评论 #13 — advancingu (2019-03-22T22:01:56Z)

As an additional anecdotal data point: I had ROCm 2.x and a Blender 2.80 daily build work on one day at the end of February. This was the first time I ever saw kernels compile successfully and Blender rendering CPU (Ryzen 1700X) + GPU (Vega 56) in tandem. For a scene with low geometry but lots of indirect light bounces, each GPU tile was finished faster than a group of 16 (small) CPU tiles combined. For the BMW test scene, kernels did still not compile though.

Unfortunately due to one or both of ROCm changing (PPA builds) and newer Blender daily builds where OpenCL is also actively worked on, I have not been able to get this back to work properly ever since.

As of today, I can get kernels to compile for the startup box scene with very slow GPU renders. When switching the viewport to Cycles rendered view, kernel compilation never (>30 minutes) finishes and appears to hang with a single compilation thread.

---

### 评论 #14 — advancingu (2019-04-14T10:55:11Z)

With `rocm-opencl` package version `1.2.0-2019040843` from `http://repo.radeon.com/rocm/apt/debian/` and Blender 2.80 `blender-2.80-a3b88c917299-linux-glibc224-x86_64` I can now successfully build kernels again. The first render then works fine, although one tile rendered by my Vega 56 presently takes about 9 to 10 times longer than a tile rendered by the CPU (Ryzen 1700X).

Additionally, trying to launch a second render immediately crashes Blender.

---

### 评论 #15 — boberfly (2019-04-14T11:19:09Z)

Hi @advancingu

Currently I am using the amdgpu-pro/OpenCL PAL stack with blender for now which much more success, and was able to have both co-exist with some ICD wrangling so that they don't replace each other on the same system. A stop-gap measure I guess until ROCm works. I have had to upgrade to a bleeding edge kernel for 18.04 (using kernel 5.0.2) so that I can use all drivers on the same running system, including the latest Mesa stack...

---

### 评论 #16 — iszotic (2019-06-08T00:09:39Z)

@boberfly I guess is more elaborate than just copying libamdocl64.so file from pro drivers and replace the one in opt/rocm/opencl/lib/x86_64, btw, rocm 2.5 compiles with low performance at rendering

---

### 评论 #17 — advancingu (2019-06-08T13:42:15Z)

Just a monthly update: Performance of the just released ROCm 2.5 is still very bad with Blender `2.80-749d53effd58`.

@iszotic Thanks for this great tip! I installed only the ROCm `rocm-opencl` package and its immediate dependencies and then manually copied `libamdocl64.so` extracted from the Radeon Pro driver package `opencl-amdgpu-pro-icd_19.10-785425_amd64.deb` to `/opt/rocm/opencl/lib/x86_64` as you said. Now Blender runs very fast. Thank you so much!

---

### 评论 #18 — esistgut (2019-07-19T11:09:12Z)

Any update on this?

---

### 评论 #19 — sp82 (2019-11-22T10:39:06Z)

2.81 is out and still not working with rocm.

---

### 评论 #20 — esistgut (2019-11-22T15:20:19Z)

> 2.81 is out and still not working with rocm.

2.81 is out with an NVIDIA contributed OptiX/RTX accelerated render support in Cycles.

---

### 评论 #21 — advancingu (2019-11-22T15:56:18Z)

> 2.81 is out with an NVIDIA contributed OptiX/RTX accelerated render support in Cycles.

How exactly does that impact AMD card owners?

---

### 评论 #22 — ghost (2020-02-04T16:16:58Z)

> @iszotic Thanks for this great tip! I installed only the ROCm `rocm-opencl` package and its immediate dependencies and then manually copied `libamdocl64.so` extracted from the Radeon Pro driver package `opencl-amdgpu-pro-icd_19.10-785425_amd64.deb` to `/opt/rocm/opencl/lib/x86_64` as you said. Now Blender runs very fast. Thank you so much!
     
Thank you! 
That works perfectly for me with: `rocm-opencl` apt package (3.0) and 'libamdocl64.so' from 'opencl-amdgpu-pro-icd_19.50-967956_amd64.deb'


---

### 评论 #23 — advancingu (2020-08-23T23:00:07Z)

Just a heads up: With ROCm 3.7.0 I had to reinstall all packages as it is not upgradeable (`sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-util`, then `sudo apt install rocm-dev`). `libamdocl64.so` from amdgpu-pro then needs to be copied to its new location at `/opt/rocm/opencl/lib/` which is a symlink to the actual version.

Although the OpenCL library shipping with ROCm does appear to not crash Blender this time around, it renders much slower than CPU and many times slower than the amdgpu-pro library.

---

### 评论 #24 — advancingu (2020-10-30T19:49:09Z)

Looks like there is some movement at last: https://www.phoronix.com/forums/forum/phoronix/latest-phoronix-articles/1215816-amd-rocm-3-9-released-with-aomp-openmp-offloading-integrated?p=1216299#post1216299

---

### 评论 #25 — ROCmSupport (2020-12-17T03:38:45Z)

Hi @boberfly 
Thanks for reaching out.
The issue mentioned in this ticket is no more now but now Blender is broken working and we have tickets to track this: #1210 and #1106 
Request to track these.
Thank you.

---
