# fresh Ubuntu install without GPU not finding OpenCL platform

> **Issue #659**
> **状态**: closed
> **创建时间**: 2019-01-03T15:05:21Z
> **更新时间**: 2019-01-03T18:48:29Z
> **关闭时间**: 2019-01-03T18:48:29Z
> **作者**: Noerr
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/659

## 描述

I tried to do a basic setup to test ROCm for OpenCL for CPU-only (initially).  clGetPlatformIDs is returning -1001.  Can anyone confirm these steps?


**Test setup:**
Fresh install of Ubuntu 18.04 **in a virtual machine**, running on Intel i7 v4 CPU with 4 cores, no discrete GPU.


**Steps:**

```
$ sudo apt update
$ sudo apt install rocm-dkms
```
 Succes. Reboot.

```
$ /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call retured 4104
```

```
$ /opt/rocm/opencl/bin/x86_64/clinfo
ERROR: clGetPlatformIDs(-1001)
```

`$ strace /opt/rocm/opencl/bin/x86_64/clinfo`
Shows that **libamdoclcl64.so** is not found in a couple dozen paths right before exit 1.


Did I miss something?  Other packages are mentioned on the install guide.

`$ sudo apt install rock-dkms`
"already the newest version" 0 upgraded, 0 newly installed.

`$ sudo apt install rocm-opencl-dev`
"already the newest version" 0 upgraded, 0 newly installed.

`$ sudo apt-get install dkms rock-dkms rocm-opencl`
for each ... "already the newest version" 0 upgraded, 0 newly installed.


I'm not sure what else to try.  Where should libamdoclcl64.so be located?   Would it be installed if I don't have a supported GPU?


---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2019-01-03T16:26:54Z)

The ROCm OpenCL runtime does not support CPUs as a valid target, so if you do not have a valid GPU in your system, `clinfo` will find no platforms and will fail. The OpenCL runtime will look in various paths for `libamdoclcl64.so` but if it doesn't find it it should fall back to looking for `libamdocl64.so` So that's not a problem.

While `rocminfo` may be able to find your CPUs as a valid HSA agent, I would guess that the call to `hsa_init()` is failing because you're running inside a virtual machine and the runtime cannot properly enumerate whatever devices it is looking for.

---

### 评论 #2 — Noerr (2019-01-03T16:43:11Z)

Perhaps you can expand on the first sentence more explicitly please.  Are you saying there's no OpenCL CPU target support in the whole ROC-whatever ecosystem?
I came to ROCm because I understood AMDAPPSDK was discontinued but redirected to this project.

---

### 评论 #3 — jlgreathouse (2019-01-03T16:56:42Z)

Correct, the ROCm OpenCL runtime does not support CPU targets. As far as I know, the OpenCL runtimes in the Linux/amdgpu-pro and [Windows](https://community.amd.com/message/2878639) software stacks also no longer support CPU targets, but I don't actively work in those areas so I can't verify that at this time.

---

### 评论 #4 — Noerr (2019-01-03T18:48:29Z)

Ok, thank you for the clarification.  I submitted a pull request to enhance the README. I think language like this would have saved me several hours down a dead-end path.
The same language can be applied to the Wiki, which I am attaching.
[Home.txt](https://github.com/RadeonOpenCompute/ROCm/files/2724958/Home.txt)



---
