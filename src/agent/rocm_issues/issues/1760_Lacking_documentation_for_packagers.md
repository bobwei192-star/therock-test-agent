# Lacking documentation for packagers

> **Issue #1760**
> **状态**: closed
> **创建时间**: 2022-06-24T16:32:28Z
> **更新时间**: 2025-03-21T19:05:16Z
> **关闭时间**: 2025-03-21T19:05:15Z
> **作者**: bgamari
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1760

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

Since ROCm 5.0, the provided installation documentation heavily leans on AMD's binary packaging and installation script. These methods may be convenient for some but are not appropriate for distribution packagers and are not a substitute for proper build documentation.

This is in large part why [no widely-used Linux distribution](https://repology.org/project/rocm-smi/versions) ships packaging for anything newer than ROCm 4.5. If ROCm is going to be a serious alternative to CUDA, there needs to be a stronger effort put into dissemination, including facilitating packaging. This would require a maintained document (ideally in this repository) which:

 * briefly summarises ROCm's components, their dependencies, and, in the case of forks (e.g. LLVM), how they relate to their upstream projects
 * either describes how to build each individual component or refers to up-to-date documentation in that component's repository which describes the same
 * describes any necessary environment configuration (e.g. which device nodes must be accessible to users)
 * optional but recommended: describes how downstream packages (e.g. `pytorch`, `tensorflow`) should be packaged to allow users to benefit from ROCm

Such documentation shouldn't be difficult to develop and yet will help avoid issues such as https://github.com/ROCm-Developer-Tools/ROCclr/issues/34, making ROCm a more attractive project to packagers.

---

## 评论 (17 条)

### 评论 #1 — saadrahim (2022-06-24T17:28:44Z)

Just an idea, what would you think if ROCm adopted a https://github.com/qt/qt5 style supermodule to show all the components in this repository?

---

### 评论 #2 — bgamari (2022-06-24T18:20:27Z)

@saadrahim, thanks for the quick reply! I can think of a few distinct "shapes" that a "supermodule" might take, only some of which would be useful:

 1. as a crutch to compensate for lacking versioning of the constituent components (since the supermodule captures a set of mutually-compatible components).
 2. as a central build system, having a build script which would build and install the whole stack
 3. as a documentation hub; the submodule references would serve as a laundry-list of components, which would be complemented by the overview- and build-documentation which I describe in the ticket summary.

ROCm has no need for a crutch as described in option (1): ROCm components are currently versioned fairly sensibly, with each component having an easily-found git tag for each ROCm release. I do hope that this does not change.

Option (2) would not be helpful to most packagers since it would be hardly any different from the installation script which AMD already offers.

Option (3) would potentially be useful, although it's not clear that it's necessary. Specifically, the real value of such a repository would be in the documentation that it contains and not in the submodule references. Afterall, it's already fairly easy to identify which repositories are likely needed to build the ROCm stack; the hard part is working out how they relate to one another, how to build them, and what environment configuration is necessary to make the stack work.

Given that it would require work to maintain the submodule references, it's not clear that the value that they offer would outweigh their on-going maintenance cost. I think just adding (and testing/maintaining) build documentation, either in this repository or elsewhere, would already be a great improvement over the status quo.

---

### 评论 #3 — littlewu2508 (2022-06-26T09:57:31Z)

I would also like to ask about the version constraints between each components. Although ROCm packages are released under one version number, they haven't to be the same version. For example, (major) version of hip can be different from packages in https://github.com/ROCmSoftwarePlatform/ as https://github.com/ROCmSoftwarePlatform/rocSOLVER/issues/367#issuecomment-1099821708 suggests. I also observed that rocr-runtime version can be different of hip, and high-level libs. 

---

### 评论 #4 — xuhuisheng (2022-06-26T11:42:28Z)

@littlewu2508 
There might be several teams in ROCm, responsing for related components. And every components of ROCm have their internel lifecycle and version control. for example, ROCm could release with 5.0, 5.1, but some component didn't have changed will create multiple tags on one same commit.

And the version of ROCm could be used to maintain the whole ROCm compatibility. So with the same ROCm version components will be confirmed compatibility. On the otherside, different versions of ROCm version, some of component may can run properly. But no body will guanrantee. It is about one major version in one year. But they never promise compatibilty between minor versions.

And there is no roadmap for ROCm, maybe there is an internal roadmap, but the community cannot have a look. What a pity.

---

### 评论 #5 — xuhuisheng (2022-06-26T11:45:21Z)

@bgamari 
I uploaded my build scripts  for ROCm on ubuntu-20.04.
If you are interesting in it, please have a look.
<https://github.com/xuhuisheng/rocm-build>


---

### 评论 #6 — saadrahim (2022-06-27T18:12:30Z)

AMD is planning to improve build instructions throughout the repositories that constitute ROCm. Besides ROClr, do you know any repository that needs immediate attention?

---

### 评论 #7 — bgamari (2022-06-28T18:51:29Z)

@saadrahim, that is great news.

To give a sense of the problems that packagers run into:

 * [`rocblas`](https://github.com/ROCmSoftwarePlatform/rocBLAS)'s build has quite a few configuration knobs  and yet has no installation documentation, instead pointing to the out-of-date ROCm 4.3 installation guide, which makes no mention of rocBLAS or more generally what `cmake` flags ROCm builds tend to expect. This is generally a 
 * various packages (`rocblas` being one) seem to expect to be installed in `/opt` and assume that their dependencies are installed there as well. Things break with non-obvious errors when this assumption is broken.
 * Happily, `MIOpen`'s `README` does have a fairly complete list of dependencies. However, this list includes non-obvious conditions without stating how to satisfy these conditions (e.g. "[MLIR](https://github.com/ROCmSoftwarePlatform/llvm-project-mlir) - (Multi-Level Intermediate Representation) with its MIOpen dialect to support and complement kernel development.")
 * `MIOpen` seems to optionally depend on `MIOpenTensile` but  (a) does not clarify why a user would want to enable this dependency, and (b) the `MIOpenTensile` repository appears to be archived
 * Judging by failed accesses to `/sys/class/kfd/kfd/topology/nodes/` various `cmake` invocations call `rocm_agent_enumerator`. However, the machine on which packaging is built may not be equipped with AMD hardware. 
 * At a glance it's quite non-obvious that https://github.com/RadeonOpenCompute/llvm-project is not the upstream of ROCm's `mlir` dependency. Rather the correct upstream appears to be https://github.com/ROCmSoftwarePlatform/llvm-project-mlir.  There is also a third LLVM fork, https://github.com/ROCmSoftwarePlatform/llvm-project, the purpose of which is quite mysterious. 

---

### 评论 #8 — cgmb (2022-06-28T18:55:06Z)

While I agree with the overall sentiment, the situation is not quite as dire as you're suggesting.

> This is in large part why [no widely-used Linux distribution](https://repology.org/project/rocm-smi/versions) ships packaging for anything newer than ROCm 4.5.

You won't find new versions of rocm-smi, because that tool was replaced with [rocm-smi-lib](https://repology.org/project/rocm-smi-lib/versions).

@Mystro256 and I are very active on the [Debian](https://lists.debian.org/debian-ai/) and [Fedora](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/VLKVGOBP2NPIB4KF3MXIAQAAYZ7MNNRS/) mailing lists, and we will happily help answer any questions you may have. This is, of course, not a substitute for good documentation, but it should be of some help.

> I would also like to ask about the version constraints between each components. Although ROCm packages are released under one version number, they haven't to be the same version. For example, (major) version of hip can be different from packages in https://github.com/ROCmSoftwarePlatform/ as [ROCmSoftwarePlatform/rocSOLVER#367 (comment)](https://github.com/ROCmSoftwarePlatform/rocSOLVER/issues/367#issuecomment-1099821708) suggests. I also observed that rocr-runtime version can be different of hip, and high-level libs.

In general, the library maintainers don't actually know the version constraints. We could document the actual minimum version constraints as they are now, but there's no dedicated testing being done to empirically verify them, so the documentation will begin to decay almost immediately.

---

### 评论 #9 — cgmb (2022-06-28T19:22:34Z)

> * [`rocblas`](https://github.com/ROCmSoftwarePlatform/rocBLAS)'s build has quite a few configuration knobs  and yet has no installation documentation, instead pointing to the out-of-date ROCm 4.3 installation guide, which makes no mention of rocBLAS or more generally what `cmake` flags ROCm builds tend to expect. This is generally a
> * various packages (`rocblas` being one) seem to expect to be installed in `/opt` and assume that their dependencies are installed there as well. Things break with non-obvious errors when this assumption is broken.

Among the math libraries, rocBLAS and Tensile have particularly convoluted build systems. I know it's a problem and I know how to resolve it, but it's a lot of effort even just to convey to the project teams why these things are important. When you file issues on the corresponding repos with a clear explanation of the problems you're facing, it really helps me to point to the user impact. So, if you have specific problems, please do file issues!

My focus over the past year has been on trying to get HIP packaged on Debian, so I haven't really given that much attention to the problems in rocBLAS. I think that will be changing soon, though. [The hipamd ITP](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1013368) has been filed recently. My expectation is that once we have HIP packaged properly, the next step will be packaging the libraries. At that point, the bugs will come rolling in for rocBLAS.

My personal todo list includes standardizing the CMake build commands used for {roc,hip}{BLAS,SOLVER,FFT,SPARSE,RAND}, but that will be a long process.

---

### 评论 #10 — bgamari (2023-01-10T00:52:03Z)

> AMD is planning to improve build instructions throughout the repositories that constitute ROCm. Besides ROClr, do you know any repository that needs immediate attention?

@saadrahim, has there been any update on this? Looking at the documentation I still don't see any "big picture" documentation explaining the structure of the ROCm stack and how these pieces fit together.

---

### 评论 #11 — cgmb (2023-01-10T19:57:10Z)

> My personal todo list includes standardizing the CMake build commands used for {roc,hip}{BLAS,SOLVER,FFT,SPARSE,RAND}, but that will be a long process.

I discovered that there was already someone working on this with a vision that I agreed with, so I stopped working on it. I'll pick it back up again if their work stalls.

---

### 评论 #12 — bgamari (2023-11-26T20:52:17Z)

Has there been any progress in packaging documentation? I would like to give my attempt at using ROCm another shot but a cursory look at the [current documentation](https://rocmdocs.amd.com/en/latest/index.html) suggests that not much has changed.

To reiterate, even just having a list of the relevant packages, the locations of their upstream repositories, which branches or tags packagers should be pulling from, and their dependency structure would already be a significant improvement over the status quo.

---

### 评论 #13 — cgmb (2023-11-29T00:26:10Z)

> Has there been any progress in packaging documentation?

There has not been anything published. It remains a work-in-progress.

> having a list of the relevant packages, the locations of their upstream repositories, which branches or tags packagers should be pulling from

This information can be found in the [`default.xml`](https://github.com/RadeonOpenCompute/ROCm/blob/rocm-5.7.1/default.xml) file in the main ROCm repo. The tag for each ROCm release is in the form `rocm-X.Y.Z`.

> and their dependency structure would already be a significant improvement over the status quo.

Each library should be documenting what dependencies are required to build it. If you're having trouble building a library, please feel free to open an issue on the library's repo.

There is ongoing work to publish build instructions sufficient to reproduce the AMD-provided binary packages. In the mean time, you may find it helpful to look through the package recipes from other distributions or package managers (e.g., Spack, Gentoo, Arch, Debian, Fedora, Nix).

---

### 评论 #14 — ppanchad-amd (2024-05-08T17:23:34Z)

@bgamari Internal ticket has been created to fix documentation. Thanks!

---

### 评论 #15 — bgamari (2024-06-19T15:08:10Z)

> @bgamari Internal ticket has been created to fix documentation. Thanks!

@ppanchad-amd, thanks. Has there been any progress on addressing this?


---

### 评论 #16 — ppanchad-amd (2024-06-19T15:44:46Z)

@bgamari I will follow up with the internal team and will let you know. Thanks!

---

### 评论 #17 — ppanchad-amd (2024-06-20T17:47:53Z)

@bgamari This is the link to the ROCm Build instructions: https://github.com/ROCm/ROCm?tab=readme-ov-file#build-rocm-from-source 

Also, dependencies are now in the ROCm.mk file:  https://github.com/ROCm/ROCm/tree/develop/tools/rocm-build#overview-for-rocmmk 

Hope this helps. Thanks!

---
