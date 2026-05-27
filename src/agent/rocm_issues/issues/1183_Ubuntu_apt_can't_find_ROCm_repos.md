# Ubuntu: apt can't find ROCm repos

> **Issue #1183**
> **状态**: closed
> **创建时间**: 2020-07-23T17:38:09Z
> **更新时间**: 2020-07-24T20:30:43Z
> **关闭时间**: 2020-07-24T20:30:43Z
> **作者**: nufsty2
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1183

## 描述

After installing ROCm, I'm getting these errors with apt:
```
$ sudo apt upgrade -y
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  comgr hip-base hip-doc hip-rocclr hip-samples hsa-ext-rocr-dev hsa-rocr-dev rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake rocm-dbgapi rocm-debug-agent rocm-dev rocm-device-libs rocm-dkms
  rocm-gdb rocm-smi rocm-smi-lib64 rocm-utils rocminfo roctracer-dev
22 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 85.8 MB of archives.
After this operation, 54.3 kB of additional disk space will be used.
Ign:1 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms-firmware all 1:3.5-32
Ign:2 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms all 1:3.5-32
Ign:3 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 comgr amd64 1.6.0.143-rocm-rel-3.5-34-e24e8c1
Ign:4 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-doc amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
Ign:5 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-samples amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
Ign:6 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-rocr-dev amd64 1.1.30501.0-rocm-rel-3.5-34-def83d8
Ign:7 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-ext-rocr-dev amd64 1.1.30501.0-rocm-rel-3.5-34-def83d8
Ign:8 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocminfo amd64 1.30501.0
Ign:9 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-clang-ocl amd64 0.5.0.51-rocm-rel-3.5-34-74b3b81
Ign:10 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-utils amd64 3.5.1-34
Ign:11 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-rocclr amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
Ign:12 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-base amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
Ign:13 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-cmake amd64 0.3.0.153-rocm-rel-3.5-34-1d1caa5
Ign:14 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dbgapi amd64 0.21.2-rocm-rel-3.5-34
Ign:15 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-debug-agent amd64 1.0.0.30501-rocm-rel-3.5-34
Ign:16 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-device-libs amd64 1.0.0.586-rocm-rel-3.5-34-ab93876
Ign:17 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-gdb amd64 9.1-rocm-rel-3.5-34
Ign:18 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi amd64 1.0.0-201-rocm-rel-3.5-34-gcdfbef4
Ign:19 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi-lib64 amd64 2.4.0.15.rocm-rel-3.5-34-2143bc3
Get:20 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 roctracer-dev amd64 1.0.0 [393 kB]
Ign:20 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 roctracer-dev amd64 1.0.0
Ign:21 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dev amd64 3.5.1-34
Ign:22 http://smd-server/repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dkms amd64 3.5.1-34
Err:1 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms-firmware all 1:3.5-32
  404  Not Found [IP: 192.168.1.253 80]
Err:2 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rock-dkms all 1:3.5-32
  404  Not Found [IP: 192.168.1.253 80]
Err:3 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 comgr amd64 1.6.0.143-rocm-rel-3.5-34-e24e8c1
  404  Not Found [IP: 192.168.1.253 80]
Err:4 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-doc amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 192.168.1.253 80]
Err:5 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-samples amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 192.168.1.253 80]
Err:6 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-rocr-dev amd64 1.1.30501.0-rocm-rel-3.5-34-def83d8
  404  Not Found [IP: 192.168.1.253 80]
Err:7 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hsa-ext-rocr-dev amd64 1.1.30501.0-rocm-rel-3.5-34-def83d8
  404  Not Found [IP: 192.168.1.253 80]
Err:8 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocminfo amd64 1.30501.0
  404  Not Found [IP: 192.168.1.253 80]
Err:9 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-clang-ocl amd64 0.5.0.51-rocm-rel-3.5-34-74b3b81
  404  Not Found [IP: 192.168.1.253 80]
Err:10 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-utils amd64 3.5.1-34
  404  Not Found [IP: 192.168.1.253 80]
Err:11 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-rocclr amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 192.168.1.253 80]
Err:12 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 hip-base amd64 3.5.20231.5357-rocm-rel-3.5-34-93097e0
  404  Not Found [IP: 192.168.1.253 80]
Err:13 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-cmake amd64 0.3.0.153-rocm-rel-3.5-34-1d1caa5
  404  Not Found [IP: 192.168.1.253 80]
Err:14 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dbgapi amd64 0.21.2-rocm-rel-3.5-34
  404  Not Found [IP: 192.168.1.253 80]
Err:15 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-debug-agent amd64 1.0.0.30501-rocm-rel-3.5-34
  404  Not Found [IP: 192.168.1.253 80]
Err:16 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-device-libs amd64 1.0.0.586-rocm-rel-3.5-34-ab93876
  404  Not Found [IP: 192.168.1.253 80]
Err:17 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-gdb amd64 9.1-rocm-rel-3.5-34
  404  Not Found [IP: 192.168.1.253 80]
Err:18 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi amd64 1.0.0-201-rocm-rel-3.5-34-gcdfbef4
  404  Not Found [IP: 192.168.1.253 80]
Err:19 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-smi-lib64 amd64 2.4.0.15.rocm-rel-3.5-34-2143bc3
  404  Not Found [IP: 192.168.1.253 80]
Get:20 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 roctracer-dev amd64 1.0.0 [393 kB]
Err:20 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 roctracer-dev amd64 1.0.0
  File has unexpected size (393098 != 393204). Mirror sync in progress? [IP: 13.82.220.49 80]
  Hashes of expected file:
   - SHA256:1b1e06e38e171ddb04eecb859bd45e2327a33722207b264aade52456f73511e1
   - SHA1:2c3a0bfacb9a3300c377f06fbcb958c137f2f770 [weak]
   - MD5Sum:e2950838fab61963549c74b79f6bd800 [weak]
   - Filesize:393204 [weak]
Err:21 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dev amd64 3.5.1-34
  404  Not Found [IP: 192.168.1.253 80]
Err:22 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 rocm-dkms amd64 3.5.1-34
  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms-firmware_3.5-32_all.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rock-dkms/rock-dkms_3.5-32_all.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/c/comgr/comgr_1.6.0.143-rocm-rel-3.5-34-e24e8c1_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-doc/hip-doc_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-samples/hip-samples_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-rocr-dev/hsa-rocr-dev_1.1.30501.0-rocm-rel-3.5-34-def83d8_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-ext-rocr-dev/hsa-ext-rocr-dev_1.1.30501.0-rocm-rel-3.5-34-def83d8_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocminfo/rocminfo_1.30501.0_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-clang-ocl/rocm-clang-ocl_0.5.0.51-rocm-rel-3.5-34-74b3b81_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-utils/rocm-utils_3.5.1-34_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-rocclr/hip-rocclr_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/h/hip-base/hip-base_3.5.20231.5357-rocm-rel-3.5-34-93097e0_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-cmake/rocm-cmake_0.3.0.153-rocm-rel-3.5-34-1d1caa5_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dbgapi/rocm-dbgapi_0.21.2-rocm-rel-3.5-34_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-debug-agent/rocm-debug-agent_1.0.0.30501-rocm-rel-3.5-34_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-device-libs/rocm-device-libs_1.0.0.586-rocm-rel-3.5-34-ab93876_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-gdb/rocm-gdb_9.1-rocm-rel-3.5-34_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-smi/rocm-smi_1.0.0-201-rocm-rel-3.5-34-gcdfbef4_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-smi-lib64/rocm-smi-lib64_2.4.0.15.rocm-rel-3.5-34-2143bc3_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/roctracer-dev/roctracer-dev_1.0.0_amd64.deb  File has unexpected size (393098 != 393204). Mirror sync in progress? [IP: 13.82.220.49 80]
   Hashes of expected file:
    - SHA256:1b1e06e38e171ddb04eecb859bd45e2327a33722207b264aade52456f73511e1
    - SHA1:2c3a0bfacb9a3300c377f06fbcb958c137f2f770 [weak]
    - MD5Sum:e2950838fab61963549c74b79f6bd800 [weak]
    - Filesize:393204 [weak]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dev/rocm-dev_3.5.1-34_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Failed to fetch http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dkms/rocm-dkms_3.5.1-34_amd64.deb  404  Not Found [IP: 192.168.1.253 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
```

I've tried with --fix-missing and it's still broken.

---

## 评论 (2 条)

### 评论 #1 — ableeker (2020-07-24T19:59:34Z)

This seems to be caused by an issue with 3.5.1. Looks like they want us to go for 3.5.0 for the moment. Someone has likely tried to point the repository back again to 3.5.0, but the result is that the file sizes aren't correct anymore, because somewhere they refer to the wrong files. That's why I'm pointing in rocm.list to the specific version (I've gone for 3.5.1) instead of the general debian. That worked for me.

---

### 评论 #2 — nufsty2 (2020-07-24T20:30:36Z)

Changed /etc/apt/sources.list.d/rocm.list from
`deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main`
to
`deb [arch=amd64] http://repo.radeon.com/rocm/apt/3.5.1/ xenial main`

That did the trick! Thanks!

---
