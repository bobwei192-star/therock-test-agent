# Error while installing rocm-dkms

> **Issue #515**
> **状态**: closed
> **创建时间**: 2018-08-25T18:59:41Z
> **更新时间**: 2018-09-01T01:19:01Z
> **关闭时间**: 2018-08-25T19:09:08Z
> **作者**: babujoym
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/515

## 描述

I am getting the below error when installing rocm-dkmsam 

I am using Ubuntu 16.04 LTS

```
/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_atpx_handler.c:577:19: error: initialization from incompatible pointer type [-Werror=incompatible-pointer-types]
   .get_client_id = amdgpu_atpx_get_client_id,
                    ^
 /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_atpx_handler.c:577:19: note: (near initialization for ‘amdgpu_atpx_handler.get_client_id’)
   CC [M]  /var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/../powerplay/smumgr/smumgr.o
 cc1: some warnings being treated as errors
 scripts/Makefile.build:332: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_atpx_handler.o' failed
 make[2]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_atpx_handler.o] Error 1
 make[2]: *** Waiting for unfinished jobs....
 scripts/Makefile.build:606: recipe for target '/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu' failed
 make[1]: *** [/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu] Error 2
 Makefile:1552: recipe for target '_module_/var/lib/dk
[error.log](https://github.com/RadeonOpenCompute/ROCm/files/2320949/error.log)
ms/amdgpu/1.8-192/build' failed
 make: *** [_module_/var/lib/dkms/amdgpu/1.8-192/build] Error 2
 make: Leaving directory '/usr/src/linux-headers-4.15.0-33-generic'
DKMSKernelVersion: 4.15.0-33-generic
Date: Sat Aug 25 23:51:42 2018
DuplicateSignature: dkms:rock-dkms:1.8-192:/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_atpx_handler.c:577:19: error: initialization from incompatible pointer type [-Werror=incompatible-pointer-ty
pes]
```
Attached is the full log.

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-08-25T19:09:08Z)

Dupe of #510. We're looking into this -- sorry about the difficulties. Kernel 4.15.0-32 and below should work, if you're OK temporarily downgrading your kernel version. We will have -33 working soon.

---

### 评论 #2 — babujoym (2018-09-01T01:13:39Z)

Yea that would be good. Thanks. 
Please let me know when the the Kernel is fixed

---

### 评论 #3 — jlgreathouse (2018-09-01T01:18:24Z)

#510 was fixed early yesterday with the release of ROCm 1.8.3.

---
