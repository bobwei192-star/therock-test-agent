# Broken `-cl-fast-relaxed-math` with ROCm 5.3 OpenCL on RDNA2 when running LuxMark 3

> **Issue #1828**
> **状态**: closed
> **创建时间**: 2022-10-09T16:42:41Z
> **更新时间**: 2022-10-17T00:28:23Z
> **关闭时间**: 2022-10-17T00:25:29Z
> **作者**: illwieckz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1828

## 描述

Hi, I faced a bug on ROCm that I know well because it also affects Mesa Clover as the regression happened on LLVM side.

I reproduced the bug with ROCm on the Steam Deck's APU (“Custom 0405”, VanGhogh, RDNA 2.0). I know this one is not officially supported but despite owning about a dozen of AMD GPUs from GCN1 to RDNA2 this is the only graphic chip that currently works with ROCm on my end. I expect the bug to affect more hardware as the bug is known to exist in LLVM and is even reproduced on other drivers using LLVM like Mesa Clover with other hardware like Hawaii/Grenada GCN2 R9 390X.

So to get ROCm behaving as expected the root cause of the regression has to be found in LLVM and fixed.

Here is the render that is gotten with LuxMark default options (`-cl-fast-relaxed-math` is enabled)

[![luxmark on rocm with broken math](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-063923-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-063923-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)

Here is the expected render (I have to disable `-cl-fast-relaxed-math`, which is not the LuxMark default option):

[![luxmark on rocm](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-064150-000.rocm-luxmark-rdna2-no-fast-relaaxed-math.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-064150-000.rocm-luxmark-rdna2-no-fast-relaaxed-math.png)

The bug is not reproduced with Orca, PAL, fglrx, rusticl (for AMD radeonsi GPU), SRB and Beignet for Intel GPU, Nvidia OpenCL for Nvidia GPU, neither CPU implementations like old AMD CPU OpenCL driver (the one shipped in fglrx or early Orca versions), the Intel CPU one shipped with SRB, PoCL or Mesa rusticl with llvmpipe. That's why, while there is still a minor chance there is something wrong in LuxMark, it is very unlikely. The [luxmark.info](http://luxmark.info/) website validated more then 8000 runs on more than 700 hardware/driver combinations.

How to reproduce the bug.

- Get LuxMark 3: http://www.wiki.luxcorerender.org/LuxMark_v3
- Install ROCm 3.5 on a computer with a supported device;
- Run the Luxball benchmark (the default one) with the default compiler options;
  If you only have one OpenCL platform (ROCm) and only one GPU device, the benchmark would immediately start in a way it will reproduce the bug.

Because I already investigated the bug for Clover, I verified it behaves the exact same way with ROCm and Clover.

- If you enable `-cl-fast-relaxed-math`, the bug is reproduced.
- If you disable `-cl-fast-relaxed-math`, the bug disappears.

But `-cl-fast-relaxed-math` implies both `-cl-finite-math-only` and `-cl-unsafe-math-optimizations`, so I driven more tests. Those individual options are not offered by default LuxMark menu but I have patches on my end to make them easy to tweak.

So:

- `-cl-finite-math-only` enabled: no bug
- `-cl-unsafe-math-optimizations` enabled: no bug
- `-cl-finite-math-only` and `-cl-unsafe-math-optimizations`: bug

The bug comes when both `-cl-finite-math-only` and `-cl-unsafe-math-optimizations` are enabled at the same time, which is implied by enabling `-cl-fast-relaxed-math`.

Which is the exact same behavior I reproduced with Mesa Clover on both GCN2 Hawaii R9 390X and GCN1 Oland R7 240.

Here is the LLVM thread about it, with extensive research:

- https://github.com/llvm/llvm-project/issues/54947

The regression is known to have been introduced in LLVM between LLVM 9 and LLVM 11.

This is considered a regression on ROCm point of view as it is known in 2018 on APP 2679.0 ROCm produced the correct result on an Hawaii/Grenada GCN2 R9 390X.

Here is a table where we can see platforms and versions that reproduce the bug, they're all LLVM-based implementations:

- https://github.com/llvm/llvm-project/issues/54947#issuecomment-1136254537

It is worth noticing PoCL also reproduced the bug starting with LLVM 11 but stopped reproducing it with LLVM 12, while I reproduce the bug with Clover on both LLVM 11, 13 and 15. So maybe getting in touch with PoCL people may help to identify the root cause of the bug if they know how to workaround it.

I'm installing ROCm OpenCL by installing the `rocm-opencl` package, which also installs `amdgpu-core comgr hsa-rocr libdrm-amdgpu-amdgpu1 libdrm-amdgpu-common libdrm2-amdgpu rocm-core rocm-ocl-icd` as dependencies. I don't see any library in `/opt/rocm-5.3.0` that dynamically links to llvm or clang so I assume it is statically linked? You'll probably know what version of LLVM you use anyway.

---

## 评论 (12 条)

### 评论 #1 — b-sumner (2022-10-09T17:26:50Z)

@illwieckz I appreciate the substantial time and effort you've put into analyzing this issue.  But it unfortunately doesn't contain what we really need to understand the problem.  What we really need is a drill down that gives us: which kernels are producing unexpected results, then which functions in those kernels are producing unexpected results, and then finally which expressions are producing unexpected results.

This kind of work would be done fastest by an expert developer of the code.  The AMD compiler team can't be considered as such.  They are not ray tracing experts, and have no idea what any calculation in that code is actually supposed to do.  Without help, it's hard to say how long it will take to see a resolution.

---

### 评论 #2 — illwieckz (2022-10-09T21:03:39Z)

Hi! Hank you for your prompt answer! Unfortunately I'm not a LuxMark/LuxCore developer myself so there are some limits up to which I can dive in. Anyway I can probably help to severely narrow down the problem.

In that comment ( https://github.com/llvm/llvm-project/issues/54947#issuecomment-1157028687 ) I documented a smaller scene that reproduces the problem, identifying which material originally used in the scene produces wrong result on newer LLVM. This can be used to reduce the scope of the code being executed. I also identified some other materials that can be used instead that also reproduces the issue, this may also reduce the scope of the code reproducing the issue by comparing what they share in common.

I also provide a script to (re)build LuxMark 3 with the exact versions of dependencies that can rebuild it and patches that makes it buildable again (the whole repo has to be cloned for the script to run as it relies on other scripts):

- https://gitlab.com/illwieckz/i-love-compute/-/blob/master/scripts/user-luxmark3

For some reasons this software is a bit old but that's still the last stable release so that's the one still used today to test for implementations and check for performance and other things like that. If someone needs to rebuild the software, this script will really makes things easy (I invested days to get the perfect match that can rebuild it, so the knowledge is now baked into the script).

I can provide more patches for LuxMark, like a patch I use to add more OpenCL compilation options to the LuxMark menu.

I may also help to locate where the OpenCL source is actually stored. I believe it's in `LuxCore/include/slg/`, so since the `matte` material is known to fail, this is likely this one:

- https://github.com/LuxCoreRender/LuxCore/blob/luxmark_v3.1/include/slg/materials/materialdefs_funcs_matte.cl

And both `matte`, `roughmatte`, and `cloth` are known to fail on other LLVM-based drivers. On ROCm I only tried `matte` (the default) for now.

I guess that can be a good entry point to start testing what value which function returns on an driver that produces the expected result (or just using an OpenCL compiler option that produces the expected result with the same ROCm driver), and what the same functions returns on default LuxMark options with ROCm. This is the farthest I was able to go as I likely reached my own limit there.

I would be happy to provide help in setting-up an environment to reproduce the issue and track it down and other things like that.

---

### 评论 #3 — illwieckz (2022-10-09T22:12:35Z)

So I did that:

```diff
diff --git a/include/slg/materials/materialdefs_funcs_matte.cl b/include/slg/materials/materialdefs_funcs_matte.cl
index 9abb70cee..bab3468eb 100644
--- a/include/slg/materials/materialdefs_funcs_matte.cl
+++ b/include/slg/materials/materialdefs_funcs_matte.cl
@@ -72,7 +72,7 @@ float3 MatteMaterial_ConstSample(__global HitPoint *hitPoint, const float3 fixed
 
 	*event = DIFFUSE | REFLECT;
 
-	return Spectrum_Clamp(kdVal);
+	return ((float3)(1.f, 0.f, 0.f));
 }
 
 #endif
```

I got that:

[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221009-235616-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221009-235616-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)

If I do `return ((float3)(0.f, 0.f, 0.f));` instead, I get that:

[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221010-000128-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221010-000128-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)

If I do `return ((float3)(1.f, 1.f, 1.f));` instead, I get that:

[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221010-000424-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221010-000424-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)

So, either `Spectrum_Clamp()` is faulty, either `kdVal` value is already wrong.

`Spectrum_Clamp()` is defined in `include/luxrays/core/color/color_funcs.cl` this way:

```opencl
float3 Spectrum_Clamp(const float3 s) {
	return clamp(s, BLACK, WHITE);
}
```

I doubt this code is wrong, so I assume the `kdVal` value is already wrong at this point.

---

_Edit:_ So I did that:

```diff
diff --git a/include/slg/materials/materialdefs_funcs_matte.cl b/include/slg/materials/materialdefs_funcs_matte.cl
index 9abb70cee..31b351946 100644
--- a/include/slg/materials/materialdefs_funcs_matte.cl
+++ b/include/slg/materials/materialdefs_funcs_matte.cl
@@ -72,7 +72,8 @@ float3 MatteMaterial_ConstSample(__global HitPoint *hitPoint, const float3 fixed
 
 	*event = DIFFUSE | REFLECT;
 
-	return Spectrum_Clamp(kdVal);
+	float3 kdVal2 = ((float3)(1.f, 0.f, 0.f));
+	return Spectrum_Clamp(kdVal2);
 }
 
 #endif
```

And I get the same greenish result as if I did `return ((float3)(1.f, 0.f, 0.f));` directly. So `kdVal` is already wrong when `MatteMaterial_ConstSample()` is called.

Basically when the bug happens `kdVal` gets a wrong value that is clamped to `1`.

---

### 评论 #4 — illwieckz (2022-10-12T14:11:51Z)

I updated my `user-luxmark3` script to (re)build LuxMark 3.1 on current systems. I tested it successfully on Ubuntu 22.04.1. It requires GCC10 and some other deps written in the beginning of [the file](https://gitlab.com/illwieckz/i-love-compute/-/blob/master/scripts/user-luxmark3). It can be found on my [i-love-compute](https://gitlab.com/illwieckz/i-love-compute/) repository.

It features additional patches with convenient bug fixes and features like:

- do not crash on OpenCL failure like no platform being available,
- do not crash on OpenCL compilation error,
- also print log on stderr (not only in the graphical application) so it can survive a crash,
- and some others.

The script can be used this way to build LuxMark 3.1: 

```sh
./user-luxmark3 build
```

The script can be used this way to run the built LuxMark 3.1:

```sh
./user-luxmark3 run
```

By default the script runs `luxmark --mode=PAUSE`, but one can start explicit commands this way:

```sh
./user-luxmark run luxmark [luxmark options or not]
```

The repositories are written in `workspace/user-luxmark3` folder. For example the OpenCL code for the `matte` material that reproduces the issue can be found there:

```
workspace/user-luxmark3/LuxCore/include/slg/materials/materialdefs_funcs_matte.cl
```

@b-sumner See also my previous comment for details about a specific kernel that fails and how one can tweak it to test values.

I'm not a LuxMark developer neither a LuxCore developer so that's probably the best I can provide to help ROCm developers to debug the LLVM regression that affects ROCm.

---

### 评论 #5 — illwieckz (2022-10-12T17:03:26Z)

I have news.

- The bug is not in the `MatteMaterial_ConstSample()` function.
- The bug happens somewhere else when the `MatteMaterial_ConstSample()` function returns `(1.0 ,1.0 , 1.0)`.
- The `MatteMaterial_ConstSample()` function returning `(1.0 ,1.0 , 1.0)` is expected to happen as the return value is clamped between `(0.0 ,0.0 , 0.0)` and `(1.0 ,1.0 , 1.0)`.

I noticed `kdVal` was set by the C++ code, so that was suspicious that switching an OpenCL driver or OpenCL option had impact on the bug if the value is not set by OpenCL. The `kdVal` value may be right.

I modified the code this way, hardcoding the return of the `MatteMaterial_ConstSample()` function to always be `(1.0 ,1.0 , 1.0)`:

```diff
diff --git a/include/slg/materials/materialdefs_funcs_matte.cl b/include/slg/materials/materialdefs_funcs_matte.cl
index 9abb70cee..672bf60f5 100644
--- a/include/slg/materials/materialdefs_funcs_matte.cl
+++ b/include/slg/materials/materialdefs_funcs_matte.cl
@@ -72,7 +72,7 @@ float3 MatteMaterial_ConstSample(__global HitPoint *hitPoint, const float3 fixed
 
        *event = DIFFUSE | REFLECT;
 
-       return Spectrum_Clamp(kdVal);
+       return ((float3)(1.f, 1.f, 1.f));
 }
 
 #endif
```

The render should not differ between using `-cl-fast-relaxed-math` or not. But It differs for both ROCm and Clover, not for Orca and RustiCL. The only code in common between ROCm and Clover is the LLVM amdgcn bytecode.

So, something looks really wrong. `(1.0, 1.0, 1.0)` is not `NaN` neither zero so we can both rule out this number being used as `NaN` in another compute or another compute doing a division by zero by dividing this number.

&nbsp;|fast (default)|nofast
---|---|---
VanGogh ROCm|❌️|✔
VanGogh RustiCL|✔|✔
Hawaii Clover|❌️|✔
Hawaii Orca|✔|✔

&nbsp;|fast (default)|nofast
---|---|---
VanGogh ROCm|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181625-000.vangogh-rocm-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181625-000.vangogh-rocm-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181927-000.vangogh-rocm-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181927-000.vangogh-rocm-nofast.png)
VanGogh RustiCL|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-183609-000.vangogh-rusticl-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-183609-000.vangogh-rusticl-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-183835-000.vangogh-rusticl-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-183835-000.vangogh-rusticl-nofast.png)
Hawaii Clover|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-175043-000.hawaii-clover-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-175043-000.hawaii-clover-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-180039-000.hawaii-clover-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-180039-000.hawaii-clover-nofast.png)
Hawaii Orca|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181513-000.hawaii-orca-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181513-000.hawaii-orca-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181753-000.hawaii-orca-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-181753-000.hawaii-orca-nofast.png)






---

### 评论 #6 — illwieckz (2022-10-12T18:03:12Z)

Even this reproduces the issue:

```diff
diff --git a/include/slg/materials/materialdefs_funcs_matte.cl b/include/slg/materials/materialdefs_funcs_matte.cl
index 9abb70cee..870d3f72b 100644
--- a/include/slg/materials/materialdefs_funcs_matte.cl
+++ b/include/slg/materials/materialdefs_funcs_matte.cl
@@ -72,7 +72,8 @@ float3 MatteMaterial_ConstSample(__global HitPoint *hitPoint, const float3 fixed
 
        *event = DIFFUSE | REFLECT;
 
-       return Spectrum_Clamp(kdVal);
+       return clamp(kdVal, ((float3)(0.0f, 0.0f, 0.0f)),
+               ((float3)(0.00000000000000000001f, 0.00000000000000000001f, 0.00000000000000000001f)));
 }
 
 #endif
```

Or simply:

```diff
diff --git a/include/slg/materials/materialdefs_funcs_matte.cl b/include/slg/materials/materialdefs_funcs_matte.cl
index 9abb70cee..00be49cc0 100644
--- a/include/slg/materials/materialdefs_funcs_matte.cl
+++ b/include/slg/materials/materialdefs_funcs_matte.cl
@@ -72,7 +72,7 @@ float3 MatteMaterial_ConstSample(__global HitPoint *hitPoint, const float3 fixed
 
        *event = DIFFUSE | REFLECT;
 
-       return Spectrum_Clamp(kdVal);
+       return ((float3)(0.00000000000000000001f, 0.00000000000000000001f, 0.00000000000000000001f));
 }
 
 #endif
```

More precisely, the bug is reproduced if at least one components is not set to `0.0`, even a very small number like `0.00000000000000000001f` in one component reproduces the bug.

OK:

```c
return ((float3)(0.00000000000000000000f, 0.00000000000000000000f, 0.00000000000000000000f));
```

Not OK:

```c
return ((float3)(0.00000000000000000001f, 0.00000000000000000001f, 0.00000000000000000001f));

return ((float3)(0.00000000000000000000f, 0.00000000000000000001f, 0.00000000000000000001f));
return ((float3)(0.00000000000000000001f, 0.00000000000000000000f, 0.00000000000000000001f));
return ((float3)(0.00000000000000000001f, 0.00000000000000000001f, 0.00000000000000000000f));

return ((float3)(0.00000000000000000001f, 0.00000000000000000000f, 0.00000000000000000000f));
return ((float3)(0.00000000000000000000f, 0.00000000000000000001f, 0.00000000000000000000f));
return ((float3)(0.00000000000000000000f, 0.00000000000000000000f, 0.00000000000000000001f));
```

---

### 评论 #7 — illwieckz (2022-10-12T18:10:04Z)

The `kdValue` looks to be either sampled from an image set in the `.scene` file, either hardcoded into the `.scene` file, so the input can't be wrong anyway.

---

### 评论 #8 — illwieckz (2022-10-13T12:16:05Z)

In fact the matte material is probably not in cause, it just happens to returns value that reproduce the bug elsewhere: input is always valid and valid outputs reproduces the bug anyway.

Here is a simple `scene.scn` file that reproduces the bug, to use as a drop-in replacement of the luxball scene in the luxball scene folder:

```
scene.camera.lookat.orig = 0.65 0.28 0.15
scene.camera.lookat.target = 0.11 1.05 -0.19
scene.camera.up = 0 0 1
scene.lights.infinitelight.type = infinite
scene.lights.infinitelight.file = scenes/luxball/imagemap-00000.exr
scene.materials.material-0x7f4e0b47a5e0.type = matte
scene.materials.material-0x7f4e0b47a5e0.kd = 0.75 0.75 0.75
scene.objects.extmesh-0x7f4e0b4c3920.material = material-0x7f4e0b47a5e0
scene.objects.extmesh-0x7f4e0b4c3920.ply = scenes/luxball/mesh-00006.ply
```

&nbsp;|fast (default)|nofast
---|---|---
VanGogh Rocm|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-220942-000.vangogh-rocm-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-220942-000.vangogh-rocm-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-220721-000.vangogh-rocm-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221012-220721-000.vangogh-rocm-nofast.png)

I probably suffered from a bias in a way I needed a light to actually _see_ if a scene was wrongly rendered or not, so I didn't thought the bug could come from the lighting itself. But in such simple scene there are now only three things:

- the light
- the model geometry (I doubt it's in cause, as in the default scene the flat surface is also affected)
- the matte material

So maybe the problem is in the lighting code.

I just checked and other LuxMark scenes are affected as well:


&nbsp;|fast (default)|nofast
---|---|---
VanGogh ROCm, Luxball scene|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-142411-000.vangogh-rocm-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-142411-000.vangogh-rocm-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-142628-000.vangogh-rocm-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-142628-000.vangogh-rocm-nofast.png)
VanGogh Rocm, Microphone scene|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-084251-000.vangogh-rocm-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-084251-000.vangogh-rocm-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-084508-000.vangogh-rocm-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-084508-000.vangogh-rocm-nofast.png)
VanGogh Rocm, Hotel scene|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-085212-000.vangogh-rocm-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-085212-000.vangogh-rocm-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-085432-000.vangogh-rocm-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-085432-000.vangogh-rocm-nofast.png)

So ROCm regressed on LuxMark on all scenes between 2018 and now (I have seen ROCm working properly with those scenes on Hawaii in 2018). I would recommend having such software being part of the CI. I'm surprised LuxMark isn't part of the CI, it is easier to bisect when things are caught as soon as possible. At 3.1 release time LuxMark people said that “Among other features, it includes some OpenCL optimization suggested by NVIDIA to LuxRender project”, I'm not surprised LuxMark still works on Nvidia if Nvidia people actually use it internally in a way they went to make suggestions to improve LuxMark.

---

### 评论 #9 — illwieckz (2022-10-13T18:56:01Z)

So, I looked for a code in LuxCore that contributes to the lighting.

I picked `AdvancePaths_MK_HIT_OBJECT` from `include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl` that has a comment mentionning `MK_DL_ILLUMINATE`.

I tried to see if I can modify it in a way I get an obvious effect on the render while behaving differently given `-cl-fast-relaxed-math` is used or not.

I got such difference when modifying this code:

https://github.com/LuxCoreRender/LuxCore/blob/358d7754f29508b73d6e9cd8c11ec8141b2176b9/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl#L209-L210

Here are the two patches I tried, first patch is to never return, ignoring the value used for the test:

```diff
diff --git a/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl b/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl
index 9d15fc36c..b8119ab0d 100644
--- a/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl
+++ b/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl
@@ -206,8 +206,6 @@ __kernel __attribute__((work_group_size_hint(64, 1, 1))) void AdvancePaths_MK_HI
        // Read the path state
        __global GPUTaskState *taskState = &tasksState[gid];
        PathState pathState = taskState->state;
-       if (pathState != MK_HIT_OBJECT)
-               return;
 
        //--------------------------------------------------------------------------
        // Start of variables setup
```

While the second patch is to always return, ignoring the value used for the test:

```diff
diff --git a/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl b/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl
index 9d15fc36c..83cde9b95 100644
--- a/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl
+++ b/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl
@@ -206,8 +206,7 @@ __kernel __attribute__((work_group_size_hint(64, 1, 1))) void AdvancePaths_MK_HI
        // Read the path state
        __global GPUTaskState *taskState = &tasksState[gid];
        PathState pathState = taskState->state;
-       if (pathState != MK_HIT_OBJECT)
-               return;
+       return;
 
        //--------------------------------------------------------------------------
        // Start of variables setup
```

Even if such modification may break the rendering, they must break in the exact same way given `-cl-fast-relaxed-math` is used or not.

It does not behave the same way on ROCm and Clover but it behaves the same way on Orca.

On the next table, `return` means always returning, `noreturn` never returning, `fast` is using `-cl-fast-relaxed-math`, `nofast` is not using `-cl-fast-relaxed-math`.

I get 3 kinds of results. With `noreturn`, it differs given is `fast` or `nofast`.

&nbsp;|noreturn, nofast|noreturn, fast|return, nofast|return, fast
-|-|-|-|-
VanGogh, ROCm|noise|light|black|black
Hawaii, Clover|noise|light|black|black
Hawaii, Orca|light|light|black|black

&nbsp;|noreturn, nofast|noreturn, fast|return, nofast|return, fast
-|-|-|-|-
VanGogh, ROCm|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-170737-000.vangogh-rocm-noreturn-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-170737-000.vangogh-rocm-noreturn-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-171005-000.vangogh-rocm-noreturn-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-171005-000.vangogh-rocm-noreturn-nofast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-175937-000.vangogh-rocm-return-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-175937-000.vangogh-rocm-return-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-180152-000.vangogh-rocm-noreturn-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-180152-000.vangogh-rocm-noreturn-fast.png)
Hawaii, Clover|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-171339-000.hawaii-clover-noreturn-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-171339-000.hawaii-clover-noreturn-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-175017-000.hawaii-clover-noreturn-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-175017-000.hawaii-clover-noreturn-nofast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-180429-000.hawaii-clover-return-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-180429-000.hawaii-clover-return-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-180702-000.hawaii-clover-return-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-180702-000.hawaii-clover-return-nofast.png)
Hawaii, Orca|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-185342-000.hawaii-orca-noreturn-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-185342-000.hawaii-orca-noreturn-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-185615-000.hawaii-orca-noreturn-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-185615-000.hawaii-orca-noreturn-nofast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-190448-000.hawaii-orca-return-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-190448-000.hawaii-orca-return-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-191514-000.hawaii-orca-return-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-191514-000.hawaii-orca-return-nofast.png)

Of course I can reproduce it with the simplified scene described [here](https://github.com/RadeonOpenCompute/ROCm/issues/1828#issuecomment-1277517852). The render should not differ but it differs when compiled with `-fast-relaxed-math`.

&nbsp;|noreturn, nofast|noreturn, fast
-|-|-
VanGogh, ROCm|noise|light

&nbsp;|noreturn, fast|noreturn, nofast
-|-|-
VanGogh, ROCm|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-181616-000.vangogh-rocm-return-fast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-181616-000.vangogh-rocm-return-fast.png)|[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-181943-000.vangogh-rocm-return-nofast.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221013-181943-000.vangogh-rocm-return-nofast.png)

So the value used by this test in LuxCore code is not correct when running the OpenCL code compiled by LLVM with `-fast-relaxed-math`:

```c
	// Read the path state
	__global GPUTaskState *taskState = &tasksState[gid];
	PathState pathState = taskState->state;
	if (pathState != MK_HIT_OBJECT)
		return;
```

I'm not a LuxCore developer and I don't know how and where this value is computed, I need help.

---

### 评论 #10 — illwieckz (2022-10-14T22:31:55Z)

@b-sumner The LLVM commit introducing the regression is: https://github.com/llvm/llvm-project/commit/29a2b20ab363bcc0b9573e358a5ad12c0eddca86 “[SDAG] simplify FP binops to undef”.

I tested with Clover as I don't know how to build ROCm, but Clover and ROCm behaves the exact same way on that topic.

This commit was added in 2020, it was added to the LLVM 11 branch before the first release candidate but it looks like the regression hasn't been caught until I reported it this year.

I managed to set up an environment that can build Mesa 21 and LLVM 11, and I then identified that `llvmorg-11.0.0-rc1` reproduced the bug while `llvmorg-11-init` didn't, so I bisected between first parent of those two references and the rc1 references. Luckily I was able to build the same Mesa reference `mesa-21.0.1` through the whole bisect run so the only thing that changed while bisecting was LLVM.

---

### 评论 #11 — b-sumner (2022-10-15T17:45:16Z)

@illwieckz that code has been in for over 2 1/2 years and is not AMD specific.  While it may/did cause luxmark to behave differently, that doesn't mean it was invalid.   Using -cl-fast-relaxed-math is playing with fire.  I still believe we need to find the source of the issue, and am expecting that the code is either not obeying the finite-math contract, or is simply unprepared to handle the other floating point relaxations.

---

### 评论 #12 — illwieckz (2022-10-17T00:25:29Z)

The bug was correctly tracked down. The root cause was a division by zero but because of some reasons, the wreckage happened when multiplying the result of the division by zero when applying a multiplication optimization in LLVM.

The result of the bad division by zero is used in a multiplication that is optimized in a way the multiplication result itself becomes wrong.

Here is a patch for LuxMark 3.1 (LuxCore patch):

- https://gitlab.com/illwieckz/i-love-compute/-/commit/c5d298f36dfc17f45f2d1eda96d602d7f0cd1a7b

The patch fixes the issue when LuxMark 3.1 is running on Mesa Clover or on AMD ROCm OpenCL platform, as both platforms use LLVM amdgcn bytecode generation.

The LLVM FMUL optimization that uncovered the bug is there:

- https://github.com/llvm/llvm-project/blob/29a2b20ab363bcc0b9573e358a5ad12c0eddca86/llvm/lib/CodeGen/SelectionDAG/DAGCombiner.cpp#L12508-L12509

The broken computation dividing something by pdf clamp even if it's zero is there:

- https://github.com/LuxCoreRender/LuxCore/blob/luxmark_v3.1/include/slg/engines/pathocl/kernels/pathocl_kernels_micro.cl#L642-L643

The pdf clamp value is set to zero there:

- https://github.com/LuxCoreRender/LuxCore/blob/luxmark_v3.1/src/slg/engines/pathocl/pathocl.cpp#L121

The patches rewrites this:

```opencl
min(1.f, something / PARAM_PDF_CLAMP_VALUE)
```

into this:

```opencl
min(1.f, something / (PARAM_PDF_CLAMP_VALUE == 0.f ? something : PARAM_PDF_CLAMP_VALUE))
```

Here are some validated run of patched LuxMark 3.1 running with `-cl-fast-relaxed-math` on Mesa Clover and ROCm:

Mesa Clover on Hawaii GCN2, validated run with `-cl-fast-relaxed-math`: http://luxmark.info/node/9562

[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-215956-000.hawaii-orca-patched-luxmark.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-215956-000.hawaii-orca-patched-luxmark.png)

[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-215958-000.hawaii-orca-patched-luxmark.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-215958-000.hawaii-orca-patched-luxmark.png)

AMD ROCm on VanGogh RDNA2, validated run with `-cl-fast-relaxed-math`: http://luxmark.info/node/9563

[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-220725-000.vangogh-rocm-patched-luxmark.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-220725-000.vangogh-rocm-patched-luxmark.png)

[![luxmark cl fast relaxed math garbage](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-220727-000.vangogh-rocm-patched-luxmark.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221016-220727-000.vangogh-rocm-patched-luxmark.png)

---
