# next step ??

> **Issue #585**
> **状态**: closed
> **创建时间**: 2018-10-24T04:16:41Z
> **更新时间**: 2018-12-24T22:04:30Z
> **关闭时间**: 2018-12-24T22:04:30Z
> **作者**: kenjo
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/585

## 标签

- **Question** (颜色: #cc317c)

## 描述

So after running repo I have 13 different projects but no information on the next step.

I guess the linux driver is self contained so I could probably go ahead and compile that one but after that
what would I then compile? I can't find any dependency information or any help in configuring the different builds.

atmi
compiler-rt
hcc
hcc-clang-upgrade
HIP
HIP-Examples
lld
llvm
ROCK-Kernel-Driver
ROCm-Device-Libs
ROCR-Runtime
ROC-smi
ROCT-Thunk-Interface



---

## 评论 (9 条)

### 评论 #1 — jlgreathouse (2018-10-24T04:47:07Z)

If you just want a ROCm installation, and if you're using a supported operating system, you can install from our .deb or .rpm packages, as per [the directions on the main repository README](https://github.com/RadeonOpenCompute/ROCm#installing-from-amd-rocm-repositories).

If you're looking to compile everything from source, each project has its own set of directions on that project's github page. If you'd like, you could follow the dependencies in the packages on repo.radeon.com if you specifically want to install things in that order.

I'll say that for the kernel driver, you're probably better off grabbing the .deb or .rpm file, because those contain the source code for the driver nicely packaged into a DKMS installation. This will put the source specifically for the driver on your system and make a DKMS module that will automatically rebuild whenever you upgrade your kernel. The repo sync will instead pull a snapshot of the entire Linux kernel, with the driver in its own directory.

Note also that the repo sync directions shown on the front page are specifically labeled how to get the source code, not how to rebuild ROCm from scratch. :) There have been requests for a full set of scripts to rebuild ROCm from the GitHub repos, but I haven't had time to write them. Our internal build system for creating our .deb and .rpm files are a bit more complex than just pulling from GitHub, since these same build systems handle a lot of our closed-source software builds as well.

That said, all of the ROCm repos should contain working directions for rebuilding each project.

A quick overview of some basic dependencies:
- The kernel driver is first. As I mentioned, getting the DKMS source directory out of one of our packages is probably the easiest way to build this.
- The [ROCT-Thunk-Interface](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface) is required for anything to talk to the driver, so you should probably build it after the driver.
- The [ROCR-Runtime](https://github.com/RadeonOpenCompute/ROCR-Runtime) is how most of our software talks to the ROCm lower-level mechanisms, so it's next.
  - The build directions are in the ./src/ directory
- You can install [ROC-smi](https://github.com/RadeonOpenCompute/ROC-smi) any time after the driver, as it directly talks to the driver through the Linux sysfs.
- You might install the [OpenCL runtime](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime) next.
  - [These directions](https://github.com/RadeonOpenCompute/ROCm/issues/537#issuecomment-423311687) may be a little easier to use than the ones on the OpenCL runtime README.
- You should install [HCC](https://github.com/RadeonOpenCompute/hcc) before [HIP](https://github.com/ROCm-Developer-Tools/HIP), since HIP currently relies on the HCC compiler.
- Once you've installed HIP you can install the [HIP examples](https://github.com/ROCm-Developer-Tools/HIP-Examples).
- I believe [ATMI](https://github.com/RadeonOpenCompute/atmi) can be installed at any time after you have ROCr installed.

Note that the HCC and OpeNCL compiler builds will pick out particular branches of the lld, llvm, hcc-clang-upgrade, and compiler-rt repos, so you don't need to compile those separately.

You may also want to build other software that is normally installed as part of the `rocm-dkms` package:
- [rocminfo](https://github.com/RadeonOpenCompute/rocminfo)
- [rocm-bandwidth-test](https://github.com/RadeonOpenCompute/rocm_bandwidth_test)
- [ROCM device libs](https://github.com/RadeonOpenCompute/ROCm-Device-Libs)
- [The various ROCm libraries](https://github.com/ROCmSoftwarePlatform/)


---

### 评论 #2 — kenjo (2018-10-24T12:32:53Z)

I'm just interested in testing this without destroying my OS installation. I'm not a big fan of installing deb packages since it can be hard to get back to the before state. Much better to compile it with a custom --prefix value so its installed outside the normal OS. 

So I'm actually on 4.19 now so maybe I do not need to compile a different version as the one tag with roc-1.9.1 was a 4.15 based kernel. but what is the kernel config options that has to be set and what is the .ko files produces

I'm looking into the readme.md from ROCT-Thunk-Interface. and it tells me to 

> The ROCt library is not a standalone product and requires that you have the correct ROCk driver set installed. We recommend reading the full compatibility and installation details which are available in the ROCk github:
> 
> https://github.com/RadeonOpenCompute/ROCK-Radeon-Open-Compute-Kernel-Driver

but that is just the linux kernel. no installation details at all. how to configure the kernel ??

any way I ignored the kernel but did not get very far 
```
mkdir install
export rocm_install=`pwd`/install

mkdir ROCT-Thunk-Interface_build
cd ROCT-Thunk-Interface_build/
cmake -DCMAKE_INSTALL_PREFIX=$rocm_install ../ROCT-Thunk-Interface
make
make install
make install-dev

mkdir ROCR-Runtime_build
cd ROCR-Runtime_build
cmake -DCMAKE_INSTALL_PREFIX=$rocm_install -DCMAKE_INCLUDE_PATH=$rocm_install/include/  ../ROCR-Runtime/src/
make
```
here I get an error. did not have time to investigate. 
```
[ 63%] Building CXX object CMakeFiles/hsa-runtime64.dir/core/runtime/runtime.cpp.o
/home/kenjo/proj/rocm/ROCR-Runtime/src/core/runtime/runtime.cpp: In member function ‘void core::Runtime::SetLinkCount(size_t)’:
/home/kenjo/proj/rocm/ROCR-Runtime/src/core/runtime/runtime.cpp:260:71: error: ‘void* memset(void*, int, size_t)’ clearing an object of non-trivial type ‘__gnu_cxx::__alloc_traits<std::allocator<core::Runtime::LinkInfo>, core::Runtime::LinkInfo>::value_type’ {aka ‘struct core::Runtime::LinkInfo’}; use assignment or value-initialization instead [-Werror=class-memaccess]
          link_matrix_.size() * sizeof(hsa_amd_memory_pool_link_info_t));
                                                                       ^
In file included from /home/kenjo/proj/rocm/ROCR-Runtime/src/core/runtime/runtime.cpp:43:
/home/kenjo/proj/rocm/ROCR-Runtime/src/core/inc/runtime.h:97:10: note: ‘__gnu_cxx::__alloc_traits<std::allocator<core::Runtime::LinkInfo>, core::Runtime::LinkInfo>::value_type’ {aka ‘struct core::Runtime::LinkInfo’} declared here
   struct LinkInfo {
          ^~~~~~~~
cc1plus: all warnings being treated as errors
make[2]: *** [CMakeFiles/hsa-runtime64.dir/build.make:349: CMakeFiles/hsa-runtime64.dir/core/runtime/runtime.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/hsa-runtime64.dir/all] Error 2
make: *** [Makefile:152: all] Error 2
```

---

### 评论 #3 — kenjo (2018-10-24T12:33:24Z)

note to self. use preview before posting. 

---

### 评论 #4 — jlgreathouse (2018-10-24T14:25:44Z)

1. If you're using a new kernel (such as 4.19) you do not need to install or build the ROCK kernel driver, as enough features from the `amdgpu`, `amdkfd`, and related drivers that come as part of the ROCK packages have been [upstreamed into the Linux kernel](https://github.com/RadeonOpenCompute/ROCm#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels).
    1. That said, I'll once again reiterate that if you want to build the ROCK drivers yourself, you're probably best off downloading the .deb or .rpm image and extracting the DKMS scripts and source. The rock-dkms packages install the source code onto your system and rebuild it to make a new module every time you update your kernel. That said, the ROCK github repo contains the same source code, but as part of the Linux kernel. You could choose to build the appropriate modules out of that source tree if you wanted.
1. Your ROCr problem with new compilers [has been reported](https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/44) and is known. Note that AMD makes no claim of guarantee that our source code will work with all compilers at all times -- I would guess if you're using GCC 8+ you're not working with an AMD-supported operating system. That said, that report includes a patch you can apply that should fix your compilation issue.

---

### 评论 #5 — kenjo (2018-10-24T14:47:56Z)

So would it be possible to add that patch to ROCR-Runtime in a roc-1.9.1-gcc8 branch or something? 
If that had been done I would have notice that and just changed over to that branch. 

---

### 评论 #6 — jlgreathouse (2018-10-24T14:51:16Z)

Your question is addressed in that issue.

---

### 评论 #7 — preda (2018-10-25T09:00:10Z)

Note that ROCm 1.9.1 may have some issues on Linux kernel 4.19, see https://github.com/RadeonOpenCompute/ROCm/issues/577


---

### 评论 #8 — jlgreathouse (2018-12-21T01:36:56Z)

Hi @kenjo 

You may be interested in the newly released Experimental ROC project. This includes scripts and tools for both installing ROCm (so you don't have to type stuff by hand from our README files), but also a full script of scripts for rebuilding ROCm from source.

This allows you to build individual ROCm components and save them into local directories (e.g. to test patches), build and install into other locations (like `/opt/rocm/`) and build .deb and .rpm packages for these components. There are also tools to build and install things "in order" so you don't run into any dependency issues (e.g. if you are not building packages and letting your package manager handle them for you).

https://github.com/RadeonOpenCompute/Experimental_ROC

I am currently in the process of updating the main ROCm README and the ROCm `default.xml` file to better address the "downloading 13 random repos with no other directions about what to do" that you brought up. But setting that aside, you should be able to use the tools in the above repository to build anything you want from ROCm.

---

### 评论 #9 — jlgreathouse (2018-12-24T22:04:30Z)

Hi @kenjo 

I have updated the the ROCm [README](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md), [website](https://rocm.github.io/ROCmInstall.html), and [documentation](https://rocm-documentation.readthedocs.io/en/latest/Installation_Guide/Installation-Guide.html) to better address your questions.

In particular:

- I have updated [this section](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#the-latest-rocm-platform---rocm-20) which explains what software is is part of ROCm and where you can get its source code.
- In addition, I updated [this section](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#rocm-binary-package-structure) which matches that software to the binary packages which install it when you are not building from source.
- I updated [the section which describes how to get source code for various ROCm projects](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#getting-rocm-source-code) to also include [a small section](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#building-the-rocm-source-code) that points to information on where to go to build each of the packages. The [Experimental ROC](https://github.com/RadeonOpenCompute/Experimental_ROC) project is a much more comprehensive walkthrough of how to build all of this software.
- I also updated the ROCm [repo manifest file](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/default.xml) to add a lot of missing ROCm software and to have it pull the correct versions that are part of the current ROCm release. This should match up to the information presented in [the section describing the current ROCm software collection](https://github.com/RadeonOpenCompute/ROCm/tree/roc-2.0.0#the-latest-rocm-platform---rocm-20).

---
