# HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.

> **Issue #1583**
> **状态**: closed
> **创建时间**: 2021-10-06T16:28:33Z
> **更新时间**: 2021-10-08T16:32:30Z
> **关闭时间**: 2021-10-07T13:05:01Z
> **作者**: alexschroeter
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1583

## 描述

Hi,

I installed ROCm from the repository on a CentOS but rocminfo gives me the error "HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu." for each of the GPUs.

The message (to me) suggested a mismatch between the driver and rocm but it seems fine to me. Am I missing something here? The GPUs should be supported. 

lsb_release -a
```
LSB Version:    :core-4.1-amd64:core-4.1-noarch
Distributor ID: CentOS
Description:    CentOS Linux release 8.4.2105
Release:        8.4.2105
Codename:       n/a
```

dkms status
```
amdgpu, 4.3-52.el7: added
```

rocminfo
```
ROCk module is loaded
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
 
HSA System Attributes
 
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE

 
HSA Agents
 

Agent 1
 
CPU 
...
*** Done ***
```


/opt/rocm/hip/bin/hipconfig
```
HIP version  : 4.3.21300-5bbc51d8

== hipconfig
HIP_PATH     : /opt/rocm-4.3.0/hip
ROCM_PATH    : /opt/rocm-4.3.0
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I"/opt/rocm-4.3.0/hip/include" -I"/opt/rocm-4.3.0/llvm/bin/../lib/clang/13.0.0" -I/opt/rocm-4.3.0/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm-4.3.0/hsa
HIP_CLANG_PATH   : /opt/rocm-4.3.0/llvm/bin
clang version 13.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-4.3.0 21295 f2943f684437d2c1143a56e418d29fc6b3314072)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-4.3.0/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 13.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
 -std=c++11 -isystem "/opt/rocm-4.3.0/llvm/lib/clang/13.0.0/include/.." -isystem /opt/rocm-4.3.0/hsa/include -isystem "/opt/rocm-4.3.0/hip/include" -O3
hip-clang-ldflags  : HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
HSA Error:  Incompatible kernel and userspace, Vega 20 WKS GL-XE [Radeon Pro VII] disabled. Upgrade amdgpu.
--driver-mode=g++ -L"/opt/rocm-4.3.0/hip/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/usr/share/Modules/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin

== Linux Kernel
Hostname     : dev.local
Linux dev.local 4.18.0-305.19.1.el8_4.x86_64 #1 SMP Wed Sep 15 15:39:39 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
LSB Version:    :core-4.1-amd64:core-4.1-noarch
Distributor ID: CentOS
Description:    CentOS Linux release 8.4.2105
Release:        8.4.2105
Codename:      n/a
```

Thanks for the help.

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-10-07T13:05:01Z)

Hi @alexschroeter 
Thanks for reaching out.
I certainly understood the problem.
We do not support CentOS 8.4(4.18.0-315) with ROCm 4.3.
ROCm 4.3 supports CentOS 8.3(4.18.0-193) and hence request to try with CentOS 8.3. 
For all supported OSes, please look at [https://github.com/RadeonOpenCompute/ROCm#supported-operating-systems](url)
Hope this helps.
Feel free to open a new issue, if any, for quick resolutions.
Thank you.

---

### 评论 #2 — alexschroeter (2021-10-08T16:32:30Z)

In case anybody comes up with the same problem. Here is what happened:

During the installation process the build with dkms of amdgpu failed which I didn't realize because it was buried in the output. Because I saw the correct version of amdgpu being used by dkms I didn't pay more attention to the install process.

In the hope of debugging my problem I was looking at the module which I was unable to remove with dkms. Further investigation let me to the realization that the kernel module I was using (modinfo amdgpu) was a file created over a month ago. 

With this information I uninstalled everything and reinstalled rocm-dkms. Here I noticed the build failed due to a signing problem where /root/dkms.key didn't exist. I was able to solve the problem by uncommenting the "/lib/modules/"$1"/build/scripts/sign-file sha512 /root/dkms.key /root/dkms.der "$2"" in /etc/dkms/sign_helper.sh.

After this the build finished successfully and I am now using the correct kernel module. I don't know if this would cause issues if you have secure boot enabled.

---
