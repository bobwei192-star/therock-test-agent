# Blender opencl on rocm

> **Issue #316**
> **状态**: closed
> **创建时间**: 2018-01-29T07:58:27Z
> **更新时间**: 2019-01-04T20:55:57Z
> **关闭时间**: 2019-01-04T18:31:03Z
> **作者**: gsedej
> **标签**: Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/316

## 标签

- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

Hi

I tried using rocm driver on RX 480. The card can be selected in "system" menu as "opencl" device, but when choosing "cycles renderer" (in upper menu)  and "rendered" (in bottom menu), there is error with log.
System Ubuntu 16.04 + kernel 4.13 + rocm 1.7

I opened bug, since I could find anything on blender+rocm

```
Device init success
Compiling OpenCL kernel ...
Build flags:  -D__NODES_MAX_GROUP__=3 -D__NODES_FEATURES__=7 -D__MAX_CLOSURE__=64 -D__NO_HAIR__ -D__NO_OBJECT_MOTION__ -D__NO_CAMERA_MOTION__ -D__NO_BAKING__
/tmp/AMD_3689_19/t_3689_21.cl:2476:12: error: used type 'float' where floating point type is not allowed
        return (t)? a/t: a;
               ~~~^
1 error generated.
OpenCL kernel build output:
Error: Failed to compile opencl source (from CL to LLVM IR).

OpenCL build failed: errors in console
```


---

## 评论 (16 条)

### 评论 #1 — preda (2018-01-29T08:40:09Z)

Please submit this bug (or CC) to blender as well, they may want to fix it themselves.

---

### 评论 #2 — gstoner (2018-03-02T23:06:46Z)

@gsedej  Can you try the beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2  It support 4.13 Linux kernel   Looking for quick report 

---

### 评论 #3 — extraymond (2018-03-13T00:08:02Z)

@gstoner 

I have tried with beta4 and still not working. 
My setup is ubuntu 16.04 with RX 480.


---

### 评论 #4 — gstoner (2018-03-14T16:16:37Z)

@extraymond  Which version of Ubuntu 16.04 and which CPU and Motherboard 

---

### 评论 #5 — extraymond (2018-03-14T16:21:35Z)

It's ubuntu 16.04.4 x64bit (vanilla with unity), hardware info below.

CPU: Intel Xeon CPU E3-1231 v3
MB: Asrock H97M Anniversary

As for blender versions, neither one from official build, ubuntu repo and ppa works.
Opencl is working fine with amdgpu-pro legacy opencl though.

---

### 评论 #6 — extraymond (2018-04-10T15:08:06Z)

@gstoner Any update on blender support?

---

### 评论 #7 — gsedej (2018-05-21T11:27:44Z)

I tested with rocm 1.8 and blender 2.79b, and it still doesn't work (rx 480, ubuntu 16.04).

The compliation of split seems OK on first run.
```
./blender
Device init success
Compiling OpenCL program split

Kernel compilation of split finished in 188.20s.

Compiling OpenCL program base
Kernel compilation of base finished in 66.73s.

Compiling OpenCL program denoising
Kernel compilation of denoising finished in 1.15s.
```

But when used it freezes (even on default cube). The blender freezes but gpu usage gets to 100% and it stays there until blender killd with "-9"
When ran with debug the output is like this:
```
./blender --debug
Switching to fully guarded memory allocator.
Blender 2.79 (sub 0)
Build: 2018-03-22 14:39:03 Linux Release
argv[0] = ./blender
argv[1] = --debug

Note: No (valid) '/home/gsedej/.config/blender/2.79/config/startup.blend' found, fall back to built-in default.

read file 
  Version 272 sub 2 date unknown hash unknown

ordered
 OBCube
 OBLamp
 OBCamera
found bundled python: /podatki/gsedej/Prenosi/blender-2.79b-linux-glibc219-x86_64/2.79/python

ED_undo_push: OpenCL
ED_undo_push: Blender Render
ED_undo_push: CPU

Device init success
```
After last line, it freezes with gpu 100%. No output on dmesg or syslog

---

### 评论 #8 — boberfly (2018-09-03T20:34:24Z)

Hi @extraymond 
The blender devs just got this patch in which fixes a compiler issue for me:
https://developer.blender.org/D3669
But it still hangs for me also unfortunately.

Cheers

---

### 评论 #9 — jlgreathouse (2019-01-04T18:31:03Z)

Hi all,

I just tested Blender 2.79b on an AMD Radeon RX 480 with ROCm 2.0.0 on Ubuntu 18.04.1 LTS. At the very least, I am able to use the cycles renderer to render the default cube on the GPU. I see GPU usage spike for a while and then return to 0, no problems there.

I'll admit that I have very little experience running Blender, but I was able to run the cube sample. When trying the [2.74 demo files](https://download.blender.org/demo/test/Demo_274.zip), kernel compilation takes an extremely long amount of time (10 hours or so for `split`), but it does not fail.

I believe that means that we have fixed the problem in this ticket. However, I will not be closing #402 as I'm not sure that Blender is totally useful yet with how things work.

---

### 评论 #10 — sp82 (2019-01-04T18:49:44Z)

> 10 hours....

this is the problem with the #402 



---

### 评论 #11 — jlgreathouse (2019-01-04T18:53:40Z)

Hi @sp82 

That's why I'm leaving that one open. :)

---

### 评论 #12 — sp82 (2019-01-04T18:58:42Z)

> Hi @sp82
> 
> That's why I'm leaving that one open. :)

The performance are poor, do you know why? Less than CPU raytracing.
Poor performance it is also another bug for me, I'm going to open an Issue for this. I'm trying to use a Vega 64 for Blender and also for Tensorflow and performance are less than the cpu version of this softwares. This is a signal that something is wrong in rocm.

---

### 评论 #13 — jlgreathouse (2019-01-04T19:34:33Z)

The Blender performance is poor -- which is why that issue is still open. Note that I have not made any comments about that issue other than the implication that "it is not fixed yet" because it is not closed.

You would be better off approaching each project about low performance, unless you can trace the problem back to something particular in ROCm as a whole. It's not guaranteed that GPUs will be faster than CPUs in all cases, and how you program a GPU is important to how much performance you get out of it. In addition, this is the wrong forum for general complaints about individual applications. AMD cannot guarantee engineering time to focus on every app on earth.

That said, for Tensorflow specifically, you may want to request help in the [ROCm tensorflow project](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream) if you believe you are not seeing the performance you expect.

---

### 评论 #14 — sp82 (2019-01-04T20:02:54Z)

sorry for hurt your feeling but I'm just an unhappy user that is tired to findout what is the next bug. I use blender on windows on the same card and the performance are really over the top. I'm here because blender, luxrender and tensorflow on ROCm are not working as expected. Guess what is the common component used by this 3 projects?

---

### 评论 #15 — sp82 (2019-01-04T20:22:14Z)

> **I'm not sure that Blender is totally useful yet with how things work.**

Can You Elaborate?

---

### 评论 #16 — jlgreathouse (2019-01-04T20:55:57Z)

> Can You Elaborate?

Yes -- requiring 10 hours for our OpenCL stack to compile the kernels does not mean that Blender is in a working state on ROCm yet. Which is why #402 is still open.

---
