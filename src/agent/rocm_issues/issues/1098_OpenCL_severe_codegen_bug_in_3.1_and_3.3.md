# OpenCL severe codegen bug in 3.1 and 3.3

> **Issue #1098**
> **状态**: closed
> **创建时间**: 2020-05-06T09:01:12Z
> **更新时间**: 2020-05-30T09:10:45Z
> **关闭时间**: 2020-05-30T09:10:44Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1098

## 描述

(compiling for Radeon VII, gfx906)

This report is about an insidious bug affecting OpenCL in ROCm 3.1 and 3.3. The bug is really subtle, hard to pin-point, that's why it took so long to report it. At the same time, the bug is maddening for us developers, I would call it severe for sure. The bug seems to be absent in ROCm 2.10.

In order to facilitate the debugging, in a recent commit https://github.com/preda/gpuowl/commit/90b9fc33b10ff7acf649f2248c3ffbed7397e845 I disabled -cl-fast-relaxed-math to take it out of the suspects list (it seems -cl-fast-relaxed-math is not related to the bug).

Please have a look at [the workaround](https://github.com/preda/gpuowl/blob/90b9fc33b10ff7acf649f2248c3ffbed7397e845/gpuowl.cl#L1510-L1514) we have in gpuowl, which consists in adding an artificial branch that is never taken. This workaround is not a solution because the underlying bug can surface in a different place; and secondarilly the workaround also has a slight performance impact. In brief we'd like the bug fixed and the workaround removed.

The workaround is controlled by the define NO_KCOS_ROCM_BUG which allows to compare the ISA and the behavior with the workaround ON/OFF (by default it's ON, and when running with *-use NO_KCOS_ROCM_BUG* it's OFF).

The way to detect the presence of the bug is: at least one of these fails (error, EE reported):
```
gpuowl -prp 95576851 -fft 5.5M -use NO_KCOS_ROCM_BUG
gpuowl -prp 95576851 -use NO_KCOS_ROCM_BUG
```

OTOH when the bug is absent, all these run correctly (OK reported):
```
gpuowl -prp 95576851 -fft 5.5M -use NO_KCOS_ROCM_BUG
gpuowl -prp 95576851 -use NO_KCOS_ROCM_BUG
gpuowl -prp 95576851 -fft 5.5M
gpuowl -prp 95576851
```

The ISA generated in both cases (with/without the workaround) can be saved using -dump <folder> and compared.

Using the above detector, I did a bisect on the LLVM history (starting from around ROCm 2.10), and it pointed to this change as the point where the bug is introduced:
https://reviews.llvm.org/rG555d8f4ef5ebb2cdce2636af5102ff944da5fef8
https://github.com/llvm/llvm-project/commit/555d8f4ef5ebb2cdce2636af5102ff944da5fef8

I attach the ISA before/after the above change, both with the workaround disabled ("after" is broken by the change):
[ISA-FFT5.5-before.txt](https://github.com/RadeonOpenCompute/ROCm/files/4585695/ISA-FFT5.5-before.txt)
[ISA-FFT5.5-after.txt](https://github.com/RadeonOpenCompute/ROCm/files/4585696/ISA-FFT5.5-after.txt)

Also I attach the ISA, after the change, fixed by applying the workaround (-use NO_KCOS_ROCM_BUG)
[ISA-FFT5.5-after-workaround.txt](https://github.com/RadeonOpenCompute/ROCm/files/4585713/ISA-FFT5.5-after-workaround.txt)

@rampitec I would appreciate help with understanding the bug precisely and fixing it. It would be a great relief for me when this is fixed.


---

## 评论 (8 条)

### 评论 #1 — b-sumner (2020-05-06T14:27:47Z)

Thanks for this report.  All the effort that went into it is appreciated.  We'll definitely take a look.

---

### 评论 #2 — rampitec (2020-05-06T18:20:18Z)

Mentioned commit slightly changes scheduling, nothing more. What happened here:

Kernel fftMiddleOut enables mul:2 with inline asm. Before the change setreg to enable omod was issued before the mul with omod, after setreg was scheduled past instruction with omod and omod was ignored.

In fact there is no dependency between s_setreg instruction from the inline asm and a mul from the inline asm. Nothing prevents compiler from rescheduling one over the other. While ENABLE_MUL2() is defined as "asm volatile" the rest of the inline asm is not volatile and can be rescheduled over.

I.e. just add volatile to the inline asm which depends on the mode setting.

---

### 评论 #3 — gwoltman (2020-05-07T03:06:12Z)

@b-sumner, @rampitec   I too have been trying to figure out what is happening here.  Apparently, there are 2 issues going on.  One is the compiler feeling free to move OMOD asm code before the volatile ENABLE_MUL2.  Our apologies for not realizing that volatile did not protect us from this.  The gcc docs at https://gcc.gnu.org/onlinedocs/gcc/Extended-Asm.html#Volatile suggest adding a false dependency, it neither confirms nor denies that adding a second volatile statement will protect us.  We'll experiment and find something that works.

The second issue here is driving us nuts.  Please look at my attempt to isolate the problem here:  https://github.com/RadeonOpenCompute/ROCm/issues/1097

Interesting side note.  IBM claims (see https://www.ibm.com/developerworks/rational/library/inline-assembly-c-cpp-guide/index.html) that volatile prevents the compiler moving any C code before or after the asm code.  Apparently there is no industry standard as to what volatile really means.

---

### 评论 #4 — preda (2020-05-07T03:07:35Z)

@rampitec Thank you! Indeed the OMOD seems to be involved. In this case it's an internal gpuowl problem not a ROCm one, my bad. I'll close the issue pending a bit more validation.

Related, it would be nice to offer a way to control the denormal settings for DP and the IEEE mode at kernel compilation time (e.g. either with attributes or with some compiler flags), as this would remove the need for explicit s_setreg in the code. Such settings would also allow LLVM to make use of OMOD (for DP) which is a potential big performance gain.


---

### 评论 #5 — gwoltman (2020-05-14T17:43:28Z)

@rampitec:  FYI, adding volatile to the asm statement using mul:2 does not help.  The workaround is to add a false dependency to both asm statements on a common variable.

---

### 评论 #6 — rampitec (2020-05-14T17:47:14Z)

Do you still see mul:2 before setreg? It helped to get a proper order when I tried.

---

### 评论 #7 — gwoltman (2020-05-14T18:00:57Z)

Sorry., stupid user error.  It does work as expected.

---

### 评论 #8 — preda (2020-05-30T09:10:44Z)

Nothing remaining on this issue -- other than maybe to offer a way to enable OMOD (e.g. with some opencl command line flag) -- otherwise as you see it's a pain to make use of the full power of the ISA because OMOD is thoroughly disabled in OpenCL.


---
