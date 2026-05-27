# Any binary version planned for Linux OSs?

> **Issue #1142**
> **状态**: closed
> **创建时间**: 2020-06-08T09:15:58Z
> **更新时间**: 2020-06-12T13:51:49Z
> **关闭时间**: 2020-06-12T13:51:49Z
> **作者**: xcom169
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1142

## 描述

Hello All!

I know it's much bigger than a simple opencl runtime, but it's crazy it needs 40 GB Ram, and 150 GB HDD to build ROCm. It's very difficult to build the package on a normal PC. 
Can't we just install the binary files ?



---

## 评论 (4 条)

### 评论 #1 — ableeker (2020-06-09T18:15:50Z)

I do believe we can. It depends on what you want to do, of course, but I'm using the OpenCL part from ROCm, and I haven't yet felt the need to build ROCm from source. If you just need the OpenCL part of ROCm, you can install rocm-opencl, or rocm-opencl-dev. If you need more than that, you can install rocm-dkms, or rocm-dev. These are all binary packages.

Won't that do the trick? Do you need to build ROCm from source?

---

### 评论 #2 — xcom169 (2020-06-09T20:32:43Z)

I installed ROCm from rocm-opencl-runtime AUR, but it needed the llvm-amdgpu which is huge to build. 

Do you know any other package for Arch/Manjaro Linux which only contains the opencl runtime binary? 

---

### 评论 #3 — ableeker (2020-06-10T17:43:13Z)

I see! The binaries are readily available, but I can only find DEB and RPM packages. Unfortunately, I don't know Arch/Manjaro, and am unable to tell you if they can be installed, and how to do that.

All I know is that ROCm 3.5.0 DEB package 'opencl-rocm' can be installed under Ubuntu by

`sudo apt install rocm-opencl`

It will install the following packages from http://repo.radeon.com/rocm/apt/debian/pool/main/:

`comgr_1.6.0.143-rocm-rel-3.5-30-e24e8c1_amd64.deb`
`hsa-ext-rocr-dev_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.deb`
`hsa-rocr-dev_1.1.30500.0-rocm-rel-3.5-30-def83d8_amd64.deb`
`hsakmt-roct_1.0.9-347-gd4b224f_amd64.deb`

And possibly the following package from http://archive.ubuntu.com/ubuntu, or more likely the AUR:

`libelf-dev_0.176-1.1build1`

After unpacking these packages in their folders, it does run a post-install script, however, all it does is the following:

`echo /opt/rocm/opencl/lib > /etc/ld.so.conf.d/x86_64-rocm-opencl.conf`
`mkdir -p /etc/OpenCL/vendors && (echo libamdocl64.so > /etc/OpenCL/vendors/amdocl64.icd)`
`INSTALL_PATH=/opt/rocm-3.5.0/opencl`
`ROCM_LIBPATH=/opt/rocm-3.5.0/lib`
`mkdir -p ${ROCM_LIBPATH}`
`ln -s -f -r ${INSTALL_PATH}/lib/libOpenCL.so ${ROCM_LIBPATH}/libOpenCL.so`
`ln -s -f -r ${INSTALL_PATH}/lib/libOpenCL.so.1 ${ROCM_LIBPATH}/libOpenCL.so.1`
`ln -s -f -r ${INSTALL_PATH}/lib/libOpenCL.so.1.2 ${ROCM_LIBPATH}/libOpenCL.so.1.2`

The hsakmt package adds another command:

`echo /opt/rocm/lib > /etc/ld.so.conf.d/x86_64-libhsakmt.conf`

So after this you'll need to run ldconfig, of course.

Then there's the usual stuff. You'll need to create the kfd rule. Then you'll have to add the user to the video group (and/or the render group?). And clinfo segfaults if libtinfo5 hasn't been installed.

Would it be possible to do this on Arch/Manjaro?

---

### 评论 #4 — xcom169 (2020-06-12T13:51:49Z)

It's a good idea. I think it's possible to convert the .DEB package to Arch Linux (AUR).
I'll consult an AUR package maintainer about this idea. 
Hopefully it can be done easily. 

---
