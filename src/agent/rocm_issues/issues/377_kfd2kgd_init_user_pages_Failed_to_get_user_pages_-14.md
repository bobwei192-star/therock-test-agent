# kfd2kgd: init_user_pages: Failed to get user pages: -14

> **Issue #377**
> **状态**: closed
> **创建时间**: 2018-04-02T12:04:55Z
> **更新时间**: 2018-06-03T14:36:17Z
> **关闭时间**: 2018-06-03T14:36:17Z
> **作者**: zexi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/377

## 描述

Hi, I have run ROCM 1.7 into a Ubuntu 16.04 VM by passthrough GPU.
GPU: amd FirePro S7150
CPU: Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz

When I run /opt/rocm/hip/samples/0_Intro/square sample, below error happend.

```bash
$ cd /opt/rocm/hip/samples/0_Intro/square && make
$ ./square.out

Backtrace:
0x00007f107e3e05e6:     Kalmar::HSAContext::initPrintfBuffer() + 0x126
0x00007f107e3c6378:     Kalmar::HSAContext::HSAContext() + 0xa68
0x00007f107e3c41b6:     _GLOBAL__sub_I_mcwamp_hsa.cpp + 0x5f6
0x00007f10816cc6ba:     _dl_rtld_di_serinfo + 0x706a
0x00007f10816cc7cb:     _dl_rtld_di_serinfo + 0x717b
0x00007f10816d18e2:     _dl_find_dso_for_object + 0xcf2
0x00007f10816cc564:     _dl_rtld_di_serinfo + 0x6f14
0x00007f10816d0da9:     _dl_find_dso_for_object + 0x1b9
0x00007f10814b8f09:     <unknown function> + 0x1b9
0x00007f10816cc564:     _dl_rtld_di_serinfo + 0x6f14
0x00007f10814b9571:     dlerror + 0x2c1
0x00007f10814b8fa1:     dlopen + 0x31
0x00007f10806ce661:     Kalmar::CLAMP::GetOrInitRuntime() + 0x261
0x00007f10806cf5ab:     Kalmar::KalmarBootstrap::KalmarBootstrap() + 0x8b
0x00007f10806cf4f9:     __hcc_shared_library_init + 0x29
0x00007f10816cc6ba:     _dl_rtld_di_serinfo + 0x706a
0x00007f10816cc7cb:     _dl_rtld_di_serinfo + 0x717b
0x00007f10816bcc6a:     <unknown function> + 0x717b

### HCC STATUS_CHECK Error: HSA_STATUS_ERROR (0x1000) at file:mcwamp_hsa.cpp line:3648
Aborted (core dumped)
```

dmesg show below.
```bash
dmesg  | tail -n 3
[  165.695012] kfd2kgd: init_user_pages: Failed to get user pages: -14
[  247.468531] kfd2kgd: init_user_pages: Failed to get user pages: -14
[  420.439295] kfd2kgd: init_user_pages: Failed to get user pages: -14
```

However, when I run /opt/rocm/hsa/sample is ok.
```bash
$ cd /opt/rocm/hsa/sample && make
$ ./vector_copy
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx802.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
Passed validation.
Freeing kernel argument memory buffer succeeded.
Destroying the signal succeeded.
Destroying the executable succeeded.
Destroying the code object succeeded.
Destroying the queue succeeded.
Freeing in argument memory buffer succeeded.
Freeing out argument memory buffer succeeded.
Shutting down the runtime succeeded.
```

So please let me know how can I make ROCM work in KVM by passthrough amd GPU?
Thanks a lot.

---

## 评论 (3 条)

### 评论 #1 — gstoner (2018-04-03T22:58:54Z)

Did you look at this http://rocm-documentation.readthedocs.io/en/latest/ROCm_Virtualization_Containers/ROCm-Virtualization-&-Containers.html#kvm-passthrough 

---

### 评论 #2 — zexi (2018-04-08T13:14:12Z)

Sorry for the late response, I followed the kvm-passthrough guide still get the the problem.

I have also test it on the host that run the kvm, dmesg still show:

[  444.255690] kfd2kgd: init_user_pages: Failed to get user pages: -14

Host CPU is 'Intel(R) Xeon(R) CPU E5-2678 v3 @ 2.50GHz', GPU is '[AMD/ATI] Tonga XT GL [FirePro S7150]', are thoese CPU and GPU supported by ROCM?

---

### 评论 #3 — gstoner (2018-06-03T14:36:17Z)

We have limited support for Tonga. 

---
