# How to uninstall newer versions like rocm-5.4.3 and packages?

> **Issue #1908**
> **状态**: closed
> **创建时间**: 2023-02-15T17:27:20Z
> **更新时间**: 2023-05-25T17:15:41Z
> **关闭时间**: 2023-05-25T17:15:41Z
> **作者**: Apisteftos
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1908

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- MathiasMagnus

## 描述

I have installed the rocm-5.3.3 and I don't want any more the rocm-5.4.3, because is not compatible with my GPU  RX 480 graphic driver. How can I uninstall the rocm-5.4.3 version? With ` sudo amdgpu-uninstall ` and ` sudo amdgpu-uninstall --rocmrelease=5.4.3 ` doesn't work, I get  ` sudo: amdgpu-uninstall: command not found `. Also the hip is the latest version rocm-5.4.3 and it seems to have a problem while I am trying to train my model with pytorch  GPU is not activated. 

` apt show rocm-libs -a `

<pre>
Package: rocm-libs
Version: 5.3.3.50303-99~22.04
Priority: optional
Section: devel
Maintainer: ROCm Libs Support <rocm-libs.support@amd.com>
Installed-Size: 13,3 kB
Depends: hipblas (= 0.52.0.50303-99~22.04), hipfft (= 1.0.9.50303-99~22.04), hipsolver (= 1.5.0.50303-99~22.04), hipsparse (= 2.3.2.50303-99~22.04), miopen-hip (= 2.18.0.50303-99~22.04), rccl (= 2.12.12.50303-99~22.04), rocalution (= 2.1.2.50303-99~22.04), rocblas (= 2.45.0.50303-99~22.04), rocfft (= 1.0.18.50303-99~22.04), rocrand (= 2.10.9.50303-99~22.04), rocsolver (= 3.19.0.50303-99~22.04), rocsparse (= 2.3.3.50303-99~22.04), rocm-core (= 5.3.3.50303-99~22.04), hipblas-dev (= 0.52.0.50303-99~22.04), hipcub-dev (= 2.10.12.50303-99~22.04), hipfft-dev (= 1.0.9.50303-99~22.04), hipsolver-dev (= 1.5.0.50303-99~22.04), hipsparse-dev (= 2.3.2.50303-99~22.04), miopen-hip-dev (= 2.18.0.50303-99~22.04), rccl-dev (= 2.12.12.50303-99~22.04), rocalution-dev (= 2.1.2.50303-99~22.04), rocblas-dev (= 2.45.0.50303-99~22.04), rocfft-dev (= 1.0.18.50303-99~22.04), rocprim-dev (= 2.10.9.50303-99~22.04), rocrand-dev (= 2.10.9.50303-99~22.04), rocsolver-dev (= 3.19.0.50303-99~22.04), rocsparse-dev (= 2.3.3.50303-99~22.04), rocthrust-dev (= 2.10.9.50303-99~22.04), rocwmma-dev (= 0.7.0.50303-99~22.04)
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 1.000 B
APT-Sources: https://repo.radeon.com/rocm/apt/5.3.3 jammy/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack
</pre>

` hipconfig --full `

<pre>
HIP version  : 5.4.22804-474e8620

== hipconfig
HIP_PATH     : /opt/rocm-5.4.3
ROCM_PATH    : /opt/rocm-5.4.3
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm-5.4.3/include -I/opt/rocm-5.4.3/llvm/bin/../lib/clang/15.0.0 -I/opt/rocm-5.4.3/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm-5.4.3/hsa
HIP_CLANG_PATH   : /opt/rocm-5.4.3/llvm/bin
AMD clang version 15.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.4.3 23045 a29fe425c7b0e5aba97ed2f95f61fd5ecba68aed)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-5.4.3/llvm/bin
AMD LLVM version 15.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver1

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags :  -isystem "/opt/rocm-5.4.3/llvm/lib/clang/15.0.0/include/.." -isystem /opt/rocm-5.4.3/hsa/include -isystem "/opt/rocm-5.4.3/include" -O3
hip-clang-ldflags  :  -L"/opt/rocm-5.4.3/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/home/me/.local/bin:/home/me/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin

== Linux Kernel
Hostname     : me-MS-7A34
Linux me-MS-7A34 5.15.0-60-generic #66-Ubuntu SMP Fri Jan 20 14:29:49 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.1 LTS
Release:	22.04
Codename:	jammy
</pre>









---

## 评论 (4 条)

### 评论 #1 — alexschroeter (2023-02-16T20:56:40Z)

If you just want to uninstall version 5.4.3, you can do that with `sudo apt autoremove rocm-core5.4.3`

Or uninstall everything with `sudo apt autoremove rocm-core amdgpu-dkms` and you probably have to remove the repository that was added by hand. After this, you can just install it as you did before.

You can find the more detailed instructions here https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.3/page/ROCm_Stack_Uninstallation.html

---

### 评论 #2 — SakiiCode (2023-02-19T11:03:09Z)

Use `sudo amdgpu-install --uninstall` instead of `sudo amdgpu-uninstall`. The repository needs to be removed manually afterwards

---

### 评论 #3 — Apisteftos (2023-02-27T11:30:35Z)

Thanks! I used also `sudo apt-get purge hsa* hip* llvm* rocm* ` and uninstalled everything because with `sudo apt autoremove rocm-core5.3.3` doesn't remove the hip version. 

---

### 评论 #4 — alexschroeter (2023-02-27T16:24:21Z)

You are welcome. Don't forget to remove/change your repository, the files should be named something like `rocm.list` and `amdgpu.list` in the `/etc/apt/source.list.d/`directory. 

If you are happy with the answer, you should think about closing the issue.

---
